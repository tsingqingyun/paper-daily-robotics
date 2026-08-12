---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06836v1"
published: "2026-06-05T02:23:05Z"
age_days: 2
score: 33
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation

> [!summary] 一句话结论（基于摘要）
> Its trained Streaming Pilot Reasoning VLM further improves UAV video reasoning, validating the effectiveness of our design.

## 关键点

- **问题**：Language-guided UAV agents must execute long-horizon semantic instructions while producing smooth, physically feasible continuous flight commands, yet existing Vision- Language Navigation (VLN) benchmarks typically use discrete or coarse actions and existing UAV Vision-Language-Action (VLA) tasks focus on short, atomi…
- **创新点 / 方法**：To address this gap in UAV task settings, we introduce \textbf{FLIGHT}, a \textbf{F}ine- grained \textbf{L}ong-horizon \textbf{I}nstruction-\textbf{G}uided benchmark for \textbf{H}ybrid UAV navigation and reasoning \textbf{T}asks, which combines multi-stage instructions with dense 6-DoF trajectory annotations across t…
- **证据**：Its trained Streaming Pilot Reasoning VLM further improves UAV video reasoning, validating the effectiveness of our design.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Language-guided UAV agents must execute long-horizon semantic instructions while
producing smooth, physically feasible continuous flight commands, yet existing Vision-
Language Navigation (VLN) benchmarks typically use discrete or coarse actions and
existing UAV Vision-Language-Action (VLA) tasks focus on short, atomic maneuvers. To
address this gap in UAV task settings, we introduce \textbf{FLIGHT}, a \textbf{F}ine-
grained \textbf{L}ong-horizon \textbf{I}nstruction-\textbf{G}uided benchmark for
\textbf{H}ybrid UAV navigation and reasoning \textbf{T}asks, which combines multi-stage
instructions with dense 6-DoF trajectory annotations across two dataset splits: Fine-
grained VLN and Long-horizon Flow. To endow the UAV agent with the capability of real-
time in-flight reasoning over task execution status and mission planning, while
simultaneously accommodating high-frequency, real-time precise control, we further
propose \textbf{FLIGHT VLA}, an asynchronous architecture that decouples a low-frequency
Streaming Pilot Vision-Language Model (VLM) for task-state reasoning from a high-
frequency diffusion action model for continuous control, supervised by explicit
\textbf{Pilot Reasoning} texts that summarize the current flight state and anticipate
the next subgoal. In closed-loop evaluation, FLIGHT VLA consistently surpasses
representative VLN and VLA baselines on our FLIGHT benchmarks, achieving stronger multi-
stage completion, subgoal adherence, and terminal control. Its trained Streaming Pilot
Reasoning VLM further improves UAV video reasoning, validating the effectiveness of our
design.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06836v1
- Authors: Xiangyi Zheng, Xiangyu Wang, Qinan Liao, Zimu Tang, Yue Liao, Dongyue Lyu, Guodong Wang, Junjie Liu, Si Liu
- Published: 2026-06-05T02:23:05Z
- Age days: 2

</details>
