---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09196v1"
published: "2026-08-10T07:08:44Z"
age_days: 0
score: 31
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# SAIN: Structure-Aware Interactive Navigation with Active Dialogue Grounding for Mobile Robot

> [!summary] 一句话结论（基于摘要）
> On the VL-LN IIGN benchmark, SAIN improves SR from 20.2 to 25.4 and SPL from 13.07 to 14.17 over the strongest reported dialogue-enabled baseline, while requiring no task-specific policy training.

## 关键点

- **问题**：However, real-world robots often encounter natural human instructions that are ambiguous, underspecified, or incomplete, requiring them to resolve such uncertainties through active questioning.
- **创新点 / 方法**：We present SAIN, a zero-shot framework that turns active dialogue into persistent navigation state.
- **证据**：On the VL-LN IIGN benchmark, SAIN improves SR from 20.2 to 25.4 and SPL from 13.07 to 14.17 over the strongest reported dialogue-enabled baseline, while requiring no task-specific policy training.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Most existing vision-language navigation tasks assume that instructions are complete and
unambiguous. However, real-world robots often encounter natural human instructions that
are ambiguous, underspecified, or incomplete, requiring them to resolve such
uncertainties through active questioning. Interactive Instance Goal Navigation (IIGN)
requires an embodied agent to find the specific instance under an ambiguous category-
level instruction through active dialogue. However, existing dialogue-enabled methods
often consume oracle answers as transient textual context for immediate decisions,
rather than persistent spatial or object-centric structured state. We present SAIN, a
zero-shot framework that turns active dialogue into persistent navigation state. Instead
of consuming oracle answers as one-step text hints, SAIN compiles them into target
evidence, route-level corridor memory, and object-candidate labels. These states are
stored in structured value, room, graph, and object memories, then consumed by a unified
policy for frontier ranking and final target approach. On the VL-LN IIGN benchmark, SAIN
improves SR from 20.2 to 25.4 and SPL from 13.07 to 14.17 over the strongest reported
dialogue-enabled baseline, while requiring no task-specific policy training. The results
support dialogue-to-state conversion as an effective zero-shot mechanism for long-
horizon interactive instance navigation. Project website:
https://zorattc.github.io/SAIN/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09196v1
- Authors: Yuhao Cao, Xiao Liu, Yang Xie, Lu Liu, Haoyao Chen
- Published: 2026-08-10T07:08:44Z
- Age days: 0

</details>
