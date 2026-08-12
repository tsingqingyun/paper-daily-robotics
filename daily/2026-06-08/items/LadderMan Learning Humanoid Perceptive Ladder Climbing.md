---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.05873v1"
published: "2026-06-04T08:47:08Z"
age_days: 3
score: 36
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "Sim2Real"]
---

# LadderMan: Learning Humanoid Perceptive Ladder Climbing

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[Sim2Real]]

## 摘要

Humanoid robots hold great promise for operating in human-centered environments, yet
ladder climbing remains one of the most challenging tasks due to sparse footholds and
handholds, complex whole-body coordination, and sensitivity to perception and control
errors. We present \textbf{LadderMan}, a unified system that enables humanoid robots to
robustly climb diverse ladders and perform manipulation under such constrained
conditions. Our climbing policy is built on a scalable two-stage learning pipeline,
where we use hybrid motion tracking to learn multiple climbing experts from a single
reference motion, and distill these experts into a unified depth-based visuomotor
climbing policy via hybrid imitation and reinforcement learning. To enable real-world
deployment, we leverage vision foundation models to bridge the sim-to-real gap in depth
perception. Building on the learned climbing policy, we further train a separate
manipulation policy using a dual-agent formulation, allowing stable on-ladder
manipulation via teleoperation. Experiments demonstrate that LadderMan achieves robust
ladder climbing across a wide range of geometries, successfully transfers to real-world
hardware in a zero-shot manner, and supports various manipulation tasks under
challenging ladder constraints. Video results are available at https://ladderman-
robot.github.io .

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.05873v1
- Authors: Siheng Zhao, Yuanhang Zhang, Ziqi Lu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Yue Wang, C. Karen Liu, Guanya Shi
- Published: 2026-06-04T08:47:08Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
