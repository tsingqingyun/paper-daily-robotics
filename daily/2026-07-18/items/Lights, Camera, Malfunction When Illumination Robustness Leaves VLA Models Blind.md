---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14698v1"
published: "2026-07-16T08:01:49Z"
age_days: 1
score: 35
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-
purpose robot manipulation; however, their transition to real-world environments reveals
vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized
physical spotlight attack framework that exploits these vulnerabilities via targeted
illuminations, dropping baseline task success rates to zero without any access to model
internals. While adversarial training is the standard countermeasure, we identify a
critical and previously underestimated defensive pitfall: naive data augmentations
incorrectly condition VLA models to discard color as noise, collapsing their visual
perception into a purely shape-biased processor. We expose this degradation through a
diagnostic grayscale evaluation, in which the defended model maintains high success
rates on grayscale inputs, while its success rate on benign, color-dependent real-world
tasks drops to at most 47.5%, well below the undefended baseline. To address this, we
propose ChromaGuard, a chroma-preserving adversarial training method. On a physical
6-DoF robotic platform, we demonstrate that ChromaGuard achieves 97.5% and 92.5% success
rates in benign and attacked color-dependent tasks, respectively.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14698v1
- Authors: Marino Watanabe, Takami Sato, Kentaro Yoshioka
- Published: 2026-07-16T08:01:49Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
