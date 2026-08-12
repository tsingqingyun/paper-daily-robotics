---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.16856v1"
published: "2026-06-15T15:31:40Z"
age_days: 2
score: 38
created: 2026-06-18
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Extensive experiments across locomotion and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms state-of-the-art offline PbRL methods under limited feedback budgets.

## 关键点

- **问题**：Extensive experiments across locomotion and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms state-of-the-art offline PbRL methods under limited feedback budgets.
- **创新点 / 方法**：Inspired by advances in Video Foundation Models (ViFMs), we present Video-based Optimal Transport Preference (VOTP), a semi-supervised framework that learns effective reward functions from only a handful of labels.
- **证据**：Extensive experiments across locomotion and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms state-of-the-art offline PbRL methods under limited feedback budgets.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Conveying complex objectives to reinforcement learning (RL) agents often requires
meticulous reward engineering. Preference-based RL (PbRL) offers a promising alternative
by learning reward functions from human feedback, but its scalability is hindered by
high labeling costs. Inspired by advances in Video Foundation Models (ViFMs), we present
Video-based Optimal Transport Preference (VOTP), a semi-supervised framework that learns
effective reward functions from only a handful of labels. By leveraging optimal
transport to align visual trajectories within the rich representation space of ViFMs,
VOTP effectively generates high-fidelity pseudo-labels for large amounts of unlabeled
data, substantially reducing human supervision. Extensive experiments across locomotion
and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms
state-of-the-art offline PbRL methods under limited feedback budgets. We also showcase
the robustness of VOTP in the presence of visual distractors and validate its utility on
real robotic tasks, where it learns meaningful rewards with minimal human input.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.16856v1
- Authors: Tung M. Luu, Hwanhee Kim, Younghwan Lee, Chang D. Yoo
- Published: 2026-06-15T15:31:40Z
- Age days: 2

</details>
