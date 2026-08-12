---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23079v1"
published: "2026-06-22T09:27:50Z"
age_days: 2
score: 29
created: 2026-06-25
concepts: ["智能体 Agent", "世界模型"]
---

# AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control

> [!summary] 一句话结论（基于摘要）
> Based on this structure, we propose AdaReP, a training-free wrapper that adapts the replanning tolerance online using the current deviation from the cached rollout and a local sensitivity estimate, without modifying the learned world model or planner.

## 关键点

- **问题**：Neural world models coupled with model predictive control (MPC) replan at every environment step to bound accumulated prediction error, but this incurs substantial computational overhead.
- **创新点 / 方法**：Based on this structure, we propose AdaReP, a training-free wrapper that adapts the replanning tolerance online using the current deviation from the cached rollout and a local sensitivity estimate, without modifying the learned world model or planner.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/AdaReP Adaptive Re-Planning under Model Mismatch for Neural World-Model Predicti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Neural world models coupled with model predictive control (MPC) replan at every
environment step to bound accumulated prediction error, but this incurs substantial
computational overhead. Reusing a cached plan reduces this overhead, yet its
effectiveness depends on how prediction mismatch propagates through the local dynamics.
We analyze this trade-off with a perturbation-based dynamic-regret framework and show
that stale-plan penalties scale with the reuse tolerance, the accumulated mismatch since
the last replanning step, and the local dynamics sensitivity. Based on this structure,
we propose AdaReP, a training-free wrapper that adapts the replanning tolerance online
using the current deviation from the cached rollout and a local sensitivity estimate,
without modifying the learned world model or planner. Across image-space planning,
latent-space control, and real-world robotic manipulation, AdaReP substantially reduces
planner-side computation while maintaining comparable task performance, including over
80% fewer queries on a 50-trial physical robot study.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23079v1
- Authors: Yutian Cheng, Xiaojian Ma, Xianhao Wang, Min Yang, Rongpeng Su, Hangxin Liu, Xi Chen, Shuai Li, Qing Li
- Published: 2026-06-22T09:27:50Z
- Age days: 2

</details>
