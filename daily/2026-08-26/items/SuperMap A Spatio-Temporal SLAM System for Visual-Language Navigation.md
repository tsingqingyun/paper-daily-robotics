---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.22896v1"
published: "2026-08-24T07:25:14Z"
age_days: 1
score: 34
created: 2026-08-26
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation

> [!summary] 一句话结论（基于摘要）
> SuperMap produces a queryable 4D scene-graph representation that interfaces naturally with Vision-Language Models by supporting compositional queries over object semantics, relations, We demonstrate SuperMap on benchmarks and real robots, including dynamic sc…

## 关键点

- **问题**：Robotic navigation in human environments requires a spatio-temporal semantic representation that can rec- oncile open-vocabulary perception with long-term environmental changes.
- **创新点 / 方法**：We present SuperMap, a 4D spatio-temporal mapping framework for language-guided navigation that integrates high-frequency geometric SLAM with asynchronous open-vocabulary perception.
- **证据**：SuperMap produces a queryable 4D scene-graph representation that interfaces naturally with Vision-Language Models by supporting compositional queries over object semantics, relations, We demonstrate SuperMap on benchmarks and real robots, including dynamic scenes with appearance/disappearance and relocation, and provi…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/SuperMap A Spatio-Temporal SLAM System for Visual-Language Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic navigation in human environments requires a spatio-temporal semantic representation that can rec- oncile open-vocabulary perception with long-term environmental changes. While foundation models provide strong zero-shot recognition, their predictions are intermittent and view-dependent, and naively integrating them into mapping pipelines leads to identity drift and stale semantics over time. We present SuperMap, a 4D spatio-temporal mapping framework for language-guided navigation that integrates high-frequency geometric SLAM with asynchronous open-vocabulary perception. Our core contribution is a consistency-driven mapping engine that combines 3D-aware instance association/re-activation with a principled existence-and-label confidence update to maintain stable object identities and prune outdated map content under occlusions and scene changes. SuperMap produces a queryable 4D scene-graph representation that interfaces naturally with Vision-Language Models by supporting compositional queries over object semantics, relations, We demonstrate SuperMap on benchmarks and real robots, including dynamic scenes with appearance/disappearance and relocation, and provide ablations and runtime analysis. We release the full system as open-source to provide the community with a deployable baseline for open-vocabulary spatio-temporal mapping. Project website: superodometry.com/supermap.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.22896v1
- Authors: Shibo Zhao, Guofei Chen, Honghao Zhu, Zhiheng Li, Changwei Yao, Nader Zantout, Seungchan Kim, Wenshan Wang, Ji Zhang, Sebastian Scherer
- Published: 2026-08-24T07:25:14Z
- Age days: 1

</details>
