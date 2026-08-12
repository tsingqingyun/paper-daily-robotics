---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20376v1"
published: "2026-06-18T15:36:13Z"
age_days: 1
score: 35
created: 2026-06-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# CRAX: Fast Safe Reinforcement Learning Benchmarking

## 为什么重要

自动筛选分数：35

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Safety is a core concern for deploying reinforcement learning (RL) agents in real-world
domains such as robotics and autonomous driving. While benchmarks have been central to
progress in RL, existing safety benchmarks with high-fidelity 3D physics remain
computationally slow, limiting large-scale experimentation and rapid prototyping. To
address this gap, we propose CRAX (Constrained RL Accelerated with JAX). Built on top of
the MuJoCo XLA (MJX) physics engine with realistic 3D dynamics, CRAX leverages
vectorized operations and hardware acceleration, yielding up to ~100x speedups over
comparable CPU-based safety benchmarks. The benchmark features six environment suites
and three agent-specific tasks, each spanning three difficulty levels. Evaluating six
popular safe RL methods shows that no single approach dominates across all tasks, and
reveals the trade-offs between performance and safety. We find that curriculum learning
across difficulty levels and safety transfer can improve performance over direct
training in harder settings.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20376v1
- Authors: Tristan Tomilin, Mourad Boustani, Mickey Beurskens, Thiago D. Simão
- Published: 2026-06-18T15:36:13Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
