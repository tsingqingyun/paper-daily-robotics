---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19451v1"
published: "2026-06-17T18:00:08Z"
age_days: 2
score: 29
created: 2026-06-20
concepts: ["AI 核心知识地图"]
---

# 3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning

## 为什么重要

自动筛选分数：29

连接概念：[[AI 核心知识地图]]

## 摘要

We introduce 3D-DLP, a self-supervised object-centric representation learning model that
decomposes scene-level RGB-D or voxel observations into a set of 3D latent particles.
Building on the Deep Latent Particles (DLP) framework, each particle encodes
disentangled attributes, including 3D keypoint position, bounding box dimensions, and
appearance features, and represents a distinct entity in the scene. The model learns
interpretable per-particle segmentation maps through an end-to-end self-supervised
reconstruction objective. We demonstrate on both simulated and real-world datasets that
the learned latent space is interpretable and controllable: by manipulating particle
positions and decoding, we can generate novel scene configurations. Furthermore, we show
that leveraging these compact 3D latent particles for downstream robotic manipulation
improves performance over baselines that either lack explicit 3D information or rely on
memory-intensive dense 3D inputs without object-centric structure. Code and videos are
available at https://eubooks3003.github.io/3d-dlp.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19451v1
- Authors: Ellina Zhang, Madhaven Iyengar, Amir Zadeh, Chuan Li, Deepak Pathak, David Held, Tal Daniel
- Published: 2026-06-17T18:00:08Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
