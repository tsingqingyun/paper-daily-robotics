---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19971v1"
published: "2026-07-22T09:54:22Z"
age_days: 2
score: 27
created: 2026-07-25
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training

> [!summary] 一句话结论（基于摘要）
> To resolve this, we propose a novel model-merging- based framework, Disjoint Parameter Training (DPT).

## 关键点

- **问题**：However, within these compact shared encoders, recent unified models often overlook severe representational conflicts that arise from the distinct objectives of predicting neighbor behaviors versus ego-centric safety planning.
- **创新点 / 方法**：To resolve this, we propose a novel model-merging- based framework, Disjoint Parameter Training (DPT).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Accurate motion prediction of surrounding agents and safe motion planning are two
closely coupled key tasks for social robot navigation in crowded environments. Deploying
these systems on resource-constrained edge devices necessitates compact, unified models
that can perform both tasks simultaneously. However, within these compact shared
encoders, recent unified models often overlook severe representational conflicts that
arise from the distinct objectives of predicting neighbor behaviors versus ego-centric
safety planning. To address this issue, we first identify the Skill
Conflict$\unicode{x2014}$a phenomenon where overlapping parameter assignments cause
distinct tasks to compete for the same weights, preventing the model from fully
specializing in individual skills. To resolve this, we propose a novel model-merging-
based framework, Disjoint Parameter Training (DPT). DPT mitigates performance
degradation caused by Skill Conflict through distributed parameter learning, which
separates the key parameter regions of each task while preserving their core
capabilities prior to merging. In addition, we observe that sparse merging, which
selectively integrates only the most influential parameters for each task rather than
combining all task-specific parameters, yields optimal performance by preventing
interference among adjacent features and concentrating representational capacity. DPT
can be applied in parallel with a variety of merging methods. Evaluated on standard
crowd navigation benchmarks (JRDB and JTA), our framework demonstrates superior
performance, validating its versatility and effectiveness for safe, resource-efficient
robot navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19971v1
- Authors: Taewon Seo, Seonae Jeon, Giwon Lee, Kuk-Jin Yoon, Daehee Park
- Published: 2026-07-22T09:54:22Z
- Age days: 2

</details>
