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
url: "https://arxiv.org/abs/2610.09479v1"
published: "2026-10-07T05:34:26Z"
age_days: 0
score: 29
created: 2026-10-08
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control

> [!summary] 这篇论文到底做了什么（基于摘要）
> ResGAC 要让人形机器人身体运动时，手仍准确跟踪指定位置和朝向。它用几何导纳控制给出基础手臂目标，再用残差强化学习补偿动力学影响，并减少骨盆晃动对手部参考目标的污染。

## 问题

具体任务是人形机器人全身运动中的末端位姿跟踪。浮动基座晃动、重力、关节间耦合和下肢运动都会扰动手；此外，若手的目标依附骨盆坐标系，骨盆倾斜或上下起伏还会让目标本身跟着动。摘要没有逐项解释既有控制器的缺陷，但给出了这些实际干扰来源。

### 用一个例子理解

理解用例（非论文实验）：机器人下肢调整姿态，右手需要保持一个指定世界位姿。输入手部目标和当前状态，GAC 生成基础手臂关节目标，残差策略补偿身体运动影响，输出全身关节位置指令；参考系选择减少不需要的骨盆晃动进入操作目标。

## 创新点或方法

ResGAC 把控制拆成有结构的反馈和学习补偿：GAC 根据手部位姿误差生成名义手臂关节位置目标，残差 RL 在共享的关节位置动作空间补偿未建模动力学，并协调移动与平衡。其几何写法允许同一控制律用于不同操作参考系，因此可以选用贴地的航向坐标系：保留平面移动，去掉骨盆滚转、俯仰和上下起伏。训练阶段如何采样运动、设置奖励和迁移到真机，摘要未说明；执行时两部分共同产生关节目标。

### 方法如何工作

1. 在选定操作参考系中表达目标与当前末端位姿，得到控制需要纠正的几何误差。
2. GAC 将反馈转为名义手臂关节位置目标，为学习部分提供有结构的基础动作。
3. 残差 RL 在共享动作空间补偿未建模影响并协调平衡，使手臂跟踪与下肢运动可以共同执行。
4. 采用贴地航向参考系保留平面运动、排除骨盆倾斜和起伏，减少参考目标本身的额外运动。

### 必要术语

- SE(3) 位姿：三维位置和朝向的组合；本文同时跟踪这两部分。
- 几何导纳控制：在位姿几何上把误差反馈转为运动目标；本文用它产生基础手臂指令。
- 残差强化学习：学习基础指令之外的补偿；本文用来处理未建模动力学并协调全身。
- 左不变表述：一种可跨参考系使用的几何误差写法；本文据此复用同一 GAC 控制律。

## 证据

摘要报告在真实 Unitree G1 上验证：四项站立末端跟踪测试中，平移和旋转误差均优于包括 SONIC 在内的代表性基线，但未给误差数值。站立插孔任务成功率为 90%，SONIC 为 50%（均来自摘要）；另有真机实验展示参考系减少骨盆运动向期望末端位姿的传播，以及下肢运动时的世界坐标系跟踪。试验次数和统计波动未给出。

## 局限

真机结果支持所测跟踪和插孔条件，但摘要没有提供行走速度、负载、外部接触强度等范围。我的待核查问题是参考系、GAC 和残差学习分别贡献多少，以及成功率差异在多少次试验上得到。

- **判断**：值得细读参考系定义和组件消融，因为这篇最有操作性的启示，是把目标随身体晃动的问题与执行补偿问题分别处理。

## 研究关联

这里最值得借鉴的是先检查目标定义：跟踪不好可能既来自执行误差，也来自参考系把身体晃动写进了手的目标。选择参考系与改进控制器应当一起考虑，尤其在移动底座上执行精细操作时。

### 下一步读哪里

核查贴地航向坐标系的精确定义、世界目标如何换算、残差作用于哪些关节，以及训练与部署条件；再看四项跟踪测试的误差分布和插孔试验次数。当前没有正文节选可定位。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Precise end-effector tracking during humanoid whole-body motion is challenging due to floating-base oscillations, gravity, dynamic coupling, and locomotion-induced disturbances. We propose ResGAC, a whole-body humanoid controller for precise end-effector pose tracking that combines geometric admittance control (GAC) with residual reinforcement learning. GAC provides structured $\SE$ task-space feedback and generates nominal arm joint-position targets, while residual RL compensates for unmodeled dynamics and coordinates locomotion and balance in the shared joint-position action space. The left-invariant geometric formulation allows the same GAC law to be used across manipulation reference frames. This enables the use of a ground-attached heading frame that preserves planar locomotion while removing pelvis roll, pitch, and heave from the manipulation reference, thereby reducing reference-induced end-effector motion during locomotion. ResGAC is validated on a real Unitree G1 humanoid. Across four standing end-effector tracking benchmarks, ResGAC consistently outperforms representative baselines, including SONIC, achieving lower translational and rotational errors. Real-world experiments further demonstrate reduced propagation of pelvis motion to the desired end-effector pose using the proposed ground-attached heading frame. ResGAC achieves $90\%$ success in a standing peg-in-hole task compared with $50\%$ for SONIC, and accurate world-frame $\SE$ end-effector pose tracking during lower-body motion. Experimental videos are included in the supplementary material and are also available on the project website: https://resgac.github.io/ResGAC-website/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09479v1
- Authors: Joohwan Seo, Xiaofeng Guo, Jinkun Cao, Roberto Horowitz, Rocky Duan, Guanya Shi, Koushil Sreenath
- Published: 2026-10-07T05:34:26Z
- Age days: 0

</details>
