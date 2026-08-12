---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.16015v1"
published: "2026-07-17T14:48:43Z"
age_days: 2
score: 31
created: 2026-07-20
concepts: ["具身智能评测与基准"]
---

# PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects

## 为什么重要

自动筛选分数：31

连接概念：[[具身智能评测与基准]]

## 摘要

6D pose estimation remains a key challenge in robotics and computer vision, particularly
in industrial environments. The deployment of currently available data-driven methods is
often limited by resource-intensive data pipelines, reliance on textured 3D models, and
sensitivity to geometric deviations caused by damages or assembly defects. We present
PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image
using only an untextured 3D model. Synthetic depth and normal maps are rendered from
sampled reference viewpoints and matched to the query image via a pretrained cross-
modality feature matcher. Matched keypoints are back-projected to obtain 2D--3D
correspondences for PnP-based pose estimation. Relying exclusively on geometry makes the
method inherently robust to lighting and texture variation, while correspondence
filtering handles geometric deviations between the model and physical object. We
evaluate on widely-used public benchmarks, reporting state-of-the-art results on
texture-less objects without object-specific training, and introduce a novel dataset
with assembly defects, texture variations, and occlusion to demonstrate real-world
applicability.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.16015v1
- Authors: Leon Jungemeyer, Alejandro Magaña, Gautham Mohan, Matthias Karl, Daniel Werdehausen
- Published: 2026-07-17T14:48:43Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
