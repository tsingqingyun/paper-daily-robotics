---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14585v1"
published: "2026-06-12T16:01:50Z"
age_days: 3
score: 22
created: 2026-06-16
concepts: ["智能体 Agent", "世界模型"]
---

# Sensitivity Shaping for Latent Modeling

## 为什么重要

自动筛选分数：22

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Generative dynamics models enable planning in challenging robotic systems, but safe
deployment requires reliably detecting policy-induced out-of-distribution (OOD)
transitions. Existing methods typically treat the learned dynamics as fixed and attach
post hoc support surrogates. We show that these surrogates can fail when the dynamics
are locally insensitive to critical action choices: unsupported control actions may
produce latent predictions that resemble demonstrated transitions, suppressing OOD
signals despite large true predictive errors. To address this, we introduce support-
conditioned control-sensitivity regularization, which promotes sensitive local response
to control input changes in learned dynamics in high-support training regions. This
preserves control-induced variation while limiting unstable extrapolation due to weak
empirical support. Experiments in vision-based obstacle avoidance, manipulation, and
real-robot navigation show improved OOD detection and safer closed-loop planning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14585v1
- Authors: Hongzhan Yu, Chenghao Li, Ruipeng Zhang, Henrik Christensen, Sicun Gao
- Published: 2026-06-12T16:01:50Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
