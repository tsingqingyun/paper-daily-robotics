---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25696v1"
published: "2026-09-22T04:59:57Z"
age_days: 1
score: 31
created: 2026-09-24
concepts: ["AI 核心知识地图"]
---

# The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers

> [!summary] 先说人话（基于摘要）
> Cartesian Hand 用全直线运动的七自由度末端执行器，让一个夹具同时抓住物体的不同部分并产生相对运动，从而完成拧盖、按压等手内操作。

## 问题

多关节灵巧手功能丰富但机械和控制复杂，普通平行夹爪又很难在抓住物体后继续操作。处理螺纹、按压或转轴机构时，常需第二夹爪、外部夹具或机械臂协同。

## 创新点或方法

两个独立驱动的平行夹爪分别固定不同物体部分，四个平移指尖产生部件间相对运动。指尖运动学不随构型改变，使操作能够由简单线性运动基元组合。

## 证据

在实验室、制造和家庭场景的 35 个物体上演示开关盖、移液、泵压、双柄操作、拧螺丝、扳机触发和抓内重定向；相同操作流程从固定机械臂迁移到人形机器人，并演示双手实验室操作。摘要未给出成功率。

## 局限

它特别适配具有螺纹、转轴和直线机构的物体，35 个物体的展示不能等同于任意物体灵巧性；软件硬件开源在摘要中仍是计划。

- **判断**：值得从硬件与任务结构共同设计的角度细读，重点看适用机构范围和操作流程的可复用性。

## 研究关联

对具身智能研究者，实际价值来自硬件设计如何简化动作空间和操作程序；与多模态基础模型或学习算法的直接联系在摘要中较弱。

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/The Cartesian Hand In-Hand Manipulation with All-Linear Fingers.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation has increasingly pursued human-like dexterous hands with many articulated degrees of freedom, offering rich manipulation capabilities at the cost of mechanical and control complexity. At the other extreme, parallel grippers are simple and robust, but provide little ability to manipulate an object after grasping it. Operating articulated objects such as threaded containers, manufacturing tools, and laboratory instruments often requires a second gripper, an external fixture, or coordinated arm motion. We introduce the Cartesian Hand, a 7-DoF end-effector that rethinks dexterous manipulation by combining independent grasping and relative manipulation within a single end-effector using only linear motion. Two independently actuated parallel grippers hold different parts of an object, while four translating fingertips generate relative motion between the grasped parts. Its configuration-independent fingertip kinematics allow manipulation to be composed from simple linear motion primitives. The Cartesian Hand is particularly suited to objects structured around common mechanisms such as threads, pivots, linear guides, plungers, and triggers. We demonstrate cap opening and closing, pipetting, pumping, two-handle manipulation, screwdriving, trigger actuation, and in-grasp reorientation across 35 objects spanning laboratory, manufacturing, and household settings. The same manipulation procedures transfer from a fixed-base robot arm to a humanoid, where we demonstrate bimanual laboratory manipulation using two Cartesian Hands. These results show that versatile in-hand manipulation capability can emerge from a mechanically simple architecture when independent grasping and relative motion are designed directly into the end-effector. We will open-source all software and hardware design. Our website is https://generalroboticslab.com/cartesian_handv1.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25696v1
- Authors: Boxi Xia, Bokuan Li, Ryan Shin, Zijiang Yang, Jiaxun Liu, Boyuan Chen
- Published: 2026-09-22T04:59:57Z
- Age days: 1

</details>
