---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17699v1"
published: "2026-07-20T08:47:43Z"
age_days: 1
score: 28
created: 2026-07-22
concepts: ["具身智能评测与基准"]
---

# SLAM in Low-Light Environments: Project Report

> [!summary] 一句话结论（基于摘要）
> Under low illumination, reduced contrast, sensor noise, and motion blur degrade both feature extraction and feature matching, while compensating with LiDAR, depth, or thermal sensors raises cost, power draw, and integration complexity.

## 关键点

- **问题**：Simultaneous localization and mapping (SLAM) is one of the fundamental problems in robotics, as it enables autonomous operations in real-world scenarios.
- **创新点 / 方法**：Under low illumination, reduced contrast, sensor noise, and motion blur degrade both feature extraction and feature matching, while compensating with LiDAR, depth, or thermal sensors raises cost, power draw, and integration complexity.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Simultaneous localization and mapping (SLAM) is one of the fundamental problems in
robotics, as it enables autonomous operations in real-world scenarios. Under low
illumination, reduced contrast, sensor noise, and motion blur degrade both feature
extraction and feature matching, while compensating with LiDAR, depth, or thermal
sensors raises cost, power draw, and integration complexity. Existing benchmarks remain
dominated by well-lit indoor or daylight sequences, leaving open how far SLAM with
standard RGB cameras can be pushed in the dark. We benchmark six systems spanning the
feature-based, direct, filter-based, and learning-based paradigms - ORB-SLAM3, DSO,
Kimera-VIO, OpenVINS, DPVO, and DPV-SLAM - on five LaMARia sequences of varying
difficulty and illumination, reporting absolute and relative pose error alongside
control-point recall. Kimera-VIO is the only system to track all five sequences to
completion, combining the lowest relative pose error with steadily growing absolute
error due to the absence of loop closure; DPVO and DPV-SLAM never lose tracking but
incur absolute errors of roughly 100 m under low light; and the classical monocular
pipelines (ORB-SLAM3, DSO) together with the filter-based OpenVINS fail outright or
diverge on most of the harder and low-light sequences. The results suggest that RGB-only
SLAM maintains stable low-light tracking only when both inertial fusion and global
optimization are present. Closing the remaining gap will likely require low-light-
specific learned front-ends or a return to complementary sensing.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17699v1
- Authors: Oleh Basystyi, Anna Stasyshyn, Oleksandr Kosovan, Yaroslav Prytula
- Published: 2026-07-20T08:47:43Z
- Age days: 1

</details>
