---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13586v1"
published: "2026-07-15T08:27:07Z"
age_days: 1
score: 29
created: 2026-07-17
concepts: ["世界模型", "具身智能评测与基准"]
---

# UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets

## 为什么重要

自动筛选分数：29

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

Physically grounded 3D assets are increasingly important for embodied AI and robotic
simulation. However, most existing 3D assets lack unified physical semantics, including
articulation semantics and intrinsic physical properties, required for realistic
interaction. Current approaches either treat these semantics independently or rely on
canonicalized object structures, limiting robustness across heterogeneous 3D assets. We
present UniPhys, a scalable framework for automatically transforming raw 3D assets into
simulation-ready assets with unified physical semantics. Based on UniPhys, we construct
UniPhys-40K, a large-scale physically grounded dataset, together with UniPhys-Bench, a
carefully verified benchmark for unified physical grounding evaluation. We further
introduce UniPhysGen, a unified physical grounding model that jointly reasons over
articulation semantics and intrinsic physical properties. UniPhysGen incorporates
geometry-robust articulation grounding to mitigate geometric shortcut bias under
heterogeneous part decompositions. Extensive experiments demonstrate state-of-the-art
performance across articulation grounding and intrinsic physical property estimation
tasks, while the resulting assets can be directly deployed in robotic simulation
environments for realistic physical interaction. Our code and dataset will be available
at https://github.com/breezexian/UniPhysGen.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13586v1
- Authors: Xian Li, Rong Wei, Lujie Yang, Haolin Huang, Junyuan Fang, Siliang Tang, Jun Xiao, Rui Tang, Juncheng Li
- Published: 2026-07-15T08:27:07Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
