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
url: "https://arxiv.org/abs/2611.33772v1"
published: "2026-11-25T04:57:52Z"
age_days: 1
score: 28
created: 2026-11-27
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform

> [!summary] 这篇论文到底做了什么（基于摘要）
> 机器人硬件已经定了，排行榜第一的模型也可能看不到关键区域，或者赶不上控制时限。TRIAGE 先用传感器和端到端时延筛掉不可用的模型，再用本地数据试探哪些问题值得微调，最后用闭环测试决定能否上线。

## 问题

选型时平台已固定，本地数据很少，基准分数却无法告诉你模型能否在这台机器上跑。相机没拍到的信息无法从这些画面里补回来，动作算完时控制时限已过也要从控制链路下手。微调能处理的是第三类差距，即平台已经采到、模型却还不适应的数据分布。

### 用一个例子理解

理解用例（非论文实验）。给固定相机的巡检车挑控制模型。先输入相机覆盖和控制时限，筛掉看不全转角或来不及输出的候选。再用仓库日志比较剩余模型，对入选者做本地适配，最后根据闭环试跑决定是否放行。

## 创新点或方法

过去按榜单挑权重再微调。TRIAGE 把观测要求和推理时限变成硬门槛，先淘汰不合格候选，再用短段本地日志做探测，只在通过者中按目标任务得分排序。微调阶段监测适配效果，放行前让模型控制车辆，观察动作改变后续观测时的实际表现。摘要未说明微调目标与监测触发条件。

### 方法如何工作

1. 把任务所需的观测与实际传感器覆盖对照，确认候选拿得到所需信息。
2. 测量观测到动作的端到端时延，淘汰赶不上控制时限的候选。
3. 用摘要所说的 10 分钟本地日志做探测，观察候选碰到本地分布时的表现。
4. 按目标任务得分排列通过者，再对入选模型做监测下的微调。
5. 让适配后的模型闭环运行，以实际验收决定是否放行。

### 必要术语

- 传感器契约：任务对可用观测的要求；用来检查现有硬件是否提供候选所需的信息。
- 闭环：模型的动作会改变下一次收到的观测；用来检查离线改善能否兑现为实际运行改善。

## 证据

摘要报告，在驾驶基准中，截止时间短于领先闭环模型的实际时延时，80%–90% 的路线发生碰撞。同像素数下，缩小视野导致的规划变化是降低分辨率的 2.2–5.7 倍。本地帧补回 75% 的稳定性差距，但小数据预算下扰动敏感性上升。实车上，加装相机后通过传感门槛。因时延被筛掉的两名最高分候选均未跑完闭环行程，入选模型通过 4/5 次验收。一次离线改善的微调版本被闭环检查拦下。结果支持在所测平台上先检查可行性。

## 局限

摘要给出的视野与分辨率比较来自驾驶基准，实车验收只有 5 次。值得核查实车路线与工况的覆盖，以及时延测量是否包含偶发慢帧，这会影响门槛能否用于部署。

- **判断**：值得读到门槛定义和实车验收流程，因为这两处决定了选型在换平台后能否复用。

## 研究关联

本地数据很少时，可以先判断哪种投入会改变结果。视野有缺口就查观测覆盖，输出超时就查整条控制链路，硬件和链路都达标后，再花样本预算处理模型对本地分布的不适应。

### 下一步读哪里

先查传感器契约怎样按任务定义，再看时延从哪一步量到哪一步。最后核查被拦下的微调模型在哪项离线指标上进步，又触发了哪条闭环验收条件。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/Triage Before Fine-Tuning Feasibility-Gated Selection and Monitored Adaptation o.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied foundation models are increasingly deployed by selection: a practitioner picks a public checkpoint by benchmark rank and fine-tunes it on local data. The platform is fixed before the model is chosen, with little or no local data. We ask what such a checkpoint loses on a fixed platform and which part of the loss local data can buy back. We split the gap by what can repair it. A sensing gap, information the sensors do not capture, cannot be closed with their data; a latency gap, output arriving after the control loop needs it, belongs to the loop, not the weights; only a distribution gap is fine-tuning's to repair. TRIAGE turns this into feasibility-gated selection and monitored adaptation in five stages: gates on the sensor contract and on end-to-end latency that no score can override, probes on ten minutes of local logs, a ranking by target-relevant score among the candidates that pass, and fine-tuning that is monitored and checked in closed loop before release. On driving benchmarks, a deadline below a leading closed-loop model's latency makes it collide on 80 to 90% of routes, and losing field of view moves plans 2.2 to 5.7 times more than losing resolution at equal pixels. Local frames close 75% of a stability gap but raise perturbation sensitivity at small budgets, and picking by score violates a gate in two of four deployment profiles. On a full-scale vehicle, the factory camera failed the sensing gate and an added camera repaired it. The latency gate removed the two highest-scoring candidates, neither of which completed a closed-loop trip. The selected model passed acceptance in 4 of 5 closed-loop trips, and the closed-loop check withheld a fine-tuned model that had improved offline. TRIAGE lets organizations that cannot train foundation models from scratch find out whether a public checkpoint can run on the robot or vehicle they own, and what to fix if not.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33772v1
- Authors: Zilin Huang, Zhengyang Wan, Zihao Sheng, Boyue Wang, Ruolin Yang, Yuhao Luo, Sikai Chen
- Published: 2026-11-25T04:57:52Z
- Age days: 1

</details>
