---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16172v1"
published: "2026-08-17T06:43:11Z"
age_days: 0
score: 32
created: 2026-08-18
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation

> [!summary] 一句话结论（基于摘要）
> On RoboCerebra, SparkVLA achieves 47.12% success rate, surpassing the official hierarchical baseline by 30.57% and the strongest reproducible method by 26.83% Real-robot experiments on multi-step tasks further validate these gains on physical hardware.

## 关键点

- **问题**：At every re-observation point in a hierarchical Vision-Language-Action (VLA) system, two interface decisions must be made: when to terminate the current subtask and how far to execute the proposed action chunk.
- **创新点 / 方法**：We present SparkVLA, a stop-aware hierarchical VLA that resolves this mutual dependency by formulating both decisions as a single ranking: Stop competes against every action-prefix length in a unified candidate set, and the system selects the highest-scoring option, eliminating threshold tuning and requiring only offl…
- **证据**：On RoboCerebra, SparkVLA achieves 47.12% success rate, surpassing the official hierarchical baseline by 30.57% and the strongest reproducible method by 26.83% Real-robot experiments on multi-step tasks further validate these gains on physical hardware.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/SparkVLA Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Hori.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

At every re-observation point in a hierarchical Vision-Language-Action (VLA) system, two interface decisions must be made: when to terminate the current subtask and how far to execute the proposed action chunk. These decisions are mutually dependent---the optimal stopping point depends on what the executor plans to do, while the optimal execution length depends on where the subtask boundary lies---yet existing architectures evaluate them in isolation, an asymmetry neither module can overcome alone. We present SparkVLA, a stop-aware hierarchical VLA that resolves this mutual dependency by formulating both decisions as a single ranking: Stop competes against every action-prefix length in a unified candidate set, and the system selects the highest-scoring option, eliminating threshold tuning and requiring only offline ordinal preferences. An Anchor-Conditioned Context Encoding module caches a history-aware subtask anchor encoding onset-state memory and goal semantics, guiding visual-token pruning toward task-relevant regions; a Stop-Aware Action-Prefix Selection head scores all candidates via full self bnattention at chunk boundaries for efficiency. On RoboCerebra, SparkVLA achieves 47.12% success rate, surpassing the official hierarchical baseline by 30.57% and the strongest reproducible method by 26.83% Real-robot experiments on multi-step tasks further validate these gains on physical hardware.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16172v1
- Authors: Xunyao Lei, Renjun Wu, Tianlin Huo, Xuesong Li
- Published: 2026-08-17T06:43:11Z
- Age days: 0

</details>
