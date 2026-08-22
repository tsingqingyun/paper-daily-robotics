---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19375v1"
published: "2026-08-19T18:41:27Z"
age_days: 2
score: 24
created: 2026-08-22
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control

> [!summary] 一句话结论（基于摘要）
> We develop a neural reduced dynamics (NRD) framework that separates the state the model propagates from what can be supplied as an input or recovered analytically, trains policies entirely inside the frozen learned model, and validates them back in the high-f…

## 关键点

- **问题**：High-fidelity embodied AI simulators provide realistic evaluation of complex robotic systems, but their computational cost limits their direct use for large-scale reinforcement learning campaigns.
- **创新点 / 方法**：We develop a neural reduced dynamics (NRD) framework that separates the state the model propagates from what can be supplied as an input or recovered analytically, trains policies entirely inside the frozen learned model, and validates them back in the high-fidelity simulator.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Learning the Right Abstraction Neural Reduced Dynamics for Complex Robot Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

High-fidelity embodied AI simulators provide realistic evaluation of complex robotic systems, but their computational cost limits their direct use for large-scale reinforcement learning campaigns. We advocate the use of less accurate but more expeditious simulations, which might draw on data-driven, e.g., neural dynamics, models. This contribution argues that the practical value of a neural dynamics model for complex robot control lies in learning the \emph{right abstraction}: a reduced state that preserves the control-relevant physics of the high-fidelity system while enabling high-throughput policy learning. We develop a neural reduced dynamics (NRD) framework that separates the state the model propagates from what can be supplied as an input or recovered analytically, trains policies entirely inside the frozen learned model, and validates them back in the high-fidelity simulator. Two case studies instantiate it across three control tasks: terrain-aware HMMWV trajectory tracking on rigid, bumpy and deformable Continuum Representation Model (CRM) terrain; and goal reaching for a stock tracked vehicle and its front-mounted articulated arm. Every policy transfers back to the high-fidelity simulator. A single policy trained inside the terrain-conditioned dynamics model, and given no terrain input of its own, attains lower median and mean tracking error than both single-terrain specialists on all three terrains, including zero-shot bumpy terrain. Quantitatively, the tracked vehicle reaches 100 of 100 goals and the arm 97 of 100, with zero contacts or joint-limit violations. The NRD models advance roughly four orders of magnitude faster in simulated time than the high-fidelity simulator scenes they replace, making iterative on-policy learning practical and supporting neural reduced dynamics as a bridge between accurate but expensive physics simulation and scalable robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19375v1
- Authors: Harry Zhang, Dan Negrut
- Published: 2026-08-19T18:41:27Z
- Age days: 2

</details>
