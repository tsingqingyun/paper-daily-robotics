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
url: "https://arxiv.org/abs/2610.23378"
published: "Mon, 19 Oct 2026 00:00:00 -0400"
age_days: 0
score: 32
created: 2026-10-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

> [!summary] 这篇论文到底做了什么（基于摘要）
> ActiveAlign 解决“机器人换个角度看清了，却反而不会操作”的问题。它从主动观察结束时的状态重新组织训练数据，让操作策略适应看完之后真正接手的画面和机器人状态。

## 问题

杂乱场景中，机器人需要移动相机看见被遮挡的目标。但原操作策略通常从示范里的起始状态出发；相机移动后的画面和机器人状态可能偏离这个分布。于是直接在策略前加一段观察动作，即便改善可见性，也可能破坏后续操作。

### 用一个例子理解

理解用例（非论文实验）：指令是拿起被盒子挡住的杯子。视点模块先移动相机；离线用这种观察终点接续拿杯示范，收集成功轨迹训练。执行时，适配后的策略从新视角和对应机器人状态接手，输出拿杯动作。

## 创新点或方法

旧做法把主动观察直接接到原策略前；ActiveAlign 改为让训练起点也经过主动观察。离线阶段，学习到的视点模块先生成相机轨迹，再通过闭环对齐把终点接到已有示范，重放示范剩余操作，只保留成功续接的数据来微调 VLA。部署时用同一视点模块先观察，再交给适配后的策略，VLA 架构不变。摘要未说明闭环对齐的具体控制方式及数据生成成本。

### 方法如何工作

1. 视点模块生成相机轨迹，获得主动观察结束时的画面和机器人状态，确定后续策略实际面对的起点。
2. 离线用闭环对齐连接该终点与已有示范，使原有操作轨迹有机会从新状态继续。
3. 重放剩余操作并筛选成功续接，得到与主动观察相匹配的训练数据。
4. 用这些数据微调 VLA，部署时再按相同顺序连接视点模块和适配后的操作策略。

### 必要术语

- 主动感知：通过主动移动选择观察方式；本文用相机轨迹暴露被遮挡目标。
- 首帧分布敏感性：策略对接手时初始观察和状态变化的敏感；这是本文定位的失败来源。
- 闭环对齐：利用执行反馈逐步接近可续接状态；本文用它连接观察终点与已有示范。

## 证据

摘要中，LIBERO 扰动起点下，直接给 pi_0.5 加相机重定位使成功率从 46.3% 降到 11.5%。在 40 个 LIBERO 任务上，ActiveAlign 配合 pi_0、pi_0.5 分别达到 70.7%、72.7%，摘要称较标准训练基线提高 40.0%、26.4%，但未说明增幅口径。匹配状态和数据量的对照支持收益不只来自缩短前缀或一般视角增强；OpenVLA、GR00T N1 也呈同向趋势。真机物理遮挡测试从 35/90 提高到 83/90。

## 局限

真机结果支持所测物理遮挡条件下的收益，不能直接外推到任意相机布局。我的待核查问题是：对齐与重放失败的数据占多少，成功筛选是否让难状态覆盖不足，以及真机提升在不同任务上是否均匀。这些细节未在摘要中提供。

- **判断**：优先读方法和控制实验：它既展示了明确的接口失配，又通过针对性对照检验了数据适配为何有效。

## 研究关联

这里值得借鉴的是检查模块交接处的数据分布。一个前置模块改变了机器人接下来会看到什么、处于什么状态，就应让后续策略在这些真实交接条件上训练，而不只评估前置模块本身是否完成目标。

### 下一步读哪里

先看闭环对齐如何定义可续接状态，再核查匹配状态、匹配数据量的对照究竟固定了什么。真机部分应检查任务构成、视点模块设置及失败类型；输入没有正文节选。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-20/Look Before You Act Bridging Active Perception and Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.23378v1 Announce Type: new Abstract: Robots manipulating objects in clutter must decide not only how to act, but also where to look. Although active camera motion can expose an occluded target, it may move the robot into an initial observation-state distribution that differs from the manipulation policy's training distribution. We identify this problem as first-frame distribution sensitivity: under perturbed starts in LIBERO, naively prepending camera repositioning to pi_0.5 reduces success from 46.3% to 11.5%. We introduce ActiveAlign, a data-adaptation framework that trains a Vision-Language-Action (VLA) policy from the states at which active perception terminates. A learned viewpoint module first generates a camera trajectory. Offline, ActiveAlign uses closed-loop alignment to connect the trajectory endpoint to an existing demonstration, replays the remaining manipulation trajectory, and retains successful continuations for fine-tuning. At deployment, the same viewpoint module precedes the adapted VLA without modifying its architecture. Across 40 LIBERO tasks, ActiveAlign achieves 70.7% success with pi_0 and 72.7% with pi_0.5, outperforming their standard-training baselines by 40.0% and 26.4% respectively. Matched-state and data-matched controls support gains beyond prefix shortening and generic viewpoint augmentation; OpenVLA and GR00T N1 also show the same trend. Success rate under physical occlusion in real world increases from 35/90 to 83/90. These results show that active perception benefits manipulation when policy training is aligned with the observation and robot-state distribution induced by viewpoint selection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23378
- Authors: Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yongchong Gu, Yanwei Fu
- Published: Mon, 19 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
