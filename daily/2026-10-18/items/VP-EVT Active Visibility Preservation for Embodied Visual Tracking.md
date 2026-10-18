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
url: "https://arxiv.org/abs/2610.21999v1"
published: "2026-10-15T14:42:23Z"
age_days: 2
score: 25
created: 2026-10-18
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# VP-EVT: Active Visibility Preservation for Embodied Visual Tracking

> [!summary] 这篇论文到底做了什么（基于摘要）
> VP-EVT 让跟随机器人的目标包含“主动保持看得见目标人”：它估计目标与遮挡行人的运动，预测继续跟随是否会持续被挡住。风险高时调整视角，风险低时保留原有跟随动作。

## 问题

机器人仅靠自身视角跟随指定的人，动态行人可能长时间挡住目标。只在目标丢失后反应，容易持续看不见；瓶颈是机器人既要判断谁挡住了目标，也要判断自己的移动能否解除遮挡。

### 用一个例子理解

理解用例（非论文实验）：机器人跟着目标走进走廊，另一名行人插到两者之间；系统根据历史位置与当前运动预测直走会继续被挡，于是调整观察位置；重新看见目标后回到稳定跟随。

## 创新点或方法

相较于沿跟随路线前进、被挡后再补救，VP-EVT 先分别提取目标与其他行人的观测，结合视觉历史和自身运动估计相对位置与运动，再判断当前跟随路点是否会延续遮挡。低风险时保留原动作，高风险时由循环控制器结合此前机动上下文调整视角并恢复跟随。训练方面，作者采集专家示范；具体训练目标、训练模块及示范规模未说明。

### 方法如何工作

1. 用语言引导的感知分别获得目标与行人观测，为区分被跟随者和遮挡者提供输入。
2. 结合视觉历史与机器人自身运动估计相对位置和运动，在当前观测不完整时维持判断。
3. 结合现有跟随路点预测遮挡是否持续，得到是否需要改变动作的风险判断。
4. 低风险保留跟随动作；高风险由循环控制器利用更新估计和先前机动上下文调整视角，再协调恢复稳定跟随。

### 必要术语

- 具身视觉跟踪：机器人一边移动一边用自身相机跟随指定目标；动作会改变它能看到的内容。
- 自身运动：机器人自己的位置与朝向变化；本文用它辅助解释历史画面中的相对运动。
- 循环控制器：能利用先前决策信息的控制器；本文用它协调连续的视角调整与跟随恢复。

## 证据

摘要报告在新建 OccEVT-Bench 的 Risk 划分中，相对一个有竞争力的基线，成功率提高 121.4%，可见性缺失指标下降 78.8%，最长目标丢失时长下降 74.4%。121.4% 是相对增幅，不是百分点；摘要未提供绝对成功率、基线名称和样本量，也未明确该评测属于仿真还是真机。结果支持持续遮挡风险场景中的改善，尚不足以判断一般跟随表现。

## 局限

我的待核查问题是：历史估计在长遮挡下会积累多少误差，主动换视角是否增加碰撞风险，以及恢复可见性是否以偏离跟随距离为代价。摘要没有给出这些结果，也不能据此断言作者未评估。

- **判断**：值得读风险预测与循环控制器的配合方式，并核查绝对成功率；它把持续遮挡转成了一个具体可控制的问题。

## 研究关联

值得借鉴的是把感知条件纳入动作选择：跟随路线即使方向正确，也可能让机器人一直看不见目标。对于依赖持续观测的任务，动作的作用还包括改变接下来能获得什么信息。

### 下一步读哪里

先核查遮挡风险如何定义、预测多远，以及触发调整和恢复跟随的条件。再看 Risk 划分构成、绝对指标、与反应式跟随的公平对照及安全约束；输入未提供正文节选。

- **概念**：智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：25
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/VP-EVT Active Visibility Preservation for Embodied Visual Tracking.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied Visual Tracking (EVT) is an essential capability for intelligent robots in human-robot collaboration, requiring an agent to follow a designated target person in dynamic environments relying solely on egocentric visual perception. However, persistent pedestrian occlusions in dynamic scenes pose critical challenges to existing EVT methods. Lacking proactive visibility preservation, reactive tracking methods frequently experience prolonged target loss under severe occlusions. Therefore, we propose VP-EVT, a framework that treats target visibility as an explicit objective of motion control rather than a by-product of following. Acting on this objective requires understanding both what obstructs the target and how robot motion can change that obstruction. VP-EVT therefore uses language-guided perception to extract separate target and pedestrian observations. When occlusion makes current observations incomplete, VP-EVT combines visual history with ego-motion to maintain estimates of their relative positions and motion. Using these estimates and the current following waypoints, VP-EVT predicts whether continued following will sustain the obstruction. When the predicted risk is low, the original following motion is retained; otherwise, a recurrent controller combines updated estimates with maneuver context from preceding decisions to coordinate viewpoint adjustment and the return to stable following. Moreover, we introduce OccEVT-Bench for closed-loop evaluation of persistent occlusion and collect expert demonstrations for training. On its Risk split, VP-EVT improves success rate by 121.4% relative to a competitive baseline and reduces visibility deficit and longest target-loss duration by 78.8% and 74.4%, respectively.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21999v1
- Authors: Yanci Wen, Tianle Zeng, Jianwei Peng, Weixi Situ, Hanjing Ye, Hong Zhang
- Published: 2026-10-15T14:42:23Z
- Age days: 2

</details>
