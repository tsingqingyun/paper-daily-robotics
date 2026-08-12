---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13677v1"
published: "2026-06-11T17:59:49Z"
age_days: 1
score: 28
created: 2026-06-13
concepts: ["智能体 Agent", "机器人学习", "Sim2Real"]
---

# Mana: Dexterous Manipulation of Articulated Tools

> [!summary] 一句话结论（基于摘要）
> Across four articulated tools spanning different scales and joint types, Mana achieves zero-shot sim-to-real transfer for both grasping and in-hand manipulation, demonstrating a scalable approach to dexterous articulated tool use.

## 关键点

- **问题**：Articulated tool manipulation remains a major challenge in dexterous robotics due to the need to coordinate internal degrees of freedom and contact-rich interactions.
- **创新点 / 方法**：We present Mana (Manipulation Animator), a general sim-to-real framework that reinterprets dexterous manipulation as an animation problem.
- **证据**：Across four articulated tools spanning different scales and joint types, Mana achieves zero-shot sim-to-real transfer for both grasping and in-hand manipulation, demonstrating a scalable approach to dexterous articulated tool use.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[Sim2Real]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/Mana Dexterous Manipulation of Articulated Tools.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Articulated tool manipulation remains a major challenge in dexterous robotics due to the
need to coordinate internal degrees of freedom and contact-rich interactions. While
prior work has largely focused on rigid objects, articulated tool use remains
underexplored because of its physical complexity and the difficulty of learning
functional grasping and manipulation policies. We present Mana (Manipulation Animator),
a general sim-to-real framework that reinterprets dexterous manipulation as an animation
problem. Inspired by computer animation, Mana employs a coarse-to-fine pipeline that
transforms procedurally-generated grasp keyframes into manipulation trajectories through
motion planning and reinforcement learning. The data generation process is largely
automatic, requiring only a few mouse clicks to specify functional affordances (<1
minute per tool). Across four articulated tools spanning different scales and joint
types, Mana achieves zero-shot sim-to-real transfer for both grasping and in-hand
manipulation, demonstrating a scalable approach to dexterous articulated tool use.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13677v1
- Authors: Zhao-Heng Yin, Guanya Shi, Pieter Abbeel, C. Karen Liu
- Published: 2026-06-11T17:59:49Z
- Age days: 1

</details>
