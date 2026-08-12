---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06917v1"
published: "2026-08-07T07:51:08Z"
age_days: 3
score: 25
created: 2026-08-10
concepts: ["多模态基础模型", "智能体 Agent"]
---

# ReGraph: Learning to Generate Recipe Graphs from Food Images

## 为什么重要

自动筛选分数：25

连接概念：[[多模态基础模型]], [[智能体 Agent]]

## 摘要

Recent Large Multimodal Models (LMMs) have achieved impressive performance in recipe
generation from food images.However, cooking is a structured transformation process in
which ingredients undergo state changes through ordered actions,while free-form recipe
language leaves the corresponding entities, intermediate states, and dependencies
largely implicit and entangled.A graph representation makes this procedural knowledge
explicit and compositional, providing a structured basis for assessing whether model
outputs encode process-level knowledge rather than merely presenting plausible textual
descriptions. To address this limitation, we present ReGraph, a large-scale recipe graph
dataset that represents ingredients, cooking actions, and tools as entities, uses entity
attributes to describe ingredient state changes, and employs typed relations to encode
manipulation targets, destinations, and procedural ordering. ReGraph further
incorporates explicit Recipe Reasoning Chain-of-Thought (RR-CoT) traces, providing
auxiliary supervision for procedural decomposition and structured graph generation.
Building on ReGraph, we propose Recipe Graph Learning (RGL), a two-stage framework that
enables LMMs to generate a plausible fine-grained cooking workflow from a food image in
the form of a structured recipe graph. Under a deterministic, schema-aware matching
protocol, our experiments reveal a substantial gap between text-generation quality and
recoverable procedural structure: recipes produced by existing approaches achieve
competitive text-generation scores yet yield limited reference-aligned entity and
relation structure under the ReGraph schema. In contrast, across two representative LMM
backbones, RGL consistently improves the generation of cooking entities and procedural
relations, while our analysis further shows that fine-grained ingredient-state capture
remains the most challenging dimension.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06917v1
- Authors: Guoshan Liu, Bin Zhu, Pengkun Jiao, Jingjing Chen, Chong-Wah Ngo, Yu-Gang Jiang
- Published: 2026-08-07T07:51:08Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
