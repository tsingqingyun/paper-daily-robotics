---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17520v1"
published: "2026-06-16T05:00:42Z"
age_days: 1
score: 33
created: 2026-06-18
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real"]
---

# GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation accuracy by over 10\% while achieving state-of-the-art inpainting quality.

## 关键点

- **问题**：Training embodied agents in the real world requires skilled operators and expensive hardware.
- **创新点 / 方法**：Simulation environments offer a compelling alternative by enabling large- scale, cost-effective data augmentation.
- **证据**：Extensive experiments demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation accuracy by over 10\% while achieving state-of-the-art inpainting quality.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-18/GASE Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simul.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Training embodied agents in the real world requires skilled operators and expensive
hardware. Simulation environments offer a compelling alternative by enabling large-
scale, cost-effective data augmentation. Consequently, rapidly constructing high-
fidelity simulation scenes with a minimal sim-to-real gap has become a critical
objective in robot learning. While reconstruction-based methods provide superior visual
quality, current workflows are hindered by inefficient data acquisition and subpar
foreground object extraction. We thus propose GASE, a highly automated system for
simulation scene construction. GASE leverages multi-view video streams from panoramic
camera arrays to enable rapid environment scanning. To ensure high-quality asset
generation, our pipeline introduces a camera-pose-based strategy that robustly extracts
objects across frames in the 2D domain, followed by high-fidelity scene inpainting.
Foreground objects and the static background are then reconstructed independently and
seamlessly imported into physics simulators for policy training. Extensive experiments
demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation
accuracy by over 10\% while achieving state-of-the-art inpainting quality. Furthermore,
real-robot deployments across manipulation and navigation tasks maintains a performance
gap of less than 10\% compared to policies trained purely on real-world data. These
results confirm that GASE provides an efficient and highly effective solution for
bridging the sim-to-real gap. Code will be released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17520v1
- Authors: Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang
- Published: 2026-06-16T05:00:42Z
- Age days: 1

</details>
