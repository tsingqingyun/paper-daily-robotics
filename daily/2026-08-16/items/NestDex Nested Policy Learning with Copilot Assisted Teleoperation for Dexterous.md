---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13362v1"
published: "2026-08-13T15:25:39Z"
age_days: 2
score: 26
created: 2026-08-16
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation

> [!summary] 一句话结论（基于摘要）
> Across real-world dexterous manipulation experiments, NestDex improves demonstration reliability and efficiency, and the resulting empirical evaluations support effective autonomous policy learning.

## 关键点

- **问题**：Dexterous manipulation promises substantially richer robot interaction with the physical world, but learning these behaviours remains constrained by the difficulty of collecting consistent, complete-task demonstrations.
- **创新点 / 方法**：We introduce NestDex, a nested policy-learning framework that reduces this burden by using learned hand skills to assist demonstration collection.
- **证据**：Across real-world dexterous manipulation experiments, NestDex improves demonstration reliability and efficiency, and the resulting empirical evaluations support effective autonomous policy learning.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/NestDex Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Dexterous manipulation promises substantially richer robot interaction with the physical world, but learning these behaviours remains constrained by the difficulty of collecting consistent, complete-task demonstrations. Unlike parallel-jaw manipulation, dexterous tasks require the operator to coordinate arm motion with precise, contact-rich finger behaviour throughout the task. We introduce NestDex, a nested policy-learning framework that reduces this burden by using learned hand skills to assist demonstration collection. The operator controls the arm and regulates the active hand skill through a single-DoF clutch, rather than directly specifying the full finger trajectory. The inner hand policy adapts its motion from the latest proprioceptive history, while a vision-language selector activates the appropriate skill for each task stage. The resulting demonstrations train a separate outer visuomotor policy that controls both the arm and hand without the inner policies at deployment. A hand-action variational autoencoder provides compact hand-action targets while retaining arm commands in joint space. Across real-world dexterous manipulation experiments, NestDex improves demonstration reliability and efficiency, and the resulting empirical evaluations support effective autonomous policy learning. Video Demo are available at project website https://aus.bot/research/nestdex.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13362v1
- Authors: James Zhao, Jinhe Tang, Mingyuan Ba, Weiming Zhi
- Published: 2026-08-13T15:25:39Z
- Age days: 2

</details>
