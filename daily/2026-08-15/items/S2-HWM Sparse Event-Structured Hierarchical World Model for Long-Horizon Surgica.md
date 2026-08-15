---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13103v1"
published: "2026-08-13T11:29:20Z"
age_days: 1
score: 29
created: 2026-08-15
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> On a SurRoL-based PegTransfer task, S2-HWM achieves a success rate of 98.7%, outperforming the flat GAS DreamerV3 baseline by 22.7 percentage points.

## 关键点

- **问题**：Manually specified stages can provide intermediate structure, but their task specific boundaries are difficult to align with state-dependent interaction transitions.
- **创新点 / 方法**：We propose S2-HWM, a Sparse Event-Structured Hierarchical World Model that learns sparse event evidence from primitive latent trajectories to coordinate an event-level manager and a primitive-step worker.
- **证据**：On a SurRoL-based PegTransfer task, S2-HWM achieves a success rate of 98.7%, outperforming the flat GAS DreamerV3 baseline by 22.7 percentage points.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/S2-HWM Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgica.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon surgical robot manipulation is challenging because task rewards are sparse, while meaningful interaction changes occur at irregular intervals. Existing world-model agents typically imagine at primitive-step resolution, leaving variable-duration task progress implicit. Manually specified stages can provide intermediate structure, but their task specific boundaries are difficult to align with state-dependent interaction transitions. We propose S2-HWM, a Sparse Event-Structured Hierarchical World Model that learns sparse event evidence from primitive latent trajectories to coordinate an event-level manager and a primitive-step worker. The event evidence schedules manager goal updates, and each selected latent goal conditions the worker's primitive actions until the next update. The learned event evidence also forms variable-duration segments for an Event Transition Model (ETM), which predicts the next?boundary stochastic state, segment duration, and accumulated segment reward. Chaining these event-level predictions provides a variable-duration continuation beyond the primitive imagination horizon for manager learning, while the worker retains primitive-step actor-critic learning. On a SurRoL-based PegTransfer task, S2-HWM achieves a success rate of 98.7%, outperforming the flat GAS DreamerV3 baseline by 22.7 percentage points.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13103v1
- Authors: Shuzhe Zhang, Xin Zhu, Yinling Qian, Qiong Wang
- Published: 2026-08-13T11:29:20Z
- Age days: 1

</details>
