---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19475v1"
published: "2026-08-19T22:17:31Z"
age_days: 3
score: 21
created: 2026-08-23
concepts: ["具身智能评测与基准"]
---

# Measuring What a Specification Determines: A Formal Semantic-Block Model and an Execution-Judged Benchmark

> [!summary] 一句话结论（基于摘要）
> A specification is represented as a structure comprising semantic blocks, dependency relations, block-owned rules, decision points, and explicitly open questions, subject to four machine-checkable well-formedness conditions: acyclicity, single ownership, cons…

## 关键点

- **问题**：This work introduces a formal semantic-block model for specifications and an execution-judged benchmark for evaluating specification quality independently of model capability.
- **创新点 / 方法**：A specification is represented as a structure comprising semantic blocks, dependency relations, block-owned rules, decision points, and explicitly open questions, subject to four machine-checkable well-formedness conditions: acyclicity, single ownership, constraint domination, and totality or ambiguity-stop.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/Measuring What a Specification Determines A Formal Semantic-Block Model and an E.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This work introduces a formal semantic-block model for specifications and an execution-judged benchmark for evaluating specification quality independently of model capability. A specification is represented as a structure comprising semantic blocks, dependency relations, block-owned rules, decision points, and explicitly open questions, subject to four machine-checkable well-formedness conditions: acyclicity, single ownership, constraint domination, and totality or ambiguity-stop. Determinacy is defined model-theoretically as agreement among all conforming implementations and is estimated empirically through convergence across independent implementers. The model is instantiated on an Oracle-to-PostgreSQL migration specification containing 18 blocks and 19 dependency edges. Computational validation shows that the five-layer decomposition reduces mean per-task context by approximately 71% through dependency closures, covers 85.5% of the study-defined Oracle construct taxonomy with all identified gaps triaged, is not Pareto-dominated by the tested alternative partitions, and is recovered at the 99.9th percentile from citation-derived edges not used to define the original structure. The benchmark keeps the implementer panel fixed, includes a mandatory no-specification control arm, and uses PostgreSQL 16 and a live Oracle instance as deterministic execution judges. Six designed studies, including three pre-registered manipulations and three diagnostic analyses, further examine specification effects. Repeated runs on a 25-unit subsample reveal an empirical variability floor with a median arm-delta spread of 14.4 percentage points. The results support determinacy as a formal concept but not as a standalone empirical quality metric for the evaluated contemporary LLM implementers.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19475v1
- Authors: Oleg Grynets, Dmytro Kostetskyi, Vasyl Lyashkevych
- Published: 2026-08-19T22:17:31Z
- Age days: 3

</details>
