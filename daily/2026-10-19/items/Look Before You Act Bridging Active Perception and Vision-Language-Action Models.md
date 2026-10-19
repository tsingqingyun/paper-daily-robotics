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
url: "https://arxiv.org/abs/2610.23378v1"
published: "2026-10-16T12:33:44Z"
age_days: 3
score: 32
created: 2026-10-19
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

> [!summary] 这篇论文到底做了什么（基于摘要）
> ActiveAlign 解决“相机找到了好视角，机械操作却变差”的问题：它让 VLA 在主动观察结束后的状态上重新学习接着操作。关键不是只增加可见性，而是让训练起点匹配真正的执行起点。

## 问题

遮挡环境里，机器人需要先移动相机寻找目标。但相机移动结束后，图像和机器人状态可能偏离操作策略熟悉的起点，直接接上原策略就容易失败。摘要中，LIBERO 扰动起点下，给 pi_0.5 直接加相机重定位，成功率从 46.3% 降至 11.5%，说明看得更清楚并不自动意味着更会操作。

### 用一个例子理解

理解用例（非论文实验）：输入是被盒子挡住的杯子和“拿起杯子”的指令；视角模块移动相机露出杯柄，适配后的策略从这个新视角和机器人状态继续抓取；输出是后续操作动作。

## 创新点或方法

旧做法直接把观察动作接在现有策略前面；ActiveAlign 则离线构造“观察结束后怎样接着做”的训练数据。学习到的视角模块先生成相机轨迹，再通过闭环对齐，把终点状态接到已有演示，重放剩余操作，只保留成功续接用于微调。部署时仍先运行同一个视角模块，再交给适配后的 VLA，不改 VLA 架构。摘要未说明闭环对齐的控制器和成功筛选细节。

### 方法如何工作

1. 生成主动观察轨迹，得到机器人真正会交给操作策略的终点状态。
2. 离线把终点连接到已有演示，使旧演示能够提供可执行的后续动作。
3. 重放剩余操作并保留成功续接，用这些数据微调 VLA，适应新的起点。
4. 部署时复用视角模块，再运行适配策略，让训练和执行的交接状态尽量一致。

### 必要术语

- 主动感知：通过移动相机主动获取信息；本文用它暴露被遮挡的目标。
- 首帧分布敏感性：策略对开始操作时的图像和状态很敏感；本文用它解释直接拼接模块的失败。
- 数据适配：为实际执行条件重建训练样本；本文重点适配观察结束后的续接操作。

## 证据

摘要报告在 40 个 LIBERO 任务上，pi_0 和 pi_0.5 分别达到 70.7% 和 72.7% 成功率，并称相较标准训练基线分别提高 40.0% 和 26.4%；后两项未注明相对百分比还是百分点，不宜自行换算。匹配状态、匹配数据的对照支持收益不只来自缩短任务前缀或普通视角增强；OpenVLA、GR00T N1 也呈同向趋势。真机物理遮挡测试从 35/90 提高到 83/90，但摘要未列任务组成与重复设置。

## 局限

现有结果覆盖仿真和真机，但不能据此推出任意相机运动都有效。需要核查适配数据的生成成本，以及对新遮挡、不同视角终点的覆盖；成功续接筛选也可能优先留下容易连接的状态。

- **判断**：优先细读数据构造和匹配对照，它把一个明确的接口失配问题转成了可验证的数据适配方案。

## 研究关联

增加一个前置模块，也会改变后续策略收到的输入分布。若要接入主动观察或其他准备动作，值得先收集该模块结束时的真实状态，并训练后续策略从那里继续，而不是只测试前置模块是否完成自己的目标。

### 下一步读哪里

重点核查终点如何连接演示、重放是否保持物理可行，以及匹配对照如何控制数据量和任务剩余长度；再看真机遮挡类型及失败案例。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/Look Before You Act Bridging Active Perception and Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots manipulating objects in clutter must decide not only how to act, but also where to look. Although active camera motion can expose an occluded target, it may move the robot into an initial observation-state distribution that differs from the manipulation policy's training distribution. We identify this problem as first-frame distribution sensitivity: under perturbed starts in LIBERO, naively prepending camera repositioning to pi_0.5 reduces success from 46.3% to 11.5%. We introduce ActiveAlign, a data-adaptation framework that trains a Vision-Language-Action (VLA) policy from the states at which active perception terminates. A learned viewpoint module first generates a camera trajectory. Offline, ActiveAlign uses closed-loop alignment to connect the trajectory endpoint to an existing demonstration, replays the remaining manipulation trajectory, and retains successful continuations for fine-tuning. At deployment, the same viewpoint module precedes the adapted VLA without modifying its architecture. Across 40 LIBERO tasks, ActiveAlign achieves 70.7% success with pi_0 and 72.7% with pi_0.5, outperforming their standard-training baselines by 40.0% and 26.4% respectively. Matched-state and data-matched controls support gains beyond prefix shortening and generic viewpoint augmentation; OpenVLA and GR00T N1 also show the same trend. Success rate under physical occlusion in real world increases from 35/90 to 83/90. These results show that active perception benefits manipulation when policy training is aligned with the observation and robot-state distribution induced by viewpoint selection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23378v1
- Authors: Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yongchong Gu, Yanwei Fu
- Published: 2026-10-16T12:33:44Z
- Age days: 3

</details>
