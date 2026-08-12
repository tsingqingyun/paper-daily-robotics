---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15641v1"
published: "2026-07-17T05:34:29Z"
age_days: 3
score: 38
created: 2026-07-20
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# IMBench: A Benchmark for Intuitive Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> We introduce IMBENCH, a benchmark designed to evaluate intuitive manipulation as an integrated capability spanning perception, physical reasoning, action generation, and iterative execution.

## 关键点

- **问题**：Experiments reveal a consistent gap: vision language models show partial physical reasoning ability but fail to produce executable plans, while state-of-the-art vision-language-action models struggle to satisfy task constraints and generalize across scenarios.
- **创新点 / 方法**：We introduce IMBENCH, a benchmark designed to evaluate intuitive manipulation as an integrated capability spanning perception, physical reasoning, action generation, and iterative execution.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/IMBench A Benchmark for Intuitive Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humans combine reasoning and motor control to solve complex manipulation tasks under
diverse constraints. They build an understanding of the physical world that helps them
convert reasoning into actions and quickly adapt to new scenes, tasks, and rules. We
refer to this capability as intuitive manipulation. Existing benchmarks fail to capture
this integration: they evaluate physical reasoning in isolation from execution, or
measure policy performance without requiring explicit reasoning. We introduce IMBENCH, a
benchmark designed to evaluate intuitive manipulation as an integrated capability
spanning perception, physical reasoning, action generation, and iterative execution. Our
tasks require models to infer task-relevant physical structure and generate feasible
action sequences under explicit constraints, including contact-rich manipulation, tool
use, and multi-stage dependencies. We introduce a benchmark of 35 tasks, 14K filtered
trajectories, and scalable tools for generating diverse scenarios. Experiments reveal a
consistent gap: vision language models show partial physical reasoning ability but fail
to produce executable plans, while state-of-the-art vision-language-action models
struggle to satisfy task constraints and generalize across scenarios. These results
identify intuitive manipulation as a missing axis in current foundation models and
generalist robot policies, and position IMBENCH as a step toward evaluating and enabling
more integrated, adaptive physical intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15641v1
- Authors: Anurag Maurya, Sukhvansh Jain, Prajwal Avhad, Gautham Balachandran, Ziyi Zhou, Atharva Kshirsagar, Satyam Singh, Bowen Li. Rishabh Mukund, Ritul Singh, Jatin Vira, Suvonil Chatterjee, Devesh K. Jha
- Published: 2026-07-17T05:34:29Z
- Age days: 3

</details>
