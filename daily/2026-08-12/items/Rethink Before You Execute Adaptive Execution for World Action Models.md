---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09492v1"
published: "2026-08-10T11:59:42Z"
age_days: 1
score: 26
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Rethink Before You Execute: Adaptive Execution for World Action Models

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09492v1
- Authors: Feng Ye, Yiming Zhao, Yong Yu, Hongxu Zhou, Yong Pan, Yuan Xue, Peng Jia, Chuanmin Jia
- Published: 2026-08-10T11:59:42Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
