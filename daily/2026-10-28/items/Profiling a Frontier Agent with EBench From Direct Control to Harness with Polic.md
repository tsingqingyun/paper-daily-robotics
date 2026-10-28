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
url: "https://arxiv.org/abs/2610.35832v1"
published: "2026-10-26T17:51:02Z"
age_days: 1
score: 42
created: 2026-10-28
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> EBench-Astra 检查 GPT-6-Astra 何时适合直接控制机器人，何时应该调用学过机器人示范的策略。组合后总体更强、更省token，但调用时机、子目标传递和控制交接仍会制造失败。

## 问题

机器人既要理解陌生指令，也要完成持续接触和精细对齐。VLA/WAM依赖机器人后训练数据；通用多模态模型理解灵活，却未必能稳定执行。已有组合系统常作为整体报告成绩，难以看出收益来自谁、交接又损失了什么。[S2](https://arxiv.org/html/2610.35832v1#S1.p1.1) [S4](https://arxiv.org/html/2610.35832v1#S1.p3.1) [S11](https://arxiv.org/html/2610.35832v1#S2.SS0.SSS0.Px2.p1.1)

### 用一个例子理解

理解用例（非论文实验）：输入“把碗拿出并叠到盘上”和相机画面；智能体调用策略完成取碗，再观察是否抓稳，接手调整落点；输出叠放动作。若接手时未持续夹紧，碗可能在交接中掉落。

## 创新点或方法

本文固定视觉与本体状态接口，比较直接控制、策略单独执行、智能体调用策略。Astra不更新参数，每项任务从一条示范获得上下文描述；推理时直接模式输出末端、底盘和夹爪路点，执行一段后再观察。组合模式可额外指定策略执行步数，但策略仍接收固定任务指令，不能接收智能体临时子目标。[S5](https://arxiv.org/html/2610.35832v1#S1.p4.1) [S13](https://arxiv.org/html/2610.35832v1#S3.SS2.p1.1) [S14](https://arxiv.org/html/2610.35832v1#S4.F1) [S15](https://arxiv.org/html/2610.35832v1#S4.SS2.p1.1)

### 方法如何工作

1. 从单条训练示范取得任务说明，为不更新参数的智能体提供操作上下文。
2. 输入当前RGB和机器人状态，智能体生成路点或决定委派。
3. 直接执行动作段，或让策略在限定步数内闭环执行，得到新观测。
4. 智能体检查进展并接手或继续委派；比较配对回合，定位收益和交接损失。

### 必要术语

- Harness：连接模型、观测和工具的控制程序；本文决定智能体能怎样调用机器人。
- 动作段：两次观测之间连续执行的一串动作；段内接触变化可能来不及纠正。
- 本体状态：机器人自身的位置、夹爪等测量；为视觉判断补充当前执行状态。

## 证据

在仿真EBench的510个测试回合中，直接控制成功率46.7%，阶段完成分0.654；短任务73.2%，长任务27.3%，桌面操作20.0%，精密接触任务11.3%。它超过包括π0.5在内的部分后训练策略，但非所有策略。[S5](https://arxiv.org/html/2610.35832v1#S1.p4.1) [S6](https://arxiv.org/html/2610.35832v1#S1.p5.1) 调用π0.5或InternW0-Δ后，总成功率为53.0%和56.0%，每次成功的token成本下降超过一半。[S7](https://arxiv.org/html/2610.35832v1#S1.p6.1) 结果显示能力互补，尚未达到逐任务选择更强组件的上界。

## 局限

作者观察到路点之间缺少及时修正、交接后夹持未维持，以及可能损伤硬件的突然转腕；这些是仿真中的执行风险，不能当作真机已验证结果。[S17](https://arxiv.org/html/2610.35832v1#S7.p1.1) [S18](https://arxiv.org/html/2610.35832v1#S7.p2.1) 两项任务的直接模式时限较短，解释了组合总分中的小部分增益。[S20](https://arxiv.org/html/2610.35832v1#A2.SS2.SSS0.Px1.p1.1) 相同观测接口也不意味着推理预算相同。

- **判断**：值得读执行轨迹和失败交接案例；它对组合控制的诊断，比总体分数更能指导实现。

## 研究关联

组合系统应把“谁来做、做哪一步、交回时保持什么状态”当成明确接口。仅给大模型增加一个策略调用按钮，并不会自动获得两者最好的能力。

### 下一步读哪里

先读[S13](https://arxiv.org/html/2610.35832v1#S3.SS2.p1.1)明确策略到底接收什么，再看[S17](https://arxiv.org/html/2610.35832v1#S7.p1.1) [S18](https://arxiv.org/html/2610.35832v1#S7.p2.1)的交接失败；核查调用比例、动作段长度、抓取保持机制，并结合[S20](https://arxiv.org/html/2610.35832v1#A2.SS2.SSS0.Px1.p1.1)校正时限差异。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：42
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.35832v1
- 获取时间：2026-10-28T01:41:08.158608+00:00
- [S1] [Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy · 正文段落 1](https://arxiv.org/html/2610.35832v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.35832v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.35832v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.35832v1#S1.p3.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.35832v1#S1.p4.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.35832v1#S1.p5.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.35832v1#S1.p6.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.35832v1#S1.I1.i1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.35832v1#S1.I1.i2)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.35832v1#S1.I1.i3)
- [S11] [Harness with policy. · 正文段落 13](https://arxiv.org/html/2610.35832v1#S2.SS0.SSS0.Px2.p1.1)
- [S12] [3 Problem Formulation · 正文段落 14](https://arxiv.org/html/2610.35832v1#S3.p1.1)
- [S13] [3.2 Direct Control and Harness with Policy · 正文段落 18](https://arxiv.org/html/2610.35832v1#S3.SS2.p1.1)
- [S14] [4 Experimental Setup · 正文段落 19](https://arxiv.org/html/2610.35832v1#S4.F1)
- [S15] [4.2 Agent and Control Interface · 正文段落 22](https://arxiv.org/html/2610.35832v1#S4.SS2.p1.1)
- [S16] [Direct control. · 正文段落 26](https://arxiv.org/html/2610.35832v1#S4.SS3.SSS0.Px1.p1.1)
- [S17] [7 Conclusions and Future Directions · 正文段落 88](https://arxiv.org/html/2610.35832v1#S7.p1.1)
- [S18] [7 Conclusions and Future Directions · 正文段落 89](https://arxiv.org/html/2610.35832v1#S7.p2.1)
- [S19] [Task prompt. · 正文段落 99](https://arxiv.org/html/2610.35832v1#A1.SS1.SSS0.Px2.p2.1)
- [S20] [Evaluation records. · 正文段落 133](https://arxiv.org/html/2610.35832v1#A2.SS2.SSS0.Px1.p1.1)
- [S21] [Appendix D Additional Qualitative Results · 正文段落 163](https://arxiv.org/html/2610.35832v1#A4.p1.1)
- [S22] [Appendix D Additional Qualitative Results · 正文段落 164](https://arxiv.org/html/2610.35832v1#A4.F1)
- [S23] [Appendix D Additional Qualitative Results · 正文段落 165](https://arxiv.org/html/2610.35832v1#A4.F2)
- [S24] [Appendix D Additional Qualitative Results · 正文段落 166](https://arxiv.org/html/2610.35832v1#A4.F3)
- [S25] [Appendix D Additional Qualitative Results · 正文段落 167](https://arxiv.org/html/2610.35832v1#A4.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/Profiling a Frontier Agent with EBench From Direct Control to Harness with Polic.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be thoroughly evaluated. In this report, we evaluate GPT-6-Astra on EBench as the core of an agent that controls a robot through an agent harness under the same visual and proprioceptive observation protocol as post-trained policies. We study two agent configurations: direct control, in which the agent generates waypoint commands directly, and harness with policy, in which it can also invoke a post-trained VLA or WAM policy for action execution. Under direct control, the agent achieves competitive overall performance relative to post-trained policies. It leads on short-horizon tasks and exhibits the least performance variation across generalization dimensions, whereas it underperforms post-trained policies on long-horizon tasks, tabletop manipulation, and high-precision contact-rich tasks. In the harness with policy, invoking a post-trained VLA or WAM combines the complementary strengths of both components, raising overall task success to the level of the strongest compared post-trained policies while substantially reducing token cost. However, performance remains below the per-task upper bound of the standalone components due to suboptimal policy invocation, fixed-instruction execution without subgoals, and grasp disruption when the agent resumes control. Overall, our study characterizes the capability boundary of a frontier MLLM agent and suggests directions for improving future agent harness design. Project page: https://internrobotics.github.io/EBench-Astra-Tech-Report/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.35832v1
- Authors: Yifei Yao, Yude Zou, Guanbo Jiao, Xing Gao, Ning Gao, Yukai Wang, Jiantong Chen, Zihou Zhu, Xinyu Li, Ningyu Yan, Shuai Wang, Jianming Ma, Haoyu Guo, Weinan Zhang, Chunhua Shen
- Published: 2026-10-26T17:51:02Z
- Age days: 1

</details>
