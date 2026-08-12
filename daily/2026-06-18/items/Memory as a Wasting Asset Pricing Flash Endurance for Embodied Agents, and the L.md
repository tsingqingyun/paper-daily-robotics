---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18144v1"
published: "2026-06-16T16:43:19Z"
age_days: 1
score: 34
created: 2026-06-18
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So

> [!summary] 一句话结论（基于摘要）
> Whether wear-aware placement improves task value remains open -- $χ$ is measured against a value proxy, and the non- monotone optimum, while proven, is not yet observed in data.

## 关键点

- **问题**：Whether wear-aware placement improves task value remains open -- $χ$ is measured against a value proxy, and the non- monotone optimum, while proven, is not yet observed in data.
- **创新点 / 方法**：A robot's flash endurance is a non-renewable stock: every persisted write spends one of a few thousand program/erase cycles and never refills, yet no fielded robot memory system prices which memories are worth an erase cycle.
- **证据**：Whether wear-aware placement improves task value remains open -- $χ$ is measured against a value proxy, and the non- monotone optimum, while proven, is not yet observed in data.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A robot's flash endurance is a non-renewable stock: every persisted write spends one of
a few thousand program/erase cycles and never refills, yet no fielded robot memory
system prices which memories are worth an erase cycle. We treat embodied memory as
depreciating capital and price that stock with a single endurance shadow price $η$,
which makes cost-minimizing placement across a RAM / on-board NVM / cloud hierarchy a
threshold in a wear-augmented per-byte index. The index is cost-optimal whatever the
sign of the value-write association $χ$; only when $χ> 0$ does the optimum turn non-
monotone, sending a robot's most valuable memories off its flash. The pivot is thus
empirical, and we measure $χ$ on real robot logs at a pre-specified gate: its sign is a
property of the deployment regime -- positive on recurrent long-horizon manipulation
($\hatχ \approx +1.0 \times 10^{-3}$, replicated at full power), null on a shorter-
horizon suite, and negative on non-recurrent teleoperation. Two boundaries scope the
result. The endurance budget is dormant on premium 3,000-P/E TLC at datasheet prices and
binding on the commodity QLC/eMMC ($\sim$1,000 P/E) that cheaper edge robots run. And
where it binds, a learned wear-aware controller only ties price-based routing on task
value, because realized value is tier-invariant across RAM, NVM, and cloud: the rent
governs device lifetime and cost, not task performance. Whether wear-aware placement
improves task value remains open -- $χ$ is measured against a value proxy, and the non-
monotone optimum, while proven, is not yet observed in data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18144v1
- Authors: Josef Liyanjun Chen
- Published: 2026-06-16T16:43:19Z
- Age days: 1

</details>
