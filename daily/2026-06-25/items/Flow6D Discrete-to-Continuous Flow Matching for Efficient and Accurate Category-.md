---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23293v1"
published: "2026-06-22T13:05:55Z"
age_days: 2
score: 29
created: 2026-06-25
concepts: ["AI 核心知识地图"]
---

# Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation

> [!summary] 一句话结论（基于摘要）
> The framework also naturally extends to articulated objects, outperforming state-of-the-art methods on synthetic and real datasets with real-time inference at 70 FPS.

## 关键点

- **问题**：Existing methods directly regress in a high-dimensional continuous space, facing two key challenges in category-level pose estimation: limited accuracy due to noise and local optima, and inefficient search over an infinite space that hinders real-time performance.
- **创新点 / 方法**：This paper proposes Flow6D, a hierarchical flow matching framework with a two-stage discrete latent space localization-continuous pose regression strategy.
- **证据**：The framework also naturally extends to articulated objects, outperforming state-of-the-art methods on synthetic and real datasets with real-time inference at 70 FPS.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/Flow6D Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

6D pose estimation is a key task in computer vision and embodied AI, widely used in
robotic manipulation, augmented reality, etc. Existing methods directly regress in a
high-dimensional continuous space, facing two key challenges in category-level pose
estimation: limited accuracy due to noise and local optima, and inefficient search over
an infinite space that hinders real-time performance. This paper proposes Flow6D, a
hierarchical flow matching framework with a two-stage discrete latent space
localization-continuous pose regression strategy. Rotation and translation parameters
are first discretized into bins, with a discrete flow matching model locking the latent
space around the true pose to reduce search complexity. Then, by sampling in the latent
space, a continuous flow matching model predicts local pose residuals to optimize the
estimate and regress to an accurate pose. The framework also naturally extends to
articulated objects, outperforming state-of-the-art methods on synthetic and real
datasets with real-time inference at 70 FPS. Project website: https://flow6d.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23293v1
- Authors: Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, Zaixing He
- Published: 2026-06-22T13:05:55Z
- Age days: 2

</details>
