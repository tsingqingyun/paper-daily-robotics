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
url: "https://arxiv.org/abs/2610.39054v1"
published: "2026-10-28T23:31:24Z"
age_days: 4
score: 26
created: 2026-11-02
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Robotic Data Inoculation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Data Inoculation（DI）在人工遥操作时主动给命令加偏差，让人边操作边示范如何纠正。巧处是偏差由持续学习的策略产生，尽量提前收集未来策略可能犯错时的恢复数据。

## 问题

模仿学习容易因小错误偏离示范轨迹，进入没见过、不会恢复的状态。人工采集通常依靠经验保证覆盖；纯在线强化学习探索成本高，DAgger 式纠正则要等策略偶然走错才获得恢复示范。

### 用一个例子理解

理解用例（非论文实验）：人遥控机械臂把物件放进盒子，残差使夹爪稍偏离入口；人观察后修正并完成放置。记录的偏离状态和纠正动作成为训练数据，最终策略学习从这些状态恢复。

## 创新点或方法

本文把正常遥操作改成共享控制：人持续给命令，残差策略叠加扰动，人再闭环修正。残差策略用不断增长的数据在线训练，优化目标与之后提取策略时的奖励目标一致，使采集偏向学习器可能出现的偏差。扰动发生在采集阶段；部署时使用这些数据训练的策略，摘要没有说还需人工或保留扰动模块。

### 方法如何工作

1. 人提供连续遥操作命令，建立可完成任务的行为基础。
2. 残差策略叠加偏差，把机器人带到普通示范较少覆盖的状态。
3. 人持续纠正，记录偏离后的恢复动作，补上数据缺口。
4. 用增长的数据更新残差策略，并用采集数据训练下游策略，让后续采集继续针对可能的错误。

### 必要术语

- 残差策略：在原命令上增加修正量的策略；本文用它产生采集扰动。
- 闭环遥操作：人根据当前反馈不断调整命令；本文借此获得恢复示范。
- 离线强化学习：从已有数据中按奖励学习策略；是本文检验数据用途的一种方式。

## 证据

摘要报告三个有挑战的真机任务，DI 数据训练出的行为克隆和离线强化学习策略，成功率持续优于或追平对照。没有给任务名称、对照采集方式、成功率数字、采集时长和人工投入，因此能说明跨两种学习方式有收益迹象，尚不能判断单位采集成本。

## 局限

人保持控制不等于扰动天然安全，摘要未说明幅度限制、接管机制或操作者负担。我还会检查：在相同人工时间下收益是否保留，以及收益来自针对性偏差还是一般扰动增加了状态覆盖。

- **判断**：值得细读采集协议与等成本对照，因为这篇最可借鉴的是怎样制造有用错误，而不是单独一个策略结构。

## 研究关联

它把数据覆盖从“操作员尽量多演示”变成“主动暴露学习器的偏差，再示范恢复”。当失败主要来自偏离熟悉轨迹时，采集过程本身可能比继续增加顺利完成的示范更值得改。

### 下一步读哪里

核查三个任务、残差动作约束、在线更新频率、奖励来源，以及是否控制演示数量、人工时长和操作者差异；摘要未提供这些细节。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/Robotic Data Inoculation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Modern robot learning systems feed on high-quality demonstration data, and their performance hinges on coverage. Without good coverage, small errors compound and the policy can quickly go into out-of-distribution states from which it cannot recover. Yet there is no principled way of collecting high-coverage data, and data collection often relies on heuristic instructions to human operators. Purely online reinforcement learning (RL) explores at the cost of safety and sample efficiency, while DAgger-style interventions require the policy to fail by chance before a human can correct it. In this paper, we ask instead whether we can modify how the robot behaves during data collection to collect more useful data. We propose Data Inoculation (DI), a shared-control framework in which a human provide closed-loop teleoperation commands while a residual policy perturbs these commands. The residual policy is trained online, on the growing dataset, with the same reward-maximizing objective later used for policy extraction, so its perturbations steer data collection toward the deviations a policy trained on the data would make. These perturbations expose the robot to a wider range of states, while the human's continuous corrections provide recovery demonstrations, "inoculating" the dataset against the learner's future mistakes while the human remains in control. On three challenging real-world robotic tasks, DI consistently improves or matches the success rate of policies trained with both behavioral cloning and offline RL, showing DI as an effective data collection strategy for improving downstream policy performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39054v1
- Authors: Qiyang Li, Zhiyuan Zhou, Charles Xu, Sergey Levine
- Published: 2026-10-28T23:31:24Z
- Age days: 4

</details>
