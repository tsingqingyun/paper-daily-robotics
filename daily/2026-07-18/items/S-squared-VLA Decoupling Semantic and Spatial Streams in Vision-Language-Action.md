---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13926v1"
published: "2026-07-15T15:07:02Z"
age_days: 2
score: 28
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level
reasoning in autonomous driving, yet they fundamentally struggle to generate precise,
low-level control actions. This limitation is rooted in a semantic-physical gap caused
by the inherent mismatch between discrete language tokens and continuous trajectory
planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by
unifying perception and control into a single policy, this entanglement creates a new
bottleneck. Standard VLAs experience a severe spatial representation collapse, which
irreversibly degrades the fine-grained spatial and geometric priors essential for safe,
boundary-aware navigation. To address this limitation, we propose the S-squared-VLA,
which explicitly decouples the semantic and spatial streams in Vision-Language-Action
models. The semantic stream leverages hierarchical bridging to extract multi-scale VLM
features for robust intent reasoning. In parallel, an independent spatial stream
bypasses the autoregressive language bottleneck, directly preserving uncompressed
spatial features from the visual encoder. By integrating auxiliary perception
supervision, this stream explicitly equips the model with rich spatial and geometric
priors. Finally, a dual-stream planning adapter fuses high-level semantic intent with
precise spatial constraints via cascaded attention mechanisms. Evaluations on the NAVSIM
closed-loop benchmark show that S-squared-VLA achieves a Predictive Driver Model Score
(PDMS) of 87.1, establishing a new state-of-the-art for VLA models under a purely
supervised fine-tuning (SFT) setting. By mitigating the spatial representation collapse
of traditional VLMs, our framework significantly outperforms baselines, achieving the
highest No Collision (NC) rate of 98.4 among all evaluated methods.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13926v1
- Authors: Jianguo Yu, Rukang Wang, Duanfeng Chu, Chen Wang, Renju Feng, Liping Lu
- Published: 2026-07-15T15:07:02Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
