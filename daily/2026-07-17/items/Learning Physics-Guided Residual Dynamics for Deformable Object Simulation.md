---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13451v1"
published: "2026-07-15T05:15:43Z"
age_days: 1
score: 29
created: 2026-07-17
concepts: ["智能体 Agent", "世界模型"]
---

# Learning Physics-Guided Residual Dynamics for Deformable Object Simulation

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Simulating deformable objects is essential for a wide range of robotic manipulation
applications, yet accurately predicting their dynamics remains challenging. We propose
Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the
advantages of physics-based and learning-based approaches. Specifically, PGRD combines
an optimizable spring-mass simulator as a backbone with a learned neural network that
predicts residual corrections to the physics-based predictions. We adopt a velocity-
based formulation to ensure stable simulation and a sliding-window transformer
architecture to capture temporal dependencies. We show that PGRD produces more accurate
results than both purely physics-based and learning-based methods on a set of diverse
real-world deformable objects. We further demonstrate the utility of PGRD in two
applications: manipulation planning via Model Predictive Control, including a language-
conditioned setting with a generated goal image; and interactive simulation via action-
conditioned video prediction by 3D Gaussian Splatting.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13451v1
- Authors: Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li
- Published: 2026-07-15T05:15:43Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
