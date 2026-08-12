---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17760v1"
published: "2026-07-20T09:51:02Z"
age_days: 1
score: 33
created: 2026-07-22
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Generalize and Guide: Decomposing Rewards for Few-Shot Inverse Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> We demonstrate the effectiveness of our method on multiple challenging navigation and manipulation tasks under significant variations (e.g., object configurations, table layouts, and initial robot poses), achieving an average success rate of 81.2%, outperform…

## 关键点

- **问题**：However, real-world tasks often exhibit substantial natural variations (e.g., picking up mugs with varying shapes), making it impractical to collect demonstrations that fully specify a new task under every possible scenario.
- **创新点 / 方法**：We introduce Multitask discriminator Proximity-Guided IRL (MPG), which learns two complementary reward components: (1) a generalizable discriminator that transfers shared structure across related tasks to identify expert behavior in a new task, and (2) a proximity function that measures how far a state deviates from e…
- **证据**：We demonstrate the effectiveness of our method on multiple challenging navigation and manipulation tasks under significant variations (e.g., object configurations, table layouts, and initial robot poses), achieving an average success rate of 81.2%, outperforming the strongest per-task baseline by an average of 24.7 pe…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Inverse reinforcement learning (IRL) provides a powerful framework for learning from
demonstrations. However, real-world tasks often exhibit substantial natural variations
(e.g., picking up mugs with varying shapes), making it impractical to collect
demonstrations that fully specify a new task under every possible scenario. In practice,
while demonstrations for the target task are limited, it is often easier to obtain
datasets of heterogeneous but related behaviors. This motivates the problem of few-shot
IRL with multi-task demonstrations (FM-IRL), where an agent must learn a new task with
substantial variations from only a limited number of target-task demonstrations,
together with sufficient demonstrations of related tasks and online agent experience. To
do so, we must both recover the expert distribution of the new task and provide guidance
when the agent deviates from it. We introduce Multitask discriminator Proximity-Guided
IRL (MPG), which learns two complementary reward components: (1) a generalizable
discriminator that transfers shared structure across related tasks to identify expert
behavior in a new task, and (2) a proximity function that measures how far a state
deviates from expert behavior and provides corrective guidance during exploration. We
demonstrate the effectiveness of our method on multiple challenging navigation and
manipulation tasks under significant variations (e.g., object configurations, table
layouts, and initial robot poses), achieving an average success rate of 81.2%,
outperforming the strongest per-task baseline by an average of 24.7 percentage points.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17760v1
- Authors: Ziyi Liu, Grace Zhang
- Published: 2026-07-20T09:51:02Z
- Age days: 1

</details>
