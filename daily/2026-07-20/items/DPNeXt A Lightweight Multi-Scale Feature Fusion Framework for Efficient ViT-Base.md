---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.16012v1"
published: "2026-07-17T14:46:39Z"
age_days: 2
score: 27
created: 2026-07-20
concepts: ["多模态基础模型"]
---

# DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]]

## 摘要

Multi-Task Learning (MTL) in robotics perception systems supports comprehensive 3D
spatial scene understanding by integrating semantic segmentation and depth estimation.
While Vision Foundation Models (VFMs) are increasingly adopted as robust feature
encoders, existing decoding strategies present a critical bottleneck. To address this,
we propose DPNeXt, a streamlined multi-scale feature fusion decoder and efficient
alternative to the standard Dense Prediction Transformer (DPT). DPNeXt uses dual
depthwise separable inverted bottlenecks to improve frozen VFM utilization through
fusion-centric decoding and independent task modularization. To further mitigate
negative inductive transfer between tasks, we introduce the Multi-Task Boundary Guidance
(MTBG) strategy. Unlike prior boundary-aware methods that add fusion modules or gating,
MTBG applies symmetric boundary-focused supervision to encourage geometric consistency
without extra annotation or inference cost. Experiments on Cityscapes show that DPNeXt-S
outperforms prior state-of-the-art (SOTA) MTL models, while DPNeXt-B further improves
the overall performance and achieves the best results among the compared methods. On
NYUv2, DPNeXt-B also achieves the best semantic segmentation and depth estimation
results among the compared methods while requiring substantially fewer trainable
parameters than prior large-scale MTL models. Compared with the standard DPT, DPNeXt-S
reduces trainable parameters by 78.6% and achieves the fastest inference speed among the
compared models on resource-constrained laptop hardware. The source code, model
checkpoints, and a demo video will be made available at
https://github.com/kangjehun/DPNeXt.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.16012v1
- Authors: Jehun Kang, Jungha Wang, Youngjun Hwang, David Hyunchul Shim
- Published: 2026-07-17T14:46:39Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
