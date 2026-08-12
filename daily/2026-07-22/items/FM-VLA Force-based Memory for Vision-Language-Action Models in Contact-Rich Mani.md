---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18231v1"
published: "2026-07-20T17:58:31Z"
age_days: 1
score: 33
created: 2026-07-22
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models have achieved impressive generalization in robotic
manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by
conditioning on past images or language summaries. Vision-based memory approaches
address this by conditioning on sampled past image frames, but they are computationally
expensive and fundamentally limited when temporal events are visually ambiguous, e.g.,
pushing a button multiple times with small movements. We propose FM-VLA, a VLA model
with force-based memory, enabling temporal context reasoning for non-Markovian, contact-
rich manipulation. We encode force histories into compact force memory tokens with a
variational autoencoder (VAE) pretrained with force time series reconstruction. By
projecting force latent representations and short state history as additional
conditioning tokens to the action expert module, we enable VLAs to leverage accumulated
contact event history to guide manipulation. We evaluate FM-VLA on three memory-
dependent tasks, including finding a hidden block, pressing a button, and wiping a dish
for a specific number of times. Our lightweight force memory achieves over 80% success
rate with minimal inference overhead, significantly outperforming baseline approaches.
Project page: https://qft-333.github.io/FM-VLA-Page/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18231v1
- Authors: Ruicheng Li, Qixiu Li, Ruichun Ma, Yu Deng, Lin Luo, Zhiying Du, Jianfeng Xiang, Huizhi Liang, Ruicheng Wang, Jiaolong Yang, Baining Guo
- Published: 2026-07-20T17:58:31Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
