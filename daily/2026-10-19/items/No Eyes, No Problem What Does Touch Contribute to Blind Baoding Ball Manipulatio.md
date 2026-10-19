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
url: "https://arxiv.org/abs/2610.23438v1"
published: "2026-10-16T13:22:03Z"
age_days: 3
score: 30
created: 2026-10-19
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这项工作让 Shadow Dexterous Hand Lite 不看物体，只靠关节感觉和二值触觉持续转动保定球。关键是让仿真中的手、触觉和动作限制更贴近硬件，并在训练中模拟传感器卡死等情况。

## 问题

任务是在真实灵巧手中持续转动双球，策略不能观察图像或物体状态。仿真强化学习能学出动作，但接触不断变化、运动引起触觉信息漂移，加上仿真与实物动力学不同，容易使策略落地后失效。

### 用一个例子理解

理解用例（非论文实验）：输入是手指关节状态和各触点的接触/未接触信号。策略据此连续输出手指动作，让双球交换位置；某个触点一直报接触时，期望训练中的故障扰动能帮助策略继续控制，但这一特定情景不能算作摘要已验证的结果。

## 创新点或方法

相较于仅在仿真中学会转球，本文同时处理手模型和观测可靠性：仿真体现传感器布局与机械耦合，配合触觉校准，并加入两种按回合变化的域随机化——动作变化速率限制、触觉单元固定值故障。训练用强化学习；部署时策略只接收本体感觉和二值触觉，摘要称实现零样本迁移，但未说明奖励、网络或各项扰动的参数。

### 方法如何工作

1. 建立与实体手传感器和机械耦合相符的仿真，减少策略利用硬件不存在的自由度或信号。
2. 校准触觉，并在训练回合中改变动作速率限制和触觉单元状态，让策略接触不理想条件。
3. 用强化学习得到从本体感觉、二值触觉到手部动作的策略；摘要未说明具体奖励。
4. 将策略零样本部署到实体手，持续闭环输出动作，并统计旋转次数与速度。

### 必要术语

- 本体感觉：机器人对自身关节等状态的感知；这里提供手部运动信息。
- 二值触觉：每个触点只报告接触或未接触；这里不需要完整压力数值。
- 域随机化：训练时改变环境或硬件条件；这里用于覆盖动作限制和触觉故障。
- Taxel：触觉传感单元；STuck-AT Taxels 模拟其输出固定不变的情况。

## 证据

摘要报告，实体手在一次连续试验中完成 225 次 180° 旋转，即 112.5 圈，速度约 0.36 圈/秒，全程无视觉或物体状态输入。这证明所示条件下可持续运行。摘要还说比较了仅本体感觉与加入触觉、分析了重要触觉区域，但未给数值或区域名称。“次数和速度最强”是作者报告的比较结论，输入未列对应文献与条件。

## 局限

一次长时间成功不能说明重复成功率，也不能外推到不同球体、握持起点或手部磨损状态。仍需核查多次试验分布与各组件消融，才能判断触觉及两种随机化各自贡献了多少；摘要未给这些结果。

- **判断**：值得细读仿真建模、校准和消融实验，因为长时真机结果很具体，而最可迁移的知识在于哪些硬件误差必须进入训练。

## 研究关联

这里可借鉴的是：触觉迁移不能只模拟接触力，还要模拟传感器如何失真，以及执行器如何限制动作变化。若策略依赖理想、即时、始终可靠的反馈，增加训练任务数量未必能解决硬件失效。

### 下一步读哪里

优先核查触觉校准步骤、机械耦合如何进入仿真，以及两种随机化的采样范围；再看仅本体感觉的对照、触觉区域消融、多次硬件试验和速度统计口径。

- **概念**：世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/No Eyes, No Problem What Does Touch Contribute to Blind Baoding Ball Manipulatio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humans manipulate objects within their hands through touch alone with remarkable ease, but for robots, achieving sustained real-world manipulation without vision remains an open challenge. Although reinforcement learning (RL) can generate sophisticated blind manipulation policies in simulation, transferring them to a real dexterous hand remains hindered by continuously changing contacts, motion-induced tactile information drift, and the gap between simulated and physical dynamics. We study this problem through Baoding ball rotation on the Shadow Dexterous Hand Lite, using only proprioception and binary tactile feedback as observations. We achieve successful zero-shot transfer through a combination of a sensor-aligned, coupling-aware embodiment in simulation, tactile calibration, and two novel episodic domain randomisations: slew-rate action limits and STuck-AT Taxels. On the physical hand, the policy achieves sustained blind Baoding rotation, completing 225 consecutive $\mathbf{180^\circ}$ rotations (112.5 full rotations) at $\sim0.36 \;\text{rot/s}$ in a single continuous trial without any vision or object-state information. Furthermore, we evaluate the contribution of tactile sensing relative to proprioception alone and identify the hand regions where tactile information is most important. This is the strongest reported hardware result for Baoding ball manipulation in both rotation count and speed, irrespective of the sensing modality used. By effectively bridging the sim-to-real gap, our framework sets a new benchmark for sustained tactile-driven dexterous manipulation on physical hardware.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23438v1
- Authors: Ayush Deshmukh, Nalin Agarwal, Elle Miller, Sethu Vijayakumar
- Published: 2026-10-16T13:22:03Z
- Age days: 3

</details>
