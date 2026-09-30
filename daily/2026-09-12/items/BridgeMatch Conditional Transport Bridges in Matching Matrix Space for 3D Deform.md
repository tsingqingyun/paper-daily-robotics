---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11472v1"
published: "2026-09-10T12:39:58Z"
age_days: 1
score: 25
created: 2026-09-12
concepts: ["世界模型"]
---

# BridgeMatch: Conditional Transport Bridges in Matching Matrix Space for 3D Deformable Registration

> [!summary] 先说人话（基于摘要）
> BridgeMatch在非刚性点云配准时保留完整的软匹配候选，避免粗匹配阶段过早删掉正确对应，再逐步细化匹配矩阵。

## 问题

粗到细配准常只保留top-K区域以省计算，但弱而正确的候选可能被删除，导致精匹配永远无法恢复这些对应。

## 创新点或方法

先在粗分辨率匹配矩阵上进行去噪扩散，再按层级提升到高分辨率；第二阶段以条件传输桥细化，分别采用确定性CFM ODE和受Schrödinger桥启发的随机Brownian-bridge SDE。

## 证据

在4DMatch和4DLoMatch上，两种变体均提高对应精度与下游配准表现，低重叠场景收益更大；使用相同形变求解器、无需目标域适配时，CAPE和DeepDeform跨数据集泛化也改善。摘要未给出可核查的结果数字。


## 局限

需核查高分辨率完整软匹配矩阵的资源开销，以及精度提升与计算成本之间的权衡。

- **判断**：做非刚性三维感知值得读算法与复杂度，纯世界模型研究可略读。

## 研究关联

对具身感知和可变形物体操作有潜在前端价值；与世界模型的关联较间接，摘要没有动作或动态预测验证。

- **概念**：世界模型
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/BridgeMatch Conditional Transport Bridges in Matching Matrix Space for 3D Deform.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable non-rigid point cloud correspondences are important for deformable anatomical registration, embodied perception and manipulation, and dynamic 3D reconstruction. Coarse-to-fine methods reduce computational cost by selecting the top-\(K\) coarse regions. However, this pruning may remove weak but correct hypotheses and restrict fine matching to an incomplete search space. We present \paper, a two-stage generative solver that maintains the complete soft matching matrix at both coarse and high resolutions. Stage~I uses denoising diffusion to estimate a global matching matrix in the compact coarse-resolution space. We then lift this matrix to high resolution while preserving its hierarchy. The lifted matrix is rank-bounded and block-constant. Stage~II refines it through a conditional transport bridge. We implement the bridge with two types of dynamics: a deterministic endpoint-parameterized conditional Flow Matching (CFM) ODE and a stochastic Brownian-bridge SDE inspired by Schrödinger bridges. Both variants share the lifted source, a time-conditioned transformer, and a matching-matrix endpoint predictor. Experiments on 4DMatch and 4DLoMatch show that both variants produce more accurate correspondences than the compared methods and improve downstream registration, with larger gains in low-overlap cases. They also improve cross-dataset generalization on CAPE and DeepDeform without target-domain adaptation while using the same deformation solver.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11472v1
- Authors: Qianliang Wu, Haobo Jiang, Guangwei Gao, Shuo Chen, Jin Xie, Jian Yang, Yaqing Ding
- Published: 2026-09-10T12:39:58Z
- Age days: 1

</details>
