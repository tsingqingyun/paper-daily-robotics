---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20988v1"
published: "2026-07-23T07:11:41Z"
age_days: 0
score: 32
created: 2026-07-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on NAVSIM v1 and v2 benchmarks demonstrate that HyWorldVLA significantly outperforms both pixel-based and latent-based world model baselines.

## 关键点

- **问题**：Conversely, latent-based world models alleviate this sensitivity but often incur limited interpretability and representational degradation due to absent pixel- level grounding.
- **创新点 / 方法**：To reconcile this trade-off, we propose HyWorldVLA, a hybrid world-VLA framework that unifies pixel-level supervision and latent representation learning.
- **证据**：Extensive experiments on NAVSIM v1 and v2 benchmarks demonstrate that HyWorldVLA significantly outperforms both pixel-based and latent-based world model baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-24/HyWorldVLA A Vision-Language-Action Model with Hybrid World Modeling for Autonom.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models augmented with world modeling represent a promising
paradigm for end-to-end autonomous driving. While pixel-level future prediction enables
fine-grained spatiotemporal reasoning, it compromises robustness in noisy driving
scenarios. Conversely, latent-based world models alleviate this sensitivity but often
incur limited interpretability and representational degradation due to absent pixel-
level grounding. To reconcile this trade-off, we propose HyWorldVLA, a hybrid world-VLA
framework that unifies pixel-level supervision and latent representation learning. In
the pre-training stage, HyWorldVLA predicts video latents encoded by a pre-trained video
VAE, while simultaneously reconstructing video frames to provide precise pixel-level
grounding. During the subsequent co-fine-tuning phase, the model exclusively predicts
latent features, which are fed into an action expert to generate trajectories. Extensive
experiments on NAVSIM v1 and v2 benchmarks demonstrate that HyWorldVLA significantly
outperforms both pixel-based and latent-based world model baselines. Notably, we present
the first comprehensive qualitative and quantitative analysis of world model noise
robustness in autonomous driving, establishing a new benchmark for evaluating future
architectures.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20988v1
- Authors: Quanfu Yu, Xian Wu, Hao Xu, Liulong Ma
- Published: 2026-07-23T07:11:41Z
- Age days: 0

</details>
