---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01442v1"
published: "2026-07-01T20:05:46Z"
age_days: 1
score: 33
created: 2026-07-03
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# From Forgeries to Foundation Models: A Systematic Survey of Identity Document Attack and Detection

> [!summary] 一句话结论（基于摘要）
> The resulting attack surface spans physical presentation, digital injection, and fully generative synthesis, introducing distinct forensic failure modes that require a unified threat model and evaluation framework.

## 关键点

- **问题**：Identity document forgery has undergone a fundamental capability shift: generative AI tools now enable high-fidelity document synthesis and field-level manipulation with minimal technical expertise, while detection methods remain constrained by benchmarks that do not reflect this threat.
- **创新点 / 方法**：The resulting attack surface spans physical presentation, digital injection, and fully generative synthesis, introducing distinct forensic failure modes that require a unified threat model and evaluation framework.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Identity document forgery has undergone a fundamental capability shift: generative AI
tools now enable high-fidelity document synthesis and field-level manipulation with
minimal technical expertise, while detection methods remain constrained by benchmarks
that do not reflect this threat. The resulting attack surface spans physical
presentation, digital injection, and fully generative synthesis, introducing distinct
forensic failure modes that require a unified threat model and evaluation framework.
This survey provides, to our knowledge, the first unified treatment of Presentation
Attacks, Digital Injection Attacks, and GenAI-driven synthesis within a single identity
verification threat model. We trace detection methodologies from rule-based heuristics
through forensic localisation, injection-aware pipelines, foundation models, and few-
shot frameworks. A systematic audit of public datasets from 2019--2025 exposes a
persistent Reality Gap between benchmark conditions and operational deployment. We
further analyse large multimodal models for identity document manipulation, identifying
Script-Dependent Generative Instability (SDGI) as a recurring typographic failure mode
in non-Latin script inpainting. Finally, zero-shot benchmarking on unseen synthesised ID
cards shows that even the strongest publicly available models achieve APCER values above
25% under security-oriented operating conditions, highlighting substantial limits in
cross-domain generalisation. We conclude by outlining future directions toward
forensically grounded, privacy-preserving, and legally accountable identity verification
systems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01442v1
- Authors: Gourab Das, Pavan Kumar C, Raghavendra Ramachandra
- Published: 2026-07-01T20:05:46Z
- Age days: 1

</details>
