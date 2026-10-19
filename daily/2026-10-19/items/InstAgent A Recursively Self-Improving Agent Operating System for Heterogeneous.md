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
url: "https://arxiv.org/abs/2610.23098v1"
published: "2026-10-16T08:10:51Z"
age_days: 3
score: 31
created: 2026-10-19
concepts: ["多模态基础模型", "智能体 Agent"]
---

# InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration

> [!summary] 这篇论文到底做了什么（基于摘要）
> InstAgent 让不同机器人按一份明确写出分工、依赖和交接检查的协作程序工作，并把执行中修好的程序保留下来。关键是让纠错成为下次能直接用的经验，而不只是当次对话里的临时提醒。

## 问题

任务是让能力互补的机器人完成长流程协作。真正难点在交接：前一台做完了什么、后一台需要什么条件、现场情况是否仍然成立。摘要指出，现有系统难以保留执行纠错、跨时空维持任务上下文，也缺少对机器人间依赖的明确表达。

### 用一个例子理解

理解用例（非论文实验）：输入“把仓库货箱送到工作台”。移动机器人运箱，机械臂等待箱子到位且可抓取；共享记忆记录位置与状态。若一次交接因停靠偏差失败，系统修订停靠或检查步骤，最终输出完成搬运的协作程序及可复用修订。

## 创新点或方法

从临时安排动作、纠错后经验难以留下，改为用 agentic 行为树组织协作：把能力分配、先后依赖和交接检查写进程序。执行反馈触发 RSI 修改，成功修订保存供未来复用；共享多模态时空记忆给规划和交接提供上下文。这里明确的是运行时程序更新，摘要未说明是否另有模型训练，也未说明修订如何验收、何时调用旧版本。

### 方法如何工作

1. 把任务对应到各机器人的能力，形成行为树中的分工，让后续执行有明确责任。
2. 写出动作间依赖和交接检查，得到可判定的启动条件，避免后一台过早行动。
3. 读取共享时空记忆并执行程序，用现场上下文判断交接是否成立。
4. 根据执行反馈修改协作程序，保存成功版本供未来复用；摘要只说明到此，未交代修订算法。

### 必要术语

- 行为树：按条件组织动作执行的程序结构；本文用它表达团队分工和协作依赖。
- RSI：递归自我改进；本文指根据执行反馈修订协作程序并保留成功版本。
- 时空记忆：把观察与时间、位置联系起来的记录；本文用它支持规划和交接判断。

## 证据

摘要报告在 20 个真实世界多机器人任务、三个高层模型上，任务成功率、首次完成率和执行效率均有一致收益。但未给任务清单、对比系统、具体数值、重复次数及效率定义。因此能支持它在所测真机协作中有效，尚不能判断收益幅度或哪个组件贡献最大。

## 局限

待核查的是：旧修订遇到场景变化会不会误用，以及共享记忆怎样处理过时或互相矛盾的观察。输入没有这些细节，不能据此认定作者未做检查。三种高层模型上的一致收益也不足以单独证明 RSI 的因果作用。

- **判断**：值得读到程序修订与交接验证的实现细节，因为它是否真正积累经验，取决于修订如何被确认、保存和再次调用。

## 研究关联

值得借鉴的是把“交接条件”做成可检查的程序内容。长流程系统若反复在相同衔接处失败，保存一条经过执行验证的修订，可能比每次重新提示模型更有用；前提是能判断修订适用于哪些新情境。

### 下一步读哪里

先核查行为树如何表达等待与失败恢复，再看成功修订的验收、适用范围和版本选择；实验中重点找去掉 RSI、共享记忆及交接检查后的比较，以及首次完成率如何统计。

- **概念**：多模态基础模型 智能体 Agent
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/InstAgent A Recursively Self-Improving Agent Operating System for Heterogeneous.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Heterogeneous robot teams enable complex, long-horizon tasks by combining complementary sensing, mobility, and manipulation capabilities across multiple embodiments. Yet existing systems struggle to retain execution-time corrections as reusable experience, maintain task-relevant context memory across space and time for reliable handoffs, and explicitly represent the inter-robot dependencies required for structured collaboration. In order to address these challenges, we present InstAgent, a recursively self-improving (RSI) Agent Operating System for heterogeneous robot collaboration. InstAgent organizes team behaviors as agentic behavior trees (BTs) that explicitly model capability assignment, inter-robot dependencies and handoff checks. The RSI mechanism updates these collaboration programs from execution feedback and preserves successful revisions for reuse in future tasks, while shared multimodal spatio-temporal memory provides context for planning and handoff validation. Experiments on 20 real-world multi-robot tasks with three high-level models show consistent gains in task success, first-attempt completion, and execution efficiency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23098v1
- Authors: Haoyang Luo, Junhao Qin, Jingyan Cao, Yi Huang, Guangjie Yang, Xiaoyu Chen, Haotao Lu, Tianxiang Gui, Ye Shi, Jingya Wang
- Published: 2026-10-16T08:10:51Z
- Age days: 3

</details>
