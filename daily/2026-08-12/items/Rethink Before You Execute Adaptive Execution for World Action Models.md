---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09492v1"
published: "2026-08-10T11:59:42Z"
age_days: 1
score: 26
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Rethink Before You Execute: Adaptive Execution for World Action Models

> [!summary] 一句话结论（基于摘要）
> On real robots, it reduces WAM inferences by 26.9% on easy tasks while maintaining success, and improves success by 13.3 points on difficult tasks.

## 关键点

- **问题**：A Recurrent Progress Monitor first estimates task progress from the current observation, task instruction, remaining actions, and execution history; and an Adaptive Execution Protocol then evaluates whether the chunk is advancing the task to decide if replanning is needed.
- **创新点 / 方法**：We propose TempoWAM (Timing Execution by Monitoring Progress Online), a lightweight plug-and-play execution scheme for WAMs.
- **证据**：On real robots, it reduces WAM inferences by 26.9% on easy tasks while maintaining success, and improves success by 13.3 points on difficult tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/Rethink Before You Execute Adaptive Execution for World Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) jointly predict future actions and the evolution of the
environment. At each inference, a WAM generates a chunk of actions and the robot
executes a fixed prefix before replanning. We argue that this fixed execution horizon is
poorly matched to execution dynamics: the chunk reliability varies across task stages,
so when to replan depends on the result of accumulated execution, not on the step
counts. We propose TempoWAM (Timing Execution by Monitoring Progress Online), a
lightweight plug-and-play execution scheme for WAMs. A Recurrent Progress Monitor first
estimates task progress from the current observation, task instruction, remaining
actions, and execution history; and an Adaptive Execution Protocol then evaluates
whether the chunk is advancing the task to decide if replanning is needed. To bridge the
training-deployment gap, the protocol is calibrated by a task-dependent calibration
factor with online adaptation. Experiments on LIBERO, RoboTwin, and real-world tasks
show that TempoWAM consistently improves the efficiency-success trade-off of WAM
execution. On real robots, it reduces WAM inferences by 26.9% on easy tasks while
maintaining success, and improves success by 13.3 points on difficult tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09492v1
- Authors: Feng Ye, Yiming Zhao, Yong Yu, Hongxu Zhou, Yong Pan, Yuan Xue, Peng Jia, Chuanmin Jia
- Published: 2026-08-10T11:59:42Z
- Age days: 1

</details>
