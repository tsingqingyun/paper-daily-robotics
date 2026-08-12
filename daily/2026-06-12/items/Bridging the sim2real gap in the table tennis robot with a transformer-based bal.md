---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11464v1"
published: "2026-06-09T21:35:59Z"
age_days: 2
score: 31
created: 2026-06-12
concepts: ["智能体 Agent", "世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Bridging the sim2real gap in the table tennis robot with a transformer-based ball states predictor

## 为什么重要

自动筛选分数：31

连接概念：[[智能体 Agent]], [[世界模型]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Robotic table tennis is a representative benchmark for high-speed, closed-loop robotic
control in dynamic environments, where accurate and fast prediction of ball states is
critical for reliable planning and control. Physics-based approaches rely heavily on
accurate parameter identification and precise initial state, while learning-based
methods often struggle to capture long-range temporal dependencies and are typically
trained on limited or simulated data. We propose a transformer-based framework for table
tennis ball state prediction that leverages attention mechanisms to model long-range
temporal correlations directly from historical observations, without relying on explicit
flight or bounce models. To support robust learning and generalization, we collected a
large-scale real-world dataset from players of varying skill levels and diverse ball
cannon configurations. The combination of a high-capacity transformer architecture and
extensive real-world data enables accurate long-horizon forecasting. Building on this
capability, we introduce a plug-and-play sim-to-real transfer strategy, Swap Predictor
at Deployment (SPAD), which replaces the physics-based simulator used during training
with the proposed real-world-trained predictor at deployment, improving the sim-to-real
transferability of the policy without requiring retraining. We demonstrate that this
simple substitution effectively narrows the sim-to-real gap while preserving the
efficiency and scalability of simulation-based training.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11464v1
- Authors: Yin Bi, Christian Conti, Bilan Yang, Alexander Sigrist, Peter Dürr, Naoya Takahashi
- Published: 2026-06-09T21:35:59Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
