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
url: "https://arxiv.org/abs/2611.06817v1"
published: "2026-11-04T17:31:35Z"
age_days: 1
score: 35
created: 2026-11-06
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> Open-HumanScale 想弄清，大量第一视角人类操作视频能给机器人学动作带来多少帮助。它用纯人类视频预训练的 HumanWAM-Vanilla 测数据量效应，再用混合人机经验、接受视觉目标的 HumanWAM-Goal 探索迁移到新目标和新条件。

## 问题

人类戴摄像头做事，比让机器人逐个采集同类操作更容易扩大规模。但视频里的手怎么动，与机器人该发什么动作指令之间还有一道转换。原始视频越多，能否转成机器人完成任务的能力也越好，需要在机器人执行任务时检验。

### 用一个例子理解

理解用例（非论文实验）｜给机器人当前桌面的画面，再给一张杯子已经放进托盘的目标图。Goal 用目标图约束动作生成，输出机械臂移杯的动作。把目标图换成杯子放在托盘另一侧，模型仍用原来的参数，根据新画面生成动作。

## 创新点或方法

直接扩大原始视频量，难以判断模型从中学到了什么。作者先筛选第一视角视频并密集标注手部运动和自然语言，再改变纯人类预训练的数据量，用闭环仿真测机器人成功率。Vanilla 先只看人类经验，再用机器人数据后训练。Goal 在预训练时混合人和机器人的经验，并让模型以目标画面为条件。真机推理时，Goal 可以换一个目标画面来调整行为，参数无需更新。摘要未说明世界预测与动作生成在训练和推理中如何衔接。

### 方法如何工作

1. 筛选第一视角视频，补上手部运动和语言标注，使操作过程有可学习的信号。
2. 按不同视频时长做纯人类预训练，再比较闭环仿真结果，测数据量和机器人表现的关系。
3. 将只用人类经验预训练的 Vanilla 用机器人数据后训练，使学到的经验能用于目标机器人。
4. 为 Goal 混合人机经验并加入视觉目标条件，使同一策略推理时能随输入目标改变行为。

### 必要术语

- 世界—动作模型：同时涉及环境演变与动作的模型；HumanWAM 属于这一类，摘要未展开两者如何连接。
- 闭环评估：执行后根据新的观察继续决策；用来检验策略能否在连续交互中完成任务。
- 视觉目标条件：用画面指定想达到的状态；Goal 据此调整生成的动作。

## 证据

摘要报告，在考察的数据规模内，纯人类预训练时长取对数后，与下游机器人成功率近似呈线性关系。机器人后训练后，Vanilla 在 RoboTwin 2.0 的 Clean2Clean 和 Clean2Random 中分别为 92.08% 和 68.88%，在 RoboDojo 的平均成功率为 14.17%，平均进度分为 19.00。Goal 在同两项 RoboTwin 设置下为 92.70% 和 84.60%。两套配方在 Clean2Random 的差距更大。摘要还报告了真机对未见视觉目标的适应，但未给任务数、成功率或对照结果。

## 局限

我最想核查的是 Clean2Random 的改善有多少来自混合数据，有多少来自视觉目标条件。Vanilla 和 Goal 同时改变了这两项，摘要中的模型对比只能反映整套配方的差异。仿真里的规模关系和真机上的新目标适应也需要分别判断。

- **判断**：值得细读规模实验和混合数据消融，前者决定数据量曲线能用到哪，后者决定 Goal 的做法能复用哪一部分。

## 研究关联

可以把人类视频的价值当成一条曲线来测。保持机器人后训练和测试设置可比，只改人类预训练时长，就能看到增加视频在哪些测试条件下还带来收益。把常规条件和随机化条件分开看，还能避免较高的常规成功率盖住迁移困难。

### 下一步读哪里

先看规模曲线用了哪些数据量、任务和拟合区间，以及各档是否使用相同的机器人后训练设置。再查 Goal 的数据配比、目标图来源，以及真机把哪些变化定义为未见目标。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/Open-HumanScale An Open Recipe for Scaling Human and Robot Experience for Embodi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training recipes. We introduce Open-HumanScale, the first fully open recipe for scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanScale-50K---a curated egocentric video corpus densely annotated with hand motion and natural language. Leveraging this corpus, we systematically investigate pure human pretraining via closed-loop simulation evaluations and uncover an empirical log-linear scaling law linking pretraining data hours to downstream robot success rates. Grounded in these findings, we develop HumanWAM-Vanilla, a world--action model pretrained exclusively on 50k hours of egocentric human video. Upon robot post-training, HumanWAM-Vanilla reaches 92.08% success on RoboTwin 2.0 Clean2Clean and 68.88% on Clean2Random, alongside a 14.17% mean success rate and a 19.00 mean progress score on RoboDojo. To push the capability frontier further, we explore joint human--robot pretraining with HumanWAM-Goal, a visual-goal-conditioned world--action model. Hybrid data scaling unlocks broad zero-shot generalization across both simulation and physical benchmarks, propelling post-trained RoboTwin 2.0 performance to new state-of-the-art levels: 92.70% on Clean2Clean and a substantial leap to 84.60% on Clean2Random. On physical robots, HumanWAM-Goal further exhibits emergent embodied in-context learning, dynamically adapting its manipulation behavior to unseen visual goals without parameter updates. To support reproducible scaling research in embodied AI, we open-source the Open-HumanScale-50K corpus, data curation and pretraining pipelines, alongside the pretrained and post-trained HumanWAM checkpoints, inference code, and simulation evaluation suites.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.06817v1
- Authors: Juncheng Ma, Jiaxin Li, Jiankai Tu, Bo Liang, Guodong Lv, Yufan Deng, Junzhe Tang, Liangzhu Yang, Chen Bian, Zicong Cao, Baohao Zhu, Jianxin Bi, Tengfei Yan, Yinyuan Zhang, Kewei Zhang, Xinglong Chen, Kaiqi Chen, Duomin Wang, Xiaotian Tang, Liang Tan, Li Li, Yuan Xu, Haosen Yang, Yuqi Wang, Jingfei Xia, Songyan Huang, Zhiyang Dou, Zhen Dong, Enze Xie, Tat-Seng Chua, Daquan Zhou
- Published: 2026-11-04T17:31:35Z
- Age days: 1

</details>
