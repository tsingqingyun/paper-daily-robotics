---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20670v1"
published: "2026-07-22T19:08:31Z"
age_days: 1
score: 27
created: 2026-07-24
concepts: ["世界模型"]
---

# ODeform: Learning Continuous 4D Motion for Shape Deformation with Neural ODEs

## 为什么重要

自动筛选分数：27

连接概念：[[世界模型]]

## 摘要

Modeling continuous object deformation is important for many computer vision and
robotics tasks, such as manipulation and simulation. Existing approaches rely on
learning-based methods or physics simulators to model shape deformations. However, these
approaches either use discrete time steps or are too computationally intensive for real-
time applications. We present ODeform, a novel extension of Neural Ordinary Differential
Equations to continuous 4D dynamics of deformable objects in 3D space. Our method
transforms 3D point clouds and physical conditions (like material properties) into a
unified latent space. By solving the resulting ordinary differential equations over
time, we model deformations as continuous flows within this learned embedding,
eliminating the need for discrete time steps while maintaining computational efficiency.
We evaluate our approach on unseen physical parameter configurations, showing improved
motion prediction accuracy over baseline methods. Our experiments further demonstrate a
successful transfer to real 3D captured objects with novel shapes, along with effective
interpolation and extrapolation of the learned dynamics. Our code and data will be made
publicly available.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20670v1
- Authors: Yordanka Velikova, Mahdi Saleh, Liming Kuang, Benjamin Busam
- Published: 2026-07-22T19:08:31Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
