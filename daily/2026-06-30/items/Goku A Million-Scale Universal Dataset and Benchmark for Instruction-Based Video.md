---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30599v1"
published: "2026-06-29T17:38:15Z"
age_days: 0
score: 30
created: 2026-06-30
concepts: ["具身智能评测与基准"]
---

# Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing

> [!summary] 一句话结论（基于摘要）
> To bridge this gap, we present Goku, a large-scale dataset featuring 2 million high-quality, instruction-aligned video editing pairs, which is the first to extend task boundaries from basic appearance editing to multi-task and structural manipulations(e.g., p…

## 关键点

- **问题**：To tackle the data synthesis challenges inherent in these complex tasks, we design an efficient data synthesis pipeline that decomposes complex edits into controllable sub-problems and introduce a progressive filtering system for data reliability throughout the whole process.
- **创新点 / 方法**：To bridge this gap, we present Goku, a large-scale dataset featuring 2 million high-quality, instruction-aligned video editing pairs, which is the first to extend task boundaries from basic appearance editing to multi-task and structural manipulations(e.g., precise control of subject movement).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/Goku A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Existing instruction-based video editing datasets commonly focus on single-task
appearance editing, failing to meet the complex creative demands of real-world
scenarios. To bridge this gap, we present Goku, a large-scale dataset featuring 2
million high-quality, instruction-aligned video editing pairs, which is the first to
extend task boundaries from basic appearance editing to multi-task and structural
manipulations(e.g., precise control of subject movement). To tackle the data synthesis
challenges inherent in these complex tasks, we design an efficient data synthesis
pipeline that decomposes complex edits into controllable sub-problems and introduce a
progressive filtering system for data reliability throughout the whole process.
Furthermore, we explore the optimal network structures on Goku, and propose Goku-Edit.
To deeply comprehend complex editing instructions, Goku-Edit leverages an MLLM as its
text encoder and adopts a decoupled dual-branch design: a dedicated mask branch handles
structural control, freeing the main branch for appearance rendering. A comprehensive
video editing benchmark, Goku-Bench, is also proposed with 1,000 human-verified test
cases and 7 novel editing-specific metrics. Evaluated on Goku-Bench, Goku-Edit obtains
up to +8% improvement on other open-source models in terms of instruction following.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30599v1
- Authors: Sen Liang, Cong Wang, Zhentao Yu, Fengbin Guan, Zhengguang Zhou, Teng Hu, Youliang Zhang, Yuan Zhou, Xin Li, Qinglin Lu, Zhibo Chen
- Published: 2026-06-29T17:38:15Z
- Age days: 0

</details>
