---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08476v1"
published: "2026-08-09T04:41:34Z"
age_days: 2
score: 26
created: 2026-08-12
concepts: ["多模态基础模型"]
---

# RayLift: Lifting Complementary Ray-Wise Evidence with 3D Geometry Priors for Semantic Scene Completion

## 为什么重要

自动筛选分数：26

连接概念：[[多模态基础模型]]

## 摘要

Camera-based 3D semantic scene completion (SSC) provides comprehensive scene
understanding for autonomous driving and robotics. However, existing methods often treat
stereo depth estimates as deterministic geometric constraints, causing depth uncertainty
and local correspondence errors to propagate directly into voxel representations. To
address this issue, we propose RayLift, a framework that uses stereo geometry as a
metric reference while incorporating complementary ray evidence to recover reliable 3D
structures adaptively. RayLift first employs a Complementary Context Encoder that
extracts geometry-aware priors from a frozen 3D vision foundation model, thereby
enriching the scene context. It then introduces a Depth Ray Evidence Lifter module that
jointly models geometric dissimilarity, depth confidence, and spatial uncertainty to
adaptively sample and weight candidate surface locations along each camera ray. Finally,
a Semantic-Aware Voxel Integrator injects the resulting ray evidence into voxel features
by explicitly modeling their spatial support. Extensive experiments on SemanticKITTI and
SSCBench-KITTI-360 demonstrate that RayLift achieves competitive performance and
consistently outperforms existing methods.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08476v1
- Authors: Meng Wang, Hongxia Yu, Wenzhe He, Xingdong Song, Huilong Pi, Jiapeng Zhang, Ruihui Li
- Published: 2026-08-09T04:41:34Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
