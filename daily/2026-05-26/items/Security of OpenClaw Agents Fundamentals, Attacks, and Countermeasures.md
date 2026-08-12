---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25435v1"
published: "2026-05-25T05:25:39Z"
age_days: 1
score: 26
created: 2026-05-26
concepts: ["智能体 Agent"]
---

# Security of OpenClaw Agents: Fundamentals, Attacks, and Countermeasures

> [!summary] 一句话结论（基于摘要）
> In this survey, we present a comprehensive study of the security landscape of OpenClaw agents.

## 关键点

- **问题**：In particular, the combination of high-privilege operations and persistent memory exposes OpenClaw agents to various emerging threats, including skill poisoning, cognitive manipulation, multi-agent cascading failures, and supply-chain vulnerabilities.
- **创新点 / 方法**：In this survey, we present a comprehensive study of the security landscape of OpenClaw agents.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/Security of OpenClaw Agents Fundamentals, Attacks, and Countermeasures.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The rapid evolution of large language model (LLM)-driven autonomous agents has given
rise to OpenClaw, a new class of open-source agent frameworks that operate as
continuously running, skill-augmented systems with persistent memory, multi-channel
interaction, and high degrees of autonomy. Such capabilities enable OpenClaw agents to
autonomously execute complex, multi-step tasks and interact seamlessly with external
applications, but simultaneously introduce a substantially enlarged attack surface. In
particular, the combination of high-privilege operations and persistent memory exposes
OpenClaw agents to various emerging threats, including skill poisoning, cognitive
manipulation, multi-agent cascading failures, and supply-chain vulnerabilities. In this
survey, we present a comprehensive study of the security landscape of OpenClaw agents.
We first examine the general architecture and key characteristics that distinguish
OpenClaw agents from traditional AI agent systems. We categorize existing security and
privacy threats into a layered framework and analyze how vulnerabilities arise during
agent reasoning, action execution, and external interaction. Representative defense
mechanisms are also reviewed to draw the current defense landscape. Finally, several
unresolved issues related to the reliability and trustworthiness of OpenClaw ecosystems
are discussed.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25435v1
- Authors: Yuntao Wang, Jianle Ba, Han Liu, Yanghe Pan, Jintao Wei, Zhou Su, Tom H. Luan, Linkang Du
- Published: 2026-05-25T05:25:39Z
- Age days: 1

</details>
