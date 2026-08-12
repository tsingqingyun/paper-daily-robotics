---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06721v1"
published: "2026-06-04T21:13:33Z"
age_days: 3
score: 28
created: 2026-06-08
concepts: ["智能体 Agent"]
---

# SCOUT: Semantic scene COverage via Uncertainty-guided Traversal

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]]

## 摘要

Robots that operate over extended periods should not merely visit space; they should
progressively understand it. Yet most 3D scene graph pipelines treat perception as a
post-processing stage over a fixed dataset, decoupling scene representation from the
decisions that determine what is observed in the first place. We present SCOUT, an
online semantic exploration framework that closes this loop by coupling active traversal
with probabilistic scene graph construction. Given a prior 2D occupancy map and posed
RGB-D observations, SCOUT incrementally builds an uncertainty-aware 3D scene graph whose
nodes maintain fused geometry and posterior beliefs over open-vocabulary object labels,
while edges encode structural relations such as on, inside, belong, and next to. These
beliefs are fed back to an uncertainty-guided traversal planner, which selects
viewpoints by balancing expected semantic certainty gain, geometric coverage gain, and
travel cost. In this way, the robot revisits ambiguous objects when additional evidence
matters and expands into unseen free space when the scene remains incomplete. The
resulting system treats semantic scene completeness as an operational objective rather
than a passive by-product of semantic mapping, moving toward autonomous agents that can
patrol, update, and reason about evolving indoor environments with minimal human
intervention.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06721v1
- Authors: Junyu Mao, Sara Ayoubi, Vishnu D. Sharma, Ilija Hadžić, Matthew Andrews
- Published: 2026-06-04T21:13:33Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
