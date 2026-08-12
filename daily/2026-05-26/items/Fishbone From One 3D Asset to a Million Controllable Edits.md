---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.24805v1"
published: "2026-05-24T01:38:43Z"
age_days: 2
score: 29
created: 2026-05-26
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# Fishbone: From One 3D Asset to a Million Controllable Edits

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

Large-scale controllable 3D assets are critical for computer graphics, embodied AI,
robotics, and interactive content creation, yet creating diverse 3D assets remains
challenging due to the high cost of manual modeling and rigging. Shape deformation
offers a natural way to generate variations from existing meshes, but existing data-
driven methods often rely on sparse user inputs, while parametric editing frameworks
require manually designed control structures and category-specific configurations.
Inspired by natural creatures, where a central spine governs global shape and cross-
sectional ribs control local variation, we introduce Fishbone, a unified rib-spine
representation for general shapes that supports controllable parametric mesh
deformation, reduced-space dynamics, and animation. Given an input mesh, Fishbone
computes a geodesic scalar field with an adaptive heat method, extracts iso-contours as
cross-sectional ribs, constructs a smooth geometry-aware spine through rib centers, and
associates surface vertices with nearby rib and spine structures using Gaussian-weighted
skinning. The resulting representation enables real-time and predictable deformation:
ribs control local profiles such as thickness, orientation, and cross-sectional
variation, while the spine controls global bending, twisting, and stretching. The same
structure also supports reduced-space simulation and keyframe animation. We further
construct Fishbone-136K by augmenting Hunyuan3D with rib-spine structures, and
demonstrate applications in controllable 3D generation, deformation-based data
augmentation for robot learning, interactive mesh editing, and agentic generation.
Experiments demonstrate the effectiveness, efficiency, and versatility of the proposed
framework.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.24805v1
- Authors: Yumeng He, Xiaoying Wang, Peihao Li, Yanjia Huang, Joe Masterjohn, Jiajun Wu, Leonidas Guibas, Yin Yang, Ying Jiang, Chenfanfu Jiang
- Published: 2026-05-24T01:38:43Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
