---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25044v1"
published: "2026-05-24T12:41:34Z"
age_days: 1
score: 42
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Experimental results across RoboCasa and Isaac Gym, covering different embodiments from grippers to dexterous hands, show that X-DiffVLA achieves state-of-the-art performance, with improvements of 15.3% and 12.5%, respectively.

## 关键点

- **问题**：Learning universal policies from cross-embodied data remains a fundamental challenge in robotics.
- **创新点 / 方法**：Specifically, we introduce Embodiment Forcing, a classifier-free guidance technique to implicitly steer action generation toward embodiment-specific functional components, capturing fine-grained structural nuances without explicit supervision.
- **证据**：Experimental results across RoboCasa and Isaac Gym, covering different embodiments from grippers to dexterous hands, show that X-DiffVLA achieves state-of-the-art performance, with improvements of 15.3% and 12.5%, respectively.
- **局限**：To overcome these limitations, we focus on cross-embodied settings with shared robotic bases and heterogeneous end-effectors, and propose X-DiffVLA, a diffusion-based VLA model featuring a unified cross-embodied action head.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/X-DiffVLA X-Embodied Diffusion Action Heads for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning universal policies from cross-embodied data remains a fundamental challenge in
robotics. Although Vision-Language-Action (VLA) models are pre-trained on large and
diverse datasets, they typically rely on embodiment-specific fine-tuning to achieve
strong performance in downstream tasks. This requirement severely limits their
generalization capability and restricts knowledge transfer across embodiments performing
similar tasks. To overcome these limitations, we focus on cross-embodied settings with
shared robotic bases and heterogeneous end-effectors, and propose X-DiffVLA, a
diffusion-based VLA model featuring a unified cross-embodied action head. X-DiffVLA can
leverage the generative strengths of diffusion models to capture both the diversity and
latent correlations in cross-embodied datasets. Specifically, we introduce Embodiment
Forcing, a classifier-free guidance technique to implicitly steer action generation
toward embodiment-specific functional components, capturing fine-grained structural
nuances without explicit supervision. In addition, a Morphological Tree Diffusion
approach is designed to strengthen behavioral correlations across diverse end-effectors,
maximizing the transferability of heterogeneous demonstrations. Experimental results
across RoboCasa and Isaac Gym, covering different embodiments from grippers to dexterous
hands, show that X-DiffVLA achieves state-of-the-art performance, with improvements of
15.3% and 12.5%, respectively. Real-world evaluations further validate the robustness of
the proposed framework and its effectiveness in scalable cross-embodied policy learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25044v1
- Authors: Boyu Li, Chaoyi Xu, Haoqi Yuan, Xinrun Xu, Börje F. Karlsson, Dongbin Zhao, Haoran Li, Zongqing Lu
- Published: 2026-05-24T12:41:34Z
- Age days: 1

</details>
