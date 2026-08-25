---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.21035"
published: "Mon, 24 Aug 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-08-25
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# TaPeR: Probabilistic Recovery of Sparse Task Precedence Graphs from a Handful of Demonstrations

> [!summary] 一句话结论（基于摘要）
> Finally, we demonstrate that the inferred graphs can be used to generate multiple valid robotic execution orders for the same task.

## 关键点

- **问题**：However, symbolic predicates require explicit grounding, which is difficult to obtain in realistic settings.
- **创新点 / 方法**：In this work, we present an approach for extracting task dependency structures from demonstrations using only simple kinematic graphs and distributions over relative object poses.
- **证据**：Finally, we demonstrate that the inferred graphs can be used to generate multiple valid robotic execution orders for the same task.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-25/TaPeR Probabilistic Recovery of Sparse Task Precedence Graphs from a Handful of.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.21035v1 Announce Type: new Abstract: Long-horizon manipulation tasks are often only partially ordered. For example, when assembling an electronic device, the battery and circuit board may be installed in either order, but both must be in place before the enclosure is closed. Recovering such dependencies enables robots to flexibly reorder subtasks while preserving task validity. Existing approaches typically infer task structure from human demonstrations using both temporal and symbolic supervision. However, symbolic predicates require explicit grounding, which is difficult to obtain in realistic settings. In this work, we present an approach for extracting task dependency structures from demonstrations using only simple kinematic graphs and distributions over relative object poses. From these representations, our method estimates pairwise task-step-dependency probabilities and uses them to initialize the edge weights of a precedence graph. We then introduce a filtering pipeline that converts this graph of probability estimates into the final task dependency graph. We evaluate our approach on an existing benchmark and on a new dataset comprising longer tasks with more complex dependencies. We find that our method recovers more accurate task structures from fewer demonstrations than the baselines. Finally, we demonstrate that the inferred graphs can be used to generate multiple valid robotic execution orders for the same task.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.21035
- Authors: Adrian R\"ofer, Karla Stepanova, Abhinav Valada
- Published: Mon, 24 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
