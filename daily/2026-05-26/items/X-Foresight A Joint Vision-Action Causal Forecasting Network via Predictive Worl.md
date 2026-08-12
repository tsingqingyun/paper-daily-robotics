---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.24892v1"
published: "2026-05-24T06:37:04Z"
age_days: 2
score: 30
created: 2026-05-26
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Physical world knowledge resides mainly in videos. Equipping Vision-Language-Action
(VLA) models with such knowledge is fundamental for safe and generalizable planning.
Predictive world modeling enables VLA to internalize physical dynamics and long-term
causality by predicting future video from past observations. However, naive next-frame
prediction faces two challenges: 1) unlike semantically distinct text tokens, video
tokens are low-entropy and redundant, causing prediction to degenerate into trivial
extrapolation. 2) world modeling poses a temporal dilemma: dense prediction captures
instantaneous dynamics, but cannot efficiently model long-horizon causality. To learn
world knowledge effectively, we introduce X-Foresight, a predictive world model
integrated directly into the VLA architecture to jointly learn world modeling and real-
time action control. At its core lies a long-horizon chunk-wise auto-regressive strategy
that addresses both challenges: by predicting semantically distant chunks rather than
adjacent frames, it escapes trivial extrapolation, while preserving dense intra-chunk
frames for instantaneous dynamics and sparse inter-chunk transitions for long-term
causality. A curriculum learning schedule progressively extends prediction horizons and
stabilizes long-horizon training. To capture long-term causality effectively, we present
temporal importance sampling, which concentrates supervision on safety-critical chunks
identified by ego-motion and behavioral signals. We further delegate photorealistic
synthesis to a diffusion-based multi-view renderer, improving photorealistic appearance.
Comprehensive experiments demonstrate that X-Foresight significantly outperforms VLA
baselines in planning performance while maintaining strong generative fidelity,
establishing a robust paradigm for world-knowledge-driven autonomous systems.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.24892v1
- Authors: Baolu Li, Jingyu Qian, Rui Guo, Yilun Chen, Hanpeng Liu, Yuan Lin, Junhong Zhou, Ruixin Liu, Willow Yang, Yutong Zheng, Zhenli Zhang, Tenglong, Gu, Zhuangzhuang Ding, Pengkun Zheng, Yu Zhang, Xianming Liu
- Published: 2026-05-24T06:37:04Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
