---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05747v1"
published: "2026-08-06T08:33:13Z"
age_days: 4
score: 25
created: 2026-08-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?

> [!summary] 一句话结论（基于摘要）
> To address this limitation, we introduce the Global-Spatial-Temporal Benchmark (GST-Bench), a VQA benchmark for global spatial intelligence in video understanding, comprising human-verified questions derived from 6,790 minutes of synthetically generated video.

## 关键点

- **问题**：We further provide GST-Train, a dataset for global spatial reasoning, as a complementary resource to facilitate future research on this challenge.
- **创新点 / 方法**：To address this limitation, we introduce the Global-Spatial-Temporal Benchmark (GST-Bench), a VQA benchmark for global spatial intelligence in video understanding, comprising human-verified questions derived from 6,790 minutes of synthetically generated video.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/GST-Bench Can VLMs Develop Global Spatial Awareness from Video.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Spatial intelligence is fundamental to embodied agents, yet existing benchmarks focus on
local spatial perception from single or few viewpoints, overlooking global spatial
awareness over continuous, long-horizon visual streams. To address this limitation, we
introduce the Global-Spatial-Temporal Benchmark (GST-Bench), a VQA benchmark for global
spatial intelligence in video understanding, comprising human-verified questions derived
from 6,790 minutes of synthetically generated video. It requires models to perform
accurate spatial inference from novel viewpoints unseen in the input video and to map
egocentric observations onto global top-down images. A comprehensive evaluation of 22
state-of-the-art VLMs exposes a striking gap between models and humans: the strongest
zero-shot model attains only 42.68, far below the human score of 79.08. To probe the
cause of this gap, we construct GST-Bench-Local and find that models, despite strong
local spatial understanding under the same task formulation, still fail to consolidate
long-horizon observations into a globally consistent scene representation. We further
provide GST-Train, a dataset for global spatial reasoning, as a complementary resource
to facilitate future research on this challenge.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05747v1
- Authors: Qifeng Zhang, Kaixiang Huang, Heng Dong, Huang Fang, Junting Chen, Junjie Zhu, Yonghang Chen, Zhiyu Zhang, Wei Li
- Published: 2026-08-06T08:33:13Z
- Age days: 4

</details>
