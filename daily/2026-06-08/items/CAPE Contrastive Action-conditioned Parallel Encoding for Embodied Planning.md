---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07304v1"
published: "2026-06-05T14:21:44Z"
age_days: 2
score: 29
created: 2026-06-08
concepts: ["智能体 Agent", "世界模型"]
---

# CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Embodied agents need to predict the future consequences of candidate actions in order to
plan effectively before execution. Existing visual dynamics models learn by
reconstructing future visual states or rolling out dense latent representations, which
spreads learning capacity across visually salient but planning-irrelevant content rather
than the action-conditioned changes that drive manipulation outcomes. We propose CAPE, a
Contrastive Action-conditioned Parallel Encoding framework that learns visual dynamics
by distinguishing the future outcomes induced by different action sequences. Given an
initial observation and a candidate action sequence, CAPE decodes the full future latent
trajectory in a single forward pass and is trained with a Goal-Convergent Contrastive
Objective that aligns predictions corresponding to the same future outcome while
separating those corresponding to different outcomes. On real-world DROID and zero-shot
transfer to RoboCasa, CAPE substantially outperforms prior baselines on future-state
retrieval, offline action matching, and closed-loop planning, while notably reducing
planning-time inference cost at long prediction horizons.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07304v1
- Authors: Cong Chen, Haowen Wang, Zhixiang Zhang, Pei Ren, Zhengping Che
- Published: 2026-06-05T14:21:44Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
