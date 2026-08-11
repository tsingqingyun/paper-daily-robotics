---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08016v1"
published: "2026-08-08T08:53:54Z"
age_days: 2
score: 28
created: 2026-08-11
concepts: ["世界模型", "具身智能评测与基准"]
---

# EgoTrack3D: A Modular Framework for Egocentric 3D Object Tracking

## 为什么重要

自动筛选分数：28

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

Understanding 3D scenes from egocentric video is fundamental for robotics and autonomous
navigation, yet rapid viewpoint changes and partial occlusions make building structured
representations challenging. Existing 3D tracking and scene graph construction methods
primarily address explicit interactions or assume static scenes, limiting their ability
to capture complex dynamics. We introduce EgoTrack3D, a modular framework that
reconstructs and maintains a dynamic 3D scene representation directly from egocentric
RGB video. The framework lifts 2D segmentation masks into a global 3D coordinate frame,
using a point-based motion scoring mechanism alongside a voxel-based merging heuristic
to associate object tracks. EgoTrack3D maintains accurate representations over time,
achieving an 11% improvement in percentage of correct locations (PCL) relative to the
strongest baseline on the Aria Digital Twin (ADT) dataset, while addressing the more
general setting of persistent 3D tracking for both static and dynamic objects.
Furthermore, to demonstrate the system's robustness under degraded conditions that
simulate real-world deployment constraints, we replace dense depth maps with sparse 3D
bounding box estimation and integrate interaction-guided dynamic association, enabling
EgoTrack3D to maintain accurate spatial representations despite noisy observations.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08016v1
- Authors: Jan Kulik, Bjarni Dagur Thor Karason, Yung-Hsu Yang, Boyang Sun, Marc Pollefeys, Xi Wang
- Published: 2026-08-08T08:53:54Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
