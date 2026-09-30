---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19796v1"
published: "2026-09-17T07:07:03Z"
age_days: 0
score: 27
created: 2026-09-18
concepts: ["视觉语言动作模型 VLA", "机器人学习"]
---

# LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> LIFD让机器人记住当前镜头外的空间，并根据历史与当前图像补全场景表示；生成过程用当前几何证据约束，供操作策略使用。

## 问题

部分可观测操作中，当前RGB特征只能描述可见结构，先前看见的区域会离开视野。模型既要保存历史，又要推断缺失内容，并保持与当前观测一致。

## 创新点或方法

通过多视角一致性学习场景令牌，使用单帧RGB和循环记忆完成表示；rectified flow生成令牌，Anchor-Guided Cross-Attention用当前几何特征约束补全，再通过紧凑槽特征连接策略。训练用多视角和几何监督，部署用单RGB相机、本体状态及任务指令。

## 证据

分阶段训练版本在LIBERO平均成功率91.6%、MetaWorld为79.8%，LIBERO比联合训练高3.1个百分点。UR5e四类任务每类10条示范时，平均成功率56.0%，OpenVLA-7B为40.5%。

## 局限

需核查记忆、生成补全与几何锚定各自收益，以及预测内容错误时如何影响动作；摘要中的实机平均成功率仍为56.0%。

- **判断**：值得精读场景记忆和训练分阶段设计，尤其适合遮挡与视野变化明显的操作任务。

## 研究关联

对VLA与机器人学习，提供在单相机部署条件下利用训练期多视角监督和历史记忆的具体路径。

- **概念**：视觉语言动作模型 VLA 机器人学习
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/LIFD Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation under partial observability requires spatial information that extends beyond the current view. Geometry-aware RGB features describe visible structure, but previously observed regions may disappear as the robot or scene moves. Maintaining a useful scene representation therefore requires retaining observation history while inferring missing content without losing its connection to visible evidence. We introduce LIFD (Look, Imagine, Focus, and Do), a framework for persistent, 3D-aware scene memory. LIFD learns a scene-token representation from multi-view agreement and completes it from a single RGB view and recurrent memory. A rectified-flow model generates the tokens while Anchor-Guided Cross-Attention conditions completion on current geometric features. Compact slot features connect this representation to a manipulation policy. Multi-view and geometric supervision are used during representation learning; deployment requires one RGB camera, proprioception, and a task instruction. LIFD (Staged) reaches 91.6% average success on LIBERO and 79.8% on MetaWorld, improving LIBERO average success by 3.1 percentage points over Joint training. On four UR5e task families with ten demonstrations per family, it achieves 56.0% mean success, compared with 40.5% for OpenVLA-7B.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19796v1
- Authors: Wenbo Li, Yiteng Chen, Wenhao Li, Qingyao Wu
- Published: 2026-09-17T07:07:03Z
- Age days: 0

</details>
