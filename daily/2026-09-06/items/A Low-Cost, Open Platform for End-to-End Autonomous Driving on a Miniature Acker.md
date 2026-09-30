---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04147"
published: "Sat, 05 Sep 2026 00:00:00 -0400"
age_days: 0
score: 17
created: 2026-09-06
concepts: ["世界模型", "机器人学习", "Sim2Real"]
---

# A Low-Cost, Open Platform for End-to-End Autonomous Driving on a Miniature Ackermann Vehicle

> [!summary] 先说人话（基于摘要）
> 该文开源一套微型 Ackermann 自动驾驶平台，把实体小车、打印道路、采集与轨迹配准工具及 Webots 数字孪生打通，并给出“图像＋导航命令到转向和速度”的行为克隆基线。

## 问题

任务是低成本、可复现地研究端到端自动驾驶及 Sim2Real；瓶颈在于仿真方法与真实闭环执行之间缺少成套实验载体和可对照的数据、轨迹及数字孪生。

## 创新点或方法

策略输入车载相机图像和高层导航命令，输出转向与速度；平台同时在实车和 Webots 中执行。进一步由数字孪生生成合成数据，并用学习式 sim-to-real 图像转换器缩小外观差异，再将合成与真实示范联合训练较大容量策略。

## 证据

真实闭环平均横向误差为 6.1 cm，接近人类示范的 4.7 cm。仿真中视场角从 58° 扩到 120° 后，误差从 35.6 cm 降至 3.3 cm；只有使用合成加真实数据训练的高容量策略完成全部四条路线，紧凑基线及仅用真实数据的同网络完成得更少。


## 局限

四条打印赛道上的成功不能直接代表复杂道路泛化；需查全文确认路线难度、运行次数、图像转换训练数据，以及视场角实验是否控制了其他变量。

- **判断**：教学、快速原型和 Sim2Real 基准团队值得精读并评估复现；若目标是大规模真实自动驾驶，其价值主要是方法验证平台而非性能结论。

## 研究关联

对机器人学习和 Sim2Real 研究者，这是可复现实车闭环的低成本试验台，可用于检验数据合成、视觉域适配和策略容量。与世界模型的联系主要体现在数字孪生环境，摘要并未训练预测式世界模型。

- **概念**：世界模型 机器人学习 Sim2Real
- **筛选分数**：17
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-06/A Low-Cost, Open Platform for End-to-End Autonomous Driving on a Miniature Acker.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04147v1 Announce Type: cross Abstract: This paper presents a low-cost, open experimental platform for research in end-to-end autonomous driving with miniature Ackermann vehicles. The platform combines a physical vehicle, a printed urban track, data collection tools, trajectory registration, and a Webots digital twin, enabling controlled experiments that connect simulation-based autonomous-driving methods to real-world execution. As a first baseline, we implement command-conditioned behavior cloning, in which a neural policy receives an on-board camera image and a high-level navigation command and outputs steering and speed. The system is evaluated both on the physical vehicle and in simulation. In real closed-loop experiments, the learned policy follows lanes and executes commanded turns, reaching a mean cross-track error of 6.1 cm with respect to the reference route, close to the 4.7 cm observed in human demonstrations. In the digital twin, camera field of view has a strong effect on performance, reducing the mean cross-track error from 35.6 to 3.3 cm when widened from 58 to 120 degrees. Using the digital twin to generate synthetic driving data and a learned sim-to-real image translator to reduce the appearance gap, we further show that a higher-capacity policy trained on this synthetic data combined with real demonstrations is the only configuration that completes all four track routes in closed loop, whereas the compact baseline and the same network trained on real data alone complete fewer. These results establish the open platform as a practical testbed for sim-to-real studies and provide an initial command-conditioned imitation-learning baseline; we release it to support reproducible research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04147
- Authors: Gustavo Claudio Karl Couto, Eric Aislan Antonelo, Gabriel George Zipperer
- Published: Sat, 05 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
