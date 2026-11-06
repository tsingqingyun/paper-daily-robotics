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
url: "https://arxiv.org/abs/2611.05244v2"
published: "2026-11-03T17:26:56Z"
age_days: 2
score: 29
created: 2026-11-06
concepts: ["世界模型"]
---

# Reality and Perceptual Gaps in Expressive Swarm Robotics

> [!summary] 这篇论文到底做了什么（基于摘要）
> Swarm Gaps 把同一套分散式协调代码放到三类真机上演出，分别看机器人怎么动，以及观众怎么看。代码都能可靠运行，但换了实体平台，运动节奏和路径会变，观众能否读懂动作意图和看起来是否安心也可能各自变化。

## 问题

把群体控制搬到真机时，小小的硬件、时序和通信差异会经由机器人之间的互动放大。到了有人观看的场合，还有一道问题：机器人可以顺利完成协调，观众却可能读不出它们在做什么，或者对动作感到威胁。只验收控制是否稳定，会漏掉这部分使用效果。

### 用一个例子理解

理解用例（非论文实验）。让一组桌面机器人和一组飞行机器人用相同规则先散开再聚拢。输入是各机可用的局部状态，规则让它们逐步调整运动，输出是两组各自可见的队形变化。演出后分别问观众看出了什么意图、看时感到多自在，再把这两种回答与运动记录对照。

## 创新点或方法

研究把代码作为共同参照，在桌面机器人、飞行机器人和人类尺度的移动操作机器人上运行，观察换了实体平台后群体运动怎样变化。再用现场观众问卷把两个判断分开记录，一个是观众觉得动作有什么目的，一个是他们感觉舒适还是受威胁。研究比较的是运行和观看结果。摘要描述的是执行既有代码，未涉及模型训练或推理流程。

### 方法如何工作

1. 在三类实体机器人上运行相同协调代码，为比较平台差异保留共同参照。
2. 比较执行节奏和轨迹形状，检查可靠运行时可见动作还能发生多大变化。
3. 分别收集观众对动作目的和情绪感受的回答，判断两项是否随平台同步变化。

### 必要术语

- 现实差距：控制在仿真和物理系统中的表现差异；文中以它说明实体执行为何需要单独核验。
- 感知差距：机器人实际做出的动作与观众感知到的内容之间的差距；文中用它区分执行表现与观看结果。
- 分散式协调：各机器人按分布在群体中的规则协调运动；同一套规则为跨平台比较提供参照。

## 证据

摘要报告，同一协调算法在三种真机上都可靠运行，但动作执行的时间尺度相差超过 3 倍，轨迹几何也发生变化。观众问卷显示，目的归因和舒适或威胁感随实体平台而异，两者没有同步变化。摘要未给出时间尺度的计算口径、问卷样本量、各平台评分或统计检验。结果支持在这些演出条件下把执行可靠、意图可读和情绪感受分开看。

## 局限

摘要的证据来自现场真机演出，未给出成对的仿真和真机数据，无法据此估计仿真偏差。我会核查观众是否看到可比的编排、距离和速度，以及问卷是否控制了观看条件。共享代码提供了比较起点，但平台形态、实际运动和表演条件可能同时变化，摘要无法单独识别哪项导致了观众反应。

- **判断**：值得读到跨平台比较和问卷设计，尤其要看不同平台究竟共享了哪些条件，以及目的判断和情绪反应是怎样分别测量的。

## 研究关联

面向观众设计群体运动时，可以把‘看得懂它在干什么’和‘看着是否安心’设成两个验收项。只收一项总体满意度，会把两个可能朝不同方向变化的结果揉在一起。

### 下一步读哪里

先核查相同代码在各平台如何映射到实际运动，再看时间尺度、轨迹形状如何度量。问卷部分重点查题目措辞、观众分组和观看条件，以及平台差异是否与编排差异一同出现。

- **概念**：世界模型
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/Reality and Perceptual Gaps in Expressive Swarm Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Moving robot swarms from simulation into the physical world can be difficult because small discrepancies in hardware, timing and communication can cascade across interacting robots and alter group behaviour. This challenge is known as the reality gap. When swarms operate in human environments, a second challenge emerges: a perceptual gap between what the swarm physically does and what human onlookers actually perceive. This study examines the same decentralised coordination code deployed across three robotic swarms-tabletop, aerial and human-scale mobile manipulators-during live artistic performances. We find that while the underlying algorithms executed reliably on all three platforms, physical embodiment drastically altered visible motion-distorting execution timescales by more than a factor of three and reshaping trajectory geometry. More importantly, audience surveys revealed that human interpretation does not mirror technical success: how observers attribute meaning (perceived purpose) and how they react emotionally (comfort versus threat) depend heavily on physical form. Meaning attribution and emotional responses did not vary together. Our results demonstrate that successfully transferring swarm software to physical hardware is insufficient for real-world deployment. Addressing the reality gap does not guarantee that the resulting collective motion will be readily interpreted by human observers. Swarms destined for human environments must be engineered not only for decentralised stability but also for the expressive physical dynamics through which humans interpret collective motion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.05244v2
- Authors: Ali Imran, Abdalwhab Bakheet Mohammed Abdalwhab, Rafael Gomes Braga, Hélène Duval, Audrey Rochette, Vivek Shankar Varadharajan, Yann Bouteiller, Jean Mazerolle, Giovanni Beltrame, David St-Onge
- Published: 2026-11-03T17:26:56Z
- Age days: 2

</details>
