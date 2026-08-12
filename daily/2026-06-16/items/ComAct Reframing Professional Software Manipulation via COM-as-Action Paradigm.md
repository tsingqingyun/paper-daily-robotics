---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13239v1"
published: "2026-06-11T11:53:32Z"
age_days: 4
score: 22
created: 2026-06-16
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# ComAct: Reframing Professional Software Manipulation via COM-as-Action Paradigm

> [!summary] 一句话结论（基于摘要）
> Extensive experiments show that ComActorachieves state-of-the-art performance on ComCADBench, with strong resilience in long-horizon taskswhere baselines collapse, and generalizes to external CAD benchmark.

## 关键点

- **问题**：Existing computer-use agents remain fundamentally limited in professional software manipulation: GUI-based agents suffer from fragile visual grounding and long-horizon error accumulation, while API-basedapproaches struggle with heterogeneous protocols and inaccessible commercial interfaces.
- **创新点 / 方法**：Tobridge the remaining gap between syntactic correctness and geometric accuracy, we develop ComActor, aself-correcting agent trained through a progressive three-stage framework, alongside ComForge, a scalableplatform for large- scale training in Windows containers.
- **证据**：Extensive experiments show that ComActorachieves state-of-the-art performance on ComCADBench, with strong resilience in long-horizon taskswhere baselines collapse, and generalizes to external CAD benchmark.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-16/ComAct Reframing Professional Software Manipulation via COM-as-Action Paradigm.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Existing computer-use agents remain fundamentally limited in professional software
manipulation: GUI-based agents suffer from fragile visual grounding and long-horizon
error accumulation, while API-basedapproaches struggle with heterogeneous protocols and
inaccessible commercial interfaces. In this work,we identify the Component Object Model
(COM) as a unified executable abstraction, proposing COM-as-Action: a new paradigm that
reframes professional software interaction as deterministic program synthesisrather than
sequential visual control. To validate this paradigm in the most demanding environments,
weintroduce ComCADBench, the first benchmark for agents operating real industrial CAD
software. Ourexperiments reveal a substantial paradigm gap: frontier proprietary models
achieve near-zero successunder GUI-based interaction, whereas COM-based execution yields
substantial immediate gains. Tobridge the remaining gap between syntactic correctness
and geometric accuracy, we develop ComActor, aself-correcting agent trained through a
progressive three-stage framework, alongside ComForge, a scalableplatform for large-
scale training in Windows containers. Extensive experiments show that ComActorachieves
state-of-the-art performance on ComCADBench, with strong resilience in long-horizon
taskswhere baselines collapse, and generalizes to external CAD benchmark.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13239v1
- Authors: Jiaxin Ai, Tao Hu, Xuemeng Yang, Shu Zou, Hairong Zhang, Daocheng Fu, Yu Yang, Hongbin Zhou, Nianchen Deng, Pinlong Cai, Zhongyuan Wang, Botian Shi, Kaipeng Zhang, Licheng Wen
- Published: 2026-06-11T11:53:32Z
- Age days: 4

</details>
