---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14199v1"
published: "2026-06-12T07:31:55Z"
age_days: 2
score: 27
created: 2026-06-15
concepts: ["多模态基础模型", "世界模型", "Sim2Real", "具身智能评测与基准"]
---

# OdysSim: Building Foundation Models for Human Behavior Simulation

> [!summary] 一句话结论（基于摘要）
> The resulting open 8B OSim model ranks first or tied-first on 8 of 23 tasks, outperforming any individual frontier model by this count, with the strongest gains on conversational and social tasks.

## 关键点

- **问题**：Large language models are increasingly deployed as human simulators for interactive evaluation and social simulation.
- **创新点 / 方法**：We present OdysSim, the largest open systematic investigation of behavioral foundation models, i.e., models trained to simulate human behavior at scale.
- **证据**：The resulting open 8B OSim model ranks first or tied-first on 8 of 23 tasks, outperforming any individual frontier model by this count, with the strongest gains on conversational and social tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large language models are increasingly deployed as human simulators for interactive
evaluation and social simulation. Yet helpfulness-driven post-training pulls them toward
a homogeneous, overly agreeable assistant register, creating a behavioral Sim2Real gap.
We present OdysSim, the largest open systematic investigation of behavioral foundation
models, i.e., models trained to simulate human behavior at scale. We propose SOUL, a
taxonomy of five capability axes (CONV, SS, COG, ROLE, EVAL) that unifies 62 datasets
and 23 benchmark tasks under one framework. Specifically, we curate the OdysSim corpus
(21.4M interactions, 10B tokens, retrofitted with back-generated social contexts),
construct the SOUL-Index benchmark, and develop an end-to-end training recipe combining
midtraining, task-specific RL, and expert distillation. The resulting open 8B OSim model
ranks first or tied-first on 8 of 23 tasks, outperforming any individual frontier model
by this count, with the strongest gains on conversational and social tasks. Its outputs
are also more human-like in length, formatting, and word choice, and it transfers zero-
shot to out-of-distribution user simulation on $τ$-bench, nearly matching real users on
reaction alignment (93.2 vs. 93.5). We further show that LLM-as-judge RL induces reward-
hacking patterns, and that our detectors can mitigate them during post-training.
Together, our findings suggest that behavioral foundation models require rethinking the
LLM training paradigm. We release all artifacts to support future research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14199v1
- Authors: Xuhui Zhou, Weiwei Sun, Weihua Du, Jiarui Liu, Haojia Sun, Qianou Ma, Tongshuang Wu, Yiming Yang, Maarten Sap
- Published: 2026-06-12T07:31:55Z
- Age days: 2

</details>
