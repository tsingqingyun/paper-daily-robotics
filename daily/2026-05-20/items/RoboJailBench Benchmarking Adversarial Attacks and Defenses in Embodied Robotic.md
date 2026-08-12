---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19328v1"
published: "2026-05-19T04:07:24Z"
age_days: 0
score: 38
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Recent advances in Vision-Language Models (VLMs) facilitate a new class of embodied AI
systems, where these models are integrated into physical platforms, e.g. robots and
autonomous vehicles, to interpret visual scenes and execute natural language commands in
diverse environments. Previous research has introduced jailbreak attacks and defenses
for embodied AI. Their evaluations, however, rely on ad-hoc datasets, limited metrics,
and emphasize attack success while neglecting the trade-off between security and the
ability to follow benign commands. Existing benchmarks and evaluation frameworks either
target traditional chat-based models or focus on non-adversarial safety evaluation for
embodied AI; neither captures the adversarial risks, inputs, consequences, and
evaluation criteria necessary for jailbreak attacks in embodied AI systems. In this
paper, we address this gap with RoboJailBench, which consists of three core components.
We establish a security taxonomy derived from ISO standards, regulatory rules, and
documented incidents. This effort yields 18 categories of security violation
consequences for embodied AI. We introduce an intent contrast dataset pipeline that
augments existing datasets with paired adversarial and benign goals to measure both
security and utility. Lastly, we provide an evolving repository with standardized
metrics and a unified process for assessing and integrating new attacks and defenses.
With this benchmark, we construct a new taxonomy-balanced dataset and augment five
existing datasets. We integrate four attacks and two defenses to evaluate their
performance on leading embodied VLMs. This benchmark provides the first standardized
evaluation framework for jailbreak attacks in embodied AI and supports future research.
We release our code, datasets, and artifacts, and maintain a leaderboard at
https://purseclab.github.io/benchmark-for-robotics-security.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19328v1
- Authors: Doguhuan Yeke, Yanming Zhou, Leo Y. Lin, Hongyu Cai, Antonio Bianchi, Z. Berkay Celik
- Published: 2026-05-19T04:07:24Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
