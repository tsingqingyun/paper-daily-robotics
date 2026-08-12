#!/bin/zsh
set -u

PROJECT="${AI_DAILY_VAULT:-${0:A:h:h}}"
PYTHON="${AI_DAILY_PYTHON:-/usr/bin/python3}"
UPDATE_SCRIPT="$PROJECT/scripts/update_info_flow.py"
LINK_CHECK_SCRIPT="$PROJECT/scripts/check_vault_links.py"
PUBLISH_SCRIPT="$PROJECT/scripts/publish_ai_daily.py"
DEEP_READ_SCRIPT="$PROJECT/scripts/start_ai_deep_read.py"
DEEP_READ_GUIDE="$PROJECT/10_MOCs/AI 论文深读工作流.md"
DEEP_READ_TEMPLATE="$PROJECT/90_Templates/Paper Deep Read.md"
DEEP_READ_INDEX="$PROJECT/50_Papers/精读论文索引.md"
STATE_DIR="$PROJECT/state"
AUTOMATION_DIR="$PROJECT/automations/ai"
ENV_FILE="$AUTOMATION_DIR/env.zsh"
RUN_LOG="$STATE_DIR/ai-daily.run.log"
MEMORY="$AUTOMATION_DIR/memory.md"
DEFAULT_GITHUB_REMOTE=""

if ! mkdir -p "$STATE_DIR" "$AUTOMATION_DIR"; then
  /bin/echo "Cannot create AI daily state directories under $PROJECT" >&2
  exit 73
fi

timestamp() {
  /bin/date "+%Y-%m-%d %H:%M:%S %Z"
}

log() {
  /bin/echo "[$(timestamp)] $*"
}

check_dns() {
  "$PYTHON" - <<'PY'
import socket
import sys

hosts = [
    "export.arxiv.org",
    "openai.com",
    "deepmind.google",
    "huggingface.co",
]

failed = []
for host in hosts:
    try:
        socket.getaddrinfo(host, 443)
    except OSError as exc:
        failed.append(f"{host}: {exc}")

if failed:
    print("DNS preflight failed:")
    for failure in failed:
        print(f"- {failure}")
    sys.exit(1)

print("DNS preflight ok")
PY
}

load_environment() {
  if [ -f "$ENV_FILE" ]; then
    # shellcheck disable=SC1090
    source "$ENV_FILE"
    log "Loaded environment from $ENV_FILE"
  else
    log "No automation environment file found at $ENV_FILE"
  fi

  if [ -n "${https_proxy:-}" ]; then
    log "HTTPS proxy configured: $https_proxy"
  else
    log "HTTPS proxy is not configured"
  fi
}

check_proxy() {
  "$PYTHON" - <<'PY'
import os
import socket
import sys
from urllib.parse import urlparse

proxy = os.environ.get("https_proxy") or os.environ.get("HTTPS_PROXY") or ""
if not proxy:
    print("Proxy preflight skipped: no https_proxy/HTTPS_PROXY")
    sys.exit(0)

parsed = urlparse(proxy)
host = parsed.hostname
port = parsed.port
if not host or not port:
    print(f"Proxy preflight failed: invalid proxy URL {proxy!r}")
    sys.exit(1)

try:
    with socket.create_connection((host, port), timeout=3):
        pass
except OSError as exc:
    print(f"Proxy preflight failed: cannot connect to {host}:{port}: {exc}")
    sys.exit(1)

print(f"Proxy preflight ok: {host}:{port}")
PY
}

run_update() {
  "$PYTHON" "$UPDATE_SCRIPT" --vault "$PROJECT" --timeout 60 --sleep 3 --fetch-retries 3 --retry-backoff 2
}

current_state_is_today() {
  "$PYTHON" - "$PROJECT" <<'PY'
import datetime as dt
import json
import sys
from pathlib import Path

project = Path(sys.argv[1])
today = dt.date.today().isoformat()
digest = (project / "30_Updates" / f"{today} AI Embodied Intelligence Update.md").resolve()
state_path = project / "state" / "seen.json"
try:
    state = json.loads(state_path.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError):
    raise SystemExit(1)
output = state.get("last_output_path")
fresh = (
    str(state.get("last_run", "")).startswith(today)
    and output
    and Path(output).expanduser().resolve() == digest
    and digest.is_file()
    and "format_version: 2" in digest.read_text(encoding="utf-8")
)
raise SystemExit(0 if fresh else 1)
PY
}

