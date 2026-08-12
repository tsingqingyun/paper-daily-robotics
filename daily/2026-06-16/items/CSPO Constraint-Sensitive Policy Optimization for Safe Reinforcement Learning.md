---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14415v1"
published: "2026-06-12T12:48:56Z"
age_days: 3
score: 21
created: 2026-06-16
concepts: ["机器人学习", "具身智能评测与基准"]
---

# CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning

## 为什么重要

自动筛选分数：21

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Safe reinforcement learning (Safe RL) aims to maximize expected return while satisfying
safety constraints, typically modeled as Constrained Markov Decision Processes (CMDPs).
While primal-dual methods scale well to deep RL, they often suffer from delayed
constraint correction, leading to oscillatory behavior and prolonged safety violations.
In this paper, we propose Constraint-Sensitive Policy Optimization (CSPO), a first-order
primal-dual method that incorporates local constraint sensitivity into policy updates.
CSPO augments the primal objective with a constraint-sensitive correction derived from
the shortest signed distance to the safety boundary, enabling smarter recovery steps
back to safety, compensating for delayed Lagrange multiplier updates, reducing
oscillations near the boundary, and preserving the KKT solutions of the original
constrained problem. Experiments on navigation and locomotion benchmarks demonstrate
that CSPO achieves faster safety recovery and high reward preservation, resulting in
higher constrained returns compared to state-of-the-art primal-dual and penalty-based
methods

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14415v1
- Authors: Ayoub Belouadah, Sylvain Kubler, Yves Le Traon
- Published: 2026-06-12T12:48:56Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
