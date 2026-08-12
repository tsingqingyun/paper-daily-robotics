---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19774v1"
published: "2026-06-18T04:14:11Z"
age_days: 1
score: 31
created: 2026-06-20
concepts: ["具身智能评测与基准"]
---

# Start Right, Arrive Right: Asynchronous Execution via Initial Noise Selection

> [!summary] 一句话结论（基于摘要）
> In summary, \texttt{PAINT} requires no gradients, retraining, or policy modification; yet it improves execution consistency and task performance across \textit{12 simulated benchmarks} and \textit{6 real-world manipulation tasks} spanning single-arm, bimanual…

## 关键点

- **问题**：Existing methods address this problem by steering generation toward the already executed action prefix.
- **创新点 / 方法**：We introduce \textbf{PAINT}, a training-free method that finds this noise via backward Euler inversion and constructs the final chunk through a repainting rule.
- **证据**：In summary, \texttt{PAINT} requires no gradients, retraining, or policy modification; yet it improves execution consistency and task performance across \textit{12 simulated benchmarks} and \textit{6 real-world manipulation tasks} spanning single-arm, bimanual, and humanoid embodiments.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action chunking enables robot policies to produce temporally coherent behavior, but
generating multi-step action sequences with flow-based policies incurs latency that is
incompatible with real-time control. Under asynchronous execution, the robot continues
executing the current chunk while the next one is generated, causing even minor delays
to create inconsistencies at chunk boundaries. Existing methods address this problem by
steering generation toward the already executed action prefix. We instead show that
prefix consistency can be achieved by selecting an appropriate initial noise before
generation begins, allowing the unmodified flow ODE to produce a coherent next chunk.
This reframes asynchronous inference as a noise selection problem rather than a
trajectory steering problem. We introduce \textbf{PAINT}, a training-free method that
finds this noise via backward Euler inversion and constructs the final chunk through a
repainting rule. In summary, \texttt{PAINT} requires no gradients, retraining, or policy
modification; yet it improves execution consistency and task performance across
\textit{12 simulated benchmarks} and \textit{6 real-world manipulation tasks} spanning
single-arm, bimanual, and humanoid embodiments. Website: ~\href{https://paint-action-
chunking.github.io}{\texttt{https://paint-action-chunking.github.io}}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19774v1
- Authors: Trong-Bao Ho, Quang-Tan Nguyen, Thien-Loc Ha, Gia-Binh Nguyen, Viet-Thanh Nguyen, Long Dinh, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
- Published: 2026-06-18T04:14:11Z
- Age days: 1

</details>
