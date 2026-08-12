---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10803v1"
published: "2026-06-09T12:49:11Z"
age_days: 0
score: 31
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use

> [!summary] 一句话结论（基于摘要）
> To address this gap, we introduce PhysTool-Bench, the first physical tool- use benchmark designed to evaluate MLLMs' ability to comprehend real-world scenarios, identify physical tools, and plan their use.

## 关键点

- **问题**：Despite the importance, MLLMs' proficiency in physical tool use remains largely unexplored.
- **创新点 / 方法**：To address this gap, we introduce PhysTool-Bench, the first physical tool- use benchmark designed to evaluate MLLMs' ability to comprehend real-world scenarios, identify physical tools, and plan their use.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/Beyond APIs Probing the Limits of MLLMs in Physical Tool Use.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

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

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10803v1
- Authors: Zhixin Ma, Yutong Zhou, Yongqi Li, Chong-Wah Ngo, Wenjie Li
- Published: 2026-06-09T12:49:11Z
- Age days: 0

</details>
