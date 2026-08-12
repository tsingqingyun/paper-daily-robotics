---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18578v1"
published: "2026-07-20T23:19:33Z"
age_days: 1
score: 28
created: 2026-07-22
concepts: ["AI 核心知识地图"]
---

# Two-Stage Extrinsic Calibration of a Static Line-Scanning Lidar with a Rotary Platform

> [!summary] 一句话结论（基于摘要）
> Any inaccuracy in this transformation directly affects the quality of the reconstructed point cloud, leading to misrepresentation of the object of interest.

## 关键点

- **问题**：However, this setup gives rise to the following problem: how can the axis of rotation of the platform be accurately identified with respect to the lidar coordinate system?
- **创新点 / 方法**：A line-scanning lidar yields range and azimuth values in a fixed plane.
- **证据**：Any inaccuracy in this transformation directly affects the quality of the reconstructed point cloud, leading to misrepresentation of the object of interest.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-22/Two-Stage Extrinsic Calibration of a Static Line-Scanning Lidar with a Rotary Pl.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A line-scanning lidar yields range and azimuth values in a fixed plane. To perceive
surrounding objects in 3D, there must be relative motion between the lidar plane and the
object. Thus, using a rotating base-platform is promising for industrial applications
where objects need to be scanned or inspected precisely, and is the main focus of this
work. In the rotary platform setup, a 3D point cloud of an object can be constructed if
the axis of rotation and the precise motion about that axis are known. However, this
setup gives rise to the following problem: how can the axis of rotation of the platform
be accurately identified with respect to the lidar coordinate system? It is referred to
as the calibration problem in the robotics community. Any inaccuracy in this
transformation directly affects the quality of the reconstructed point cloud, leading to
misrepresentation of the object of interest. In this work, we explore automated
approaches to statically and dynamically estimate the transformation of a rotary
platform's axis of rotation with respect to a static line-scanning lidar. The proposed
algorithms have been validated on real-world datasets obtained from a custom made rotary
platform and an FMCW lidar, and their convergence characteristics are studied for
various initial conditions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18578v1
- Authors: Vikram Shree, Hike Danakian, Long Nguyen, Rajanish Gokidi, Patrick Nercessian
- Published: 2026-07-20T23:19:33Z
- Age days: 1

</details>
