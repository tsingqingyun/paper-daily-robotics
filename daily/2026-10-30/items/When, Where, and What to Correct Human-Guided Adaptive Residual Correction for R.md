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
url: "https://arxiv.org/abs/2610.37547"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 29
created: 2026-10-30
concepts: ["机器人学习", "具身智能评测与基准"]
---

# When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> Adaptive Residual Correction（ARC）让已经基本会做任务的机器人，只在容易失败的位置加上小幅动作修正。人类纠正负责提示何时介入、往哪些方向探索，最终修正动作由强化学习按任务奖励学出来。

## 问题

具体任务是精密操控：模仿策略能完成大部分轨迹，却在少数需要最后一点精度的位置失败。更新整个策略，或在所有状态探索修正动作，都把局部问题扩大成了全局学习问题，浪费探索，也可能干扰原本可靠的动作。

### 用一个例子理解

理解用例（非论文实验）：输入机械臂对准插孔时的观测和原策略动作；系统识别到接近插入的易错状态，只在学到的少数关节组合方向上施加修正；输出调整后的动作，目标是完成插入。

## 创新点或方法

ARC 冻结原策略，在其动作上叠加可学习的残差。训练时，人类介入前的状态帮助确定残差何时启用；纠正动作的几何结构限定探索方向；强化学习再依据任务奖励选择有效修正。因此人类动作不是必须照抄的标准答案。执行时保留原策略与残差模块，但门控和动作组合的具体形式、是否仍需人工介入，摘要未说明。

### 方法如何工作

1. 保留已会完成大部分轨迹的基础策略，并收集少量人类纠正，得到局部失败附近的信息。
2. 利用介入前状态学习何时启用残差，让探索集中到需要修正的阶段。
3. 利用纠正几何限定残差探索方向，减少需要搜索的动作维度。
4. 在限定区域内按任务奖励训练残差，得到以完成任务为目标的修正，而非固定复现人工动作。

### 必要术语

- 残差动作：加在原动作上的调整量；本文用它修补冻结策略。
- 动作子空间：只允许沿某些方向组合动作的范围；本文用来收窄探索。
- 强化学习：根据任务奖励改进动作选择；本文由它决定最终修正。

## 证据

摘要报告三项真机精密操控任务，平均成功率从 33.3% 升到 75.0%。在人类纠正形成的七关节残差空间中，任务相关的二维或三维子空间保留了 96.0%–97.7% 的纠正幅度平方。这说明纠正方向具有较强集中性，也提供了方法有效的真机证据；但摘要未给任务名称、试验次数、误差范围及其他残差方法的成绩，无法判断统计稳定性或相对优势。

## 局限

摘要没有列出作者明确局限。我会核查低维空间是否遗漏少见但关键的纠正方向，以及门控漏掉危险状态时如何处理。保留大部分纠正幅度平方，不等于保留同等比例的任务成功能力；成功率提升也不能在没有消融时归因于某一个设计。

- **判断**：值得细读方法和消融，尤其是“何时启用”与“向哪里探索”如何分别改善学习效率；它给出了清楚的机制和真机结果。

## 研究关联

这里可借鉴的是改变人类反馈的用途：一次纠正除了提供动作示范，还能告诉学习器把试错集中在哪里。当基础策略已可靠、失败又集中在少数阶段时，这种信息可能比要求策略完整复现人类动作更合适。

### 下一步读哪里

优先核查门控的监督信号、纠正子空间的构造方法、奖励定义和人工纠正数量；再看完整空间探索、直接模仿纠正、仅使用门控等对照，以及各项真机任务的独立成绩。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/When, Where, and What to Correct Human-Guided Adaptive Residual Correction for R.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.37547v1 Announce Type: cross Abstract: Imitation policies that reliably execute most of a manipulation trajectory can still fail in localized regions requiring last-mile precision. Updating the full policy or exploring residual actions everywhere treats this local failure as a global learning problem. We introduce Adaptive Residual Correction (ARC), a lightweight post-training module that uses reinforcement learning (RL) to learn a residual correction on top of a frozen policy while using sparse human corrections to structure autonomous exploration. Rather than treating human corrections as imitation targets, ARC uses pre-intervention states to determine 'when' residual control should become active and correction geometry to determine 'where' in residual action space autonomous refinement should explore; task reward determines 'what' residual is ultimately executed. Across three precision-manipulation tasks on a real robot, ARC improves average task success from 33.3% to 75.0%. The human corrections define task-dependent 2-3 dimensional subspaces of the seven-joint residual space that retain 96.0-97.7% of squared correction magnitude. Together, these results show that sparse human corrections can localize and constrain autonomous post-training without requiring the observed correction itself to serve as the final action target.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37547
- Authors: Anukriti Singh, Maxime Caniot, Pratap Tokekar, Firas Abi-Farraj
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
