---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.31207v1"
published: "2026-09-25T12:45:36Z"
age_days: 2
score: 36
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling

> [!summary] 先说人话（基于摘要）
> 这项工作把不同双指夹爪看到的操作场景转换到统一夹爪坐标系，让策略围绕“夹爪、手中物体、目标”的交互学习。它试图减少策略对机器人外观和观察视角的依赖。

## 问题

跨机器人模仿学习容易把任务语义与硬件视觉几何绑在一起，导致换夹爪、平台或视角后难以泛化。目标是在异构双指夹爪平台间实现零样本仿真到现实迁移。

## 创新点或方法

输入语言和 RGB-D，由 VLM 识别子任务并定位交互三元组，SAM 2.1 跟踪掩码以减少 VLM 查询。参数化通用夹爪建立规范坐标表示，结合目标与碰撞人工势场、局部分割点云，再由 Flow-Matching Transformer 输出平滑的 7 自由度动作块。

## 证据

摘要报告仿真与真实任务实验，声称同时实现有竞争力的基准成绩和跨平台、跨视角零样本迁移。摘要未给出可核查的结果数字，也未列出具体平台与基准分数。

## 局限

共享结构明确限定在双指夹爪；“极端迁移”和“首次”的覆盖范围，以及对 VLM 定位和掩码跟踪的依赖，都需全文核查。

- **判断**：值得读表示构建与跨平台实验细节，是否具有广泛迁移价值取决于实际测试差异有多大。

## 研究关联

对机器人学习和 Sim2Real 研究者，价值在于把跨本体泛化落实为坐标、交互对象和几何特征的规范化，提供了可检查的表示设计。

- **概念**：多模态基础模型 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulati.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Achieving robust cross-embodiment generalization in imitation learning demands overcoming a critical representation flaw that inextricably entangles task semantics with hardware-specific visual geometry. We propose an interaction-centric framework that leverages the shared structure of two-finger grippers via a parameterized universal gripper abstraction, yielding a canonical gripper-frame representation. Given language and RGB-D observations, a VLM infers the subtask and grounds an interaction triplet (gripper, held, target), while SAM~2.1 tracks masks to reduce VLM queries. We design concise hybrid features that combine target/collision artificial potential fields for global guidance with segmented gripper-frame point clouds for local geometry, and use a Flow-Matching Transformer to predict smooth 7-DoF action chunks. Experiments in simulation and real-world tasks demonstrate that ours is the first imitation learning approach to simultaneously achieve competitive benchmark scores and extreme cross-embodiment/cross-viewpoint zero-shot sim-to-real transfer to completely distinct, heterogeneous robot platforms.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.31207v1
- Authors: Guanlin Li, Shifeng Bao, Yihan Zhao, Haitao Shen, Haoyang Li, Chen Zhao, Tong Yang, Jie Tang, Jing Zhang
- Published: 2026-09-25T12:45:36Z
- Age days: 2

</details>
