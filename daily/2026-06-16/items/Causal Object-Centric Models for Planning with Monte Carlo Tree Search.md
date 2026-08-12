---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14418v1"
published: "2026-06-12T12:55:25Z"
age_days: 3
score: 24
created: 2026-06-16
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Causal Object-Centric Models for Planning with Monte Carlo Tree Search

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

We introduce COMET (Causal Object-centric Model for Efficient Tree search), a model-
based reinforcement learning algorithm that performs Monte Carlo Tree Search in a slot-
structured latent space. COMET pairs a frozen unsupervised object-centric encoder with a
transformer-based world model, in which actions are bound to objects through a novel
action-slot fusion mechanism that is used in slot transition prediction. Policy and
value heads use object-causal attention, modulating token interactions by learned per-
slot relevance scores so that decision-making concentrates on task-relevant entities.
COMET adds an explicit object-level inductive bias to MuZero-style latent planning.
Across eight visually and dynamically diverse tasks from the Object-Centric Visual RL
benchmark, ManiSkill, Robosuite, and VizDoom, COMET achieves a higher mean normalized
score during the early stages of training compared to object-centric and monolithic
baselines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14418v1
- Authors: Rodion Vakhitov, Leonid Ugadiarov, Alexey Skrynnik, Aleksandr Panov
- Published: 2026-06-12T12:55:25Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
