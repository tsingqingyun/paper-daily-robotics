---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06170v1"
published: "2026-08-06T15:36:12Z"
age_days: 3
score: 27
created: 2026-08-10
concepts: ["AI 核心知识地图"]
---

# Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured Environments

## 为什么重要

自动筛选分数：27

连接概念：[[AI 核心知识地图]]

## 摘要

Hierarchical 3D scene graphs are a promising representation for high-level spatial
reasoning in autonomous mobile platforms. However, existing extraction frameworks
typically rely on purely local visual clustering or strict geometric heuristics, such as
wall-separated rooms, which fail in open-plan or arbitrarily-structured environments. We
propose Prior-SG, a task- and prior-driven framework that casts scene graph generation
fundamentally as a probabilistic alignment problem. As the robot explores, it
continuously aggregates an incoming RGB-D sensor stream into a physically grounded
Instance Graph utilizing a multi-scale, open-vocabulary feature fusion strategy. The
system then infers the high-level functional semantics of this map through a Maximum A
Posteriori (MAP) estimate, guided by a Prior Graph-a logical expectation of the
environment's structure and task-relevant vocabulary synthesized dynamically by a Large
Language Model. By optimizing a Markov Random Field that fuses heterogeneous experts
(visual, geometric, and discrete objects) with these topological priors, the system
resolves local perceptual ambiguities. We validate this approach across diverse
simulated residential datasets and large, open-plan real-world environments. Prior-SG
achieves state-of-the-art semantic region segmentation accuracy compared to recent
baselines, robustly delineates distant functional boundaries in the absence of physical
walls, and uniquely provides zero-shot ontological flexibility, enabling the robot to
entirely restructure its spatial partitioning based on a given high-level task.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06170v1
- Authors: Giorgio Tonetti, Laurent Kneip, Abel Gawel, Marco Hutter
- Published: 2026-08-06T15:36:12Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
