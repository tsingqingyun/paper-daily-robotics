---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00544v1"
published: "2026-07-01T07:35:12Z"
age_days: 5
score: 25
created: 2026-07-06
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# GEAR-Seg: A Grounded Explainable Agent for Reasoning Segmentation and Data Engine

> [!summary] 一句话结论（基于摘要）
> As a zero-shot inference framework, it achieves highly competitive performance across diverse reasoning and fine-grained referring segmentation benchmarks.

## 关键点

- **问题**：Current end-to-end models typically entangle perception and deduction into an opaque black box, severely limiting interpretability and scalability.
- **创新点 / 方法**：To address this, we propose GEAR-Seg (Grounded Explainable Agent for Reasoning Segmentation), an explicitly decoupled agent that shifts the paradigm by translating visual pixels into dense, attribute-rich text.
- **证据**：As a zero-shot inference framework, it achieves highly competitive performance across diverse reasoning and fine-grained referring segmentation benchmarks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

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

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00544v1
- Authors: Yanan Wang, Wen Li, Yibin Ying, Zhenghao Fei
- Published: 2026-07-01T07:35:12Z
- Age days: 5

</details>
