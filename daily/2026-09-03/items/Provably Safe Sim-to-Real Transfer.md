---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.01418v1"
published: "2026-09-01T15:34:57Z"
age_days: 1
score: 32
created: 2026-09-03
concepts: ["智能体 Agent", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Provably Safe Sim-to-Real Transfer

> [!summary] 先说人话（基于摘要）
> 论文把安全 Sim2Real 表述为 reward-free safe RL：先利用不完美模拟器减少真实交互，再在安全约束下探索，最终可针对任意奖励求近最优可行策略。其理论界用仿真—现实偏差刻画模拟器究竟省了多少真实样本。

## 这篇到底在做什么

- **卡在哪里**：仿真策略可能因现实差距而次优，纠偏又必须采集真实数据；机器人和医疗等场景中，采集本身受安全约束，因此不能靠无保护的在线试错完成适配。
- **关键解法**：算法在无奖励安全强化学习框架内复用模拟器信息，以计算高效的方式组织安全现实探索，并保留之后针对潜在奖励函数求解近最优可行策略的能力；区别于直接部署，它对安全和样本复杂度给出保证。
- **拿什么证明**：摘要声称证明安全探索、近最优可行策略求解以及减少真实交互，并给出依赖 Sim2Real mismatch 的真实样本复杂度界；未给出界的公式、实验或结果数字。

## 值不值得读

- **和你的研究有什么关系**：对安全关键机器人学习，它提供了衡量模拟器价值的理论语言：模拟器不是默认有益，其收益应随现实偏差定量变化。
- **先别急着信**：关键结论依赖全文中的环境假设、偏差定义和安全信息可得性；摘要没有说明这些条件在真实机器人上是否可满足。
- **判断**：理论型读者应精读定理与假设；工程读者可先看问题设定，因为摘要尚无真实部署证据。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Provably Safe Sim-to-Real Transfer.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be suboptimal in the real world due to sim-to-real mismatch. Correcting this mismatch requires collecting data from the real system, but in many applications, such as robotics and healthcare, this data-collection process is itself subject to safety constraints. This gives rise to the problem of safe sim-to-real transfer: how can an agent exploit an imperfect simulator while ensuring safe real-world data collection and learning a near-optimal feasible policy for the target system? We address this problem by formulating safe sim-to-real transfer within the framework of reward-free safe RL. We design a computationally efficient algorithm that exploits simulator information to provably reduce real-world interaction while ensuring safe exploration and enabling the computation of a near-optimal feasible policy for any potential reward function. Our real-world sample complexity bound characterizes the benefit of using the simulator in terms of the sim-to-real mismatch.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.01418v1
- Authors: Tingting Ni, Maryam Kamgarpour
- Published: 2026-09-01T15:34:57Z
- Age days: 1

</details>
