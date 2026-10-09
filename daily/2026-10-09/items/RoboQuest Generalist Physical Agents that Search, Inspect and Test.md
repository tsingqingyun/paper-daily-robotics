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
url: "https://arxiv.org/abs/2610.10388v1"
published: "2026-10-07T16:46:45Z"
age_days: 1
score: 34
created: 2026-10-09
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RoboQuest: Generalist Physical Agents that Search, Inspect and Test

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboQuest 检验机器人能否为了完成任务，主动找东西、检查隐藏属性、试用陌生工具，并根据证据调整行动。它揭示的瓶颈是：会执行动作，还不代表知道何时该继续探索。

## 问题

任务是在陌生环境中完成移动操作，而关键事实可能不在初始观察里。机器人必须通过身体交互获取信息，才能决定下一步。普通操作能力无法解决“物品在哪里”“未观察的属性是什么”“工具有什么效果”这些问题；摘要把这种缺信息的情形作为基准核心。

### 用一个例子理解

理解用例（非论文实验）：输入“把装有螺丝的盒子放到工作台”；机器人先搜索盒子，打开检查内容，根据观察排除空盒，再搬运正确盒子。输出不仅是搬运动作，还包括支持选盒决定的观察证据。

## 创新点或方法

本文主要贡献是评测设计。它把任务组织成搜索、操作式检查和交互测试三类不确定性，让模型自行取证、调整动作并决定何时完成任务。评测侧让五个前沿多模态智能体使用共同视觉动作接口；训练侧另将 π₀.₅ 用完整回合示范微调。还在提供隐藏信息后单独测执行技能，用来区分取证决策与动作执行的困难。接口、提示和微调配置未说明。

### 方法如何工作

1. 接收目标与初始观察，识别完成任务还缺哪些信息，决定探索方向。
2. 通过搜索、操作检查或测试取得新观察，补上原来不可见的事实。
3. 根据所得证据调整行动，并处理探索可能造成的环境扰动。
4. 判断证据是否足够，再提交任务完成；基准用最终结果和失败分析检验这一决策。

### 必要术语

- 具身探索：通过移动和操作获取信息；本文要求探索服务于具体目标。
- 操作式检查：动手后才能看清属性；本文用它测试隐藏信息获取。
- 交互测试：试用物品以发现效果；本文测试智能体能否据反馈调整行动。

## 证据

摘要给出十项移动操作任务，最佳智能体仅成功 23% 的回合，微调策略几乎不成功。提供隐藏信息后的独立技能测试显示，智能体能完成大多数所需动作；失败分析认为执行只占少数失败，常见问题是证据不足就停止探索，以及很少预防或修复探索造成的扰动。摘要未给模型名单、回合数、分项成绩或统计不确定性，也未明确运行平台。

## 局限

隐藏信息已知时技能表现较好，支持探索决策是重要瓶颈，但尚不能把所有剩余失败归因于某一种推理缺陷。微调策略的结果也不能推广成示范学习普遍无效；我会核查示范量、训练设置和任务分布。

- **判断**：优先读任务完成条件和失败案例，因为这篇最有用的地方是教我们怎样测出“会动但不会取证”。

## 研究关联

可借鉴的是把任务完成条件写成需要观察到的证据，再评估智能体是否真的取得证据。这样能区分“动作做不了”和“还没弄清楚就行动”，避免只增加操作训练，却没有针对信息获取的决策问题。

### 下一步读哪里

检查每项任务必须取得哪些证据、如何判定提前停止，以及独立技能测试与完整任务的动作条件是否一致；再核查扰动修复、试错学习的具体失败统计和实验环境。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/RoboQuest Generalist Physical Agents that Search, Inspect and Test.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advances in multimodal foundation models have made them capable generalist physical agents for a range of manipulation tasks. However, successful operation in an unfamiliar environment may require an agent to seek task-relevant information through interaction when it is absent from the observations: it may need to determine where a relevant object is, inspect an unobserved property, or discover the effect of an unfamiliar tool. We thus introduce RoboQuest, a benchmark for goal-directed embodied exploration, where agents must actively acquire task-relevant information through physical interaction, use the resulting evidence to adapt subsequent actions, and autonomously decide when to commit to task completion. RoboQuest comprises ten mobile manipulation tasks centered on three forms of uncertainty: search, manipulation-based inspection, and interactive testing. We evaluate five frontier multimodal agents through a common visuomotor interface, as well as a $π_{0.5}$ policy fine-tuned on the full-episode demonstrations we release. The best agent succeeds in only 23\% of the episodes, and the fine-tuned policy almost never succeeds. Isolated tests of the execution skills the tasks are built from, with the hidden information supplied, show that the agents can carry out most of the required actions, and our failure analysis attributes only a minority of the failures to execution. Our failure analysis further finds that the agents often stop exploring too early as they make decisions before observing the required evidence for task completion. We also find that agents rarely prevent or repair the disturbances caused by their exploration. Moreover, learning by trial and error remains difficult for most models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10388v1
- Authors: Liu Renhang, Navonil Majumder, Tej Deep Pala, Soujanya Poria
- Published: 2026-10-07T16:46:45Z
- Age days: 1

</details>
