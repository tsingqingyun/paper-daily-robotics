---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13731v1"
published: "2026-06-11T11:49:31Z"
age_days: 3
score: 28
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# TwinBI: An Agentic Digital Twin for Efficient Augmented Interactions with Business Intelligence Dashboards

> [!summary] 一句话结论（基于摘要）
> In a controlled A/B benchmark with the same backbone agent, TwinBI improves exact-match accuracy from 43.3% to 63.3%, partial-credit accuracy from 48.3% to 70.8%, and substantially reduces timeout rate from 40.0% to 10.0% relative to Dashboard alone.

## 关键点

- **问题**：As users switch between direct dashboard manipulation and natural-language queries, it becomes difficult to preserve a consistent analytical state across filters, hierarchies, metrics, and chart context.
- **创新点 / 方法**：We present TwinBI, an agentic digital-twin framework that couples an LLM-based agent system with an executable BI dashboard state.
- **证据**：In a controlled A/B benchmark with the same backbone agent, TwinBI improves exact-match accuracy from 43.3% to 63.3%, partial-credit accuracy from 48.3% to 70.8%, and substantially reduces timeout rate from 40.0% to 10.0% relative to Dashboard alone.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/TwinBI An Agentic Digital Twin for Efficient Augmented Interactions with Busines.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Business intelligence (BI) increasingly combines dashboard interaction with LLM-based
assistance, but these two modes often fall out of sync during multi-step analysis. As
users switch between direct dashboard manipulation and natural-language queries, it
becomes difficult to preserve a consistent analytical state across filters, hierarchies,
metrics, and chart context. We present TwinBI, an agentic digital-twin framework that
couples an LLM-based agent system with an executable BI dashboard state. TwinBI unifies
conversational interaction, dashboard manipulation, semantic grounding, and provenance
tracking through a shared analytical state reconstructed from a unified interaction log.
It also exposes artifacts such as schema views, SQL, logs, and an /insights command for
state-grounded analytical summaries. We evaluate TwinBI in two complementary ways. In a
controlled A/B benchmark with the same backbone agent, TwinBI improves exact-match
accuracy from 43.3% to 63.3%, partial-credit accuracy from 48.3% to 70.8%, and
substantially reduces timeout rate from 40.0% to 10.0% relative to Dashboard alone. In a
usability study, participants benefited from the integrated dashboard-and-chat workflow,
with high task accuracy, moderate workload, and favorable ratings for state-aware
interaction mechanisms. These results suggest that TwinBI improves both agent-level
analytical reliability and user-facing analytical support by turning visible dashboard
state into richer actionable context. Our dataset and source code are available at:
https://github.com/simonjisu/TwinBI

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13731v1
- Authors: Jisoo Jang Wen-Syan Li
- Published: 2026-06-11T11:49:31Z
- Age days: 3

</details>
