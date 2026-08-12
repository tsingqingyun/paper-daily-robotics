---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15727v1"
published: "2026-07-17T08:04:43Z"
age_days: 2
score: 35
created: 2026-07-20
concepts: ["具身智能评测与基准"]
---

# Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation

## 为什么重要

自动筛选分数：35

连接概念：[[具身智能评测与基准]]

## 摘要

Robust 3D reconstruction is essential for robotics and embodied perception. Recent feed-
forward approaches such as DUSt3R have demonstrated impressive progress in dense 3D
reconstruction from RGB images, achieving global geometric consistency and strong
generalization. However, extending such dense 3D reconstruction to event cameras remains
challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the
lack of large-scale, well-labeled datasets. In this work, we introduce Event3R, a feed-
forward framework that directly maps asynchronous event streams to globally consistent
3D point clouds. Event3R represents incoming events as spatial-temporal voxels, enabling
time-aware feature integration through a temporal attention module that enhances the
module's temporal feature learning. To further strengthen temporal representation
learning and reduce reliance on labeled data, we propose a Masked Bin Modeling (MBM)
strategy for self-supervised pre-training, enabling robust temporal representation
learning with minimal labeled data, and retain it as an auxiliary fine-tuning objective.
In addition, contrastive alignment and consistency regularization losses are
incorporated during fine-tuning to reinforce structural correspondence and temporal
coherence across views. Extensive experiments on both synthetic and real-world
benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally
aligned 3D reconstructions, significantly outperforming existing event-based methods.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15727v1
- Authors: Jian Huang, Haotian Shen, Xinhao Lou, Chengrui Dong, Wenpu Li, Peidong Liu
- Published: 2026-07-17T08:04:43Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
