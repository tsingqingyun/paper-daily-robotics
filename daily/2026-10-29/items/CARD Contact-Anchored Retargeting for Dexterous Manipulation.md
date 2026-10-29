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
url: "https://arxiv.org/abs/2610.36539v1"
published: "2026-10-27T02:51:20Z"
age_days: 1
score: 28
created: 2026-10-29
concepts: ["世界模型", "机器人学习"]
---

# CARD: Contact-Anchored Retargeting for Dexterous Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> CARD 转移人手示范时，不仅要求机器人手摆出相似姿势，还明确要求维持接触力目标。它把视频、动作捕捉和触觉手套转换成共同的手部与接触表示，再用触觉控制器帮助机器人在执行时实现这些目标。

## 问题

任务是把人的灵巧操作转成机器人动作，避免示范者必须通过遥操作等方式迁就机器人身体。现有重定向主要匹配运动学，但手指位置相近不代表接触稳定，更不代表施力合适，因此动作看起来对，任务仍可能失败。

### 用一个例子理解

理解用例（非论文实验）：输入一段人手捏住小盒子并抬起的视频；Vid-HACO 推断手与接触信息，CARD 转成机器人手姿态和接触力目标，机器人执行时用触觉调整施力，输出一次以维持抓持为目标的动作。

## 创新点或方法

旧做法主要转移关节或手部运动；CARD 在共同表示中加入显式接触力目标，让重定向同时关心手怎么动、接触如何维持。视频没有直接触觉读数，便用 Vid-HACO 估计接触信息。执行时再由触觉跟踪控制器追踪目标力。摘要称重定向无需仿真器和物体，但没有解释物体信息的具体依赖边界；这不代表实际操作无需物体。模型训练数据、损失和控制律均未说明。

### 方法如何工作

1. 把不同来源的示范转换成共同的手部与接触表示，使后续重定向不必为每种输入单独定义接口。
2. 对没有触觉读数的视频使用 Vid-HACO 补充接触信息；具体预测量和训练方式摘要未说明。
3. 同时生成机器人运动与接触力目标，使动作转换保留任务所需的交互要求。
4. 硬件执行时用触觉跟踪目标力，补偿仅回放运动指令无法保证接触的问题。

### 必要术语

- 重定向：把人的动作转换成另一种身体可执行的动作；本文用于人手到机器人手。
- 运动学：描述位置、姿态和运动，不直接保证施力结果；是本文要补足的原有目标。
- 接触力目标：希望接触处达到的力；为重定向和实际执行提供共同要求。
- 触觉跟踪控制器：根据触觉反馈调整执行，使实际受力接近期望值；用于硬件回放。

## 证据

摘要报告，在视频、手套、动作捕捉及 GRAB 数据上，CARD 在 43%—78% 的接触帧中维持接触，运动学方法低于 10%，物体感知方法为 22.5%。把其目标表述加入基于物理的重定向后，GRAB 上严格任务成功率由 12% 升至 32%。这些分别支持接触保持和特定任务成功的改善，不能混为同一指标。硬件回放还显示触觉跟踪器对复现示范力关键，但没有给出力误差数字；Vid-HACO 的最优表现也缺少指标细节。

## 局限

摘要没有列出明确局限。需要核查接触帧的判定阈值、不同手型和物体的适用范围，以及视频估计出的力如何校准。文中提到硬件开环回放，但同时使用触觉反馈，因此不能理解成完全没有反馈；高层回放与底层控制的边界需要看方法。

- **判断**：值得深入读接触表示和控制器，并核对任务成功实验：它把重定向中最容易被姿态指标掩盖的接触问题单独拿了出来。

## 研究关联

这里值得借鉴的是把示范理解成需要实现的交互条件：如果任务依赖摩擦和持续抓持，转移动作轨迹时也应转移接触要求。这样才有机会解释为何两段相似运动会产生不同结果。

### 下一步读哪里

先查共同表示如何编码接触位置、方向和力，再查视频估计的监督来源；实验重点核查 43%—78% 对应哪些设置，以及 12% 到 32% 的对照是否保持其他条件一致。

- **概念**：世界模型 机器人学习
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/CARD Contact-Anchored Retargeting for Dexterous Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humans are dexterous, but traditional data collection paradigms such as teleoperation, kinesthetic teaching, and wearable exoskeletons force humans to act through the robot embodiment, bottlenecking their dexterity. Retargeting can avoid this. However, existing methods purely translate kinematics and ignore the real-world contact dynamics essential for task success. We present CARD: Contact-Anchored Retargeting for Dexterous Manipulation, a simulator and object-free framework that retargets human demonstrations to robot actions by explicitly preserving contact force targets. CARD unifies human data sources including video, motion capture, and tactile gloves via a shared hand--contact representation and generates explicit contact force targets in addition to kinematics. To maintain these contact targets during hardware open-loop replay, CARD also introduces a tactile tracking controller. For video which does not contain an explicit tactile source, we present Vid-HACO, our video-to-contact model that sets a new state of the art. Across our video, glove, motion-capture data and the GRAB dataset, CARD maintains contact on $43$--$78\%$ of contact frames, while kinematic and object-aware retargeting methods maintain contact on $<10\%$ and $22.5\%$ of the frames respectively. Further, integrating our formulation into physics-based retargeting improves strict task success from 12\% to 32\% on GRAB dataset. Finally, we show that our tactile tracker is critical to reproduce demonstrated forces during hardware replay. These results establish that contact preservation via CARD is a scalable interface for transferring human dexterity to robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36539v1
- Authors: Cunxi Dai, Botao He, Francois R Hogan, Wei Pan, Rao Fu, Wen-Han Hsieh, Ruoshi Liu, Jitendra Malik, Guanya Shi, Akash Sharma
- Published: 2026-10-27T02:51:20Z
- Age days: 1

</details>
