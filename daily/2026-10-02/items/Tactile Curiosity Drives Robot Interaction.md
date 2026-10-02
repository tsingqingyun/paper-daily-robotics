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
url: "https://arxiv.org/abs/2609.40134"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 40
created: 2026-10-02
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Tactile Curiosity Drives Robot Interaction

> [!summary] 这篇论文到底做了什么（基于摘要）
> TacEx 把机器人的探索兴趣集中到“触觉上还有哪些接触现象没弄懂”。这样收集的数据更偏向碰触、抓取等操作过程，再用于离线学习拾放技能或后训练 VLA。

## 问题

操作技能来自接触，但随机动作常让机器人把大量训练时间花在空中运动。按模型分歧或认知不确定性探索虽然更有方向，也可能被空中无规律运动吸引：难预测的变化未必对操作有用。

### 用一个例子理解

理解用例（非论文实验）：输入物体图像、机器人状态和触觉读数→TacEx 驱动机器人尝试尚不熟悉的接触，记录动作及结果→离线学习器利用这些交互训练拿起并放置物体的策略。

## 创新点或方法

旧做法奖励整体不确定性，TacEx 按感觉模态拆分模型不确定性，把好奇心引向触觉通道。探索阶段无需任务奖励或专家演示，通过接触相关的不确定性驱动交互；随后用收集的数据离线学习拾放策略，不再增加环境交互，也用于后训练原先未使用触觉预训练的 VLA。摘要未说明不确定性计算、模型结构及最终策略执行时是否仍需触觉。

### 方法如何工作

1. 把不同感觉通道的模型不确定性分开估计，使系统能够识别触觉相关的未知变化。
2. 让探索偏向触觉不确定性，增加接触交互；具体动作优化过程摘要只说明到此。
3. 保存这些交互形成数据集，使后续学习能够利用操作所需的接触经验。
4. 用数据离线学习拾放策略，或后训练 VLA，将探索所得转化为下游任务能力。

### 必要术语

- 认知不确定性：模型因经验不足而不确定；本文把它按感觉模态拆开用于探索。
- 内在奖励：由学习系统产生的探索动力；本文聚焦触觉相关信息。
- 离线策略学习：用已有交互记录学习动作策略；本文的下游拾放学习无需新增环境交互。

## 证据

摘要报告，无任务奖励和专家演示的探索可以产生密集接触数据，支持下游拾放策略的离线学习；TacEx 后训练也显著改善 VLA 的下游表现，并具有较高样本效率。但摘要没有列出测试环境、仿真或真机属性、基线名称、成功率及样本数。因此目前只能复述这些定性结果，无法估计提升幅度或硬件适用范围。

## 局限

需要核查触觉不确定性是否会被传感器噪声或重复碰撞持续放大，以及数据是否覆盖多样、可迁移的接触。探索时不使用任务奖励，也不代表下游策略学习不需要任务标签或其他监督；摘要未说明这些条件。

- **判断**：值得读到探索奖励定义和模态消融，因为真正可迁移的想法是怎样把探索预算分配给有用的信息。

## 研究关联

它提供了一个可借鉴的探索原则：先判断任务所需的信息主要来自哪个感觉通道，再决定奖励哪类不确定性。对以接触为核心的操作，触觉能给探索增加方向，避免把所有不可预测变化都当成同样有用。

### 下一步读哪里

先核查触觉传感器及不确定性公式，再看与整体不确定性探索在相同交互预算下的比较。重点问：更多接触是否带来更高任务成功率，以及 VLA 后训练和执行分别需要哪些输入。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：40
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/Tactile Curiosity Drives Robot Interaction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.40134v1 Announce Type: new Abstract: Mastering robot manipulation skills via reinforcement learning (RL) remains largely sample-inefficient. The most common RL algorithms rely on random action sampling to discover new strategies, resulting in agents that allocate most of their training budget to motions in free space, away from the contacts from which manipulation skills emerge. Existing intrinsic motivation methods based on model disagreement or epistemic uncertainty improve on isotropic noise, but they can also reward uncertainty in functionally irrelevant transitions, such as erratic motions in free space. In this work, we argue that tactile feedback provides a natural signal for exploration, and introduce TacEx, a framework that incorporates touch into epistemic uncertainty-driven exploration by decomposing model uncertainty across sensory modalities and directing curiosity toward the tactile channel. By anchoring curiosity to the sense of touch, TacEx drives the robot to discover complex contact dynamics, learning to manipulate and grasp objects without task rewards or expert demonstrations during exploration. The interaction-dense dataset collected through this tactile-driven curiosity supports offline learning of downstream pick-and-place policies without additional environment interaction. We further use tactile-driven exploration to post-train vision-language-action (VLA) models. Although the VLAs are initially pre-trained without tactile feedback, post-training with TacEx substantially improves downstream performance while remaining highly sample-efficient.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.40134
- Authors: Klemens Iten, Alexander Proshkin, Bhavya Sukhija, Stelian Coros, Andreas Krause, Pieter Abbeel, Carmelo Sferrazza
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
