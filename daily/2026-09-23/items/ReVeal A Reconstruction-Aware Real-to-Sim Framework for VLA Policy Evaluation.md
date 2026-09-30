---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23910v1"
published: "2026-09-20T22:36:15Z"
age_days: 2
score: 34
created: 2026-09-23
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ReVeal: A Reconstruction-Aware Real-to-Sim Framework for VLA Policy Evaluation

> [!summary] 先说人话（基于摘要）
> ReVeal研究重建出来的仿真环境是否足够可靠，能否用来评价真实机器人的VLA。它把重建质量指标与真实、仿真中的闭环策略表现对齐检查。

## 问题

仿真评测虽然可扩展、可重复，但场景重建误差可能改变策略表现，使模拟结果无法准确反映真实能力。

## 创新点或方法

结合工作空间重建、重建质量测量和匹配的闭环评测；NVMF衡量观测保真度，APGF衡量平面几何保真度，并用单目深度监督的PGSR-D改善多视角线索不足处的几何。

## 证据

8个评估场景中，两项指标可区分2DGS、PGSR与PGSR-D。GR00T、SmolVLA和π₀.₅在8项人形操作任务中的匹配评测显示，重建保真度与真实—仿真表现一致性的排序一致。

## 局限

摘要支持的是有限场景与管线中的关联，没有提供通用误差阈值；视觉及平面几何保真也不能代表所有物理因素。

- **判断**：搭建真实场景仿真评测时值得精读，重点看指标对策略表现差异的解释范围。

## 研究关联

对具身评测，价值在于先验证评测环境本身，帮助判断仿真中的策略排名和失败结论能否用于现实。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/ReVeal A Reconstruction-Aware Real-to-Sim Framework for VLA Policy Evaluation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Simulation-based evaluation provides a scalable and repeatable alternative to real-world evaluation of vision-language-action (VLA) policies. However, reconstruction errors can cause simulated policy performance to diverge from real-world performance, motivating the need to assess reconstructed environments for downstream VLA policy evaluation. We present ReVeal, a real-to-sim assessment framework combining workspace reconstruction, reconstruction-level assessment, and matched closed-loop policy evaluation. Novel-View Mesh Fidelity (NVMF) and Annotated Planar Geometry Fidelity (APGF) assess observation and planar geometric fidelity, respectively. We also develop PGSR-D, a reconstruction pipeline incorporating monocular depth supervision to improve geometry where multi-view visual cues are limited. Across 8 assessment scenes, NVMF and APGF consistently distinguish the fidelity of 2DGS, PGSR, and PGSR-D. Matched evaluations of GR00T, SmolVLA, and pi0.5 across 8 humanoid manipulation tasks show consistent ordering between reconstruction fidelity and real-sim performance agreement across pipelines. Further analysis of the evaluation workspaces shows that higher fidelity is associated with stronger real-sim agreement.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23910v1
- Authors: Xinyi Wang, Heng Hao, Wenjun Hu, Anna Enyu Li, Dizhi Ma, Karthik Ramani, Hankyu Moon, Yeong-Dae Kwon
- Published: 2026-09-20T22:36:15Z
- Age days: 2

</details>
