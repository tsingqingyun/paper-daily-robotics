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
url: "https://arxiv.org/abs/2602.16705"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-16
concepts: ["智能体 Agent", "Sim2Real"]
---

# HERO: Learning Humanoid End-Effector Control for Visual Whole-Body Open-Vocabulary Object Grasping

> [!summary] 这篇论文到底做了什么（基于摘要）
> HERO 把“看懂要抓什么”和“让手准确到位”分开解决：大视觉模型负责场景理解，仿真训练的控制策略负责身体与手的运动。关键是结合逆运动学、学习到的前向模型和目标重规划，持续处理末端到位误差。

## 问题

人形机器人从 RGB-D 等视觉输入抓取日常物体，既要找到目标，也要协调身体把手送到合适位置。摘要认为，把场景理解和精确末端控制一起端到端学习，会让模仿学习与仿真迁移方法难以扩展；识别能力和控制精度被绑在同一学习问题里。

### 用一个例子理解

理解用例（非论文实验）：输入咖啡桌的 RGB-D 图像和“拿起苹果”；视觉侧确定目标位置，HERO 将末端目标转成身体与手臂参考运动，并调整到位偏差，最终输出用于接近和抓取的控制动作。

## 创新点或方法

旧做法联合学习感知与动作；本文把视觉理解交给大视觉模型，把准确跟踪末端目标交给 HERO。控制侧用逆运动学将剩余末端目标转成参考轨迹，再结合学习到的神经前向模型、目标调整和重规划。可以理解为：先算怎样到位，再处理实际运动与目标之间的差距。控制策略通过仿真训练，部署时接收视觉侧目标并执行控制；前向模型的训练数据、残差定义及各模块调用顺序未在摘要展开。

### 方法如何工作

1. 视觉侧理解场景和指定物体，形成控制侧可使用的目标，避免控制策略同时承担全部语义理解。
2. 逆运动学将剩余末端目标转成参考轨迹，为身体与手臂提供可跟踪的运动依据。
3. 结合神经前向模型、目标调整与重规划处理到位偏差；各模块精确接口，摘要只说明到此。
4. 训练好的控制策略在真实场景执行运动，再通过模块与整体测试检查控制精度和抓取效果。

### 必要术语

- 末端执行器：机器人与物体接触的手或工具；本文主要衡量它能否准确到达目标。
- 逆运动学：从手的目标位置反求关节运动；本文用它构造参考轨迹。
- 前向运动学：从机器人状态推算手的位置；本文加入学习到的模型以改善这一估计。

## 证据

摘要报告末端跟踪误差为 2.44 厘米，相对最强既有方法有 5.5 倍改善，但没有列出对手名称、误差聚合方式或这一数字来自仿真还是真机。完整系统在办公室、咖啡店等真实环境抓取杯子、苹果和玩具，物体所在表面高度为 43—92 厘米。摘要称做了模块与端到端测试，却未给抓取成功率和试验次数，因此不能把跟踪误差直接换算为抓取可靠性。

## 局限

2.44 厘米是否足够，取决于物体尺寸和抓取容差；杯子与细小物体不能据此等同判断。需要核查遮挡、视觉定位误差和动态扰动下的表现；现有材料也不能说明哪些改善分别由三个控制改动带来。

- **判断**：值得读控制细节和模块消融，重点看残差如何进入参考轨迹，以及精度提升是否确实转化为真机抓取收益。

## 研究关联

这里值得借鉴的是按误差来源拆任务：视觉负责决定手应该去哪，控制负责把它送到那里。若主要困难是身体协调与末端偏差，先改善可单独测量的跟踪能力，可能比扩大整套端到端模型更容易定位问题。

### 下一步读哪里

下一步核查残差的坐标系、神经前向模型预测什么、重规划触发条件，以及跟踪误差的测量环境；再检查真机成功率是否按物体、表面高度和场景分别报告。输入没有正文节选。

- **概念**：智能体 Agent Sim2Real
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/HERO Learning Humanoid End-Effector Control for Visual Whole-Body Open-Vocabular.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2602.16705v4 Announce Type: replace Abstract: Visual loco-manipulation of arbitrary in-the-wild objects requires accurate end-effector (EE) control and a generalizable understanding of the scene from visual inputs (eg, RGB-D images). Existing imitation and sim2real methods jointly learn both these aspects via monolithic end-to-end learning and are thus hard to scale. In this work, we bring to bear the best tools for each of these problems -- large vision models for generalizable scene understanding and simulated training for accurate EE control -- leading to an overall modular loco-manipulation system that exhibits strong generalization. Our core technical innovation is HERO, an accurate residual-aware EE tracking policy made possible by combining classical robotics with machine learning. It uses a) inverse kinematics to convert residual end-effector targets into reference trajectories, b) a learned neural forward model for accurate forward kinematics, and c) goal adjustment and replanning. Together, these innovations reduce the end-effector tracking error to 2.44cm, outperforming the strongest prior method by 5.5x. Our overall system operates in diverse real-world environments, from offices to coffee shops, where the robot reliably grasps various everyday objects (eg, mugs, apples, toys) on surfaces ranging from 43cm to 92cm in height. Systematic modular and end-to-end tests demonstrate the effectiveness of our proposed design. We believe our advances open up new ways of training humanoids to interact with daily objects. Project page: https://hero-humanoid.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2602.16705
- Authors: Runpei Dong, Ziyan Li, Arjun Gupta, Xialin He, Saurabh Gupta
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
