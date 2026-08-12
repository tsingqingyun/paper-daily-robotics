---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06493v1"
published: "2026-06-04T17:59:50Z"
age_days: 3
score: 30
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

> [!summary] 一句话结论（基于摘要）
> To this end, we introduce HANDOFF, a single humanoid whole- body controller that follows this interface and is distilled via multi-teacher KL distillation under a context-conditioned gating scheme into a mixture-of-experts student from three complementary spe…

## 关键点

- **问题**：Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics.
- **创新点 / 方法**：To this end, we introduce HANDOFF, a single humanoid whole- body controller that follows this interface and is distilled via multi-teacher KL distillation under a context-conditioned gating scheme into a mixture-of-experts student from three complementary specialists: whole-body motion tracking with safety-filtered da…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/HANDOFF Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementa.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

For a humanoid robot to be deployed in the real world, the choice of command space
(i.e., the interface between task planning and whole-body control) is crucial. Existing
whole-body controllers typically demand dense kinematic or spatial references that
planners struggle to synthesize from task semantics. We instead propose a compact,
explicit interface that is intuitive, general, modular, and expressive enough for
diverse manipulation skills. To this end, we introduce HANDOFF, a single humanoid whole-
body controller that follows this interface and is distilled via multi-teacher KL
distillation under a context-conditioned gating scheme into a mixture-of-experts student
from three complementary specialists: whole-body motion tracking with safety-filtered
data, locomotion, and fall-recovery. On the Unitree G1, HANDOFF matches state-of-the-art
velocity tracking and offers one of the largest robust manipulation workspaces. We
further demonstrate hardware feasibility through multiple natural-language-driven task
roll-outs, powered by a VLM-driven agentic planner with no task-specific data or
controller fine-tuning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06493v1
- Authors: Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames
- Published: 2026-06-04T17:59:50Z
- Age days: 3

</details>
