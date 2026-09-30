---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19142v1"
published: "2026-09-16T17:59:30Z"
age_days: 1
score: 38
created: 2026-09-18
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics

> [!summary] 先说人话（基于摘要）
> PointZero通过“补全三维点未来怎么走”学习动力学：给定一张RGB-D观测和少量局部轨迹，预测所有已观测点的未来轨迹，预训练不需要机器人动作标签。

## 问题

现有动作条件三维动力学方法通常依赖机器人动作标注，阻碍利用无动作标签的视频。核心问题是找到既能学习交互动态、又能迁移到机器人任务的预训练目标。

## 创新点或方法

用Transformer完成稀疏部分三维轨迹到全体可见点未来轨迹的补全，在290万帧合成数据上预训练。后训练时分别加入末端位姿条件做动力学预测，或联合预测动作与三维轨迹做模仿学习。

## 证据

数据覆盖可变形、关节式和刚体对象；摘要称同数据训练下优于既有方法，在PGND上优于基线，在7项仿真与实机操作任务中的6项优于或持平基线，并评估了从零训练以区分架构和预训练收益。

## 局限

摘要实际报告的是合成数据预训练，并非网络视频训练；从普通视频获得RGB-D与部分三维轨迹的条件仍需核查。

- **判断**：值得精读预训练目标及从零训练对照，重点判断可迁移先验究竟来自目标设计、架构还是数据。

## 研究关联

对世界模型与机器人学习，价值是把动力学预训练从特定机器人的动作接口中解耦，同时用下游动力学和控制两类任务检验迁移。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/PointZero 3D Point Track Completion for Learning Transferable 3D Dynamics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models endow perceptual systems with the ability to predict how scenes evolve under interaction. They are most beneficial when trained on diverse volumes of data, to instill a rich prior into downstream applications. Existing methods typically require robot action labels to learn action-conditioned 3D dynamics, which excludes web video data from the training pool. We study 3D point track completion as a pre-training objective for learning transferable 3D dynamics without robot data. Given a single RGB-D observation and sparse partial 3D trajectories (tracks), we predict future 3D tracks of all observed points. We show this objective produces a rich 3D dynamics prior, without requiring robot action labels. We contribute a diverse dataset of 2.9 million synthetic frames spanning deformable, articulated, and rigid objects, and use it to train PointZero. We show that a flexible and expressive transformer, PointZero, outperforms prior methods on the same data. We demonstrate the utility of our pre-training objective by post-training PointZero for two downstream applications: (1) action-conditioned 3D dynamics prediction and (2) imitation learning. When fine-tuned to condition on end-effector pose, PointZero outperforms the baselines on the recent PGND 3D dynamics benchmark. When fine-tuned to predict robot actions and 3D tracks, PointZero outperforms or matches the baselines on 6/7 simulated and real-world robot manipulation tasks. We furthermore evaluate training PointZero from scratch to isolate the benefits of our proposed architecture from those of our proposed pre-training objective and dataset. We release the dataset, checkpoints, and full training recipe.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19142v1
- Authors: Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung, Bowen Wen, Stan Birchfield, Yunzhu Li, Deva Ramanan, Jeffrey Ichnowski
- Published: 2026-09-16T17:59:30Z
- Age days: 1

</details>
