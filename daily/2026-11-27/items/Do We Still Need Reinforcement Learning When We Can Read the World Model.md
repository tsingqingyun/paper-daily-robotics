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
url: "https://arxiv.org/abs/2611.34656v1"
published: "2026-11-25T16:29:37Z"
age_days: 1
score: 27
created: 2026-11-27
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Do We Still Need Reinforcement Learning When We Can Read the World Model?

> [!summary] 这篇论文到底做了什么（基于摘要）
> Read the World Model 让 LLM 编程智能体阅读环境源码，把状态怎样变化直接写成可执行的控制策略。智能体用在线反馈或离线数据反复改代码，省去针对该任务的强化学习训练。

## 问题

传统强化学习往往需要大量交互才能学会动作的后果。基于模型的强化学习已经利用环境模型来规划或优化策略。这里问的是，当环境规律能直接从源码读懂时，能否把这些规律直接写进决策规则，从而少靠试错。

### 用一个例子理解

理解用例（非论文实验）。输入一个库存模拟器的源码和当前库存。智能体读到订货有延迟，写出按预计到货前消耗量补货的规则。回放发现某些日子仍会缺货，就修改阈值。运行时，生成的策略根据库存和在途订单输出订货量。

## 创新点或方法

编程智能体在策略构建阶段阅读环境源码，推断哪些状态与动作后果有关，把推断写成可运行的规则，再根据在线试跑或离线数据修改规则。执行阶段由生成的代码决定动作。摘要未说明策略运行时能读哪些状态、能否调用环境模型，以及代码修订用掉多少模型调用。

### 方法如何工作

1. 读取环境实现，找出状态、动作以及与任务相关的后果。
2. 把推断出的规律写成可执行策略，让状态输入能够产生具体动作。
3. 用试跑反馈或离线数据识别规则的失效情形，迭代修改代码。
4. 运行合成策略并比较表现与经验用量，检验直接写规则能省下多少试错。

### 必要术语

- 可读世界模型：能够直接查看的环境规律描述；本文用环境源码作为策略合成的输入。
- 直接策略合成：把理解到的规则写成程序；生成的程序负责把执行时的输入转为动作。

## 证据

摘要称，生成策略在多种决策基准上与传统 RL 方法相当或更好，同时使用明显更少的经验。作者还比较了能读源码和不能读源码时生成的策略，并分析了规则怎样随反馈修订。摘要未给具体环境、指标数值、基线配置或经验计量口径。结果支持在所测的可读环境中尝试直接合成策略。

## 局限

摘要提供的是决策基准证据，真机适用性仍待核查。最影响公平比较的是源码里有哪些信息，以及生成的策略在执行时是否只使用与 RL 基线相同的观测。交互量和代码生成成本也需要分别计量。

- **判断**：值得优先读实验协议，尤其是源码访问、执行观测与交互预算，因为它们决定了这个结果能回答多大范围的 RL 替代问题。

## 研究关联

如果任务已有可读的仿真规则或业务约束，可以先用规则合成策略，再看反馈揭示了哪些必须靠经验补上的缺口。生成物是代码时，还能检查具体哪条判断在何处失效。

### 下一步读哪里

核查读源码组与不读源码组是否有相同反馈预算，执行时看到的状态是否一致，以及传统 RL 基线能访问什么信息。再读一个规则修订案例，看反馈纠正的是对环境规律的理解，还是某个经验阈值。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/Do We Still Need Reinforcement Learning When We Can Read the World Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically used to support planning or policy optimization. In this paper, we investigate an alternative paradigm in which autonomous LLM-based coding agents directly synthesize control policies by reasoning over readable world models. By examining environment source code, these agents translate environmental knowledge into executable decision rules and iteratively refine their policies using online feedback or offline data, without task-specific RL training. Experiments across diverse decision-making benchmarks show that synthesized policies match or outperform conventional RL methods while requiring substantially less experience. Further analyses reveal interpretable decision rules and how they evolve through feedback-driven refinement. Comparisons with policies generated without source code access and experiments under challenging conditions further demonstrate the benefits of readable world models. These findings suggest that direct policy synthesis can reduce reliance on trial and error, challenging the necessity of task-specific RL training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34656v1
- Authors: Mingchao Zhang, Miduo Cui, Kangze He, Yuanjun Li, Dapeng Li, Ce Zhang, Chuanchen Luo, Xue Yan, Mingzhe Xing, Zhumin Chen, Hangyu Mao, Bin Zhang, Zhiwei Xu
- Published: 2026-11-25T16:29:37Z
- Age days: 1

</details>
