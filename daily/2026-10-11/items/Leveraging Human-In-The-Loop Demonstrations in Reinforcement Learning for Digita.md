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
url: "https://arxiv.org/abs/2610.12140v1"
published: "2026-10-08T15:26:12Z"
age_days: 2
score: 26
created: 2026-10-11
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Leveraging Human-In-The-Loop Demonstrations in Reinforcement Learning for Digital Twin-Driven Robot Flexibility

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇把实时更新的数字孪生、强化学习和人类示范连在一起，让机器人在工作区变化后继续训练。关键是双 actor 接入示范，避免直接要求强化学习 actor 模仿可能很差的示范。

## 问题

任务是让 Ufactory Xarm5 的末端到达目标位置，同时避开障碍，且能适应物理工作区变化。传统数字孪生主要在执行前生成合成数据，难以持续反映现场变化；直接给强化学习 actor 加模仿损失，又可能让它受非最优示范牵制。这里要解决的是现场反馈如何进入训练，以及失败示范怎样仍能帮助学习。

### 用一个例子理解

理解用例（非论文实验）：机械臂要绕开桌上盒子到达标记点，盒子随后被移动。摄像头把变化送入数字孪生，训练结合现场反馈和一段未完成到达任务的人类示范继续更新；输出是重新学习的避障到达策略。

## 创新点或方法

旧做法使用执行前准备好的孪生数据，或把模仿目标直接叠加到强化学习 actor 上；本文通过摄像头实时同步物理系统，让虚拟机器人依据现实反馈更新观测和策略。双 actor 结构整合模仿学习，但不给 RL actor 直接加模仿损失，使示范能够引导适应，而不必成为最终行为的复制目标。摘要未说明两个 actor 如何交换信息、选择动作或共同更新，因此不能补写具体算法。训练是在线适应过程；确定性评估检验学习后的行为，但虚实策略的部署链路尚未交代。

### 方法如何工作

1. 用摄像头同步物理工作区与数字孪生，使训练观测能反映现场变化。
2. 把人类示范接入双 actor 结构，为适应提供行为线索，而不直接给 RL actor 加模仿损失。
3. 结合现实反馈继续更新虚拟机器人的观测与策略，使工作区变化后能够恢复训练。
4. 用确定性评估检查到达与避障成功率，比较不同示范接入方式；虚实评估分配摘要只说明到此。

### 必要术语

- 数字孪生：与物理系统对应的虚拟系统；本文通过摄像头持续同步现场信息。
- actor：根据观测产生动作的策略部分；本文用两个 actor 整合强化学习和模仿学习。
- 模仿损失：推动策略接近示范动作的训练目标；本文避免把它直接加到 RL actor 上。
- 确定性评估：按固定决策规则执行策略来测表现；本文报告这种评估下的成功率。

## 证据

摘要报告系统在物理工作区变化后可以恢复训练，并在固定非最优示范下优于两种给 actor 加模仿损失的方法。使用 VR 采集的真实人类示范时，即使示范从未到达目标，双 actor 的平均确定性评估成功率仍为 83—100%，两个对照为 0—17%（摘要）。这是特定到达与避障任务的结果；范围对应哪些条件、重复次数及各方法名称未给出。虽然系统在 Xarm5 上演示，摘要也未明确上述成功率是否全部来自真机评估。

## 局限

不能把结果概括为“失败示范总能帮助学习”，收益可能依赖示范质量、任务及双 actor 的具体耦合。我会核查无示范 RL 对照，以区分示范本身的帮助与避免模仿损失的帮助，并确认虚拟评估和真机执行各占哪些结果。

- **判断**：值得读双 actor 的更新规则及评估条件，尤其适合了解如何使用非最优示范；实时适应能力还需结合虚实同步细节判断。

## 研究关联

可借鉴的是把示范当作引导来源，同时给强化学习留下超越示范的空间。当示范包含有用动作片段却没有完成任务时，直接追随整段行为可能限制最终策略；本文给出了值得进一步核查的替代接入方式。

### 下一步读哪里

核查两个 actor 的职责、示范进入更新的具体位置，以及改变工作区后继续训练的触发方式；重点确认成功率所在环境、重复试验、无示范对照和真机部署过程。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/Leveraging Human-In-The-Loop Demonstrations in Reinforcement Learning for Digita.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Growing automation makes collaborative robots work in more variable environments, increasing the need for adaptation. We propose a human-in-the-loop online training framework combining a digital twin (DT), reinforcement learning (RL), and human demonstrations. Unlike DTs used mainly to generate synthetic data before task execution, our DT is synchronized with the physical system in real time through camera feeds, allowing the virtual robot to update its observations and policy from real-world feedback. A dual actor framework integrates imitation learning (IL) without adding a direct imitation loss to the RL actor, so demonstrations can guide adaptation instead of manual reprogramming. The proposed framework is demonstrated on the Ufactory Xarm5 collaborative robot, where the robot's end-effector aims to reach the target position while avoiding obstacles. The experiments show that the framework can resume training after a change in the physical workspace and that, with a fixed set of non-optimal demonstrations, the dual actor framework achieves a much higher final success rate than two methods that add an imitation loss to the actor. The same pattern holds with real human demonstrations collected in virtual reality (VR): with demonstrations that never reach the goal, the dual actor framework reached 83-100% mean deterministic evaluation success, against 0-17% for the two imitation-loss methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12140v1
- Authors: Yuzhu Sun, Mien Van, Nguyen Minh Nhat, Stephen McIlvanna, Sean McLoone
- Published: 2026-10-08T15:26:12Z
- Age days: 2

</details>
