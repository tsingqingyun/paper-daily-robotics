---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19469v1"
published: "2026-05-19T07:21:53Z"
age_days: 0
score: 30
created: 2026-05-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Sampling-Based Safe Reinforcement Learning

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Safe exploration remains a fundamental challenge in reinforcement learning (RL),
limiting the deployment of RL agents in the real world. We propose Sampling-Based Safe
Reinforcement Learning (SBSRL), a model-based RL algorithm that maintains safety
throughout the learning process by enforcing constraints jointly across a finite set of
dynamics samples. This formulation approximates an intractable worst-case optimization
over uncertain dynamics and enables practical safety guarantees in continuous domains.
We further introduce an exploration strategy based on constraining epistemic
uncertainty, eliminating the need for explicit exploration bonuses. Under regularity
conditions, we derive high-probability guarantees of safety throughout learning and a
finite-time sample complexity bound for recovering a near-optimal policy. Empirically,
SBSRL achieves safe and efficient exploration both in simulation and in real robotic
hardware, and readily extends to practical deep-ensemble implementations that scale to
high-dimensional continuous control problems.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19469v1
- Authors: Luca Vignola, Bruce D. Lee, Manish Prajapat, Manuel Wendl, Melanie Zeilinger, Andreas Krause, Yarden As
- Published: 2026-05-19T07:21:53Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
