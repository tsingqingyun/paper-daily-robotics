---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.16146v1"
published: "2026-07-17T17:27:08Z"
age_days: 2
score: 28
created: 2026-07-20
concepts: ["具身智能评测与基准"]
---

# VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds

## 为什么重要

自动筛选分数：28

连接概念：[[具身智能评测与基准]]

## 摘要

Vision and touch are complementary modalities essential for robotic perception and
manipulation. While vision provides global object context, touch offers precise local
information at contact points. Integrating these modalities for contact localization,
i.e., predicting the location of touch on an object's surface, poses significant
challenges due to the need for accurate spatial alignment between tactile data and
visual geometry. To address this challenge, we propose VTLoc, a novel visual-tactile
framework that localizes contact points from tactile readings using a 3D point cloud as
visual input. VTLoc introduces two key components: a geometric multi-modal alignment
module, which reconstructs a pseudo-point cloud from fused visual-tactile features and
aligns it with the visual point cloud to enforce spatial consistencies across
modalities; and an iterative localizing updater, which iteratively refines the predicted
contact location using fused visual-tactile features. Evaluated on a new benchmark of
100 real-world objects, VTLoc improves single-touch contact localization by reducing
local-to-global correspondence ambiguity.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.16146v1
- Authors: Zhiyuan Wu, Zhuo Chen, Shan Luo
- Published: 2026-07-17T17:27:08Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
