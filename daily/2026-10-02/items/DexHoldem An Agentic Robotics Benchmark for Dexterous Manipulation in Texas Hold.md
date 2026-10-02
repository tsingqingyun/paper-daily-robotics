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
url: "https://arxiv.org/abs/2605.18727"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-02
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# DexHoldem: An Agentic Robotics Benchmark for Dexterous Manipulation in Texas Hold'em

> [!summary] 这篇论文到底做了什么（基于摘要）
> DexHoldem 用真实 ShadowHand 执行德州扑克相关桌面操作，检查机器人能否看清局面、完成动作，并给下一步留下可用的现场。它最有用的区分是：一次动作完成，不等于整局还能继续。

## 问题

孤立的灵巧手测试只能说明某个动作会不会做。连续桌面任务还要求智能体恢复结构化游戏状态、选择操作，并避免弄乱后续要用的牌和筹码；其中任何一环失败，都可能让整局停住。

### 用一个例子理解

理解用例（非论文实验）：输入是一张桌面图像；智能体识别筹码和牌的位置，决定移动一摞筹码，再调用手部策略；输出不仅要把筹码送到目标区，还要保证附近牌面和筹码仍能被下一轮识别。

## 创新点或方法

DexHoldem 把单项动作测试扩展成同一物理场景中的三层检查：动作执行、游戏状态感知，以及智能体与动作策略组成的闭环。它同时记录任务完成和场景保持，避免把“做完但破坏现场”算成同样好的结果。数据包含遥操作示范，但摘要未说明各策略如何训练或微调；运行时则由智能体感知状态、派发动作，并可能重试或请求人工帮助。

### 方法如何工作

1. 收集各类操作示范并固定物理测试条件，让不同策略执行可比较的桌面动作。
2. 分别检查目标完成和现场可用性，识别动作成功却妨碍后续执行的情况。
3. 要求感知系统输出结构化游戏状态，检查零散识别能力能否拼成完整决策输入。
4. 把感知、派发和执行接成闭环，记录重试、求助和整局完成，暴露跨步骤累积问题。

### 必要术语

- 操作原语：可单独调用的一项基本动作；它是这里的策略测试单位。
- 场景保持成功率：完成动作后现场仍满足规定可用条件的比例；具体判据需查正文。
- 字段准确率：逐项检查状态信息是否正确；多个字段各自较准，仍可能无法组成一份全对的状态。

## 证据

摘要给出 14 类操作、1,470 条示范。动作测试中，π₀.₅ 完成率最高，为 61.2%；π₀.₅ 与 π₀ 的场景保持成功率同为 47.5%。感知测试中，Opus 5.5 的整题严格准确率为 49.1%，字段平均准确率为 80.6%。一个智能体—策略组合执行 33 次整手牌闭环，完成率仅 12.1%；34 次重试派发中有 12 次恢复失败动作，四次完成中有三次靠重试解除长时间停滞，只有一次既未重试也未请求人工帮助。这些是不同层级的指标，不能直接互相相减来归因。

## 局限

这是实际灵巧硬件上的评测，但完整闭环只覆盖一个组合和 33 次运行，不能据此排名各类智能体。重试的恢复记录说明它有用，却不足以量化独立因果收益；还需检查对照运行和人工帮助发生的位置。

- **判断**：值得细读成功判据和失败案例，尤其是场景保持与整局完成的差距；模型排行榜反而是次要信息。

## 研究关联

具体启示是把“给下一步留下什么状态”写进成功标准。对任何连续桌面操作，都可以分别记录当前目标是否达成，以及剩余物品是否仍满足后续操作条件，从而发现单步成功率掩盖的问题。

### 下一步读哪里

先查场景保持的判定规则、感知字段定义和严格准确率的计算方式，再核查示范如何用于各模型、闭环何时重试与求助，以及最终完成是否包含人工介入。

- **概念**：智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/DexHoldem An Agentic Robotics Benchmark for Dexterous Manipulation in Texas Hold.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.18727v2 Announce Type: replace Abstract: Evaluating embodied systems with real dexterous hardware requires more than isolated motor-skill tests: an agent must perceive a changing scene (e.g. a tabletop), choose a context-appropriate action, execute it with a dexterous hand, and leave the scene usable for later decisions. We introduce DexHoldem, a comprehensive real-world benchmark evaluating Texas Hold'em related dexterous manipulations with a ShadowHand. DexHoldem provides 1,470 teleoperated demonstrations across 14 Texas Hold'em manipulation primitives, a standardized physical policy benchmark, and an agentic perception benchmark that tests whether agents can recover the structured game state needed for embodied decision making. On primitive execution, $\pi_{0.5}$ obtains the highest task completion rate ($61.2\%$), while $\pi_{0.5}$ and $\pi_0$ tie on scene-preserving success rate ($47.5\%$). On agentic perception, Opus 5.5 narrowly leads on both strict problem-level accuracy ($49.1\%$) and average field-wise accuracy ($80.6\%$); the gap between the two exposes the distance between isolated visual sub-capabilities and complete routing-relevant state recovery. Finally, we instantiate the full embodied-agent loop with one agent--policy pairing over 33 closed-loop hand-level rollouts, in which only $12.1\%$ of hands complete; retries restore the failed primitive in 12 of 34 dispatches and resolve prolonged execution stalls in three of the four completed hands, which would otherwise have required manual termination. Only one hand completes with neither a retry nor a human-help request. DexHoldem therefore evaluates dexterous tabletop execution, agentic perception, and embodied decision routing in a shared physical setting. Project Website at https://dexholdempage.github.io/DexHoldem

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18727
- Authors: Feng Chen, Tianzhe Chu, Li Sun, Pei Zhou, Zhuxiu Xu, Shenghua Gao, Yuexiang Zhai, Yanchao Yang, Yi Ma
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
