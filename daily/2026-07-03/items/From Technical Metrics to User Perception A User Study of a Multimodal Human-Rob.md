---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00530v1"
published: "2026-07-01T07:19:00Z"
age_days: 2
score: 31
created: 2026-07-03
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection and Grasping

> [!summary] 一句话结论（基于摘要）
> Results show that 17 out of 24 participants (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs were rated significantly higher for the improved configuration after Holm correction, with large…

## 关键点

- **问题**：Improvements in the technical performance of human--robot interaction (HRI) systems do not automatically translate into differences that human users can detect during live interaction.
- **创新点 / 方法**：This paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and measurable differences in user perception.
- **证据**：Results show that 17 out of 24 participants (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs were rated significantly higher for the improved configuration after Holm correction, with large to very large effect sizes (p < 0.001).
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Improvements in the technical performance of human--robot interaction (HRI) systems do
not automatically translate into differences that human users can detect during live
interaction. This paper investigates whether a 15 percentage point gain in end-to-end
task success (from 75% in a multimodal baseline system to 90% in an improved
configuration identified through a prior ablation study) is sufficient to produce
consistent and measurable differences in user perception. The baseline system combines
Whisper for speech recognition, Florence-2 for open-vocabulary object detection, LLaMA
3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion
execution. The improved configuration replaces the perception and language modules with
Grounding DINO + SAM and Qwen 3.5 9B, respectively, while retaining the same controller.
A within-subject user study with 24 participants compared both systems on the same
tabletop object-grasping task. After interacting with each configuration, participants
rated perceived speed, reliability, and overall competence and fluency on a 7-point
Likert scale. Results show that 17 out of 24 participants (70.83%) preferred the
improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual
constructs were rated significantly higher for the improved configuration after Holm
correction, with large to very large effect sizes (p < 0.001). These findings confirm
that the identified technical improvements are perceptible to users in direct
interaction and underscore the importance of complementing benchmark evaluation with
user-centred evidence when assessing robotic manipulation pipelines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00530v1
- Authors: Jian Song, Tian Zi, Shen Guanting
- Published: 2026-07-01T07:19:00Z
- Age days: 2

</details>
