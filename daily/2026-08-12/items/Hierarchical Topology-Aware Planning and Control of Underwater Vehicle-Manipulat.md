---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08871v1"
published: "2026-08-09T19:22:51Z"
age_days: 2
score: 24
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# Hierarchical Topology-Aware Planning and Control of Underwater Vehicle-Manipulator Systems in Confined Environments

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

This paper addresses autonomous intervention with an underwater vehicle--manipulator
system (UVMS) in confined, cluttered, and partially known environments, where poor
maneuverability, narrow passages, and uncertain execution may cause the robot to enter
unrecoverable regions. We propose MANTA, a three-layer hierarchical planning-and-control
framework that couples passage accessibility, manipulation feasibility, and closed-loop
execution. The first layer performs global connectivity reasoning in a conservative
reduced base space to extract traversable corridor candidates toward the task region.
The second layer refines each candidate corridor by jointly optimizing the continuous
base motion and arm trajectory, producing a collision-free base--arm trajectory. The
third layer learns a reach-and-hold base policy using Gaussian-process model-based
reinforcement learning (MBRL) through MC-PILCO, enabling trajectory tracking and station
keeping at the planned manipulation state. During execution, the framework monitors map
updates and can trigger recovery and route repair when the active passage becomes
infeasible. MANTA is evaluated in confined UVMS planning and closed-loop tracking
experiments. Across 120 matched planning queries, it achieves higher task success than
full-state sampling-based baselines while producing larger clearance margins and lower
arm motion. The learned MC-PILCO policy further reduces position and yaw tracking errors
on both training and unseen tube-like references. These results show MANTA as a
structured and data-efficient framework for safe autonomous underwater intervention in
caves, tubes, and cluttered subsea structures.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08871v1
- Authors: Mohamed Abdelwahab, Ruggero Carli, Damiano Varagnolo, Alberto Dalla Libera
- Published: 2026-08-09T19:22:51Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
