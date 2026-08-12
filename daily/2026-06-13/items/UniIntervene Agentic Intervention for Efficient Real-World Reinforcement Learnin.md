---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12372v1"
published: "2026-06-10T17:38:24Z"
age_days: 2
score: 30
created: 2026-06-13
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# UniIntervene: Agentic Intervention for Efficient Real-World Reinforcement Learning

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Human-in-the-loop reinforcement learning (HiL-RL) has emerged as an effective paradigm
for real-world robotic manipulation, enabling online policy improvement with human
guidance. However, current HiL-RL frameworks remain intervention-intensive, relying on
frequent human corrections to redirect the policy out of unproductive exploration, which
incurs high labor cost and limits real-world scalability. To address this, we propose
UniIntervene, an agentic intervention model that detects unproductive exploration and
autonomously recovers the policy toward high-value states, taking over the bulk of
interventions from human operators. Specifically, UniIntervene first performs future-
conditioned action-value estimation, predicting the latent consequence of the current
action and evaluating its induced value, which provides a more stable progress signal.
Building on this, a temporal value-risk critic aggregates recent value dynamics and
triggers intervention when the estimated value exhibits sustained stagnation or
degradation. When intervention is required, UniIntervene retrieves a high-value recovery
target from a memory of past intervention episodes and produces executable corrective
actions through a goal-conditioned recovery policy. In this way, UniIntervene turns
intervention from passive human correction into a value-aware recovery process for
efficient real-world RL. Extensive experiments on diverse real-world manipulation tasks
demonstrate that UniIntervene improves the average success rate by 8.6% while reducing
human interventions by 57% relative to state-of-the-art HiL-RL baselines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12372v1
- Authors: Haoyuan Deng, Yitong Gao, Yudong Lin, Haichao Liu, Zhenyu Wu, Ziwei Wang
- Published: 2026-06-10T17:38:24Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
