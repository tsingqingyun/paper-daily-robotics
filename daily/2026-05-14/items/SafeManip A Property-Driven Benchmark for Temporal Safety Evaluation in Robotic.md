---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12386v1"
published: "2026-05-12T16:49:28Z"
age_days: 1
score: 32
created: 2026-05-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Results show that even strong models often behave unsafely.

## 关键点

- **问题**：Many safety failures are temporal: a robot may touch a clean surface after contamination or release an object before it is fully inside an enclosure.
- **创新点 / 方法**：We introduce SafeManip, a property-driven benchmark to explicitly evaluate temporal safety properties in robotic manipulation, moving beyond prior evaluations that largely focus on task completion or per-state constraint violations.
- **证据**：Results show that even strong models often behave unsafely.
- **局限**：Robotic manipulation is typically evaluated by task success, but successful completion does not guarantee safe execution.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation is typically evaluated by task success, but successful completion
does not guarantee safe execution. Many safety failures are temporal: a robot may touch
a clean surface after contamination or release an object before it is fully inside an
enclosure. We introduce SafeManip, a property-driven benchmark to explicitly evaluate
temporal safety properties in robotic manipulation, moving beyond prior evaluations that
largely focus on task completion or per-state constraint violations. SafeManip defines
reusable safety templates over finite executions using Linear Temporal Logic over finite
traces (LTLf). It maps observed rollouts to symbolic predicate traces and evaluates them
with LTLf-based monitors. Its property suite covers eight manipulation safety
categories: collision and contact safety, grasp stability, release stability, cross-
contamination, action onset, mechanism recovery, object containment, and enclosure
access. Templates can be instantiated with task-specific objects, fixtures, regions, or
skills, allowing the same safety specifications to generalize across tasks and
environments. We evaluate SafeManip on six vision-language-action policies, including
$π_0$, $π_{0.5}$, GR00T, and their training variants, across 50 RoboCasa365 household
tasks. Results show that even strong models often behave unsafely. Task-success gains do
not reliably translate into safer execution: many successful rollouts remain unsafe,
while longer-horizon or more complex tasks expose more violations. SafeManip provides a
reusable evaluation layer for diagnosing temporal safety failures and measuring safe
success beyond task completion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12386v1
- Authors: Chengyue Huang, Khang Vo Huynh, Sebastian Elbaum, Zsolt Kira, Lu Feng
- Published: 2026-05-12T16:49:28Z
- Age days: 1

</details>
