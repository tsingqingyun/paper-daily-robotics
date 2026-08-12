---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14561v1"
published: "2026-06-12T15:38:34Z"
age_days: 2
score: 29
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# ORCA: A Platform for Open-Source Dexterity Research

> [!summary] 一句话结论（基于摘要）
> We demonstrate a complete end-to-end workflow, collecting expert demonstrations of an in- hand reorientation task by teleoperation with a consumer-grade VR headset, training an autonomous policy with \lerobot, and evaluating the learned policy in a fully repr…

## 关键点

- **问题**：Grippers are nonetheless limited by their form factor, often requiring bimanual setups even for simple reorientation tasks.
- **创新点 / 方法**：In this work, we introduce the \orca~learning stack, an open-source research stack for dexterity as a first-class robot learning domain.
- **证据**：We demonstrate a complete end-to-end workflow, collecting expert demonstrations of an in- hand reorientation task by teleoperation with a consumer-grade VR headset, training an autonomous policy with \lerobot, and evaluating the learned policy in a fully reproducible and observable setup.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/ORCA A Platform for Open-Source Dexterity Research.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotics manipulation research increasingly focuses on two-finger parallel grippers for
their effectiveness, affordability, and ease of teleoperation. Grippers are nonetheless
limited by their form factor, often requiring bimanual setups even for simple
reorientation tasks. Anthropomorphic hands are a more natural platform for dexterous
robot learning -- closer to the human hand, and capable of learning from human video --
yet they remain hard to use in learning research: even where open and accessible hand
hardware exists, the software for control, simulation, teleoperation, and retargeting is
scattered in one-off code bases, and largely disconnected from the robot-learning
ecosystem. In this work, we introduce the \orca~learning stack, an open-source research
stack for dexterity as a first-class robot learning domain. Our \orca~stack unifies low-
level control, simulation, teleoperation from a range of consumer platforms, and hand
retargeting, behind a single interface, and integrates natively with popular robot-
learning frameworks such as \lerobot, so dexterous hand researchers can leverage the
same data, training, and evaluation pipelines used for non-dexterous robot learning. We
demonstrate a complete end-to-end workflow, collecting expert demonstrations of an in-
hand reorientation task by teleoperation with a consumer-grade VR headset, training an
autonomous policy with \lerobot, and evaluating the learned policy in a fully
reproducible and observable setup. We open-source the entire stack as a shared,
reproducible foundation for dexterous-manipulation research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14561v1
- Authors: Francesco Capuano, Maximilian Eberlein, Fabrice Bourquin, Clemens Claudio Christoph
- Published: 2026-06-12T15:38:34Z
- Age days: 2

</details>
