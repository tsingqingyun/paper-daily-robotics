---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12122v1"
published: "2026-08-12T14:41:53Z"
age_days: 2
score: 36
created: 2026-08-15
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# HandEdit: A Unified Benchmark for Egocentric Human-to-Robot Dexterous Hand Image Editing

> [!summary] 一句话结论（基于摘要）
> In this work, we present HandEdit, a unified large-scale embodiment-aware image-editing dataset and benchmark specifically designed to transform human hands and arms into various dexterous robotic embodiments within egocentric frames.

## 关键点

- **问题**：While abundant egocentric videos of human hands offer a scalable alternative, the profound discrepancies in appearance, articulation, and camera viewpoints between human and robotic data raise significant challenges for co-training.
- **创新点 / 方法**：In this work, we present HandEdit, a unified large-scale embodiment-aware image-editing dataset and benchmark specifically designed to transform human hands and arms into various dexterous robotic embodiments within egocentric frames.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/HandEdit A Unified Benchmark for Egocentric Human-to-Robot Dexterous Hand Image.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation with dexterous hands is a cornerstone of Embodied AI, yet its progress is stifled by the high cost of collecting embodiment-aware teleoperation data. While abundant egocentric videos of human hands offer a scalable alternative, the profound discrepancies in appearance, articulation, and camera viewpoints between human and robotic data raise significant challenges for co-training. Though existing general image-editing models demonstrate strong capabilities, they lack necessary embodiment-specific priors to fully bridge this gap. In this work, we present HandEdit, a unified large-scale embodiment-aware image-editing dataset and benchmark specifically designed to transform human hands and arms into various dexterous robotic embodiments within egocentric frames. HandEdit comprises over 200M editing instances derived from five diverse source datasets, covering 26 distinct URDFs, including 13 hand-only and 13 hand-arm configurations. Alongside the dataset, we establish a unified benchmark protocol with two tracks: Hand-only and Hand-Arm, supporting URDF-conditioned evaluation. We conduct extensive evaluations of 11 representative image-editing baselines using a multi-dimensional metric suite, including generic similarity metrics, VLM-based judgment, and embodiment-aware metrics. HandEdit serves as a critical resource at the intersection of image editing and robotics: it advances embodiment-aware editing models while enabling scalable dexterous robotic learning from abundant human video data, paving the way for more generalizable Embodied AI.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12122v1
- Authors: Zhenjie Yang, Xingyu Jiao, Guopeng Zhong, Shuzhe Yang, Shi Che, Chao Wu, Chenyu Jiang, Dongjie Zhang, Yideng Zhang, Zheng Zhang, Muyun Jiang, Haisheng Su, Shuang Jin, Donghang Zhang, Chao Yang, Li Chen, Hongyang Li, Zuxuan Wu, Yu-Gang Jiang, Xiaosong Jia, Junchi Yan
- Published: 2026-08-12T14:41:53Z
- Age days: 2

</details>
