---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19243v1"
published: "2026-07-21T16:15:05Z"
age_days: 3
score: 26
created: 2026-07-25
concepts: ["具身智能评测与基准"]
---

# Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs

> [!summary] 一句话结论（基于摘要）
> These findings suggest that cross-lingual inconsistency is at least partly a selection problem, and that simple contextual interventions may outperform more invasive methods for robust, transferable alignment.

## 关键点

- **问题**：Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their internal knowledge representations remain disproportionately biased toward high-resource languages.
- **创新点 / 方法**：This leads to cross-lingual factual inconsistency, where they shift their empirical answer distributions based solely on the prompt language.
- **证据**：These findings suggest that cross-lingual inconsistency is at least partly a selection problem, and that simple contextual interventions may outperform more invasive methods for robust, transferable alignment.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their
internal knowledge representations remain disproportionately biased toward high-resource
languages. This leads to cross-lingual factual inconsistency, where they shift their
empirical answer distributions based solely on the prompt language. We investigate
whether these biases can be mitigated at inference time, forcing an English-prompted
model to answer as if it were queried in target languages (German, Spanish, Bulgarian),
and evaluate four intervention strategies: zero-shot contextual steering (persona
prompting), internal representation manipulation via Contrastive Activation Addition
(CAA), and lightweight weight modification via Direct Preference Optimization (DPO)
trained on benchmark-derived factual data as well as conceptual generalization data. To
assess alignment, we curate a multilingual factual dataset alongside a novel
generalization benchmark comprising culturally rooted queries to determine whether
factual interventions transfer to broader target-centric preferences. Experiments on
Gemma 3 12B Instruct reveal persona prompting to be the strongest overall intervention,
balancing efficacy, safety, and out-of-domain generalization. While CAA yields sharp
inconsistency benchmark shifts, it is configuration-sensitive and risks knowledge
degradation. DPO-based adapters offer permanent, yet narrower and less transferable
gains. These findings suggest that cross-lingual inconsistency is at least partly a
selection problem, and that simple contextual interventions may outperform more invasive
methods for robust, transferable alignment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19243v1
- Authors: Alexander Manev
- Published: 2026-07-21T16:15:05Z
- Age days: 3

</details>
