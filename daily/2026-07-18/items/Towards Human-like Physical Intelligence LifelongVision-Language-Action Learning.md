---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14852v1"
published: "2026-07-16T11:22:06Z"
age_days: 1
score: 35
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Similar to the natural capabilities of humans to sequentially learn new tasks, robots
with Vision-Language-Action (VLA) models should possess lifelong learning ability to
learn a new task when deployed in open-world environments. However, most recently
proposed lifelong learning models aim to effectively learn the current task (plasticity)
or maintain high accuracy on previous tasks (stability), while the plasticity-stability
trade-off remains largely unsolved in robotic manipulation models. To address this
fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action
learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the
plasticity-stability trade-off with a dual-timescale adaptation mechanism while
achieving low-cost robotic deployment with a cache-efficient replay strategy. More
concretely, we propose a dual-timescale LoRA gating module to decompose VLA adaptation
into two lightweight pathways: a short-term adapter for plasticity and a long-term
adapter for stable consolidation. These pathways are integrated via a task-aware gate,
enabling explicit control of the plasticity-stability trade-off. In the skill replay
phase, a cache-efficient stochastic replay strategy is proposed to preserve more
balanced retention signals without full-trajectory storage. Finally, experiments show
that LifelongVLA outperforms existing baselines, demonstrating efficient skill
expansion, robust retention of learned manipulation behaviors, and reduced reliance on
retraining for real-world deployment on an xArm robot.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14852v1
- Authors: Yao He, Gan Sun, Wenqi Liang, Fazeng Li, Yang Cong
- Published: 2026-07-16T11:22:06Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
