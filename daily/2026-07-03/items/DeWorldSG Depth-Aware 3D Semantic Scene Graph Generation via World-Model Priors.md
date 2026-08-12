---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00889v1"
published: "2026-07-01T12:55:09Z"
age_days: 1
score: 33
created: 2026-07-03
concepts: ["世界模型"]
---

# DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors

> [!summary] 一句话结论（基于摘要）
> In particular, our method improves triplet recall by 77.4% and predicate recall by 23.2% over prior SoTA approaches, making it suitable for robotic manipulation and AR applications.

## 关键点

- **问题**：Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference.
- **创新点 / 方法**：We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences.
- **证据**：In particular, our method improves triplet recall by 77.4% and predicate recall by 23.2% over prior SoTA approaches, making it suitable for robotic manipulation and AR applications.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/DeWorldSG Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D
Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct
reliable 3D scene graphs due to unstable 3D object representations and missing relations
caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-
level geometric 3D Gaussian distributions through depth-guided filtering and
representing each object as a probabilistic 3D node rather than a single projected
point. To mitigate relational sparsity from frame-wise inference, our framework further
aggregates spatiotemporal evidence across object pairs and refines relations using
contextual priors derived from a world model (V-JEPA 2). Experiments on the 3DSSG and
ReplicaSSG datasets demonstrate state-of-the-art (SoTA) performance in both object and
predicate prediction, while producing temporally consistent scene structures. In
particular, our method improves triplet recall by 77.4% and predicate recall by 23.2%
over prior SoTA approaches, making it suitable for robotic manipulation and AR
applications. Our code and models are open-sourced.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00889v1
- Authors: Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo
- Published: 2026-07-01T12:55:09Z
- Age days: 1

</details>
