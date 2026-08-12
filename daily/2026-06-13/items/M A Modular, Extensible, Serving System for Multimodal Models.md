---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12688v1"
published: "2026-06-10T21:22:22Z"
age_days: 2
score: 31
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# M*: A Modular, Extensible, Serving System for Multimodal Models

> [!summary] 一句话结论（基于摘要）
> We instantiate M* on representative models and find that it achieves, on average, 20% lower end-to-end latency than vLLM-Omni for text-to-image workloads on BAGEL, while delivering up to 2.9x lower real-time factor and 2.7x higher throughput for text-to-speec…

## 关键点

- **问题**：However, existing model serving frameworks were built on narrow assumptions about model structure, making them ill-suited to accommodate this new architectural diversity.
- **创新点 / 方法**：Here we present M*, a universal serving system for efficient serving of composite AI models.
- **证据**：We instantiate M* on representative models and find that it achieves, on average, 20% lower end-to-end latency than vLLM-Omni for text-to-image workloads on BAGEL, while delivering up to 2.9x lower real-time factor and 2.7x higher throughput for text-to-speech workloads on Qwen3-Omni.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/M A Modular, Extensible, Serving System for Multimodal Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We are entering a new era of composite model architectures that integrate diverse
components such as vision encoders, language backbones, diffusion and flow heads, audio
codecs, action generators, and world-model predictors. Such architectures underpin a
broad class of multimodal models, including unified multimodal models, omni models,
speech-language models, vision-language-action policies, and world models. However,
existing model serving frameworks were built on narrow assumptions about model
structure, making them ill-suited to accommodate this new architectural diversity. Here
we present M*, a universal serving system for efficient serving of composite AI models.
M* represents models as dataflow graphs, processing requests spanning diverse modalities
and tasks as traversals over these graphs. The core insight is a modular abstraction
that supports arbitrary composition of model components, flexible placement onto a
physical cluster, and model-agnostic optimizations within a distributed runtime. We call
this abstraction the Walk Graph and show how it can concisely capture composite models
from a broad range of families. We instantiate M* on representative models and find that
it achieves, on average, 20% lower end-to-end latency than vLLM-Omni for text-to-image
workloads on BAGEL, while delivering up to 2.9x lower real-time factor and 2.7x higher
throughput for text-to-speech workloads on Qwen3-Omni. M* also outperforms the V-JEPA
2-AC rollout baseline for robotic planning by up to 12.5x. Thus, our work paves the road
towards more efficient serving of complex models with minimal developer effort.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12688v1
- Authors: Atindra Jha, Naomi Sagan, Keisuke Kamahori, Irmak Sivgin, Rohan Sanda, Steven Gao, Mark Horowitz, Luke Zettlemoyer, Olivia Hsu, Jure Leskovec, Baris Kasikci, Stephanie Wang
- Published: 2026-06-10T21:22:22Z
- Age days: 2

</details>
