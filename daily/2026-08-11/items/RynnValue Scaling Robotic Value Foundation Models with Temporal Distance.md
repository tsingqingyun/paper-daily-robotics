---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09853v1"
published: "2026-08-10T17:09:37Z"
age_days: 0
score: 35
created: 2026-08-11
concepts: ["多模态基础模型", "机器人学习"]
---

# RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[机器人学习]]

## 摘要

General-purpose reward models are increasingly the bottleneck for scaling robot
learning, yet the recipe for learning value-related capabilities from large-scale
heterogeneous corpora remains underexplored. Existing approaches tie supervision to
task-internal anchors such as preferences or normalized progress, none of which transfer
cleanly across embodiments and data sources. We introduce RynnValue, an open-source
value foundation model for robotic manipulation that replaces these anchors with
temporal distance, the directed cost-to-go from an observation to the language-specified
goal. Because temporal-distance labels can be derived directly from timestamps,
RynnValue scales to over 7,000 hours and roughly 3M instruction-conditioned clips
without preference or progress annotations. To make temporal-value learning reliable at
scale, we combine random temporal sampling, temporal-order shuffling, and value-
isolation attention, suppressing shortcuts that would leave predictions insensitive to
failures and regressions. Trained without preference labels, RynnValue attains an
average Kendall's tau_a of 0.675 on RBM-EVAL-OOD, surpassing the fully preference-
supervised state of the art (0.655) and more than doubling a progress-only counterpart
(0.292), while generalizing zero-shot to unseen tasks, embodiments, and viewpoints.
Converted into dense rewards via potential-based shaping, it raises real-world policy
success from 52.5% to 72.5% online and from 63.8% to 82.5% offline. These results
establish temporal distance as a scalable supervision target and practical reward
interface for generalist robot policies.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09853v1
- Authors: Dongchi Huang, Hongyin Zhang, Bohan Hou, Siteng Huang, Zhian Su, Hang Guo, Tong Lu, Zhaofeng Xu, Jiahao Tang, Jianfei Yang, Donglin Wang, Peixi Peng, Mingxiu Chen, Deli Zhao, Xin Li
- Published: 2026-08-10T17:09:37Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
