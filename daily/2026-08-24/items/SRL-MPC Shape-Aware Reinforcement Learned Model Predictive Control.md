---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.21175v1"
published: "2026-08-21T14:46:06Z"
age_days: 2
score: 23
created: 2026-08-24
concepts: ["机器人学习", "具身智能评测与基准"]
---

# SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control

> [!summary] 一句话结论（基于摘要）
> The results show that SRL-MPC substantially outperforms representative baselines in safety and adaptability.

## 关键点

- **问题**：Safe and efficient shape-aware navigation in heterogeneous crowds and robot fleets remains challenging.
- **创新点 / 方法**：Toward this end, we propose Shape-Aware Reinforcement Learned Model Predictive Control (SRL-MPC), a method for safe, efficient, and adaptive navigation in crowds with heterogeneous shapes without geometry simplification.
- **证据**：The results show that SRL-MPC substantially outperforms representative baselines in safety and adaptability.
- **局限**：Safe and efficient shape-aware navigation in heterogeneous crowds and robot fleets remains challenging.

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/SRL-MPC Shape-Aware Reinforcement Learned Model Predictive Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safe and efficient shape-aware navigation in heterogeneous crowds and robot fleets remains challenging. Traditional approaches often assume homogeneous robots, sparse workspaces, simplified geometry, offline computation, or handcrafted parameters to make the problem tractable, which limits their deployment in dense crowd scenarios. Toward this end, we propose Shape-Aware Reinforcement Learned Model Predictive Control (SRL-MPC), a method for safe, efficient, and adaptive navigation in crowds with heterogeneous shapes without geometry simplification. To encode shape-aware safety, we formulate high-order control barrier function (HOCBF) constraints from geometric separation features (GSFs) based on support function transformation. A reinforcement learning (RL) framework then learns a neural policy that reads GSFs and outputs real-time MPC parameter updates, enabling the MPC solver to adapt to neighboring crowd geometries. The key advantage of SRL-MPC is that it preserves the safety structure and generalizability of MPC while integrating the adaptability and intelligence of RL. Experiments in randomized crowd scenarios with arbitrary shaped robot fleets demonstrate the effectiveness, scalability, and robustness of SRL-MPC. The results show that SRL-MPC substantially outperforms representative baselines in safety and adaptability. Project website: https://hanruihua.github.io/srl_mpc_project/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.21175v1
- Authors: Ruihua Han, Rui Gao, Zhe Liu, Xinyi Wang, Chang Chen, Shuai Wang, Qi Hao, Jia Pan, Hengshuang Zhao
- Published: 2026-08-21T14:46:06Z
- Age days: 2

</details>
