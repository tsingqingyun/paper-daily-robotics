---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05586v1"
published: "2026-08-06T04:17:13Z"
age_days: 4
score: 25
created: 2026-08-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# PathCover: A Fast Convex Decomposition along a Path via Randomized Iterative Space Partitioning (RISP) on Point Clouds

> [!summary] 一句话结论（基于摘要）
> To resolve this bottleneck, we introduce PathCover, a framework driven by RISP; a novel randomized algorithm that constructs convex polytopes directly from raw point cloud data in expected linear time under a mild probabilistic elimination condition.

## 关键点

- **问题**：However, existing corridor generators struggle to meet real-time, sensor-rate computational constraints.
- **创新点 / 方法**：To resolve this bottleneck, we introduce PathCover, a framework driven by RISP; a novel randomized algorithm that constructs convex polytopes directly from raw point cloud data in expected linear time under a mild probabilistic elimination condition.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/PathCover A Fast Convex Decomposition along a Path via Randomized Iterative Spac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous robot navigation requires the rapid generation of obstacle-free regions for
trajectory planning. However, existing corridor generators struggle to meet real-time,
sensor-rate computational constraints. To resolve this bottleneck, we introduce
PathCover, a framework driven by RISP; a novel randomized algorithm that constructs
convex polytopes directly from raw point cloud data in expected linear time under a mild
probabilistic elimination condition. PathCover generates sequences of overlapping,
obstacle-free polytopes that safely constrain downstream MPC and trajectory
optimization. We mathematically guarantee that the algorithm terminates in finite steps
while ensuring continuous progress along any obstacle-free reference path. Extensive
benchmarks on synthetic and real-world LiDAR datasets demonstrate an order-of-magnitude
speedup over state-of-the-art methods while maintaining comparable corridor volumes. The
complete pipeline is validated via high-fidelity quadrotor simulations and physical
deployment on a quadrupedal robot navigating constrained environments using live LiDAR
perception.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05586v1
- Authors: Kunal S. Narkhede, Abhijeet M. Kulkarni, Guoquan Huang, Ioannis Poulakakis
- Published: 2026-08-06T04:17:13Z
- Age days: 4

</details>
