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
url: "https://arxiv.org/abs/2610.22496v1"
published: "2026-10-15T18:00:28Z"
age_days: 3
score: 46
created: 2026-10-19
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Scaling Online Exploration for Robot Agents

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RAX 让编码智能体直接操作机器人，边试边改控制程序，再把成功经验保存成能重复运行的技能。它的学习主要发生在代码、笔记和技能库里，底层语言模型权重不变。

## 问题

任务从精细插入一直到家庭移动操作。作者针对的瓶颈是：换机器人或任务往往还得重新收遥操作数据，而静态模仿没有让机器人主动尝试、诊断失败和发现新办法的过程；已有动作会做，不代表能在陌生布局里把它们可靠组合起来。[S5](https://arxiv.org/html/2610.22496v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：输入“把插头插进插座”和相机、力觉数据；智能体先定位，尝试后发现偏差，修改接触搜索和退出条件；输出能根据新观测纠偏、失败时重试的插入程序。

## 创新点或方法

旧路线主要从示范拟合动作；RAX 改为让编码智能体调用传感器、控制 SDK 和运动学工具，执行后检查结果并修改程序。关键是保存“根据当前观测怎样决策”，而非只记录一串动作。探索阶段不断调试，部署时由程序执行感知—规划—控制闭环，必要时仍可调用模型；不是每个控制周期都重新让大模型推理。[S7](https://arxiv.org/html/2610.22496v1#S1.p4.1) [S10](https://arxiv.org/html/2610.22496v1#S1.p7.1) 不训练新策略，但允许目标图片或视觉示例；不能把它理解成完全没有先验或任务提示。

### 方法如何工作

1. 读取任务和机器人接口，获得可观察、可控制的范围，避免把抽象目标当成现成动作。
2. 调用感知和运动工具尝试操作，观察结果，得到具体失败或成功证据。
3. 据证据修改程序中的定位、规划或反馈逻辑，使下次执行能应对当前瓶颈。
4. 把无人监督成功执行的代码、日志和前提存成技能，后续任务检索组合并检查执行结果。[S17](https://arxiv.org/html/2610.22496v1#S3.SS4.p2.1) [S18](https://arxiv.org/html/2610.22496v1#S3.SS4.SSS0.Px1.p1.1)

### 必要术语

- 在线探索：实际交互后根据结果修改行为；本文用它积累程序经验。
- 闭环控制：执行中持续读取反馈并调整动作；让保存的程序适应位置误差。
- 逆运动学：把目标末端姿态换成关节配置；帮助代码寻找机器人能做到的动作。

## 证据

仿真覆盖多种机器人，探索和未见场景评估分开。[S12](https://arxiv.org/html/2610.22496v1#S1.p9.1) 平均领先 37.4 个百分点是五个基准相对最强既有学习策略的等权差值，不是相对所有智能体方法；其中 DexJoCo 只取双臂任务，LIBERO-Pro 对比 VPP2。换成全部任务或更强编码智能体，差值不同。[S25](https://arxiv.org/html/2610.22496v1#S13.p1.1) [S26](https://arxiv.org/html/2610.22496v1#S13.p2.1) 真机为 Franka、RB-Y1，报告五项桌面任务及长程移动操作，但节选未给逐项成功率。HumanoidArena 使用每任务三条遥操作示范，不能把全部实验统称零示范。[S12](https://arxiv.org/html/2610.22496v1#S1.p9.1)

## 局限

我的待核查重点是比较条件：深度、力觉、探索次数与模型调用预算是否匹配；这些丰富输入本身也可能贡献收益。[S9](https://arxiv.org/html/2610.22496v1#S1.p6.1) BEHAVIOR-1K 部分测试实例还收到其他测试实例的运行评审，不能一概理解为完全独立的冻结程序测试。[S23](https://arxiv.org/html/2610.22496v1#S10.SS4.SSS0.Px3.p1.1) 碰撞后生成安全检查的案例也不等于已有安全保证。

- **判断**：值得细读程序形成和评估协议：真正有启发的是把在线试错变成可复用闭环代码，效果大小则必须连同输入和预算一起看。

## 研究关联

值得借鉴的是把成功经验存成带前提条件和检查点的可执行程序。若机器人接口稳定、能承担反复试验成本，这让后续任务可以复用已验证行为，而不必把每次改进都变成权重训练。[S11](https://arxiv.org/html/2610.22496v1#S1.p8.1) [S17](https://arxiv.org/html/2610.22496v1#S3.SS4.p2.1)

### 下一步读哪里

先沿 [S7](https://arxiv.org/html/2610.22496v1#S1.p4.1) [S10](https://arxiv.org/html/2610.22496v1#S1.p7.1) [S11](https://arxiv.org/html/2610.22496v1#S1.p8.1) 看经验怎样进入程序，再核查 [S22](https://arxiv.org/html/2610.22496v1#S10.SS3.SSS0.Px3.p1.1) [S23](https://arxiv.org/html/2610.22496v1#S10.SS4.SSS0.Px3.p1.1) [S24](https://arxiv.org/html/2610.22496v1#S10.SS5.SSS0.Px3.p1.1) [S25](https://arxiv.org/html/2610.22496v1#S13.p1.1) [S26](https://arxiv.org/html/2610.22496v1#S13.p2.1) 的数据划分、评分和对比口径；还应查真机重置、人类介入、探索耗时及技能失效条件。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：46
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.22496v1
- 获取时间：2026-10-19T15:35:12.664104+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.22496v1#p1.1)
- [S2] [正文 · 正文段落 2](https://arxiv.org/html/2610.22496v1#S0.F1)
- [S3] [Scaling Online Exploration for Robot Agents · 正文段落 3](https://arxiv.org/html/2610.22496v1#abstract1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.22496v1#S1.I1.i1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.22496v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.22496v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.22496v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.22496v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.22496v1#S1.p6.1)
- [S10] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.22496v1#S1.p7.1)
- [S11] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.22496v1#S1.p8.1)
- [S12] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.22496v1#S1.p9.1)
- [S13] [1 Introduction · 正文段落 14](https://arxiv.org/html/2610.22496v1#S1.I2.i1)
- [S14] [1 Introduction · 正文段落 15](https://arxiv.org/html/2610.22496v1#S1.I2.i2)
- [S15] [1 Introduction · 正文段落 17](https://arxiv.org/html/2610.22496v1#S1.p10.2)
- [S16] [3.2 Planning and Control · 正文段落 27](https://arxiv.org/html/2610.22496v1#S3.SS2.p1.1)
- [S17] [3.4 Continual Learning with Memory · 正文段落 32](https://arxiv.org/html/2610.22496v1#S3.SS4.p2.1)
- [S18] [3.4 Continual Learning with Memory · 正文段落 33](https://arxiv.org/html/2610.22496v1#S3.SS4.SSS0.Px1.p1.1)
- [S19] [5 Experiments · 正文段落 48](https://arxiv.org/html/2610.22496v1#S5.p1.1)
- [S20] [5.2 Simulation Results · 正文段落 52](https://arxiv.org/html/2610.22496v1#S5.SS2.p1.1)
- [S21] [5.3 Ablations · 正文段落 79](https://arxiv.org/html/2610.22496v1#S5.SS3.p1.1)
- [S22] [10.3 RoboDojo · 正文段落 140](https://arxiv.org/html/2610.22496v1#S10.SS3.SSS0.Px3.p1.1)
- [S23] [10.4 BEHAVIOR-1K · 正文段落 145](https://arxiv.org/html/2610.22496v1#S10.SS4.SSS0.Px3.p1.1)
- [S24] [10.5 HumanoidArena · 正文段落 150](https://arxiv.org/html/2610.22496v1#S10.SS5.SSS0.Px3.p1.1)
- [S25] [13 Summary Results of 1 · 正文段落 212](https://arxiv.org/html/2610.22496v1#S13.p1.1)
- [S26] [13 Summary Results of 1 · 正文段落 213](https://arxiv.org/html/2610.22496v1#S13.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/Scaling Online Exploration for Robot Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot learning has advanced by scaling demonstration datasets and model capacity; however, deploying a new robot embodiment or task typically necessitates a dedicated teleoperation corpus. The resulting policies remain bounded by their imitation distributions, limiting generalization and continual self-improvement. We introduce RAX (Robot Agent eXploration), an open-source framework for robot agents centered on scaling exploration: enabling agents to improve by acquiring online experience and synthesizing executable programs. In RAX, a general-purpose coding agent generates robot control code, operating without action demonstration data, hand-engineered action primitives, or value-function guidance. Through online exploration, the agent identifies decision sequences that achieve task goals and compiles them into modular programs encapsulating the full perception-planning-control loop. Using RAX, we present a systematic multi-embodiment study on scaling online exploration across precision and long-horizon manipulation tasks using single-arm, bimanual, dexterous, mobile, and humanoid systems in simulation and on real robots. Generalization performance on unseen environments improves consistently as exploration scales. In simulation, RAX outperforms top baseline models by +37.4% on average. On real robots, RAX autonomously learns memory-dependent, articulated, high-precision, deformable, and long-horizon mobile manipulation tasks without human demonstrations, continually improving performance by composing verified skills from prior exploration sessions. As exploration scales, we observe emergent capabilities including active perception, error recovery, safety guardrails, and human-robot collaboration. We open-source RAX as a generalist robot-agent platform in which new robot embodiments are integrated through their APIs alone, without teleoperated data collection or policy training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22496v1
- Authors: Runhan Huang, Xiangcheng Zhang, Haoyu Chen, Yitong Li, Yen-Jen Wang, Bohan Lyu, Haotian Ye, Chuye Hong, Yixuan Wang, Chloe Su, Haoyu Xiong, Yangzhen Wu, Enze Xie, Travis Manderson, Stefano Ermon, Pieter Abbeel, Antonio Torralba, Dawn Song, Weirui Ye, Yilun Du
- Published: 2026-10-15T18:00:28Z
- Age days: 3

</details>
