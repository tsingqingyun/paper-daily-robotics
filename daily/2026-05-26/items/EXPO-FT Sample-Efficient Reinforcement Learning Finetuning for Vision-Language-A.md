---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25477v1"
published: "2026-05-25T06:31:03Z"
age_days: 1
score: 44
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

## 为什么重要

自动筛选分数：44

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

The ability to efficiently and reliably learn new tasks has been a foundational
challenge in robotics. Vision-Language-Action (VLA) models have demonstrated strong
generalization across diverse manipulation tasks, yet pretrained policies consistently
fall short of the reliability required for real-world deployment. Reinforcement learning
(RL) fine-tuning offers a promising path to bridge this gap, but existing approaches
either train from scratch without fully leveraging pretrained priors, or fine-tune VLAs
without achieving the sample efficiency and success rates that practical deployment
demands. We present EXPO-FT, a system for stable, sample-efficient RL finetuning of
pretrained VLA policies that closes this gap. Our system solves a suite of challenging
manipulation tasks, including routing string lights and inserting the plug to light it
up, striking a pool ball into a pocket, and inserting a flower into a wine bottle, each
requiring combinations of high precision, dynamic actions, and robustness to varied
initial states. Our system achieves perfect task performance (30/30 successes) across
all evaluated tasks within an average of 19.1 minutes of online robot data,
outperforming both prior RL-from-scratch and VLA finetuning approaches. We release an
open-source codebase with the aim of facilitating broader adoption of RL finetuning of
VLA models in robotics.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25477v1
- Authors: Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn
- Published: 2026-05-25T06:31:03Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
