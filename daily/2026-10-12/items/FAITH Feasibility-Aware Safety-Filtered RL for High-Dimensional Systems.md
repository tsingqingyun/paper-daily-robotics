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
url: "https://arxiv.org/abs/2610.12432v1"
published: "2026-10-08T17:57:06Z"
age_days: 3
score: 24
created: 2026-10-12
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# FAITH: Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems

> [!summary] 这篇论文到底做了什么（基于摘要）
> FAITH 把“完成任务”和“避免伤害”分给策略与动作过滤器：策略学习经过过滤后还能获得高回报的行为，过滤器负责修改危险动作。已经无路可安全走时，它转而寻找预测伤害最小的动作。

## 问题

任务是让高维机器人在安全限制下行动，尤其要处理已经进入危险状态的情况。把安全惩罚和任务奖励放进同一目标，可能产生相互竞争的更新；传统过滤器又依赖解析安全函数和动力学模型。只追求当前动作改得最少，也没有直接考虑长期回报；不存在安全动作时，硬投影甚至没有定义。

### 用一个例子理解

理解用例（非论文实验）：人形机器人收到穿过走廊的目标和当前状态，策略提出向前迈步；过滤器预测这会进入保护区，修改动作后执行。若已无法避免危险，它改选预测峰值伤害更小的动作。

## 创新点或方法

旧做法先学任务动作，再按即时偏差把它拉回安全集合。FAITH 学习状态—动作安全价值，并用前馈网络近似最小干预过滤；训练任务策略时，让它面对过滤后的动力学，因此策略能学到“这个动作会被改成什么”，而不是持续提出无法执行的动作。策略更新不再混入竞争性的安全项。推理时先过滤再执行；若学到的条件判定没有可行动作，同一过滤器趋向预测峰值伤害最小的动作。摘要未说明安全价值的监督来源和具体损失。

### 方法如何工作

1. 从状态与候选动作估计安全价值，为判断动作可不可执行提供依据；具体学习目标摘要未说明。
2. 过滤器近似最小干预修改，让可行状态下的执行动作满足学到的安全条件。
3. 任务策略通过过滤后的动力学学习回报，使它考虑动作修改对后续任务的影响。
4. 若没有动作满足条件，过滤器趋向预测峰值伤害最小的动作，避免硬投影无解。

### 必要术语

- 安全过滤器：执行前修改动作的机制；本文用它承担安全处理。
- 可行状态：存在满足安全条件的动作的状态；它决定过滤器采用哪种处理方式。
- 峰值伤害：伤害过程中的最高水平；本文在无安全动作时以预测值选择退路。

## 证据

摘要报告：在双积分器与 Safety Gym 中，FAITH 在可行起点零违规的方法里回报最高，在不可行起点达到最低伤害水平。29 自由度人形机器人的 Walking-Avoid 安全率为 99.95%，保留未过滤回报的 97%；Push-Avoid 中实测安全率最高，并学会牺牲平衡、向保护区域外跌倒。同一策略还在真机 Unitree G1 上演示。对比算法名称、试验次数及真机量化结果未给出，不能把上述比例直接视为真机保证。

## 局限

我的关键待核查问题是：学到的安全条件误判时，过滤器还能提供什么保证？摘要中的高安全率是实验结果，不等于所有状态都安全；真机演示也不足以确认不可行起点下的伤害最小化在现实中成立。

- **判断**：值得读方法与训练细节，核心价值在于解释任务策略如何适应安全过滤，以及不可行状态下如何定义合理退路。

## 研究关联

值得借鉴的是让任务策略适应实际执行接口：如果部署时动作必然经过约束处理，训练时也应让策略经历这种处理。它还提醒我们，“保持站立”与“保护某一区域”可能冲突，安全行为取决于伤害定义。

### 下一步读哪里

先核查安全价值究竟预测什么、如何学习，再看过滤器的可行性判断和不可行分支；实验重点检查安全率分母、伤害定义，以及仿真与真机结果如何分开报告。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：24
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-12/FAITH Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safe reinforcement learning commonly places safety and task performance in the same policy objective, where they can introduce competing updates. Safety filters separate them at action execution, but classical designs require an analytic safety function and dynamics model, and standard minimal-intervention filters are myopic to long-horizon task return because they minimize only instantaneous action deviation. Hard projections are also undefined when no safe action exists. We present FAITH, a feasibility-aware, model-free framework that approximates the optimal state-action safety value and amortizes minimal-intervention filtering with a feedforward network. The task policy optimizes the task return through the filtered dynamics, which recovers the feasible constrained problem without a competing safety term in the task-policy update. When no action satisfies the learned safety condition, the same filter approaches the action with minimum predicted peak harm. On a double integrator example and a Safety Gym environment, FAITH achieves the highest return among methods with no feasible-start violations and matches the lowest harm from infeasible starts. On a 29-DoF humanoid, it reaches a 99.95% safety rate while retaining 97% of the unfiltered return in Walking-Avoid, and obtains the highest measured safety rate in Push-Avoid by learning to sacrifice balancing and fall away from the protected region. The same policies are also demonstrated on a real-world Unitree G1 humanoid.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12432v1
- Authors: Songyuan Zhang, Baljeet Singh, Sarthak Ranjeet Kaingade, Chuchu Fan, Bryan Trinh
- Published: 2026-10-08T17:57:06Z
- Age days: 3

</details>
