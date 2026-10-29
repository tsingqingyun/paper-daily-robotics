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
url: "https://arxiv.org/abs/2610.37547v1"
published: "2026-10-27T16:58:54Z"
age_days: 1
score: 29
created: 2026-10-29
concepts: ["机器人学习", "具身智能评测与基准"]
---

# When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> ARC 专门修补机器人策略在精细操作处的局部失误，保留原策略不动，只学习附加纠正。人类纠正用来指出何时介入、往哪些方向探索，最终纠正动作由强化学习的任务奖励决定。

## 问题

任务是改善已经能完成大部分轨迹、却在最后精确对齐等局部阶段失败的模仿策略。摘要指出，更新整个策略或在所有位置探索残差，把局部故障变成了全局学习问题，浪费了原策略已经掌握的行为。

### 用一个例子理解

理解用例（非论文实验）：机器人把插头送到插座附近却插不进去；人的少量纠正显示应在接近插口时介入，并主要调整几个方向。ARC 据此限定探索，再按是否插入成功学习最终修正。

## 创新点或方法

ARC 在冻结策略上增加轻量残差模块。训练时，人的介入前状态用于学习何时启用纠正；纠正动作的几何结构用于限制残差探索方向；强化学习再根据任务奖励决定具体修正。因此人的动作不是必须复现的标签，而是探索线索。推理时原策略提供基础动作，模块在需要时附加残差。介入判定模型、奖励定义和训练期间的安全措施，摘要未说明。

### 方法如何工作

1. 冻结已能完成大部分轨迹的策略，保留已有能力，并采集少量人工纠正。
2. 利用介入前状态确定纠正应在哪些局部阶段启动，避免全程探索。
3. 从纠正动作提取主要变化方向，把七关节残差探索限制到任务相关子空间。
4. 在受限空间内按任务奖励学习具体残差，执行时将其加到基础动作上。

### 必要术语

- 残差动作：加在原策略动作上的修正量；使 ARC 无需重学整套行为。
- 介入门控：决定何时启用纠正的机制；把学习集中到易失败阶段。
- 低维子空间：完整动作空间中的少数变化方向；用于缩小自主探索范围。
- 平方幅值：各维纠正量平方的总和；本文用其衡量低维空间保留了多少纠正变化。

## 证据

摘要报告三个真机精密操作任务，平均成功率从 33.3% 提高到 75.0%。人的纠正定义了七关节残差空间中的任务相关二维或三维子空间，保留 96.0%—97.7% 的纠正平方幅值。这说明观测到的纠正主要集中在少数方向，但不保证最优纠正也在其中。摘要未给任务名称、试验次数、人工介入量和训练耗时，无法判断稳定性与成本。

## 局限

我的待核查问题是：收益分别来自介入门控、低维探索还是额外强化学习，以及限制方向会不会排除必要动作。三个任务的平均提升不代表每个任务同幅改善，也不能推到整段轨迹都不可靠的策略。

- **判断**：值得细读方法与分项消融，尤其适合借鉴其使用人工纠正的方式；是否省人工和训练时间，还需成本数据。

## 研究关联

这里值得借鉴的是把人的帮助用作搜索结构：人可以准确指出哪里有问题，却未必给出最佳动作。对于失败集中在少数阶段的策略，可以先限定纠正时机和方向，再让任务反馈寻找具体解。

### 下一步读哪里

优先核查介入前状态如何构成训练样本、低维空间怎样提取，以及不设门控、不限制方向和直接模仿人类纠正的对照；还需查看每个任务的成功率与人工成本。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/When, Where, and What to Correct Human-Guided Adaptive Residual Correction for R.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Imitation policies that reliably execute most of a manipulation trajectory can still fail in localized regions requiring last-mile precision. Updating the full policy or exploring residual actions everywhere treats this local failure as a global learning problem. We introduce Adaptive Residual Correction (ARC), a lightweight post-training module that uses reinforcement learning (RL) to learn a residual correction on top of a frozen policy while using sparse human corrections to structure autonomous exploration. Rather than treating human corrections as imitation targets, ARC uses pre-intervention states to determine 'when' residual control should become active and correction geometry to determine 'where' in residual action space autonomous refinement should explore; task reward determines 'what' residual is ultimately executed. Across three precision-manipulation tasks on a real robot, ARC improves average task success from 33.3% to 75.0%. The human corrections define task-dependent 2-3 dimensional subspaces of the seven-joint residual space that retain 96.0-97.7% of squared correction magnitude. Together, these results show that sparse human corrections can localize and constrain autonomous post-training without requiring the observed correction itself to serve as the final action target.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37547v1
- Authors: Anukriti Singh, Maxime Caniot, Pratap Tokekar, Firas Abi-Farraj
- Published: 2026-10-27T16:58:54Z
- Age days: 1

</details>
