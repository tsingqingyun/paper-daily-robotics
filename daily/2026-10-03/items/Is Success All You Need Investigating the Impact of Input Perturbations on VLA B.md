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
url: "https://arxiv.org/abs/2610.01351"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks

> [!summary] 这篇论文到底做了什么（基于摘要）
> Is Success All You Need? 检查机器人受到输入扰动后，即使仍然完成任务，动作是否变得绕路、抖动或抓夹不稳定。它给成功率补上了对成功轨迹执行方式的测量。

## 问题

任务是评估桌面操作 VLA 对输入扰动的稳健性。现有评估主要统计任务成功率，但这只能回答是否完成：两个模型成功率相近，完成任务时的动作质量仍可能明显不同。真正瓶颈是用一个终点指标代表整个执行过程。

### 用一个例子理解

理解用例（非论文实验）：同一取杯任务输入原图和改变光照后的图像；机器人两次都成功；评估程序读取轨迹，比较路径长度、动作平滑度和夹爪行为，输出“成功率相同，但执行方式发生变化”的行为报告。

## 创新点或方法

旧做法比较扰动前后的成功率；本文进一步对成功轨迹测量运动平滑度、效率和夹爪行为，同时观察典型行为与行为变异如何变化。作者将这种评估方式实现在 LIBERO 和 LIBERO-Plus 的扩展中。这里没有提出新策略训练方法，主要变化发生在测试与轨迹分析阶段；各指标的公式、扰动条件及轨迹匹配方式，摘要未说明。

### 方法如何工作

1. 让模型在基准条件及输入扰动条件下执行任务，记录成功状态和动作轨迹。
2. 对成功轨迹计算平滑度、效率和夹爪行为指标，使完成过程变成可比较的量。
3. 比较典型指标与变异程度，判断扰动是否改变执行方式或稳定性。
4. 结合成功率解释差异，识别终点表现相近但执行行为不同的模型。

### 必要术语

- 任务成功率（TSR）：完成任务的试验比例；本文指出它不能完整描述执行过程。
- 轨迹：机器人一次执行中的连续动作或状态记录；本文从中计算行为指标。
- 行为变异：多次执行之间行为差别的程度；本文用它补充典型行为的比较。

## 证据

摘要给出的评估范围是三个先进 VLA、四个 LIBERO 任务套件和七种扰动条件。作者发现，扰动会改变成功轨迹的行为，并找到相同扰动下成功率相近、成功轨迹行为明显不同的情况。这支持成功率不足以描述执行行为，但摘要没有模型名称、具体差异数值或统计显著性，也未报告真机验证。

## 局限

摘要未明确列出局限。我会特别核查只分析成功轨迹带来的筛选影响：扰动后留下的成功样本可能已经换了一批，行为差异不一定全由同一类轨迹改变造成。基准中的平滑度变化也不能直接等同于真机损伤或安全风险。

- **判断**：值得先读指标定义和成功样本的比较方法，再看结果；它的用途在于改变评估问题，而不是提供新的动作模型。

## 研究关联

这里最直接的启示是，验证一个策略是否可靠时，应同时检查它怎样成功。若部署条件关心动作平稳、执行时间或夹爪操作次数，可以把这些量加入测试，避免只凭成功率选择模型。

### 下一步读哪里

下一步核查七种扰动具体是什么、每项指标怎样计算、不同任务时长如何归一化，以及是否用配对初始状态控制比较；还应检查失败轨迹是否有另外的分析。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/Is Success All You Need Investigating the Impact of Input Perturbations on VLA B.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.01351v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have achieved high task success rates on robot manipulation task benchmarks. More recently, there has been an emphasis on evaluating the robustness of VLA models to perturbations. However, this robustness is still predominantly measured through Task Success Rate (TSR). In this work, we propose a benchmark-agnostic evaluation framework to measure the behavioural robustness of models by characterising how successful trajectories are executed under perturbation. We implement this methodology by extending the widely-used LIBERO and LIBERO-Plus benchmarks. Across three state-of-the-art VLA models, four LIBERO task suites and seven perturbation conditions, we evaluate changes in both typical successful behaviour and its variability, including metrics of motion smoothness, efficiency and gripper behaviour. We find that perturbations can alter the behaviour of successful trajectories, a phenomenon which cannot necessarily be inferred from TSR alone. Across LIBERO suites, we identify cases where state-of-the-art VLA models achieve comparable TSR under the same perturbation condition, yet behaviour on successful trajectories diverges substantially. Therefore, to have a more robust assessment of task performance, we argue that suitable measures of robustness should capture not only whether a task is completed, but also how the robot behaves while completing it. When evaluating the robustness of VLA models, TSR may be complemented by behavioural evaluation metrics that characterise the nature and variability of successful task execution by robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.01351
- Authors: Sophie Higham, Riccardo Andrea Izzo, Matteo Matteucci, Alessandro Suglia
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
