---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18063v1"
published: "2026-07-20T15:30:38Z"
age_days: 1
score: 29
created: 2026-07-22
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security

> [!summary] 一句话结论（基于摘要）
> Holding the 21 scenarios, attackers, defenders, and structured-output scoring fixed, restricting scoring to the first attacker turn yields $0$-$1\%$ attack success rate (ASR); allowing 15 rounds of adaptive attack yields $5.4$-$14.0\%$.

## 关键点

- **问题**：LLM-based agents process external content, exposing them to prompt injection and multi- turn manipulation.
- **创新点 / 方法**：We present a 21-scenario benchmark for \emph{adaptive multi-round attacks against memoryless LLM defenders}: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction.
- **证据**：Holding the 21 scenarios, attackers, defenders, and structured-output scoring fixed, restricting scoring to the first attacker turn yields $0$-$1\%$ attack success rate (ASR); allowing 15 rounds of adaptive attack yields $5.4$-$14.0\%$.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-22/Adaptive Adversaries A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

LLM-based agents process external content, exposing them to prompt injection and multi-
turn manipulation. Most safety benchmarks evaluate defenders against fixed attack pools
collected before evaluation, single-turn or multi-turn. We present a 21-scenario
benchmark for \emph{adaptive multi-round attacks against memoryless LLM defenders}: an
autonomous LLM attacker observes prior defender responses and pivots across rounds,
while each defender response is evaluated as a fresh interaction. Holding the 21
scenarios, attackers, defenders, and structured-output scoring fixed, restricting
scoring to the first attacker turn yields $0$-$1\%$ attack success rate (ASR); allowing
15 rounds of adaptive attack yields $5.4$-$14.0\%$. Pooling three frontier attacker LLMs
uncovers $1.4$-$2.2\times$ as many unique successful attacks as the best single
attacker, and the generated attacks have low cosine similarity ($0.02$-$0.14$) to
attacks in existing benchmarks. Claude Opus 4.6 and GPT-5.4 are tied in aggregate
($5.4\%$ each; overlapping $95\%$ CIs), but their weaknesses differ sharply: on one
scenario Opus reaches $60\%$ ASR ($95\%$ CI $36$--$80\%$) while GPT-5.4 and Gemini each
stay at $7\%$ (CI $1$-$30\%$; the gap is preserved in a higher-$N$ replication). $13$ of
$21$ scenarios distinguish at least one defender pair, yet rankings disagree across
scenarios (Kendall's $W = 0.19$). We release the benchmark -- 21 evaluation scenarios,
10 public development scenarios, the orchestrator, baseline harnesses, and a multi-
attacker CLI -- plus 945 transcripts from the 3$\times$3 frontier matrix, an attack-
replay dataset, and 18{,}422 gpt-oss-20b battles from an open competition's final
scoring rounds.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18063v1
- Authors: Devina Jain, David Hartmann, Chuan Li
- Published: 2026-07-20T15:30:38Z
- Age days: 1

</details>
