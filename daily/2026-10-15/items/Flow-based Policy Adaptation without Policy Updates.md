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
url: "https://arxiv.org/abs/2606.06461"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 41
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Flow-based Policy Adaptation without Policy Updates

> [!summary] 这篇论文到底做了什么（基于摘要）
> GLOVES 给已有策略加一个动作纠正模块：原策略提出要怎么动，模块只在动作偏离专家行为分布时出手。它训练一个轻量先验，无须更新原策略参数。

## 问题

通用策略可能懂任务和场景，却不熟悉具体环境及机器人身体，导致动作执行不准。任务是保留原策略的任务知识，同时补上局部执行能力；摘要没有展开其他适配方案的具体缺点，不能据此声称所有微调方法都低效。

### 用一个例子理解

理解用例（非论文实验）：输入当前画面及原策略提出的一段靠近抽屉把手的动作；GLOVES 判断其是否符合本地专家行为，必要时修正接近动作，输出供机器人执行的动作片段。

## 创新点或方法

原策略单独执行时，任务意图和具体动作都由它承担；GLOVES 在输出动作片段后增加纠正。训练时，学习以观测为条件、但不以目标为条件的专家动作先验，原策略保持不变。推理时，先用反向流评估动作是否符合专家分布：符合则直接放行，异常则纠正。原动作提供任务方向，先验提供局部行为约束；如何在纠正中保持意图、流模型如何训练，摘要未给出公式。

### 方法如何工作

1. 先用观测与专家动作学习局部行为先验，为纠正提供环境和身体相关知识。
2. 执行时接收原智能体的动作片段，让原策略继续表达任务意图。
3. 通过反向流评估动作与专家分布的一致性，得到是否需要干预的信号。
4. 对一致动作直接放行，对异常动作进行纠正，再交给机器人执行；具体纠正计算摘要未说明。

### 必要术语

- 动作先验：从专家数据学到的动作规律；本文用它约束局部执行。
- 目标无关：先验不以任务目标为条件；任务意图主要由原策略动作提供。
- 流模型：学习分布及其变换的模型；本文用于动作适配与分布一致性评分。
- 干预门控：决定是否启动纠正的判断；本文让正常动作保持原样。

## 证据

摘要列出受控分布外恢复研究、仿真基准和真机实验，并称 GLOVES 持续改善 VLA 与 Code-as-Policy 智能体的成功表现，且不重训底层策略。但没有任何成功率数值、具体任务、基线名单或统计信息，因此只能确认作者报告了跨这些测试类别的改善，无法比较收益大小，也不能判断额外延迟。

## 局限

我的关键待核查问题是：任务所需的新动作会不会被误判为异常并纠正？分布内评分衡量的是与专家行为的一致性，不能直接当作任务正确性或安全性的证明；真机评测也不等于已覆盖所有接触风险。

- **判断**：值得读纠正公式和干预门控实验，因为保留任务意图与避免错误干预，是这套方法成立的核心。

## 研究关联

它把“懂目标”和“动作像不像熟练执行”分成两种知识。若已有策略的任务判断可用，而错误集中在局部动作，训练一个可复用的动作先验可能比重新学习整套任务策略更合适；前提是专家数据覆盖需要修正的局部行为。

### 下一步读哪里

下一步检查专家数据规模与覆盖范围、异常阈值如何选、纠正幅度如何限制，以及始终纠正和按需纠正的对照。还应核查失败案例是否包含有效新动作被误改，以及实际推理开销。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/Flow-based Policy Adaptation without Policy Updates.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.06461v2 Announce Type: replace Abstract: Foundation models and other policies trained on large and diverse datasets can endow robots with semantic and task knowledge that would be difficult to acquire from task-specific demonstrations alone. Despite their broad scene understanding and reasoning capabilities, however, these models often lack the environment- and embodiment-specific knowledge required for precise and reliable execution. We propose GLOVES, a flow-based framework that complements an existing agent with a lightweight, goal-agnostic expert action prior that refines the action chunks proposed by the agent without updating its parameters. The prior captures observation-conditioned expert behavior, while the agent's proposal supplies task- and context-specific intent that the correction aims to preserve. The learned flow also provides a natural in-distribution scoring mechanism through reverse flow evaluation. We use this signal as an intervention gate: actions that appear consistent with the expert distribution are passed through unchanged, while anomalous or out-of-distribution (OOD) actions are corrected. In this way, GLOVES only provides assistance when necessary. By learning local goal-agnostic expert action patterns and using them to adapt agent-proposed actions during execution, GLOVES provides a lightweight shared-control module for robust action adaptation across tasks and environments. Across controlled OOD-recovery studies, simulation benchmarks, and real-robot experiments, GLOVES consistently improves the success of vision-language-action models (VLAs) and Code-as-Policy agents without retraining the underlying policy. Code and demos are available at ripl.github.io/GLOVES_web.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06461
- Authors: Luzhe Sun, Jingtian Ji, Haoran Chen, Jiawei Zhou, Matthew R. Walter
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
