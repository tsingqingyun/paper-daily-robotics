---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19341v1"
published: "2026-07-21T17:59:02Z"
age_days: 2
score: 29
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Recent advances in multimodal generative models have enabled instruction-based image
generation to move beyond semantic manipulation to knowledge-driven visual reasoning.
However, these methods focus on explicit commonsense reasoning, shallow causal
understanding, and direct knowledge recall, failing at knowledge-intensive generation.
We develop \textbf{ExpertVerse}, a capability-centric benchmark to evaluate generative
models via knowledge-intensive lens. ExpertVerse stratifies reasoning generation across
an orthogonal taxonomy of \textit{9 cognitive capabilities} and \textit{8 expert
disciplines}, yielding \textit{58 sub-disciplines}. We curate 1,611 expert-annotated
instances covering single-image editing, multi-image composition, and text-to-image
generation. We further develop an automated workflow to produce
\textbf{ExpertVerse-100K}, a large-scale dataset with reasoning traces and knowledge-
anchored rationale annotations. Based on this, we train \textbf{KnowThinker} with RL
fine-tuning, a VLM reasoning engine with world knowledge that jointly generates thinking
processes and refined instructions. Towards the cross-modal credit misalignment and
multi-objective gradient conflicts in multi-reward optimization, we propose a tailored
Bootstrapped Pareto Policy Optimization (BPPO), which synergizes Bootstrapping Reward
Rectification (BRR) and Conflict-Aware Pareto Advantage Fusion (CPAF). Extensive results
of both open-source and proprietary models exposes critical reasoning deficits,
highlighting imperative for knowledge-intensive benchmarks towards next-generation
visual generation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19341v1
- Authors: Yuan Wang, Yongchao Du, Mengting Chen, Jinsong Lan, Xuetao Feng, Xiaoyong Zhu
- Published: 2026-07-21T17:59:02Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
