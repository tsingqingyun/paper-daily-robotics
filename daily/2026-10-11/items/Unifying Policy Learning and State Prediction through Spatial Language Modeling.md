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
url: "https://arxiv.org/abs/2610.12172v1"
published: "2026-10-08T15:43:08Z"
age_days: 2
score: 28
created: 2026-10-11
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Unifying Policy Learning and State Prediction through Spatial Language Modeling

> [!summary] 这篇论文到底做了什么（基于摘要）
> Spatial Language Modeling 用同一套坐标和语义 token 表达场景、目标、动作以及动作后的状态，让一个 Transformer 同时学“往哪推”和“推完会怎样”。控制时，它只生成可执行动作，再用实际观察更新历史。

## 问题

任务是把物体推到目标位置。只学习示范中的动作选择，可能没有充分利用“某个动作会怎样改变物体几何状态”的监督。本文要让这种状态变化知识帮助目标导向控制；摘要没有逐一说明已有策略的具体缺陷。

### 用一个例子理解

理解用例（非论文实验）：输入桌上 T 形块的轮廓和目标轮廓，模型输出推杆应到达的坐标；执行后拍摄新状态，将其加入历史，再生成下一次推的位置。

## 创新点或方法

相对于单独学习动作，本文把场景轮廓、目标、动作目标和未来状态组织进共同序列，用下一 token 预测训练同一个模型。先从零开始用随机操作产生的转移预训练：记录的动作坐标作为条件，不计入预测损失，让模型学习给定动作后的状态。随后用专家示范联合训练动作和状态。实际控制时只解码动作目标，随后接入新观察，而不是必须靠自己预测的状态继续执行。

### 方法如何工作

1. 把轮廓、目标和动作目标编码为共享 token，使动作选择与状态变化可以放进同一序列。
2. 用随机操作中的已知动作预测后续状态，先学习动作造成的几何变化。
3. 用专家示范联合训练动作和状态，让模型同时接触目标导向决策及其后果。
4. 控制时只生成可执行动作，执行后用新观察更新历史，使下一次决策依据实际状态。

### 必要术语

- 空间语言建模：用离散坐标和语义符号组成空间序列；是本文统一动作与状态的表示方式。
- 自回归：根据已有序列逐个生成后续 token；同一模型据此生成动作或状态。
- 随机操作预训练：先学习非专家操作产生的状态转移；为后续控制提供动作后果知识。

## 证据

摘要报告在 Push-T 仿真和真实机器人上评测：仿真表现具有竞争力，真机成功率与目标覆盖率高于所评测策略基线。消融显示，联合动作与状态序列改善控制，随机操作预训练带来进一步收益；给定动作轨迹时，同一模型还能预测连续状态。摘要未提供基线名称、数值、试验次数和方差，因此无法判断优势规模，也不能推广到其他操作任务。

## 局限

我会核查离散坐标精度、轮廓提取方式，以及遮挡或轮廓误差对控制的影响。真机证据确实存在，但范围仍是摘要所述的推动任务；能预测推动几何变化，也不能直接推出它已学会完整接触动力学。

- **判断**：值得细读序列语法和训练消融，因为它明确区分了学习动作后果与实际控制，能帮助理解状态预测监督究竟如何改善策略。

## 研究关联

值得借鉴的是把容易获得的随机操作记录用于学习动作后果，再用专家示范学习如何选动作。这样，即使一段操作没有完成目标，其中的状态变化仍可成为训练材料。

### 下一步读哪里

先看序列语法如何安排动作和状态、随机操作阶段怎样屏蔽动作损失，再核查联合训练消融是否控制数据量和训练预算；真机部分重点看基线、成功定义与观察误差。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/Unifying Policy Learning and State Prediction through Spatial Language Modeling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning how actions change scene geometry can provide complementary supervision for goal-directed manipulation. We introduce Spatial Language Modeling, which represents scene contours, goals, action targets, and future states with a shared vocabulary of discrete coordinates and semantic tokens. A task-specific grammar organizes these elements into spatial sequences, allowing one autoregressive Transformer to learn action generation and action-conditioned state prediction through a common next-token objective. We train the model from scratch using random-play transition pretraining followed by joint action and state training on expert demonstrations. During pretraining, recorded action coordinates condition subsequent state predictions and are excluded from the prediction loss. During control, the model decodes only executable action targets and updates its history with newly observed states. We evaluate the approach on Push-T in simulation and on a real robot. The model achieves competitive simulation performance and higher task success and target coverage than the evaluated real-robot policy baselines. Training ablations show improved control with joint action and state sequences, with further gains from random-play pretraining. Given supplied action trajectories, the same model also predicts successive scene states, capturing the geometric effects of pushing.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12172v1
- Authors: Minye Wu, Zehao Wang, Tinne Tuytelaars
- Published: 2026-10-08T15:43:08Z
- Age days: 2

</details>
