---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07100v1"
published: "2026-06-05T09:51:25Z"
age_days: 2
score: 41
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# LARA: Latent Action Representation Alignment for Vision-Language-Action Models

## 为什么重要

自动筛选分数：41

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Visual-language action (VLA) models enable robots to predict actions directly from
observations and language instructions, but their performance depends on large-scale,
high-quality data and is limited by the scarcity of real-world robot action datasets. To
facilitate VLA model learning with abundant unlabeled human videos, Latent Action Models
(LAM) learn latent action representations from visual dynamics to provide additional
supervision for VLA learning. However, LAM and VLA are typically trained separately,
leaving LAM ungrounded during VLA training and VLA models constrained by frozen LAM
representations. To address these issues, we propose Latent Action Representation
Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via
representation alignment. This enables reciprocal benefits where LAMs learn with action
trajectories to avoid spurious visual changes, while VLAs are regularized by forward
dynamics learned within LAMs to reduce hallucinations of functionally ineffective
trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-
training enhancement of pre-trained VLA models, and LAM refinement, achieving an average
of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-
world robotic manipulation benchmarks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07100v1
- Authors: Mengya Liu, Baoxiong Jia, Jiangyong Huang, Jingze Zhang, Siyuan Huang
- Published: 2026-06-05T09:51:25Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
