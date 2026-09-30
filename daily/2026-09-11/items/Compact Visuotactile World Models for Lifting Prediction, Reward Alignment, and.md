---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09597v1"
published: "2026-09-09T01:50:54Z"
age_days: 1
score: 26
created: 2026-09-11
concepts: ["世界模型"]
---

# Compact Visuotactile World Models for Lifting: Prediction, Reward Alignment, and Force Constraints

> [!summary] 先说人话（基于摘要）
> However, tactile persistence achieves lower errors of 0.095 and 0.498 N, respectively.

## 问题

However, tactile persistence achieves lower errors of 0.095 and 0.498 N, respectively.

## 创新点或方法

Accurate contact prediction is useful for robotic manipulation only if it supports effective decisions.

## 证据

However, tactile persistence achieves lower errors of 0.095 and 0.498 N, respectively.


## 局限

The evidence is limited to public sensing records and simulator execution, without a demonstrated transfer between them.

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：世界模型
- **筛选分数**：26
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Compact Visuotactile World Models for Lifting Prediction, Reward Alignment, and.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Accurate contact prediction is useful for robotic manipulation only if it supports effective decisions. We investigate this connection using a compact, randomly initialized visuotactile world model, trajectory-level uncertainty calibration, and behavior-initialized actor-critic learning in imagination. On 160 MuJoCo Lift episodes, adding touch reduces endpoint-force prediction error from 1.058 to 0.228 N and interval-peak error from 2.724 to 0.523 N across three training seeds. However, tactile persistence achieves lower errors of 0.095 and 0.498 N, respectively. Two exploratory control rounds comprise 680 executions on 40 independent test initial conditions. A matched reward revision on fresh test environments increases in-distribution 10 cm lifting success from 20.0% to 93.3%, while success within an 8 N per-finger budget reaches only 33.3%, compared with 70.0% for force feedback. Calibration margins reduce force violations at the cost of task completion. In a separate study of public GelSight recordings, a force regressor achieves 0.04234 N error, but frame-level calibration covers only 15.80% of complete trajectories; trajectory-level calibration raises this to 87.36% at nominal 90% coverage. Together, these findings distinguish improvements in sensing and task reward from improvements in force-constrained control. The evidence is limited to public sensing records and simulator execution, without a demonstrated transfer between them.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09597v1
- Authors: Qinzhen Ma, Sida Peng
- Published: 2026-09-09T01:50:54Z
- Age days: 1

</details>
