---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01060v1"
published: "2026-07-01T15:22:41Z"
age_days: 4
score: 28
created: 2026-07-06
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation

> [!summary] 一句话结论（基于摘要）
> We introduce RoboWorld, an automated evaluation pipeline that pairs a fast autoregressive video world model with a task-progress-aware vision-language model scoring.

## 关键点

- **问题**：However, evaluating policies with video world models remains challenging, as world-model errors can make generated rollouts unreliable and slow inference limits large-scale throughput.
- **创新点 / 方法**：We introduce RoboWorld, an automated evaluation pipeline that pairs a fast autoregressive video world model with a task-progress-aware vision-language model scoring.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：However, evaluating policies with video world models remains challenging, as world-model errors can make generated rollouts unreliable and slow inference limits large-scale throughput.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video world models are emerging as a scalable alternative for evaluating generalist
robot policies, bypassing the physical constraints and engineering burdens of real-world
deployment. However, evaluating policies with video world models remains challenging, as
world-model errors can make generated rollouts unreliable and slow inference limits
large-scale throughput. We introduce RoboWorld, an automated evaluation pipeline that
pairs a fast autoregressive video world model with a task-progress-aware vision-language
model scoring. To enable reliable long-horizon autoregressive world-model rollouts, we
propose Step Forcing, which combines anchored and one-step self-forwarded contexts to
reduce train--test mismatch while preserving action--observation dynamics. Together,
these components enable RoboWorld to align strongly with real-world robot evaluation
across tasks and environments, achieving Pearson's r = 0.989 and Spearman's \r{ho} =
0.970.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01060v1
- Authors: Byeongguk Jeon, Seonghyeon Ye, JaeHyeok Doo, Sungdong Kim, Minjoon Seo, Hyungmok Son, Kimin Lee
- Published: 2026-07-01T15:22:41Z
- Age days: 4

</details>
