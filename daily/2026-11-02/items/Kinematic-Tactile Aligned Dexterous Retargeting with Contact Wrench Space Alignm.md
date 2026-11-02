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
url: "https://arxiv.org/abs/2610.39582v1"
published: "2026-10-29T08:23:58Z"
age_days: 3
score: 27
created: 2026-11-02
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇不只把人的手势转换成机器人手势，还要传递“这样接触能对物体施加哪些力和力矩”。它用接触力旋量空间对齐两种手的受力能力，再把所需指尖力转换为可回放的关节位置修正。

## 问题

任务是把人类灵巧操作示范迁移到机器人手。只对齐关节和接触位置，可能得到外形相似却拿不稳的动作，因为两种手的结构和接触力不同。摘要指出，现有重定向主要传递运动学，往往没有保留支撑物理交互的触觉信息。

### 用一个例子理解

理解用例（非论文实验）：输入人手握杯倒水时的姿态、接触位置和触觉力；方法先生成机器人握姿，再计算支撑杯子及抵抗翻转所需的指尖力，转换成关节位置修正，输出可回放的倒水轨迹。

## 创新点或方法

旧做法重点匹配手如何运动；本文再匹配物体如何受力。先对齐手部运动和接触几何，再利用人手触觉力与接触位置构建受力支持描述，最后优化机器人指尖力，使其覆盖人手的支持范围，并转成关节位置修正。摘要描述的是示范转换与轨迹回放，没有说明另行训练操作策略；力到位置的转换模型、回放时是否使用在线触觉反馈也未说明。

### 方法如何工作

1. 对齐人手与机器人手的运动和接触几何，建立对应的抓持轨迹。
2. 结合人手触觉力与接触位置，描述物体受到的力和力矩支持。
3. 优化机器人指尖力，使不同手型也能覆盖相应受力需求。
4. 将力目标转换成关节位置修正，生成可直接回放的轨迹；具体转换细节未说明。

### 必要术语

- 重定向：把一种身体结构的示范转换给另一种结构；本文从人手转给机器人手。
- 接触力旋量：把作用于物体的力与力矩一起表示；连接接触和物体稳定性。
- 受力支持描述：概括接触能够提供的力与力矩支持；作为两种手对齐的目标。
- 运动学对齐：匹配姿态、位置及运动关系；提供受力修正之前的基础轨迹。

## 证据

摘要报告在三种倾倒条件下进行仿真与真机实验，真机回放成功率为 96.7%，受力传递保真度高于代表性重定向基线。但未提供试验次数、基线名称与数值、保真度公式或三种条件的具体区别。因此证据支持受测倾倒条件下的轨迹迁移，尚不能证明任意灵巧任务的迁移能力。

## 局限

受力支持覆盖得更好，不必然意味着接触全过程都稳定。我会核查摩擦、滑动、触觉误差和执行器限制如何进入优化，以及成功率收益是否主要来自新增力信息；摘要未提供足以分离这些因素的结果。

- **判断**：值得深入读受力表示、优化约束和力到位置的转换，因为这三处决定它能否从物理上解释并修正重定向失败。

## 研究关联

这里值得借鉴的是把跨手型迁移的共同目标放在物体上：不同手不必复刻相同关节姿态，却可能需要提供相近的支撑力和抗转动能力。这给“动作看起来相似但执行失败”提供了一个具体检查方向。

### 下一步读哪里

优先核查 wrench support 的数学定义、“覆盖”的优化目标、接触与摩擦约束，以及力目标怎样变为位置命令。实验部分需确认各倾倒条件、失败定义及触觉对齐的独立贡献。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignm.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human demonstrations provide a natural and scalable source of data for learning dexterous manipulation policies. However, existing retargeting methods primarily transfer human kinematics, while the tactile information underlying physical interaction is rarely preserved across embodiments. To address this limitation, we present a hierarchical three-stage framework for kinematic-tactile aligned dexterous retargeting. We use object-centric contact wrench space as a physical representation for tactile alignment between human and robot hands. The framework first aligns hand kinematics and contact geometry, and then constructs a human wrench support profile from tactile forces and contact geometry. Robot fingertip force targets are subsequently optimized to cover the human wrench support and converted into joint position corrections, yielding directly replayable robot hand trajectories. We evaluate the framework in simulation and real robot experiments across three pouring conditions. In the real robot experiments, our method achieves a 96.7\% replay success rate and higher wrench transfer fidelity than representative retargeting baselines. The framework enables physically grounded transfer of kinematic and tactile information from human demonstrations to robot hands, providing a path toward scalable learning of contact-rich dexterous manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39582v1
- Authors: Xinyuan He, Ziheng Xu, Yueyuan Chen, Yufan Ye, Yuanshuo Tan, Huiming Pan, Jianjun Meng, Shuo Jiang, Peter B. Shull
- Published: 2026-10-29T08:23:58Z
- Age days: 3

</details>
