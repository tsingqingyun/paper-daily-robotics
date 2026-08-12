---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14010v1"
published: "2026-06-12T01:06:42Z"
age_days: 3
score: 26
created: 2026-06-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RT-VLA: Real-Time Vision-Language-Action Models via Knowledge Distillation

## 为什么重要

自动筛选分数：26

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models have shown strong potential for end-to-end
autonomous driving by jointly modeling visual perception, language reasoning,
explainability and action prediction. However, their large vision-language backbones and
reasoning modules introduce substantial inference latency and thereby prevent their
deployment in the unforgiving reality of the road networks. We propose RT-VLA, a
lightweight, distilled VLA model that transfers the driving and reasoning capabilities
of the state-of-the-art SimLingo model into a compact student through multi-level
supervised distillation. RT-VLA preserves language-based reasoning and supports post-hoc
explanation through offline language analysis of safety-critical driving moments without
adding latency to real-time control. Compared to the SimLingo teacher, RT-VLA maintains
competitive closed-loop driving and language reasoning performance while reducing
inference time by 44.8X in vision-only mode and 7.9X in vision+language mode. These
results suggest that supervised distillation is a practical approach for building real-
time, explainable VLA-style autonomous driving models.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14010v1
- Authors: Xiangyu Huang, Zhenlin Hua, Han Zhou, Shounak Sural, Ragunathan Rajkumar
- Published: 2026-06-12T01:06:42Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
