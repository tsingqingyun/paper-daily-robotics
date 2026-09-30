---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19574v1"
published: "2026-08-20T02:28:25Z"
age_days: 3
score: 22
created: 2026-08-23
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> HiTac-WAM achieves a mean contact F1 of 0.921; under matched training budgets, the directed hierarchy reduces 3D displacement L2 error by 17.6% relative to the deformation-only predictor and improves slip AUPRC by 60.4% relative to the slip-only predictor.

## 问题

World action models jointly predict future visual observations and actions, whereas existing tactile-aware variants typically represent future touch as an image or latent stream without modeling the physical dependencies that organize tactile states hierarchically.

## 创新点或方法

We present HiTac-WAM, a hierarchical tactile world action model that forecasts a sequence of future tactile states for each candidate action chunk before execution.

## 证据

HiTac-WAM achieves a mean contact F1 of 0.921; under matched training budgets, the directed hierarchy reduces 3D displacement L2 error by 17.6% relative to the deformation-only predictor and improves slip AUPRC by 60.4% relative to the slip-only predictor.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/HiTac-WAM A Hierarchical Tactile World Action Model for Contact-Rich Robot Manip.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World action models jointly predict future visual observations and actions, whereas existing tactile-aware variants typically represent future touch as an image or latent stream without modeling the physical dependencies that organize tactile states hierarchically. We present HiTac-WAM, a hierarchical tactile world action model that forecasts a sequence of future tactile states for each candidate action chunk before execution. The forecast factorizes into contact state, a 3D deformation field, and slip risk, organized as a directed hierarchy in which each downstream stage is conditioned on stop-gradient signals from preceding stages. A directed attention mask allows tactile queries to attend to the video-action context of each candidate while preventing video and action queries from attending to tactile tokens. For planning, HiTac-WAM ranks candidate action chunks using tactile forecasts and task-progress estimates. For execution, the selected tactile forecast is retained as a reference; persistent discrepancies between predicted and observed tactile states trigger corrective replanning. HiTac-WAM achieves a mean contact F1 of 0.921; under matched training budgets, the directed hierarchy reduces 3D displacement L2 error by 17.6% relative to the deformation-only predictor and improves slip AUPRC by 60.4% relative to the slip-only predictor. Across chip grasping, blackboard erasing, and USB insertion, selection guided by the hierarchical forecasts increases the average real-robot success rate from 31.1% to 61.1%, while the full system attains 72.2%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19574v1
- Authors: Chao Xue, Chaofan Zhang, Wenxuan Ma, Guocai Yao, Shaowei Cui, Shuo Wang
- Published: 2026-08-20T02:28:25Z
- Age days: 3

</details>
