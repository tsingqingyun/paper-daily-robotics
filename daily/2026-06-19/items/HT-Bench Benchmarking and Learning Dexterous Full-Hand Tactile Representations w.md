---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19161v1"
published: "2026-06-17T15:01:30Z"
age_days: 1
score: 29
created: 2026-06-19
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# HT-Bench: Benchmarking and Learning Dexterous Full-Hand Tactile Representations with Egocentric Vision

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Establishing a universal benchmark for tactile representation learning in robotic
manipulation remains challenging due to the diversity of tactile sensor designs, data
formats, and robot embodiments. Rather than seeking to establish such, we explore a
scalable and promising direction for future development: egocentric vision paired with
full-hand tactile data. To this end, we introduce \textbf{HT-Bench}, a large-scale
multi-task benchmark for dexterous full-hand tactile sensing, comprising 10M RGB frames
and 7.8M tactile frames collected across 226 tasks. HT-Bench evaluates tactile
representations from three key perspectives: whether they encode meaningful contact
geometry, whether they can align tactile observations with visual information, and
whether they generalize to unseen tasks. To assess these capabilities, HT-Bench includes
four tasks: fine-grained tactile similarity retrieval, masked tactile inpainting,
vision-to-tactile synthesis, and multimodal tactile frame prediction. We further propose
\textbf{HandTouch}, a vector-quantized vision--tactile encoder that learns tactile
representations through progressive spatial, cross-modal, and temporal training. Across
HT-Bench, HandTouch consistently outperforms representative tactile encoder baselines,
improving Recall@5 on fine-grained tactile similarity retrieval from 74.65\% to 85.23\%,
reducing RMSE on masked tactile inpainting from 0.022 to 0.010, and increasing OOD cIoU
on vision-to-tactile synthesis from 0.628 to 0.705. These results demonstrate the
effectiveness of HandTouch and suggest that large-scale egocentric full-hand tactile
data provides a scalable basis for evaluating and advancing tactile representation
learning in dexterous manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19161v1
- Authors: Yuzhe Huang, Jiaping Wu, Jiaming Jiang, Hezhe Lin, Aikebaier Aierken, Yunlong Wang, Kun Cheng, Ziyuan Jiao, Yuanxin Zhong
- Published: 2026-06-17T15:01:30Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
