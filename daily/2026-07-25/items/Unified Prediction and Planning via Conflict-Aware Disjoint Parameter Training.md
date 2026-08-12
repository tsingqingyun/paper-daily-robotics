---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19971v1"
published: "2026-07-22T09:54:22Z"
age_days: 2
score: 27
created: 2026-07-25
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training

## 为什么重要

自动筛选分数：27

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Accurate motion prediction of surrounding agents and safe motion planning are two
closely coupled key tasks for social robot navigation in crowded environments. Deploying
these systems on resource-constrained edge devices necessitates compact, unified models
that can perform both tasks simultaneously. However, within these compact shared
encoders, recent unified models often overlook severe representational conflicts that
arise from the distinct objectives of predicting neighbor behaviors versus ego-centric
safety planning. To address this issue, we first identify the Skill
Conflict$\unicode{x2014}$a phenomenon where overlapping parameter assignments cause
distinct tasks to compete for the same weights, preventing the model from fully
specializing in individual skills. To resolve this, we propose a novel model-merging-
based framework, Disjoint Parameter Training (DPT). DPT mitigates performance
degradation caused by Skill Conflict through distributed parameter learning, which
separates the key parameter regions of each task while preserving their core
capabilities prior to merging. In addition, we observe that sparse merging, which
selectively integrates only the most influential parameters for each task rather than
combining all task-specific parameters, yields optimal performance by preventing
interference among adjacent features and concentrating representational capacity. DPT
can be applied in parallel with a variety of merging methods. Evaluated on standard
crowd navigation benchmarks (JRDB and JTA), our framework demonstrates superior
performance, validating its versatility and effectiveness for safe, resource-efficient
robot navigation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19971v1
- Authors: Taewon Seo, Seonae Jeon, Giwon Lee, Kuk-Jin Yoon, Daehee Park
- Published: 2026-07-22T09:54:22Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
