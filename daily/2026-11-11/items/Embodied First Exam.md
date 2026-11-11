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
url: "https://arxiv.org/abs/2611.12177v1"
published: "2026-11-09T10:29:19Z"
age_days: 1
score: 37
created: 2026-11-11
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Embodied First Exam

> [!summary] 这篇论文到底做了什么（基于摘要）
> Embodied First Exam 要检查的是：会写代码的智能体，能否在机器人持续行动、信息有限、不能随意重来的条件下完成任务。它允许智能体自己选择直接控制、写控制代码或训练策略，再通过不同权限和时间条件检验能力。

## 问题

已有基准主要围绕视觉到动作的策略学习，难以回答编码智能体能否驾驭不同机器人。真正的瓶颈不只是动作是否正确，还包括智能体能否根据传感器理解局面、选对控制方式，并在失败难以撤销的过程中继续推进任务。

### 用一个例子理解

理解用例（非论文实验）：输入相机画面和“把积木放进窄槽”的任务，智能体选择写控制代码，根据新观察调整动作，最终输出机器人执行的运动。若积木滑落，标准设置下不能靠重置抹掉这次失误。

## 创新点或方法

旧评测以学习控制策略为中心；这里把控制路径的选择也交给智能体。标准设置只提供传感器观察，默认不能重置；实时变体让环境在智能体思考时继续运行；特权设置则开放完整仿真状态和无限重置，允许搜索可行解。训练策略只是可选路径，特权解也可服务训练；摘要未说明各智能体具体如何训练、如何分配计算预算。

### 方法如何工作

1. 把任务和传感器观察交给智能体，让它从有限信息形成控制判断。
2. 智能体选择直接控制、写代码或训练策略，得到可执行动作；摘要未展开具体接口。
3. 按设置限制状态访问和重置机会，使同一任务暴露不同执行约束。
4. 记录成败并标注失败发生阶段，用于比较不同智能体的失误位置。

### 必要术语

- 编码智能体：能通过编写和调用代码执行任务的模型系统；这里由它决定控制路径。
- 特权状态：仿真器内部的完整状态信息；这里用于降低观察难度并搜索可行解。
- 实时评测：模型思考时环境仍继续变化；这里检验决策延迟的影响。

## 证据

摘要给出总规模为 1,156 个任务、35 个套件、47 种机器人，其中 9 个新套件覆盖空间谜题、灵巧操作、多机器人交互等。八个智能体在 456 个核心任务上比较，最强的 GPT-6 Astra in Codex 在标准设置成功率为 34%。这说明该设置仍有大量未完成任务，不能外推为全部任务或真机成功率；摘要未给其他模型成绩及实时设置差距。

## 局限

特权设置成绩只是作者所说的近似上界，不是数学上界。摘要未交代真机覆盖范围，也未给失败阶段的具体分布，因此还不能判断主要瓶颈来自感知、规划还是执行。

- **判断**：值得读到评测协议和失败分析：它最有用的部分，是把“机器人控制成功”拆成可检查的条件，而单个总成功率解释不了这些差异。

## 研究关联

值得借鉴的是把信息权限、重试机会和思考耗时作为评测条件。若只在可反复重置的环境中测成功率，很难判断控制方法能否承受一次实际执行的约束。

### 下一步读哪里

先核查三种设置的时间与调用预算是否可比，再看核心任务如何选取、成功如何判定，以及失败阶段标注能否稳定区分感知错误和控制错误。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-11/Embodied First Exam.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. We therefore introduce the Embodied First Exam, a unified, comprehensive, and agent-native evaluation framework where coding agents can choose their own control approach: direct control, code to control, or train a policy to control. We hope it serves as a first exam for coding agents before they enter the physical world, with 1,156 tasks in 35 suites on 47 robots, including 9 new suites that go beyond pick-and-place to spatial puzzles, dexterous manipulation, multi-robot interaction, dynamic whole-body control, and sim-to-sim engineering. Each task can be run in up to three evaluation settings. The Standard Setting mimics the real world: the agent receives only sensor observations and, by default, cannot reset the environment. Its Realtime variant keeps the environment running while the agent reasons. The Privileged Setting gives the agent access to the full simulator state and unlimited resets, allowing it to search for an oracle solution for training purposes. Success rates in this setting serve as an approximate upper bound. On the 456 core tasks, the strongest of eight agents, GPT-6 Astra in Codex, achieves a success rate of 34% in the Standard Setting, leaving much room for improvement. To see where agents fail, we label the stage at which failed attempts go wrong and compare failures across agents, settings, and stage categories.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.12177v1
- Authors: Kangrui Wang, Qineng Wang, Changhe Chen, Pingyue Zhang, Chi Gui, Feishi Wang, Canyu Chen, Wenli Xiao, Xiaoyu Huang, Tonghe Zhang, Linjie Li, Zihan Wang, Minyeong Kim, Yiyou Sun, Mingkai Deng, Jinyu Hou, Qi Zhu, Han Liu, Eric P. Xing, Huaxiu Yao, Zhiwen Fan, Yuejiang Liu, Dawn Song, Pieter Abbeel, Li Fei-Fei, Jiajun Wu, Yuke Zhu, Guanya Shi, Ruohan Zhang, Manling Li
- Published: 2026-11-09T10:29:19Z
- Age days: 1

</details>
