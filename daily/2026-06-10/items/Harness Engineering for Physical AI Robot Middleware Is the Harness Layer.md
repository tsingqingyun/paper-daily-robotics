---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09416v1"
published: "2026-06-08T12:29:54Z"
age_days: 1
score: 36
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer

> [!summary] 一句话结论（基于摘要）
> The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness.

## 关键点

- **问题**：Robot middleware faces a new role in the era of Physical AI.
- **创新点 / 方法**：The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot middleware faces a new role in the era of Physical AI. Learned policies, planners,
and vision-language-action (VLA) models now enter deployed robots as causal participants
on the control path, but the layer that integrates them with timing, scheduling, and
network has not been named. Recent language-agent work names this layer the harness, the
external system that mediates tools, manages state, bounds resources, and records
execution. The robotics community has not yet adopted this framing, and we propose that
robot middleware is that harness. A Physical AI harness differs from a software harness
in where it intervenes. A software harness mediates at tool-call boundaries. A Physical
AI harness must mediate at control, computing, and communication simultaneously, because
a learned policy's output crosses all three: its commands shift the trajectory, its
inference time shifts the schedule, and its payload shifts the bandwidth. Robot
middleware is the lowest robot-stack layer with mediating abstractions over all three,
so it is best positioned to compose their enforcement. It already provides most of what
a harness needs but lacks the enforcement for an AI model. We name this missing
enforcement as three functions: Projection gates each output at emission, Isolation
bounds the model's execution and transmission slot, and Transfer falls back to a
verified baseline when checks fail. Each appears today as hand-built application code in
deployed robot systems, built on surfaces robot middleware already provides. Robot
middleware should host them not as the best single-axis enforcer but as the layer that
composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact
that carries an AI model's declared output region, inference budget, and operating
regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09416v1
- Authors: Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park
- Published: 2026-06-08T12:29:54Z
- Age days: 1

</details>
