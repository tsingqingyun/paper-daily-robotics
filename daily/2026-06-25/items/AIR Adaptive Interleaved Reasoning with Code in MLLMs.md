---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23678v1"
published: "2026-06-22T17:58:54Z"
age_days: 2
score: 30
created: 2026-06-25
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# AIR: Adaptive Interleaved Reasoning with Code in MLLMs

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that after Reinforcement Learning training with the group-constrained reward function, performance improves by an average of 6.1 percentage points (pp) on evaluation benchmarks.

## 关键点

- **问题**：However, such approaches typically rely on predefined heuristics for visual manipulation and are inherently incapable of addressing numerical computation problems due to their exclusive focus on visual operations.
- **创新点 / 方法**：To this end, we propose a comprehensive three-component solution consisting of: a two-stage cold-start data construction pipeline, data filtering strategies for RL dataset curation, and an adaptive tool-invocation strategy leveraging a group-constrained reward function for interleaved reasoning trajectories.
- **证据**：Extensive experiments demonstrate that after Reinforcement Learning training with the group-constrained reward function, performance improves by an average of 6.1 percentage points (pp) on evaluation benchmarks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Following the paradigm shift initiated by OpenAI o3, interleaved reasoning with code to
enhance multimodal large language models (MLLMs) has become a pivotal research frontier.
The existing literature focuses primarily on tool-use within vision-perception tasks.
However, such approaches typically rely on predefined heuristics for visual manipulation
and are inherently incapable of addressing numerical computation problems due to their
exclusive focus on visual operations. This paper empowers MLLMs with adaptive
interleaved reasoning capabilities through extended reinforcement learning training on
code-augmented complex numerical computation tasks. To this end, we propose a
comprehensive three-component solution consisting of: a two-stage cold-start data
construction pipeline, data filtering strategies for RL dataset curation, and an
adaptive tool-invocation strategy leveraging a group-constrained reward function for
interleaved reasoning trajectories. Extensive experiments demonstrate that after
Reinforcement Learning training with the group-constrained reward function, performance
improves by an average of 6.1 percentage points (pp) on evaluation benchmarks.
Specifically, the accuracy for interleaved reasoning samples increases by 9.9 pp, and
the overall success rate of tool-use exceeds 95%. Our data and code are available at:
https://github.com/CongHan0808/AIR.git.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23678v1
- Authors: Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong
- Published: 2026-06-22T17:58:54Z
- Age days: 2

</details>
