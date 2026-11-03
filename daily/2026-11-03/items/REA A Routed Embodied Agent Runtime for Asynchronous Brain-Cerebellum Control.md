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
url: "https://arxiv.org/abs/2610.42053v1"
published: "2026-10-30T17:18:13Z"
age_days: 3
score: 37
created: 2026-11-03
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> REA 解决的是慢模型与快控制器怎样配合：先根据开发回合选好策略，让它按自己的速度执行，在交接处再决定是否换策略。它用历史成功记录、完成判断和共同恢复预算，减少等待、漏检失败及无休止重试。

## 问题

让大模型每次决定下一步，会拖慢控制；只在程序报错时求助，又会漏掉“程序正常结束但任务没完成”的失败，持续错误还可能反复触发求助。不同方法使用不同环境和判分接口，也让优劣难以归因。[S5](https://arxiv.org/html/2610.42053v1#S1.p2.1) REA 因而同时处理执行协调和对齐比较。

### 用一个例子理解

理解用例（非论文实验）：输入“把物体放进盒子”；路由记录选择以往更可靠的控制器，控制器独立运行；返回后图像显示物体仍在盒外，判断器触发备用代码策略从当前状态接手，最终输出完成状态或预算耗尽。

## 创新点或方法

旧做法在线反复询问大模型，REA 则提前记录每个策略在各任务上的成功率和成本，在线直接选路。System 0 执行程序、VLA 或全身控制器；System 1 负责调度；System 2 生成策略或判断完成。策略返回时，视觉判断可决定停止还是从当前状态升级恢复，所有尝试共用步数和时间预算。这里主要是开发期测量和运行时组织，并非训练一个新的端到端控制模型。[S6](https://arxiv.org/html/2610.42053v1#S1.p3.1) [S7](https://arxiv.org/html/2610.42053v1#S1.p4.1)

### 方法如何工作

1. 在开发回合测量候选策略的任务成功率和成本，得到可直接查询的路由记录。
2. 收到任务后按记录选择策略，避开在线大模型选路的延迟。
3. 让策略在自身闭环中运行，到返回或分段边界才交还控制，保留快控制的节奏。
4. 按所用门控判断是否升级；若需要恢复，则从当前状态换策略，并扣除同一份剩余预算。

### 必要术语

- 路由记忆：保存策略过去在任务上的实测表现；本文用它决定先运行谁。
- 静默失败：没有程序异常，任务却没完成；本文用返回后的视觉判断发现它。
- 升级阶梯：按顺序尝试后续策略；本文用共享预算限制恢复成本。

## 证据

LIBERO-Pro 的60任务、3,000测试回合中，REA-M 为95.9%，最佳单方法为94.7%，每次成功步数从1,343降至1,003。[S26](https://arxiv.org/html/2610.42053v1#S4.T1.11) [S27](https://arxiv.org/html/2610.42053v1#S4.SS2.p1.1) 但该主结果使用异常门，不包含视觉判断；仅路由记忆已至少达到95.7%。视觉判断在另一个 ASPIRE 对照中增加3.1个百分点，却需2.1倍的每次成功耗时。[S29](https://arxiv.org/html/2610.42053v1#S4.SS4.p1.1) 独立100回合 RoboTwin 研究中，VLA和VLA+代码分别为84%、86%，单 VLA 为80%。[S8](https://arxiv.org/html/2610.42053v1#S1.SS0.SSS0.Px1.p1.1)

## 局限

作者明确指出，BEHAVIOR 的27/50对25/50并不显著；另一项 RoboTwin 研究同一配置跨夜相差36个场景，因此应优先看同步对照。[S31](https://arxiv.org/html/2610.42053v1#S4.SS7.p1.1) [S32](https://arxiv.org/html/2610.42053v1#S4.SS7.p2.1) 真机 G1 的8/10只是小样本演示。[S33](https://arxiv.org/html/2610.42053v1#S4.SS8.p1.1) 我的核查重点是路由对新任务的适用范围：逐任务开发记录不能自动证明能处理未见任务。

- **判断**：值得细读路由消融和对齐协议；主结果支持减少不必要在线推理，但不能把所有收益归给异步视觉判断。

## 研究关联

如果已有几种能力互补的控制器，可以先测清“什么任务交给谁”，再考虑增加在线推理。REA 的主结果表明，在这个策略库里，事先选择可靠且较短的程序，已经解释了大部分收益。

### 下一步读哪里

先对照[S25](https://arxiv.org/html/2610.42053v1#S4.T1) [S26](https://arxiv.org/html/2610.42053v1#S4.T1.11) [S27](https://arxiv.org/html/2610.42053v1#S4.SS2.p1.1) [S28](https://arxiv.org/html/2610.42053v1#S4.F5) [S29](https://arxiv.org/html/2610.42053v1#S4.SS4.p1.1)分清 REA-M、REA-A、REA-V，检查同一程序库上的比较。再核查分段执行时判断结果何时生效、恢复策略能否接受中途状态，以及等待时间和离线生成成本如何计入。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：37
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.42053v1
- 获取时间：2026-11-03T00:10:22.272245+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.42053v1#p1.2)
- [S2] [正文 · 正文段落 2](https://arxiv.org/html/2610.42053v1#S0.F1)
- [S3] [REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control · 正文段落 3](https://arxiv.org/html/2610.42053v1#abstract1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.42053v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.42053v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.42053v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.42053v1#S1.p4.1)
- [S8] [Results. · 正文段落 9](https://arxiv.org/html/2610.42053v1#S1.SS0.SSS0.Px1.p1.1)
- [S9] [Contributions. · 正文段落 11](https://arxiv.org/html/2610.42053v1#S1.F3)
- [S10] [Embodied brains and fast policies. · 正文段落 12](https://arxiv.org/html/2610.42053v1#S2.SS0.SSS0.Px1.p1.1)
- [S11] [Dual-system control. · 正文段落 13](https://arxiv.org/html/2610.42053v1#S2.SS0.SSS0.Px2.p1.1)
- [S12] [Routing, evaluation and completion judging. · 正文段落 14](https://arxiv.org/html/2610.42053v1#S2.SS0.SSS0.Px3.p1.1)
- [S13] [3 The REA Runtime · 正文段落 15](https://arxiv.org/html/2610.42053v1#S3.p1.1)
- [S14] [REA variants. · 正文段落 16](https://arxiv.org/html/2610.42053v1#S3.SS0.SSS0.Px1.p1.1)
- [S15] [REA variants. · 正文段落 18](https://arxiv.org/html/2610.42053v1#S3.I1.i2)
- [S16] [REA variants. · 正文段落 19](https://arxiv.org/html/2610.42053v1#S3.I1.i3)
- [S17] [System 0: policy execution. · 正文段落 21](https://arxiv.org/html/2610.42053v1#S3.SS1.SSS0.Px1.p1.1)
- [S18] [System 2: the brain, offline and online. · 正文段落 22](https://arxiv.org/html/2610.42053v1#S3.SS1.SSS0.Px2.p1.1)
- [S19] [Backends · 正文段落 23](https://arxiv.org/html/2610.42053v1#S3.SS1.SSS0.Px3.p1.1)
- [S20] [Boundary-triggered judge gate: consult the brain when a policy returns. · 正文段落 27](https://arxiv.org/html/2610.42053v1#S3.SS2.SSS0.Px2.p1.1)
- [S21] [Baselines. · 正文段落 29](https://arxiv.org/html/2610.42053v1#S3.SS2.SSS0.Px4.p1.1)
- [S22] [3.3 Aligned Evaluation Protocol · 正文段落 31](https://arxiv.org/html/2610.42053v1#S3.SS3.p1.1)
- [S23] [4 Experiments · 正文段落 32](https://arxiv.org/html/2610.42053v1#S4.p1.1)
- [S24] [System 2 policy-generation methods. · 正文段落 34](https://arxiv.org/html/2610.42053v1#S4.SS1.SSS0.Px2.p1.1)
- [S25] [4.2 Routing Beats Each Policy-Generation Baseline · 正文段落 36](https://arxiv.org/html/2610.42053v1#S4.T1)
- [S26] [4.2 Routing Beats Each Policy-Generation Baseline · 正文段落 37](https://arxiv.org/html/2610.42053v1#S4.T1.11)
- [S27] [4.2 Routing Beats Each Policy-Generation Baseline · 正文段落 38](https://arxiv.org/html/2610.42053v1#S4.SS2.p1.1)
- [S28] [4.2 Routing Beats Each Policy-Generation Baseline · 正文段落 39](https://arxiv.org/html/2610.42053v1#S4.F5)
- [S29] [4.4 REA Improves Policies from Different Methods · 正文段落 42](https://arxiv.org/html/2610.42053v1#S4.SS4.p1.1)
- [S30] [4.7 Extensional Experiments on BEHAVIOR and RoboTwin-2 · 正文段落 50](https://arxiv.org/html/2610.42053v1#S4.F7)
- [S31] [4.7 Extensional Experiments on BEHAVIOR and RoboTwin-2 · 正文段落 51](https://arxiv.org/html/2610.42053v1#S4.SS7.p1.1)
- [S32] [4.7 Extensional Experiments on BEHAVIOR and RoboTwin-2 · 正文段落 52](https://arxiv.org/html/2610.42053v1#S4.SS7.p2.1)
- [S33] [4.8 Real Robot Experiments on Unitree-G1 · 正文段落 53](https://arxiv.org/html/2610.42053v1#S4.SS8.p1.1)
- [S34] [4.9 Real-World Block Placement on AlohaMini2 · 正文段落 54](https://arxiv.org/html/2610.42053v1#S4.SS9.p1.1)
- [S35] [4.9 Real-World Block Placement on AlohaMini2 · 正文段落 55](https://arxiv.org/html/2610.42053v1#S4.F8)
- [S36] [Use the brain ahead of time or at policy returns, never inside a running policy. · 正文段落 57](https://arxiv.org/html/2610.42053v1#S5.SS0.SSS0.Px1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/REA A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers. Conversely, fast policies like VLAs and whole-body controllers offer more efficient reflexes, but struggle to generalize. While pairing a deliberative brain (foundation models) with a reactive cerebellum (fast policies) seems natural for embodied systems, two obstacles remain: methods are built and scored on incompatible stacks, and their asynchronous coordination is difficult. For example, an agent that calls the VLA in the agentic loop can stall the fast execution, while a VLA that calls the agent on errors tends to re-trigger fallbacks repeatedly or completely miss silent failures. To address this, we propose REA (Routed Embodied Agent), a unified runtime where a deliberative System 2, an embodied router System 1 and reactive System 0 policies cooperate under a single golden rule - no running policy waits on the brain. Instead of querying the brain at each failure, REA employs a route memory that stores each policy's measured success ahead of time, a boundary-triggered judge gate that consults the brain on policy execution, and a shared-budget escalation ladder for bounded recovery. Evaluated on 3,000 test episodes across 60 LIBERO-Pro tasks, REA reaches 95.9% success and beats the best single-agent baseline in its own policy pool (94.7%) while reducing control steps by 25% and control time by 17%. In a separate 100-episode RoboTwin 2.0 study, REA achieves 84% success with VLA policies and 86% with VLA+code, compared with 80% for the strongest single VLA baseline MEDex. These results demonstrate learned and programmatic policies operating within the same runtime. REA also transfers to BEHAVIOR-1K and a real Unitree G1 humanoid, achieving the highest observed success among the compared methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.42053v1
- Authors: Pengfei Zhou, Yixing Ma, Zhengfeiyang Zhang, Haoyuan Chen, Zhenglin Wan, Hexin Wang, Wangbo Zhao, Yang You
- Published: 2026-10-30T17:18:13Z
- Age days: 3

</details>
