---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09827v1"
published: "2026-06-08T17:59:53Z"
age_days: 1
score: 45
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> For example, on real robots, it achieves +9%, +26%, +28% gains on general, memory-dependent, and imagination-dependent tasks.

## 关键点

- **问题**：However, most VLA models rely primarily on the current observation and therefore struggle with long- horizon, temporally dependent tasks.
- **创新点 / 方法**：Inspired by these mechanisms, we propose MemoryVLA++, a full temporal modeling framework that equips VLA models with memory and imagination for robotic manipulation.
- **证据**：For example, on real robots, it achieves +9%, +26%, +28% gains on general, memory-dependent, and imagination-dependent tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：45
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/MemoryVLA++ Temporal Modeling via Memory and Imagination in Vision-Language-Acti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Temporal modeling is essential for robotic manipulation, as effective control requires
both memory of past interactions and imagination of future states. However, most VLA
models rely primarily on the current observation and therefore struggle with long-
horizon, temporally dependent tasks. Cognitive science suggests that humans rely on
working memory to buffer short-lived context, the hippocampal system to preserve
episodic memory of past experience, and internal models to imagine possible future state
evolution. Inspired by these mechanisms, we propose MemoryVLA++, a full temporal
modeling framework that equips VLA models with memory and imagination for robotic
manipulation. A pretrained VLM encodes the current observation into perceptual and
cognitive tokens, forming working memory. These tokens query a Perceptual-Cognitive
Memory Bank to retrieve relevant historical context. This bank stores low-level details
and high-level semantics from past interactions, and is updated through redundancy-aware
consolidation. A world model imagines future states in a denoising latent space, and the
imagined latents are integrated under memory guidance to form full temporal-aware
tokens. The resulting tokens condition a diffusion action expert to predict temporally
consistent action sequences. We conduct extensive experiments on 5 simulation benchmarks
and 3 categories of real-robot tasks across 3 robots, covering general manipulation,
long-horizon temporal tasks, robustness, and generalization. Our method achieves strong
performance across Libero, SimplerEnv, Mikasa-Robo, Calvin, Libero-Plus, and diverse
real-robot tasks, validating the effectiveness of full temporal modeling with memory and
imagination. For example, on real robots, it achieves +9%, +26%, +28% gains on general,
memory-dependent, and imagination-dependent tasks. Project Page:
https://shihao1895.github.io/MemoryVLA-PP-Web

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09827v1
- Authors: Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou, Tiancai Wang, Xiangyu Zhang, Ping Luo, Gao Huang
- Published: 2026-06-08T17:59:53Z
- Age days: 1

</details>
