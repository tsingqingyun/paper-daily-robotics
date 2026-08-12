---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09166v1"
published: "2026-08-10T06:22:10Z"
age_days: 1
score: 24
created: 2026-08-12
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Particle-Based Conformal Prediction for Contact-Aware Uncertainty Calibration in Stratified Configuration Spaces

## 为什么重要

自动筛选分数：24

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Reliable uncertainty representation is essential for deploying autonomous systems that
interact with their environment, as robots must reason about how uncertainty arising
from both stochasticity and model mismatch is impacted by contacts with obstacles (e.g.,
when navigating through a cluttered environment or inserting a part into an assembly).
We propose Calibrated Particle-sets for Trans-dimensional Uncertainty Representation
(CaPTURe), a geometry-aware, conformal prediction-based algorithm that generates
probabilistically valid prediction regions of the unknown future system configuration
using particle-based models of arbitrary fidelity. While calibrated uncertainty
predictions are essential for safe and efficient planning, analytical or learned motion
models are often inaccurate - due to limited data, simplifying assumptions, unmodeled
effects, etc. - which can lead to unsafe executions or task failure. Additionally, when
a robot contacts an obstacle, the distribution of its future configurations can become
multimodal or disjoint, or lie along manifolds of lower intrinsic dimension than the
space of possible robot configurations. Our method uses a calibration dataset of system
transitions to locally calibrate motion uncertainty estimates, constructing regions
guaranteed to contain the future robot configuration at a user-set probability. Our
calibration procedure captures how motion uncertainty varies between contact-rich and
contactless motions, leading to sufficient coverage in both cases. We evaluate our
method on two simulated planning tasks: controlling a marble around a labyrinth and
performing tight-tolerance peg-in-hole insertion with a manipulator. Compared to
relevant baselines, CaPTURe achieves the user-specified coverage requirement both in and
out of contact and achieves up to a 30% absolute improvement in task success rate over
the best baseline.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09166v1
- Authors: Luís Marques, Kristian Popov, Dmitry Berenson
- Published: 2026-08-10T06:22:10Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
