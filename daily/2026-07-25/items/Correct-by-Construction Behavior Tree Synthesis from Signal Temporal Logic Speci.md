---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18731v1"
published: "2026-07-21T05:43:19Z"
age_days: 3
score: 24
created: 2026-07-25
concepts: ["世界模型", "具身智能评测与基准"]
---

# Correct-by-Construction Behavior Tree Synthesis from Signal Temporal Logic Specifications with Application to Robotic Missions

## 为什么重要

自动筛选分数：24

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

Behavior Trees (BTs) are widely adopted for complex task execution in robotics,
providing modular, reactive control but lacking formal guarantees. However, existing
correct-by-construction synthesis from Linear Temporal Logic (LTL) cannot express
quantitative timing constraints. This letter synthesizes correct-by-construction BTs
from Signal Temporal Logic (STL) specifications. The workspace is modeled as a timed
transition system and abstracted into a zone graph, and an augmented state space
tracking both logical progress and timing constraints is introduced. A hierarchical
fixed-point algorithm computes winning sets for an STL fragment encompassing safety,
reachability, response, recurrence, and persistence, yielding BT subtrees with a runtime
constraint function. Correctness guarantees are proven and complexity bounds are
derived. Simulations demonstrate specification satisfaction with strictly positive
robustness, and a physical quadrotor experiment with six STL specifications validates
practical deployability.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18731v1
- Authors: Jiaheng Dong, Jingyi Huang, Liang Han
- Published: 2026-07-21T05:43:19Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
