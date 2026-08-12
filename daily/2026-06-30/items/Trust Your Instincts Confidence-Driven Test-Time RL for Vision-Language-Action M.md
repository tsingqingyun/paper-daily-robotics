---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29892v1"
published: "2026-06-29T07:31:41Z"
age_days: 1
score: 36
created: 2026-06-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Reinforcement learning (RL) has become indispensable for pushing Vision-Language-Action
Models (VLAs) beyond static imitation learning. However, existing RL methods typically
require external environmental feedback, relying on predefined success signals to guide
policy updates. In this work, we show that VLA models possess useful internal evaluative
capabilities: in discrete-action VLAs, trajectories with higher generation confidence
are significantly more likely to succeed. Based on this observation, we introduce T^2VLA
(Test-time VLA), an architecture-agnostic test-time RL framework that enables VLA models
to achieve self-bootstrapping policy improvement. Instead of relying on external
rewards, T^2VLA leverages trajectory-level similarity to high-confidence expert
demonstrations as an intrinsic reward signal. In addition, we propose a Confidence-
Driven Dual Expert Bootstrapping mechanism, which dynamically balances a Local Pseudo-
Expert for exploration and a Global Expert Pool for training stability. Extensive
experiments on the LIBERO and RoboTwin benchmarks show that T^2VLA consistently
outperforms supervised baselines and approaches oracle RL performance with ground-truth
rewards, achieving effective improvement without external reward feedback. Furthermore,
T^2VLA adapts to distinct VLA paradigms, including both OpenVLA-OFT and the pi series.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29892v1
- Authors: Siyao Chen, Jiakang Yuan, Jiaxin Wang, Tao Chen
- Published: 2026-06-29T07:31:41Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
