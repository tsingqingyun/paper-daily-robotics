---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13119v1"
published: "2026-05-13T07:40:34Z"
age_days: 0
score: 36
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Experiments show that VLAs-as-Tools improves the success rate of $π_{0.5}$ by 4.8 points on LIBERO-Long and 23.1 points on RoboTwin, and further enhances invocation fidelity by 15.0 points as measured by Non-biased Rate.

## 关键点

- **问题**：Vision-language-action (VLA) models are effective robot action executors, but they remain limited on long-horizon tasks due to the dual burden of extended closed-loop planning and diverse physical operations.
- **创新点 / 方法**：To tightly couple agent planning with VLA tool execution in long-horizon tasks, we introduce a VLA tool-family interface that exposes explicit tool selection and in-execution progress feedback, enabling efficient event- triggered agent replanning without continuous agent polling.
- **证据**：Experiments show that VLAs-as-Tools improves the success rate of $π_{0.5}$ by 4.8 points on LIBERO-Long and 23.1 points on RoboTwin, and further enhances invocation fidelity by 15.0 points as measured by Non-biased Rate.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Mo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models are effective robot action executors, but they
remain limited on long-horizon tasks due to the dual burden of extended closed-loop
planning and diverse physical operations. We therefore propose VLAs-as-Tools, a strategy
that distributes this burden across a high-level vision language model (VLM) agent for
temporal reasoning and a family of specialized VLA tools for diverse local physical
operations. The VLM handles scene analysis, global planning, and recovery, while each
VLA tool executes a bounded subtask. To tightly couple agent planning with VLA tool
execution in long-horizon tasks, we introduce a VLA tool-family interface that exposes
explicit tool selection and in-execution progress feedback, enabling efficient event-
triggered agent replanning without continuous agent polling. To obtain diverse
specialized VLA tools that faithfully follow agent invocations, we further propose Tool-
Aligned Post-Training (TAPT), which constructs invocation-aligned training units for
instruction following and adopts tool-family residual adapters for efficient tool
specialization. Experiments show that VLAs-as-Tools improves the success rate of
$π_{0.5}$ by 4.8 points on LIBERO-Long and 23.1 points on RoboTwin, and further enhances
invocation fidelity by 15.0 points as measured by Non-biased Rate. Code will be
released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13119v1
- Authors: Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, Siheng Chen
- Published: 2026-05-13T07:40:34Z
- Age days: 0

</details>
