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
url: "https://arxiv.org/abs/2610.22368v1"
published: "2026-10-15T17:59:31Z"
age_days: 1
score: 32
created: 2026-10-17
concepts: ["智能体 Agent", "机器人学习"]
---

# Value as Memory: Online Value-Guided Post-training for General Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> VaM 把近期价值预测留作任务进度记忆，帮助机器人区分看起来相似、实际处于不同阶段的状态。它还把部署采集和在线强化学习接起来，让机器人更及时地用新经验更新策略。

## 问题

通用机器人策略在真实环境中继续学习时，当前观察可能不足以确定该做什么；同时，离线后训练不能及时吸收部署反馈。前者是动作判断缺上下文，后者是经验进入训练太慢。VaM 同时处理这两个问题，但两种机制的收益需要分开理解。

### 用一个例子理解

理解用例（非论文实验）：输入是机器人整理布料时的当前画面和近期价值预测；两次画面都像布角堆在一起，但价值历史可能提示它刚完成一次有效展开。策略据此选择下一动作，执行结果再进入在线训练。这里仅说明思路，不代表论文验证过这一具体流程。

## 创新点或方法

相较于只靠当前观察选择动作，价值缓存把近期价值预测也作为条件，给策略提供关于任务进展的历史线索。训练从离线强化学习预热开始，再结合离线演示、离策略干预和当前策略采集的轨迹，进入稀疏奖励下的在线学习。执行时策略读取近期价值；在线阶段同时采集数据和更新参数。价值定义、缓存长度、各类数据如何混合，摘要未说明。

### 方法如何工作

1. 用离线数据预热策略与价值学习，使机器人具备开始在线交互的基础。
2. 执行时缓存近期价值预测，给下一次动作选择补充任务进展线索。
3. 汇集演示、干预和当前策略轨迹，为更新提供不同来源的经验。
4. 在稀疏奖励下在线更新，并发进行采集与训练，让新经验更快影响后续策略；具体更新算法摘要未说明。

### 必要术语

- 价值预测：估计从某种状态继续执行能获得多少回报；本文还把它作为进度记忆。
- 稀疏奖励：只有少数时刻得到反馈；本文在线自主学习在这种反馈条件下进行。
- 离策略与同策略数据：分别来自其他行为方式和当前策略的经验；本文结合两者进行适配。

## 证据

摘要在涉及可变形物体和接触密集操作的长时程任务上，报告价值缓存带来平均绝对成功率增益 29.4%，按绝对差表述应理解为百分点；在线自主学习相对匹配的离线训练增益为 32.8%。相同梯度步预算下，所测在线日程进行了 8 倍策略迭代，并发采集训练时每梯度步记录耗时不足原来一半。摘要缺任务数量、原始成功率和重复次数，两项成功率增益不能相加。

## 局限

价值预测也可能把不同失败状态压成相近数值，不能等同于完整状态记忆，这是我的待核查问题。在线结果来自真实机器人后训练，但自主学习具体依赖多少干预仍需查证。相同梯度预算也不等于相同真机时间或数据成本。

- **判断**：值得深入读价值缓存消融和在线日程，因为它把记忆设计与部署反馈放在同一控制问题里，而收益来源需要仔细拆开。

## 研究关联

可借鉴的是用与控制目标直接相关的预测作为记忆。若价值变化能反映进展，它可能帮助区分相似画面对应的不同阶段；但价值是否足够稳定、足够区分阶段，必须通过实验确认。

### 下一步读哪里

先查价值预测目标、缓存形式以及是否有普通历史缓存对照；再查两项成功率增益各自对应的基线。在线实验应核查干预量、真机采集时长，以及策略迭代和每梯度步耗时的统计口径。

- **概念**：智能体 Agent 机器人学习
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/Value as Memory Online Value-Guided Post-training for General Robot Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world post-training of generalist robot policies faces two challenges: partial observability makes action selection ambiguous, while offline post-training methods delay feedback from deployment experience. We present Value as Memory (VaM), a framework that addresses these challenges through value caching and online real-world reinforcement learning (RL). Value caching conditions actions on recent value predictions as task-progress memory, while online updates enable timely policy improvement by combining offline demonstrations, off-policy interventions, and on-policy rollouts for sample-efficient adaptation. As a result, VaM transitions from offline RL warmup to online autonomous learning with sparse rewards. Across long-horizon tasks involving deformable objects and contact-rich manipulation, VaM yields a mean absolute success-rate gain of $29.4\%$ with value caching, while achieving a $32.8\%$ gain with online autonomous learning over matched offline training. The evaluated online schedule performs $8\times$ as many policy iterations under the same gradient-step budget, with more than $2\times$ lower recorded time per gradient step with concurrent data collection and training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22368v1
- Authors: Wenye Yu, Yijin Chen, Kaiyi Xiong, Wenbo Han, Wendi Chen, Yang Jin, Han Xue, Jun Lv, Cewu Lu, Chuan Wen
- Published: 2026-10-15T17:59:31Z
- Age days: 1

</details>
