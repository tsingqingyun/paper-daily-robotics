---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23312v1"
published: "2026-06-22T13:26:17Z"
age_days: 1
score: 38
created: 2026-06-24
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Operating in complex real-world environments requires robots to understand their
surroundings on a functional semantic level. This demands a detailed multi-layer world
model capturing the complex relations of its surroundings. Hierarchical 3D scene graphs
address this challenge by integrating geometric, semantic, and relational data within a
unified spatial framework. However, current 3D scene graph approaches often restrict
themselves to rigid structures of pre-determined relationship classes, mostly neglecting
important semantic connections, like causal connections or environmental contexts. This
paper explores the potential of foundation models to build forests of 3D scene graphs
with open semantic relationships to improve scene understanding and robotic task
execution. We propose a method where instance-specific concept-nodes and relationships
are first identified by a VLM and extended upon by a LLM, inferring broader, more
abstract concept-nodes and relationships through reasoning. These object-nodes, concept-
nodes, and relationships are then assembled into a forest of hierarchical 3D scene
graphs, enhanced with concept-nodes to represent abstract concepts. Evaluations were
conducted on the uHumans2 and ScanNet indoor dataset, validating the accuracy and
relevance of the generated relationships. Downstream suitability of scene-graph forests
for robotics applications is demonstrated in an open-vocabulary object-retrieval task
utilizing both ScanNet data and a real-world indoor deployment using a Boston Dynamics
Spot. This paper leverages foundation models to create more expressive, semantically
deep 3D hierarchical scene graphs and demonstrates their potential to advance semantic
and environmental understanding in robotics.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23312v1
- Authors: David Oberacker, Meike Deitersen, Niklas Spielbauer, Tristan Schnell, Georg Heppner, Arne Roennau
- Published: 2026-06-22T13:26:17Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
