---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12028v1"
published: "2026-06-10T12:51:25Z"
age_days: 1
score: 31
created: 2026-06-12
concepts: ["多模态基础模型"]
---

# VICX: Generalizable Robot Manipulation via Video Generation and In-Context Operator Network

> [!summary] 一句话结论（基于摘要）
> To bridge this gap, we propose VICX (Video generation and In-Context eXecution), a decoupled closed-loop manipulation framework.

## 关键点

- **问题**：Generalizable robot manipulation requires not only task-level reasoning over unseen scenes, but also reliable grounding of visual plans into embodiment-specific execution.
- **创新点 / 方法**：To bridge this gap, we propose VICX (Video generation and In-Context eXecution), a decoupled closed-loop manipulation framework.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/VICX Generalizable Robot Manipulation via Video Generation and In-Context Operat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalizable robot manipulation requires not only task-level reasoning over unseen
scenes, but also reliable grounding of visual plans into embodiment-specific execution.
To bridge this gap, we propose VICX (Video generation and In-Context eXecution), a
decoupled closed-loop manipulation framework. In VICX, a frozen video generation model
produces vision-language-conditioned high-level visual plans, while a Video-to-
Trajectory In-Context Operator Network (V2T-ICON) serves as the task-agnostic interface
that grounds these plans into executable robot-state trajectories. To improve execution
generalization, V2T-ICON operates on segmentation-extracted arm-only frame observations
and uses retrieved image-state pairs as in-context prompts, allowing a robust and
generalizable visual-to-state mapping at inference time without parameter updates.
Experiments on Meta-World show that VICX supports cross-task generalization, closed-loop
self-correction, and cross-embodiment transfer, demonstrating dual generalization across
both task semantics and robot execution. The project webpage can be found here:
https://scaling-group.github.io/vicx/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12028v1
- Authors: Song Chen, Linyan Xiang, Ying Zhou, Liu Yang
- Published: 2026-06-10T12:51:25Z
- Age days: 1

</details>
