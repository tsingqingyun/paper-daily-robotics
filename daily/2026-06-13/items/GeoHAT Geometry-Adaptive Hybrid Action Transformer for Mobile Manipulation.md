---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13394v1"
published: "2026-06-11T14:25:09Z"
age_days: 1
score: 28
created: 2026-06-13
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# GeoHAT: Geometry-Adaptive Hybrid Action Transformer for Mobile Manipulation

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Whole-body mobile manipulation requires coordinating mobile base and manipulator under
shifting viewpoints, posing challenges in geometric perception and action generation.
Current policies either rely on 2D features or sparse 3D representations that lack dense
spatial structure, and typically encode arm and base within one action vector that
ignores their distinct control demands. Moreover, existing dense fusion strategies risk
corrupting pretrained representations under noisy depth while incurring heavy
computational overhead. We present GeoHAT, an end-to-end diffusion-based framework built
on a simple principle: geometry should be injected only where reliable and attended to
only where needed. GeoHAT employs a lightweight Fourier spatial encoder that maps dense
per-pixel 3D coordinates into geometric tokens without an additional 3D vision backbone.
These tokens are then selectively injected into vision foundation model features through
per-token gated fusion modulated by depth validity, preserving the semantic prior while
enriching spatial understanding. For action generation, a Hybrid Whole-Body Action
Decoder decomposes arm and base into distinct subspaces and lets each action modality
attend to its task-relevant visual context through sparse cross-attention, while causal
temporal modeling captures intra-timestep coordination and inter-timestep dependencies.
Experiments on the ManiSkill-HAB simulation benchmark demonstrate that GeoHAT achieves a
79.3% mean success rate, surpassing the strongest baseline by 23.7%. Furthermore, real-
world experiments on diverse tasks also confirm consistent improvements over all
baselines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13394v1
- Authors: Xiangyu Zhu, Renjun Wu, Luzhou Ge, Jinyan Liu, Xuesong Li
- Published: 2026-06-11T14:25:09Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
