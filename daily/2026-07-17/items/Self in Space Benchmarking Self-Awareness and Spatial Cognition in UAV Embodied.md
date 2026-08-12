---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.12477v2"
published: "2026-07-14T08:04:31Z"
age_days: 2
score: 30
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence

> [!summary] 一句话结论（基于摘要）
> Experimental results show that modeling agent motion consistently improves perception and memory performance, not only in spatial cognition but also in self-awareness, and generalizes to downstream UAV decision-making tasks.

## 关键点

- **问题**：However, existing UAV-oriented approaches and benchmarks remain largely environment-centric, primarily focusing on spatial understanding tasks, with the agent's self-awareness remaining implicit.
- **创新点 / 方法**：To address this gap, we introduce SIS-Bench, a benchmark for evaluating embodied spatial intelligence in UAV scenarios under a unified self-in-space formulation.
- **证据**：Experimental results show that modeling agent motion consistently improves perception and memory performance, not only in spatial cognition but also in self-awareness, and generalizes to downstream UAV decision-making tasks.
- **局限**：Extensive evaluations reveal that current MLLMs exhibit fundamental limitations in modeling dynamic and agent-centered processes.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/Self in Space Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous UAV systems increasingly rely on multimodal large language models (MLLMs) to
operate in complex real-world environments. Such embodied scenarios require not only
understanding the surrounding space but also maintaining a coherent representation of
the agent itself. However, existing UAV-oriented approaches and benchmarks remain
largely environment-centric, primarily focusing on spatial understanding tasks, with the
agent's self-awareness remaining implicit. To address this gap, we introduce SIS-Bench,
a benchmark for evaluating embodied spatial intelligence in UAV scenarios under a
unified self-in-space formulation. SIS-Bench organizes evaluation along two
complementary dimensions, space and self, and a three-level hierarchy of perception,
memory, and reasoning. It contains 4,856 question--answer pairs across 13 tasks derived
from 1,646 real-world UAV videos through a task-conditioned construction pipeline with
expert verification. Extensive evaluations reveal that current MLLMs exhibit fundamental
limitations in modeling dynamic and agent-centered processes. In particular, we observe
a clear imbalance between spatial cognition and self-awareness, as well as a progressive
performance degradation across cognitive levels. Motivated by these findings, we further
explore a motion-aware representation that incorporates self-related dynamics through
optical flow and visual feature fusion. Experimental results show that modeling agent
motion consistently improves perception and memory performance, not only in spatial
cognition but also in self-awareness, and generalizes to downstream UAV decision-making
tasks. Our results highlight the importance of self-awareness for advancing embodied
spatial intelligence, and provide both a new benchmark and empirical evidence for
motion-aware self-in-space modeling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.12477v2
- Authors: Zhishan Zou, Guoyan Sun, Zhiwei Wei, Jiancheng Pan, Yujie Li, Mugen Peng, Wenjia Xu
- Published: 2026-07-14T08:04:31Z
- Age days: 2

</details>
