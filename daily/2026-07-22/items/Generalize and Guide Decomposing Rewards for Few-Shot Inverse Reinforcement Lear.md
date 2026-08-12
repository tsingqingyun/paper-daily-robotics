---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17760v1"
published: "2026-07-20T09:51:02Z"
age_days: 1
score: 33
created: 2026-07-22
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Generalize and Guide: Decomposing Rewards for Few-Shot Inverse Reinforcement Learning

## 为什么重要

自动筛选分数：33

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Inverse reinforcement learning (IRL) provides a powerful framework for learning from
demonstrations. However, real-world tasks often exhibit substantial natural variations
(e.g., picking up mugs with varying shapes), making it impractical to collect
demonstrations that fully specify a new task under every possible scenario. In practice,
while demonstrations for the target task are limited, it is often easier to obtain
datasets of heterogeneous but related behaviors. This motivates the problem of few-shot
IRL with multi-task demonstrations (FM-IRL), where an agent must learn a new task with
substantial variations from only a limited number of target-task demonstrations,
together with sufficient demonstrations of related tasks and online agent experience. To
do so, we must both recover the expert distribution of the new task and provide guidance
when the agent deviates from it. We introduce Multitask discriminator Proximity-Guided
IRL (MPG), which learns two complementary reward components: (1) a generalizable
discriminator that transfers shared structure across related tasks to identify expert
behavior in a new task, and (2) a proximity function that measures how far a state
deviates from expert behavior and provides corrective guidance during exploration. We
demonstrate the effectiveness of our method on multiple challenging navigation and
manipulation tasks under significant variations (e.g., object configurations, table
layouts, and initial robot poses), achieving an average success rate of 81.2%,
outperforming the strongest per-task baseline by an average of 24.7 percentage points.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17760v1
- Authors: Ziyi Liu, Grace Zhang
- Published: 2026-07-20T09:51:02Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
