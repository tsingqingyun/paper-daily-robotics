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
url: "https://arxiv.org/abs/2611.33722v1"
published: "2026-11-25T03:36:01Z"
age_days: 3
score: 23
created: 2026-11-28
concepts: ["具身智能评测与基准"]
---

# Practice Makes Fluent: Learning to Use Earlier Predictions in Looped Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> FLUENT 让反复运行同一组权重的模型学会少跑几轮。它用原模型的最后一轮预测训练早期输出，同时稳住末轮，再教退出门判断继续计算是否值得。

## 问题

循环模型每轮都有预测，本可以在某些输入上提前停下。但各轮共享参数，训练早期预测时也会改变末轮预测，可能损害完整计算的结果。早期输出还在变，负责决定何时停止的门控也要跟上这种变化。

### 用一个例子理解

理解用例（非论文实验）：机械臂接到把杯子移到托盘上的指令。动作头先生成一版移动指令，退出门判断当前预测是否值得再算一轮。视野清楚时可能更早输出，遮挡时可以继续迭代，最终把选中轮次的动作交给控制器。

## 创新点或方法

FLUENT 先冻结初始模型，用它的末轮预测监督当前模型的早期输出，同时约束当前模型的末轮向同一个教师靠拢。训练退出门时，参照改用当前模型的末轮，因为门需要判断此刻的早期预测还差多少。门控目标在这份分歧和继续循环的计算代价之间取舍。训练无需额外任务标签或奖励。推理时按门的决定继续迭代或输出中间预测。

### 方法如何工作

1. 冻结初始模型的末轮预测作为训练参照，给共享权重的后续更新一个稳定目标。
2. 同时训练早期轮次和末轮接近这个参照，让早期预测更早可用，并约束末轮漂移。
3. 用早期输出与当前末轮的分歧及计算代价训练退出门，推理时由门选择何时输出。

### 必要术语

- 循环模型：用共享权重迭代更新预测的模型。在本文中，每轮输出都可成为退出候选。
- 蒸馏：用已有模型的预测作为学习目标。在本文中，冻结教师供早期轮学习，也约束当前末轮。
- 退出门：决定停止还是继续计算的模块。在本文中，它按预测分歧与计算代价学习取舍。

## 证据

摘要报告，FLUENT 在新的 Crafter 世界中较浅时表现更好，在 LIBERO 用更少动作头迭代取得更高成功率，在语言建模中以更低的选定深度维持准确率。真机成功率由 62.3% 升至 74.6%，成功回合的平均耗时由 69 秒降至 31 秒。摘要未给出各项基线配置、真机任务细节或样本量，真机耗时也只统计了成功回合。

## 局限

门控看的是早期与当前末轮的分歧，两者可能在困难输入上同时出错。我会核查退出深度、任务成功和实际耗时的关系，以及真机时间差中有多少来自计算、多少来自动作执行。真机结果展示的是成功率和成功回合耗时同时改善，摘要不足以确定各训练项的独立作用。

- **判断**：值得读到退出门的目标函数和消融，重点看两个末轮参照如何分工，以及减少迭代能节省多少端到端时间。

## 研究关联

可以把提前退出拆成两个学习目标：让早期输出更有用，再依据当前版本的预测判断是否值得多算一轮。对共享权重模型，冻结教师还能给末轮质量提供一个固定参照。

### 下一步读哪里

先核对蒸馏、末轮锚定和门控损失各自的参照，再检查计算代价系数如何影响退出深度。看真机评估时，核对失败回合的计时口径及推理时间和动作执行时间是否分别统计。

- **概念**：具身智能评测与基准
- **筛选分数**：23
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/Practice Makes Fluent Learning to Use Earlier Predictions in Looped Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

People become faster at a task through practice, but models that improve with experience do not necessarily learn to use less computation. We train looped models, whose intermediate predictions allow earlier exits, to perform tasks with fewer iterations through practice. This is difficult because shared-weight updates can degrade the final-loop prediction while improving early ones, and the exit gate must track early predictions as their quality changes. We propose FLUENT, which requires no additional task labels or rewards: it distills the initial model's final-loop prediction into early predictions, anchors the current final-loop prediction to the same frozen teacher, and trains the exit gate to balance disagreement with the current final-loop prediction against computation cost. FLUENT improves performance at shallower depth in new Crafter worlds, raises LIBERO success with fewer action-head iterations, and maintains language-model accuracy at lower selected depth. On a real robot, success rises from 62.3\% to 74.6\% while mean time over successful episodes falls from 69\,s to 31\,s. The project page is available at https://msseok96-cpu.github.io/FLUENT/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33722v1
- Authors: Minseok seo, Hee-Seon Kim, Changick Kim
- Published: 2026-11-25T03:36:01Z
- Age days: 3

</details>