verify_current_run() {
  "$PYTHON" - "$PROJECT" "$1" <<'PY'
import datetime as dt
import json
import sys
from pathlib import Path

project = Path(sys.argv[1])
started_at = float(sys.argv[2])
today = dt.date.today().isoformat()
digest = (project / "30_Updates" / f"{today} AI Embodied Intelligence Update.md").resolve()
state_path = project / "state" / "seen.json"
try:
    state = json.loads(state_path.read_text(encoding="utf-8"))
    last_run = dt.datetime.fromisoformat(str(state.get("last_run", "")))
except (OSError, json.JSONDecodeError, ValueError) as exc:
    print(f"State verification failed: {exc}")
    raise SystemExit(65)
output = state.get("last_output_path")
if not digest.is_file():
    print(f"State verification failed: daily digest missing: {digest}")
    raise SystemExit(65)
if not output or Path(output).expanduser().resolve() != digest:
    print(f"State verification failed: last_output_path={output!r}, expected={str(digest)!r}")
    raise SystemExit(65)
if last_run.timestamp() + 2 < started_at:
    print(f"State verification failed: stale last_run={last_run.isoformat()}")
    raise SystemExit(65)
print(f"State verification ok: {digest}")
PY
}

verify_compact_format() {
  "$PYTHON" - "$PROJECT" <<'PY'
import datetime as dt
import re
import sys
from pathlib import Path

project = Path(sys.argv[1])
today = dt.date.today().isoformat()
digest = project / "30_Updates" / f"{today} AI Embodied Intelligence Update.md"
text = digest.read_text(encoding="utf-8")
required = [
    "format_version: 2",
    "> [!summary] 30 秒结论",
    "## 必读 ",
    "## 扫读 ",
    "## 其余存档 ",
    "[[AI 论文深读工作流|",
]
missing = [marker for marker in required if marker not in text]
if missing:
    print(f"Compact format verification failed for {digest}: missing {missing}")
    raise SystemExit(65)

reference_re = re.compile(rf"\[\[(30_Updates/{today}/[^|\]\n]+)(?:\|[^\]\n]+)?\]\]")
references = sorted(set(reference_re.findall(text)))
if not references:
    print(f"Compact format verification failed: no referenced paper notes in {digest}")
    raise SystemExit(65)
for target in references:
    note = project / f"{target.removesuffix('.md')}.md"
    note_text = note.read_text(encoding="utf-8")
    if (
        "format_version: 2" not in note_text
        or "## 关键点" not in note_text
        or "[[AI 论文深读工作流|" not in note_text
    ):
        print(f"Compact format verification failed for referenced note: {note}")
        raise SystemExit(65)
print(f"Compact format verification ok: format v2, {len(references)} referenced notes")
PY
}

run_link_check() {
  "$PYTHON" "$LINK_CHECK_SCRIPT" --vault "$PROJECT"
}

run_publish() {
  "$PYTHON" "$PUBLISH_SCRIPT" \
    --vault "$PROJECT" \
    --remote "$AI_DAILY_GITHUB_REMOTE" \
    --branch "$AI_DAILY_GITHUB_BRANCH" \
    --push-retries 3 \
    --push-backoff 10
}

