---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.34538v1"
published: "2026-11-25T15:20:36Z"
age_days: 1
score: 35
created: 2026-11-27
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> DTU-Bench 在机器人做到一半时换指令，保留当时的抓握和物体位置，检验策略能不能从那里改做新任务。它也检查机器人是否先完成了旧任务，以及新目标能否保持住。

## 问题

从起点就知道该抓哪个物体，和已经抓住一个物体后收到改口，是两种任务。中途换目的地可能还用得上当前抓握，换对象往往得先解除抓握。固定指令评测很少制造这种冲突，而只看新目标有没有达成，也可能把旧动作碰巧经过的状态算成成功 [S3](https://arxiv.org/html/2611.34538v1#S1.p1.1) [S4](https://arxiv.org/html/2611.34538v1#S1.p2.1) [S5](https://arxiv.org/html/2611.34538v1#S1.p3.1) [S6](https://arxiv.org/html/2611.34538v1#S1.p4.1)[S13](https://arxiv.org/html/2611.34538v1#S3.SS5.p3.1)。

### 用一个例子理解

理解用例（非论文实验）。机器人已经抓起红杯，用户改口说“把蓝杯放进托盘”。从这一刻保存的状态分别继续原指令和新指令，记录先放了哪个杯子、蓝杯曾否进入托盘及结束时是否仍在。若先放红杯再放蓝杯，最终达标的同时也留下了改道延迟的记录。

## 创新点或方法

DTU-Bench 直接测试已发布的 LIBERO 策略，无额外训练。每个任务有原指令起跑、新指令起跑、以及执行中换指令的条件。前两组给出起点能力，第三组保留旧任务造成的物理状态。诊断时从同一个记录状态恢复两条分支，丢掉待执行动作，再分别用旧指令和新指令推理，两条都按新目标检查。作者还测试了先退回预设姿态、或先松手再退回的脚本 [S6](https://arxiv.org/html/2611.34538v1#S1.p4.1)[S17](https://arxiv.org/html/2611.34538v1#S4.SS1.p1.1)[S20](https://arxiv.org/html/2611.34538v1#S4.SS1.p4.1)[S27](https://arxiv.org/html/2611.34538v1#S4.SS2.p6.1) [S28](https://arxiv.org/html/2611.34538v1#S4.SS2.p7.1)。

### 方法如何工作

1. 在相同初始场景分别跑原指令和新指令，得到两项任务各自从头执行的参照。
2. 按原指令运行到指定阶段，保留机器人姿态、抓握及场景，换成新指令继续执行。
3. 逐步检查新目标是否曾达到、是否持续、是否到结束还成立，同时记录旧目标完成时刻。
4. 对选中的切换状态恢复两条等预算分支，只改变指令，检验观察到的行为有多少由更新本身引起。

### 必要术语

- 干预状态：发出新指令时机器人和物体的状态；本文从这里启动可比的续跑。
- 目标判定条件：从仿真状态判断任务要求是否满足的规则；本文用同一个新目标条件给两条分支打分。
- Held-10：新目标连续十次观测成立；本文用它衡量短期保持，并与结束时的 Final 对照。

## 证据

LIBERO 仿真包含 40 个修订情境、七类改动和三个切换阶段。13 个配置在对象类原任务的平均成功率为 95.8%，中途换对象后为 1.6% [S1](https://arxiv.org/html/2611.34538v1#abstract1.1)。这两个数字对应不同目标。同一新目标的对照中，OpenVLA-OFT 在复合目标改动的 Held-10 从头与中途差距为 96.7 个百分点 [S35](https://arxiv.org/html/2611.34538v1#S5.SS2.p1.1)。另有 94 对同状态诊断，37 对无论给哪条指令都曾维持新目标十次观测，三对只在给新指令时做到 [S40](https://arxiv.org/html/2611.34538v1#S5.SS4.p2.1)。换对象的脚本诊断中，松手后撤让 π₀.₅ 从 2% 升到 38%，DM0.5 从 8% 升到 48% [S1](https://arxiv.org/html/2611.34538v1#abstract1.1)[S28](https://arxiv.org/html/2611.34538v1#S4.SS2.p7.1)。

## 局限

作者指出，不同更新类别的场景和任务难度也在变化 [S32](https://arxiv.org/html/2611.34538v1#S5.SS1.p1.1)。同状态实验可以隔离所选仿真状态下更换指令的效果。松手后撤可能带来意外的物体移动 [S1](https://arxiv.org/html/2611.34538v1#abstract1.1)，我会核查抓着易碎物或附近有障碍时，是否还有可行的恢复动作。

- **判断**：值得读到同状态续跑和时间顺序分析 [S27](https://arxiv.org/html/2611.34538v1#S4.SS2.p6.1)[S40](https://arxiv.org/html/2611.34538v1#S5.SS4.p2.1) [S41](https://arxiv.org/html/2611.34538v1#S5.SS4.p3.1)，这两处最能说明常规任务成功率漏掉了什么。

## 研究关联

能恢复同一执行状态时，可以把“只改指令”的分支用作行为对照。把它与旧目标完成顺序和新目标保持时间一起看，才有依据区分及时改道、先做完旧任务再改道，以及偶然经过新目标。

### 下一步读哪里

看 [S14](https://arxiv.org/html/2611.34538v1#S3.SS6.p3.1)[S34](https://arxiv.org/html/2611.34538v1#S5.F3) 区分短暂达标、持续达标与试验分母，再读 [S27](https://arxiv.org/html/2611.34538v1#S4.SS2.p6.1)[S40](https://arxiv.org/html/2611.34538v1#S5.SS4.p2.1) 核对成对续跑怎样实现。结合 [S41](https://arxiv.org/html/2611.34538v1#S5.SS4.p3.1) 检查延长执行预算后，新增成功是及时改道还是延迟完成。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34538v1
- 获取时间：2026-11-27T02:55:44.556575+00:00
- [S1] [Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2611.34538v1#abstract1.1)
- [S2] [Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation · 正文段落 2](https://arxiv.org/html/2611.34538v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.34538v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.34538v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.34538v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.34538v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.34538v1#S1.I1.i1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.34538v1#S1.I1.i2)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.34538v1#S1.I1.i3)
- [S10] [2 Related Work · 正文段落 12](https://arxiv.org/html/2611.34538v1#S2.p2.1)
- [S11] [3.1 Task Update Formulation · 正文段落 15](https://arxiv.org/html/2611.34538v1#S3.SS1.p1.1)
- [S12] [3.2 What Changes: Task Update Taxonomy · 正文段落 22](https://arxiv.org/html/2611.34538v1#S3.SS2.p3.1)
- [S13] [3.5 What Remains: Progress Compatibility and Execution State · 正文段落 31](https://arxiv.org/html/2611.34538v1#S3.SS5.p3.1)
- [S14] [3.6 Evaluation and Diagnostic Analysis · 正文段落 35](https://arxiv.org/html/2611.34538v1#S3.SS6.p3.1)
- [S15] [3.6 Evaluation and Diagnostic Analysis · 正文段落 36](https://arxiv.org/html/2611.34538v1#S3.SS6.p4.1)
- [S16] [3.6 Evaluation and Diagnostic Analysis · 正文段落 37](https://arxiv.org/html/2611.34538v1#S3.SS6.p5.1)
- [S17] [4.1 Experimental Setup · 正文段落 40](https://arxiv.org/html/2611.34538v1#S4.SS1.p1.1)
- [S18] [4.1 Experimental Setup · 正文段落 41](https://arxiv.org/html/2611.34538v1#S4.SS1.p2.1)
- [S19] [4.1 Experimental Setup · 正文段落 42](https://arxiv.org/html/2611.34538v1#S4.SS1.p3.1)
- [S20] [4.1 Experimental Setup · 正文段落 43](https://arxiv.org/html/2611.34538v1#S4.SS1.p4.1)
- [S21] [4.1 Experimental Setup · 正文段落 44](https://arxiv.org/html/2611.34538v1#S4.SS1.p5.1)
- [S22] [4.2 Controlled Diagnostic Experiments · 正文段落 45](https://arxiv.org/html/2611.34538v1#S4.SS2.p1.1)
- [S23] [4.2 Controlled Diagnostic Experiments · 正文段落 46](https://arxiv.org/html/2611.34538v1#S4.SS2.p2.1)
- [S24] [4.2 Controlled Diagnostic Experiments · 正文段落 47](https://arxiv.org/html/2611.34538v1#S4.SS2.p3.1)
- [S25] [4.2 Controlled Diagnostic Experiments · 正文段落 48](https://arxiv.org/html/2611.34538v1#S4.SS2.p4.1)
- [S26] [4.2 Controlled Diagnostic Experiments · 正文段落 49](https://arxiv.org/html/2611.34538v1#S4.SS2.p5.1)
- [S27] [4.2 Controlled Diagnostic Experiments · 正文段落 50](https://arxiv.org/html/2611.34538v1#S4.SS2.p6.1)
- [S28] [4.2 Controlled Diagnostic Experiments · 正文段落 51](https://arxiv.org/html/2611.34538v1#S4.SS2.p7.1)
- [S29] [4.2 Controlled Diagnostic Experiments · 正文段落 52](https://arxiv.org/html/2611.34538v1#S4.T3)
- [S30] [4.2 Controlled Diagnostic Experiments · 正文段落 53](https://arxiv.org/html/2611.34538v1#S4.T3.6)
- [S31] [4.2 Controlled Diagnostic Experiments · 正文段落 54](https://arxiv.org/html/2611.34538v1#S4.F2)
- [S32] [5.1 Responses Differ by Task Update Types · 正文段落 56](https://arxiv.org/html/2611.34538v1#S5.SS1.p1.1)
- [S33] [5.1 Responses Differ by Task Update Types · 正文段落 57](https://arxiv.org/html/2611.34538v1#S5.SS1.p2.1)
- [S34] [5.1 Responses Differ by Task Update Types · 正文段落 58](https://arxiv.org/html/2611.34538v1#S5.F3)
- [S35] [5.2 Task Competence \neq Runtime Success · 正文段落 59](https://arxiv.org/html/2611.34538v1#S5.SS2.p1.1)
- [S36] [5.2 Task Competence \neq Runtime Success · 正文段落 60](https://arxiv.org/html/2611.34538v1#S5.SS2.p2.1)
- [S37] [5.3 Intervention Stage Affects Runtime Success · 正文段落 61](https://arxiv.org/html/2611.34538v1#S5.SS3.p1.1)
- [S38] [5.3 Intervention Stage Affects Runtime Success · 正文段落 62](https://arxiv.org/html/2611.34538v1#S5.SS3.p2.1)
- [S39] [5.4 Reaching the New Goal \neq Adaptation Success · 正文段落 63](https://arxiv.org/html/2611.34538v1#S5.SS4.p1.1)
- [S40] [5.4 Reaching the New Goal \neq Adaptation Success · 正文段落 64](https://arxiv.org/html/2611.34538v1#S5.SS4.p2.1)
- [S41] [5.4 Reaching the New Goal \neq Adaptation Success · 正文段落 65](https://arxiv.org/html/2611.34538v1#S5.SS4.p3.1)
- [S42] [5.4 Reaching the New Goal \neq Adaptation Success · 正文段落 68](https://arxiv.org/html/2611.34538v1#S5.SS4.p6.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/Dynamic Task Update Benchmark (DTU-Bench) Evaluating Runtime Task Adaptation in.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies perform well on fixed-instruction robotic manipulation benchmarks, but their ability to adapt to instruction changes during execution remains understudied. We introduce the Dynamic Task Update Benchmark (DTU-Bench), evaluating 40 task revisions across seven update types and three execution stages using LIBERO, a simulated robotic manipulation benchmark. We compare performance when a new instruction is given before execution starts versus during execution, and examine whether the new task instructions are followed. Across 13 representative VLA configurations, average task success is 95.8% on the original object-manipulation tasks, compared with only 1.6% when the instruction changes which object to manipulate during execution. Controlled diagnostics show that policies often complete the original task before the updated one, and that their responses depend on the robot's physical state. We further test whether a simple scripted controller that releases the grasped object and moves the arm back helps robots respond to instruction changes. This improves success from 2% to 38% for π0.5 and from 8% to 48% for DM0.5, but can cause unwanted object motion. These findings reveal limitations that fixed-instruction benchmarks and task-success metrics alone can overlook in evaluating robotic manipulation. Project page: https://dtu-bench.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34538v1
- Authors: Yanran Jiang, Cécile Paris, Dana Kulić, Leimin Tian
- Published: 2026-11-25T15:20:36Z
- Age days: 1

</details>
