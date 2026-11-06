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
url: "https://arxiv.org/abs/2611.05979v1"
published: "2026-11-04T05:13:03Z"
age_days: 1
score: 37
created: 2026-11-06
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> 这篇的 Object-Centric Motion Priors（物体中心运动先验）从人手与物体的三维记录中预测两者接下来怎么动，再用预测轨迹给仿真里的机器人打分。物体运动提供了可复用的任务进度信号，各种机器人手可以分别学会怎样做到。

## 问题

多指手的关节多，接触变化又复杂，强化学习只靠最终成功来探索往往很慢，逐任务写过程奖励也费工。直接移植人手动作能提供手形参考，却容易丢掉物体应当怎样移动的信息；要求人工先指定目标物体轨迹，也会增加新场景的准备工作。[S5](https://arxiv.org/html/2611.05979v1#Sx1.p1.1) [S6](https://arxiv.org/html/2611.05979v1#Sx1.p2.1)[S11](https://arxiv.org/html/2611.05979v1#Sx2.SSx2.p1.1) [S12](https://arxiv.org/html/2611.05979v1#Sx2.SSx2.p2.1) [S13](https://arxiv.org/html/2611.05979v1#Sx2.SSx2.p3.1)

### 用一个例子理解

理解用例（非论文实验）。输入是一只带铰链的小盒子的形状和起始位姿。预测器给出盒盖逐步转开的轨迹，仿真里的机器人尝试用不同手指接触盒盖，盖子越贴近参考运动就越得分。输出是学好的开盖控制策略。

## 创新点或方法

先用 Dex-YCB 和 ARCTIC 的三维手与物体位姿训练预测器，结合物体形状和历史状态，逐步预测参考轨迹。把其中的人手动作按指尖位置映射到机器人关节，物体轨迹则直接用来给仿真动作打分。PPO 同时拿到手部跟随、物体跟随、接触与最终成功奖励，避障时另有碰撞惩罚。部署前校准仿真控制参数，并在训练时随机扰动物理参数。上机直接运行学好的状态策略，从关节位置与物体位姿输出末端和手指的增量动作。[S15](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.1) [S16](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.2) [S17](https://arxiv.org/html/2611.05979v1#Sx3.SSx2.p2.2) [S18](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p2.1) [S19](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p2.2) [S20](https://arxiv.org/html/2611.05979v1#Sx3.Ex8) [S21](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p5.1) [S22](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p6.1) [S23](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p7.1) [S24](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p8.1) [S25](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p9.1) [S26](https://arxiv.org/html/2611.05979v1#Sx3.SSx4.p1.1)

### 方法如何工作

1. 编码物体形状并输入历史手与物体位姿，训练预测器学习二者怎样一起变化。[S15](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.1) [S16](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.2)
2. 从起始状态向前滚动预测，得到手和物体参考轨迹，再按指尖位置把手部参考转换为机器人能使用的关节目标。[S9](https://arxiv.org/html/2611.05979v1#Sx1.F1)[S16](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.2) [S17](https://arxiv.org/html/2611.05979v1#Sx3.SSx2.p2.2)
3. 让 PPO 在仿真里试动作，同时奖励物体跟随、手部跟随、有效接触和完成任务，使策略在接触动力学下找到可执行动作。[S20](https://arxiv.org/html/2611.05979v1#Sx3.Ex8) [S21](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p5.1) [S22](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p6.1) [S23](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p7.1) [S24](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p8.1) [S25](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p9.1)
4. 用校准和随机扰动缩小仿真与实物差异，将训练好的策略部署到真机，用实测状态闭环控制。[S18](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p2.1)[S26](https://arxiv.org/html/2611.05979v1#Sx3.SSx4.p1.1)[S37](https://arxiv.org/html/2611.05979v1#Sx4.SSx4.p1.1)

### 必要术语

- 人手–物体交互数据（HOI）：同步记录手和物体怎么动的数据；在本文中用于训练参考轨迹预测器。
- 物体跟随奖励：实际物体状态越接近参考轨迹，得分越高；在本文中给最终成功之前的动作提供反馈。
- 动作重定向：把人手运动转换为机器人手可用的参考；在本文中按指尖位置匹配，并受关节范围约束。

## 证据

SAPIEN 和真机都测试了 YCB 抓取、铰接物体操作与避障抓取。指标为成功率，例如 YCB 物体需抬高 10 cm。比较对象包括 ViViDex、AdaDexGrasp、ManipTrans、HOP、Obj-Dex 以及用接近目标奖励替代轨迹跟随的 PPO，具体对照随任务而变。作者报告新物体和新摆位下表现较稳，去掉物体跟随后，YCB 仿真学习变慢。节选只有部分表题和定性结果，无法量化真机领先幅度。换手实验验证的是重用预测器并重新训练控制的可行性。[S29](https://arxiv.org/html/2611.05979v1#Sx4.I2.i1) [S30](https://arxiv.org/html/2611.05979v1#Sx4.I2.i2) [S31](https://arxiv.org/html/2611.05979v1#Sx4.I2.i3) [S32](https://arxiv.org/html/2611.05979v1#Sx4.I2.i4)[S38](https://arxiv.org/html/2611.05979v1#Sx4.SSx5.p1.1) [S39](https://arxiv.org/html/2611.05979v1#Sx4.Ex10) [S40](https://arxiv.org/html/2611.05979v1#Sx4.SSx5.p1.2) [S41](https://arxiv.org/html/2611.05979v1#Sx4.SSx6.p1.1) [S42](https://arxiv.org/html/2611.05979v1#Sx4.T2) [S43](https://arxiv.org/html/2611.05979v1#Sx4.T4) [S44](https://arxiv.org/html/2611.05979v1#Sx4.SSx10.p1.1) [S45](https://arxiv.org/html/2611.05979v1#Sx5.p1.1)

## 局限

真机使用基于模型的物体位姿跟踪，且每种手都调过控制参数。[S26](https://arxiv.org/html/2611.05979v1#Sx3.SSx4.p1.1)[S37](https://arxiv.org/html/2611.05979v1#Sx4.SSx4.p1.1) 我会核查新物体对运动预测器是未见的 [S33](https://arxiv.org/html/2611.05979v1#Sx4.SSx2.p1.1)，但在低层仿真训练中是否也完全留出，以及物体跟随奖励在铰接和避障任务上的独立贡献。

- **判断**：值得读到奖励公式与换手协议，最可借鉴的是把预测的物体运动变成逐步奖励，并看清仍需保留哪些人工约束。

## 研究关联

如果任务进度能从物体位姿读出，就可以先从示范学一条物体参考，再让仿真中的机器人自己试出合适的手指动作。换硬件时，优先复用物体侧的目标，比照搬旧手的关节轨迹更符合这个方法的分工。

### 下一步读哪里

对照 [S15](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.1) [S16](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.2) [S17](https://arxiv.org/html/2611.05979v1#Sx3.SSx2.p2.2) 看如何从人手轨迹得到机器人参考，再逐项读 [S20](https://arxiv.org/html/2611.05979v1#Sx3.Ex8) [S21](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p5.1) [S22](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p6.1) [S23](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p7.1) [S24](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p8.1) [S25](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p9.1) 的奖励。查 [S42](https://arxiv.org/html/2611.05979v1#Sx4.T2) [S43](https://arxiv.org/html/2611.05979v1#Sx4.T4) [S44](https://arxiv.org/html/2611.05979v1#Sx4.SSx10.p1.1) 指向的结果，分别核对仿真与真机差距，以及物体跟随带来的是更快学习、最终更高成功率，还是两者都有。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.05979v1
- 获取时间：2026-11-06T00:08:05.170803+00:00
- [S1] [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation · 正文段落 1](https://arxiv.org/html/2611.05979v1#abstract1.1)
- [S2] [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation · 正文段落 2](https://arxiv.org/html/2611.05979v1#p1.1)
- [S3] [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation · 正文段落 3](https://arxiv.org/html/2611.05979v1#p1.2)
- [S4] [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation · 正文段落 4](https://arxiv.org/html/2611.05979v1#p2.1)
- [S5] [Introduction · 正文段落 5](https://arxiv.org/html/2611.05979v1#Sx1.p1.1)
- [S6] [Introduction · 正文段落 6](https://arxiv.org/html/2611.05979v1#Sx1.p2.1)
- [S7] [Introduction · 正文段落 7](https://arxiv.org/html/2611.05979v1#Sx1.p3.1)
- [S8] [Introduction · 正文段落 10](https://arxiv.org/html/2611.05979v1#Sx1.I1.i3)
- [S9] [Introduction · 正文段落 11](https://arxiv.org/html/2611.05979v1#Sx1.F1)
- [S10] [Dexterous Manipulation · 正文段落 13](https://arxiv.org/html/2611.05979v1#Sx2.SSx1.p1.1)
- [S11] [Learning Dexterous Manipulation from Human · 正文段落 14](https://arxiv.org/html/2611.05979v1#Sx2.SSx2.p1.1)
- [S12] [Learning Dexterous Manipulation from Human · 正文段落 15](https://arxiv.org/html/2611.05979v1#Sx2.SSx2.p2.1)
- [S13] [Learning Dexterous Manipulation from Human · 正文段落 16](https://arxiv.org/html/2611.05979v1#Sx2.SSx2.p3.1)
- [S14] [Methods · 正文段落 17](https://arxiv.org/html/2611.05979v1#Sx3.p1.1)
- [S15] [Hand-Object Poses Prediction · 正文段落 18](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.1)
- [S16] [Hand-Object Poses Prediction · 正文段落 20](https://arxiv.org/html/2611.05979v1#Sx3.SSx1.p1.2)
- [S17] [Robot-Object Trajectories Extraction · 正文段落 30](https://arxiv.org/html/2611.05979v1#Sx3.SSx2.p2.2)
- [S18] [Trajectory-Guided Reinforcement Learning · 正文段落 32](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p2.1)
- [S19] [Trajectory-Guided Reinforcement Learning · 正文段落 34](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p2.2)
- [S20] [Trajectory-Guided Reinforcement Learning · 正文段落 37](https://arxiv.org/html/2611.05979v1#Sx3.Ex8)
- [S21] [Trajectory-Guided Reinforcement Learning · 正文段落 39](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p5.1)
- [S22] [Trajectory-Guided Reinforcement Learning · 正文段落 40](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p6.1)
- [S23] [Trajectory-Guided Reinforcement Learning · 正文段落 43](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p7.1)
- [S24] [Trajectory-Guided Reinforcement Learning · 正文段落 44](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p8.1)
- [S25] [Trajectory-Guided Reinforcement Learning · 正文段落 45](https://arxiv.org/html/2611.05979v1#Sx3.SSx3.p9.1)
- [S26] [Sim-to-Real Transfer · 正文段落 46](https://arxiv.org/html/2611.05979v1#Sx3.SSx4.p1.1)
- [S27] [Sim-to-Real Transfer · 正文段落 47](https://arxiv.org/html/2611.05979v1#Sx3.F3)
- [S28] [Experiment Setting · 正文段落 48](https://arxiv.org/html/2611.05979v1#Sx4.SSx1.p1.1)
- [S29] [Experiment Setting · 正文段落 49](https://arxiv.org/html/2611.05979v1#Sx4.I2.i1)
- [S30] [Experiment Setting · 正文段落 50](https://arxiv.org/html/2611.05979v1#Sx4.I2.i2)
- [S31] [Experiment Setting · 正文段落 51](https://arxiv.org/html/2611.05979v1#Sx4.I2.i3)
- [S32] [Experiment Setting · 正文段落 52](https://arxiv.org/html/2611.05979v1#Sx4.I2.i4)
- [S33] [Abbreviation: · 正文段落 53](https://arxiv.org/html/2611.05979v1#Sx4.SSx2.p1.1)
- [S34] [Simulation Configuration · 正文段落 54](https://arxiv.org/html/2611.05979v1#Sx4.SSx3.p1.1)
- [S35] [Simulation Configuration · 正文段落 55](https://arxiv.org/html/2611.05979v1#Sx4.T1.1)
- [S36] [Simulation Configuration · 正文段落 56](https://arxiv.org/html/2611.05979v1#Sx4.T1)
- [S37] [Real-World Robot Setup · 正文段落 57](https://arxiv.org/html/2611.05979v1#Sx4.SSx4.p1.1)
- [S38] [Baselines · 正文段落 58](https://arxiv.org/html/2611.05979v1#Sx4.SSx5.p1.1)
- [S39] [Baselines · 正文段落 59](https://arxiv.org/html/2611.05979v1#Sx4.Ex10)
- [S40] [Baselines · 正文段落 60](https://arxiv.org/html/2611.05979v1#Sx4.SSx5.p1.2)
- [S41] [YCB Object Grasping · 正文段落 61](https://arxiv.org/html/2611.05979v1#Sx4.SSx6.p1.1)
- [S42] [YCB Object Grasping · 正文段落 63](https://arxiv.org/html/2611.05979v1#Sx4.T2)
- [S43] [YCB Object Grasping · 正文段落 67](https://arxiv.org/html/2611.05979v1#Sx4.T4)
- [S44] [Ablation Study on the Reward Design · 正文段落 73](https://arxiv.org/html/2611.05979v1#Sx4.SSx10.p1.1)
- [S45] [Conclusion · 正文段落 74](https://arxiv.org/html/2611.05979v1#Sx5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Manipulating diverse objects with multi-fingered dexterous hands is challenging due to the high dimensionality and complex dynamics. Human-Object Interaction (HOI) datasets provide rich knowledge about task information and embodied interactions. Instead of solely imitating the human demonstrations, our method learns to holistically predict future hand-object states by leveraging these datasets. The predicted future states of the object can serve as a general-purpose reward term for reinforcement learning, reducing reliance on task-specific reward engineering and enhancing generalization across tasks. We conduct extensive experiments on three manipulation tasks in simulation and the real world. Our approach outperforms existing SOTA methods in both success rate and generalizability on novel objects. Furthermore, we validate the cross-embodiment compatibility of our methods by successfully deploying the skills on different robot hands.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.05979v1
- Authors: Zhengdong Hong, Guofeng Zhang
- Published: 2026-11-04T05:13:03Z
- Age days: 1

</details>
