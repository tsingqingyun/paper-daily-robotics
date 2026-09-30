---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2512.24497"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 33
created: 2026-09-04
concepts: ["智能体 Agent", "世界模型"]
---

# What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

> [!summary] 先说人话（基于摘要）
> 论文系统拆解联合嵌入预测世界模型（JEPA-WM）为何能用于物理规划，比较架构、训练目标和规划算法，并把有效选择组合成一个优于DINO-WM与V-JEPA-2-AC的方案。

## 这篇到底在做什么

- **卡在哪里**：潜空间规划被认为能过滤无关细节、提高效率，但具体成功往往由多个技术选择共同决定，现有研究缺少对模型结构、目标函数和规划器的统一比较。
- **关键解法**：先从状态—动作轨迹训练联合嵌入预测世界模型，再让规划器在学习到的表示空间中优化动作；研究在仿真环境与真实机器人数据上逐项改变架构、训练目标及规划算法，并组合最佳组件。关键差异是系统辨析整类方法，而非只推出单个模型。
- **拿什么证明**：组合模型在导航和操作任务上均超过DINO-WM与V-JEPA-2-AC。摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对世界模型和Agent研究者，这篇论文的实际价值在于提供潜空间规划的组件选择证据和公开代码、数据、检查点，可帮助避免把成功错误归因于某个单独模块。
- **先别急着信**：摘要没有说明各组件影响大小、任务范围或统计稳定性；“最优方法”应理解为其研究范围内的组合，不能外推为普遍最优。
- **判断**：值得精读实验矩阵和规划实现；它更像一篇技术选型指南，价值可能高于单看最终榜单提升。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/What Drives Success in Physical Planning with Joint-Embedding Predictive World M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2512.24497v4 Announce Type: replace-cross Abstract: A long-standing challenge in AI is to develop agents capable of solving a wide range of physical tasks and generalizing to new, unseen tasks and environments. A popular recent approach involves training a world model from state-action trajectories and subsequently use it with a planning algorithm to solve new tasks. Planning is commonly performed in the input space, but a recent family of methods has introduced planning algorithms that optimize in the learned representation space of the world model, with the promise that abstracting irrelevant details yields more efficient planning. In this work, we characterize models from this family as JEPA-WMs and investigate the technical choices that make algorithms from this class work. We propose a comprehensive study of several key components with the objective of finding the optimal approach within the family. We conducted experiments using both simulated environments and real-world robotic data, and studied how the model architecture, the training objective, and the planning algorithm affect planning success. We combine our findings to propose a model that outperforms two established baselines, DINO-WM and V-JEPA-2-AC, in both navigation and manipulation tasks. Code, data and checkpoints are available at https://github.com/facebookresearch/jepa-wms.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2512.24497
- Authors: Basile Terver, Tsung-Yen Yang, Jean Ponce, Adrien Bardes, Yann LeCun
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
