---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14852v1"
published: "2026-07-16T11:22:06Z"
age_days: 1
score: 35
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation…

## 关键点

- **问题**：However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models.
- **创新点 / 方法**：To address this fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the plasticity-stability trade-off with a dual-timescale adaptation mechanism while achieving low-cost robotic deployment with a cache-ef…
- **证据**：However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/Towards Human-like Physical Intelligence LifelongVision-Language-Action Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Similar to the natural capabilities of humans to sequentially learn new tasks, robots
with Vision-Language-Action (VLA) models should possess lifelong learning ability to
learn a new task when deployed in open-world environments. However, most recently
proposed lifelong learning models aim to effectively learn the current task (plasticity)
or maintain high accuracy on previous tasks (stability), while the plasticity-stability
trade-off remains largely unsolved in robotic manipulation models. To address this
fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action
learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the
plasticity-stability trade-off with a dual-timescale adaptation mechanism while
achieving low-cost robotic deployment with a cache-efficient replay strategy. More
concretely, we propose a dual-timescale LoRA gating module to decompose VLA adaptation
into two lightweight pathways: a short-term adapter for plasticity and a long-term
adapter for stable consolidation. These pathways are integrated via a task-aware gate,
enabling explicit control of the plasticity-stability trade-off. In the skill replay
phase, a cache-efficient stochastic replay strategy is proposed to preserve more
balanced retention signals without full-trajectory storage. Finally, experiments show
that LifelongVLA outperforms existing baselines, demonstrating efficient skill
expansion, robust retention of learned manipulation behaviors, and reduced reliance on
retraining for real-world deployment on an xArm robot.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14852v1
- Authors: Yao He, Gan Sun, Wenqi Liang, Fazeng Li, Yang Cong
- Published: 2026-07-16T11:22:06Z
- Age days: 1

</details>
