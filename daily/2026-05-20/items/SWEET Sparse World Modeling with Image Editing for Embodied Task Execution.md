---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19319v1"
published: "2026-05-19T03:54:46Z"
age_days: 0
score: 30
created: 2026-05-20
concepts: ["智能体 Agent", "世界模型"]
---

# SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution

> [!summary] 一句话结论（基于摘要）
> Experiments on DROID and RoboMimic show that SWEET improves keyframe prediction across seen and unseen scenes and enables a full pipeline from sequential keyframe planning to executable robot actions, suggesting that image editing is a promising and underexpl…

## 关键点

- **问题**：However, dense video generation is computationally expensive and often unnecessary for many manipulation tasks, whose progress can be summarized by a small number of task-relevant visual states.
- **创新点 / 方法**：Motivated by this observation, we propose SWEET, a one-shot sparse visual planning framework that progressively generates a sequence of task-relevant manipulation keyframes through successive image editing, conditioned on language instructions and optional arrow-based spatial guidance.
- **证据**：Experiments on DROID and RoboMimic show that SWEET improves keyframe prediction across seen and unseen scenes and enables a full pipeline from sequential keyframe planning to executable robot actions, suggesting that image editing is a promising and underexplored direction for embodied visual prediction.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-20/SWEET Sparse World Modeling with Image Editing for Embodied Task Execution.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual prediction has emerged as a promising paradigm for embodied control, where future
observations are generated and then translated into actions. However, dense video
generation is computationally expensive and often unnecessary for many manipulation
tasks, whose progress can be summarized by a small number of task-relevant visual
states. In this work, we study whether image editing models can serve as sparse visual
world models for robot manipulation by predicting task-level future states without dense
video rollout. We first conduct a controlled comparison between the video generation
model Wan2.2 and the image editing model FLUX-Kontext under the same robotic data
setting, and find that image editing produces more reliable task-level keyframes with
better visual fidelity and substantially lower inference cost. Motivated by this
observation, we propose SWEET, a one-shot sparse visual planning framework that
progressively generates a sequence of task-relevant manipulation keyframes through
successive image editing, conditioned on language instructions and optional arrow-based
spatial guidance. A goal-conditioned diffusion action predictor then converts adjacent
imagined keyframes into executable action chunks. To reduce the mismatch between real
and edited visual subgoals, we further introduce a mixed-training strategy with filtered
edited targets. Experiments on DROID and RoboMimic show that SWEET improves keyframe
prediction across seen and unseen scenes and enables a full pipeline from sequential
keyframe planning to executable robot actions, suggesting that image editing is a
promising and underexplored direction for embodied visual prediction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19319v1
- Authors: Yiren Song, Yihan Wang, Xiyao Deng, Zhuoran Yan, Mike Zheng Shou
- Published: 2026-05-19T03:54:46Z
- Age days: 0

</details>
