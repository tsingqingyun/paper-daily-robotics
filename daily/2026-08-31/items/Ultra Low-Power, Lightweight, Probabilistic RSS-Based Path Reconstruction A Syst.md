---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27152v1"
published: "2026-08-27T14:05:24Z"
age_days: 3
score: 22
created: 2026-08-31
concepts: ["AI 核心知识地图"]
---

# Ultra Low-Power, Lightweight, Probabilistic RSS-Based Path Reconstruction: A System for Landscape-Scale Bee Tracking

> [!summary] 先说人话（基于摘要）
> 该系统用少量旋转高增益发射器的 RSS 测量概率推断到达角，再以高斯过程和双随机变分推断重建超轻接收器的移动路径，实现低功耗、大范围蜜蜂追踪。

## 这篇到底在做什么

- **卡在哪里**：极小设备无法承担 GNSS；仅靠 RSS 推断到达角的替代方案通常量程有限，并需要大量测量，功耗和重量不适合昆虫等载体。
- **关键解法**：接收器只采集最少量 RSS，300 米量程的旋转定向发射器提供方向信息；概率模型先推断 AoA，再以高斯过程描述连续路径，用双随机变分推断完成重建。输出是景观尺度的移动轨迹。
- **拿什么证明**：含电源的接收器重 38 毫克；功耗低于 180 微瓦时轨迹精度约 15 米，增加 RSS 测量后在低于 600 微瓦时约 10 米；发射器范围为 300 米。系统用于追踪地熊蜂返巢飞行。

## 值不值得读

- **和你的研究有什么关系**：对超低功耗定位、IoT 和微型机器人，这是精度、重量、功耗与覆盖范围间的具体工程折中；对主流具身学习、VLA 或世界模型没有直接价值。
- **先别急着信**：10–15 米精度不适合精细控制，且需核查复杂地形、多径、发射器布设密度及真实飞行轨迹真值的获取方式。
- **判断**：做微型定位或生态追踪者值得精读，AI 机器人学习者浏览即可；贡献主要是系统级功耗—精度平衡。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/Ultra Low-Power, Lightweight, Probabilistic RSS-Based Path Reconstruction A Syst.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Applications in fields such as movement ecology, Internet of Things or robotics share the need for systems that localize devices that are too small and power constrained to implement GNSS (Global Navigation Satellite Systems). Alternative low-power localization methods often rely on only measurements of RSS (Received Signal Strength) to infer the AoA (Angle of Arrival) of a transmitted radio frequency signal, but are limited by range and the power demand of the large number of RSS measurements required to infer an accurate AoA. In this paper we address these issues with a novel RSS-based method for tracking ultra lightweight and low-power moving receivers across a complex landscape, achieved by using a minimal number of RSS measurements from simple rotating high-gain transmitters with a range of 300m, and applying probabilistic modelling to infer their AoA. The receiver's movement path is then modelled using a Gaussian process and reconstructed using doubly stochastic variational inference, resulting in approximately 15m accuracy tracking of receivers weighing 38mg (including power source) over a scalable landscape range while consuming less than 180uW, increased to approximately 10m accuracy at less than 600uW by taking more RSS measurements. We anticipate that this method will support fields such as the behavioural study of flying insect species, which we demonstrate by applying the system to track Bombus terrestris nest return flights.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27152v1
- Authors: Christopher J. Noroozi, Joseph L. Woodgate, Michael Mangan, Michael T. Smith
- Published: 2026-08-27T14:05:24Z
- Age days: 3

</details>
