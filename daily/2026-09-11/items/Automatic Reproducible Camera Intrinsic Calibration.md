---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10082v1"
published: "2026-09-09T12:05:17Z"
age_days: 1
score: 25
created: 2026-09-11
concepts: ["AI 核心知识地图"]
---

# Automatic Reproducible Camera Intrinsic Calibration

> [!summary] 先说人话（基于摘要）
> Accurate camera intrinsic calibration is fundamental to robot perception, and the accuracy depends on the quality of the collected images.

## 这篇到底在做什么

- **卡在哪里**：However, existing target-based calibration methods often require the practitioner to manually filter out high-quality images and to specify an appropriate radial distortion order.
- **关键解法**：Accurate camera intrinsic calibration is fundamental to robot perception, and the accuracy depends on the quality of the collected images.
- **拿什么证明**：Accurate camera intrinsic calibration is fundamental to robot perception, and the accuracy depends on the quality of the collected images.

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Automatic Reproducible Camera Intrinsic Calibration.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Accurate camera intrinsic calibration is fundamental to robot perception, and the accuracy depends on the quality of the collected images. However, existing target-based calibration methods often require the practitioner to manually filter out high-quality images and to specify an appropriate radial distortion order. This paper presents a fully automatic intrinsic calibration pipeline that determines both from the collected data. We adopt an iterative rejection scheme that estimates parameters on a candidate image set and removes views whose mean residual exceeds a multiple of the median. Crucially, this process runs independently under each candidate distortion order, so that the retained image set is consistent with the residual scale of that order. Further, the distortion order is selected on held-out images, with the intrinsics and distortion fixed and only the board pose re-estimated, ensuring that an added coefficient is supported by independent observations. Finally, we integrate both steps into an interactive calibration tool that supports full-pipeline data inspection and parameter estimation. Experiments on our own camera data and five public real-world datasets show that image filtering reduces the held-out reprojection error by 25\%, the order selection further by 5\%, achieving the lowest held-out mean among four compared configurations without manual image selection. We will release the code and data to facilitate future research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10082v1
- Authors: Xiangcheng Hu
- Published: 2026-09-09T12:05:17Z
- Age days: 1

</details>
