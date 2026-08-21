---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18840v1"
published: "2026-08-19T12:00:35Z"
age_days: 1
score: 30
created: 2026-08-21
concepts: ["智能体 Agent", "世界模型"]
---

# Beyond Placement and Articulation: Usage-Driven Code Scenes for Embodied Interaction

> [!summary] 一句话结论（基于摘要）
> To address this problem, we present RoomWright, an agentic usage-driven framework for generating 3D scenes represented entirely as code for embodied interaction.

## 关键点

- **问题**：Recent code-based scene generation methods produce editable and extensible environments, yet they remain focused on visual construction and object-level articulation, leaving the functional usage of scenes largely unmodeled.
- **创新点 / 方法**：To address this problem, we present RoomWright, an agentic usage-driven framework for generating 3D scenes represented entirely as code for embodied interaction.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Beyond Placement and Articulation Usage-Driven Code Scenes for Embodied Interact.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Indoor scene synthesis provides essential environments for embodied AI, robotic manipulation, and simulation-based policy learning. Recent code-based scene generation methods produce editable and extensible environments, yet they remain focused on visual construction and object-level articulation, leaving the functional usage of scenes largely unmodeled. To address this problem, we present RoomWright, an agentic usage-driven framework for generating 3D scenes represented entirely as code for embodied interaction. RoomWright performs usage-driven object reasoning, which treats each anchor as a task centre and admits task-required objects and their affordances. A code agent further enables multi-part interaction by compiling each interaction into a trigger, condition, effect rule that updates structured object states, capturing causal dependencies across objects. Moreover, since manipuland orientation is ambiguous and hard to recover from pixels, RoomWright alleviates this via annotation-informed usage-guided orientation. Extensive experiments demonstrate the effectiveness of our method. The resulting scenes are executable, editable, and simulation-ready, providing interactive environments for embodied AI and policy learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18840v1
- Authors: Zijian Xiao, Zipeng Ye, Jinkun Hao, Xiong Yang, Yuchen Xie, Ran Yi
- Published: 2026-08-19T12:00:35Z
- Age days: 1

</details>
