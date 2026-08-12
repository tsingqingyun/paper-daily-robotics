---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05586v1"
published: "2026-08-06T04:17:13Z"
age_days: 4
score: 25
created: 2026-08-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# PathCover: A Fast Convex Decomposition along a Path via Randomized Iterative Space Partitioning (RISP) on Point Clouds

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Autonomous robot navigation requires the rapid generation of obstacle-free regions for
trajectory planning. However, existing corridor generators struggle to meet real-time,
sensor-rate computational constraints. To resolve this bottleneck, we introduce
PathCover, a framework driven by RISP; a novel randomized algorithm that constructs
convex polytopes directly from raw point cloud data in expected linear time under a mild
probabilistic elimination condition. PathCover generates sequences of overlapping,
obstacle-free polytopes that safely constrain downstream MPC and trajectory
optimization. We mathematically guarantee that the algorithm terminates in finite steps
while ensuring continuous progress along any obstacle-free reference path. Extensive
benchmarks on synthetic and real-world LiDAR datasets demonstrate an order-of-magnitude
speedup over state-of-the-art methods while maintaining comparable corridor volumes. The
complete pipeline is validated via high-fidelity quadrotor simulations and physical
deployment on a quadrupedal robot navigating constrained environments using live LiDAR
perception.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05586v1
- Authors: Kunal S. Narkhede, Abhijeet M. Kulkarni, Guoquan Huang, Ioannis Poulakakis
- Published: 2026-08-06T04:17:13Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
