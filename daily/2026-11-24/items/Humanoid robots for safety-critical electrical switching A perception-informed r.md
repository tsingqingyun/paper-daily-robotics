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
url: "https://arxiv.org/abs/2611.27845v1"
published: "2026-11-20T16:58:59Z"
age_days: 3
score: 26
created: 2026-11-24
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇把运行时约束滤波器加在 VR 操作指令和人形机器人之间，专门防止工具误碰邻近的非目标开关。它根据头部相机估计的场景检查每条指令，安全指令原样通过。

## 问题

遥操作员要让手持工具接触指定开关，旁边可能紧挨着外观相似的设备。即使操作员选对目标，手部指令的偏差也可能让工具碰到另一只开关。控制器既要保留到达目标的动作空间，又要限制朝错误设备靠近的动作。

### 用一个例子理解

理解用例（非论文实验）：面板上两只开关并排，任务是拨左边。相机给出两只开关的位置，操作者的一条指令却让工具向右偏。滤波器检查这条指令并修正偏移，输出一条满足右侧避让约束的动作。操作员随后给出的安全指令可以直接通过。

## 创新点或方法

直接遥操作会把操作者的动作指令交给机器人执行。本文先用头部相机估计场景，再根据当前目标确定哪个开关要避开，把这一要求写成控制屏障函数约束，由二次规划在执行前检查并修正指令。安全指令保留原样。摘要描述的是在线过程，视觉场景估计如何训练、目标如何指定，以及优化不可行时如何处理均未说明。

### 方法如何工作

1. 从头部相机估计开关场景，为工具与开关之间的避让检查提供位置依据。
2. 根据当前指定目标识别需要避开的开关，让工具仍可接触任务指定对象。
3. 把避让要求写成控制屏障函数约束，在执行每条遥操作指令前交给二次规划检查。
4. 原样传递满足约束的指令，修正会违反约束的指令，再把结果交给机器人执行。

### 必要术语

- 控制屏障函数：用状态和动作表达系统应如何留在安全区域；文中用于约束工具避开非目标开关。
- 二次规划：在约束下优化动作指令的计算方法；这里负责保留安全指令，并在需要时修正指令。

## 证据

摘要报告，Unitree G1 真机在两个站位各做六轮，其中目标保持不变的十轮全部成功，且无非目标开关动作。摘要未交代另外两轮的结果。仿真以安全完成为指标，滤波后为 9/9，直接遥操作为 5/9。仿真有直接对照，所述真机结果支持固定目标条件下的可行性，摘要未给出真机直接遥操作对照。

## 局限

作者把真机的十轮成功限定在目标保持不变的轮次。我会核查目标切换时约束何时更新，以及定位误差和工具跟踪误差怎样计入安全距离。仿真的组间差异能说明所测条件下滤波器有帮助，实际设备上的可靠性仍取决于这些误差和控制执行情况。

- **判断**：值得读到约束怎么写、感知误差怎么处理，以及十二轮真机试验各自发生了什么，才能判断方法适用的操作条件。

## 研究关联

若任务必须接触一个物体，同时避开紧邻的另一个物体，把避让约束绑定到当前选中的目标，可以保留操作者的大部分控制权，让系统集中处理容易造成误操作的那部分指令。

### 下一步读哪里

先核查约束采用工具上的点还是完整几何、何时更新场景和目标，以及求解失败时机器人的行为。再按轮查看真机记录，确认目标切换轮次和仿真成功判据。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/Humanoid robots for safety-critical electrical switching A perception-informed r.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch. This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of a humanoid robot. The filter integrates a scene model estimated from the robot head camera and a target-conditioned control barrier function quadratic program that keeps the tool away from the non-target switch while passing safe commands unchanged. In real-world experiments on a Unitree G1 humanoid robot, with six rounds at each of two standing positions, target operations succeed in all ten rounds with an unchanged target and no non-target actuation. A simulation study achieves 9/9 safe completions, compared with 5/9 for raw teleoperation, demonstrating the feasibility of the method for humanoid switching operations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27845v1
- Authors: Songyang Liu, Yu Hou, Yuqing Hu, Shuai Li
- Published: 2026-11-20T16:58:59Z
- Age days: 3

</details>
