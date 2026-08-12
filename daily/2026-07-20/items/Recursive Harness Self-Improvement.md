---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15524v1"
published: "2026-07-17T00:21:19Z"
age_days: 3
score: 28
created: 2026-07-20
concepts: ["多模态基础模型", "智能体 Agent"]
---

# Recursive Harness Self-Improvement

> [!summary] 一句话结论（基于摘要）
> We show that these gains arise primarily from improved task-specific context management through more effective inter-agent information flow rather than longer reasoning traces.

## 关键点

- **问题**：However, continually updating provider-built scaffolds is costly and labor-intensive.
- **创新点 / 方法**：To this end, we introduce Recursive Harness Self-Improvement (RHI), which represents the harness as a prompt-level specification of the agent loop and iteratively refines it using pairwise feedback over its own revision history.
- **证据**：We show that these gains arise primarily from improved task-specific context management through more effective inter-agent information flow rather than longer reasoning traces.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/Recursive Harness Self-Improvement.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Under model--harness co-evolution, harnesses are not merely inference-time scaffolds but
data-generating components whose execution traces can shape future foundation models.
This motivates harness-in-the-loop learning: optimizing harnesses for both immediate
agent performance and the quality of traces used for future model training. However,
continually updating provider-built scaffolds is costly and labor-intensive. We
therefore investigate whether optimizing user-constructed harnesses in a task-specific
manner can improve execution-trace quality while remaining computationally lightweight
and requiring only a few update iterations. To this end, we introduce Recursive Harness
Self-Improvement (RHI), which represents the harness as a prompt-level specification of
the agent loop and iteratively refines it using pairwise feedback over its own revision
history. Across 30 synthetic machine-learning research tasks spanning quantitative
finance, robotics, and pharmacy, a few RHI iterations suffice to substantially raise the
performance ceiling of low-reasoning-effort agents, exceeding the corresponding maximum-
reasoning-effort setting while reducing inference cost by up to 60%. We show that these
gains arise primarily from improved task-specific context management through more
effective inter-agent information flow rather than longer reasoning traces. Finally, we
formalize this behavior as an information-theoretic hypothesis for RHI's implicit
optimization objective, suggesting RHI as a practical algorithm for continual learning
within the paradigm of model--harness co-evolution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15524v1
- Authors: Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Matei Zaharia, Yujin Tang
- Published: 2026-07-17T00:21:19Z
- Age days: 3

</details>
