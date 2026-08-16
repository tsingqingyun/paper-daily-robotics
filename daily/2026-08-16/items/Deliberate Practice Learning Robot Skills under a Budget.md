---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13415v1"
published: "2026-08-13T16:09:25Z"
age_days: 2
score: 25
created: 2026-08-16
concepts: ["智能体 Agent"]
---

# Deliberate Practice: Learning Robot Skills under a Budget

> [!summary] 一句话结论（基于摘要）
> Through simulated and real-world experiments on long-horizon manipulation tasks, we show that our approach allows robots to optimally use limited practice time to acquire useful policies and improve long-horizon planning.

## 关键点

- **问题**：We consider the problem of autonomously learning robot skills under a limited practice budget for sequential tasks.
- **创新点 / 方法**：We propose an active skill learning algorithm, \emph{Deliberate Practice (DP)}, that computes a provably \emph{budget-optimal} allocation---practicing skills that maximize expected cumulative reward while being learnable within the budget.
- **证据**：Through simulated and real-world experiments on long-horizon manipulation tasks, we show that our approach allows robots to optimally use limited practice time to acquire useful policies and improve long-horizon planning.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Deliberate Practice Learning Robot Skills under a Budget.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We consider the problem of autonomously learning robot skills under a limited practice budget for sequential tasks. We propose an active skill learning algorithm, \emph{Deliberate Practice (DP)}, that computes a provably \emph{budget-optimal} allocation---practicing skills that maximize expected cumulative reward while being learnable within the budget. DP estimates both the time needed to master skills and the cumulative reward of the task plans that the skills unlock. Computing a budget-optimal allocation is challenging as it requires reasoning about combinatorially many skill plans over a large practice budget. Our key contribution is a bilinear program that can compute this exactly using off-the-shelf solvers. Through simulated and real-world experiments on long-horizon manipulation tasks, we show that our approach allows robots to optimally use limited practice time to acquire useful policies and improve long-horizon planning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13415v1
- Authors: Shivam Vats, Sudarshan Harithas, Mete Tuluhan Akbulut, Arvind Raghunathan, George Konidaris
- Published: 2026-08-13T16:09:25Z
- Age days: 2

</details>
