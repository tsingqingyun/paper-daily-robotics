---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10495v1"
published: "2026-06-09T07:18:01Z"
age_days: 0
score: 34
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Safe social navigation requires robots to distinguish people from ordinary obstacles and
to react before danger becomes imminent. We show that pretrained Vision-Language-Action
(VLA) models already encode pedestrian-object distinctions and future collision signals
in their internal representations, but behavior cloning fails to translate these signals
into socially appropriate actions. To address this mismatch, we propose SALSA, a two-
stage annotation-free post-training framework: (1) social behavioral alignment bridges
intermediate-layer social features to the action head and trains on counterfactual
human-object scene pairs to break visual saliency shortcuts; (2) temporal safety
alignment provides automatically generated future-risk supervision to enable
anticipatory collision avoidance. On SCAND and real-world deployment, SALSA reduces
near-collisions by 86.4% and improves social counterfactual accuracy from 53% to 93%,
demonstrating that safer social navigation can be achieved by teaching VLA policies to
act on representations they already possess. These results show that pretrained VLA
policies can be adapted for safer social navigation by better aligning their latent
representations with action generation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10495v1
- Authors: Qingzi Wang, Xiyang Wu, Guangyao Shi, Dianwei Chen, Xianfeng Yang, Dinesh Manocha
- Published: 2026-06-09T07:18:01Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
