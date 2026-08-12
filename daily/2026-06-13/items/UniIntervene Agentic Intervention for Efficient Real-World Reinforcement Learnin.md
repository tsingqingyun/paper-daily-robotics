---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12372v1"
published: "2026-06-10T17:38:24Z"
age_days: 2
score: 30
created: 2026-06-13
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# UniIntervene: Agentic Intervention for Efficient Real-World Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on diverse real-world manipulation tasks demonstrate that UniIntervene improves the average success rate by 8.6% while reducing human interventions by 57% relative to state-of-the-art HiL-RL baselines.

## 关键点

- **问题**：However, current HiL-RL frameworks remain intervention-intensive, relying on frequent human corrections to redirect the policy out of unproductive exploration, which incurs high labor cost and limits real-world scalability.
- **创新点 / 方法**：To address this, we propose UniIntervene, an agentic intervention model that detects unproductive exploration and autonomously recovers the policy toward high-value states, taking over the bulk of interventions from human operators.
- **证据**：Extensive experiments on diverse real-world manipulation tasks demonstrate that UniIntervene improves the average success rate by 8.6% while reducing human interventions by 57% relative to state-of-the-art HiL-RL baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/UniIntervene Agentic Intervention for Efficient Real-World Reinforcement Learnin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human-in-the-loop reinforcement learning (HiL-RL) has emerged as an effective paradigm
for real-world robotic manipulation, enabling online policy improvement with human
guidance. However, current HiL-RL frameworks remain intervention-intensive, relying on
frequent human corrections to redirect the policy out of unproductive exploration, which
incurs high labor cost and limits real-world scalability. To address this, we propose
UniIntervene, an agentic intervention model that detects unproductive exploration and
autonomously recovers the policy toward high-value states, taking over the bulk of
interventions from human operators. Specifically, UniIntervene first performs future-
conditioned action-value estimation, predicting the latent consequence of the current
action and evaluating its induced value, which provides a more stable progress signal.
Building on this, a temporal value-risk critic aggregates recent value dynamics and
triggers intervention when the estimated value exhibits sustained stagnation or
degradation. When intervention is required, UniIntervene retrieves a high-value recovery
target from a memory of past intervention episodes and produces executable corrective
actions through a goal-conditioned recovery policy. In this way, UniIntervene turns
intervention from passive human correction into a value-aware recovery process for
efficient real-world RL. Extensive experiments on diverse real-world manipulation tasks
demonstrate that UniIntervene improves the average success rate by 8.6% while reducing
human interventions by 57% relative to state-of-the-art HiL-RL baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12372v1
- Authors: Haoyuan Deng, Yitong Gao, Yudong Lin, Haichao Liu, Zhenyu Wu, Ziwei Wang
- Published: 2026-06-10T17:38:24Z
- Age days: 2

</details>
