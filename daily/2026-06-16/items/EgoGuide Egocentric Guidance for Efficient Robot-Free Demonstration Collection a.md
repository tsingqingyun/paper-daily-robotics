---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14665v1"
published: "2026-06-12T17:36:23Z"
age_days: 3
score: 25
created: 2026-06-16
concepts: ["机器人学习", "具身智能评测与基准"]
---

# EgoGuide: Egocentric Guidance for Efficient Robot-Free Demonstration Collection and Learning

> [!summary] 一句话结论（基于摘要）
> Real-world experiments show that EgoGuide reduces the required number of data episodes and improves data efficiency.

## 关键点

- **问题**：Universal Manipulation Interface (UMI) provides an efficient robot-free data collection interface, yet current UMI-style pipelines often collect redundant demonstrations and lack global scene context.
- **创新点 / 方法**：To improve data efficiency, we present EgoGuide, a collection interface that records synchronized wrist and head/egocentric observations and couples them with online visual-geometric data quality guidance.
- **证据**：Real-world experiments show that EgoGuide reduces the required number of data episodes and improves data efficiency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot learning from real-world demonstrations is currently constrained by data scaling.
Universal Manipulation Interface (UMI) provides an efficient robot-free data collection
interface, yet current UMI-style pipelines often collect redundant demonstrations and
lack global scene context. To improve data efficiency, we present EgoGuide, a collection
interface that records synchronized wrist and head/egocentric observations and couples
them with online visual-geometric data quality guidance. We also introduce a Gated
Egocentric Residual Policy for robust learning from a viewpoint-varying egocentric
camera, allowing head/egocentric context to correct ambiguous local observations while
preserving stable wrist-view control. Real-world experiments show that EgoGuide reduces
the required number of data episodes and improves data efficiency. The residual policy
further improves robustness under visual occlusion. Project Page:
https://silicx.github.io/EgoGuide

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14665v1
- Authors: Yue Xu, Mingtao Nie, Tianle Li, Hong Li, Yibo Luo, Siyuan Huang, Yong-Lu Li
- Published: 2026-06-12T17:36:23Z
- Age days: 3

</details>
