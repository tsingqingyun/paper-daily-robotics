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
url: "https://arxiv.org/abs/2610.12957v1"
published: "2026-10-09T03:54:58Z"
age_days: 3
score: 40
created: 2026-10-13
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> JoyInside-VLM-Agent训练一个能按产品能力办事、遇到目标变化或执行失败就修改决定的多模态智能体。其DPER用两种训练期额外信息判断每个生成token该受到多强的奖励更新，但不改变奖励原本鼓励或抑制它的方向。

## 问题

同一请求在不同产品上可执行的动作不同，交互途中用户还可能改目标、设备可能报错。仅有顺利完成的示范不够；整条轨迹的奖励又难以判断哪些生成片段该负主要责任[S5](https://arxiv.org/html/2610.12957v1#S1.p2.1) [S6](https://arxiv.org/html/2610.12957v1#S1.p3.1)。任务是训练持续遵守能力约束、追踪当前目标并利用反馈的决策策略。

### 用一个例子理解

理解用例（非论文实验）：输入“去找红球”、当前图像和设备能力；智能体调用搜索与移动工具，收到通路阻塞后更新任务状态，改走另一条可用路线；若仍找不到，则输出明确失败报告。

## 创新点或方法

先把产品角色、工具与约束放进有状态沙箱，生成包含改目标和失败恢复的轨迹，并核查执行结果与视觉反馈。之后依次做示范学习、教师在学生实际生成上下文上的蒸馏、DPER强化学习。DPER由冻结教师和共享策略参数的特权学生提供token证据，按分歧和支持程度选择来源，缩放奖励优势而保留正负号[S7](https://arxiv.org/html/2610.12957v1#S1.p4.1) [S8](https://arxiv.org/html/2610.12957v1#S1.p5.1)。部署只用一个学生、产品配置和交互上下文，不提供特权参考[S20](https://arxiv.org/html/2610.12957v1#S4.p1.1)。

### 方法如何工作

1. 把产品规格和场景加载进沙箱，明确可用动作与限制，生成可执行的交互上下文[S18](https://arxiv.org/html/2610.12957v1#S3.SS2.p1.1)。
2. 执行动作并返回结果、错误与新图像，核查记录一致性，积累可用于学习恢复行为的轨迹[S19](https://arxiv.org/html/2610.12957v1#S3.SS2.p2.1)。
3. 先模仿有效轨迹，再让教师指导学生自己生成的上下文，减少只会跟随固定示范的问题[S21](https://arxiv.org/html/2610.12957v1#S4.F3) [S22](https://arxiv.org/html/2610.12957v1#S4.SS2.p1.1) [S23](https://arxiv.org/html/2610.12957v1#S4.SS2.p2.1) [S24](https://arxiv.org/html/2610.12957v1#S4.E1) [S25](https://arxiv.org/html/2610.12957v1#S4.SS2.p2.2) [S26](https://arxiv.org/html/2610.12957v1#S4.SS2.p3.1)。
4. 用过程、评审排名和任务队列生成轨迹奖励，再由DPER证据调节token更新强度；精确路由公式未在节选中提供[S8](https://arxiv.org/html/2610.12957v1#S1.p5.1) [S27](https://arxiv.org/html/2610.12957v1#S4.SS3.SSS3.p1.1)。
5. 部署单一学生，根据当前观测与执行反馈持续决定回应、工具调用或终止[S18](https://arxiv.org/html/2610.12957v1#S3.SS2.p1.1) [S20](https://arxiv.org/html/2610.12957v1#S4.p1.1)。

### 必要术语

- ReAct：交替分析当前情况与采取动作；这里组织多轮交互决策。
- 在策略蒸馏：教师指导学生实际生成的上下文；让训练贴近学生会遇到的状态。
- 特权信息：训练时额外可见、部署时不可见的信息；用于提供更有依据的token评分。
- 优势：某次生成比同任务其他生成好或差的奖励信号；DPER改变其强度而保留符号。

## 证据

相对基础Qwen3.5-35B-A3B和更大Qwen3.5-397B-A17B，BFCL v4为77.44，对照67.30与72.90；ToolBench为23.50，对照18.30与21.00。但MSAgent和ToolACE低于大模型[S39](https://arxiv.org/html/2610.12957v1#S5.T1.5)。BFCL按官方评分，其他三个公共集按完整工具调用序列精确匹配[S35](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px6.p1.1)。私有集领先评估基线，但包含固定参数下的技能指令优化[S32](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px3.p1.1)。两次四足真机案例是定性展示，不能当长期完成率证据[S29](https://arxiv.org/html/2610.12957v1#S5.p1.1)。

## 局限

作者明确指出能力库覆盖、沙箱反馈真实性与更广产品泛化仍是限制[S40](https://arxiv.org/html/2610.12957v1#S7.p1.1)。我的待核查问题是DPER的精确路由条件、独立消融和私有集规模；给定节选不足以把系统收益单独归因于DPER。工具名正确、参数匹配或回答重叠，也不等同于真实机器人完成任务。

- **判断**：值得读数据闭环与DPER细节，但应把它视为交互策略训练方案；真机可靠性的证据目前主要是案例。

## 研究关联

具体启示是把“知道产品不能做什么”和“失败后如何继续”放进训练轨迹，而不仅写在部署提示中。DPER还提供一个信用分配思路：额外证据调整更新强度，任务奖励继续决定更新方向。

### 下一步读哪里

先读[S18](https://arxiv.org/html/2610.12957v1#S3.SS2.p1.1) [S19](https://arxiv.org/html/2610.12957v1#S3.SS2.p2.1)确认动作如何改变状态和生成反馈，再核查DPER路由与特权信息的具体内容。查看各阶段消融，并检查私有结果中训练策略和技能优化各自贡献；[S36](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px7.p1.1)提醒Plan.EM只衡量步骤决策类型。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.12957v1
- 获取时间：2026-10-13T00:21:45.076593+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.12957v1#p1.2)
- [S2] [JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents · 正文段落 2](https://arxiv.org/html/2610.12957v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.12957v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.12957v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.12957v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.12957v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.12957v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.12957v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.12957v1#S1.p6.1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.12957v1#S1.I1.i2)
- [S11] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.12957v1#S1.I1.i3)
- [S12] [1 Introduction · 正文段落 14](https://arxiv.org/html/2610.12957v1#S1.I1.i4)
- [S13] [2.1 Embodied and Context-Aware Interaction · 正文段落 16](https://arxiv.org/html/2610.12957v1#S2.SS1.p2.1)
- [S14] [2.2 Multimodal Trajectory Construction · 正文段落 17](https://arxiv.org/html/2610.12957v1#S2.SS2.p1.1)
- [S15] [2.2 Multimodal Trajectory Construction · 正文段落 18](https://arxiv.org/html/2610.12957v1#S2.SS2.p2.1)
- [S16] [2.3 Post-Training and Reward-Guided Optimization · 正文段落 19](https://arxiv.org/html/2610.12957v1#S2.SS3.p1.1)
- [S17] [2.3 Post-Training and Reward-Guided Optimization · 正文段落 20](https://arxiv.org/html/2610.12957v1#S2.SS3.p2.1)
- [S18] [3.2 Closed-Loop Trajectory Generation · 正文段落 28](https://arxiv.org/html/2610.12957v1#S3.SS2.p1.1)
- [S19] [3.2 Closed-Loop Trajectory Generation · 正文段落 29](https://arxiv.org/html/2610.12957v1#S3.SS2.p2.1)
- [S20] [4 Method · 正文段落 34](https://arxiv.org/html/2610.12957v1#S4.p1.1)
- [S21] [4 Method · 正文段落 35](https://arxiv.org/html/2610.12957v1#S4.F3)
- [S22] [4.2 Multi-Teacher On-Policy Distillation · 正文段落 40](https://arxiv.org/html/2610.12957v1#S4.SS2.p1.1)
- [S23] [4.2 Multi-Teacher On-Policy Distillation · 正文段落 41](https://arxiv.org/html/2610.12957v1#S4.SS2.p2.1)
- [S24] [4.2 Multi-Teacher On-Policy Distillation · 正文段落 42](https://arxiv.org/html/2610.12957v1#S4.E1)
- [S25] [4.2 Multi-Teacher On-Policy Distillation · 正文段落 43](https://arxiv.org/html/2610.12957v1#S4.SS2.p2.2)
- [S26] [4.2 Multi-Teacher On-Policy Distillation · 正文段落 44](https://arxiv.org/html/2610.12957v1#S4.SS2.p3.1)
- [S27] [4.3.3 Evidence-Weighted Policy Optimization · 正文段落 57](https://arxiv.org/html/2610.12957v1#S4.SS3.SSS3.p1.1)
- [S28] [4.4.1 Generative Process Evaluation · 正文段落 72](https://arxiv.org/html/2610.12957v1#S4.SS4.SSS1.p3.1)
- [S29] [5 Experiments · 正文段落 82](https://arxiv.org/html/2610.12957v1#S5.p1.1)
- [S30] [5.1 Experimental Setup · 正文段落 83](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px1.p1.1)
- [S31] [5.1 Experimental Setup · 正文段落 84](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px2.p1.1)
- [S32] [5.1 Experimental Setup · 正文段落 85](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px3.p1.1)
- [S33] [5.1 Experimental Setup · 正文段落 86](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px4.p1.1)
- [S34] [5.1 Experimental Setup · 正文段落 87](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px5.p1.1)
- [S35] [5.1 Experimental Setup · 正文段落 88](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px6.p1.1)
- [S36] [5.1 Experimental Setup · 正文段落 89](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px7.p1.1)
- [S37] [5.3 Benchmark Results · 正文段落 94](https://arxiv.org/html/2610.12957v1#S5.SS3.p1.1)
- [S38] [5.3 Benchmark Results · 正文段落 95](https://arxiv.org/html/2610.12957v1#S5.T1)
- [S39] [5.3 Benchmark Results · 正文段落 96](https://arxiv.org/html/2610.12957v1#S5.T1.5)
- [S40] [7 Limitations and Future Work · 正文段落 111](https://arxiv.org/html/2610.12957v1#S7.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/JoyInside-VLM-Agent Product-Conditioned Multimodal Policy Learning for Embodied.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied agents must translate multimodal observations and user requests into executable actions while adapting to product constraints, changing goals, and execution feedback. We present JoyInside-VLM-Agent, a ReAct-style multimodal agent developed through product-conditioned trajectory construction and staged policy learning for robotic platforms and smart hardware. A closed-loop sandbox generates multimodal interaction trajectories covering goal revisions and failure recovery, which are checked against execution outcomes and semantic criteria. Supervised fine-tuning and multi-teacher on-policy distillation precede reinforcement learning with DPER (Dual-Source Privileged On-Policy Self-Distillation with Token-Level Evidence Routing). DPER routes token-level evidence between a frozen privileged teacher and a privileged student sharing the rollout policy's parameters, modulating reward-derived token advantages while preserving their signs. Training rewards combine generative process evaluation, multi-judge rankings, and task-queue consistency. JoyInside-VLM-Agent achieves a BFCL v4 overall score of 77.44, exceeding the evaluated baselines; results on the other public benchmarks are mixed. On JoyInside-Devices and JoyInside-Robotics, the evaluated system, which includes domain-specific skill refinement, leads the baselines on all reported metrics. Two real-world quadruped case studies illustrate visually grounded search, replanning after execution failure, and explicit failure reporting.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12957v1
- Authors: Gangyi Li, LuYao Wang, Jingfu Sun, Jingyi Yuan, Hang Liu, Hao Zong, Yujia Hu, Tingting Gao, Jianyong Wang, Xu Yang
- Published: 2026-10-09T03:54:58Z
- Age days: 3

</details>
