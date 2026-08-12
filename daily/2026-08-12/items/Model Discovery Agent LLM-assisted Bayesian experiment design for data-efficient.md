---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09696v1"
published: "2026-08-10T14:59:22Z"
age_days: 1
score: 25
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models

> [!summary] 一句话结论（基于摘要）
> On three different benchmarks --- covering physics (\DPbench, \citep{wiemann2026discoverphysics}), chemistry (\CHEMbench, \citep{kabra2026autoscilab}) and biology (\HHbench, a new partially observed single-neuron electrophysiology benchmark we create) --- we…

## 关键点

- **问题**：Experiments are expensive, so the central problem is \emph{data efficiency}.
- **创新点 / 方法**：We present the Model Discovery Agent (MDA), which couples a large language model (LLM), used as a \emph{proposer} of candidate structures, with standard Bayesian machinery --- sequential Monte Carlo (SMC) for parameter and structure posteriors, simulation-based inference (SBI) for intractable likelihoods, and value-of…
- **证据**：On three different benchmarks --- covering physics (\DPbench, \citep{wiemann2026discoverphysics}), chemistry (\CHEMbench, \citep{kabra2026autoscilab}) and biology (\HHbench, a new partially observed single-neuron electrophysiology benchmark we create) --- we show that MDA sets a new SOTA in terms of data-efficient mod…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/Model Discovery Agent LLM-assisted Bayesian experiment design for data-efficient.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Predicting the answer to interventional ``what if'' questions --- the outcome of an
action never taken --- requires a \emph{mechanistic}, causal model, not a curve fit; and
learning such a model requires \emph{experiments}, because passive data leaves its
mechanisms unidentified. Experiments are expensive, so the central problem is \emph{data
efficiency}. We present the Model Discovery Agent (MDA), which couples a large language
model (LLM), used as a \emph{proposer} of candidate structures, with standard Bayesian
machinery --- sequential Monte Carlo (SMC) for parameter and structure posteriors,
simulation-based inference (SBI) for intractable likelihoods, and value-of-information
(VoI) for experiment design --- to discover latent mechanistic world models from few
interventions. MDA operates in the M-open setting: when the truth lies outside the
current hypothesis class, a predictive check flags the inadequacy and the proposer
expands the hypothesis space with a new model whose parameters are then identified by
designed experiments. We show that \emph{discovery and design reinforce}: the design
step identifies the mechanism the discovery step proposes, and the identified mechanism
improves predictions, enabling further discoveries from the remaining unexplained
residuals. On three different benchmarks --- covering physics (\DPbench,
\citep{wiemann2026discoverphysics}), chemistry (\CHEMbench, \citep{kabra2026autoscilab})
and biology (\HHbench, a new partially observed single-neuron electrophysiology
benchmark we create) --- we show that MDA sets a new SOTA in terms of data-efficient
model learning and reliable interventional forecasting ability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09696v1
- Authors: Kevin Murphy
- Published: 2026-08-10T14:59:22Z
- Age days: 1

</details>
