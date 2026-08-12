---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25044v1"
published: "2026-05-24T12:41:34Z"
age_days: 1
score: 42
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models

## 为什么重要

自动筛选分数：42

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Learning universal policies from cross-embodied data remains a fundamental challenge in
robotics. Although Vision-Language-Action (VLA) models are pre-trained on large and
diverse datasets, they typically rely on embodiment-specific fine-tuning to achieve
strong performance in downstream tasks. This requirement severely limits their
generalization capability and restricts knowledge transfer across embodiments performing
similar tasks. To overcome these limitations, we focus on cross-embodied settings with
shared robotic bases and heterogeneous end-effectors, and propose X-DiffVLA, a
diffusion-based VLA model featuring a unified cross-embodied action head. X-DiffVLA can
leverage the generative strengths of diffusion models to capture both the diversity and
latent correlations in cross-embodied datasets. Specifically, we introduce Embodiment
Forcing, a classifier-free guidance technique to implicitly steer action generation
toward embodiment-specific functional components, capturing fine-grained structural
nuances without explicit supervision. In addition, a Morphological Tree Diffusion
approach is designed to strengthen behavioral correlations across diverse end-effectors,
maximizing the transferability of heterogeneous demonstrations. Experimental results
across RoboCasa and Isaac Gym, covering different embodiments from grippers to dexterous
hands, show that X-DiffVLA achieves state-of-the-art performance, with improvements of
15.3% and 12.5%, respectively. Real-world evaluations further validate the robustness of
the proposed framework and its effectiveness in scalable cross-embodied policy learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25044v1
- Authors: Boyu Li, Chaoyi Xu, Haoqi Yuan, Xinrun Xu, Börje F. Karlsson, Dongbin Zhao, Haoran Li, Zongqing Lu
- Published: 2026-05-24T12:41:34Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
