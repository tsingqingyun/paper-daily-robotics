---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05588v1"
published: "2026-08-06T04:17:38Z"
age_days: 4
score: 26
created: 2026-08-10
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Lifelong Multi-Agent Path Finding (LMAPF) requires repeatedly planning collision-free
paths for agents that continuously receive new goals upon reaching their current ones.
While many learning-based planners have been proposed for LMAPF, most rely on
oversimplified kinematic assumptions that may overlook motion constraints critical to
real-world performance. In this work, we study a more realistic LMAPF model derived from
many real-world automated warehouse systems, termed LMAPF-R2, which incorporates robust
safety constraints and in-place rotation constraints. These constraints substantially
increase coordination difficulty, particularly in highly constrained spaces. To address
these challenges, we propose Search-Aided Joint Reinforcement Learning (SJRL). We first
augment neural policies with Causal PIBT, a single-step search-based planner that
resolves agents' collisions and propagates their intentions. We then introduce a unified
RL formulation that jointly optimizes agent and environment policies, where the
environment policy learns graph edge costs to provide global movement guidance via
backward Dijkstra search. Experiments demonstrate that SJRL achieves significant
improvements over the strong search-based planner, Causal-PIBT, across multiple high-
density maps. We further validate SJRL in a challenging mixed-reality warehouse
environment with 8 physical robots and 248 virtual robots.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05588v1
- Authors: He Jiang, Jingtian Yan, Yulun Zhang, Yimin Tang, Tanishq Duhan, Rishi Veerapaneni, Guillaume Sartoretti, Jiaoyang Li
- Published: 2026-08-06T04:17:38Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
