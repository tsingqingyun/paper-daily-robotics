"""Collect bounded official arXiv HTML excerpts; never claim a complete reading."""
from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote


CONTEXT_VERSION = 3


class ArticleText(HTMLParser):
    """Keep DOM blocks intact; source-code line breaks are only whitespace."""

    BLOCKS = {"p", "h1", "h2", "h3", "h4", "table", "tr", "figcaption", "li"}
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__()
        self.in_article = False
        self.stack = []
        self.skip = None
        self.math = None
        self.block = None
        self.heading = "正文"
        self.paragraphs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in self.VOID:
            self.stack.append((tag, attrs))
        if tag == "article":
            self.in_article = True
        if not self.in_article or self.skip is not None:
            return
        hidden = ("ltx_phantom" in attrs.get("class", "").split()
                  or "hidden" in attrs or attrs.get("aria-hidden") == "true"
                  or re.search(r"(?:visibility\s*:\s*hidden|display\s*:\s*none)", attrs.get("style", ""), re.I))
        if tag not in self.VOID and (tag in {"script", "style", "nav", "annotation", "annotation-xml"} or hidden):
            self.skip = len(self.stack)
            return
        if self.math is not None:
            return
        if tag == "math":
            self.math = {"depth": len(self.stack), "alttext": attrs.get("alttext", ""), "parts": []}
            return
        if tag in self.BLOCKS and self.block is None:
            anchor = next((a["id"] for _, a in reversed(self.stack) if a.get("id")), "")
            bibliography = any("ltx_bibliography" in a.get("class", "").split() for _, a in self.stack)
            self.block = {"depth": len(self.stack), "tag": tag, "anchor": anchor,
                          "parts": [], "bibliography": bibliography}
        elif self.block is not None and tag in self.BLOCKS | {"br", "td", "th"}:
            separator = " | " if tag in {"td", "th"} else " ; " if tag == "tr" else " "
            self.block["parts"].append(separator)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        depth = next((i + 1 for i in range(len(self.stack) - 1, -1, -1) if self.stack[i][0] == tag), None)
        if depth is None:
            return
        if self.skip == depth:
            self.skip = None
        if self.math is not None and self.math["depth"] == depth:
            value = self.math["alttext"] or "".join(self.math["parts"])
            if self.block is not None:
                self.block["parts"].append(" " + value + " ")
            self.math = None
        if self.block is not None and self.block["depth"] == depth:
            text = re.sub(r"\s+", " ", "".join(self.block["parts"])).strip(" ;|")
            if self.block["tag"] in {"h1", "h2", "h3", "h4"}:
                self.heading = text or self.heading
            elif text and not self.block["bibliography"]:
                self.paragraphs.append({"text": text, "anchor": self.block["anchor"],
                                        "heading": self.heading, "kind": self.block["tag"]})
            self.block = None
        self.stack = self.stack[:depth - 1]
        if tag == "article":
            self.in_article = False

    def handle_data(self, data):
        if not self.in_article or self.skip is not None:
            return
        if self.math is not None:
            if not self.math["alttext"]:
                self.math["parts"].append(data)
        elif self.block is not None:
            self.block["parts"].append(data)


def extract_sections(html: str, budget: int = 22000, source_url: str = "") -> list[dict]:
    parser = ArticleText()
    parser.feed(html)
    paragraphs = parser.paragraphs
    if sum(len(p["text"]) for p in paragraphs) < 2000:
        raise ValueError("Official HTML has insufficient article text")
    # Reserve room for later evidence and limitations, rather than filling the
    # entire budget from the introduction and early methods in source order.
    selected = set(range(min(4, len(paragraphs))))
    cues = re.compile(r"method|train|policy|baseline|success|experiment|limitation|ablation|demonstration|dataset|simulation|real.world", re.I)
    limitations = re.compile(r"limitation|limited to|unvalidated|future work|can struggle|currently only", re.I)
    limits = [i for i, p in enumerate(paragraphs) if i not in selected and limitations.search(p["text"])][:4]
    selected.update(limits)
    candidates = sorted(selected)
    groups = [[], [], []]
    for i, p in enumerate(paragraphs):
        if i in selected or not cues.search(p["heading"] + " " + p["text"]):
            continue
        if re.search(r"result|evaluation|experiment|ablation|real.world|conclusion", p["heading"], re.I):
            group = 0
        elif re.search(r"method|policy|learning|train|control|formulation|representation|architecture|scheduling|reconstruct|distill|generation", p["heading"], re.I):
            group = 1
        else:
            group = 2
        groups[group].append(i)
    for offset in range(max(map(len, groups), default=0)):
        candidates.extend(group[offset] for group in groups if offset < len(group))
    chosen = []
    used = 0
    for i in candidates:
        paragraph = paragraphs[i]
        if used + len(paragraph["text"]) > budget:
            continue
        chosen.append((i, paragraph))
        used += len(paragraph["text"])
    sections = []
    for j, (i, p) in enumerate(sorted(chosen), 1):
        fragment = quote(p["anchor"], safe="._:-") if p["anchor"] else ":~:text=" + quote(p["text"][:160], safe="")
        sections.append({"id": f"S{j}", "heading": f"{p['heading']} · 正文段落 {i + 1}",
                         "text": p["text"], "source_url": source_url + "#" + fragment})
    return sections


def enrich_papers(items: list[dict], vault: Path, limit: int = 5) -> None:
    cache = vault / "state" / "paper-reading-context"
    cache.mkdir(parents=True, exist_ok=True)
    for item in items[:limit]:
        match = re.fullmatch(r"https?://arxiv\.org/abs/(\d{4}\.\d{4,5}v\d+)", item.get("url", ""))
        if not match:
            item["source_context_error"] = "No supported versioned official arXiv HTML URL"
            continue
        ident = match.group(1)
        path = cache / f"{ident}.json"
        try:
            context = json.loads(path.read_text()) if path.is_file() else {}
            if context.get("context_version") != CONTEXT_VERSION:
                url = f"https://arxiv.org/html/{ident}"
                request = urllib.request.Request(url, headers={"User-Agent": "AI-paper-reading/1.0"})
                with urllib.request.urlopen(request, timeout=35) as response:
                    raw = response.read(5_000_001)
                if len(raw) > 5_000_000:
                    raise ValueError("Official HTML exceeds 5 MB limit")
                context = {"context_version": CONTEXT_VERSION, "url": url,
                           "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                           "scope": "selected complete DOM blocks, not full paper",
                           "sections": extract_sections(raw.decode("utf-8"), source_url=url)}
                if path.is_file():
                    backup = path.with_suffix(".json.backup")
                    if backup.exists():
                        backup = path.with_suffix(f".json.{dt.datetime.now().strftime('%Y%m%d-%H%M%S-%f')}.backup")
                    shutil.copy2(path, backup)
                path.write_text(json.dumps(context, ensure_ascii=False, indent=2) + "\n")
            item["source_context"] = context
        except Exception as exc:
            item["source_context_error"] = f"{type(exc).__name__}: {exc}"