{
  log "Starting AI embodied intelligence daily update"
  log "Project: $PROJECT"

  cd "$PROJECT" || {
    log "Cannot cd into project"
    exit 1
  }

  load_environment

  AI_DAILY_GITHUB_REMOTE="${AI_DAILY_GITHUB_REMOTE:-$DEFAULT_GITHUB_REMOTE}"
  AI_DAILY_GITHUB_BRANCH="${AI_DAILY_GITHUB_BRANCH:-main}"

  if [ -z "$AI_DAILY_GITHUB_REMOTE" ]; then
    log "AI_DAILY_GITHUB_REMOTE is not configured"
    exit 78
  fi

  for required in "$UPDATE_SCRIPT" "$LINK_CHECK_SCRIPT" "$PUBLISH_SCRIPT" "$DEEP_READ_SCRIPT" "$DEEP_READ_GUIDE" "$DEEP_READ_TEMPLATE" "$DEEP_READ_INDEX"; do
    if [ ! -f "$required" ]; then
      log "Required script missing: $required"
      exit 78
    fi
  done

  today=$(/bin/date "+%Y-%m-%d")
  daily_note="$PROJECT/30_Updates/$today AI Embodied Intelligence Update.md"
  run_started_epoch=$(/bin/date "+%s")
  exit_code=0

  if current_state_is_today; then
    log "Today's verified state already exists; skipping duplicate fetch and resuming verification/publication"
    run_started_epoch=0
  else
    proxy_status=0
    check_proxy || proxy_status=$?
    if [ "$proxy_status" -ne 0 ]; then
      log "Proxy preflight failed; feed-level retries will test whether direct access recovers"
    fi

    dns_status=0
    check_dns || dns_status=$?
    if [ "$dns_status" -ne 0 ]; then
      log "DNS preflight failed; feed-level and whole-run retries will attempt recovery"
    fi

    attempt=1
    exit_code=75
    while [ "$attempt" -le 3 ]; do
      log "Update attempt $attempt/3"
      run_update
      exit_code=$?
      if [ "$exit_code" -eq 0 ]; then
        break
      fi
      log "Attempt $attempt failed with exit code $exit_code"
      case "$exit_code" in
        69|73|78)
          log "Exit code $exit_code is not retryable; stopping update retries"
          break
          ;;
        75)
          if [ "$attempt" -lt 3 ]; then
            if [ "$attempt" -eq 1 ]; then retry_delay=30; else retry_delay=120; fi
            log "Temporary failure; retrying whole update in ${retry_delay}s"
            /bin/sleep "$retry_delay"
          fi
          ;;
        *)
          if [ "$attempt" -lt 3 ]; then
            log "Unexpected failure; retrying once after 30s"
            /bin/sleep 30
          fi
          ;;
      esac
      attempt=$((attempt + 1))
    done
  fi

  if [ "$exit_code" -eq 0 ]; then
    verify_current_run "$run_started_epoch"
    exit_code=$?
  fi

  if [ "$exit_code" -eq 0 ]; then
    verify_compact_format
    exit_code=$?
  fi

  if [ "$exit_code" -eq 0 ]; then
    log "Running vault link gate"
    run_link_check
    exit_code=$?
    if [ "$exit_code" -ne 0 ]; then
      log "Link gate failed; GitHub publication is blocked"
      exit_code=65
    fi
  fi

  publish_code=0
  if [ "$exit_code" -eq 0 ]; then
    publish_attempt=1
    publish_code=75
    while [ "$publish_attempt" -le 3 ]; do
      log "GitHub publication attempt $publish_attempt/3"
      run_publish
      publish_code=$?
      if [ "$publish_code" -eq 0 ]; then
        break
      fi
      log "Publication attempt $publish_attempt failed with exit code $publish_code"
      if [ "$publish_code" -eq 78 ] || [ "$publish_attempt" -ge 3 ]; then
        break
      fi
      if [ "$publish_attempt" -eq 1 ]; then publish_delay=30; else publish_delay=120; fi
      log "Retrying publication in ${publish_delay}s"
      /bin/sleep "$publish_delay"
      publish_attempt=$((publish_attempt + 1))
    done
  fi

  final_code="$exit_code"
  if [ "$final_code" -eq 0 ] && [ "$publish_code" -ne 0 ]; then
    final_code="$publish_code"
  fi

  if [ -f "$daily_note" ]; then
    log "Daily note present: $daily_note"
  else
    log "Daily note missing for $today"
  fi

  "$PYTHON" - "$PROJECT" "$final_code" "$daily_note" "$run_started_epoch" "$publish_code" >> "$MEMORY" <<'PY'
import datetime as dt
import json
import sys
from pathlib import Path

project = Path(sys.argv[1])
exit_code = sys.argv[2]
daily_note = sys.argv[3]
started_at = float(sys.argv[4])
publish_code = sys.argv[5]
state_path = project / "state" / "seen.json"
state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
now = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
try:
    last_run = dt.datetime.fromisoformat(str(state.get("last_run", "")))
    fresh = (
        last_run.timestamp() + 2 >= started_at
        and Path(daily_note).is_file()
        and state.get("last_output_path")
        and Path(state["last_output_path"]).expanduser().resolve() == Path(daily_note).resolve()
    )
except (ValueError, OSError):
    fresh = False

if fresh:
    failures = state.get("last_failures", [])
    concept_counts = state.get("last_concept_counts", {})
    concept_summary = "、".join(f"{name} {count}" for name, count in concept_counts.items()) or "无"
    metrics = (
        f"Candidates: {state.get('last_candidate_count', 0)}. "
        f"Selected: {state.get('last_selected_count', 0)}. "
        f"Top: {state.get('last_top_title') or '无'}. "
        f"Concepts: {concept_summary}. Feed failures: {len(failures)}."
    )
else:
    metrics = "Current-run metrics unavailable; previous seen state was preserved."

print()
print(
    f"{now}: launchd wrapper ran project-local AI update. "
    f"Exit code: {exit_code}. Publish code: {publish_code}. {metrics} Daily note: {daily_note}."
)
PY

  log "Finished AI embodied intelligence daily update with exit code $final_code"
  exit "$final_code"
} >> "$RUN_LOG" 2>&1
