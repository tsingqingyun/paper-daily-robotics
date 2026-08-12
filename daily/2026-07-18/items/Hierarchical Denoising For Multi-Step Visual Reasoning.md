---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15278v1"
published: "2026-07-16T17:59:57Z"
age_days: 1
score: 31
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Hierarchical Denoising For Multi-Step Visual Reasoning

> [!summary] 一句话结论（基于摘要）
> Compared with streaming autoregressive diffusion baselines, HDR improves success from 34.22 to 60.29 (76.2% relative gain) and increases average progress from 76.00 to 89.56, demonstrating more consistent reasoning trajectories.

## 关键点

- **问题**：Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning.
- **创新点 / 方法**：We propose HDR (Hierarchical Denoising for Visual Reasoning), a unified framework that integrates hierarchical latents into causal video generation for multi-step reasoning.
- **证据**：Compared with streaming autoregressive diffusion baselines, HDR improves success from 34.22 to 60.29 (76.2% relative gain) and increases average progress from 76.00 to 89.56, demonstrating more consistent reasoning trajectories.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/Hierarchical Denoising For Multi-Step Visual Reasoning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video models are evolving into vision foundation models, yet they still lack human-like
multi-step reasoning. Streaming autoregressive diffusion models are efficient but
limited in reasoning, while bidirectional diffusion enables global revision with high
inference costs due to dense frame-level denoising. Both paradigms struggle to achieve
logical consistency and low-latency streaming for complex reasoning tasks. We propose
HDR (Hierarchical Denoising for Visual Reasoning), a unified framework that integrates
hierarchical latents into causal video generation for multi-step reasoning. HDR
organizes video latents into a tree-structured hierarchy, enabling coarse-to-fine
reasoning before streaming output. Coarse denoising layers preserve uncertain hypotheses
for global planning, while finer layers progressively refine them into concrete visual
states. A sparse hierarchical attention pattern (SHAP) further reduces temporal
attention costs. We introduce a level-stratified multi-step video reasoning benchmark
with out-of-distribution cases, covering six tasks: maze navigation, Tower of Hanoi,
one-line drawing, sliding puzzle, Sokoban, and water pouring. Compared with streaming
autoregressive diffusion baselines, HDR improves success from 34.22 to 60.29 (76.2%
relative gain) and increases average progress from 76.00 to 89.56, demonstrating more
consistent reasoning trajectories. HDR maintains low-latency streaming at 0.70 seconds
per latent, achieving 54.2 times faster inference than bidirectional diffusion. It also
retains 82.9% of full-data performance with only 2% training data, compared with 52.0%
for bidirectional diffusion. Real-world robot experiments further demonstrate HDR's
potential for physical interaction and world modeling. Project demo:
https://hierarchical-diffusion-reasoning.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15278v1
- Authors: Zezhong Qian, Xiaowei Chi, Chak-Wing Mak, Tianze Zhou, Ruibin Yuan, Yuhan Rui, Hengzhe Sun, Zhuoqun Wu, Yuming Li, Siyuan Qian, Sirui Han, Shanghang Zhang
- Published: 2026-07-16T17:59:57Z
- Age days: 1

</details>
