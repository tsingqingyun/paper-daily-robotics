---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14585v1"
published: "2026-06-12T16:01:50Z"
age_days: 3
score: 22
created: 2026-06-16
concepts: ["智能体 Agent", "世界模型"]
---

# Sensitivity Shaping for Latent Modeling

> [!summary] 一句话结论（基于摘要）
> We show that these surrogates can fail when the dynamics are locally insensitive to critical action choices: unsupported control actions may produce latent predictions that resemble demonstrated transitions, suppressing OOD signals despite large true predicti…

## 关键点

- **问题**：Generative dynamics models enable planning in challenging robotic systems, but safe deployment requires reliably detecting policy-induced out-of-distribution (OOD) transitions.
- **创新点 / 方法**：To address this, we introduce support- conditioned control-sensitivity regularization, which promotes sensitive local response to control input changes in learned dynamics in high-support training regions.
- **证据**：We show that these surrogates can fail when the dynamics are locally insensitive to critical action choices: unsupported control actions may produce latent predictions that resemble demonstrated transitions, suppressing OOD signals despite large true predictive errors.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generative dynamics models enable planning in challenging robotic systems, but safe
deployment requires reliably detecting policy-induced out-of-distribution (OOD)
transitions. Existing methods typically treat the learned dynamics as fixed and attach
post hoc support surrogates. We show that these surrogates can fail when the dynamics
are locally insensitive to critical action choices: unsupported control actions may
produce latent predictions that resemble demonstrated transitions, suppressing OOD
signals despite large true predictive errors. To address this, we introduce support-
conditioned control-sensitivity regularization, which promotes sensitive local response
to control input changes in learned dynamics in high-support training regions. This
preserves control-induced variation while limiting unstable extrapolation due to weak
empirical support. Experiments in vision-based obstacle avoidance, manipulation, and
real-robot navigation show improved OOD detection and safer closed-loop planning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14585v1
- Authors: Hongzhan Yu, Chenghao Li, Ruipeng Zhang, Henrik Christensen, Sicun Gao
- Published: 2026-06-12T16:01:50Z
- Age days: 3

</details>
