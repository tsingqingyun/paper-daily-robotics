---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.26730v1"
published: "2026-11-19T19:25:14Z"
age_days: 4
score: 27
created: 2026-11-24
concepts: ["具身智能评测与基准"]
---

# SparseHPS: A Unified Model for Human Pose and Shape across Depth Cameras and LiDARs

> [!summary] 这篇论文到底做了什么（基于摘要）
> SparseHPS 用同一套权重，从深度相机或 LiDAR 的人体点云估计三维姿态、体形和位置。它统一训练标签，用共享方式解码各个关节，并在连续输入时用历史帧补充当前观测。

## 问题

两类传感器都能测量真实尺度下的三维点，但不同设备的点云密度可相差十倍以上。已有方法通常按传感器分别设计，公开数据集的人体模型也不兼容，难以直接混训。稀疏的 LiDAR 扫描还让部分方法依赖长序列，限制了只有当前帧时能做的估计。

### 用一个例子理解

理解用例（非论文实验）：输入一帧行人的稀疏 LiDAR 扫描。各关节查询从体素特征中找对应线索，投票估计人体整体所在位置。若前几帧曾看到当前被挡住的手腕，历史特征也可参与估计，最后输出人体姿态、体形和全局平移。

## 创新点或方法

SparseHPS 先把不同来源的标签统一成 SMPL-X，再合用十个数据集训练。模型用 LitePT 在有观测点的体素上提取特征，各关节用自己的可学习查询取信息，再由同一个输出头解码。体素投票另行估计人体的全局位置。推理能用单帧，也能从前七帧的特征记忆中补信息，无需未来观测。摘要未说明训练时如何安排单帧和多帧输入。

### 方法如何工作

1. 统一渲染点云和真实采集点云的人体标签，让不同来源监督同一套输出。
2. 把观测点归入稀疏体素，由 LitePT 提取局部三维特征。
3. 用关节查询从点云特征取信息，再共享解码规则，使各关节使用统一的预测方式。
4. 用体素投票估计人体全局位置。有连续帧时再利用过去的特征，为当前估计补充线索。

### 必要术语

- SMPL-X：用参数描述人体几何和姿态的人体模型；这里用它统一不同数据集的预测目标。
- 根节点相对关节误差：以人体根节点为参照计算关节误差；本文用它衡量 LiDAR 上的相对姿态精度。
- 因果记忆：只保存过去观测特征的记忆；模型用前七帧补信息，流式运行时无需等待未来帧。

## 证据

摘要报告，在 SLOPER4D 和 FreeMotion 两个 LiDAR 基准上，相对人体根节点计算的关节误差分别比最强既有方法低 22% 和 11%，对方需要 32 帧。在 Azure Kinect 实采的 HuMMan 留出受试者上，关节误差为 34.7 毫米，摘要未明确该数是否采用同样的根节点对齐口径。摘要称单帧已取得大部分精度，但未给出单帧与连续输入的具体差值。

## 局限

作者的结果覆盖所列基准和 Azure Kinect 留出受试者。我会核查有没有整种设备留出的评估，以及极稀疏或遮挡时误差多大。LiDAR 的根节点对齐误差主要衡量关节相对位置，判断整体落点还需要看全局平移指标。

- **判断**：值得读到数据标签转换、指标定义和单帧消融，因为这三处决定同一套权重可以迁移到什么条件。

## 研究关联

跨传感器复用可以先从统一预测目标入手。若不同数据源对同一个关节的定义都不一致，混合训练会同时引入传感器差异和标签差异。先统一人体表示，再量化历史帧的增益，才能判断部署时有多依赖连续输入。

### 下一步读哪里

先核查各数据集怎样转成 SMPL-X 以及训练和评估如何划分。再找单帧与记忆版本的误差差值，并查看全局平移是否有单独的结果。

- **概念**：具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/SparseHPS A Unified Model for Human Pose and Shape across Depth Cameras and LiDA.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recovering 3D human pose and shape from point clouds is central to motion capture, robotics and self-driving vehicles, because depth cameras and LiDARs sense a person directly in metric 3D and work under any lighting. However, current approaches are each tailored to one sensor type: point density differs by more than ten times between devices, public datasets are labeled with incompatible body models, and LiDAR approaches need long input sequences to offset sparse scans. In this work, we present SparseHPS, a novel sensor-agnostic network that recovers SMPL-X pose, shape and global translation from a human point cloud with one set of weights, for single frames and streams alike. Specifically, SparseHPS encodes the cloud with a LitePT backbone over sparse voxels, represents every joint by a learnable query decoded with one common head, localizes the body by voting over voxels, and draws temporal context from a causal memory of tokens from the seven preceding frames. A single model is trained on ten datasets that mix rendered clouds with real depth-camera and LiDAR captures, all converted to one body model. Experiments demonstrate state-of-the-art results on the SLOPER4D and FreeMotion LiDAR benchmarks, where SparseHPS lowers the root-relative joint error by 22% and 11%, respectively, compared with the strongest prior method, which needs 32 frames. On real Azure Kinect captures of held-out HuMMan subjects, SparseHPS attains a joint error of 34.7 mm. Moreover, the current frame alone already yields the bulk of this accuracy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.26730v1
- Authors: Ilya Zaychuk
- Published: 2026-11-19T19:25:14Z
- Age days: 4

</details>
