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
url: "https://arxiv.org/abs/2610.37518v1"
published: "2026-10-27T16:40:10Z"
age_days: 1
score: 29
created: 2026-10-29
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer

> [!summary] 这篇论文到底做了什么（基于摘要）
> World Dreamer v5-lite 让多个机器人先把看到的东西放进同一份有空间坐标的状态，再分别决定动作。巧处是让机器人共享观察、交换与姿态有关的信息，同时保留各自动作输出，避免把多摄像头画面简单堆在一起。

## 问题

任务是根据分散的摄像头观察，同时预测多个机器人的动作序列。瓶颈不只是画面多，而是不同画面中的物体、位置和机器人如何对应；多数现有 VLA 和世界动作模型面向单机器人，仅合并视图不能自动建立这种空间关系。

### 用一个例子理解

理解用例（非论文实验）：两台机械臂共同整理桌面。输入两侧画面和整理指令，系统把物体特征放到共同坐标中；左臂的查询借助右侧视角确认被遮挡物体的位置，最后分别输出两台机械臂的动作序列。

## 创新点或方法

旧做法把多路视觉输入交给策略，本文先用标定信息把预训练视频编码器的特征放到工作空间坐标中，形成大小不随视图数量增长的共享状态。视觉语言模型补充场景信息，并为每个机器人提供一个查询；查询读取共享状态、交换姿态相关信息，各自生成动作流。训练还会同时遮掉两个视觉分支中的部分视图，却保留全部动作目标，迫使模型借用其他机器人的观察。推理时读取可用观察输出动作；具体状态更新和动作解码方式未说明。

### 方法如何工作

1. 将各摄像头特征按标定关系放入共同工作空间，使不同视图有位置对应。
2. 用视觉语言模型提供场景上下文和机器人查询，让每个机器人带着自身需求读取状态。
3. 让查询交换姿态相关信息，再分别预测动作，兼顾协作与独立控制。
4. 训练时遮掉部分视图但保留全部动作目标，使利用其他视角成为完成预测的必要途径。

### 必要术语

- 共享世界状态：多路观察汇入的共同空间表示；本文用它连接各机器人的视觉信息。
- 标定：确定摄像头与工作空间的几何关系；本文靠它建立跨视图位置对应。
- 查询：代表某个机器人读取信息的向量；本文用不同查询得到各自动作。

## 证据

摘要报告：RoboFactory 平均成功率为 74.0%，比最强受测基线高 23.7 个百分点；四项真机任务平均成功率为 78.8%，高 13.8 个百分点；RoboCasa365 总体成绩为 58.08%。预训练使用超过一万小时、覆盖 20 种仿真机器人及其他来源的轨迹。摘要未给基线名称、任务明细、重复次数或模块消融，因此支持整套系统的效果，尚不能单独确认共享状态或遮视图训练各贡献多少。

## 局限

真机结果覆盖四项任务，不能直接推到任意机器人数量和布局。我要核查标定误差、视图缺失及机器人数量变化时的表现；共享状态尺寸固定，也不代表总计算量固定。

- **判断**：值得深入读空间特征写入和遮视图训练部分，因为它们直接回答了多机器人如何真正利用彼此观察。

## 研究关联

可以借鉴的是：协作首先需要让观察具有共同坐标，而非仅增加输入数量。当机器人能互相看见对方看不到的区域、且摄像头能够标定时，这种共享方式尤其值得尝试。

### 下一步读哪里

先检查标定特征如何进入共享状态，再看查询之间交换了什么。重点核查取消空间对齐、取消视图遮挡后的对照，以及真机任务是否真正要求跨机器人利用观察。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/World Dreamer v5-lite A Multi-Robot World Action Model with One Dreamer.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multi-robot control requires integrating distributed camera views while predicting separate action sequences. Most vision-language-action and world-action models target one robot. Combining multiple views alone does not establish spatial correspondence between them. World Dreamer v5-lite is a multi-robot world-action model built around a shared world state for robot-specific action prediction. Calibrated features from a pretrained video encoder populate this state in workspace coordinates; its spatial size remains fixed as views are added. A vision-language model provides scene context and one query per robot. The queries read the shared state and exchange pose-aware information, while their action streams remain separate. Masked-view cooperative training withholds selected camera views from both visual branches while retaining all action targets. This encourages the use of observations shared by other robots. Pretraining uses more than 10,000 hours of trajectories from 20 simulated robot types, RoboFactory, and real robots. On RoboFactory, World Dreamer v5-lite achieves 74.0% mean success, 23.7 percentage points above the strongest evaluated baseline. Across four real-robot tasks, it reaches 78.8% mean success, a margin of 13.8 points. It also reaches 58.08% overall on RoboCasa365.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37518v1
- Authors: Guoning Wu, Zijian Cai, Yuhang Zhang, Ying Liu, Yongbin Zheng
- Published: 2026-10-27T16:40:10Z
- Age days: 1

</details>
