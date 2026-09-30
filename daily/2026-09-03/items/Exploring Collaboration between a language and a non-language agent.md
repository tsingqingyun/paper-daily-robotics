---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00474v2"
published: "2026-08-31T23:25:10Z"
age_days: 2
score: 28
created: 2026-09-03
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Exploring Collaboration between a language and a non-language agent

> [!summary] 先说人话（基于摘要）
> LLAMIA 用 latent state internalization 把非语言代理的连续内部状态投影为可学习状态 token，直接送入 LLM，并随环境动作动态重编码。它避免把丰富状态压缩成稀疏文字所产生的“verbalization debt”。

## 问题

LLM 编排棋类或机器人等强非语言代理时，通常需要把连续表征口头化；这种压缩可能丢失关键状态，而且语言代理或棋类代理单独都无法完成所设协作任务。

## 创新点或方法

LLAMIA-Bench 用6种棋类协作任务覆盖行为模仿、状态评估和语言解释；模型把子代理连续表示映射进 token 流，而非每步生成文字摘要，并在状态推进时重新编码。

## 证据

内部化相对文字集成的差距随训练扩大，并在 LLM 从4B扩至14B时仍存在；单个14B LLAMIA 在全部任务上达到或超过任务专家及含工具的 GPT-5.1，并在任务微调模型失效的分布外情形中泛化。摘要未给具体分数。


## 局限

实证全部来自棋类，连续状态可访问且可微投影的条件在真实机器人或封闭式专家系统中未必成立。

- **判断**：值得精读接口设计和 OOD 实验；结论对异构 Agent 很有启发，但向机器人外推时应视作待验证假设。

## 研究关联

对多代理和机器人 Agent，这表明语言未必是异构模块间的最佳总线；直接共享潜在状态可能保留控制所需细节，尤其适合连续感知或规划器接入 LLM。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Exploring Collaboration between a language and a non-language agent.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

LLMs are increasingly deployed as orchestrators that coordinate specialized subagents to solve complex tasks through natural language. However, in many important domains like game playing and robotics, the strongest available agents are not language models. Integrating non-language agents with LLMs would require \emph{verbalization}: compressing their rich continuous representations into sparse textual summaries at each interaction step. To study whether verbalization constitutes a bottleneck, we introduce \textsc{LLAMIA-Bench}, a suite of six diverse collaborative chess tasks spanning three facets: behavioral imitation, state assessment, and natural-language explanation. Each task instantiates a well-established chess problem that neither the LLM nor the chess engine can solve alone. To solve LLM collaboration with non-language agents, we introduce \emph{latent state internalization}, which projects the subagent's continuous representations directly into the LLM's token stream as learned state tokens, with dynamic re-encoding as actions advance the environment state. Comparing internalization to verbalized integration, our experiments reveal a consistent \emph{verbalization debt}: the performance gap widens throughout training and persists as the LLM scales from 4B to 14B parameters. A single 14B model, \textsc{LLAMIA}, trained with latent state internalization, matches or exceeds task specialists and frontier models including GPT-5.1 with tool access across all benchmark tasks, and generalizes out-of-distribution where task-specific finetunes collapse

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00474v2
- Authors: Harini S, Somesh Singh, Yaman K Singla, Rajiv Ratn Shah, David Doermann, Balaji Krishnamurthy
- Published: 2026-08-31T23:25:10Z
- Age days: 2

</details>
