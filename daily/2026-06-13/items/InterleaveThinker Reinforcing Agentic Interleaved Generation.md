---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13679v1"
published: "2026-06-11T17:59:50Z"
age_days: 1
score: 33
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# InterleaveThinker: Reinforcing Agentic Interleaved Generation

> [!summary] 一句话结论（基于摘要）
> On interleaved generation benchmarks, it achieves performance comparable to Nano Banana and GPT-5.

## 关键点

- **问题**：However, constrained by their architectures, they cannot achieve interleaved generation (text-image sequence), which has crucial applications in visual narratives, guidance, and embodied manipulation.
- **创新点 / 方法**：In this paper, we introduce InterleaveThinker, the first multi-agent pipeline designed to endow any existing image generator with interleaved generation capabilities.
- **证据**：On interleaved generation benchmarks, it achieves performance comparable to Nano Banana and GPT-5.
- **局限**：However, constrained by their architectures, they cannot achieve interleaved generation (text-image sequence), which has crucial applications in visual narratives, guidance, and embodied manipulation.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

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

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13679v1
- Authors: Dian Zheng, Harry Lee, Manyuan Zhang, Kaituo Feng, Zoey Guo, Ray Zhang, Hongsheng Li
- Published: 2026-06-11T17:59:50Z
- Age days: 1

</details>
