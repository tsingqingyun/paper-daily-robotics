---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12706v1"
published: "2026-06-10T21:53:33Z"
age_days: 3
score: 27
created: 2026-06-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models generate chain-of-thought (CoT) reasoning alongside
driving trajectories, but existing benchmarks evaluate only trajectory quality and do
not assess whether the CoT is relevant, consistent, or causally connected to the driving
action. We introduce VLADriveBench, a framework that combines observational metrics
(mentioning, hallucination, contradiction, action alignment) with a CoT intervention
protocol to provide complementary views of the CoT-action relationship. Applying
VLADriveBench to three models across two architectures, we find that the two analyses
can diverge sharply: ORION scores highest on observational alignment yet its CoT is
epiphenomenal, while Alpamayo v1.5 scores lower yet its CoT is strongly causal, with
visual salience gating the extent of CoT influence.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12706v1
- Authors: Thach Nguyen, Danhua Guo, Tom Lampo, Fei Wu, Burhan Yaman
- Published: 2026-06-10T21:53:33Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
