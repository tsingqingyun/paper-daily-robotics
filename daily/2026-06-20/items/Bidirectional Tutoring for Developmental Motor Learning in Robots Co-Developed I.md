---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19728v1"
published: "2026-06-18T02:51:29Z"
age_days: 1
score: 34
created: 2026-06-20
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Bidirectional Tutoring for Developmental Motor Learning in Robots: Co-Developed Interaction Dynamics Support Stable Learning

> [!summary] 一句话结论（基于摘要）
> Although such social interaction is crucial for human development, motor- skill learning in robots is often treated as a unidirectional process in which robots passively receive demonstrations from tutors.

## 关键点

- **问题**：Infants are well known to develop their motor skills through dense interaction with caregivers.
- **创新点 / 方法**：Although such social interaction is crucial for human development, motor- skill learning in robots is often treated as a unidirectional process in which robots passively receive demonstrations from tutors.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/Bidirectional Tutoring for Developmental Motor Learning in Robots Co-Developed I.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Infants are well known to develop their motor skills through dense interaction with
caregivers. Although such social interaction is crucial for human development, motor-
skill learning in robots is often treated as a unidirectional process in which robots
passively receive demonstrations from tutors. This overlooks a key property of social
interaction: it is inherently bidirectional, with tutor and learner dynamically adapting
to each other. In such interactions, the robot's past experiences may function as prior
constraints that shape the dynamics of their co-developed trajectories. We hypothesize
that bidirectional tutoring allows such constraints to guide the formation of consistent
behavioral patterns that preserve behavioral coherence and support generalization,
whereas unidirectional interaction lacks such constraints and leads to broader, less
consistent behavioral patterns. To examine this hypothesis, we conducted two experiments
with a physical humanoid robot performing an object manipulation task: one involving
human-robot interaction and another employing an AI tutor interacting with the real
robot through an adaptive intervention mechanism designed to examine whether similar
effects would emerge under more controlled conditions. We implement the developmental
learning framework using a free-energy-principle-based neural network extended with
generative replay, which supports stable sequence-by-sequence learning from single
tutored episodes. Across both settings, bidirectional tutoring fostered consistent
behaviors and stage-wise generalization, while the robot gradually required less tutor
guidance. These results suggest that bidirectional tutoring, as an embodied and socially
grounded approach, provides an effective scaffold for developmental motor learning in
robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19728v1
- Authors: Rui Fukushima, Jun Tani
- Published: 2026-06-18T02:51:29Z
- Age days: 1

</details>
