---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01212v1"
published: "2026-07-01T17:51:21Z"
age_days: 1
score: 35
created: 2026-07-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model

> [!summary] 一句话结论（基于摘要）
> FurnitureVLA improves average simulation success from 48% to 80% compared to baselines across three furniture types, with an additional 21% gain from our design factor study.

## 关键点

- **问题**：Current work on robot furniture assembly mostly focuses on toy-scale settings or single- arm manipulation.
- **创新点 / 方法**：We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture assembly using Vision-Language-Action models (VLAs).
- **证据**：FurnitureVLA improves average simulation success from 48% to 80% compared to baselines across three furniture types, with an additional 21% gain from our design factor study.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Current work on robot furniture assembly mostly focuses on toy-scale settings or single-
arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale
bimanual furniture assembly using Vision-Language-Action models (VLAs). We formalize the
task, develop a scalable simulation pipeline for expert data generation and evaluation,
and build a VR teleoperation system for single-operator bimanual control to collect
high-quality real-world demonstrations. To address extreme long-horizon assembly with up
to 7 subtasks and 1550 control steps, we propose a progress-enhanced VLA, finetuned on
semantically grounded subtasks, that jointly predicts actions and a continuous progress
signal, enabling automatic subtask transitions and reducing compounding errors during
inference. We further study perception and control design factors that critically affect
precision in real-scale assembly. FurnitureVLA improves average simulation success from
48% to 80% compared to baselines across three furniture types, with an additional 21%
gain from our design factor study. We validate on a real Kinova Gen3 platform with only
16% drop on the hardest task.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01212v1
- Authors: Chenyang Ma, Yue Yang, Radu Corcodel, Siddarth Jain, Andrew Wu, Chiori Hori, Diego Romeres
- Published: 2026-07-01T17:51:21Z
- Age days: 1

</details>
