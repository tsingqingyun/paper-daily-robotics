---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14551v1"
published: "2026-06-12T15:30:18Z"
age_days: 2
score: 25
created: 2026-06-15
concepts: ["智能体 Agent"]
---

# TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation

> [!summary] 一句话结论（基于摘要）
> Across real-world long-horizon manipulation tasks with visually ambiguous branch points, TRACE improves branch selection and task success over alternative baselines, including short-history and recurrent memory.

## 关键点

- **问题**：TRACE stores task-relevant visual and robot-state evidence, such as object identity, target choice, or route-dependent state, in a fixed- size latent memory that remains bounded over long episodes.
- **创新点 / 方法**：We introduce TRAjectory-routed Causal Evidence (TRACE), a memory framework for visuomotor imitation policies.
- **证据**：Across real-world long-horizon manipulation tasks with visually ambiguous branch points, TRACE improves branch selection and task success over alternative baselines, including short-history and recurrent memory.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots under autonomous operation may require decisions based on evidence that is no
longer visible. We study \emph{delayed-evidence} tasks, where an early cue disappears
before a later decision point, so visually similar observations can require different
actions. In these settings, the current observation is not a sufficient state for
control. We introduce TRAjectory-routed Causal Evidence (TRACE), a memory framework for
visuomotor imitation policies. TRACE stores task-relevant visual and robot-state
evidence, such as object identity, target choice, or route-dependent state, in a fixed-
size latent memory that remains bounded over long episodes. Instead of indexing memory
by raw time or manually provided task labels, TRACE uses \emph{path signatures}:
compact, order-sensitive features of the executed robot-state trajectory. These
signatures do not store the visual cue itself; rather, they provide trajectory-
conditioned keys for writing and retrieving the evidence stored when the cue was
visible. When the robot later reaches an ambiguous observation, the policy conditions on
TRACE memory to recover the missing context and choose the correct branch. TRACE
attaches through lightweight adapters to policies, without changing the policy backbone,
action head, or imitation objective. Across real-world long-horizon manipulation tasks
with visually ambiguous branch points, TRACE improves branch selection and task success
over alternative baselines, including short-history and recurrent memory. Project page:
https://jeong-zju.github.io/trace

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14551v1
- Authors: Zihao Li, Ranpeng Qiu, Yincong Chen, Guoqiang Ren, Weiming Zhi
- Published: 2026-06-12T15:30:18Z
- Age days: 2

</details>
