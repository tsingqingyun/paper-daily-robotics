---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12365v1"
published: "2026-06-10T17:34:12Z"
age_days: 3
score: 28
created: 2026-06-14
concepts: ["机器人学习", "Sim2Real"]
---

# Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics

## 为什么重要

自动筛选分数：28

连接概念：[[机器人学习]], [[Sim2Real]]

## 摘要

We propose Ambient Diffusion Policy, a simple and principled method for imitation
learning from suboptimal data in robotics. High-quality, task-specific robot data is
expensive and time-consuming to collect, while suboptimal datasets with lower-quality or
out-of-distribution demonstrations are abundant. Existing methods that co-train on both
data sources in robotics often fail to separate the meaningful and the harmful features
in the suboptimal samples. In contrast, our method extracts only the useful features by
introducing a new axis to co-training in robotics: noise-dependent data usage. Ambient
Diffusion Policy restricts the contribution of suboptimal data during training to only
the high and low diffusion times. To rigorously justify our approach, we first observe
that robot action data exhibits a spectral power law. This induces two important
properties on the optimal Diffusion Policy that we exploit: a global-to-local hierarchy
and locality. We theoretically formalize this discussion using a simplified model. Our
experiments validate Ambient Diffusion Policy on four types of suboptimal action data
(noisy trajectories, sim-to-real gap, task mismatch, and large-scale data mixtures)
across six tasks. The results show that it effectively learns from arbitrary sources of
suboptimal data. Notably, it outperforms existing co-training baselines by up to 33%
when scaled to Open X-Embodiment - a large dataset with heterogeneous data quality and
unstructured distribution shifts. Overall, Ambient Diffusion Policy increases the
utility of suboptimal demonstrations and expands the set of usable data sources in
robotics.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12365v1
- Authors: Adam Wei, Nicholas Pfaff, Thomas Cohn, Arif Kerem Dayı, Constantinos Daskalakis, Giannis Daras, Russ Tedrake
- Published: 2026-06-10T17:34:12Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
