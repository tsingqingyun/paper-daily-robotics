---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07017v1"
published: "2026-06-05T08:00:25Z"
age_days: 2
score: 34
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "Sim2Real", "具身智能评测与基准"]
---

# The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective

> [!summary] 一句话结论（基于摘要）
> Foundation model agents are increasingly deployed for real-world decision-making, but suffer from the sim-to-real gap.

## 关键点

- **问题**：Our paper proposes formalizing the foundation model agent evaluation and training gap as a classical sim-to-real problem structured entirely around the four elements of a Markov Decision Process, including Observation, Action, Transition, and Reward.
- **创新点 / 方法**：Foundation model agents are increasingly deployed for real-world decision-making, but suffer from the sim-to-real gap.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/The Sim-to-Real Gap of Foundation Model Agents A Unified MDP Perspective.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Foundation model agents are increasingly deployed for real-world decision-making, but
suffer from the sim-to-real gap. While robotics and classical control have mature
frameworks to address this gap, the foundation model community is treating agent
robustness as an entirely novel phenomenon. Our paper proposes formalizing the
foundation model agent evaluation and training gap as a classical sim-to-real problem
structured entirely around the four elements of a Markov Decision Process, including
Observation, Action, Transition, and Reward. In this paper, we set a comprehensive
research agenda that translates classical discrepancies into the foundation model domain
and advocates for adopting established solutions like domain randomization. We provide
concrete examples, such as a multilingual tool calling to demonstrate how severe
observation space gaps lead to operationally invalid actions despite correct semantic
intent. Ultimately, this agenda aims to drive a paradigm shift, yielding a unified
vocabulary and standardized stress test benchmarks to foster a new generation of highly
trustworthy agents for reliable real-world applications.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07017v1
- Authors: Xiaoou Liu, Tiejin Chen, Weibo Li, Xiyang Hu, Hua Wei
- Published: 2026-06-05T08:00:25Z
- Age days: 2

</details>
