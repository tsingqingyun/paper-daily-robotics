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
url: "https://arxiv.org/abs/2611.34280v1"
published: "2026-11-25T12:36:42Z"
age_days: 1
score: 28
created: 2026-11-27
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Escapingthe instruction blackhole of vision-language-action policies via optimal-transport wormholes

> [!summary] 这篇论文到底做了什么（基于摘要）
> Wormhole 解决机器人已经开始执行旧任务、收到新指令却仍继续旧任务或停住的问题。它把机器人移到适合接续新任务的接近状态，再交回原策略控制，全程无需重新训练。

## 问题

机器人伸手去拿第一个物体时，人可能改口让它拿第二个。固定指令的模仿数据里，已经伸出的手往往足以暴露原任务，策略只看执行状态也可能猜中下一步。作者证明，在状态已经揭示任务的条件下，静态模仿无法区分遵循指令的策略和忽略指令的策略。这解释了为什么训练时表现正常，途中改口却可能失效。

### 用一个例子理解

理解用例（非论文实验）。输入是机械臂已伸向红杯的当前状态和新指令“拿蓝杯”。Wormhole 选择一个适合接近蓝杯的状态，限速将机械臂移过去，再由原策略输出剩余的靠近与抓取动作。

## 创新点或方法

单纯改写指令会把原策略留在旧任务已经展开的状态。Wormhole 用最优传输选出新任务的一个接近阶段状态，再通过限速过渡把机器人带过去，让原策略从新任务较早的阶段接手。改动发生在推理时。摘要未说明候选状态怎样取得、匹配代价怎样设计，也未说明怎样处理过渡路径上的障碍。

### 方法如何工作

1. 在执行已展开后下发新指令，测试机器人是否会跟随变化，避免把起步时换任务与中途切换混为一谈。
2. 用最优传输选择新任务接近阶段的目标状态，让后续控制从适合展开新任务的位置开始。
3. 用限速过渡把机器人移向目标状态，减小直接切换时的动作突变。
4. 到达接续状态后交回原策略，由它执行新任务。摘要未说明精确的交接判据。

### 必要术语

- 静态模仿：从任务指令固定的示范中学习动作；本文分析这种训练何时无法识别策略是否真的使用指令。
- 最优传输：按给定代价匹配分布中的样本；本文用它在新任务的接近阶段选择接续状态。
- 接近阶段：机器人为后续操作靠近目标的阶段；本文从这一阶段选取原策略接手的位置。

## 证据

据摘要，在 LIBERO 仿真中，对所测两种 VLA 策略，任务已进入执行阶段后的切换成功率从最高 1.2% 升到 93.1%。与脚本化后退重启相比，成功表现持平或更好，动作不连续性为其五分之一。摘要未给出逐策略结果、任务对、试验次数或不连续性的计算方式。数字支持所测仿真切换设置中的效果，真机表现需要另行核查。

## 局限

理论结论有一个具体条件，即执行状态已经能揭示任务。实证来自 LIBERO。我会核查当夹爪已抓住物体，或旧任务已改变环境时，新任务的接近状态是否仍可达。限速与动作不连续性指标本身无法回答这个问题。

- **判断**：值得读静态模仿的证明、接近状态的选择规则和过渡实现，这三处决定何时会切换失败，以及插件何时能接得上。

## 研究关联

如果策略能完成各个固定任务，想知道它是否会在途中响应改口，就应在已经出现任务特定动作后再切换指令。这会暴露常规任务成功率掩盖的问题。若系统能够把机器人带到一个合适的接续状态，也可以单独研究如何交接，无需先改动原策略。

### 下一步读哪里

先查指令传输率与事件视界怎样定义，以及作者在哪些执行时刻下发新指令。再看候选状态来源、传输代价和过渡如何执行，并查评测是否包含旧任务已经改变物体状态的情形。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/Escapingthe instruction blackhole of vision-language-action policies via optimal.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies are trained to follow a fixed instruction, yet people change their minds while the robot acts. We identify the instruction black hole: once a VLA policy commits to a task, new instructions are absorbed and the robot completes the old task or freezes. We quantify it with a transmission ratio and an event horizon and prove it is a blind spot of static imitation, which cannot distinguish a policy that listens from a deaf one once the execution state reveals the task. We propose Wormhole, a training-free plug-in that relocates the robot instead of re-instructing it: optimal transport selects an approach-phase state of the new task, a rate-limited traversal carries the robot there, and the unmodified policy takes over. On LIBERO,Wormhole raises committed-switch success of pi to and pi0.5 from at most 1.2% to 93.1%, matching or exceeding scripted retreat-and-restart with one fifth of its action discontinuity.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34280v1
- Authors: Xuetao Li, Chen Liu, Jing Wu, Sheng Liu, Miao Li
- Published: 2026-11-25T12:36:42Z
- Age days: 1

</details>
