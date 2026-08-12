---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19745v2"
published: "2026-07-22T04:44:26Z"
age_days: 2
score: 25
created: 2026-07-25
concepts: ["机器人学习"]
---

# EgoRecovery: Acquiring Failure Recovery Ability Through Human Recovery Demonstration

## 为什么重要

自动筛选分数：25

连接概念：[[机器人学习]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19745v2
- Authors: Zuhao Ge, Yuchen Zhou, Weitao Zhou, Minglei Li, Xinyu Li, Chao Wu, Hanwen Zhao, Haotian Wang, Zuxuan Wu, Xiaosong Jia, Yu-Gang Jiang
- Published: 2026-07-22T04:44:26Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
