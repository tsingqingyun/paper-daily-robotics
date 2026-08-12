---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19122v1"
published: "2026-06-17T14:35:52Z"
age_days: 1
score: 30
created: 2026-06-19
concepts: ["具身智能评测与基准"]
---

# Monocular 3D Occupancy Perception for Robots on Sidewalks via Hybrid 2D-3D Learning

## 为什么重要

自动筛选分数：30

连接概念：[[具身智能评测与基准]]

## 摘要

Sidewalks in the real world are crowded, cluttered, and less structured than roads,
making 3D occupancy prediction a key ingredient for the safe navigation of mobile robots
such as delivery bots and electric wheelchairs. Existing occupancy learning pipelines
are largely designed for on-road autonomous driving and often train on large-scale
paired LiDAR-RGB datasets with dense 3D supervision and multiple camera inputs, which
are costly to collect and do not adequately capture sidewalk-specific characteristics.
We propose WalkOCC, a hybrid Ray-marching monocular 3D occupancy perception framework
for robots operating on sidewalks. WalkOCC explicitly couples geometric grounding from
LiDAR-RGB paired data with scalable learning from large-scale unpaired monocular images.
It bootstraps pseudo occupancy supervision from paired sequences and jointly learns
image-level representations on additional 2D-only data. It yields stable optimization
and improved generalization without requiring costly 3D occupancy annotations. Extensive
experiments demonstrate consistent gains in prediction accuracy, fine-grained
segmentation of subtle urban structures such as curbs and gutters, and robustness to
environmental and cross-embodiment shifts compared with self-supervised image-based
baselines. To facilitate evaluation and benchmarking, we also introduce Sidewalk3D, a
large-scale sidewalk perception dataset with LiDAR-camera paired sequences collected
across multiple locations and time periods, along with 3D semantic occupancy annotations
for evaluation. Code and data will be made available.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19122v1
- Authors: Yukai Ma, Joe Lin, Liu Liu, Honglin He, Lulu Ricketts, Brad Squicciarini, Yong Liu, Bolei Zhou
- Published: 2026-06-17T14:35:52Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
