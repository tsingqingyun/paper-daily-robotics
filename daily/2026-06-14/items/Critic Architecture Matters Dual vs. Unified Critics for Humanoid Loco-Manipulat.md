---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11891v1"
published: "2026-06-10T10:21:38Z"
age_days: 3
score: 27
created: 2026-06-14
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation

> [!summary] 一句话结论（基于摘要）
> We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets.

## 关键点

- **问题**：Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy.
- **创新点 / 方法**：We present a controlled comparison on the Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation policies through a sequential curriculum spanning 13 levels from stationary reaching to walking with variable-orientation targets.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/Critic Architecture Matters Dual vs. Unified Critics for Humanoid Loco-Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multi-objective reinforcement learning for humanoid robots must coordinate locomotion
and manipulation within a single policy. A natural design choice is whether to use a
single (unified) critic that estimates the combined value of all objectives, or separate
(dual) critics with disjoint reward signals. We present a controlled comparison on the
Unitree G1 humanoid (23 active DoF) in NVIDIA Isaac Lab, training loco-manipulation
policies through a sequential curriculum spanning 13 levels from stationary reaching to
walking with variable-orientation targets. In standardized evaluation, dual-critic
policies reach targets 3.5$\times$ faster (6.5 vs. 22.6 simulation steps), achieve
2$\times$ higher throughput (14.3 vs. 7.0 validated reaches per 1,000 steps), and attain
higher validated reach rates (65.2% vs. 53.8%) compared to the unified-critic policy.
Notably, additional anti-gaming reward mechanisms provide no further improvement beyond
the architectural change alone (60.9% vs. 65.2%). These results have direct implications
for the emerging paradigm of RL fine-tuning of imitation-learned policies: when refining
a pre-trained manipulation policy with RL, a unified critic risks suppressing the
learned behavior through competing locomotion gradients. These findings demonstrate that
critic architecture is a primary - and often overlooked - design choice in multi-
objective humanoid RL, with greater impact than reward engineering on reaching
efficiency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11891v1
- Authors: Mehmet Turan Yardımcı
- Published: 2026-06-10T10:21:38Z
- Age days: 3

</details>
