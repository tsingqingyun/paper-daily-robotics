---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06721v1"
published: "2026-06-04T21:13:33Z"
age_days: 3
score: 28
created: 2026-06-08
concepts: ["智能体 Agent"]
---

# SCOUT: Semantic scene COverage via Uncertainty-guided Traversal

> [!summary] 一句话结论（基于摘要）
> We present SCOUT, an online semantic exploration framework that closes this loop by coupling active traversal with probabilistic scene graph construction.

## 关键点

- **问题**：In this way, the robot revisits ambiguous objects when additional evidence matters and expands into unseen free space when the scene remains incomplete.
- **创新点 / 方法**：We present SCOUT, an online semantic exploration framework that closes this loop by coupling active traversal with probabilistic scene graph construction.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots that operate over extended periods should not merely visit space; they should
progressively understand it. Yet most 3D scene graph pipelines treat perception as a
post-processing stage over a fixed dataset, decoupling scene representation from the
decisions that determine what is observed in the first place. We present SCOUT, an
online semantic exploration framework that closes this loop by coupling active traversal
with probabilistic scene graph construction. Given a prior 2D occupancy map and posed
RGB-D observations, SCOUT incrementally builds an uncertainty-aware 3D scene graph whose
nodes maintain fused geometry and posterior beliefs over open-vocabulary object labels,
while edges encode structural relations such as on, inside, belong, and next to. These
beliefs are fed back to an uncertainty-guided traversal planner, which selects
viewpoints by balancing expected semantic certainty gain, geometric coverage gain, and
travel cost. In this way, the robot revisits ambiguous objects when additional evidence
matters and expands into unseen free space when the scene remains incomplete. The
resulting system treats semantic scene completeness as an operational objective rather
than a passive by-product of semantic mapping, moving toward autonomous agents that can
patrol, update, and reason about evolving indoor environments with minimal human
intervention.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06721v1
- Authors: Junyu Mao, Sara Ayoubi, Vishnu D. Sharma, Ilija Hadžić, Matthew Andrews
- Published: 2026-06-04T21:13:33Z
- Age days: 3

</details>
