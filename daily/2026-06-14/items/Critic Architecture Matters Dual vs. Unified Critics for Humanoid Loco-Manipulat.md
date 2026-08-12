---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11891v1"
published: "2026-06-10T10:21:38Z"
age_days: 3
score: 27
created: 2026-06-14
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation

## 为什么重要

自动筛选分数：27

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Multi-objective reinforcement learning for humanoid robots must coordinate locomotion
and manipulation within a single policy. A natural design choice is whether to use a
single (unified) critic that estimates the combined value of all objectives, or separate
(dual) critics with disjoint reward signals. We present a controlled comparison on the
Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation
policies through a sequential curriculum spanning 13 levels from stationary reaching to
walking with variable-orientation targets. In standardized evaluation, dual-critic
policies reach targets 3.5$\times$ faster (6.5 vs. 22.6 simulation steps), achieve
2$\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain
higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy.
Notably, additional anti-gaming reward mechanisms provide no further improvement beyond
the architectural change alone (60.9% vs. 65.2%). These results have direct implications
for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining
a pre-trained manipulation policy with RL, a unified critic risks suppressing the
learned behavior through competing locomotion gradients. These findings demonstrate that
critic architecture is a primary - and often overlooked - design choice in multi-
objective humanoid RL, with greater impact than reward engineering on reaching
efficiency.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11891v1
- Authors: Mehmet Turan Yardımcı
- Published: 2026-06-10T10:21:38Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
