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
url: "https://arxiv.org/abs/2610.19155"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 41
created: 2026-10-16
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# FACT: A Multimodal Force-Action-Track Foundation Model for Human-to-Robot Dexterity

> [!summary] 这篇论文到底做了什么（基于摘要）
> FACT 先预测动作和接下来会看到的运动，再根据预计接触力细化动作。它配合含力信息的人类示范数据 EgoForce，试图让机器人从人类操作中同时学到“怎么动”和“该用多大力”。

## 问题

任务是需要精细协调和接触控制的灵巧操作。人类示范容易扩大规模，但多数数据没有力测量；只看动作和画面，难以学会接触时的力度变化。因此，人类数据再多，也未必能补上机器人精细操作所需的力信息。

### 用一个例子理解

理解用例（非论文实验）：输入将细管插入支架的观察信息和任务要求；粗规划预测移动动作、未来画面及管子的轨迹，细化器结合预计接触力调整动作，输出更细致的插入方案。该例不代表已验证的实验。

## 创新点或方法

相比主要从视觉和动作学习，本文先用 EgoForce 与机器人示范共同预训练，再用人机数据微调。FACT 的两个部分联合训练：Track-Guided Coarse Planner 同时预测动作、未来视频和视觉轨迹，用未来视觉变化联系不同身体的操作；Force-Action Joint Refiner 接着联合预测未来力并细化粗动作，让二者相互约束。执行时按粗规划到细化的顺序生成动作；是否实时输入力反馈、如何执行动作片段，摘要未说明。

### 方法如何工作

1. 以含力的人类数据和机器人示范共同预训练，为视觉、动作与接触建立联系。
2. 粗规划器联合预测动作、未来视频和轨迹，得到可跨身体共享的任务变化描述。
3. 细化器在粗计划上预测未来力并修正动作，使预期接触参与动作生成。
4. 用人机示范微调到目标操作，再按两级流程生成动作；具体网络及执行频率摘要未说明。

### 必要术语

- 视觉轨迹：画面中目标随时间移动的路径；本文用来辅助规划与跨身体迁移。
- 跨身体迁移：把人类操作经验用于机器人等不同身体；本文借助未来视觉变化建立联系。
- 力监督：训练时提供实际力信息；用于学习接触与动作之间的关系。

## 证据

摘要报告十项任务，涉及工具、乐器和精密实验操作。在少至 10 条机器人轨迹配合 90 条人类轨迹微调时，FACT 优于两个基线，相比 T-Rex 的成功率增幅最高达 60 个百分点；这不是十项平均增幅。消融支持人类预训练力监督、视觉轨迹预测及未来力预测有帮助。摘要未列另一基线名称、逐任务成功率或重复实验波动，也未明确各实验的真机与仿真配置。

## 局限

人机数据比例实验只“提示”人类示范的学习效果接近机器人示范，不能推出任意任务上二者可等量替换。待核查的是人类力测量如何对应机器人接触、传感配置及失败类型；摘要没有足够信息判断这种迁移的条件。

- **判断**：值得深入读两级预测的耦合方式和力监督消融，因为关键问题是力信息是否真正改变动作生成。

## 研究关联

这里值得借鉴的是跨身体迁移时共享什么信息：人的关节动作不一定适合机器人，但物体怎样移动、接触力如何变化，更可能成为共同学习目标。需要细致接触控制时，采集这些信息可能比只增加普通视频更有针对性。

### 下一步读哪里

先查两个组件怎样联合训练、力和动作怎样相互影响，再看十任务逐项结果与数据比例实验；尤其核查推理是否需要力传感器，以及 60 个百分点对应什么任务和数据配置。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：41
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/FACT A Multimodal Force-Action-Track Foundation Model for Human-to-Robot Dexteri.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.19155v1 Announce Type: new Abstract: Human demonstrations offer a scalable alternative to costly robot data collection for dexterous manipulation, but most human datasets lack force measurements. Dexterous manipulation requires not only visual and proprioceptive understanding but also the ability to anticipate and regulate interaction forces. To scale force-aware human-robot co-training, we introduce EgoForce, a large-scale human tactile dataset capturing force-rich manipulation experience, and combine it with robot demonstrations for pretraining. We present FACT, a robot foundation model that cascades from prospective visual planning to force-aware refinement for dexterous manipulation. FACT comprises two jointly trained components. A Track-Guided Coarse Planner jointly predicts actions, future video, and visual tracks. Future video and visual tracks also provide a shared task representation that facilitates cross-embodiment knowledge transfer and coarse action generation. Building on this coarse plan, a Force-Action Joint Refiner jointly predicts future force and refines the coarse action, allowing anticipated force and action to shape each other during refinement. We evaluate the model on ten tasks requiring fine-grained coordination and force feedback, including tool use, musical instruments, and precision laboratory procedures. Using as few as 10 robot trajectories with 90 human trajectories for fine-tuning, FACT outperforms both baselines, with success-rate gains of up to 60 percentage points over T-Rex. Ablations show that force supervision in human pretraining data is crucial for downstream robot performance after fine-tuning, while visual track prediction and training with future-force prediction improve dexterous execution. Experiments varying the human-robot data ratio during fine-tuning further suggest that FACT learns from human demonstrations nearly as effectively as from robot demonstrations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.19155
- Authors: Zhi Cao, Yining Hong, Jiaolong Yang, Yejin Choi, Li Fei-Fei, Jiajun Wu, Huang Huang
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
