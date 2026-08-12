---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09696v1"
published: "2026-08-10T14:59:22Z"
age_days: 1
score: 25
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09696v1
- Authors: Kevin Murphy
- Published: 2026-08-10T14:59:22Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
