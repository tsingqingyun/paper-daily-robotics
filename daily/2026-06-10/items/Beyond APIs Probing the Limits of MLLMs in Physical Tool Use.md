---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10803v1"
published: "2026-06-09T12:49:11Z"
age_days: 0
score: 31
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Multimodal Large Language Models (MLLMs) excel at utilizing digital APIs and
increasingly serve as the "brain" of embodied AI, instructing robots to interact with
the physical world. In such embodied settings, a central capability is the use of
physical tools, which underpins MLLMs' ability to assist humans in real-world tasks.
Despite the importance, MLLMs' proficiency in physical tool use remains largely
unexplored. To address this gap, we introduce PhysTool-Bench, the first physical tool-
use benchmark designed to evaluate MLLMs' ability to comprehend real-world scenarios,
identify physical tools, and plan their use. PhysTool-Bench comprises 2,510 queries over
2,678 real-world physical tools spanning diverse domains, including manufacturing,
electrical work, agriculture, and healthcare. Concretely, models are evaluated along two
primary dimensions: 1) recognizing all physical tools present in the scene, and 2)
planning the tool selection and use sequence based on the instruction and visual
context. Across 13 leading MLLMs, even the strongest model (Gemini-3.1-Pro) identifies
only 58.7% of tools in a scene and completes merely 21.0% of queries end-to-end. Our
analysis reveals a two-level deficit: MLLMs struggle to perceive tools in realistic
scenes, and the much larger drop at the planning stage further indicates a lack of
functional commonsense for mapping perceived tools onto task semantics, pinpointing a
critical bottleneck for the development of practical embodied AI.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10803v1
- Authors: Zhixin Ma, Yutong Zhou, Yongqi Li, Chong-Wah Ngo, Wenjie Li
- Published: 2026-06-09T12:49:11Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
