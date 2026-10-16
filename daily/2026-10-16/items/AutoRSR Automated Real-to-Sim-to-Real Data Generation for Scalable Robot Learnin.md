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
url: "https://arxiv.org/abs/2610.20336"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-16
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# AutoRSR: Automated Real-to-Sim-to-Real Data Generation for Scalable Robot Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> AutoRSR 把扫描到的真实工作台变成与机器人坐标对齐的仿真场景，再从少量参考动作扩出操作数据，用这些数据训练策略并回到真机测试。它主要减少的是做仿真资产、标定场景和制作轨迹的人工工作。

## 问题

大规模操作学习需要大量示范，但真人遥操作消耗人力和机器人时间。仿真虽能批量生成数据，前期仍要人工提取物体、处理资产、标定坐标和指定轨迹。瓶颈因此不只是仿真运行速度，而是真实工作区如何变成能供机器人训练的仿真环境。

### 用一个例子理解

理解用例（非论文实验）：输入收纳盒与积木的多视角扫描、机器人状态，以及“积木”“盒子”等查询。系统提取资产、对齐坐标，从参考搬运动作扩出不同位置与外观的数据，训练后输出真机搬运动作。此例不代表论文测试了积木收纳。

## 创新点或方法

旧流程把扫描、资产整理、标定和轨迹制作分成多项人工工作；AutoRSR 将它们接成自动流程。输入多视角观测、机器人状态和开放词汇语义查询，系统重建场景、分离物体资产，并以真实尺度将场景配准到机器人基座坐标系。之后从少量参考动作生成可执行轨迹，再用轨迹插值和域随机化扩大数据。训练阶段用这些数据学习操作策略；部署阶段让策略执行真机任务。摘要明确说扫描和语义查询之后无需人工物体标注、场景标定或机器人遥操作，但参考动作的来源、策略输入和训练配方未说明。

### 方法如何工作

1. 结合多视角观测、机器人状态和语义查询重建工作区，得到场景与单独物体资产。
2. 把重建结果按真实尺度对齐到机器人基座，使场景位置能用于机器人轨迹生成。
3. 从少量参考动作生成可执行轨迹，再通过插值和域随机化扩大数据覆盖。
4. 用生成数据训练策略并在真机测试，检查自动制作的仿真数据能否支持现实操作。

### 必要术语

- Real-to-Sim-to-Real：从真实场景制作仿真、训练后回到现实执行；这是本文的数据与验证路线。
- 坐标配准：把重建场景的位置对齐到机器人使用的坐标系；本文借此连接扫描结果与可执行运动。
- 域随机化：改变仿真中的部分条件来生成多样数据；本文用它扩充训练数据，具体随机项未说明。

## 证据

摘要报告三项真机操作任务：每项使用 1K 条自动生成数据训练，真机成功率为 73.3%—86.7%，与使用 150 条人类遥操作示范训练的 pi 0.5 相当；数据生成所需人力时间降低一个数量级。结果支持这些工作区与任务下的数据生产可行性，但没有提供逐任务对照、测试次数、时间统计口径或两组训练配置，不能据此认定任意任务都能以同样成本替代人工示范。

## 局限

这是仿真训练后回到真机测试的证据，但仅覆盖摘要所述三项任务。我的待核查问题是接触、摩擦和遮挡重建误差怎样处理，以及参考动作需要多少人工准备。“后续无需遥操作”并不等于整个流程没有人工输入，摘要已明确保留扫描、语义查询和少量参考动作。

- **判断**：值得深入读坐标配准、轨迹可执行性和人力统计；它的吸引力在于降低数据生产门槛，适用范围要由这三处细节决定。

## 研究关联

这里值得借鉴的是把数据扩增的前提做扎实：场景不仅要重建出来，还要有正确尺度、机器人坐标关系和可执行轨迹。评估一条仿真数据流水线时，应把人工资产处理与标定时间计入成本，否则容易高估其扩展能力。

### 下一步读哪里

先核查真实尺度和基座配准如何获得，再看参考动作的来源、插值后的轨迹如何检查可执行性。实验部分重点确认三项任务各自成功率、pi 0.5 对照配置，以及人力时间是否包含扫描、查询和参考动作准备。

- **概念**：世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/AutoRSR Automated Real-to-Sim-to-Real Data Generation for Scalable Robot Learnin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.20336v1 Announce Type: new Abstract: Scaling embodied robot learning requires large and diverse manipulation datasets, but collecting real-world demonstrations remains expensive in human effort and robot time. Simulation provides a scalable alternative, yet converting a real workspace into a robot-learning-ready environment still requires substantial manual effort for object extraction, asset processing, coordinate calibration, and trajectory specification. We present AutoRSR, a highly automated real-to-sim-to real framework that converts scanned real-world workspaces into reusable embodied simulation assets and scalable manipulation data. Given multi-view observations, robot states, and open-vocabulary semantic queries, AutoRSR reconstructs the workspace, extracts individual object assets, and automatically registers the reconstructed scene to the robot base frame at metric scale. Starting from a small number of reference motions, AutoRSR then generates executable manipulation trajectories and scales them through trajectory interpolation and domain randomization. After workspace scanning and semantic queries, the remaining pipeline requires no manual object annotation, scene-to-robot calibration, or robot teleoperation. Across three real-world manipulation tasks, policies trained on 1K automatically generated episodes per task achieve 73.3--86.7% real-world success rates, comparable to pi 0.5 trained from 150 human teleoperated demonstrations, while reducing the human time required for data generation by an order of magnitude. These results demonstrate that real-world observations can be converted into metrically aligned, executable, and scalable simulation data with substantially reduced human effort.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.20336
- Authors: Jiawei Zhang, Chang Liu, Litao Deng, Tao Zhang, Qin Jin
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
