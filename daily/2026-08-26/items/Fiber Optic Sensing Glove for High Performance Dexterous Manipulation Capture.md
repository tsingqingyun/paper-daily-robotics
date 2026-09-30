---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.24572v1"
published: "2026-08-25T13:59:35Z"
age_days: 0
score: 32
created: 2026-08-26
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Fiber Optic Sensing Glove for High Performance Dexterous Manipulation Capture

> [!summary] 一句话结论（基于摘要）
> Benchmarked on a 2-hour dataset of dexterous object manipulation tasks across 5 subjects, the glove achieves 7.2 mm mean fingertip position error against motion capture ground truth, reduced to 4.9 mm by a one-time factory calibration of the fiber routing hub…

## 关键点

- **问题**：Capturing hand pose during dexterous manipulation remains difficult: vision-based methods degrade under occlusion and challenging lighting, while sensorized gloves, though occlusion-free, are prone to drift and magnetic interference and rarely match motion-capture accuracy.
- **创新点 / 方法**：We introduce a fiber optic sensing glove for full hand pose tracking that targets these failure modes, using multi-core shape-sensing fibers that capture each fiber's full 3D shape rather than curvature alone.
- **证据**：Benchmarked on a 2-hour dataset of dexterous object manipulation tasks across 5 subjects, the glove achieves 7.2 mm mean fingertip position error against motion capture ground truth, reduced to 4.9 mm by a one-time factory calibration of the fiber routing hub that transfers across users and sessions.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Fiber Optic Sensing Glove for High Performance Dexterous Manipulation Capture.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Capturing hand pose during dexterous manipulation remains difficult: vision-based methods degrade under occlusion and challenging lighting, while sensorized gloves, though occlusion-free, are prone to drift and magnetic interference and rarely match motion-capture accuracy. We introduce a fiber optic sensing glove for full hand pose tracking that targets these failure modes, using multi-core shape-sensing fibers that capture each fiber's full 3D shape rather than curvature alone. A novel pipeline registers each reconstructed fiber shape to a common hand reference frame, and a new inverse-kinematics solver reconstructs full hand pose at 60 Hz using curve constraints. Benchmarked on a 2-hour dataset of dexterous object manipulation tasks across 5 subjects, the glove achieves 7.2 mm mean fingertip position error against motion capture ground truth, reduced to 4.9 mm by a one-time factory calibration of the fiber routing hub that transfers across users and sessions. These capabilities enable high-fidelity data capture and bimanual virtual teleoperation - both essential to advancing the robotics field.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.24572v1
- Authors: J. D. Peiffer, Taylor Niehues, Li Guan, Ziyi Kou, Ergys Ristani
- Published: 2026-08-25T13:59:35Z
- Age days: 0

</details>
