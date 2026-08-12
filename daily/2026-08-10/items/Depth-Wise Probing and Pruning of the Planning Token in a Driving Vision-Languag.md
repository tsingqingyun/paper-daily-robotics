---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.07361v1"
published: "2026-08-07T16:02:34Z"
age_days: 2
score: 25
created: 2026-08-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Depth-Wise Probing and Pruning of the Planning Token in a Driving Vision-Language-Action Model

## 为什么重要

自动筛选分数：25

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-language-action (VLA) models route driving decisions through a deep language
model, but it is unclear how much of that depth the action itself requires. We study a
representative driving VLA whose entire plan is carried by a single planning token that
a generative planner decodes into a trajectory. Borrowing the planner as a trajectory-
space logit lens, we decode the planning token from every one of the 32 decoder layers
and measure two signals: the linear decodability of the navigation command and
trajectory compatibility with the frozen native planner. Our diagnostic shows that
semantic intent is linearly decodable early: command-probe accuracy reaches 97.7\% after
the first decoder layer, compared with 16.7\% chance. In contrast, compatibility with
the frozen native planner improves gradually across depth, with open-loop Avg-L2
reaching its minimum of 2.11\,m only at the final layer. Learned readouts from the first
layer recover much of this gap, indicating that planning information is already present
early but is not yet represented in the format expected by the deployed planner. Ranking
decoder layers by the angular deviation they induce in the planning token permits
removal of 8 of 32 layers within an approximately 5\% relative open-loop error increase
and yields a measured 1.33$\times$ decoder speedup. At the evaluated sample size, no
family-specific degradation is statistically resolved. These findings are limited to the
evaluated ORION checkpoint and Bench2Drive setup.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.07361v1
- Authors: Harisankar Babu, Benjamin Coors, Christopher Lang, Hendrik Berkemeyer, Tamim Asfour, Simon Foell
- Published: 2026-08-07T16:02:34Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
