---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18672v1"
published: "2026-08-19T08:24:40Z"
age_days: 1
score: 28
created: 2026-08-21
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Orienteering Problem with Uncertain Time-Varying Rewards: Framework and Benchmark for Everyday Service Robotics

> [!summary] 一句话结论（基于摘要）
> We present the orienteering problem with uncertain time-varying rewards (OP-UTVR), a novel variant of the orienteering problem (OP).

## 关键点

- **问题**：We address this problem using three planners that differ in planning horizon and online adaptivity, and derive theoretical bounds on their performance under reward stochasticity.
- **创新点 / 方法**：We present the orienteering problem with uncertain time-varying rewards (OP-UTVR), a novel variant of the orienteering problem (OP).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Orienteering Problem with Uncertain Time-Varying Rewards Framework and Benchmark.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present the orienteering problem with uncertain time-varying rewards (OP-UTVR), a novel variant of the orienteering problem (OP). While most existing OP formulations assume rewards to be known in advance, practical applications involve uncertain and time-varying rewards, as with shifting customer demand for delivery agents. OP-UTVR relaxes this assumption by allowing agents to estimate reward dynamics from observations and forecast future rewards. This enables informed routing decisions despite stochastic reward changes and inevitable prediction errors. We address this problem using three planners that differ in planning horizon and online adaptivity, and derive theoretical bounds on their performance under reward stochasticity. We further introduce a mobile service robot benchmark for OP-UTVR, where a robot navigates among pedestrians in indoor environments. Experiments reveal trade-offs between planning horizon and adaptivity, and demonstrate the effectiveness of long-horizon planning with online adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18672v1
- Authors: Masafumi Endo, Kohei Honda, Yuu Jinnai, Ryo Yonetani
- Published: 2026-08-19T08:24:40Z
- Age days: 1

</details>
