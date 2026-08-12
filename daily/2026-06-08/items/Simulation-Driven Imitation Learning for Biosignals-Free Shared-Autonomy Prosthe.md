---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07389v1"
published: "2026-06-05T15:26:26Z"
age_days: 2
score: 30
created: 2026-06-08
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthetic Grasping

## 为什么重要

自动筛选分数：30

连接概念：[[世界模型]], [[机器人学习]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Biosignals-free shared-autonomy control of upper-limb prosthetic hands aims to enable
natural and low-effort manipulation without relying on EMG or other physiological
signals. Recent imitation-learning-based approaches have shown promising results, but
their scalability is limited by the cost and variability of collecting large amounts of
real-world human demonstration data. In this work, we present a scalable simulation
framework that automatically generates diverse reach-to-grasp demonstrations from a
wrist-mounted virtual camera. The framework combines physically feasible grasp
synthesis, natural reaching trajectories retargeting, and reach--grasp--lift execution
in procedurally generated indoor environments. It records wrist-view observations,
proprioception, and actions to build a large-scale demonstration dataset for imitation
learning. Through extensive simulation benchmarks, we evaluate object and scene
generalization and compare several representative state-of-the-art imitation learning
methods. Results show that the simulated demonstrations are sufficiently rich and
consistent for effective policy learning. In three realistic settings, the learned sim-
to-real policy achieves over 90\% grasp success, surpasses baseline methods, and
exhibits stronger generalization, highlighting the promise of simulation-driven training
for biosignals-free shared-autonomy prosthetic grasping. The demonstrations are
available at \href{https://sites.google.com/view/sim-prosthetic-
grasp/home}{https://sites.google.com/view/sim-prosthetic-grasp/home}.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07389v1
- Authors: Kaijie Shi, Wanglong Lu, Huiling Chen, Vinicius Prado da Fonseca, Ting Zou, Hanli Zhao, Xianta Jiang
- Published: 2026-06-05T15:26:26Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
