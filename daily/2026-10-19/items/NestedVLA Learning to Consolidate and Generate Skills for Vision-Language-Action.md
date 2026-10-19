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
url: "https://arxiv.org/abs/2610.23271v1"
published: "2026-10-16T10:42:29Z"
age_days: 3
score: 40
created: 2026-10-19
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> NestedVLA 想把分别学会的机器人技能装进同一个系统，又避免合并权重时互相破坏。它用任务条件驱动超网络，为当前任务生成动作专家参数，同时保留冻结的基础 VLA 和各任务压缩后的视觉语言残差。

## 问题

任务是整合来自不同任务、环境和平台的技能。一起训练会相互干扰；分别训练后直接合并参数，又可能发生权重冲突，或需要改架构。真正瓶颈是：怎样共享已有能力，同时保住每个任务的专门适配。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“打开抽屉”任务；系统据此生成开抽屉所需的动作专家参数，再结合基础 VLA 输出动作。换成“按按钮”时，生成对应参数，而不是让两套专家权重直接取平均。

## 创新点或方法

旧做法把多个模型的参数揉在一起；本文改为学习“给定任务，该生成怎样的动作专家”。训练上先独立学习技能，再事后整合；嵌套超网络具体如何训练、用什么损失，摘要未说明。推理时，超网络按目标任务合成动作专家参数，与冻结基础 VLA 配合；任务专属的压缩 VLM 残差单独保留。巧处是把共享集中在参数生成器里，减少不同任务直接争用同一套专家权重。

### 方法如何工作

1. 先独立学习各任务技能，获得任务适配，避免联合训练阶段的任务干扰。
2. 再用任务条件训练参数生成器，学习如何合成相应动作专家；摘要只说明到此，未交代监督方式。
3. 部署时选择目标任务，生成专家参数并配合冻结基础模型，保留该任务的专门能力。
4. 单独保留任务压缩 VLM 残差，承接视觉语言侧的适配；其具体接入方式未说明。

### 必要术语

- 超网络：输出另一个网络参数的网络；本文用它按任务生成动作专家。
- 冻结基础 VLA：整合时不更新的视觉语言动作模型；提供共同底座。
- VLM 残差：任务适配相对基础视觉语言模型的改变量；本文压缩后按任务保留。

## 证据

摘要报告在 MetaWorld、ManiSkill、CALVIN 三个 RL 基准上，相比最强模型合并基线平均高 41 个百分点；在 ManiSkill 上与逐任务微调相差不超过 1 个百分点，并缩小了 CALVIN 上的差距。摘要未给出具体指标定义、基线名称、逐项成绩和存储量；这些结果支持所测基准上的技能整合优势，不能据此认定真机、未见任务或跨平台迁移已解决。

## 局限

我会核查任务条件是否必须明确给出，以及新任务加入时是否需要重训生成器。摘要没有提供这些信息，也没有量化存储节省，不能把“高效存储路线”当成已充分证明的部署收益。

- **判断**：值得读方法和存储对照实验：关键在于它是否以较小的共享生成器，保住了独立专家的能力。

## 研究关联

值得借鉴的是：整合技能不必等于平均权重。如果已有许多独立训练的任务专家，可以尝试学习它们随任务变化的参数规律；是否划算，要把生成器和全部任务残差的存储一起算。

### 下一步读哪里

先核查嵌套超网络的输入、输出和训练目标，再看逐任务微调与合并基线是否使用相同数据和基础模型；最后检查总存储量、参数生成耗时及新增技能的代价。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/NestedVLA Learning to Consolidate and Generate Skills for Vision-Language-Action.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, joint multi-task training suffers from interference, and model merging tends to introduce parameter conflicts or require architectural changes. We instead advocate a paradigm in which skills are first learned independently and then consolidated post hoc. To this end, we propose NestedVLA, which replaces parameter aggregation with parameter generation: a nested hypernetwork, conditioned on the target task, synthesizes task-adaptive action-expert parameters that compose with a frozen base VLA. Task-specific compressed VLM residuals are retained separately. This formulation enables flexible task-conditioned skill reuse while mitigating interference. Across three RL benchmarks (MetaWorld, ManiSkill, CALVIN), NestedVLA outperforms the strongest model-merging baseline by 41 pp on average, matches per-task fine-tuning within 1 pp on ManiSkill, and substantially closes the gap on CALVIN, pointing toward a storage-efficient route to skill consolidation. Code is available at https://github.com/WanyuGroup/NeurIPS2026-NestedVLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23271v1
- Authors: Guodong Du, Wanyu Lin
- Published: 2026-10-16T10:42:29Z
- Age days: 3

</details>
