---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09516v1"
published: "2026-08-10T12:15:59Z"
age_days: 1
score: 25
created: 2026-08-12
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# HarnessWAM: Bridging Prediction and Deliberation in World Action Models

> [!summary] 一句话结论（基于摘要）
> HarnessWAM achieves state-of-the-art full-task and subtask success rates of 59.6% and 69.9% on RoboMemArena, and an SR of 23.7% on RoboCerebra Ideal.

## 关键点

- **问题**：However, finite- horizon prediction and action generation are insufficient for complex embodied tasks that require global planning, cross-stage state maintenance, execution verification, and failure recovery.
- **创新点 / 方法**：To address this gap, we propose HarnessWAM, an agentic framework for WAMs.
- **证据**：HarnessWAM achieves state-of-the-art full-task and subtask success rates of 59.6% and 69.9% on RoboMemArena, and an SR of 23.7% on RoboCerebra Ideal.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/HarnessWAM Bridging Prediction and Deliberation in World Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) jointly learn environmental dynamics and robot actions,
introducing priors over physical evolution into embodied control. However, finite-
horizon prediction and action generation are insufficient for complex embodied tasks
that require global planning, cross-stage state maintenance, execution verification, and
failure recovery. We refer to this mismatch as the prediction-deliberation gap of WAMs.
To address this gap, we propose HarnessWAM, an agentic framework for WAMs. HarnessWAM
employs a vision-language-model-based Task Manager to maintain an evidence-grounded
scene belief and a structured task graph. A capability-conditioned executable-space
projection further constrains open-ended semantic plans into sequences of atomic skills
that satisfy task dependencies, embodiment-state constraints, and the capability
boundary of the underlying WAM. During execution, HarnessWAM operates through an event-
driven, dual-timescale feedback loop: a lightweight progress estimator continuously
provides high-frequency execution evidence, while the Task Manager deliberates at
salient milestones by jointly considering the current observation, task state, and
interaction history to determine whether to advance the task, acquire additional
observations, revise the plan, or initiate local recovery. This mechanism enables the
robot to recover its state after a subtask failure and resume execution without
discarding previously acquired scene knowledge. HarnessWAM achieves state-of-the-art
full-task and subtask success rates of 59.6% and 69.9% on RoboMemArena, and an SR of
23.7% on RoboCerebra Ideal. These results demonstrate that model-external structured
state maintenance and closed-loop agentic decision making can effectively extend the
local control capabilities of WAMs into embodied task execution that is plannable,
verifiable, and recoverable.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09516v1
- Authors: Zhaopeng Gu, Bingke Zhu, Tianxi Lin, Guibo Zhu, Yingying Chen, Kai Wang, Tingyu Yuan, Chaoyang Zhao, Zhaowen Li, Peng Su, Jinqiao Wang
- Published: 2026-08-10T12:15:59Z
- Age days: 1

</details>
