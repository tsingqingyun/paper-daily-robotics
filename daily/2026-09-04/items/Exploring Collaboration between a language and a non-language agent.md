---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00474"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-09-04
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Exploring Collaboration between a language and a non-language agent

> [!summary] 先说人话（基于摘要）
> 这项工作认为，把非语言智能体的连续状态先压成文字会产生“语言化债务”。LLAMIA直接将这些表示投影为LLM词元流中的可学习状态token，并随环境动作动态重编码。

## 这篇到底在做什么

- **卡在哪里**：LLM可协调子智能体，但棋类、机器人等领域的强专家往往不是语言模型；把其丰富连续表示压缩成稀疏文字会丢信息，可能成为协作瓶颈。
- **关键解法**：LLAMIA-Bench让LLM与棋类引擎共同完成模仿、状态评估和自然语言解释任务，且任一方单独都无法解决。方法将引擎连续表示直接投影进LLM token序列，并在棋局推进后重新编码，区别于先生成文本摘要再交给LLM。
- **拿什么证明**：基准包含6项协作棋类任务、覆盖3类能力。实验显示内部化相对语言化的差距随训练扩大，并从4B扩至14B时仍存在；14B LLAMIA在全部任务上匹配或超过任务专家及包括带工具GPT-5.1在内的前沿模型，并在任务微调模型失效的分布外条件下泛化。摘要未给出具体分数。

## 值不值得读

- **和你的研究有什么关系**：对Agent和多模态基础模型研究者，它提示异构智能体协作未必应强制经过自然语言接口；连续状态token可能更适合机器人策略、搜索器或世界模型向LLM传递高带宽状态。机器人价值目前仍属方法启发。
- **先别急着信**：证据全部来自棋类协作，能否迁移到带噪声、连续控制和实时约束的机器人系统尚未由摘要支持。
- **判断**：做多智能体接口或工具增强LLM者值得精读；机器人研究者应把它视为有力假设和基准证据，而非已验证的具身方案。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/Exploring Collaboration between a language and a non-language agent.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.00474v2 Announce Type: replace-cross Abstract: LLMs are increasingly deployed as orchestrators that coordinate specialized subagents to solve complex tasks through natural language. However, in many important domains like game playing and robotics, the strongest available agents are not language models. Integrating non-language agents with LLMs would require \emph{verbalization}: compressing their rich continuous representations into sparse textual summaries at each interaction step. To study whether verbalization constitutes a bottleneck, we introduce \textsc{LLAMIA-Bench}, a suite of six diverse collaborative chess tasks spanning three facets: behavioral imitation, state assessment, and natural-language explanation. Each task instantiates a well-established chess problem that neither the LLM nor the chess engine can solve alone. To solve LLM collaboration with non-language agents, we introduce \emph{latent state internalization}, which projects the subagent's continuous representations directly into the LLM's token stream as learned state tokens, with dynamic re-encoding as actions advance the environment state. Comparing internalization to verbalized integration, our experiments reveal a consistent \emph{verbalization debt}: the performance gap widens throughout training and persists as the LLM scales from 4B to 14B parameters. A single 14B model, \textsc{LLAMIA}, trained with latent state internalization, matches or exceeds task specialists and frontier models including GPT-5.1 with tool access across all benchmark tasks, and generalizes out-of-distribution where task-specific finetunes collapse

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00474
- Authors: Harini S I, Somesh Singh, Yaman K Singla, Rajiv Ratn Shah, David Doermann, Balaji Krishnamurthy
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
