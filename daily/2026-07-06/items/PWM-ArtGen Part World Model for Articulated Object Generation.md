---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02045v1"
published: "2026-07-02T11:12:29Z"
age_days: 3
score: 24
created: 2026-07-06
concepts: ["世界模型"]
---

# PWM-ArtGen: Part World Model for Articulated Object Generation

## 为什么重要

自动筛选分数：24

连接概念：[[世界模型]]

## 摘要

The key challenge in articulated 3D object generation from a single image is accurately
predicting the underlying kinematic structure. Existing methods either infer kinematic
parameters directly from a static image that lacks dynamic part-level kinematic
relationships, or estimate parameters from visual dynamics generated from a single
image, which is prone to accumulated errors of two steps. Moreover, the limited scale
and diversity of existing annotated datasets further hinder generalization to complex,
real-world objects. To overcome these limitations, we propose to learn the joint
distribution of visual dynamics and kinematic parameters. Recognizing that articulated
objects can be formulated as dynamic systems, we propose a unified Part World Model
called PWM-ArtGen. To leverage unannotated data, this model couples action diffusion and
image diffusion with independent diffusion timesteps, which enables visual branch co-
training. We further curate a photorealistic dataset of 19.7k part-level image pairs
without kinematic annotations, to support co-training. Experiments demonstrate that PWM-
ArtGen substantially outperforms existing baselines in the resting state and exhibits
strong zero-shot generalization to out-of-distribution objects.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02045v1
- Authors: Wentao Zheng, Ancong Wu
- Published: 2026-07-02T11:12:29Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
