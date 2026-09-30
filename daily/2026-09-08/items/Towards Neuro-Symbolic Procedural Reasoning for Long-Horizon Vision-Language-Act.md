---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.05369"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 36
created: 2026-09-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# Towards Neuro-Symbolic Procedural Reasoning for Long-Horizon Vision-Language-Action Manipulation

> [!summary] 先说人话（基于摘要）
> 这项神经符号方法给 VLA 增加明确的任务步骤表和过程记忆，使它知道当前做到哪一步、下一步是否满足条件。示范中的视觉关注线索进一步帮助选择对象与目标位置。

## 问题

短技能执行能力不足以支撑长流程；机器人还需要持续记录状态、遵守依赖关系、处理条件分支并正确定位操作对象。

## 创新点或方法

任务图编码依赖、合法转移和分支，记忆保存当前步骤、已完成动作、文本与视觉证据，共同驱动子目标分派和状态核验；机器人视角视频上的伪凝视标注用于微调与推理。

## 证据

研究工作区清理和手术器械处理两个领域，列出对象选择、步骤顺序、完整任务成功等评测项；摘要未给出可核查的结果数字。


## 局限

初步研究绕过跨视角凝视迁移，直接人工标注伪凝视；需核查任务图来源，以及各模块实际贡献。

- **判断**：先读系统设计即可；是否值得深入复现，取决于全文能否证明结构化记忆与视觉指导的独立收益。

## 研究关联

为长时程 VLA 提供结构化状态管理方案，也为 Agent 研究者连接流程推理与底层控制提供参考。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/Towards Neuro-Symbolic Procedural Reasoning for Long-Horizon Vision-Language-Act.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.05369v1 Announce Type: new Abstract: Vision-language-action (VLA) models can execute short manipulation skills, but remain brittle in long-horizon procedures requiring persistent task state, dependency-aware reasoning, conditional decisions, and reliable grounding. We investigate a neuro-symbolic framework that combines learned VLA control with explicit task graphs and multimodal procedural memory. Task graphs encode action dependencies, valid transitions, and branch conditions, while memory maintains the active step, completed actions, textual context, and task-relevant visual evidence. Together, these structures guide object selection, destination grounding, subgoal dispatch, and verification of expected state transitions. Human demonstrations provide additional spatial and temporal guidance through gaze or saliency cues. To isolate their effect on policy learning, our initial study bypasses cross-view gaze transfer and directly annotates pseudo-gaze in robot-view teleoperation videos. The resulting guidance is used during VLA fine-tuning and inference. We study two long-horizon manipulation domains, workspace clearing and surgical-instrument handling, which require ordered execution, visually grounded decisions, and conditional branching. We evaluate correct-object and destination selection, subtask completion, task progress, step-order consistency, complete-task success, and procedural or execution mistakes. This work positions structured symbolic reasoning and demonstration-derived visual guidance as complementary mechanisms for reliable long-horizon VLA manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.05369
- Authors: Vivek Chavan, Yahuan Shi, Oliver Heimann, Kevin Haninger, J\"org Kr\"uger
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
