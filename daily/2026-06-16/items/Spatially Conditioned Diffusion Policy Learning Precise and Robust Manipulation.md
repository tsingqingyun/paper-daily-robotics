---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14535v1"
published: "2026-06-12T15:12:03Z"
age_days: 3
score: 25
created: 2026-06-16
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera

## 为什么重要

自动筛选分数：25

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Recent visual imitation learning systems have widely adopted multi-camera setups with
wrist-mounted cameras as the de facto standard. However, manipulation from a single
global view remains challenging, as the policy should capture fine-grained interaction
details and identify task-relevant regions without local wrist views. To address this
challenge, we present Spatially Conditioned Diffusion Policy (SCDP), a diffusion-based
visuomotor policy that achieves precise and robust manipulation in a single-camera
setting. Our key idea is that end-effector trajectories can serve as visual attention
anchors that reflect task-relevant regions. Building on this idea, SCDP consists of two
key components: (i) a visual encoder that produces multi-scale feature maps to capture
both broader context and fine-grained visual features, and (ii) a spatial conditioning
module that samples point-wise features along intermediate end-effector trajectories in
the diffusion loop. Extensive simulation experiments show that SCDP consistently
outperforms strong single-view baselines and achieves performance comparable to multi-
camera baselines. Real-world experiments further demonstrate precise manipulation and
robustness to visual distractors, highlighting the potential of single-camera imitation
learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14535v1
- Authors: Seoyoon Kim, Kanghyun Kim, Dongwoo Ko, Yeong Jin Heo, Min Jun Kim
- Published: 2026-06-12T15:12:03Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
