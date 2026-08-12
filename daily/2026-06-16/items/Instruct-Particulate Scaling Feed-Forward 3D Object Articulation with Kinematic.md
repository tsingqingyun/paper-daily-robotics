---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14699v1"
published: "2026-06-12T17:59:36Z"
age_days: 3
score: 24
created: 2026-06-16
concepts: ["多模态基础模型", "世界模型"]
---

# Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control

## 为什么重要

自动筛选分数：24

连接概念：[[多模态基础模型]], [[世界模型]]

## 摘要

Reconstructing articulated 3D objects is important for animation, gaming, and robotic
simulations. Recent neural networks can estimate the articulated structure of 3D
objects, but their generalization remains limited by the scarcity of annotated data for
this task. To address this gap, we introduce Instruct-Particulate, a model that takes a
3D mesh together with a target kinematic specification, including part descriptions,
connectivity, joint types, and optional point prompts, and predicts the corresponding
kinematic part segmentation and joint motion parameters. The kinematic specification
disambiguates the task and allows the model to target annotations of different
granularity, thereby making it possible to use more abundant heterogeneous training
data. At test time, the kinematic specification can be obtained automatically from
large-scale vision-language models, so the model can be applied to any input mesh. To
train our model at scale, we construct a heterogeneous dataset of more than 150,000
articulated 3D objects, extending existing publicly available collections with data
obtained by partially labelling other 3D models (monolithic or already decomposed into
parts) with kinematic labels by means of vision-language models. Experiments show that
our model generalizes better across categories and to AI-generated meshes, enabling
articulated asset reconstruction from real-world images via image-to-3D models.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14699v1
- Authors: Ruining Li, Yuxin Yao, Matt Zhou, Chuanxia Zheng, Christian Rupprecht, Joan Lasenby, Shangzhe Wu, Andrea Vedaldi
- Published: 2026-06-12T17:59:36Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
