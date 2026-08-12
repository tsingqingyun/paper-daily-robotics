---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19745v2"
published: "2026-07-22T04:44:26Z"
age_days: 2
score: 25
created: 2026-07-25
concepts: ["机器人学习"]
---

# EgoRecovery: Acquiring Failure Recovery Ability Through Human Recovery Demonstration

> [!summary] 一句话结论（基于摘要）
> In this work, we show that egocentric human data capturing failure recovery processes provides a scalable alternative.

## 关键点

- **问题**：Robust embodied robots should be able to recover from failures and retry tasks in order to operate reliably in unstructured and noisy real-world environments.
- **创新点 / 方法**：To address the embodiment gap between human and robot, we propose EgoRecovery, a co-training framework for learning recovery behavior, where human recovery demonstrations are aligned to a compact corrective-intent space shared with robot data, which captures the timing and magnitude of correction.
- **证据**：In this work, we show that egocentric human data capturing failure recovery processes provides a scalable alternative.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robust embodied robots should be able to recover from failures and retry tasks in order
to operate reliably in unstructured and noisy real-world environments. Achieving this
capability requires training policies on data that captures recovery behaviors. However,
collecting such data through robot teleoperation is difficult to scale, as it is time-
consuming to induce diverse failure states, perform corrective actions, and reset the
environment. This challenge is further exacerbated by the high diversity of failure
modes, which demands substantially more recovery data than success demonstrations. In
this work, we show that egocentric human data capturing failure recovery processes
provides a scalable alternative. By efficiently arranging task-level failure
configurations and recording short recovery segments, human operators can generate more
than 10x as much valid recovery data per hour compared to robot teleoperation under our
protocol. To address the embodiment gap between human and robot, we propose EgoRecovery,
a co-training framework for learning recovery behavior, where human recovery
demonstrations are aligned to a compact corrective-intent space shared with robot data,
which captures the timing and magnitude of correction. Only a small number of robot
recovery demonstrations are required to connect this intent to executable robot actions.
At deployment, a learned recovery gate predicts when correction is needed from robot
observations and activates the corrective intent only in recovery states. Experiments on
real-world recovery tasks show that EgoRecovery improves success from failure starts
over robot-only recovery, direct co-training with human recovery data, and direct
intent-transfer baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19745v2
- Authors: Zuhao Ge, Yuchen Zhou, Weitao Zhou, Minglei Li, Xinyu Li, Chao Wu, Hanwen Zhao, Haotian Wang, Zuxuan Wu, Xiaosong Jia, Yu-Gang Jiang
- Published: 2026-07-22T04:44:26Z
- Age days: 2

</details>
