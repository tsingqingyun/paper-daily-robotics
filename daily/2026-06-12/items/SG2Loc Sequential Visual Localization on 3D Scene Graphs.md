---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11880v1"
published: "2026-06-10T10:03:21Z"
age_days: 1
score: 32
created: 2026-06-12
concepts: ["智能体 Agent"]
---

# SG2Loc: Sequential Visual Localization on 3D Scene Graphs

> [!summary] 一句话结论（基于摘要）
> Our method represents the environment with a compact scene graph, where nodes represent objects (with coarse meshes) and edges encode spatial relationships.

## 关键点

- **问题**：Visual localization in complex indoor environments remains a critical challenge for robotics and AR applications.
- **创新点 / 方法**：Our method represents the environment with a compact scene graph, where nodes represent objects (with coarse meshes) and edges encode spatial relationships.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual localization in complex indoor environments remains a critical challenge for
robotics and AR applications. Sequential localization, where pose estimates are refined
over time, is important for autonomous agents. However, traditional methods often
require storing extensive image databases or point clouds, leading to significant
overhead. This paper introduces a novel, lightweight approach to sequential visual
localization using 3D scene graphs. Our method represents the environment with a compact
scene graph, where nodes represent objects (with coarse meshes) and edges encode spatial
relationships. For each image in the localization phase, we extract per-patch semantic
features, predicting object identities. Localization is performed within a particle
filter framework. Each particle, representing a camera pose, projects the coarse object
meshes from the scene graph into the image, assigning object identities to patches based
on visibility. The similarity of the per-patch features, in the input image, and object
features from the scene graph determines the weight of a particle. Subsequent images are
incorporated sequentially, refining the pose estimate. By leveraging a compact scene
graph and efficient semantic matching, our method significantly reduces storage while
maintaining performance on real-world datasets. The code will be available at
https://github.com/DmblnNicole/sg2loc.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11880v1
- Authors: Nicole Damblon, Olga Vysotska, Federico Tombari, Marc Pollefeys, Daniel Barath
- Published: 2026-06-10T10:03:21Z
- Age days: 1

</details>
