---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.16012v1"
published: "2026-07-17T14:46:39Z"
age_days: 2
score: 27
created: 2026-07-20
concepts: ["多模态基础模型"]
---

# DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction

> [!summary] 一句话结论（基于摘要）
> On NYUv2, DPNeXt-B also achieves the best semantic segmentation and depth estimation results among the compared methods while requiring substantially fewer trainable parameters than prior large-scale MTL models.

## 关键点

- **问题**：While Vision Foundation Models (VFMs) are increasingly adopted as robust feature encoders, existing decoding strategies present a critical bottleneck.
- **创新点 / 方法**：To address this, we propose DPNeXt, a streamlined multi-scale feature fusion decoder and efficient alternative to the standard Dense Prediction Transformer (DPT).
- **证据**：On NYUv2, DPNeXt-B also achieves the best semantic segmentation and depth estimation results among the compared methods while requiring substantially fewer trainable parameters than prior large-scale MTL models.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

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

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.16012v1
- Authors: Jehun Kang, Jungha Wang, Youngjun Hwang, David Hyunchul Shim
- Published: 2026-07-17T14:46:39Z
- Age days: 2

</details>
