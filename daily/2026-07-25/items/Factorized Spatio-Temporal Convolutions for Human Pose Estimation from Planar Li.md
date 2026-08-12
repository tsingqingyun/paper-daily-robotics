---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21309v1"
published: "2026-07-23T13:31:54Z"
age_days: 1
score: 24
created: 2026-07-25
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar

> [!summary] 一句话结论（基于摘要）
> Quantitative experiments show that our approach consistently outperforms a parameter-matched baseline model, reducing errors in distance (-38%), position (-28%), and orientation (-15%).

## 关键点

- **问题**：Localizing nearby humans and estimating their facing direction are key capabilities for safe navigation and socially aware human-robot interaction.
- **创新点 / 方法**：Quantitative experiments show that our approach consistently outperforms a parameter-matched baseline model, reducing errors in distance (-38%), position (-28%), and orientation (-15%).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Li.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Localizing nearby humans and estimating their facing direction are key capabilities for
safe navigation and socially aware human-robot interaction. Many pose-estimation
pipelines target cameras and 3D LiDAR or assume GPU-class compute, whereas service
robots are often equipped only with omnidirectional planar LiDARs and modest onboard
processors. We address omnidirectional human detection and relative 2D pose estimation
from planar LiDAR sequences with a lightweight network based on Space-Time Blocks, which
explicitly separate spatial processing along scan rays from temporal aggregation across
scans. Our network processes 360° LiDAR sequences to output per-ray human presence,
distance, and relative orientation. We train it via cross-modal self-supervision from a
narrow RGB-D body tracker in the sensors' overlap region, removing the need for manual
LiDAR labels. Quantitative experiments show that our approach consistently outperforms a
parameter-matched baseline model, reducing errors in distance (-38%), position (-28%),
and orientation (-15%). We further benchmark on the public FROG dataset, report real-
time CPU inference on a service robot, and validate with in-field demonstrations,
supporting its suitability for spatial perception on computationally constrained service
robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21309v1
- Authors: Simone Arreghini, Mirko Nava, Nicholas Carlotti, Antonio Paolillo, Alessandro Giusti
- Published: 2026-07-23T13:31:54Z
- Age days: 1

</details>
