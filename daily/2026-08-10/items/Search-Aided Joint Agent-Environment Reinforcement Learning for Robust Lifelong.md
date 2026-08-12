---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05588v1"
published: "2026-08-06T04:17:38Z"
age_days: 4
score: 26
created: 2026-08-10
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations

> [!summary] 一句话结论（基于摘要）
> Experiments demonstrate that SJRL achieves significant improvements over the strong search-based planner, Causal-PIBT, across multiple high- density maps.

## 关键点

- **问题**：These constraints substantially increase coordination difficulty, particularly in highly constrained spaces.
- **创新点 / 方法**：To address these challenges, we propose Search-Aided Joint Reinforcement Learning (SJRL).
- **证据**：Experiments demonstrate that SJRL achieves significant improvements over the strong search-based planner, Causal-PIBT, across multiple high- density maps.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Lifelong Multi-Agent Path Finding (LMAPF) requires repeatedly planning collision-free
paths for agents that continuously receive new goals upon reaching their current ones.
While many learning-based planners have been proposed for LMAPF, most rely on
oversimplified kinematic assumptions that may overlook motion constraints critical to
real-world performance. In this work, we study a more realistic LMAPF model derived from
many real-world automated warehouse systems, termed LMAPF-R2, which incorporates robust
safety constraints and in-place rotation constraints. These constraints substantially
increase coordination difficulty, particularly in highly constrained spaces. To address
these challenges, we propose Search-Aided Joint Reinforcement Learning (SJRL). We first
augment neural policies with Causal PIBT, a single-step search-based planner that
resolves agents' collisions and propagates their intentions. We then introduce a unified
RL formulation that jointly optimizes agent and environment policies, where the
environment policy learns graph edge costs to provide global movement guidance via
backward Dijkstra search. Experiments demonstrate that SJRL achieves significant
improvements over the strong search-based planner, Causal-PIBT, across multiple high-
density maps. We further validate SJRL in a challenging mixed-reality warehouse
environment with 8 physical robots and 248 virtual robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05588v1
- Authors: He Jiang, Jingtian Yan, Yulun Zhang, Yimin Tang, Tanishq Duhan, Rishi Veerapaneni, Guillaume Sartoretti, Jiaoyang Li
- Published: 2026-08-06T04:17:38Z
- Age days: 4

</details>
