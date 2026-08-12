---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09827v1"
published: "2026-06-08T17:59:53Z"
age_days: 1
score: 45
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models

## 为什么重要

自动筛选分数：45

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09827v1
- Authors: Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou, Tiancai Wang, Xiangyu Zhang, Ping Luo, Gao Huang
- Published: 2026-06-08T17:59:53Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
