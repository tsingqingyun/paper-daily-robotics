---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30913v1"
published: "2026-09-25T07:25:19Z"
age_days: 3
score: 29
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

> [!summary] 先说人话（基于摘要）
> Causeway 处理 VLA 换指令后“会做新任务，却回不到能开始的位置”的问题。它直接干预冻结模型的动作内部表示，让模型自己生成返回目标任务入口的运动。

## 问题

从标准初始状态能完成的任务，在前一任务改变物理状态后可能无法启动。摘要将这些状态称为 task islands，说明多任务能力不自动等于中途切换任务的能力。

## 创新点或方法

给定当前状态与目标任务的重入位姿，Causeway 通过冻结解码计算反向传播，在动作流表示中进行状态定向写入。无需训练、更新参数、新增动作头或外部生成动作。

## 证据

在 LIBERO-Goal 的 71 个跨物体配对、三个切换时机和三种 VLA 架构上，直接切换成功率 3–26% 提升至 47–65%，到达交接邻域的比例提高 42–72 个百分点。另有 LIBERO-Object 和真实 xArm 实验支持扩展性。

## 局限

方法需要目标任务的重入位姿，需核查其来源和适用条件；到达入口与完成任务是两个指标，不能混为一谈。

- **判断**：值得精读问题定义、重入位姿设定和干预机制，适合研究多任务连续执行的人。

## 研究关联

对 VLA 研究者，它提出了比标准初始状态成功率更接近连续使用的评测问题，并给出通过内部表示恢复任务可达性的推理期干预。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/Causeway Restoring Task Accessibility for Instruction Switching in VLA Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies can execute many tasks from standard initial states, yet a new instruction may fail after another task has altered the robot's physical state. We study instruction switching, where a new task is issued during or after the execution of a different one. We observe that a target task that is reliably completed from its standard initial states can become inaccessible from states produced by a preceding task. We call such states task islands. We propose Causeway, a training-free inference-time intervention. Given the current state and a re-entry pose for the target task, Causeway back-propagates through the frozen decoding computation and applies a state-directed write within the action-stream representation. The VLA decodes the return motion itself, without parameter updates, a new action head, or external action generation. Across 71 cross-object pairs, three switch timings, and three VLA architectures on LIBERO-Goal, Causeway raises bare-switch success from 3-26% to 47-65% and increases the rate of reaching the handoff neighborhood by 42-72 percentage points across models. Additional experiments on LIBERO-Object and a real xArm platform show that the recovery extends beyond the main LIBERO-Goal setting, both in simulation and on a robot.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30913v1
- Authors: Qingzi Wang, Kaixi Feng, Guangyao Shi, Xiyang Wu, Ang Li, Dinesh Manocha
- Published: 2026-09-25T07:25:19Z
- Age days: 3

</details>
