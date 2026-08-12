---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21518v1"
published: "2026-07-23T17:02:11Z"
age_days: 1
score: 23
created: 2026-07-25
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation

> [!summary] 一句话结论（基于摘要）
> Using OpenAI's gpt-5.6-sol model alias, we test 25 pre-specified mirrored trade-off profiles.

## 关键点

- **问题**：Even a current high-capability LLM can appear safer when shown a dangerous objective directly than when other agents transform and relay its direction.
- **创新点 / 方法**：Using OpenAI's gpt-5.6-sol model alias, we test 25 pre-specified mirrored trade-off profiles.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：A user with endpoint-only access likewise cannot directly inspect those upstream messages including the objective.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Even a current high-capability LLM can appear safer when shown a dangerous objective
directly than when other agents transform and relay its direction. Using OpenAI's
gpt-5.6-sol model alias, we test 25 pre-specified mirrored trade-off profiles. Direct
exposure to an objective authorizing concealment, fabrication, and pressure produced
advice net opposed to its target. After an Id and Censor transformed the same objective
into affect and a constraint-rewritten, target-bearing intention, the user-facing
Superego---which saw the preferred direction but not the raw objective, its manipulative
clauses, or its source---produced advice net aligned with the target. This behavioral
reverse shift is consistent with the model recognizing or distrusting the manipulative
motive, although we do not identify its internal mechanism. The second result exposes a
compositional safety gap: a current high-capability model can be used as the user-facing
component of an automated, multi-stage workflow serving an explicitly manipulative
objective. The workflow can keep the raw instruction, its manipulation-authorizing
clauses, and its provenance outside the downstream model's context while preserving the
objective's target direction. A user with endpoint-only access likewise cannot directly
inspect those upstream messages including the objective.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21518v1
- Authors: Linjun Li
- Published: 2026-07-23T17:02:11Z
- Age days: 1

</details>
