---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.11051v1"
published: "2026-08-11T15:22:14Z"
age_days: 3
score: 32
created: 2026-08-15
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation

> [!summary] 一句话结论（基于摘要）
> To this end, we introduce HUI360, the largest dataset for human-robot interaction anticipation in the wild and its set of baselines.

## 关键点

- **问题**：Automatic anticipation of human-robot interactions is thus emerging as a crucial perception challenge for embodied agents.
- **创新点 / 方法**：To this end, we introduce HUI360, the largest dataset for human-robot interaction anticipation in the wild and its set of baselines.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/HUI360 A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Antic.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As robots increasingly operate in human-populated environments, anticipating human intentions is essential for enabling proactive and socially aware behavior. Automatic anticipation of human-robot interactions is thus emerging as a crucial perception challenge for embodied agents. To this end, we introduce HUI360, the largest dataset for human-robot interaction anticipation in the wild and its set of baselines. The dataset was collected from a mobile robot, in the wild, over multiple days within a 3-month period, and in several environments, capturing natural, spontaneous behaviors from both passersby and users, and encompassing a diverse range of individuals. This variety enables evaluating and improving the generalization capabilities of interaction anticipation models. We designed a pipeline and share code for automatic interaction annotation in arbitrary 360-degree equirectangular videos, along with interfaces for manual refinement. Using this pipeline, we release the HUI360 open set of 1M pre-processed annotations, including detailed 2D poses, facial keypoints, and segmentation masks, obtained using state-of-the-art computer vision methods and manually curated to ensure high-quality tracking and interaction annotation. Additionally, we release the raw panoptic 360-degree images captured from the robot's egocentric viewpoint (on demand, for research purpose only in compliance with GDPR). Finally, we establish benchmark baselines for interaction anticipation, including the first cross-dataset evaluations for this task: to this end, we also release 6M annotations for another existing in-the-wild outdoor dataset collected from a mobile robot (SSUP-HRI). Dataset and code can be found at https://hucebot.github.io/hui360.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.11051v1
- Authors: Raphael Lorenzo-Louis, Fabio Amadio, Bertrand Luvison, Serena Ivaldi
- Published: 2026-08-11T15:22:14Z
- Age days: 3

</details>
