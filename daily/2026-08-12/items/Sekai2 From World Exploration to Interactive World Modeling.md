---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09449v1"
published: "2026-08-10T11:23:01Z"
age_days: 1
score: 24
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型"]
---

# Sekai2: From World Exploration to Interactive World Modeling

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Video world models must capture how scenes evolve over time and across viewpoints.
Training them for long-horizon generation and camera control therefore benefits from
long videos paired with camera trajectories and temporally grounded semantics. Existing
corpora rarely offer the three together: large-scale web video provides broad visual
diversity but no trajectories or time-aligned text, while pose-annotated datasets are
typically short-range or reconstruction-oriented. We introduce Sekai2, a multi-source
real-world video dataset that carries the world-exploration footage of Sekai toward
interactive world modeling. The release contains 128,892 clips totaling 2,826 hours from
10,428 source videos across 113 countries or regions, and is deliberately weighted
toward sustained observation: under a common 120-second decomposition, 43,594 segments
reach the full two minutes and account for 51.4% of all footage. Every clip includes a
released camera trajectory and hierarchical annotations disentangling subject motion,
environment dynamics, static scene content, and camera behavior, resulting in 649,597
temporally grounded segments. Crucially, we further introduce 982 panoramic sequences
captured along non-linear trajectories with loops and revisits. These revisits provide
repeated observations of the same locations across time and viewpoints, offering
essential supervision for learning persistent scene representations, long-term spatial
memory, and geometrically consistent world models. Corpus-scale analyses demonstrate
complete pose-and-caption coverage, broad geographic and semantic diversity, varied
camera trajectories, and highly non-redundant temporal descriptions. Together, these
properties make Sekai2 a scalable resource for long-horizon video generation, camera-
controllable synthesis, and interactive world-model pre-training.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09449v1
- Authors: Kang He, Wenshuo Peng, Zihui Gao, Jiaming Tan, Kaipeng Zhang, Yongtao Ge
- Published: 2026-08-10T11:23:01Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
