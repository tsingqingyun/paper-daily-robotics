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
url: "https://arxiv.org/abs/2610.21429v1"
published: "2026-10-15T07:40:22Z"
age_days: 2
score: 26
created: 2026-10-18
concepts: ["具身智能评测与基准"]
---

# MuSTMM: Learning Sound-Triggered Mobile Manipulation across Multiple Scenes

> [!summary] 这篇论文到底做了什么（基于摘要）
> MuSTMM 测试机器人能否在陌生建筑里，听到声音后找到相关物体并操作它。它还给导航策略加入由历史深度观测积累的空间地图，让声音提示和已见过的几何结构一起指路。

## 问题

声音触发移动操作要求连续完成听声、导航和物理交互。瓶颈是声音不能直接告诉机器人墙在哪里、该怎么绕路。摘要指出，已有评测主要在有限建筑结构里改变物体布局，难以检验换一栋建筑后是否还能成功。

### 用一个例子理解

理解用例（非论文实验）：机器人听见另一间房里设备报警；输入声音、深度图和位姿，系统把走过的走廊与墙体记入地图，结合声源方向选择绕行路线，最终输出通往设备附近的导航动作，为后续操作创造条件。

## 创新点或方法

评测从有限建筑内的布局变化，改为训练与测试场景分离。方法上，为 Navigation Policy Model 增加显式空间记忆：把不同位置采集的深度观测对齐到共同坐标系，再转成机器人视角的俯视占据图；地图特征与声音上下文融合，产生兼顾目标位置和场景结构的导航描述。训练目标与流程未说明；运行时需要持续积累观测并更新地图。

### 方法如何工作

1. 接收声音与深度观测，分别获得声源线索和当前可见几何。
2. 利用位姿把深度观测对齐并积累，让离开视野的结构仍可被使用。
3. 将记忆投影为自身视角的俯视占据图，得到与当前导航方向相关的空间表示。
4. 融合地图和声音形成目标描述，指导机器人进入可进行物理交互的目标区域；交互策略细节摘要未说明。

### 必要术语

- 双耳房间脉冲响应：描述声音经房间传播后到达双耳的变化；用于生成空间听觉线索。
- 俯视占据图：从上方表示障碍与空间的地图；本文由深度记忆生成。
- 场景分离划分：训练与测试使用不同场景；用于检验陌生建筑中的表现。

## 证据

摘要提供：数据集覆盖 31 个场景，预计算 1436 万个双耳房间脉冲响应，并设置陌生场景的单事件与多事件测试。导航策略相对已有方法成功率提高 2.60%，组件消融支持空间记忆有效。摘要未给基线名称、原始成功率，也未说明 2.60% 是相对增幅还是百分点，因此不能据此判断提升的绝对规模。

## 局限

数据使用空间音频渲染，摘要没有提供真机证据。我的待核查问题是位姿误差怎样影响地图积累，以及收益主要来自导航改善还是最终操作改善；提供的材料不足以拆开判断。

- **判断**：值得读数据划分和地图构建细节；它的阅读重点是陌生场景评测是否严格，以及记忆为何帮助完成任务。

## 研究关联

这里的启示是，声学定位和路径选择需要不同信息。若任务必须穿过陌生空间才能操作目标，保存已观察几何可能比只增强声音编码更直接；同时，测试应真正隔离建筑场景，避免把熟悉布局中的成功误当成跨场景能力。

### 下一步读哪里

核查场景如何隔离、声音事件如何设置、成功是否要求完成物理交互；再看有无记忆的消融，以及地图对位姿精度和历史长度的要求。

- **概念**：具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/MuSTMM Learning Sound-Triggered Mobile Manipulation across Multiple Scenes.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Sound-Triggered Mobile Manipulation (STMM) requires robots to respond to sound events by navigating to the associated objects and performing appropriate physical interactions. Existing STMM evaluations primarily vary object layouts within limited architectural structures, leaving challenges to unseen scenes insufficiently explored. We introduce Multi-scene Sound-Triggered Mobile Manipulation (MuSTMM), a dataset that combines spatial audio rendering and physical interaction across 31 scenes with diverse architectures and object layouts. MuSTMM contains 14.36 million precomputed binaural Room Impulse Responses (RIRs) and a scene-disjoint split for evaluating single-event and multi-event settings in unseen scenes. We further augment the Navigation Policy Model with explicit spatial memory that complements acoustic cues with observed geometry. Specifically, we accumulate pose-aligned depth observations in a shared coordinate frame and project this memory into an egocentric Bird's-Eye View (BEV) occupancy map. Fusing map features with sound context produces a goal descriptor that provides both target-location and scene-structure priors, guiding navigation to the target region required for subsequent physical interaction. This policy achieves a 2.60% success rate boost over existing methods, while component ablations further support the effectiveness of spatial memory. MuSTMM and the navigation policy provide a testbed for the new challenge of studying sound-triggered mobile manipulation in unseen scenes. The code and dataset will be released upon acceptance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21429v1
- Authors: Hao Ju, Feng Yan, Zhihao Zhong, Heng Yang, Shaofei Huang, Zhedong Zheng
- Published: 2026-10-15T07:40:22Z
- Age days: 2

</details>
