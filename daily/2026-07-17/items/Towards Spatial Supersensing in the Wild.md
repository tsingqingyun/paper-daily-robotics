---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13681v1"
published: "2026-07-15T10:24:51Z"
age_days: 1
score: 30
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Towards Spatial Supersensing in the Wild

> [!summary] 一句话结论（基于摘要）
> To address the gap, we introduce $\textbf{VSI-Super-Wild}$, a large-scale benchmark for evaluating spatial supersensing over long temporal horizons in diverse in-the-wild scenes.

## 关键点

- **问题**：To mimic this capacity, spatial supersensing challenges multimodal models to move beyond linguistic understanding toward true world modeling.
- **创新点 / 方法**：To address the gap, we introduce $\textbf{VSI-Super-Wild}$, a large-scale benchmark for evaluating spatial supersensing over long temporal horizons in diverse in-the-wild scenes.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：However, their benchmark relies on synthetic long videos, formed by concatenating random short clips, and is mostly limited to household scenes, leaving real-world continuity and diversity underexplored.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humans can efficiently parse continuous sensory streams, from hours to years,
scaffolding an internal world model that grounds spatial reasoning and prediction. To
mimic this capacity, spatial supersensing challenges multimodal models to move beyond
linguistic understanding toward true world modeling. However, their benchmark relies on
synthetic long videos, formed by concatenating random short clips, and is mostly limited
to household scenes, leaving real-world continuity and diversity underexplored. To
address the gap, we introduce $\textbf{VSI-Super-Wild}$, a large-scale benchmark for
evaluating spatial supersensing over long temporal horizons in diverse in-the-wild
scenes. Notably, inspired by cognitive studies on how humans structure experience, we
systematically probe the full triad of world state: the agent (observer), objects (scene
items), and the environment (places and global layout). In total, VSI-Super-Wild
contains $\textbf{6,980}$ human-verified question-answer pairs derived from
$\textbf{442}$ real-world videos spanning 8 scene categories, including long-form
recordings exceeding 4 hours. Results on VSI-Super-Wild expose a fundamental disconnect:
despite advances in static image understanding, models consistently fail at tasks that
require coherent world-state tracking over time. We characterize how performance
degrades with world-state complexity and temporal horizon, and diagnose four failure
modes: spatial collapse, semantic shortcuts, insufficient update, and instance
confusion. This taxonomy reveals that models lack mechanisms to bind objects, agents,
and environments into a unified spatial world model, a fundamental gap that defines the
path forward for spatial supersensing.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13681v1
- Authors: Tianjun Gu, Tianyu Xin, Kuan Zhang, Bowen Yang, Kok-Chung Chua, Peize Li, Xinran Zhang, Yupeng Chen, Qiyue Zhao, Qinlei Xie, Jianhang Liu, Yucheng Lu, Yinan Han, Marco Pavone, Yiming Li
- Published: 2026-07-15T10:24:51Z
- Age days: 1

</details>
