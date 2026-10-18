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
url: "https://arxiv.org/abs/2610.20998v1"
published: "2026-10-14T22:33:20Z"
age_days: 3
score: 26
created: 2026-10-18
concepts: ["智能体 Agent", "机器人学习"]
---

# MoCaP: Mobile Code-as-Policies for Zero-Shot Mobile Manipulation from Passive Human Videos

> [!summary] 这篇论文到底做了什么（基于摘要）
> MoCaP 从日常人类视频中提取“东西在哪里”和“人靠近后怎样准备操作”，帮助移动机器人找到既能到达、又方便机械臂动手的位置。它再结合实时观测，用闭环代码策略协调规划和工具调用，处理机器人自身的运动约束。

## 问题

移动操作不只是找到物体：机器人还得停在机械臂够得到、姿态允许操作的位置。人类视频没有为机器人标好这些信息，而且人的身体与机器人不同，照搬人的动作未必可行；真正需要转移的是空间线索和接近物体的方式。

### 用一个例子理解

理解用例（非论文实验）：输入一段人从厨房拿杯子的视频和机器人当前画面；系统从视频找出杯子所在区域及人靠近台面的方式，再按机械臂可达性检查候选站位；输出底座移动和取杯动作，并随新观测调整。

## 创新点或方法

相较于只凭当前观测寻找目标、决定站位，MoCaP 增加视频提供的空间记忆和人类接近先验，再由机器人自己的规划工具求解可行动作。视频负责提供方向，机器人几何与运动学约束负责筛选可执行方案；执行时持续结合观测调整。摘要没有说明是否另行训练策略、视频提取器如何训练，也没有展开代码生成与纠错细节。

### 方法如何工作

1. 从被动视频提取空间与交互准备线索，得到寻找目标和接近目标的参考，避免完全从当前视角开始搜索。
2. 结合实时观测使用空间记忆引导导航，使机器人接近可能的目标位置。
3. 利用人类接近线索搜索操作站位，再按机器人几何与运动学约束求解动作，处理身体差异。
4. 闭环代码策略协调规划和工具调用，根据执行中的观测继续决策；摘要只说明到此，未展开失败恢复机制。

### 必要术语

- 被动人类视频：未经机器人任务专门采集的日常活动录像；本文从中提取空间与接近线索。
- Code-as-Policy：用可执行代码组织决策和工具调用；本文用它协调导航与操作。
- 可达底座姿态：机器人停下后机械臂能够触及目标的位置与朝向；它连接导航成功和实际操作。

## 证据

摘要报告：在室内真机的两个移动操作任务上，各取得 80% 成功率，所比较的现有方法未能成功，但未给出方法名称和试验次数。视频空间记忆使物体导航成功率从 70% 到 100%；在一个不利起点，人类接近先验使找到可达底座姿态的比例从 0% 到 100%。这些结果支持所测场景中导航与站位线索有用，尚不能推到任意房间或操作任务。

## 局限

这些是真机结果，但任务种类和环境范围有限。我的待核查问题是：视频与执行环境有多接近，物体移动后记忆怎样更新，以及两项消融是否控制了其他条件；摘要不足以回答这些问题。

- **判断**：值得读方法与站位消融，重点看人类接近线索如何转成机器人可达姿态，这是比总成功率更值得复用的部分。

## 研究关联

值得借鉴的是把人类经验拆成机器人可使用的中间信息：物体位置用于找路，操作前的接近方式用于选站位。当人的动作无法直接映射到机器人时，仍可以转移“动手之前怎样布置身体与目标的关系”。

### 下一步读哪里

先核查空间记忆保存什么、接近先验如何表示，再看候选站位如何通过运动学检查。实验应检查两个任务的具体定义、重复次数、基线配置及失败原因；输入未提供正文节选。

- **概念**：智能体 Agent 机器人学习
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/MoCaP Mobile Code-as-Policies for Zero-Shot Mobile Manipulation from Passive Hum.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Passive human videos of everyday activity offer robots access to a massive amount of human experience without requiring a demonstration for each task. However, using this experience requires recovering knowledge from unstructured video recordings and adapting it to a different body (i.e., the robot). To overcome these challenges, we present mobile code-as-policy (MoCaP), an agentic framework that turns passive human video recordings into guidance for an end-to-end mobile manipulation policy. MoCaP extracts spatial memory and cues of how people prepare to interact with objects, which inform navigation and the search for a manipulation-ready configuration. Guided by passive human experience and current observations, MoCaP uses a closed-loop code-as-policy to coordinate planning and tool use primitives to solve motions under the robot's geometry and kinematic constraints. On a real mobile manipulator, MoCaP achieves 80% success on each of two mobile manipulation tasks in an indoor environment whereas existing approaches cannot succeed at the task. Video-derived spatial memory improves object-navigation success from 70% to 100%, and human approach prior raises the rate of finding a reachable base pose from 0% to 100% at an unfavorable start location. Videos and code are available on the project website: https://mocap-7.github.io/MoCAP-page/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.20998v1
- Authors: Yiyang Cai, Tatsuya Kamijo, Ninghao Lu, Zijin Hu, Sherry Yang
- Published: 2026-10-14T22:33:20Z
- Age days: 3

</details>
