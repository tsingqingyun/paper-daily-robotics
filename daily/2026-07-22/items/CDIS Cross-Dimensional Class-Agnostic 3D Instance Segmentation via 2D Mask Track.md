---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17778v1"
published: "2026-07-20T10:09:12Z"
age_days: 1
score: 31
created: 2026-07-22
concepts: ["具身智能评测与基准"]
---

# CDIS: Cross-Dimensional Class-Agnostic 3D Instance Segmentation via 2D Mask Tracking and 3D-2D Projection Merging

## 为什么重要

自动筛选分数：31

连接概念：[[具身智能评测与基准]]

## 摘要

Class-agnostic 3D instance segmentation is critical for robotic systems operating in
unknown environments, enabling perception of previously unseen objects for reliable
manipulation and navigation. Existing approaches typically project per-frame 2D instance
masks into 3D and merge them, which often breaks object identities across time and
yields fragmented 3D instances. We introduce Cross-Dimensional Class-Agnostic 3D
Instance Segmentation (CDIS), a zero-shot framework that explicitly tracks 2D instance
masks across frames and associates them with 3D superpoints, creating a feedback loop
between 2D and 3D. This cross-dimensional reasoning links temporally stable 2D tracks
with spatially coherent 3D regions, producing globally consistent 3D instance labels
without any 3D-specific training. Experiments on benchmark datasets demonstrate that
CDIS achieves higher accuracy and consistency than state-of-the-art zero-shot methods,
while remaining efficient and scalable to diverse real-world environments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17778v1
- Authors: Juno Kim, Hye-Jung Yoon, Yesol Park, Byoung-Tak Zhang
- Published: 2026-07-20T10:09:12Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
