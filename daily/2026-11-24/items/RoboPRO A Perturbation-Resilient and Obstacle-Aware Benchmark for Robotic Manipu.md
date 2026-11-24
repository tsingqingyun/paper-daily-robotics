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
url: "https://arxiv.org/abs/2611.26971v1"
published: "2026-11-20T01:47:52Z"
age_days: 4
score: 32
created: 2026-11-24
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RoboPRO: A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboPRO 把双臂操作放进有杂物和扰动的室内场景，除了看任务成没成，还记录机器人有没有发生不安全接触。它通过分因素比较，帮助定位策略究竟怕杂物、指令变化，还是物体层面的变化。

## 问题

在干净桌面上拿到目标，只能说明策略在那种布置下完成了任务。换成拥挤台面，非目标物体既可能让策略认错，也可能挡住手臂的运动路径。只看成功率，完成任务却撞到旁边物体的情况会被掩盖，失败时也难以判断策略对哪种变化最敏感。

### 用一个例子理解

理解用例（非论文实验）。让双臂机器人把指定杯子放进托盘，先用原始布置和指令执行，再分别试着改写指令或在路线上放一个碗。每次都记录杯子是否入托盘，以及手臂是否碰碗。若两次都放对了，接触记录仍能区分哪次执行更稳妥。

## 创新点或方法

RoboPRO 设置从只有目标物体到非目标物体密集摆放的场景，并在不同杂物密度下按因素分析视觉、语言和物体层面的扰动。评测保留任务成功率，同时增加两种接触事件指标，追踪机器人与环境或非目标物体之间的不安全接触。基准提供示范和语言指令。策略在评测时执行任务，由基准记录结果与接触。摘要未给出各参评策略怎样使用示范或是否统一重训。

### 方法如何工作

1. 为同类操作设置不同的非目标物体密度，使策略在空旷和拥挤条件下都要完成任务。
2. 在各密度下按视觉、语言和物体因素评测，观察同一类操作对不同条件变化的敏感程度。
3. 执行时同时记录任务结果和两种接触事件，区分完成任务与执行过程中的碰撞。
4. 按扰动因素、杂物密度和训练数据设置比较成绩，定位哪些条件与成功下降或碰撞增加一起出现。

### 必要术语

- 非目标物体：当前指令未要求操作的物体；它们可以干扰识别，也可以限制手臂可走的路线。
- 分因素评测：按输入或场景变化的类型分别比较结果；RoboPRO 用它定位策略对哪种扰动敏感。
- 接触事件指标：记录符合判定条件的机器人接触；这里用于补充任务成功率。

## 证据

摘要列出四个布置家具的室内环境、80 项双臂原子与组合任务、16,000 条示范和约 5,600 条指令。作者评估了多种先进操作策略，报告杂物会降低成功率并增加非目标碰撞，不同扰动影响也不同，训练数据构成与表现有关。摘要未列策略名、分条件降幅或碰撞定义，也未交代实验载体属于仿真还是真机。

## 局限

作者指出杂物同时带来视觉干扰和操作空间受限。单看高密度场景成功率下降，无法确定哪条路径导致失败。我会核查实验是否分别控制可见杂物和运动障碍，以及接触指标怎样处理任务所需的正常接触。

- **判断**：值得读到扰动协议和接触指标定义，只有弄清每次改了什么、怎样算碰撞，分项结果才有诊断意义。

## 研究关联

可以把测试设计成先复现基准条件，再逐项改变输入或场景，并同时记录成功与接触。这样能区分完成任务却撞到东西、换种说法后做错目标、加入障碍后无法完成等不同失效，缩小下一步要查的范围。

### 下一步读哪里

先查两种接触指标的触发条件，再看不同密度与扰动之下成功率和碰撞是否一起变化。涉及训练配方时，核查各数据设置是否匹配训练量，评测是否保持在相同条件下。

- **概念**：智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/RoboPRO A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipu.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object manipulation in the real world requires robotic policies to be robust to contextual perturbations and capable of safe planning in cluttered scenes. However, the majority of existing robotics benchmarks contain clean tabletop environments with success rate as the sole metric, leaving two critical deployment questions unanswered: does the policy manipulate safely under real conditions and what does lead to its failure? To this end, we present RoboPRO, a Robotics benchmark for Perturbation-Resilient and Obstacle-aware planning, which unifies various axes of robustness in manipulation. RoboPRO comprises 80 diverse bimanual atomic and compositional tasks across four furnished indoor environments, with a total of 16,000 demonstrations and 5.6K diverse language instructions. The scenes are populated with different numbers of distractors (non-targets), ranging from clean, involving only target objects, to densely populated to impose both visual and operational clutter. Moreover, we propose two safety-aware event metrics to determine unsafe contact between the robot and the environment or distractors. Our evaluation protocol consists of a per-factor analysis of three key perturbations, namely visual, linguistic, and object-level, with different levels of distractor densities. We conduct extensive experiments on RoboPRO using state-of-the-art manipulation policies to analyze the impact of visual and operational clutter, perturbations, and instructional diversity. Our findings indicate clutter can drastically reduce success and increase non-target collision, different perturbations have different effects on the performance, and that training data composition affects overall performance. Our findings highlight the key challenges for manipulation in real-world conditions and motivate future research in this domain. Project page: https://robopro-bench.github.io/RoboPRO/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.26971v1
- Authors: Zhiyuan Li, Charles Eret, Dingsheng Liu, Xuan Zhao, Joshua Choi, Yangzheng Wu, Tongtong Cao, Yingxue Zhang, Amir Rasouli
- Published: 2026-11-20T01:47:52Z
- Age days: 4

</details>
