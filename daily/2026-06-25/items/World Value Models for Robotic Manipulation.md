---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24742v1"
published: "2026-06-23T16:07:48Z"
age_days: 1
score: 38
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# World Value Models for Robotic Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Generalist value models play a pivotal role in scaling robotic policy learning from
large-scale, mixed-quality data. Mathematically, accurate value estimation demands deep
temporal understanding, requiring models to both ground the current belief using
historical context and plan over future outcomes. However, most existing robotic value
models are built on Vision-Language Model (VLM) backbones that are pretrained primarily
on static or temporally sparse visual observations, lacking the requisite temporal
modeling capabilities for value estimation. Unlike VLMs, world models naturally excel at
temporal modeling and future planning, making them ideal foundations for learning
generalizable value functions. Driven by this insight, we marry world models with value
estimation to construct a new generalist robotic value model, World Value Model (WVM),
that offers accurate task progressions to assess data quality. On standard benchmarks,
WVM delivers state-of-the-art (SOTA) Value-Order Correlation (VOC) results.
Complementing standard evaluation suites that contains only expert data, we further
introduce Suboptimal-Value-Bench, a multi-embodiment benchmark consisting of 800
suboptimal trajectories with high-fidelity, human-labeled frame annotations. Our
evaluations show that WVM maintains its SOTA performance on Suboptimal-Value-Bench,
establishing its robustness in handling both expert and suboptimal data. When deployed
for policy learning, WVM improves manipulation performance across various policy
extraction approaches in both simulated and real-world deployment, providing robust
guidance for learning from mixed-quality data.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24742v1
- Authors: Zhihao Wang, Jianxiong Li, Yu Cui, Yuan Gao, Xianyuan Zhan, Junzhi Yu, Xiao Ma
- Published: 2026-06-23T16:07:48Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
