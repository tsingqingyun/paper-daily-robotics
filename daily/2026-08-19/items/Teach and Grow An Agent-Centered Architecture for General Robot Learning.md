---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17209v1"
published: "2026-08-17T23:45:21Z"
age_days: 1
score: 42
created: 2026-08-19
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Teach and Grow: An Agent-Centered Architecture for General Robot Learning

> [!summary] 一句话结论（基于摘要）
> We present Teach-and-Grow Learning (TGL), an agent-centered architecture for general robot learning.

## 关键点

- **问题**：When an unfamiliar object, sensor, embodiment, or contact falls outside that coverage and no validated fallback exists, correcting the failure requires new robot data, a policy update, and regression testing.
- **创新点 / 方法**：We present Teach-and-Grow Learning (TGL), an agent-centered architecture for general robot learning.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Teach and Grow An Agent-Centered Architecture for General Robot Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end vision-language-action (VLA) and world-action models offer an elegant route to general-purpose robotics, but their reliability is bounded by validated physical coverage. When an unfamiliar object, sensor, embodiment, or contact falls outside that coverage and no validated fallback exists, correcting the failure requires new robot data, a policy update, and regression testing. This recurring burden is the retraining tax. Unlike text, embodied data must often be created by operating machines. We present Teach-and-Grow Learning (TGL), an agent-centered architecture for general robot learning. In its general form, a multimodal agent turns a few successful demonstrations into reusable Skill Blocks: closed-loop behaviors for meaningful subgoals. In a new scene, the agent grounds and composes these blocks, selects learned or geometric tools, observes the physical outcome, and revises the route when execution departs from intent. A Skill Library stores executable behavior, while structured Experience Memory carries forward success, failure, and repair. New tasks are acquired without task-specific policy retraining. Our LIBERO evaluation attains state-of-the-art performance; controlled studies expose skill induction, persistent reuse, and agent-directed adaptation. Finally, we propose the Teach-and-Grow scaling-law hypothesis: if X denotes effective reusable experience, future-task error and teaching demand should approach irreducible floors as power laws in X. The architecture therefore treats deployment as a period of continued learning, in which one task can make the next easier.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17209v1
- Authors: Chang Nie, Zhe Liu, Hesheng Wang
- Published: 2026-08-17T23:45:21Z
- Age days: 1

</details>
