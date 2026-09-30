---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26800v1"
published: "2026-08-27T08:39:00Z"
age_days: 2
score: 31
created: 2026-08-30
concepts: ["机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Rapid On-Robot Learning for Dynamic Manipulation Skills: Robot Juggling

> [!summary] 先说人话（基于摘要）
> 该工作让双臂机器人在真机上几分钟内学会多种三球杂耍：局部记忆模型吸收新经验，原有全局模型负责稀疏区域外推，再用互相可达集合约束连续抛接安全。

## 问题

动态操控存在明显 sim2real 差距，直接丢弃不准确模型会迫使机器人在巨大行为空间盲目探索；连续真机练习还可能把机械臂带入下一动作必然违反关节或执行器限制的状态。

## 创新点或方法

在线输入累计真机经验，更新局部动力学模型并保留全局先验作为正则和外推依据；互相可达集合筛选相邻抛接状态，使两臂能安全衔接。输出是可组合的双臂多指杂耍策略。

## 证据

带机载视觉的双臂多指机器人在少于 5 分钟真实交互内学会并组合 cascade、tennis、half-shower、shower、box 五种经典三球模式。


## 局限

需核查五分钟如何计时、各模式成功持续时间与重复稳定性，以及互相可达集合是否依赖任务专用建模。

- **判断**：非常值得精读学习更新和安全集合构造；其真机速度比单一杂耍演示本身更有价值。

## 研究关联

对机器人学习和 Sim2Real 研究者，它提供了“不完美模型仍可作为安全先验”的强案例，尤其适合高速、数据昂贵且不能随意探索的任务。

- **概念**：机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Rapid On-Robot Learning for Dynamic Manipulation Skills Robot Juggling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present an online learning framework that enables a bimanual robot to acquire diverse juggling patterns directly on physical hardware within minutes, even with a significant sim2real gap. One of the most important lessons from this work is that a model, even when far from reality, can be extremely useful for learning. This motivates a central philosophy of our approach: learning should build upon the robot's current knowledge rather than replace it. Our regularized memory-based learning puts this principle into practice by learning a local model from accumulated experience while retaining the global prior model to extrapolate where experience is sparse. This enables efficient and stable online learning from each new experience without resorting to uninformed exploration over a vast space of possible behaviors. Equally important to continual on-robot learning is safety, allowing the robot to repeatedly practice and improve in the real world. We construct a mutually reachable set that allows safe transitions between successive throws and catches, without driving either arm into a state from which its next action would require violating the robot's joint or actuator limits. Together, these ideas enable a bimanual robot with multi-fingered hands and onboard vision to safely learn and compose five canonical three-ball juggling patterns, including cascade, tennis, half-shower, shower, and box, within less than 5 minutes of real-world interaction. More broadly, this work points toward robots that build upon imperfect prior knowledge and continually refine their behavior through their own real-world experience.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26800v1
- Authors: Taeyoon Lee, Chunpeng Wang, Christopher G. Atkeson, Alfred A. Rizzi, Nicolas Rojas
- Published: 2026-08-27T08:39:00Z
- Age days: 2

</details>
