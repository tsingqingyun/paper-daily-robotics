---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19425v1"
published: "2026-08-19T20:24:29Z"
age_days: 3
score: 21
created: 2026-08-23
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation

> [!summary] 一句话结论（基于摘要）
> SCAPE also improves testing sample efficiency, produces narrower calibrated prediction intervals, generalizes better to out-of-distribution scenarios, and enables fine-grained deployment strategies.

## 问题

Reliable performance evaluation is a central bottleneck for deploying robot-learning policies in real-world conditions.

## 创新点或方法

We propose SCAPE, a scenario-conditioned simulation-augmented policy evaluation framework that predicts scenario-conditioned real-world policy performance using limited paired sim-and-real samples and large-scale simulation rollouts.

## 证据

SCAPE also improves testing sample efficiency, produces narrower calibrated prediction intervals, generalizes better to out-of-distribution scenarios, and enables fine-grained deployment strategies.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：世界模型 Sim2Real 具身智能评测与基准
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/SCAPE Scenario-Conditioned Simulation-Augmented Policy Evaluation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable performance evaluation is a central bottleneck for deploying robot-learning policies in real-world conditions. Real-world testing is faithful but costly and difficult to scale, whereas simulation-based testing scales easily but is inevitably biased by the sim-to-real gap. Existing simulation-augmented methods combine limited real-world rollouts with abundant simulation proxies, but focus on performance averaged over initial conditions and deployment settings. Such population-level averages obscure scenario-specific variation and provide limited guidance about when and where a policy can be safely deployed. We propose SCAPE, a scenario-conditioned simulation-augmented policy evaluation framework that predicts scenario-conditioned real-world policy performance using limited paired sim-and-real samples and large-scale simulation rollouts. SCAPE corrects sim-to-real bias in simulation labels before training the prediction model and calibrates prediction uncertainty through conformal prediction. We validate SCAPE on autonomous driving and quadruped velocity tracking. In sim-to-sim studies, SCAPE reduces scenario-level prediction error by 4.9%/34.7% (driving) and 14.5%/27.7% (quadruped) relative to scene-conditioned neural and aggregate statistical baselines on average. We further evaluate a velocity-tracking policy deployed on a physical Unitree Go2. SCAPE also improves testing sample efficiency, produces narrower calibrated prediction intervals, generalizes better to out-of-distribution scenarios, and enables fine-grained deployment strategies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19425v1
- Authors: Dijie Zhu, Seunghun Oh, Ruopeng Huang, Zhiyu Huang, Jiaqi Ma, Chen Tang
- Published: 2026-08-19T20:24:29Z
- Age days: 3

</details>
