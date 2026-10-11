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
url: "https://arxiv.org/abs/2610.12424v1"
published: "2026-10-08T17:55:12Z"
age_days: 2
score: 30
created: 2026-10-11
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RoboRSI 用 Top-Down Skill Refinement（TSR）把机器人程序分成责任明确的技能，失败后找到源头，只修改相关分支。修复先经过检查和历史用例验证，再供后续任务复用。

## 问题

任务是让执行代码的机器人在反复做家务时积累能力。困难在于失败经常晚于原因出现：放置失败可能来自先前定位错误，直接给放置步骤加重试会修错地方；共享技能改动还可能破坏其他任务。长日志和临时提示也容易让修复只适应最新场景。[S9](https://arxiv.org/html/2610.12424v1#S2.SS0.SSS0.Px2.p1.1) [S11](https://arxiv.org/html/2610.12424v1#S3.p1.1)

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子收进柜子”；执行记录显示夹爪虽张开但杯子未进入柜内，诊断追溯到使用旧目标位置。系统修改定位相关技能，验证受影响的放置任务后发布，后续任务调用修好的版本。

## 创新点或方法

从直接反复修整段程序，改为维护有输入、输出、责任和执行记录的技能层级。Manager、Planner、Engineer、Reviewer 分工协调规划、执行、诊断与修订，沿调用路径寻找最早失败节点，把补丁限定在相关范围；接口改变则扩展到调用者。[S12](https://arxiv.org/html/2610.12424v1#S3.SS1.p1.1) [S13](https://arxiv.org/html/2610.12424v1#S3.SS1.SSS0.Px1.p1.1) [S14](https://arxiv.org/html/2610.12424v1#S3.SS2.SSS0.Px1.p1.1) [S15](https://arxiv.org/html/2610.12424v1#S3.SS2.SSS0.Px2.p1.3) 修订在隔离副本中接受测试和受影响任务检查，通过后发布。稳定序列可压成复合技能，但参数从当前感知重新计算。主要学习过程是在线修改技能代码，并非每轮更新控制网络；训练 ACT 是另一个附加实验。[S27](https://arxiv.org/html/2610.12424v1#S4.SS5.SSS5.p1.1) [S33](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px6.p1.1)

### 方法如何工作

1. 把任务拆成带可观察结果的技能，得到能追踪责任的调用结构。
2. 执行并用新观察核验后置条件，形成有位置、有版本的失败证据。
3. 沿调用路径定位源头，限制补丁范围，避免在多个调用者重复修补。
4. 测试修改并检查受影响历史用例，通过后发布，使下一轮使用已验证版本。
5. 把反复成功的共同序列合成参数化技能，运行时重算场景参数，减少重复规划。

### 必要术语

- TSR：按任务层级定位和限制修订范围；连接失败诊断与局部修改。
- 后置条件：技能结束后必须成立的可观察事实；用于判定真实完成。
- 复合技能：把稳定技能序列封装成一次调用；保留运行时感知和参数计算。

## 证据

仿真对比 CaP-X、Maestro、OpenETA，匹配骨干、工具和每回合交互预算。RoboRSI 在 LIBERO、LIBERO-PRO、RoboTwin 随评估在线改进，对方技能固定。[S17](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px1.p1.1) [S18](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px2.p1.1) [S19](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px5.p1.1) [S20](https://arxiv.org/html/2610.12424v1#S4.SS3.SSS0.Px1.p1.1) 成功率分别为 56.0%、49.5%、24.0%，OpenETA 为 50.7%、38.5%、21.3%；冻结库的 LIBERO-Plus 为 42.1%，对方 36.4%。RoboTwin 回合数为 154 对 150。[S22](https://arxiv.org/html/2610.12424v1#S4.T1.9) 真机经历 104 轮家务开发并跨场景变化，但所给节选没有完整真机成功率曲线。[S7](https://arxiv.org/html/2610.12424v1#S1.p6.1)

## 局限

作者把仿真经验迁移到实体机器人、跨平台共享技能列为后续工作。[S29](https://arxiv.org/html/2610.12424v1#S5.p1.1) 真机有人工指导和安全监督；历史检查采用最近合格记录的离线回放，不等于完整物理重演。[S32](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px5.p1.1) [S33](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px6.p1.1) 主结果衡量带在线积累的系统收益，不能单独证明 TSR 或角色分工贡献，仍需查消融和总开发成本。

- **判断**：值得读到技能接口、发布条件和失败归因实例，才能判断这套自动修复是否适用于自己的工具边界。

## 研究关联

可以借鉴软件维护中的责任边界：先规定技能承诺什么、怎样验证承诺，再谈自动改进。这样失败记录才有明确归属，修复才可能成为跨任务能力，而不是越来越长的临时补丁。

### 下一步读哪里

重点读 [S33](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px6.p1.1) 的后置条件、验证种子和复合技能生成规则；核查如何识别最早失败节点、角色与 TSR 消融，以及 [S31](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px4.p1.1) 是否把诊断、审查和验证成本计入总账。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.12424v1
- 获取时间：2026-10-11T00:33:20.030045+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.12424v1#p1.1)
- [S2] [RoboRSI: Stable, Efficient, and Reusable Robot Self-Evolution in Complex Real-World Environments · 正文段落 2](https://arxiv.org/html/2610.12424v1#abstract1.1)
- [S3] [RoboRSI: Stable, Efficient, and Reusable Robot Self-Evolution in Complex Real-World Environments · 正文段落 3](https://arxiv.org/html/2610.12424v1#p2.fig1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.12424v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.12424v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.12424v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.12424v1#S1.p6.1)
- [S8] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.12424v1#S1.I1.i3)
- [S9] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.12424v1#S2.SS0.SSS0.Px2.p1.1)
- [S10] [2 Related Work · 正文段落 16](https://arxiv.org/html/2610.12424v1#S2.SS0.SSS0.Px3.p1.1)
- [S11] [3 Method · 正文段落 17](https://arxiv.org/html/2610.12424v1#S3.p1.1)
- [S12] [3.1 Overall Framework · 正文段落 18](https://arxiv.org/html/2610.12424v1#S3.SS1.p1.1)
- [S13] [3.1 Overall Framework · 正文段落 19](https://arxiv.org/html/2610.12424v1#S3.SS1.SSS0.Px1.p1.1)
- [S14] [3.2 Top-Down Skill Refinement · 正文段落 25](https://arxiv.org/html/2610.12424v1#S3.SS2.SSS0.Px1.p1.1)
- [S15] [3.2 Top-Down Skill Refinement · 正文段落 30](https://arxiv.org/html/2610.12424v1#S3.SS2.SSS0.Px2.p1.3)
- [S16] [4 Experiment · 正文段落 33](https://arxiv.org/html/2610.12424v1#S4.p1.1)
- [S17] [4.2 Evaluation Design · 正文段落 40](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px1.p1.1)
- [S18] [4.2 Evaluation Design · 正文段落 41](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px2.p1.1)
- [S19] [4.2 Evaluation Design · 正文段落 44](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px5.p1.1)
- [S20] [4.3 Main Simulation Results · 正文段落 46](https://arxiv.org/html/2610.12424v1#S4.SS3.SSS0.Px1.p1.1)
- [S21] [4.3 Main Simulation Results · 正文段落 47](https://arxiv.org/html/2610.12424v1#S4.T1)
- [S22] [4.3 Main Simulation Results · 正文段落 48](https://arxiv.org/html/2610.12424v1#S4.T1.9)
- [S23] [4.3 Main Simulation Results · 正文段落 49](https://arxiv.org/html/2610.12424v1#S4.SS3.SSS0.Px2.p1.1)
- [S24] [4.3 Main Simulation Results · 正文段落 50](https://arxiv.org/html/2610.12424v1#S4.SS3.SSS0.Px3.p1.1)
- [S25] [4.3 Main Simulation Results · 正文段落 51](https://arxiv.org/html/2610.12424v1#S4.T2)
- [S26] [4.3.1 LIBERO Results by Suite · 正文段落 56](https://arxiv.org/html/2610.12424v1#S4.SS3.SSS1.p1.1)
- [S27] [4.5.5 Learning Policies from Execution Data · 正文段落 84](https://arxiv.org/html/2610.12424v1#S4.SS5.SSS5.p1.1)
- [S28] [4.5.5 Learning Policies from Execution Data · 正文段落 85](https://arxiv.org/html/2610.12424v1#S4.F11)
- [S29] [5 Conclusions and Future Work · 正文段落 86](https://arxiv.org/html/2610.12424v1#S5.p1.1)
- [S30] [Appendix A TSR Formulation and Analysis · 正文段落 89](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px2.p1.1)
- [S31] [Appendix A TSR Formulation and Analysis · 正文段落 94](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px4.p1.1)
- [S32] [Appendix A TSR Formulation and Analysis · 正文段落 95](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px5.p1.1)
- [S33] [Appendix A TSR Formulation and Analysis · 正文段落 96](https://arxiv.org/html/2610.12424v1#A1.SS0.SSS0.Px6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/RoboRSI Stable, efficient, and reusable robot self-evolution in complex real-wor.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A generalist robot should not only perform diverse tasks but also improve through experience, turning what it learns during execution into capabilities that later tasks can reuse. Robot agents that act through code can already repair programs from execution feedback, yet it remains a central challenge to organize this experience around the task structure that gives it meaning, so that each repair is attributed to the responsible capability, supported by execution evidence, and validated before it is reused. We introduce RoboRSI, a robot self-improvement system built on Top-Down Skill Refinement (TSR). TSR decomposes tasks into compound, atomic, and base skills with scoped responsibilities and explicit input--output contracts, attributes each execution outcome to the responsible branch, and confines revision to that branch. Building upon this structure, a Manager, Planner, Engineer, and Reviewer coordinate planning, execution, diagnosis, and the validated release of new skills, while people steer the process through objectives and corrections; stable skill sequences are further consolidated into reusable compound skills. On a mobile manipulator, RoboRSI develops multi-object household cleanup over 104 rounds. In simulation, it achieves the highest success rate on LIBERO, LIBERO-PRO, LIBERO-Plus, and RoboTwin, exceeding the strongest baseline by 2.7 to 11.0 percentage points.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12424v1
- Authors: Zimo Wen, Yijin Chen, Yuxuan Cao, Wendi Chen, Yanwen Zou, Wenye Yu, Fuhang Kuang, Han Xue, Jun Lv, Chuan Wen, Cewu Lu
- Published: 2026-10-08T17:55:12Z
- Age days: 2

</details>
