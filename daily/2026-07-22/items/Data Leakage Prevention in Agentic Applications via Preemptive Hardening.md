---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18847v1"
published: "2026-07-21T08:35:22Z"
age_days: 0
score: 28
created: 2026-07-22
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Data Leakage Prevention in Agentic Applications via Preemptive Hardening

> [!summary] 一句话结论（基于摘要）
> To address this challenge in multi agentic systems, we present a pre-deployment pipeline for scanning, hardening, and validation of agentic applications.

## 关键点

- **问题**：Agentic systems integrate LLM driven planning with interfaces to external tools, making data leakage and tool misuse feasible via instruction/data boundary failures and prompt injection attacks.
- **创新点 / 方法**：To address this challenge in multi agentic systems, we present a pre-deployment pipeline for scanning, hardening, and validation of agentic applications.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Agentic systems integrate LLM driven planning with interfaces to external tools, making
data leakage and tool misuse feasible via instruction/data boundary failures and prompt
injection attacks. Enforcing required controls consistently is particularly challenging
in workflows spanning many codebases and heterogeneous agents. To address this challenge
in multi agentic systems, we present a pre-deployment pipeline for scanning, hardening,
and validation of agentic applications. The pipeline analyzes prompt templates, tool
interfaces, and tool-invocation code to identify leakage-enabling patterns and generate
actionable patches. The hardened application is then validated through adversarial
prompt injection attacks and benign input variations ensuring that mitigations do not
disrupt intended behavior. In the hardening stage, high-risk tools are prioritized, and
minimally invasive mitigations are applied, including schema tightening, boundary
sanitization, allowlist-based tool gating, and least-privilege checks. In the validation
stage, the pipeline automatically generates attack inputs that mimic jailbreaks,
instruction overrides, and tool-targeted manipulation, along with benign task variants,
to confirm that the functionality of the hardened application is preserved after
remediation. We evaluated the pipeline on five real-world agentic applications, as well
as on the AgentDojo benchmark. Across all applications, the proposed pipeline identified
recurring leakage-enabling patterns and generated patches that can be integrated without
disrupting the intended application behavior. The resulting modifications of application
code were shown to eliminate leaks when targeted by basic jailbreak and instruction-
override attacks, achieving a 100% reduction in leakage, and reduce leaks by 91% under
conditions of stress-induced manipulation, without the need of continuous runtime policy
enforcement.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18847v1
- Authors: Akansha Shukla, Emily Bellov, Parth Atulbhai Gandhi, Yuval Elovici, Asaf Shabtai
- Published: 2026-07-21T08:35:22Z
- Age days: 0

</details>
