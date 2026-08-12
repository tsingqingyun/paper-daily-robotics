---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15901v1"
published: "2026-07-17T12:14:55Z"
age_days: 2
score: 27
created: 2026-07-20
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# DSWorld: A Data Science World Model for Efficient Autonomous Agents

> [!summary] 一句话结论（基于摘要）
> Experiments show that DSWorld accelerates RL-based agent training by approximately $14\times$ and search-based inference by approximately $3$-$6\times$ while maintaining competitive performance, and outperforms the strongest LLM baseline by 35.6% on transitio…

## 关键点

- **问题**：This bottleneck motivates models that can anticipate the effects of data science operations before real execution.
- **创新点 / 方法**：In this paper, we introduce the concept of Data Science World Model, which model the data science execution environment by predicting environment state transitions conditioned on current workflow states and candidate operations.
- **证据**：Experiments show that DSWorld accelerates RL-based agent training by approximately $14\times$ and search-based inference by approximately $3$-$6\times$ while maintaining competitive performance, and outperforms the strongest LLM baseline by 35.6% on transition prediction tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Despite strong capabilities in data understanding and decision-making, autonomous data
science agents still heavily rely on trial-and-error workflows that involve expensive
computation. This bottleneck motivates models that can anticipate the effects of data
science operations before real execution. In this paper, we introduce the concept of
Data Science World Model, which model the data science execution environment by
predicting environment state transitions conditioned on current workflow states and
candidate operations. We further propose DSWorld, a practical framework that combines
structured state construction, cost-aware routing, lightweight real execution, and an
LLM-based simulator for expensive operations. To support training, we construct an
8K-scale transition trajectory dataset and introduce Reflective World Model
Optimization, an error-aware reinforcement learning strategy for improving transition
prediction. Experiments show that DSWorld accelerates RL-based agent training by
approximately $14\times$ and search-based inference by approximately $3$-$6\times$ while
maintaining competitive performance, and outperforms the strongest LLM baseline by 35.6%
on transition prediction tasks. The code is available at
https://anonymous.4open.science/r/DSWorld.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15901v1
- Authors: Zherui Yang, Fan Liu, Hao Liu
- Published: 2026-07-17T12:14:55Z
- Age days: 2

</details>
