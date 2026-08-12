---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13679v2"
published: "2026-06-11T17:59:50Z"
age_days: 3
score: 33
created: 2026-06-15
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# InterleaveThinker: Reinforcing Agentic Interleaved Generation

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Recent image generators have demonstrated impressive photorealism and instruction-
following capabilities in single-image generation and editing. However, constrained by
their architectures, they cannot achieve interleaved generation (text-image sequence),
which has crucial applications in visual narratives, guidance, and embodied
manipulation. Even the latest open-source Unified Multimodal Models (UMMs) exhibit
limited performance in this regard. In this paper, we introduce InterleaveThinker, the
first multi-agent pipeline designed to endow any existing image generator with
interleaved generation capabilities. Specifically, we employ a planner agent to organize
the image-text input sequence, instructing the image generator on the required execution
at each step. Subsequently, we introduce a critic agent to evaluate the generator's
outputs, identify samples that deviate from the planned instructions, and refine the
instructions for regeneration. To implement this pipeline, we construct the Interleave-
Planner-SFT-80k and Interleave-Critic-SFT-112k to perform a format cold-start. Then we
develop Interleave-Critic-RL-13k to reinforce the step-wise instruction correction
capability within a generation trajectory using GRPO. Since a single interleaved
generation trajectory may involve over 25 generator calls, optimizing the entire
trajectory is computationally impractical. Therefore, we propose accuracy reward and
step-wise reward, allowing single-step RL to effectively guide the entire generation
trajectory. The results show that InterleaveThinker improves performance across various
image generators. On interleaved generation benchmarks, it achieves performance
comparable to Nano Banana and GPT-5. Surprisingly, it also significantly enhances the
base model on reasoning-based benchmarks; for example, on 4-step FLUX.2-klein, we
observe substantial gains on WISE and RISE.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13679v2
- Authors: Dian Zheng, Harry Lee, Manyuan Zhang, Kaituo Feng, Zoey Guo, Ray Zhang, Hongsheng Li
- Published: 2026-06-11T17:59:50Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
