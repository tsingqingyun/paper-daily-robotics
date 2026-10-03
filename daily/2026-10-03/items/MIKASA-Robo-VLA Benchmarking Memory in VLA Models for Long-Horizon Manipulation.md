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
url: "https://arxiv.org/abs/2610.00604"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 45
created: 2026-10-03
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> MIKASA-Robo-VLA 把“动作所需线索先出现、随后消失”做成明确的测试条件，检查 VLA 是否能记住过去。它主要提供评测任务和示范数据，没有在摘要中给出一种新的记忆模型。

## 问题

任务是根据语言完成操作，但决定正确动作的线索可能早已离开画面。许多 VLA 只看当前或最近几帧，常规任务又可能一直保留线索，因此成功率难以说明模型是否使用了记忆。这里真正要解决的是评测可辨别性：让任务必须依赖过去的信息，同时设置仍可看见线索的反应式对照。

### 用一个例子理解

理解用例（非论文实验）：输入指令“把球放进刚才亮过灯的盒子”；机器人先看到左盒亮灯，随后灯熄灭，再拿到球；策略必须保留“左盒”这条信息，输出向左盒放球的动作。若灯一直亮着，就构成反应式对照。

## 创新点或方法

相比原有 32 项任务、仅部分任务使用语言的 MIKASA-Robo，新基准扩为 90 项，全部提供语言指令；其中 80 项隐藏动作所依赖的线索，10 项始终保留线索作为对照。它还用环境阶段的时间安排标记线索确定消失的间隔。训练资源是 22,500 条 oracle 示范轨迹；参考基线在 14 项任务上微调。测试时基线只输入当前图像和本体状态，没有历史观测或显式记忆模块，因此它展示的是这一配置的表现。

### 方法如何工作

1. 先让任务相关线索出现，给策略获得正确决策信息的机会。
2. 随后隐藏线索，使当前观测不足以决定后续动作，从任务条件上要求记忆。
3. 记录线索确定缺席的间隔，用它判断近期帧窗口能否覆盖所需信息。
4. 提供示范并训练参考策略，再与线索始终可见的任务一起测试，以帮助解释成功和失败。

### 必要术语

- 信息空缺：关键线索确定不可见的时间段；本文用它刻画记忆测试条件。
- 反应式对照：仅靠当前可见线索就能决策的任务；本文用它对照记忆任务。
- 本体状态：机器人自己的关节等状态信息；参考基线将其与当前图像一起输入。
- 开环动作块：预测一段动作后，在这段执行中不逐步依据新观测重算；作者指出它会混杂长间隔结果。

## 证据

摘要给出 10 类记忆任务和两种数据格式。70 项任务有明确的信息空缺时长，其中 28 项超过所调查固定上下文 VLA 中最宽的 16 帧窗口。参考 π₀.₅ 在 14 项任务上平均成功率为 0.211 ± 0.044；摘要未说明误差项定义。这个结果不能代表全部 90 项任务，也不能代表带记忆模型。作者明确提醒，Long 划分上更低的成功率还受到开环动作块和该子集中记忆类型的混杂影响。

## 局限

作者明确说明，测量间隔只覆盖线索确定不在场的时间，并非全部记忆需求时长，所以短间隔任务也仍可能依赖记忆。Long 划分的差异不能直接归因于记忆长度。摘要未交代仿真或真机环境，也没有多种记忆模型的比较，需要进一步核查。

- **判断**：值得细读任务构造和信息间隔定义；它最有用的地方是帮助设计能解释失败原因的记忆实验。

## 研究关联

可借鉴的是用任务设计证明“此时必须记忆”，而不只是按任务总时长贴上长程标签。比较记忆机制时，保留可见线索的对照还能帮助区分基础操作困难与信息丢失困难。

### 下一步读哪里

检查隐藏线索是否还有其他可见替代线索、14 项基线任务怎样选择，以及 Long 划分如何控制动作块长度与记忆类型；还要核查成功率误差项和环境设定。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：45
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/MIKASA-Robo-VLA Benchmarking Memory in VLA Models for Long-Horizon Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.00604v1 Announce Type: cross Abstract: Vision-language-action policies often see only one or a few recent frames, which makes it difficult to evaluate how they use information that disappears during a task. We introduce MIKASA-Robo-VLA, a benchmark of 90 language-conditioned manipulation tasks. All but 10 hide the cue an action depends on. Those 10 are reactive controls. MIKASA-Robo, the suite it rebuilds, has 32 tasks and uses language only in a representative VLA subset. Here every task provides an instruction, while memory-dependent tasks hide a task-relevant cue and reactive controls keep it available. For 70 tasks, environment phase timings specify an information gap, and for 28 of them the gap exceeds the 16-frame window of the widest fixed-context VLA we survey. The gap counts only the interval the cue is provably absent, not the full duration a policy must retain it, so every memory-dependent task still requires memory by construction, including the ones whose measured gap is short. We release 22,500 oracle trajectories across 10 memory types in RLDS and LeRobotDataset v3. A reference $\pi_{0.5}$ baseline with current images and proprioception, but no observation history or explicit memory module, is fine-tuned on 14 tasks and achieves 0.211 $\pm$ 0.044 mean task success. Its lower success on the evaluated Long-split tasks is confounded by open-loop chunking and the memory types represented in that subset. Project page: https://mikasarobo.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.00604
- Authors: Egor Cherepanov, Nikita Kachaev, Aleksandr I. Panov, Alexey K. Kovalev
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
