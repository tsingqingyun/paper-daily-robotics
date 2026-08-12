---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05695v1"
published: "2026-08-06T07:37:49Z"
age_days: 4
score: 27
created: 2026-08-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model

> [!summary] 一句话结论（基于摘要）
> Experiments across four benchmarks and an online guardrail evaluation show that DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves the best safety-utility trade-off among evaluated guardrails, and maintains an average end-to…

## 关键点

- **问题**：Recent runtime guardrails mitigate such risks by checking proposed actions before execution, but many remain reactive: they primarily assess the apparent safety of the current action, lacking an explicit model of how risk evolves across the trajectory.
- **创新点 / 方法**：In response, we propose DreamGuard, a proactive guardrail for LLM agents built around a risk-aware world model.
- **证据**：Experiments across four benchmarks and an online guardrail evaluation show that DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves the best safety-utility trade-off among evaluated guardrails, and maintains an average end-to-end latency of 25 ms per call.
- **局限**：This limitation creates a critical blind spot for long-horizon risks, where individually benign-looking actions can gradually drift the agent toward hazardous states.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/DreamGuard Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As large language model (LLM) agents increasingly invoke external tools and interact
with real-world systems, unsafe actions may cause irreversible consequences on external
states, user data, and downstream services. Recent runtime guardrails mitigate such
risks by checking proposed actions before execution, but many remain reactive: they
primarily assess the apparent safety of the current action, lacking an explicit model of
how risk evolves across the trajectory. This limitation creates a critical blind spot
for long-horizon risks, where individually benign-looking actions can gradually drift
the agent toward hazardous states. In response, we propose DreamGuard, a proactive
guardrail for LLM agents built around a risk-aware world model. The world model
maintains a compact recurrent latent state over the trajectory and predicts future
latent states from which DreamGuard derives immediate-hazard and prefix-risk evidence.
It then fuses these multi-horizon signals into intervention decisions before execution.
Experiments across four benchmarks and an online guardrail evaluation show that
DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves
the best safety-utility trade-off among evaluated guardrails, and maintains an average
end-to-end latency of 25 ms per call.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05695v1
- Authors: Wenhao Lin, Chenyu Yu, Xingwei Lin, Sicong Cao, Xiang Chen, Lei Xue, Le Yu, Letian Sha, Chunming Wu
- Published: 2026-08-06T07:37:49Z
- Age days: 4

</details>
