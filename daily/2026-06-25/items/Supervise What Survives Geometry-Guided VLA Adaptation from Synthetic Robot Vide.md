---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24448v1"
published: "2026-06-23T11:35:13Z"
age_days: 1
score: 33
created: 2026-06-25
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos

> [!summary] 一句话结论（基于摘要）
> On real-robot tasks, GRA outperforms pseudo-action baselines under matched data budgets and narrows the gap to policies trained with substantially more real demonstrations, suggesting that correctly routed geometry bridges generated videos to robot policies m…

## 关键点

- **问题**：Vision-Language-Action (VLA) models require large-scale video-action pairs, yet real teleoperation remains scarce.
- **创新点 / 方法**：Following this principle, we propose \textbf{GRA} (\textbf{G}eometry-guided \textbf{R}epresentation \textbf{A}lignment), which extracts the geometric content as future 2D end-effector waypoints, computed from the source human video through pose estimation, retargeting, simulation, and calibrated projection, and routes…
- **证据**：On real-robot tasks, GRA outperforms pseudo-action baselines under matched data budgets and narrows the gap to policies trained with substantially more real demonstrations, suggesting that correctly routed geometry bridges generated videos to robot policies more reliably than recovered actions.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/Supervise What Survives Geometry-Guided VLA Adaptation from Synthetic Robot Vide.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models require large-scale video-action pairs, yet real
teleoperation remains scarce. While generated robot videos offer a scalable alternative,
existing methods treat them as real robot data by recovering pseudo-actions from
synthesized pixels. We argue that deriving low-level control from generated visuals is a
mismatched abstraction. A video captures only \emph{geometry}: the spatial trajectory
representing the \emph{where} of a task. A real demonstration captures \emph{control}:
the exact motor commands representing the \emph{how}. Human-to-robot video generation
preserves these unequally: the visible geometry survives the generation process, while
the underlying control signals are lost. This \textbf{Asymmetric Preservation Principle}
dictates a clean rule: this surviving geometry should solely supervise visual
perception, leaving control to real demonstrations. Following this principle, we propose
\textbf{GRA} (\textbf{G}eometry-guided \textbf{R}epresentation \textbf{A}lignment),
which extracts the geometric content as future 2D end-effector waypoints, computed from
the source human video through pose estimation, retargeting, simulation, and calibrated
projection, and routes them to the VLA vision backbone via an auxiliary 2D head. The
action head is trained on real demonstrations only. During fine-tuning, the waypoint
loss persists as a \textbf{spatial representation anchor} that prevents the backbone
from losing its geometric grounding. On real-robot tasks, GRA outperforms pseudo-action
baselines under matched data budgets and narrows the gap to policies trained with
substantially more real demonstrations, suggesting that correctly routed geometry
bridges generated videos to robot policies more reliably than recovered actions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24448v1
- Authors: Danze Chen, Yanzhe Chen, Qiming Huang, Zhijun Cao, Chen Gao, Mike Zheng Shou
- Published: 2026-06-23T11:35:13Z
- Age days: 1

</details>
