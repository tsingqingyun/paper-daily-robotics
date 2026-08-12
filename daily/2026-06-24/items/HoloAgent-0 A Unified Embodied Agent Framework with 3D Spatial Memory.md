---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23565v1"
published: "2026-06-22T16:31:48Z"
age_days: 1
score: 37
created: 2026-06-24
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory

> [!summary] 一句话结论（基于摘要）
> In this work, we introduce HoloAgent-0, a unified embodied agent framework for real- world robot deployment.

## 关键点

- **问题**：Extending this loop to physical robots is difficult because physical execution is continuous, embodiment-dependent, uncertain, and constrained by safety.
- **创新点 / 方法**：In this work, we introduce HoloAgent-0, a unified embodied agent framework for real- world robot deployment.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

LLM agents follow a practical execution loop in digital environments: they reason over
structured states, invoke tools, inspect feedback, and revise actions. Extending this
loop to physical robots is difficult because physical execution is continuous,
embodiment-dependent, uncertain, and constrained by safety. Existing embodied-AI systems
have advanced manipulation, spatial understanding, navigation, and humanoid control, but
these capabilities often remain specialized modules or loosely coupled decision loops.
In this work, we introduce HoloAgent-0, a unified embodied agent framework for real-
world robot deployment. Embodied AgentOS converts language instructions into executable
skill graphs, schedules robot resources, monitors execution, and triggers clarification
or re-planning from runtime feedback. HoloAgent-0 organizes heterogeneous robot models
and controllers through three coupled layers: Embodied AgentOS for closed-loop
execution, 3D spatial memory for physical world grounding, and embodied skills for robot
action. We deploy HoloAgent-0 on real hardware and evaluate its spatial memory, long-
horizon navigation, and closed-loop execution across motion generation, object search,
cross-robot coordination, and mobile manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23565v1
- Authors: Xiaolin Zhou, Liu Liu, Tingyang Xiao, Wei Feng, Fa Fu, Xinrui Meng, Xinjie Wang, Jialiang Han, Boyang Yu, Yun Du, Wei Sui, Zhizhong Su
- Published: 2026-06-22T16:31:48Z
- Age days: 1

</details>
