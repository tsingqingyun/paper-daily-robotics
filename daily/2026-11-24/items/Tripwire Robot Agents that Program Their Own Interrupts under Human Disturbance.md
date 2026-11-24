---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.27182v1"
published: "2026-11-20T06:12:51Z"
age_days: 3
score: 40
created: 2026-11-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> TRIP 让高层智能体在启动机器人动作时，顺手写一段监测程序。程序发现人靠近或目标被挪动等情况时，可以先叫停机器人，再请智能体决定怎么继续。

## 问题

人在机器人执行过程中可能走进路线或挪动目标。底层策略虽能根据新画面调整动作，高层智能体却要等调用结束才能更改任务决策。缩短调用只能用更多次、每次耗时数秒的高层推理换取更短的观察空窗。[S3](https://arxiv.org/html/2611.27182v1#S1.p1.1) [S4](https://arxiv.org/html/2611.27182v1#S1.p2.1) [S5](https://arxiv.org/html/2611.27182v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）——机器人正去取洗碗池旁的盒子。摄像头和深度图显示有人向路线靠近，监测程序叫停并报告原因。智能体让机器人原地等待，把监测条件改成观察路线是否清空。通道空出后，智能体重新调用取盒策略。

## 创新点或方法

旧做法让智能体选定执行时长，到点再看。TRIP 在推理时为每次调用附上一段带记忆的 Python 程序，可用小型视觉语言模型找人，再结合深度和前几次观测判断是否接近。条件满足时，执行层立即停止当前调用并保持静止，再把触发原因交给智能体。智能体若决定等人离开，就把下次唤醒条件改成通道清空。整个过程无需训练或微调底层策略。[S6](https://arxiv.org/html/2611.27182v1#S1.p4.1)[S14](https://arxiv.org/html/2611.27182v1#S3.SS1.p1.1) [S15](https://arxiv.org/html/2611.27182v1#S3.SS2.SSS0.Px1.p1.1) [S16](https://arxiv.org/html/2611.27182v1#S3.I1.i2) [S17](https://arxiv.org/html/2611.27182v1#S3.SS3.p1.2)

### 方法如何工作

1. 智能体根据任务选定动作调用和监测条件，把当前最需要关注的变化交给监测程序。
2. 程序在动作执行中读取观测并更新记忆，以区分持续接近和单帧位置变化。
3. 条件触发时，执行层先停住机器人，再返回原因，让停机免于等待高层推理。
4. 智能体检查现场并决定继续、等待或换位，同时改写下一次需要关注的事件。

### 必要术语

- Tripwire：随动作调用运行的监测程序；满足条件时返回原因并触发中断。
- 有状态监测：保留之前的观测或计时信息；在本文中可用来判断人是否在接近。

## 证据

RoboHD 在 168 个模拟厨房场景中测试了三个 VLA 和一个 WAM。最强策略 XR 接入 TRIP 后，相比同智能体、同工具的回合制基线，无接触率从 61.3% 升到 81.3%，有人的任务成功率从 31.0% 升到 38.7%。前一指标只统计至少一种对照方法能在无人时完成的 150 个 XR 场景，后一指标要求完成且无接触。真机挂杯和挂毛巾受扰时，TRIP 成功 25/40，回合制为 5/40，单独运行策略为 1/40。[S7](https://arxiv.org/html/2611.27182v1#S1.p5.1)[S32](https://arxiv.org/html/2611.27182v1#S4.I2.i1) [S33](https://arxiv.org/html/2611.27182v1#S4.I2.i2) [S34](https://arxiv.org/html/2611.27182v1#S4.I2.i3) [S35](https://arxiv.org/html/2611.27182v1#S4.F4)

## 局限

作者的仿真在模型计算时暂停物理，人体接触按几何重叠判定。[S21](https://arxiv.org/html/2611.27182v1#S3.SS4.SSS0.Px3.p3.1)[S25](https://arxiv.org/html/2611.27182v1#S4.SS1.p2.1) 真机试验说明两项操作可以在干扰下恢复。我会另外核查遮挡或快速靠近时的漏检，以及从触发到机械臂实际停稳的延迟尾部。

- **判断**：值得读到执行循环和消融。固定初始规则后 XR 的无接触率降回 61.3%，能看出随决策改写规则在该设置中的作用。[S40](https://arxiv.org/html/2611.27182v1#S4.T2.3) [S41](https://arxiv.org/html/2611.27182v1#S4.T2)

## 研究关联

是否必须马上停，以及停下后该做什么，可以交给两个速度不同的环节。只要扰动有可及时测量的信号、底层调用也能中止，就可以保留原有策略，把耗时推理留给真正需要改计划的时刻。

### 下一步读哪里

先看 [S14](https://arxiv.org/html/2611.27182v1#S3.SS1.p1.1) [S15](https://arxiv.org/html/2611.27182v1#S3.SS2.SSS0.Px1.p1.1) 的中断语义和观测如何进入规则，再看 [S40](https://arxiv.org/html/2611.27182v1#S4.T2.3) [S41](https://arxiv.org/html/2611.27182v1#S4.T2) 的固定规则消融。留意预定义规则可以换来更高的无接触率，同时明显降低任务成功率。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.27182v1
- 获取时间：2026-11-24T01:58:54.745628+00:00
- [S1] [Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance · 正文段落 1](https://arxiv.org/html/2611.27182v1#abstract1.1)
- [S2] [Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance · 正文段落 2](https://arxiv.org/html/2611.27182v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.27182v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.27182v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.27182v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.27182v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.27182v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.27182v1#S1.I1.i1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.27182v1#S1.I1.i3)
- [S10] [Robot foundation models and agentic manipulation. · 正文段落 12](https://arxiv.org/html/2611.27182v1#S2.SS0.SSS0.Px1.p1.1)
- [S11] [Runtime monitoring and event-driven control. · 正文段落 14](https://arxiv.org/html/2611.27182v1#S2.SS0.SSS0.Px2.p1.1)
- [S12] [3 Method · 正文段落 16](https://arxiv.org/html/2611.27182v1#S3.p1.1)
- [S13] [3 Method · 正文段落 17](https://arxiv.org/html/2611.27182v1#alg1)
- [S14] [3.1 Event-driven Control · 正文段落 18](https://arxiv.org/html/2611.27182v1#S3.SS1.p1.1)
- [S15] [Visual perception and computation. · 正文段落 23](https://arxiv.org/html/2611.27182v1#S3.SS2.SSS0.Px1.p1.1)
- [S16] [3.3 Agent Decisions and Tools · 正文段落 28](https://arxiv.org/html/2611.27182v1#S3.I1.i2)
- [S17] [3.3 Agent Decisions and Tools · 正文段落 32](https://arxiv.org/html/2611.27182v1#S3.SS3.p1.2)
- [S18] [Scene construction. · 正文段落 35](https://arxiv.org/html/2611.27182v1#S3.SS4.SSS0.Px1.p1.1)
- [S19] [Reactive human simulation. · 正文段落 37](https://arxiv.org/html/2611.27182v1#S3.SS4.SSS0.Px3.p1.1)
- [S20] [Reactive human simulation. · 正文段落 38](https://arxiv.org/html/2611.27182v1#S3.SS4.SSS0.Px3.p2.1)
- [S21] [Reactive human simulation. · 正文段落 39](https://arxiv.org/html/2611.27182v1#S3.SS4.SSS0.Px3.p3.1)
- [S22] [4 Experiments · 正文段落 40](https://arxiv.org/html/2611.27182v1#S4.p1.1)
- [S23] [4 Experiments · 正文段落 41](https://arxiv.org/html/2611.27182v1#S4.T1.3)
- [S24] [4 Experiments · 正文段落 42](https://arxiv.org/html/2611.27182v1#S4.T1)
- [S25] [4.1 Setup · 正文段落 44](https://arxiv.org/html/2611.27182v1#S4.SS1.p2.1)
- [S26] [4.1 Setup · 正文段落 45](https://arxiv.org/html/2611.27182v1#S4.SS1.p3.1)
- [S27] [4.1 Setup · 正文段落 48](https://arxiv.org/html/2611.27182v1#S4.I1.i3)
- [S28] [4.2 Baselines · 正文段落 50](https://arxiv.org/html/2611.27182v1#S4.SS2.p1.1)
- [S29] [Policies alone. · 正文段落 51](https://arxiv.org/html/2611.27182v1#S4.SS2.SSS0.Px1.p1.1)
- [S30] [Agentic harness baseline. · 正文段落 52](https://arxiv.org/html/2611.27182v1#S4.SS2.SSS0.Px2.p1.1)
- [S31] [Metrics. · 正文段落 53](https://arxiv.org/html/2611.27182v1#S4.SS3.SSS0.Px1.p1.1)
- [S32] [Metrics. · 正文段落 54](https://arxiv.org/html/2611.27182v1#S4.I2.i1)
- [S33] [Metrics. · 正文段落 55](https://arxiv.org/html/2611.27182v1#S4.I2.i2)
- [S34] [Metrics. · 正文段落 56](https://arxiv.org/html/2611.27182v1#S4.I2.i3)
- [S35] [Metrics. · 正文段落 57](https://arxiv.org/html/2611.27182v1#S4.F4)
- [S36] [Overall performance. · 正文段落 58](https://arxiv.org/html/2611.27182v1#S4.SS3.SSS0.Px2.p1.1)
- [S37] [With and without the person. · 正文段落 59](https://arxiv.org/html/2611.27182v1#S4.SS3.SSS0.Px3.p1.1)
- [S38] [Safety. · 正文段落 60](https://arxiv.org/html/2611.27182v1#S4.SS3.SSS0.Px4.p1.1)
- [S39] [4.4 Ablation · 正文段落 61](https://arxiv.org/html/2611.27182v1#S4.SS4.p1.1)
- [S40] [4.4 Ablation · 正文段落 62](https://arxiv.org/html/2611.27182v1#S4.T2.3)
- [S41] [4.4 Ablation · 正文段落 63](https://arxiv.org/html/2611.27182v1#S4.T2)
- [S42] [Results. · 正文段落 80](https://arxiv.org/html/2611.27182v1#S4.SS5.SSS0.Px5.p1.1)
- [S43] [6 Conclusion · 正文段落 85](https://arxiv.org/html/2611.27182v1#S6.p1.1)
- [S44] [The avatar’s controller. · 正文段落 132](https://arxiv.org/html/2611.27182v1#S9.SS0.SSS0.Px3.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/Tripwire Robot Agents that Program Their Own Interrupts under Human Disturbance.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Agent harnesses are turn-based: the agent acts, waits for the result, then reasons. When the action invokes a pretrained robot policy, such as a vision-language-action (VLA) or world action model (WAM), the policy may react continuously to observations, but the agent cannot revisit its decision until the call returns. Meanwhile, a person may step into the robot's path or move the object it is about to grasp. Invoking the agent more often narrows this blind interval, but a reasoning model takes seconds per decision and most control steps need no new one. We propose TRIP, a training-free, event-driven harness in which the agent programs its own interrupts. With each call, the agent writes a tripwire: a lightweight, stateful Python program that runs alongside the policy, can query a compact VLM (for example, to locate a person and measure their distance), and decides whether the call continues or control returns to the agent. When it fires, the harness halts the policy and returns control with the reason; the agent then reassesses, adapts, and continues under a rewritten tripwire. We evaluate TRIP with three VLAs and one WAM on RoboHD, a benchmark of 168 RoboCasa365 scenes in which a simulated person disturbs the robot and any human-robot contact counts as failure. Compared with a turn-based harness using the same agent and tools, TRIP halves the rate of human contact with the strongest policy, raising safety from 61.3% to 81.3%, without sacrificing task success (38.7% vs. 31.0%). Real-robot experiments show that TRIP completes two manipulation tasks under human interference where the turn-based harness and the policy alone largely fail.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27182v1
- Authors: Sunli Chen, Yun Zong, Qinhong Zhou, Xiaowen Qiu, Jiaben Chen, Zeyuan Yang, Chuang Gan
- Published: 2026-11-20T06:12:51Z
- Age days: 3

</details>
