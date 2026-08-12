---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19876v1"
published: "2026-07-22T08:04:17Z"
age_days: 1
score: 36
created: 2026-07-24
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Evaluating the physical consistency of embodied world models(EWMs) is a critical open
challenge. While closed-loop evaluation via simulator rollouts offers a more faithful
assessment of physical plausibility than open-loop alternatives, existing frameworks
almost exclusively rely on Inverse Dynamics Models(IDMs) for action extraction. Due to
the intricate mapping from 2D pixel space to 3D kinematic space, the learned IDMs can be
brittle to data outside their training distribution, resulting in unreliable action
extraction from the generated videos with novel objects and scenarios. This creates an
unavoidable attribution ambiguity between world model inaccuracies and extractor errors.
To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for
EWMs, built upon an explicit kinematic grounding pipeline. Given a generated video,
KineBench employs cascaded visual foundation models to directly extract 6D end-effector
poses from individual frames, which are then executed in a physics simulator for closed-
loop validation. Beyond execution-based task success, KineBench incorporates two
classical 3D kinematic metrics--Spectral Arc Length (SPARC) and the Maruyama
Manipulability Index--to characterize trajectory smoothness and kinematic feasibility
from a robot-centric perspective. Built on 20 diverse manipulation tasks in ManiSkill3,
KineBench evaluates EWMs across four progressive suites: basic execution, task transfer,
visual out-of-distribution generalization, and complexity-conditioned scaling.
Evaluation across frontier models reveals task-complexity-bounded nonlinear scaling in
embodied video generation, providing empirical guidance for future data-scaling
strategies.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19876v1
- Authors: Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai, Xuelong Li
- Published: 2026-07-22T08:04:17Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
