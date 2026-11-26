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
url: "https://arxiv.org/abs/2611.33390v1"
published: "2026-11-24T20:14:04Z"
age_days: 1
score: 38
created: 2026-11-26
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RoboARC 用必须沿特定路线运动的仿真谜题，测试机器人能否按眼前的几何解题。它在同一场景里切换可读完整状态、可重置的模式和仅凭传感器、单次执行的模式，再用补充信息实验定位卡点。

## 问题

穿窄缝、拆互锁零件或穿绳时，能走的路线由零件形状和当前位置决定。旧示范可能教会抓和推，但一个小角度变化就可能让原路线卡死。仅看最终成功率，又很难分清机器人是没看清、没想出路线，还是沿路线执行时出了差错。[S5](https://arxiv.org/html/2611.33390v1#S1.p1.1)[S10](https://arxiv.org/html/2611.33390v1#S1.p6.1)

### 用一个例子理解

理解用例（非论文实验）——让机械臂把一块带凸耳的板穿过稍宽的缝。标准模式由深度图估计板和缝的位置，规划先旋转再平移，执行后由判分器检查板是否通过。若卡住，就在同一题补给精确位姿和外形，检查可行路线是否随之出现。

## 创新点或方法

RoboARC 把问题做成固定初始场景，每题都配经验证、可精确回放的参考解和基于物理状态的判分器。特权模式可读完整仿真状态、反复重置试走；标准模式的编程智能体只能在一次实时运行中根据相机和机器人本体读数决定下一段动作。任务、物理规则、判分保持一致。评测系统均未针对这些题训练；运行时编程智能体写代码处理当前任务，VLA 在适配其硬件的标准模式子集上直接生成动作。[S2](https://arxiv.org/html/2611.33390v1#abstract1.1)[S4](https://arxiv.org/html/2611.33390v1#S1.F2)[S15](https://arxiv.org/html/2611.33390v1#S3.SS1.p1.1) [S16](https://arxiv.org/html/2611.33390v1#S3.SS1.p2.1) [S17](https://arxiv.org/html/2611.33390v1#S3.SS2.SSS0.Px1.p1.1) [S18](https://arxiv.org/html/2611.33390v1#S3.F4) [S19](https://arxiv.org/html/2611.33390v1#S3.SS2.SSS0.Px2.p1.1) [S20](https://arxiv.org/html/2611.33390v1#S4.SS1.SSS0.Px1.p1.1)

### 方法如何工作

1. 固定谜题初始状态，并用参考轨迹验证场景与成功判定确实可达。
2. 让同一智能体在两种权限下解题，保留相同物理规则和动作目标。
3. 记录动作和仿真状态，由判分器判断任务是否完成，并回放定位失败步骤。
4. 在标准模式逐项补回位姿和形状，测量各项信息及其组合对选定难题的作用。

### 必要术语

- 位姿：物体在哪里、朝哪边；它决定可行路线该怎样放进当前场景。
- 部分可观测：传感器只看见完整状态的一部分；标准模式需要从有限观察推断关键几何。
- 物理判分器：根据模拟状态或事件判定成功；本文用它对实际执行结果统一评分。

## 证据

MuJoCo 中有三种机器人配置、六类约束和 90 题。七个编程智能体中，GPT-6 Astra 的特权和标准成功率分别为 86% 和 43%。四个零样本 VLA 在其 18 道单臂题上均未解出。对筛出的 15 道题，补物体位姿或零件形状分别增加 4 和 13 个百分点，两者同给使标准模式从 24% 到 60%。这组干预支持两种信息在所选题上能互补。[S2](https://arxiv.org/html/2611.33390v1#abstract1.1)[S19](https://arxiv.org/html/2611.33390v1#S3.SS2.SSS0.Px2.p1.1) [S20](https://arxiv.org/html/2611.33390v1#S4.SS1.SSS0.Px1.p1.1)[S23](https://arxiv.org/html/2611.33390v1#S6.p1.1)[S30](https://arxiv.org/html/2611.33390v1#A5.SS4.SSS0.Px4.p1.1)[S37](https://arxiv.org/html/2611.33390v1#A6.T16.5.1)

## 局限

两种模式同时改变了状态可见性和重置权限，主结果的差距不能归给感知一项。信息消融专挑特权成功、标准失败的题，且与主评测的推理档位、种子安排有别。作者的失败回放也发现规划和接触执行错误。评测全在仿真，部分抓取有辅助；我会查取消抓取辅助后，瓶颈是否转向稳定抓持。[S10](https://arxiv.org/html/2611.33390v1#S1.p6.1)[S19](https://arxiv.org/html/2611.33390v1#S3.SS2.SSS0.Px2.p1.1)[S23](https://arxiv.org/html/2611.33390v1#S6.p1.1)[S30](https://arxiv.org/html/2611.33390v1#A5.SS4.SSS0.Px4.p1.1)

- **判断**：优先读双模式协议和信息消融，分数最值得用来找精细操作卡在哪里。

## 研究关联

调试精细操作时，可以固定同一道题和同一种判分，先补物体当前位置，再补形状，最后都补。若单独提供一项几乎无效，继续加同一类传感器之前，值得先查规划器是否同时缺另一项信息。

### 下一步读哪里

用 [S15](https://arxiv.org/html/2611.33390v1#S3.SS1.p1.1) [S16](https://arxiv.org/html/2611.33390v1#S3.SS1.p2.1)[S28](https://arxiv.org/html/2611.33390v1#A3.SS2.p1.1) [S29](https://arxiv.org/html/2611.33390v1#A3.F22) [S30](https://arxiv.org/html/2611.33390v1#A5.SS4.SSS0.Px4.p1.1) 核对观测、控制和重置权限。读 [S31](https://arxiv.org/html/2611.33390v1#A5.T14) 指向的表 14 时看每个补信息条件的试验数与波动，再用 [S37](https://arxiv.org/html/2611.33390v1#A6.T16.5.1) 检查总体落差主要集中于哪些任务家族。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.33390v1
- 获取时间：2026-11-26T03:57:06.751211+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.33390v1#p1.2)
- [S2] [RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints · 正文段落 2](https://arxiv.org/html/2611.33390v1#abstract1.1)
- [S3] [RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints · 正文段落 3](https://arxiv.org/html/2611.33390v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.33390v1#S1.F2)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.33390v1#S1.p1.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.33390v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.33390v1#S1.T1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.33390v1#S1.T1.5.1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.33390v1#S1.p5.1)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.33390v1#S1.p6.1)
- [S11] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.33390v1#S1.p7.1)
- [S12] [1 Introduction · 正文段落 13](https://arxiv.org/html/2611.33390v1#S1.p8.1)
- [S13] [1 Introduction · 正文段落 15](https://arxiv.org/html/2611.33390v1#S1.I1.i2)
- [S14] [1 Introduction · 正文段落 17](https://arxiv.org/html/2611.33390v1#S1.I1.i4)
- [S15] [3.1 Problem formulation · 正文段落 23](https://arxiv.org/html/2611.33390v1#S3.SS1.p1.1)
- [S16] [3.1 Problem formulation · 正文段落 26](https://arxiv.org/html/2611.33390v1#S3.SS1.p2.1)
- [S17] [Constraint types. · 正文段落 27](https://arxiv.org/html/2611.33390v1#S3.SS2.SSS0.Px1.p1.1)
- [S18] [Constraint types. · 正文段落 28](https://arxiv.org/html/2611.33390v1#S3.F4)
- [S19] [Scale and simulation. · 正文段落 29](https://arxiv.org/html/2611.33390v1#S3.SS2.SSS0.Px2.p1.1)
- [S20] [Policy classes. · 正文段落 32](https://arxiv.org/html/2611.33390v1#S4.SS1.SSS0.Px1.p1.1)
- [S21] [Agents. · 正文段落 33](https://arxiv.org/html/2611.33390v1#S4.SS1.SSS0.Px2.p1.1)
- [S22] [4.2 Main results · 正文段落 37](https://arxiv.org/html/2611.33390v1#S4.SS2.p1.1)
- [S23] [6 Conclusion · 正文段落 68](https://arxiv.org/html/2611.33390v1#S6.p1.1)
- [S24] [Constraint types. · 正文段落 98](https://arxiv.org/html/2611.33390v1#A2.SS2.SSS0.Px1.p1.1)
- [S25] [Constraint types. · 正文段落 99](https://arxiv.org/html/2611.33390v1#A2.SS2.SSS0.Px1.p2.1)
- [S26] [Budget. · 正文段落 103](https://arxiv.org/html/2611.33390v1#A2.SS2.SSS0.Px4.p1.1)
- [S27] [Interfaces for any policy class. · 正文段落 131](https://arxiv.org/html/2611.33390v1#A3.SS1.SSS0.Px3.p1.1)
- [S28] [C.2 What a policy receives · 正文段落 132](https://arxiv.org/html/2611.33390v1#A3.SS2.p1.1)
- [S29] [C.2 What a policy receives · 正文段落 133](https://arxiv.org/html/2611.33390v1#A3.F22)
- [S30] [The same puzzles in the main evaluation. · 正文段落 182](https://arxiv.org/html/2611.33390v1#A5.SS4.SSS0.Px4.p1.1)
- [S31] [The same puzzles in the main evaluation. · 正文段落 183](https://arxiv.org/html/2611.33390v1#A5.T14)
- [S32] [F.1 Per-family results · 正文段落 185](https://arxiv.org/html/2611.33390v1#A6.SS1.p1.1)
- [S33] [F.1 Per-family results · 正文段落 186](https://arxiv.org/html/2611.33390v1#A6.T15)
- [S34] [F.1 Per-family results · 正文段落 188](https://arxiv.org/html/2611.33390v1#A6.F27)
- [S35] [F.1 Per-family results · 正文段落 189](https://arxiv.org/html/2611.33390v1#A6.F28)
- [S36] [F.1 Per-family results · 正文段落 190](https://arxiv.org/html/2611.33390v1#A6.T16)
- [S37] [F.1 Per-family results · 正文段落 191](https://arxiv.org/html/2611.33390v1#A6.T16.5.1)
- [S38] [F.1 Per-family results · 正文段落 192](https://arxiv.org/html/2611.33390v1#A6.T17)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/RoboARC Physical Puzzles for Robotic Manipulation under Spatial Constraints.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than itself or separating two interlocked parts. These motions depend on the exact geometry of each scene, so demonstrations and skills recorded elsewhere rarely transfer. We therefore ask: when manipulation hinges on spatial constraints, can robots reason out the right motions? We introduce RoboARC, a benchmark of 90 tasks in six constraint types over rigid and soft materials, on three robots in MuJoCo. Every task is a frozen scene with a physics-based grader and a verified reference solution that replays bit-identically. Each task comes in a Privileged regime, with the full simulator state and resets, and a Standard regime with real-sensor inputs (camera images and proprioception) and a single attempt without resets. We evaluate seven coding agents and four VLA policies, none trained on these tasks. The strongest agent, GPT-6 Astra in Codex, solves 86% of the tasks in the Privileged regime and 43% in the Standard regime, and the four VLA policies, run zero-shot, solve none of their 18 one-arm puzzles. On 15 puzzles that GPT-6 Astra solved in the Privileged regime and failed in the Standard regime, object poses add 4 points and part geometry 13, but both together add 36, from 24% to 60%. Only 7% of the coding agents' failed runs pass more than half of a task, and 53% of the failed runs in the Standard regime are stuck on a single step. Frontier coding agents already reason out the right motions for many of these tasks once they know where the parts are and what shape they have. From their own sensors, in a single attempt, the strongest solves fewer than half of the tasks. The website can be found at https://roboarc.embodied-first-exam.ai

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33390v1
- Authors: Qineng Wang, Jianwen Lyu, Pingyue Zhang, Reuben Tan, Xiaoyu Huang, Tonghe Zhang, Kangrui Wang, Yelong Shen, Jianfeng Gao, Guanya Shi, Ruohan Zhang, Manling Li
- Published: 2026-11-24T20:14:04Z
- Age days: 1

</details>
