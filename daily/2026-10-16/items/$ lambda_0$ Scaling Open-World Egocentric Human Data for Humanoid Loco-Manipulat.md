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
url: "https://arxiv.org/abs/2610.18950"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-10-16
concepts: ["多模态基础模型", "世界模型", "机器人学习"]
---

# $\lambda_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> λ₀ 想让人形机器人从大量人的日常活动中学习边走边操作；关键是把人的视角、身体动作和控制器输入一起对齐，让人类演示成为机器人可用的监督。

## 问题

任务要求走路、调整姿态和手部操作相互配合。机器人演示采集昂贵，而已有第一视角人类监督常遗漏走路和姿态；即便补上动作，人和机器人身体不同、控制器响应不同，也会让手最终到错位置。

### 用一个例子理解

理解用例（非论文实验）：输入一个人走到桌边拿杯子的视频及同步身体、手部动作；流程将视角、手臂外观和动作参考调整到机器人条件，再修正控制输入；输出可供训练使用的机器人对齐演示，帮助模型学习走近、站稳和伸手之间的配合。

## 创新点或方法

旧做法提供的人类观察和动作不足以直接指导机器人，本文先采集同步的第一视角视频、身体与手部运动，再对齐相机视角和手臂外观，并离线修正运动参考及控制器输入，兼顾手端精度与全身协调。对齐后的演示用于 λ₀ 的中期训练。部署时机器人执行任务；具体模型结构、动作输出形式及在线控制流程，摘要未说明。

### 方法如何工作

1. 同步记录视频、身体和手部运动，补齐仅靠第一视角画面容易遗漏的走路与姿态信息。
2. 对齐相机视角和手臂外观，减少人的观察与机器人观察之间的差异。
3. 离线修正动作参考和控制输入，使手端位置更准确，同时保留全身配合；修正算法摘要未说明。
4. 用对齐演示进行中期训练，再让机器人执行下游任务，检验这些监督是否转化为实际能力。

### 必要术语

- 移动操作：移动身体的同时完成操作；本文需要让走路、姿态与手部动作协调。
- 末端执行误差：手等操作端实际位置与目标的偏差；本文用离线修正来减小它。
- 中期训练：模型训练流程中的一个阶段；本文在此加入机器人对齐的人类演示，前后训练配方未说明。

## 证据

摘要给出 HumanVerse 共 500 小时，并报告在 Unitree G1 上，无目标任务机器人演示即可零样本迁移，覆盖全身操作和长距离移动操作。另报告 λ₀ 在 SIMPLE 上成功率为 90.0%，在真实世界移动操作任务上为 62.5%，增加全身人类数据持续改善任务进度。摘要未交代 SIMPLE 的环境性质、对比基线、试验次数，也未明确这些成功率与前述零样本验证的对应关系。

## 局限

我会核查离线修正需要多少机器人专用信息，以及最终模型还用了哪些训练数据。“无目标任务机器人演示”不能推成完全不需要机器人数据；真机结果也不代表已覆盖任意开放环境。

- **判断**：值得读到数据对齐和控制修正的实现细节，因为这决定了 500 小时人的活动究竟怎样转成机器人能执行的动作。

## 研究关联

值得借鉴的是：使用人类数据时，要检查缺失的是否恰好是任务所需的身体自由度，以及动作能否经过实际控制器准确执行。采更多视频和得到更多可执行监督，是两个需要分别验证的步骤。

### 下一步读哪里

先核查运动参考与控制器输入分别怎样修正、依据什么误差；再看数据规模实验是否控制了其他训练条件，以及真机成功标准、任务分布和失败类型。

- **概念**：多模态基础模型 世界模型 机器人学习
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/$ lambda_0$ Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.18950v1 Announce Type: new Abstract: Humanoid loco-manipulation requires coordinated whole-body interaction with the physical world, yet collecting robot demonstrations at scale remains costly. Human demonstrations offer a scalable alternative, but existing egocentric human supervision often omits locomotion and posture, while embodiment differences and controller dynamics hinder accurate end-effector execution. We introduce HumanVerse, a 500-hour dataset of open-world human loco-manipulation pairing egocentric video with synchronized body and hand motion. Our human-to-humanoid pipeline aligns camera viewpoints and arm appearance, and refines motion references and controller inputs offline to reduce end-effector errors while preserving whole-body coordination. We validate the pipeline through zero-shot transfer to Unitree G1 on representative whole-body manipulation and long-range loco-manipulation tasks, without target-task robot demonstrations. Building on this pipeline, we develop $\lambda_0$, a humanoid foundation model for whole-body loco-manipulation, with robot-aligned human demonstrations providing supervision for mid-training. Increasing whole-body human data consistently improves downstream task progress. $\lambda_0$ achieves 90.0% success on SIMPLE and 62.5% across real-world loco-manipulation tasks. We expect this study to guide scalable whole-body human data collection toward humanoid foundation models for richer interaction with the physical world. Homepage: https://lambdahumanoid.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.18950
- Authors: humanoid Team
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
