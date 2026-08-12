---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20376v1"
published: "2026-06-18T15:36:13Z"
age_days: 1
score: 35
created: 2026-06-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# CRAX: Fast Safe Reinforcement Learning Benchmarking

> [!summary] 一句话结论（基于摘要）
> To address this gap, we propose CRAX (Constrained RL Accelerated with JAX).

## 关键点

- **问题**：While benchmarks have been central to progress in RL, existing safety benchmarks with high-fidelity 3D physics remain computationally slow, limiting large-scale experimentation and rapid prototyping.
- **创新点 / 方法**：To address this gap, we propose CRAX (Constrained RL Accelerated with JAX).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/CRAX Fast Safe Reinforcement Learning Benchmarking.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safety is a core concern for deploying reinforcement learning (RL) agents in real-world
domains such as robotics and autonomous driving. While benchmarks have been central to
progress in RL, existing safety benchmarks with high-fidelity 3D physics remain
computationally slow, limiting large-scale experimentation and rapid prototyping. To
address this gap, we propose CRAX (Constrained RL Accelerated with JAX). Built on top of
the MuJoCo XLA (MJX) physics engine with realistic 3D dynamics, CRAX leverages
vectorized operations and hardware acceleration, yielding up to ~100x speedups over
comparable CPU-based safety benchmarks. The benchmark features six environment suites
and three agent-specific tasks, each spanning three difficulty levels. Evaluating six
popular safe RL methods shows that no single approach dominates across all tasks, and
reveals the trade-offs between performance and safety. We find that curriculum learning
across difficulty levels and safety transfer can improve performance over direct
training in harder settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20376v1
- Authors: Tristan Tomilin, Mourad Boustani, Mickey Beurskens, Thiago D. Simão
- Published: 2026-06-18T15:36:13Z
- Age days: 1

</details>
