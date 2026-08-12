---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02497v1"
published: "2026-07-02T17:56:49Z"
age_days: 3
score: 29
created: 2026-07-06
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Seek to Segment: Active Perception for Panoramic Referring Segmentation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.

## 关键点

- **问题**：Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments.
- **创新点 / 方法**：To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS).
- **证据**：Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-06/Seek to Segment Active Perception for Panoramic Referring Segmentation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Existing referring segmentation models passively process static images captured from
fixed perspectives, limiting their applicability in Embodied AI, where agents must
perform active perception in the continuous 360$^\circ$ environments. To bridge this
gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this
setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the
360$^\circ$ environment, seeking the object specified by a user instruction for
segmentation. To tackle this challenging task, we propose PanoSeeker, a memory-augmented
agent for efficient APRS. Rather than relying on heuristic scanning, PanoSeeker
integrates a Vision-Language Model (VLM) with EgoSphere, an explicit spatial visual
memory. By progressively integrating sequential local observations into a unified
360$^\circ$ representation, EgoSphere enables the agent to plan efficient and non-
redundant search trajectories. Once the target is found, the agent performs active
viewpoint alignment and outputs the segmentation mask. Furthermore, we curate an expert-
annotated search trajectory dataset with memory timelines for Supervised Fine-Tuning,
followed by Reinforcement Learning post-training to explicitly optimize PanoSeeker's
exploration efficiency. Extensive experiments on our newly established APRS benchmark
demonstrate that PanoSeeker achieves superior search efficiency and segmentation
accuracy, significantly outperforming adapted state-of-the-art baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02497v1
- Authors: Song Tang, Shuming Hu, Xincheng Shuai, Henghui Ding, Yu-Gang Jiang
- Published: 2026-07-02T17:56:49Z
- Age days: 3

</details>
