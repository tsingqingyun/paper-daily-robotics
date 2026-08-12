---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02403v1"
published: "2026-07-02T16:38:10Z"
age_days: 3
score: 26
created: 2026-07-06
concepts: ["智能体 Agent", "世界模型"]
---

# ACID: Action Consistency via Inverse Dynamics for Planning with World Models

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Decision-time planning with action-conditioned world models has become a popular
paradigm for embodied control. However, the standard planning cost judges a candidate
solely by how close its predicted terminal state lies to the goal, leaving the
realizability of the intermediate transitions unchecked -- a predicted trajectory can
look convincing while the environment rollout drifts away from it. In this paper, we
propose ACID, a decision-time planning framework that introduces cycle action
consistency: the action inferred backward from a predicted transition by an inverse
dynamics model should recover the one that was conditioned on. We fold this per-step
residual into the planning cost via a scale-invariant adaptive weight. Across four
action-conditioned world models and six tasks spanning rigid and deformable
manipulation, articulated control, and visual navigation, ACID consistently improves
planning and matches the baseline's accuracy with substantially less planning compute.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02403v1
- Authors: Gawon Seo, Dongwon Kim, Suha Kwak
- Published: 2026-07-02T16:38:10Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
