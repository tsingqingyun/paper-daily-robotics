---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09138v1"
published: "2026-08-10T05:31:41Z"
age_days: 1
score: 30
created: 2026-08-11
concepts: ["机器人学习", "具身智能评测与基准"]
---

# SpeedTuning: Speeding Up Policy Execution with Lightweight Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> We provide empirical evidence that SpeedTuning achieves substantial improvements in execution speed, exceeding 2.4x speed-up, while preserving an adequate success rate compared to both the original task policy and straightforward speed-up methods such as line…

## 关键点

- **问题**：Imitation learning policies are inherently limited by hardware constraints and the speed of the operator during data collection.
- **创新点 / 方法**：To address these issues, we introduce SpeedTuning, a reinforcement learning framework specifically designed to enhance the speed of manipulation policies.
- **证据**：We provide empirical evidence that SpeedTuning achieves substantial improvements in execution speed, exceeding 2.4x speed-up, while preserving an adequate success rate compared to both the original task policy and straightforward speed-up methods such as linear interpolation at a fixed speed.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While learned robotic policies hold promise for advancing generalizable manipulation,
their practical deployment is often hindered by suboptimal execution speeds. Imitation
learning policies are inherently limited by hardware constraints and the speed of the
operator during data collection. In addition, there are no established methods for
accelerating policies learned via imitation, and the empirical relationship between
execution speed and task success remains underexplored. To address these issues, we
introduce SpeedTuning, a reinforcement learning framework specifically designed to
enhance the speed of manipulation policies. SpeedTuning learns to predict the optimal
execution speed for actions, thereby complementing a base policy without necessitating
additional data collection. We provide empirical evidence that SpeedTuning achieves
substantial improvements in execution speed, exceeding 2.4x speed-up, while preserving
an adequate success rate compared to both the original task policy and straightforward
speed-up methods such as linear interpolation at a fixed speed. We evaluate our approach
across a diverse set of dynamic and precise tasks, including pouring, throwing, and
picking, demonstrating its effectiveness and robustness in enhancing real-world robotic
manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09138v1
- Authors: David D. Yuan, Tony Z. Zhao, Kaylee Burns, Chelsea Finn
- Published: 2026-08-10T05:31:41Z
- Age days: 1

</details>
