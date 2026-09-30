---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11382v1"
published: "2026-09-10T11:17:20Z"
age_days: 1
score: 31
created: 2026-09-12
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# SwarmNxt: Open-source Software-Hardware Platform for Fast and Agile Aerial Swarms

> [!summary] 先说人话（基于摘要）
> SwarmNxt把多无人机实验所需的硬件装配、批量部署和自主飞行软件整合起来，降低搭建实体集群的工程成本。

## 问题

敏捷视觉集群飞行需要机载计算和自主导航，但商业平台常封闭或计算资源不足；多机软件部署与维护也耗费大量工程工作。

## 创新点或方法

基于OmniNxt硬件，提供装配教程、并行部署和集群更新工具，并在ROS 2多智能体系统中集成控制、规划与深度估计。

## 证据

报告两项真实实验：六机分布式规划与高速机间避碰，以及四机在障碍环境中结合机载深度估计协同飞行。两者均在室内使用外部动捕提供全局位置，感知、规划和控制在机载运行。


## 局限

实验依赖外部动捕定位，尚不能据此确认其在灾害现场或无外部定位环境中的整体自主能力；摘要未给出速度或成功率数字。

- **判断**：做实体无人机集群值得读部署与系统接口，做通用Agent算法可略读。

## 研究关联

对实体多智能体与具身实验研究者，主要价值是可复用基础设施，便于开展物理集群实验。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/SwarmNxt Open-source Software-Hardware Platform for Fast and Agile Aerial Swarms.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Aerial robot swarms have the potential to transform time-critical safety, security, and search-and-rescue operations. By coordinating multiple robots, they can rapidly survey disaster sites, map collapsed or GPS-denied environments, and search cluttered areas faster than a single robot, reducing response times and minimizing risks to first responders. Realizing this potential, however, requires robust autonomous swarm navigation, which remains an active research challenge. Progress is further constrained by existing platforms, as commercial drones are often closed-source or lack the onboard computational resources needed for agile, vision-based collective flight. Moreover, developing, deploying, and maintaining software across multiple aerial robots requires significant engineering effort. To address these challenges, we present SwarmNxt, an open-source software platform built on the open-source OmniNxt drone hardware. SwarmNxt provides an end-to-end toolkit, including detailed hardware assembly instructions with a video tutorial, automation tools for parallel software deployment and swarm-wide updates, and a ROS 2-based framework for autonomous navigation. The platform integrates state-of-the-art control, planning, and depth estimation into a single ROS 2 multi-agent system, providing an open research infrastructure for physical swarm experimentation. We validate SwarmNxt through two real-world experiments: a six-drone swarm performing decentralized planning with high-speed inter-drone collision avoidance, and a four-drone swarm executing collective flight with onboard depth estimation in an obstacle-filled environment. Both experiments were run indoors with global position from external motion capture; perception, planning, and control run onboard.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11382v1
- Authors: Charbel Toumieh, Niel Mistry, Benjamin Jarvis, Simon Jeger, Peize Liu, Shaojie Shen, Dario Floreano
- Published: 2026-09-10T11:17:20Z
- Age days: 1

</details>
