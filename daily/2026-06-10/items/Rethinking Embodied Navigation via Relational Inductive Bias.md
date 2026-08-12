---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10348v1"
published: "2026-06-09T02:57:34Z"
age_days: 0
score: 30
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Rethinking Embodied Navigation via Relational Inductive Bias

> [!summary] 一句话结论（基于摘要）
> Experiments on ObjectNav benchmarks show that DB-Nav significantly outperforms existing methods in success rate (SR) and Success weighted by Path Length (SPL), offering a lightweight, interpretable, and robust navigation framework without costly online VLM re…

## 关键点

- **问题**：Open-vocabulary perception is prone to systematic misleading evidence: false positives, outdated static priors, and repeated failed exploration due to lack of embodied verification, which contaminates mapping and decision-making.
- **创新点 / 方法**：To address this, we propose DB-Nav, a framework that reshapes the search space via dual relational biases.
- **证据**：Experiments on ObjectNav benchmarks show that DB-Nav significantly outperforms existing methods in success rate (SR) and Success weighted by Path Length (SPL), offering a lightweight, interpretable, and robust navigation framework without costly online VLM reasoning.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/Rethinking Embodied Navigation via Relational Inductive Bias.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object navigation requires an agent to locate a target in an unknown environment through
visual observations. Existing methods typically rely on open-vocabulary detectors or
vision-language models (VLMs) to answer where to search, but often overlook what not to
trust - which semantic cues are unreliable. Open-vocabulary perception is prone to
systematic misleading evidence: false positives, outdated static priors, and repeated
failed exploration due to lack of embodied verification, which contaminates mapping and
decision-making. Such errors are rooted in structured object relations in real-world
scenes. To address this, we propose DB-Nav, a framework that reshapes the search space
via dual relational biases. It factorizes target-centric relations into an Activation
Bias (propagates contextual evidence) and an Inhibition Bias (suppresses unreliable
regions via perceptual confusion and action-level falsification). These biases are
unified into a Relational Activation-Inhibition Exploration Graph that modulates
frontier exploration values using online observations and failed accesses. Experiments
on ObjectNav benchmarks show that DB-Nav significantly outperforms existing methods in
success rate (SR) and Success weighted by Path Length (SPL), offering a lightweight,
interpretable, and robust navigation framework without costly online VLM reasoning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10348v1
- Authors: Weitao An, Chenghao Xu, Xu Yang, Cheng Deng
- Published: 2026-06-09T02:57:34Z
- Age days: 0

</details>
