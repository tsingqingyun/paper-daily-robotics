---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12965v1"
published: "2026-06-11T06:49:39Z"
age_days: 2
score: 26
created: 2026-06-14
concepts: ["机器人学习", "具身智能评测与基准"]
---

# EmbodiSteer: Steering Embodiment-Agnostic Visuomotor Policies with Joint-Space Guidance for Zero-Shot Cross-Embodiment Deployment

## 为什么重要

自动筛选分数：26

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Scalable robot imitation learning relies on large-scale heterogeneous data from diverse
robots or body-free data, making Cartesian end-effector actions a key interface for
embodiment-agnostic policy learning. However, end-effector-only abstraction leaves
Cartesian policies unaware of the deployed robot body, making them brittle under robot-
specific constraints such as whole-body collision avoidance. To overcome this
limitation, we present EmbodiSteer, a training-free framework that steers embodiment-
agnostic visuomotor policies toward zero-shot, embodiment-aware deployment. EmbodiSteer
keeps policy learning in Cartesian space while efficiently lifting inference-time
diffusion sampling into the target robot's joint space via forward kinematics and
Jacobian-based updates. With whole-body collision-aware guidance over joint trajectories
after each denoising step, the arm can be steered away from collisions while preserving
learned end-effector behavior. Compared with Cartesian-only execution, EmbodiSteer
reduces collision rate by 46.1% and improves task success rate by 28.5% across 9
simulated robots, and further achieves 90.0% collision rate reduction and 36.7% success
rate increase on two physical robots in highly constrained scenarios. Our project page
is at https://frankwang67.github.io/EmbodiSteer-Page.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12965v1
- Authors: Shihefeng Wang, Kangchen Lv, Mingrui Yu, Xiang Li
- Published: 2026-06-11T06:49:39Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
