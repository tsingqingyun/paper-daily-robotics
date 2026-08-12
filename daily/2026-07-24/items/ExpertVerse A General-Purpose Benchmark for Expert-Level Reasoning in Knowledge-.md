---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19341v1"
published: "2026-07-21T17:59:02Z"
age_days: 2
score: 29
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis

> [!summary] 一句话结论（基于摘要）
> We develop \textbf{ExpertVerse}, a capability-centric benchmark to evaluate generative models via knowledge-intensive lens.

## 关键点

- **问题**：However, these methods focus on explicit commonsense reasoning, shallow causal understanding, and direct knowledge recall, failing at knowledge-intensive generation.
- **创新点 / 方法**：We develop \textbf{ExpertVerse}, a capability-centric benchmark to evaluate generative models via knowledge-intensive lens.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-24/ExpertVerse A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

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

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19341v1
- Authors: Yuan Wang, Yongchao Du, Mengting Chen, Jinsong Lan, Xuetao Feng, Xiaoyong Zhu
- Published: 2026-07-21T17:59:02Z
- Age days: 2

</details>
