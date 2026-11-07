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
url: "https://arxiv.org/abs/2611.06817v2"
published: "2026-11-04T17:31:35Z"
age_days: 2
score: 35
created: 2026-11-07
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> Open-HumanWAM 研究怎样把大量人类第一视角操作视频变成机器人可用的经验：先整理手部运动和语言标注，再比较纯人类数据与人机混合预训练。关键在于把数据规模、训练配方和机器人闭环表现放到一起验证。

## 问题

任务是让机器人借助人类视频学会操作，并应对变化后的场景。瓶颈是人类手部动作与机器人控制存在差异，原始视频再多也不会自动变成可靠策略；摘要强调，必须同时处理数据筛选、标注和训练方法。

### 用一个例子理解

理解用例（非论文实验）：输入桌面画面和“杯子放进托盘”的目标图像，策略结合预训练经验生成机器人动作，最终尝试摆成目标状态；目标图像提供结果要求，并不等于提供完整动作示范。

## 创新点或方法

从直接扩大视频量，改为先构建带密集手部运动和语言标注的 Open-HumanWAM-50K，再系统测量规模收益。HumanWAM-Vanilla 只用人类视频预训练，之后用机器人数据后训练；HumanWAM-Goal 则在人机混合数据上预训练，并以目标图像为条件。推理时后者可根据未见视觉目标调整行为，无须更新参数；世界预测与动作预测如何结合、训练损失如何设置，摘要未说明。

### 方法如何工作

1. 筛选第一视角视频并标注手部运动和语言，让视频中的操作内容具备可学习的对应关系。
2. 改变人类预训练数据量，再做机器人后训练和闭环评估，用实际执行结果测量规模收益。
3. 构建纯人类预训练的 Vanilla 与人机混合、视觉目标条件化的 Goal；具体训练结构摘要只说明到此。
4. 部署后根据观测与条件生成行为；Goal 在真机上展示无需参数更新的目标适应，但适应机制细节未说明。

### 必要术语

- 第一视角视频：从操作者视角记录的画面；本文用它提供人类操作经验。
- 世界—动作模型：将环境变化与动作建模结合的模型；本文未交代二者的具体连接方式。
- 闭环评估：执行动作后继续观察并决策；用于检验策略实际完成任务的能力。
- 上下文学习：通过当前输入调整行为而不更新参数；本文用来描述 Goal 的真机适应。

## 证据

摘要报告：纯人类视频预训练的数据小时数与下游成功率呈经验性对数线性关系。Vanilla 后训练后在 RoboTwin 2.0 的 Clean2Clean／Clean2Random 成功率为 92.08%／68.88%，在 RoboDojo 的平均成功率为 14.17%、平均进度分为 19.00。Goal 在前两项达到 92.70%／84.60%。这些支持所测条件下的规模收益；真机适应只有定性描述，未给任务数、成功率或完整基线。

## 局限

经验拟合不保证继续扩大规模仍有同样收益，也不单独证明数据小时数是唯一原因。摘要中的真机无参数更新适应，不能直接理解成任意新任务都能现场学会；其输入上下文和任务边界仍需核查。

- **判断**：值得深入读数据配方和规模实验，因为可复用之处在于如何把人类经验转成稳定收益，而不只是最大成功率。

## 研究关联

值得借鉴的是把“更多数据有没有用”拆成可测问题：保持评估流程一致，改变预训练规模与数据组成，再观察变化场景下的收益。尤其应核查 Goal 的优势有多少来自机器人数据、有多少来自目标图像条件。

### 下一步读哪里

下一步核查手部标注怎样连接机器人动作、规模实验控制了哪些变量，以及 Goal 的人机数据比例和视觉目标输入形式。还应查看真机适应的任务划分与失败案例；本次只有摘要。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/Open-HumanWAM An Open Recipe for Scaling Human and Robot Experience for Embodied.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training recipes. We introduce Open-HumanWAM, the first fully open recipe for scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanWAM-50K---a curated egocentric video corpus densely annotated with hand motion and natural language. Leveraging this corpus, we systematically investigate pure human pretraining via closed-loop simulation evaluations and uncover an empirical log-linear scaling law linking pretraining data hours to downstream robot success rates. Grounded in these findings, we develop HumanWAM-Vanilla, a world--action model pretrained exclusively on 50k hours of egocentric human video. Upon robot post-training, HumanWAM-Vanilla reaches 92.08% success on RoboTwin 2.0 Clean2Clean and 68.88% on Clean2Random, alongside a 14.17% mean success rate and a 19.00 mean progress score on RoboDojo. To push the capability frontier further, we explore joint human--robot pretraining with HumanWAM-Goal, a visual-goal-conditioned world--action model. Hybrid data scaling unlocks broad zero-shot generalization across both simulation and physical benchmarks, propelling post-trained RoboTwin 2.0 performance to new state-of-the-art levels: 92.70% on Clean2Clean and a substantial leap to 84.60% on Clean2Random. On physical robots, HumanWAM-Goal further exhibits emergent embodied in-context learning, dynamically adapting its manipulation behavior to unseen visual goals without parameter updates. To support reproducible scaling research in embodied AI, we open-source the Open-HumanWAM-50K corpus, data curation and pretraining pipelines, alongside the pretrained and post-trained HumanWAM checkpoints, inference code, and simulation evaluation suites.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.06817v2
- Authors: Juncheng Ma, Jiaxin Li, Jiankai Tu, Bo Liang, Guodong Lv, Yufan Deng, Junzhe Tang, Liangzhu Yang, Chen Bian, Shukai Gong, Yintianrun Zhang, Zicong Cao, Baohao Zhu, Jianxin Bi, Tengfei Yan, Yinyuan Zhang, Kewei Zhang, Xinglong Chen, Kaiqi Chen, Duomin Wang, Xiaotian Tang, Liang Tan, Li Li, Yuan Xu, Haosen Yang, Yuqi Wang, Jingfei Xia, Songyan Huang, Zhiyang Dou, Zhen Dong, Enze Xie, Tat-Seng Chua, Daquan Zhou
- Published: 2026-11-04T17:31:35Z
- Age days: 2

</details>
