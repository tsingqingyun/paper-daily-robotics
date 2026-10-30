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
url: "https://arxiv.org/abs/2610.37215"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-10-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution

> [!summary] 这篇论文到底做了什么（基于摘要）
> Retrieve to Act（R2A）在 VLA 执行时检索训练示范中的运动片段，用历史几何经验修正当前动作。基础 VLA 保持冻结，另一个学到的门控按动作维度决定该借用多少检索结果。

## 问题

VLA 能理解新指令，却可能因背景等分布外视觉变化而走错空间轨迹。摘要指出，已有测试时方法主要压制误导性的视觉线索，却没有充分利用训练经验中仍然可靠的运动学信息。本文要解决的是执行中的轨迹失真，而不是重新学习整个任务。

### 用一个例子理解

理解用例（非论文实验）：更换桌布后，VLA 把抓杯动作预测得偏向一侧。输入是当前执行信息和 VLA 动作；系统从图中找到兼容的接近杯子片段，门控融合位置等维度，输出修正动作。这里的任务及纠正过程是解释用例。

## 创新点或方法

本文将成功训练示范离线整理成时空运动基元图。推理时，查询相关的图神经网络把当前执行定位到图中，检索结构兼容的后续运动；逐维门控再将检索运动与冻结 VLA 的动作融合。这样既能借历史轨迹修正空间错误，也试图保留基础策略对局部变化的反应。基础策略无需微调，但图网络和门控是学到的组件，其训练目标与数据划分未说明；因此不能把它理解为整个系统无需训练。

### 方法如何工作

1. 把成功示范整理为时空运动图，保留可供执行时调用的历史几何关系。
2. 根据当前查询在图中定位执行位置，找到与当前过程兼容的后续运动片段。
3. 由逐维门控融合检索运动和冻结 VLA 的预测，使不同动作维度能够采用不同程度的修正。
4. 输出融合动作以继续执行；查询更新频率和门控具体训练方法，摘要未说明。

### 必要术语

- 运动基元：可复用的一段运动；本文将其组织成图并检索后续片段。
- 运动学先验：历史示范中关于怎么移动的几何经验；用于补偿视觉变化下的轨迹错误。
- 逐维门控：分别决定各动作分量如何融合；用于平衡检索修正与基础策略反应。

## 证据

摘要报告在 GR00T N1.7、π₀.₅ 和 StableVLA 三种架构上测试，仿真涉及 LIBERO-Plus、RoboTwin2.0-Plus。成功率绝对增幅最高为仿真 12 个百分点、真机 40 个百分点（摘要）。这些是最高增幅，不代表平均收益；摘要没有提供各模型基线成功率、扰动明细和试验次数。证据支持对所测情境扰动的改善，不能直接扩展到新动力学或新技能。

## 局限

关键待核查问题是：在视觉已经失真的情况下，当前查询如何可靠定位到正确图节点。还需看示范未覆盖的运动、不同初始姿态，以及检索错误时门控是否会引入额外偏差。摘要没有交代图大小、查询延迟和运动坐标对齐方式，这些都影响实际复用。

- **判断**：值得细读查询定位、坐标对齐和逐维门控，这三处决定它能否在视觉变化时真正提供可靠的运动修正。

## 研究关联

可借鉴的是把已有示范当作执行时可查询的运动资源，而不只当作训练材料。当主要变化来自画面、所需运动仍被历史经验覆盖时，检索几何片段可能是一条有用的补偿路径。

### 下一步读哪里

先核查查询包含哪些视觉、状态或历史信息，以及运动片段怎样对齐当前坐标。再看门控训练、错误检索消融和运行延迟；实验要分清最高收益、平均收益，以及视觉扰动和几何变化的边界。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/Retrieve to Act Motion Primitive Graph Retrieval for Robust VLA Execution.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.37215v1 Announce Type: cross Abstract: Vision-Language-Action (VLA) policies demonstrate remarkable semantic generalization, yet remain highly vulnerable to out-of-distribution (OOD) visual shifts during execution. While existing test-time methods attempt to suppress spurious visual cues, they fundamentally overlook the rich, uncorrupted kinematic priors embedded in the policy's own training experience. We introduce Retrieve to Act (R2A), a test-time scaling framework that formulates OOD robustness purely as a geometric motion primitive retrieval problem. R2A bypasses fragile visual features by structuring successful training demonstrations into an offline spatiotemporal motion primitive graph. During inference, a query-dependent Graph Neural Network dynamically localizes the robot's ongoing execution within this graph, retrieving structurally compatible future motion primitives. These retrieved geometric priors are then seamlessly harmonized with the frozen VLA's predicted actions via a learned, dimension-wise gating mechanism, adaptively rectifying erroneous spatial trajectories while preserving the policy's local reactivity. Extensive experiments across three state-of-the-art VLA architectures, GR00T N1.7, $\pi_{0.5}$, and StableVLA, demonstrate that R2A consistently and significantly enhances robustness against diverse contextual perturbations. R2A achieves absolute success rate improvements of up to +12% in simulation benchmarks (LIBERO-Plus, RoboTwin2.0-Plus) and +40% in real-world deployments, without requiring any finetuning of the base policies. Project page: https://retrieve2act.github.io/r2a/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37215
- Authors: Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen, Duc-Duy Nguyen, Hung T. Ho, Linh Dang Le, Trong-Bao Ho, Thien-Loc Ha, Tan Q. Nguyen, Tuan Dam, Vu N. Duong, Daniel Sonntag, Ngan Le, Khoa D. Doan, Jan Peters, An Thai Le, Duy M. H. Nguyen, Vien Anh Ngo
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
