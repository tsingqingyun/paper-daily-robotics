---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12334v1"
published: "2026-06-10T17:05:50Z"
age_days: 1
score: 37
created: 2026-06-12
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Fourier Features Let Agents Learn High Precision Policies with Imitation Learning

## 为什么重要

自动筛选分数：37

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

High-precision robotic manipulation requires fine-grained spatial reasoning that is
often difficult to achieve with RGB-only policies due to depth ambiguity and perspective
scale issues. Policies that leverage 3D information directly, such as those based on
point clouds, offer a stronger geometric prior over purely image-based ones, yet their
performance remains highly task-dependent. We hypothesize that this discrepancy may be
due to the spectral bias of neural networks towards learning low frequency functions,
which especially affects architectures conditioned on slow-moving Cartesian features. We
thus propose to map point clouds from Cartesian space into high-dimensional Fourier
space, effectively equipping the point cloud encoder with direct access to high-
frequency features. We experimentally validate the use of Fourier features on
challenging manipulation tasks from the RoboCasa and ManiSkill3 benchmarks and on a real
robot setup. Despite their simplicity, we find that Fourier features provide significant
benefits across diverse encoder architectures and benchmarks and are robust across
hyperparameters. Our results indicate that Fourier features let policies leverage
geometric details more effectively than Cartesian features, showing their potential as a
general-purpose tool for point cloud-based imitation learning. We provide source code
and videos on our project page: https://fourier-il.github.io/fourier-il

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12334v1
- Authors: Balázs Gyenes, Emiliyan Gospodinov, Jan Frieling, Enrico Krohmer, Nicolas Schreiber, Xiaogang Jia, Niklas Freymuth, Gerhard Neumann
- Published: 2026-06-10T17:05:50Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
