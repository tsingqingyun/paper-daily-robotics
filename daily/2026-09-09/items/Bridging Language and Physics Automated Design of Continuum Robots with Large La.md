---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08220v1"
published: "2026-09-08T04:02:59Z"
age_days: 1
score: 31
created: 2026-09-09
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Bridging Language and Physics: Automated Design of Continuum Robots with Large Language Models

> [!summary] 先说人话（基于摘要）
> AID-SR让LLM设计连续体机器人后，接收仿真中的物理反馈并反复修改。它显著提高设计通过可行性检查的比例，但真正完成任务的比例仍低得多。

## 问题

从高层需求自动生成连续体机器人时，语言推理难以预见复杂物理交互的后果，容易给出物理有效性不足的设计。

## 创新点或方法

将仿真器观察到的物理状态转成结构化反馈，结合语义批评、人类反馈和迭代修订，形成设计闭环；对生成的腱驱动连续体机器人采用共同强化学习训练方案检验任务能力。

## 证据

在涵盖到达、抓取、运动和操作的14任务基准上，96.2%的设计通过仿真可行性检查，26.7%的机器人经共同强化学习训练后完成相应任务；制造出的3台机器人成功完成真实任务。


## 局限

需核查人类反馈的介入程度及3台实体机器人的选择方式；96.2%的可行率不能当作任务成功率。

- **判断**：值得精读反馈协议与失败设计，26.7%的任务成功率比高可行率更能揭示当前瓶颈。

## 研究关联

对机器人学习与设计评测有直接价值，尤其清楚区分了物理可行性和功能成功。与世界模型的关联在于物理反馈闭环，摘要未描述学习式世界模型。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/Bridging Language and Physics Automated Design of Continuum Robots with Large La.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large language models (LLMs) have recently emerged as a promising tool for automating robot design from high-level specifications, yet they remain ineffective for robots operating under complex physical interactions. This limitation stems from the gap between language-based reasoning and the physical consequences of embodiment, often resulting in designs with low physical validity. In this work, we propose a multi-layered framework, AID-SR, that establishes a closed loop by translating simulator-observed physical states into structured feedback for the LLM designer. Combined with semantic critique, human feedback, and iterative refinement, the framework promotes the generation of physically feasible and functionally meaningful robot designs. We evaluate our approach on tendon-driven continuum robots across a benchmark of 14 tasks spanning reaching, grasping, locomotion, and manipulation. The proposed framework achieves 96.2% rate for passing the simulation feasibility check and by applying a common reinforcement learning training, 26.7% robots can successfully fulfill the corresponding task. We then fabricate three designed robots of AID-SR that successfully complete the task in real-world. These extensive experiments across simulation and real-world environments demonstrate and break the wall of utilizing the LLMs for automated design of continuum robots. The source code and experimental resources are publicly available at https://github.com/UNITES-Lab/AID-SR.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08220v1
- Authors: Jingyi Chen, Mohan Zhang, Laura Yao, Yingtai Ni, Jianmin Ji, Jie Peng, Song Wang, Tianlong Chen
- Published: 2026-09-08T04:02:59Z
- Age days: 1

</details>
