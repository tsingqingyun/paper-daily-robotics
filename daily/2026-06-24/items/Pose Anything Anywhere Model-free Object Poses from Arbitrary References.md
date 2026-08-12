---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23634v1"
published: "2026-06-22T17:23:57Z"
age_days: 1
score: 32
created: 2026-06-24
concepts: ["世界模型", "具身智能评测与基准"]
---

# Pose Anything Anywhere:Model-free Object Poses from Arbitrary References

## 为什么重要

自动筛选分数：32

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

Estimating the 6D pose of unseen objects is a fundamental yet challenging problem for
open-world robotics and embodied perception. Model-based methods are accurate but depend
on CAD assets or heavy onboarding, while most model-free approaches are still limited to
pairwise single-anchor matching and thus fail under occlusion and large viewpoint
changes with low query-reference overlap. Therefore, we present PANY, a unified model-
free framework that seamlessly supports both RGB and RGB-D inputs, operates on one or
sparse pose-free reference views, and generalizes effectively to novel objects. Built on
a multi-view transformer geometry backbone, PANY moves beyond pairwise matching by
learning view-consistent geometry and cross-view alignment cues that remain stable under
wide baselines and limited overlap. When additional unposed assist views are available,
PANY aggregates them via pose-graph canonical registration to increase geometric
coverage and reinforce the final pose. Extensive experiments show that PANY achieves
state-of-the-art performance across multiple benchmarks, substantially outperforming
existing model-free methods, improving pose accuracy by +12% on YCB-V and over +20% on
LM-O. Furthermore, PANY consistently performs well under both single-reference and
sparse-reference settings, demonstrating strong robustness in real-world environments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23634v1
- Authors: Hongli Xu, Jiaqi Hu, Junwen Huang, Boyang Zhong, Peter KT Yu, Nassir Navab, Benjamin Busam, Slobodan Ilic
- Published: 2026-06-22T17:23:57Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
