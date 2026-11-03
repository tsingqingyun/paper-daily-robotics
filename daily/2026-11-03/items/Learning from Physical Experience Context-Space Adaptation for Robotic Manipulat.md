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
url: "https://arxiv.org/abs/2610.41320v1"
published: "2026-10-30T06:32:51Z"
age_days: 3
score: 31
created: 2026-11-03
concepts: ["多模态基础模型", "智能体 Agent"]
---

# Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> LEXP 让机器人把做过的事转化成下次行动可用的经验：解释执行证据，提炼带适用条件的教训，再把相关教训送回行动上下文。它固定模型权重和动作接口，通过改变模型接下来看到的信息来适应任务。

## 问题

多模态模型会感知和推理，并不自动意味着能可靠完成物理操作。本文针对的是执行中的纠错与跨回合复用：普通模型容易无法持续推进任务，而只保留记忆也未充分解决如何从经历中提取行动指导的问题。

### 用一个例子理解

理解用例（非论文实验）：输入“取出抽屉里的物品”和当前观察；机器人发现拉动后抽屉未打开，经验模块记录“遇到此类状态先检查是否受阻”；后续匹配到同类情形时加入检查反馈，模型据此输出下一步检查或操作指令。

## 创新点或方法

从直接调用通用推理模型，改为加入任务规划和经验模块。规划负责组织任务进程；经验模块解释执行证据，保留教训及其适用条件，后续选取相关经验形成反馈。这样过去的失败或检查策略可以影响下一次动作。这里的“学习”发生在交互时的上下文中，没有权重训练；证据格式、经验检索及动作接口细节未说明。

### 方法如何工作

1. 任务级规划组织操作进程，为后续动作提供当前目标。
2. 模型经固定动作接口执行，获得物理交互证据，使系统能够判断执行情况。
3. 经验模块解释证据并提炼带适用条件的教训，将具体经历整理成可复用指导。
4. 后续行动前调用相关教训生成上下文反馈，帮助模型推进或纠正动作；摘要未说明具体检索算法。

### 必要术语

- 上下文空间适应：通过改变模型读到的信息来改变行为；本文不更新模型权重。
- 适用条件：一条经验在什么情形下才该使用；用于约束经验复用。
- 任务级规划：组织完成任务所需的阶段；在本文中与经验反馈共同支持行动。

## 证据

摘要报告 12 项真实操作任务：LEXP 成功 23/36 次，63.9%；仅记忆为 19/36，52.8%；原始 Astra 为 2/36，5.6%。在面包转移、垃圾与洗漱用品分类、抽屉取物三项任务中，完整配置为 7/9，去规划为 4/9，去保留经验为 3/9。轨迹展示了反馈纠错和跨回合检查策略复用。这些支持所测任务上的组合效果，但试次数较少，轨迹案例也不能说明机制出现的普遍频率。

## 局限

摘要没有明确列出作者承认的局限。我的待核查问题是各配置是否获得相同观察和交互预算，经验是否在评测任务间共享，以及错误教训怎样被纠正。这里确有真机证据，但不能据此推断换机器人或动作接口仍有效。

- **判断**：值得读经验条目的实际内容和完整执行轨迹，因为关键不只是有记忆，而是经验如何被提炼、匹配并改变下一步动作。

## 研究关联

可借鉴的是经验的存储单位：保留“什么情况下该怎样做”，比单纯积累历史更接近下一次行动需要的信息。当动作接口已经可用、主要困难是任务推进和错误修正时，这种做法值得尝试。

### 下一步读哪里

先核查教训及适用条件的生成、保存、检索格式，再看原始模型、仅记忆和完整系统的预算是否一致。还应检查失败轨迹、经验污染处理，以及跨回合复用是否包含真正不同的初始条件。

- **概念**：多模态基础模型 智能体 Agent
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/Learning from Physical Experience Context-Space Adaptation for Robotic Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent multimodal foundation models exhibit strong perception, reasoning, and in-context learning capabilities, but translating these capabilities into physical action remains challenging. Through real-world experiments across diverse manipulation tasks, we find that ChatGPT-6-Astra, a state-of-the-art general-purpose reasoner, can serve as a physically actionable, context-responsive manipulation policy, demonstrating effective fine manipulation and spatial reasoning. Building on these findings, we introduce LEXP, a harness for learning from physical experience through context-space adaptation. LEXP combines task-level planning with an experience module that interprets execution evidence, extracts and retains lessons with applicability conditions, and reuses relevant lessons to generate contextual feedback for subsequent actions. Model weights and the action interface remain fixed throughout. Across 12 real-world manipulation tasks, LEXP achieves $23/36$ successful trials (63.9\%), compared with $19/36$ (52.8\%) with memory alone and $2/36$ (5.6\%) for vanilla Astra. On three tasks, bread transfer, sort trash and toiletries, and retrieve drawer, removing planning reduces success from $7/9$ to $4/9$, while removing retained experience reduces it to $3/9$. Execution traces illustrate feedback-guided corrections and cross-episode reuse of an inspection strategy. Execution analyses illustrate how task structure and experience-derived feedback guide task progression, action correction, and experience reuse. These results support context-space adaptation as a practical mechanism for turning physical interaction into reusable guidance for robotic manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.41320v1
- Authors: Yihan Zeng, Yisu Li, Kaixin Huang, Marc WuDunn, Amelia Kovacs, Mikael Harseno, Kimmy Lin, Porter Hunley, Fred Shentu, Philipp Wu, Zhongyu Li, Zike Yan
- Published: 2026-10-30T06:32:51Z
- Age days: 3

</details>
