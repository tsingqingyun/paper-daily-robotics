---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18062v1"
published: "2026-07-20T15:30:16Z"
age_days: 1
score: 28
created: 2026-07-22
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# UniETP: Unifying Environments for Generalizable Embodied Task Planning

> [!summary] 一句话结论（基于摘要）
> As an effort towards generalizable embodied planning, we propose UniETP, a unified interface integrating four commonly-used simulators (AI2-THOR, VirtualHome, Habitat, BEHAVIOR).

## 关键点

- **问题**：This paper focuses on the problem of Embodied Task Planning, where an agent is required to execute a sequence of atomic actions within an interactive environment to complete a user-specified task.
- **创新点 / 方法**：As an effort towards generalizable embodied planning, we propose UniETP, a unified interface integrating four commonly-used simulators (AI2-THOR, VirtualHome, Habitat, BEHAVIOR).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This paper focuses on the problem of Embodied Task Planning, where an agent is required
to execute a sequence of atomic actions within an interactive environment to complete a
user-specified task. Though a variety of simulators and datasets have previously been
built for this task, these efforts are largely isolated, with each using its own
observation format, action type, and task domain. This fragmentation complicates
comprehensive model evaluation and hinders the scalability of training data. As an
effort towards generalizable embodied planning, we propose UniETP, a unified interface
integrating four commonly-used simulators (AI2-THOR, VirtualHome, Habitat, BEHAVIOR).
UniETP is characterized by both standardization and diversity. On one hand, it
formalizes all the simulators into a consistent observation and action space, and builds
an evaluation system to support complicated task goal. On the other hand, it enhances
task diversity and complexity across dimensions like task logic, instance grounding, and
instruction understanding, constructing a new dataset with varied levels of difficulty
in an automatic manner. Extensive experiments on the proposed benchmark are conducted to
evaluate the embodied planning capabilities of recent models and analyze the performance
bottlenecks. Codes and data will be available at https://github.com/woyut/UniETP .

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18062v1
- Authors: Peiran Xu, Jiaqi Zheng, Ziyou Wang, Yadong Mu
- Published: 2026-07-20T15:30:16Z
- Age days: 1

</details>
