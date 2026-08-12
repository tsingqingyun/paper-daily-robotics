---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06556v1"
published: "2026-06-04T10:43:14Z"
age_days: 3
score: 60
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Robots Need More than VLA and World Models

> [!summary] 一句话结论（基于摘要）
> In this position paper, we argue that this framing is incomplete.

## 关键点

- **问题**：Generalist robot intelligence is often framed as a policy-scaling problem: collect more robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect broader generalisation.
- **创新点 / 方法**：In this position paper, we argue that this framing is incomplete.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：60
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/Robots Need More than VLA and World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist robot intelligence is often framed as a policy-scaling problem: collect more
robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect
broader generalisation. In this position paper, we argue that this framing is
incomplete. The central bottleneck is not only policy learning, but the absence of
mechanisms that convert the world's abundant unstructured behavioural data into grounded
robot supervision. Human motion, internet video, simulation rollouts, and interactive
demonstrations contain rich information about tasks, goals, contacts, failures, and
physical constraints, yet most of this information is not directly usable by robot
policies because it lacks embodiment-specific action labels, task semantics, and reward
structure. We identify four missing components for the next generation of robotics: data
interfaces for autolabelling unstructured behaviour, embodiment interfaces for
retargeting human motion to robot actions, world-model interfaces for physics-grounded
3D reasoning, and reward interfaces for inferring task progress and success from video
and language. We survey recent progress in robot foundation models, cross-embodiment
datasets, learning from video, world models, and reward modelling, and propose a
research agenda for building robotics systems that can learn not only from robot
demonstrations, but from the broader physical world.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06556v1
- Authors: Elis Karcini, Faisal Mehrban, Quang Nguyen, Mac Schwager, Arash Ajoudani, Cesar Cadena, Jan Peters, Marco Hutter, Haitham Bou-Ammar
- Published: 2026-06-04T10:43:14Z
- Age days: 3

</details>
