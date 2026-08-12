---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19038v1"
published: "2026-07-21T12:28:58Z"
age_days: 3
score: 24
created: 2026-07-25
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling

> [!summary] 一句话结论（基于摘要）
> Experiments demonstrate that FilmWorld consistently outperforms state-of-the-art video generation agent systems, with particularly pronounced improvements in narrative fidelity and cross-scene consistency.

## 关键点

- **问题**：Translating novels into films poses a grand challenge for generative artificial intelligence, requiring conversion of abstract literary prose into long-form, multi- scene visual narratives.
- **创新点 / 方法**：We propose FilmWorld, an end-to-end agentic system where two groups of specialized agents collaborate to instantiate these phases.
- **证据**：Experiments demonstrate that FilmWorld consistently outperforms state-of-the-art video generation agent systems, with particularly pronounced improvements in narrative fidelity and cross-scene consistency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Translating novels into films poses a grand challenge for generative artificial
intelligence, requiring conversion of abstract literary prose into long-form, multi-
scene visual narratives. While current video generation models excel at short, single-
scene clips within narrow temporal and spatial contexts, novel-to-film generation
operates in a more complex regime, demanding long-duration content across diverse scenes
with dynamically evolving entity states. To address this, we formalize novel-to-film
generation as dynamic cinematic world modeling, decomposed into two phases:
construction, which grounds abstract, underspecified literary narratives into concrete,
stateful, and persistent world entities; and evolution, which governs how these entities
dynamically update under plot progression to maintain causal consistency across scenes.
We propose FilmWorld, an end-to-end agentic system where two groups of specialized
agents collaborate to instantiate these phases. Construction-side agents perform
narrative structured translation, world entity state modeling with visual anchoring, and
state-driven shot planning, progressively projecting literary language into a cinematic
blueprint. Evolution-side agents perform state-anchored visual generation, cross-shot
dynamic state propagation, and closed-loop state verification to maintain causal
consistency and visual coherence. To address the evaluation gap in long-form generation,
we introduce FilmEval, a systematic evaluation framework that couples a difficulty-
graded benchmark of 15 representative novels with an automated protocol of nine
objective metrics spanning three dimensions: cinematic presentation, film consistency,
and novel fidelity. Experiments demonstrate that FilmWorld consistently outperforms
state-of-the-art video generation agent systems, with particularly pronounced
improvements in narrative fidelity and cross-scene consistency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19038v1
- Authors: Jialong Zuo, Haotong Zuo, Shiwei Zhang, Xiang Wang, Chen Li, Nong Sang, Changxin Gao, Xiang Bai
- Published: 2026-07-21T12:28:58Z
- Age days: 3

</details>
