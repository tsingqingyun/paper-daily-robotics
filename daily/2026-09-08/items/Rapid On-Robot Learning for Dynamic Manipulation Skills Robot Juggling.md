---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26800"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 31
created: 2026-09-08
concepts: ["机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Rapid On-Robot Learning for Dynamic Manipulation Skills: Robot Juggling

> [!summary] 先说人话（基于摘要）
> 这项在线学习方法让双臂机器人在几分钟内学会多种杂耍。它保留不完美的先验模型，用实际经验修正局部预测，并限制动作始终能安全衔接下一次抛接。

## 这篇到底在做什么

- **卡在哪里**：高速动态操作存在显著仿真到现实差距，盲目探索代价高；连续练习还必须避免进入下一动作无法满足关节或执行器限制的状态。
- **关键解法**：正则化记忆学习从累积经验拟合局部模型，在经验稀疏处保留全局先验进行外推；通过互相可达集合约束连续抛接之间的安全转移。
- **拿什么证明**：配备多指手和机载视觉的双臂机器人，在少于五分钟真实交互内学习并组合 cascade、tennis、half-shower、shower、box 五种三球杂耍模式。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习与 Sim2Real 的价值在于展示如何利用有偏先验加速真机适应，并把可持续练习的约束纳入学习过程。
- **先别急着信**：需核查五分钟的统计口径、初始先验及成功判定；安全机制的明确范围是关节和执行器约束下的连续动作可达性。
- **判断**：优先精读局部模型与可达集合设计，是今天真机快速学习中机制最值得追踪的工作之一。

## 研究关联

- **概念**：[[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/Rapid On-Robot Learning for Dynamic Manipulation Skills Robot Juggling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.26800v2 Announce Type: replace Abstract: We present an online learning framework that enables a bimanual robot to acquire diverse juggling patterns directly on physical hardware within minutes, even with a significant sim2real gap. One of the most important lessons from this work is that a model, even when far from reality, can be extremely useful for learning. This motivates a central philosophy of our approach: learning should build upon the robot's current knowledge rather than replace it. Our regularized memory-based learning puts this principle into practice by learning a local model from accumulated experience while retaining the global prior model to extrapolate where experience is sparse. This enables efficient and stable online learning from each new experience without resorting to uninformed exploration over a vast space of possible behaviors. Equally important to continual on-robot learning is safety, allowing the robot to repeatedly practice and improve in the real world. We construct a mutually reachable set that allows safe transitions between successive throws and catches, without driving either arm into a state from which its next action would require violating the robot's joint or actuator limits. Together, these ideas enable a bimanual robot with multi-fingered hands and onboard vision to safely learn and compose five canonical three-ball juggling patterns, including cascade, tennis, half-shower, shower, and box, within less than 5 minutes of real-world interaction. More broadly, this work points toward robots that build upon imperfect prior knowledge and continually refine their behavior through their own real-world experience.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26800
- Authors: Taeyoon Lee, Chunpeng Wang, Christopher G. Atkeson, Alfred A. Rizzi, Nicolas Rojas
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
