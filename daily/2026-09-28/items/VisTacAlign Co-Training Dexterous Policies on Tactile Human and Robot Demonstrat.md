---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30959v1"
published: "2026-09-25T08:12:04Z"
age_days: 3
score: 28
created: 2026-09-28
concepts: ["多模态基础模型", "机器人学习"]
---

# VisTacAlign: Co-Training Dexterous Policies on Tactile Human and Robot Demonstrations

> [!summary] 先说人话（基于摘要）
> VisTacAlign 将人类示范的手部动作、视觉观测和触觉信号都转换到机器人侧可用的形式，再与机器人数据联合训练灵巧操作策略。它特别处理人手与机器手在三维视觉误差上的差异。

## 问题

人类示范便宜，但视觉触觉策略同时消费多种模态，仅对齐动作不足以跨越人机差异。视觉几何、遮挡及触觉信号都可能不一致。

## 创新点或方法

将手套追踪动作重定向到 17 自由度触觉机器手并做一次指尖校正；双目图像中用机器人网格替换人手，再重跑立体模型，使点云具有机器人式误差和可见性。触觉映射为统一逐指力表示，扩散 Transformer 接收点云、本体感知和触觉 token。

## 证据

在乐高装配、不同大小草莓采摘、启动并举起电钻三个真机任务上，加入对齐后的人类示范优于仅用机器人数据；消融支持触觉输入和视觉对齐均有必要。摘要未给出可核查的结果数字。

## 局限

需核查一次性校正和触觉映射的适用范围，以及人类数据加入后的预算对照；摘要的证据限于三个任务。

- **判断**：做灵巧手和人类示范共训练值得精读数据处理部分，其工程接口比泛化口号更有价值。

## 研究关联

对多模态机器人学习研究者，它提醒跨本体数据复用需要对齐传感器观测特性，而不仅是理想几何或动作坐标，并给出视觉触觉联合处理流程。

- **概念**：[[多模态基础模型]] [[机器人学习]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/VisTacAlign Co-Training Dexterous Policies on Tactile Human and Robot Demonstrat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human demonstrations are a cheap source of data for dexterous manipulation, but co-training a robot policy on them requires closing the human--robot gap in every modality the policy consumes. We present VisTacAlign, a framework for co-training 3D-visual-tactile dexterous policies on human and robot demonstrations. Glove-tracked human hand motion is retargeted to a 17-DoF tactile robot hand with a one-time fingertip correction. The human hand is then erased from both stereo views and replaced by a posed robot-hand mesh painted with pixels from robot recordings, and a real-time stereo foundation model is re-run on the composite, so the human point clouds carry the same stereo errors and visibility as the robot ones. Finally, a capacitive tactile glove is aligned to the robot's fingertip sensors in its signal space, giving one interpretable per-finger force representation. A diffusion transformer consumes point-cloud, proprioceptive, and per-finger tactile tokens. On three real-world tasks requiring precise force -- Lego assembly, plucking strawberries of varying size, and activating and lifting a power drill -- adding aligned human demonstrations to existing robot data improves over robot-only policies, and ablations show that both tactile input and visual alignment are necessary. Project page: https://vis-tac-align.github.io

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30959v1
- Authors: Julien Poffet, Matthew Strong, Ankush Dhawan, Baiyu Shi, Shalika Neelaveni, Yujia Yuan, Zhenan Bao, Monroe Kennedy
- Published: 2026-09-25T08:12:04Z
- Age days: 3

</details>
