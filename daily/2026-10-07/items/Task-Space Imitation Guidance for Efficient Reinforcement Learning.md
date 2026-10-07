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
url: "https://arxiv.org/abs/2610.07527v1"
published: "2026-10-05T23:49:17Z"
age_days: 1
score: 29
created: 2026-10-07
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Task-Space Imitation Guidance for Efficient Reinforcement Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> TIGER 把模仿策略预测的动作转换成末端执行器短程目标，用“有没有朝目标前进”给强化学习提供密集反馈。强化学习仍自己选动作，最终主要追求环境的稀疏任务奖励。

## 问题

任务是稀疏奖励的桌面操作：机器人尝试很多动作，却很少得到成功信号，早期探索容易偏离合理行为。TIGER 要利用示范中的方向信息帮助学习。摘要没有具体解释各个既有 RL 或 IL-RL 基线的失败机制，只明确区分了本文与直接执行模仿策略、把它用作动作先验的做法。

### 用一个例子理解

理解用例（非论文实验）：输入当前观测和“把积木放进盒子”，模仿策略预测一段移动动作，映射后形成夹爪短程参考；RL 自选动作，向参考推进时得到密集反馈，真正放入盒子时得到环境成功奖励。

## 创新点或方法

常见利用方式是让模仿策略给动作或约束动作选择；本文让它估计局部任务进展。预测动作块先经考虑控制器语义的动作到运动映射，变成短程末端参考，再据此构造朝参考前进的密集奖励，同时保持环境稀疏奖励的主导地位。预训练还用模仿引导的前瞻信号，对预计能产生任务空间进展的动作放松保守价值惩罚，减少早期在线探索偏离数据覆盖范围。摘要未说明奖励权重、预训练损失，或部署时是否仍需调用模仿策略。

### 方法如何工作

1. 模仿策略根据观测预测动作块，提供短期行动方向。
2. 通过考虑控制器的映射把动作变成末端运动参考，使不同动作表达能落到实际运动上。
3. 训练时根据朝参考的进展给密集奖励，同时以环境稀疏奖励维持最终任务目标。
4. 预训练用前瞻进度信号调整保守价值惩罚，为后续在线 RL 提供更有方向的起点。

### 必要术语

- 任务空间：这里指末端执行器运动所在的空间；用于表达短程参考与进度。
- 稀疏奖励：只有少数状态或成功时才给反馈；是本文补充密集提示的原因。
- 保守价值惩罚：压低部分动作价值估计的训练约束；本文对预计有进展的动作放松它。
- 离开数据流形：动作偏离已有数据支持的行为范围；本文希望减少早期这类探索。

## 证据

摘要报告仿真与真机操作实验，并称相对已有 RL 和 IL-RL 基线，早期样本效率更高、测得的安全违规更少，最终成功率持平或更高。没有任务名称、基线名称、交互次数、违规定义及数值，因此只能把结论限定为所评估任务上的报告趋势，不能判断收益幅度，也不能视为通用安全保证。

## 局限

我的待核查问题是错误示范预测会不会提供误导奖励，以及需要暂时远离目标的动作会不会被压制。控制器映射也决定参考是否可信，换机器人后未必可直接复用。摘要报告违规减少，尚不能推出风险约束或安全因果保证。

- **判断**：值得读到奖励公式和预训练消融，因为把模仿输出变成进度信号是清楚且可借鉴的改动；效果大小仍需实验表格确认。

## 研究关联

值得借鉴的是把示范策略当作“短期往哪走有进展”的参考。这样可在利用示范方向信息的同时，让 RL 继续针对最终任务结果学习不同动作。前提是预测动作确实能转换成有意义的末端进度，且局部进度与任务完成足够一致。

### 下一步读哪里

下一步检查动作到运动映射如何处理不同控制器、进度奖励和稀疏奖励的相对权重、保守惩罚放松条件；再找奖励引导与预训练分别贡献多少，以及违规指标如何定义。输入没有正文节选。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/Task-Space Imitation Guidance for Efficient Reinforcement Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce Task-Space Imitation Guidance for Efficient Reinforcement Learning (TIGER), a reward-construction and pretraining framework for sparse-reward tabletop robotic manipulation. TIGER treats an action-chunked imitation policy not as an executable controller or action prior, but as a local task-space progress estimator: predicted action chunks are converted, using controller-aware action-to-motion mapping, into short-horizon end-effector references, and the RL agent receives dense progress rewards toward these references while the sparse environment reward remains the dominant objective. During pretraining, TIGER uses imitation-guided look-ahead signals to relax conservative value penalties for actions predicted to make task-space progress, reducing off-manifold exploration during early online RL. Across simulation and real-robot experiments, TIGER improves early sample efficiency and reduces measured safety violations while matching or improving final success rates relative to prior RL and IL-RL baselines on the evaluated tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.07527v1
- Authors: Salar Asayesh, Hossein Darani, Todd Cao, Evgeny Andriash, Mani Ranjbar
- Published: 2026-10-05T23:49:17Z
- Age days: 1

</details>
