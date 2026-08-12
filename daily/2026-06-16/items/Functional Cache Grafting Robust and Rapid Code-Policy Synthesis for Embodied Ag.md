---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13097v1"
published: "2026-06-11T09:25:27Z"
age_days: 4
score: 22
created: 2026-06-16
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents

> [!summary] 一句话结论（基于摘要）
> By eliminating redundant prefill computation, this approach reduces generation latency, while reusing validated control structures improves robustness over prompt-level caching methods RAGCache, achieving 18.31% higher task success rate and 2.3x faster policy…

## 关键点

- **问题**：However, policy generation in open-domain embodied environments suffers from two fundamental limitations: (i) delayed decoding caused by repetitive prefill computation over long prompts, and (ii) limited robustness due to fully generative decoding, which often produces API mismatches, missing safety guards, and unstab…
- **创新点 / 方法**：To address these limitations, we present FCGraft, a Functional Cache Grafting framework.
- **证据**：By eliminating redundant prefill computation, this approach reduces generation latency, while reusing validated control structures improves robustness over prompt-level caching methods RAGCache, achieving 18.31% higher task success rate and 2.3x faster policy synthesis.
- **局限**：However, policy generation in open-domain embodied environments suffers from two fundamental limitations: (i) delayed decoding caused by repetitive prefill computation over long prompts, and (ii) limited robustness due to fully generative decoding, which often produces API mismatches, missing safety guards, and unstab…

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-16/Functional Cache Grafting Robust and Rapid Code-Policy Synthesis for Embodied Ag.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Code-writing large language models (CodeLLMs) generate executable code policies for
embodied agents by translating natural language goals and environmental constraints into
structured control programs. However, policy generation in open-domain embodied
environments suffers from two fundamental limitations: (i) delayed decoding caused by
repetitive prefill computation over long prompts, and (ii) limited robustness due to
fully generative decoding, which often produces API mismatches, missing safety guards,
and unstable control logic. To address these limitations, we present FCGraft, a
Functional Cache Grafting framework. FCGraft maintains a library of function-level
validated code skeletons and their associated prompt-level Transformer key-value (KV)
caches, and synthesizes new policies by retrieving relevant functions and grafting their
KV caches when a new task is provided. Given retrieved function caches, FCGraft performs
cache grafting via stitching, which composes cached function segments into a composite
policy, and patching, which locally adapts only the necessary code regions to satisfy
task-specific parameters and constraints with minimal additional decoding. By
eliminating redundant prefill computation, this approach reduces generation latency,
while reusing validated control structures improves robustness over prompt-level caching
methods RAGCache, achieving 18.31% higher task success rate and 2.3x faster policy
synthesis.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13097v1
- Authors: Saehun Chun, Wonje Choi, Sera Choi, Sanghyun Ahn, Honguk Woo
- Published: 2026-06-11T09:25:27Z
- Age days: 4

</details>
