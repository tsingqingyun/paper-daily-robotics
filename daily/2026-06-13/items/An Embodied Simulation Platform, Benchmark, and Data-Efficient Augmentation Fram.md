---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12936v1"
published: "2026-06-11T05:58:38Z"
age_days: 1
score: 42
created: 2026-06-13
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics

> [!summary] 一句话结论（基于摘要）
> We further introduce an 11-task wet-lab embodied benchmark covering sample handling, culture-ware manipulation, device operation, and precision placement.

## 关键点

- **问题**：Wet-lab robots can improve the reproducibility, throughput, and safety of biomedical experiments, but scaling their learning requires customizable simulators for safe and reproducible task generation, open editable laboratory assets, and efficient pipelines that turn limited demonstrations into usable training data.
- **创新点 / 方法**：We present Pipette, an embodied simulation platform, benchmark, and data-efficient augmentation framework for wet-lab robot learning.
- **证据**：We further introduce an 11-task wet-lab embodied benchmark covering sample handling, culture-ware manipulation, device operation, and precision placement.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Wet-lab robots can improve the reproducibility, throughput, and safety of biomedical
experiments, but scaling their learning requires customizable simulators for safe and
reproducible task generation, open editable laboratory assets, and efficient pipelines
that turn limited demonstrations into usable training data. We present Pipette, an
embodied simulation platform, benchmark, and data-efficient augmentation framework for
wet-lab robot learning. Pipette releases over 43 open-source and re-editable wet-lab
assets, together with an extensible asset-building pipeline. A key component of Pipette
is its simulation-based data augmentation pipeline, replaying human demonstrations in
simulation, applies lighting, camera, speed, and action perturbations, and filters
generated episodes with automatic task success checks, rapidly expanding usable training
data from limited manual demonstrations. We further introduce an 11-task wet-lab
embodied benchmark covering sample handling, culture-ware manipulation, device
operation, and precision placement. With only 30 demonstrations per task, ACT achieves
65.5% average success rate, while simulation augmentation improves SmolVLA from 44.1% to
74.7% and π0 from 40.4% to 46.5%, validating the effectiveness of Pipette for data-
efficient VLA training and evaluation. Pipette also supports natural-language-driven
scene construction and task registration, lowering the barrier for non-expert users to
define new wet-lab robotic tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12936v1
- Authors: Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu, Peijia Li, Jiaming Gu, Quan Lu, Qi Wang, Bin Ji, Ting Xiao
- Published: 2026-06-11T05:58:38Z
- Age days: 1

</details>
