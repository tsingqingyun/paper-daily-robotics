---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13621v1"
published: "2026-07-15T09:09:25Z"
age_days: 1
score: 34
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# UESF-Bench: Benchmarking and Probing for Unified Embodied Seeking and Following

> [!summary] 一句话结论（基于摘要）
> Experimental results show that SeekFollow-VLA achieves clear improvements over both single-head and dual-head baselines across single-person and multi-person environments, establishing a baseline for unified embodied seek-and-follow.

## 关键点

- **问题**：This setting simplifies the problem and overlooks a more realistic requirement: an agent often needs to first find a language-described target and then persistently follow that target in a dynamic environment.
- **创新点 / 方法**：To address these limitations, we introduce the Unified Embodied Seeking and Following Benchmark (UESF-Bench), a large-scale and diverse benchmark for embodied human seeking and following.
- **证据**：Experimental results show that SeekFollow-VLA achieves clear improvements over both single-head and dual-head baselines across single-person and multi-person environments, establishing a baseline for unified embodied seek-and-follow.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Language-guided human following is an important capability for embodied agents, but
existing benchmarks typically assume that the target person is visible at the start of
an episode. This setting simplifies the problem and overlooks a more realistic
requirement: an agent often needs to first find a language-described target and then
persistently follow that target in a dynamic environment. While recent work has started
to study human search, existing settings are typically evaluated in task-specific
scenarios and often rely on stronger prior knowledge of the environment. Moreover, they
usually treat searching and following as separate tasks and still lack a unified
benchmark for systematic evaluation. To address these limitations, we introduce the
Unified Embodied Seeking and Following Benchmark (UESF-Bench), a large-scale and diverse
benchmark for embodied human seeking and following. The benchmark requires agents to
handle semantic-guided exploration, reliable behavior switching and recovery, and
delayed identity grounding. To this end, we propose SeekFollow-VLA, a vision-language-
action framework with a task-driven routing mechanism for latent phase inference and
transition modeling between seeking and following. Experimental results show that
SeekFollow-VLA achieves clear improvements over both single-head and dual-head baselines
across single-person and multi-person environments, establishing a baseline for unified
embodied seek-and-follow.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13621v1
- Authors: Kun Yu, Jianhua Yang, Yixiang Chen, Changwei Wang, Hongyuan Yu, Yan Huang, Fushuo Huo, Ya Jing, Zhumin Chen, Keji He
- Published: 2026-07-15T09:09:25Z
- Age days: 1

</details>
