---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00544v1"
published: "2026-07-01T07:35:12Z"
age_days: 5
score: 25
created: 2026-07-06
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# GEAR-Seg: A Grounded Explainable Agent for Reasoning Segmentation and Data Engine

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Reasoning segmentation requires localizing targets based on complex, implicit queries.
Current end-to-end models typically entangle perception and deduction into an opaque
black box, severely limiting interpretability and scalability. To address this, we
propose GEAR-Seg (Grounded Explainable Agent for Reasoning Segmentation), an explicitly
decoupled agent that shifts the paradigm by translating visual pixels into dense,
attribute-rich text. By decoupling class-agnostic segmentation, semantic description,
and Large Language Model (LLM) deduction, GEAR-Seg transforms implicit reasoning into an
explicit, trackable logic chain. As a zero-shot inference framework, it achieves highly
competitive performance across diverse reasoning and fine-grained referring segmentation
benchmarks. Furthermore, GEAR-Seg inherently functions as a highly scalable data engine.
Utilizing this engine, we construct GEAR-131K, a massive benchmark (over 38k images,
656k QA-mask pairs) introducing a multifaceted taxonomy tailored for complex real-world
manipulation-oriented reasoning. Finally, distillation experiments demonstrate that
lightweight models supervised exclusively by our automated pipeline closely match the
upper-bound performance of costly human-annotated baselines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00544v1
- Authors: Yanan Wang, Wen Li, Yibin Ying, Zhenghao Fei
- Published: 2026-07-01T07:35:12Z
- Age days: 5

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
