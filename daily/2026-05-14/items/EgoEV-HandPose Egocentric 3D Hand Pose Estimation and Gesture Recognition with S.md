---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12297v1"
published: "2026-05-12T15:51:04Z"
age_days: 1
score: 32
created: 2026-05-14
concepts: ["具身智能评测与基准"]
---

# EgoEV-HandPose: Egocentric 3D Hand Pose Estimation and Gesture Recognition with Stereo Event Cameras

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that EgoEV-HandPose achieves state-of-the-art performance with an MPJPE of 30.54mm and 86.87% Top-1 gesture recognition accuracy, significantly outperforming RGB-based stereo and prior event-camera methods, particularly in lo…

## 关键点

- **问题**：However, conventional frame-based cameras suffer from motion blur and limited dynamic range, while existing event-based methods are hindered by ego-motion interference, monocular depth ambiguity, and the lack of large-scale real-world stereo datasets.
- **创新点 / 方法**：To overcome these limitations, we propose EgoEV-HandPose, an end-to-end framework for joint 3D bimanual pose estimation and gesture recognition from stereo event streams.
- **证据**：Extensive experiments demonstrate that EgoEV-HandPose achieves state-of-the-art performance with an MPJPE of 30.54mm and 86.87% Top-1 gesture recognition accuracy, significantly outperforming RGB-based stereo and prior event-camera methods, particularly in low-light and bimanual occlusion scenarios, thereby setting a…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/EgoEV-HandPose Egocentric 3D Hand Pose Estimation and Gesture Recognition with S.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric 3D hand pose estimation and gesture recognition are essential for immersive
augmented/virtual reality, human-computer interaction, and robotics. However,
conventional frame-based cameras suffer from motion blur and limited dynamic range,
while existing event-based methods are hindered by ego-motion interference, monocular
depth ambiguity, and the lack of large-scale real-world stereo datasets. To overcome
these limitations, we propose EgoEV-HandPose, an end-to-end framework for joint 3D
bimanual pose estimation and gesture recognition from stereo event streams. Central to
our approach is KeypointBEV, a flexible stereo fusion module that lifts features into a
canonical bird's-eye-view space and employs an iterative reprojection-guided refinement
loop to progressively resolve depth uncertainty and enforce kinematic consistency. In
addition, we introduce EgoEVHands, the first large-scale real-world stereo event-camera
dataset for egocentric hand perception, containing 5,419 annotated sequences with dense
3D/2D keypoints across 38 gesture classes under varying illumination. Extensive
experiments demonstrate that EgoEV-HandPose achieves state-of-the-art performance with
an MPJPE of 30.54mm and 86.87% Top-1 gesture recognition accuracy, significantly
outperforming RGB-based stereo and prior event-camera methods, particularly in low-light
and bimanual occlusion scenarios, thereby setting a new benchmark for event-based
egocentric perception. The established dataset and source code will be publicly released
at https://github.com/ZJUWang01/EgoEV-HandPose.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12297v1
- Authors: Luming Wang, Hao Shi, Jiajun Zhai, Kailun Yang, Kaiwei Wang
- Published: 2026-05-12T15:51:04Z
- Age days: 1

</details>
