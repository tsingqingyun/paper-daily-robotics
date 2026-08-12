---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13675v1"
published: "2026-06-11T17:59:45Z"
age_days: 1
score: 30
created: 2026-06-13
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# Improving Robotic Generalist Policies via Flow Reversal Steering

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Generalist policies can learn a wide range of skills from diverse robot datasets. In
order to solve or improve on challenging news tasks, we need a way to infer and invoke
the appropriate actions from the policy's rich behavioral prior, especially when
directly commanding the policy fails. We focus on flow matching generalists and propose
Flow Reversal Steering (FRS): a method that takes suboptimal but ``reasonable'' actions,
finds their latent noises by passing them through the flow policy in reverse, and maps
them to nearby generalist action modes. We evaluate FRS across many simulated and real-
world manipulation settings. First, FRS can turn coarse semantic guidance from humans or
vision-language models (VLMs) into corresponding good robot actions, improving zero-shot
control. These gains can be distilled with behavioral cloning by training an auxiliary
policy to output noises that the generalist maps to good actions -- showing up to 95%
absolute task success rate boosts in under a minute of training. Finally, FRS enables
policy improvement by bootstrapping reinforcement learning with semantic knowledge,
improving on several tasks that standard RL fails to improve on.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13675v1
- Authors: Andy Tang, William Chen, Andrew Wagenmaker, Chelsea Finn, Sergey Levine
- Published: 2026-06-11T17:59:45Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
