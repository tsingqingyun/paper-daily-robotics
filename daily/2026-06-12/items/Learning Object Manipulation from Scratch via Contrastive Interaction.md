---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11525v1"
published: "2026-06-10T00:06:24Z"
age_days: 2
score: 34
created: 2026-06-12
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real"]
---

# Learning Object Manipulation from Scratch via Contrastive Interaction

## 为什么重要

自动筛选分数：34

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[Sim2Real]]

## 摘要

Contrastive Reinforcement Learning (CRL) has seen recent success in a wide variety of
goal-conditioned robotics tasks by learning structured representations of the dynamics.
However, despite its success in locomotion and simpler control domains, CRL often
struggles in interaction-rich manipulation. We argue that a key source of this
difficulty is object-centric interaction, such as contact or grasping, that induces
distinct changes in the underlying dynamic modes. In this work, we formulate
manipulation dynamics as a piecewise-smooth Markov process and show that interaction-
induced mode changes create piecewise nonlinear reachability structures that are
difficult for standard CRL energy functions to represent and plan over. Based on this
analysis, we introduce Interaction-weighted Resampling (IWR). IWR performs interaction-
aware resampling around phases before, during, and after interactions, encouraging the
learned representation to preserve the mode boundaries that determine future
reachability to capture multi-modal and piecewise nonlinear reachability. Across
interaction-centric environments, including 2D dynamic control, robotic manipulation,
and robot air hockey, IWR improves both sample efficiency and overall performance over
prior CRL methods, with 19.8% average improvement in simulation. Finally, using a sim-
to-real pipeline with policies trained by IWR, we demonstrate the first real-world goal-
conditioned robot air hockey agent capable of hitting goals, improving success from 25%
to 60%. Project Page: IWR-arxiv.github.io.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11525v1
- Authors: Tongle Shen, Caleb Chuck, Fan Feng, Biwei Huang
- Published: 2026-06-10T00:06:24Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
