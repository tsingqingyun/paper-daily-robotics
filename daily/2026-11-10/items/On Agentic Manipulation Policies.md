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
url: "https://arxiv.org/abs/2611.09892v1"
published: "2026-11-06T18:59:34Z"
age_days: 3
score: 41
created: 2026-11-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# On Agentic Manipulation Policies

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> AMP1 让通用 AI 模型直接看机器人画面、写代码并发出运动命令，执行一段后再观察和改策略。它不预置抓取、推放技能，而是把这些动作的组织交给模型；增加持久记忆后，还能复用此前尝试得到的经验。

## 问题

传统专用策略依赖示范训练，遇到陌生语义或难以直接抓取的物体可能反复执行无效动作。让通用模型只选择预置技能，又受技能能力限制；一次性生成程序则不能让模型在执行中重新考虑整体策略。[S5](https://arxiv.org/html/2611.09892v1#S1.p2.1) 本文考察给模型更细控制权，能否改善这种僵持。

### 用一个例子理解

理解用例（非论文实验）：输入“把托盘上的盒子取出”和相机画面；模型发现夹爪无处伸入，先命令将盒子推到边缘，再重新观察并计算抓取位置，最后取出。输出是一串可随反馈调整的运动命令。

## 创新点或方法

AMP1 提供视觉、代码执行和机械臂运动接口，模型反复观察、计算并执行，再根据新状态调整。基本模式没有任务专用训练或示范，但仍依赖底层运动规划和控制。[S6](https://arxiv.org/html/2611.09892v1#S1.p4.1) [S14](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p4.1) 经验学习时，反思过程读取尝试记录及二元成败反馈，把规则与代码写进跨回合记忆；模型权重不变，评估时使用冻结记忆。[S19](https://arxiv.org/html/2611.09892v1#S2.SS3.SSS0.Px1.p1.1) 因而“学会了”主要体现为外部记忆和程序变化。

### 方法如何工作

1. 读取指令、相机与机器人状态，判断任务条件，形成当前可执行的动作策略。
2. 生成代码调用运动接口，将策略变成轨迹；底层控制负责实际执行。
3. 执行后获取新画面与错误状态，修正判断或请求恢复，使模型持续参与任务。
4. 练习模式汇总成败与记录，更新规则和代码记忆，再冻结记忆测试新布局，检验经验能否复用。

### 必要术语

- AMP：通用模型在执行过程中持续指挥操作的策略形式；本文用它直接组织机械臂动作。
- Harness：连接模型、观察、代码和机器人接口的运行环境；它决定模型能看到和控制什么。
- 持久记忆：跨回合保留的规则、观察与代码；本文通过它积累经验，不更新模型权重。
- 准静态场景：决策间隙中环境变化较慢；本文的推理等待在这类条件下更可容忍。

## 证据

RoboLab-120 仿真成功率为 85.6%，对照 VLA、WAM 为 49.2%、42.9%（摘要）。Franka 真机 12 项任务共 108 次，AMP1 成功 104 次，FLUX 和 π₀.₅ 分别成功 49、30 次。[S6](https://arxiv.org/html/2611.09892v1#S1.p4.1) [S11](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p1.1) 允许控制器报错恢复时为上述成绩，不提供恢复接口则降到 94 次。[S14](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p4.1) RoboDojo 仿真练习后从 26.4% 到 84.1%，但每任务练习五次并选最成功的一次评估。[S18](https://arxiv.org/html/2611.09892v1#S2.F4) 不能据此推断所有任务都稳定复现。

## 局限

作者明确说明机器人常等待模型推理，轨迹执行中模型无法重新决策，评测主要是准静态场景。[S22](https://arxiv.org/html/2611.09892v1#S3.SS2.p1.1) 我会核查基线的适配预算、恢复权限和时限是否一致；当前优势属于整套模型与接口系统，不能单独归因于“推理”。

- **判断**：值得深入读控制接口、恢复协议和评测设置；结果有冲击力，但对动态操作和实时控制的结论必须收窄。

## 研究关联

困难有时来自行动策略选错，而非动作预测不够精细。值得借鉴的是保留观察后改变策略的能力，并将已成功的程序存下来，减少每回合重新推导；适用前提是场景允许较慢的观察与决策循环。

### 下一步读哪里

先看 [S14](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p4.1) [S22](https://arxiv.org/html/2611.09892v1#S3.SS2.p1.1) 理解碰撞恢复和决策时序，再读 [S18](https://arxiv.org/html/2611.09892v1#S2.F4) [S19](https://arxiv.org/html/2611.09892v1#S2.SS3.SSS0.Px1.p1.1) [S20](https://arxiv.org/html/2611.09892v1#S2.SS3.SSS0.Px1.p2.1) 的练习预算、最佳运行选择与记忆冻结。核查完整接口是否依赖深度和标定，以及成功率对应的耗时、调用成本和基线公平性。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.09892v1
- 获取时间：2026-11-10T00:15:39.859985+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.09892v1#p1.2)
- [S2] [On Agentic Manipulation Policies · 正文段落 2](https://arxiv.org/html/2611.09892v1#abstract1.1)
- [S3] [On Agentic Manipulation Policies · 正文段落 3](https://arxiv.org/html/2611.09892v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.09892v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.09892v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.09892v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.09892v1#S1.p6.1)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.09892v1#S1.p7.1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.09892v1#S1.p8.1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.09892v1#S1.F2)
- [S11] [2A.2 Real-world trials · 正文段落 25](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p1.1)
- [S12] [2A.2 Real-world trials · 正文段落 26](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p2.1)
- [S13] [2A.2 Real-world trials · 正文段落 27](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p3.1)
- [S14] [2A.2 Real-world trials · 正文段落 28](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p4.1)
- [S15] [2A.2 Real-world trials · 正文段落 29](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p5.1)
- [S16] [2C Learning from Experience · 正文段落 48](https://arxiv.org/html/2611.09892v1#S2.SS3.p4.1)
- [S17] [2C Learning from Experience · 正文段落 50](https://arxiv.org/html/2611.09892v1#S2.SS3.p6.1)
- [S18] [2C Learning from Experience · 正文段落 51](https://arxiv.org/html/2611.09892v1#S2.F4)
- [S19] [2C Learning from Experience · 正文段落 52](https://arxiv.org/html/2611.09892v1#S2.SS3.SSS0.Px1.p1.1)
- [S20] [2C Learning from Experience · 正文段落 53](https://arxiv.org/html/2611.09892v1#S2.SS3.SSS0.Px1.p2.1)
- [S21] [3A AMP1 versus other manipulation policies · 正文段落 75](https://arxiv.org/html/2611.09892v1#S3.SS1.SSS0.Px2.p1.1)
- [S22] [3B Outlook · 正文段落 79](https://arxiv.org/html/2611.09892v1#S3.SS2.p1.1)
- [S23] [3B Outlook · 正文段落 80](https://arxiv.org/html/2611.09892v1#S3.SS2.p2.1)
- [S24] [S1 Real-world trials · 正文段落 118](https://arxiv.org/html/2611.09892v1#S5.F1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-10/On Agentic Manipulation Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged across single-arm, bimanual, and mobile manipulation. AMP1 achieves state-of-the-art results on the RoboLab-120 and CaP-Gym benchmarks, with no demonstrations or task-specific training. On RoboLab-120, AMP1 reaches an 85.6\% success rate zero-shot, compared to 49.2\% and 42.9\% for leading VLA and WAM policies. The agent succeeds zero-shot in 104 of 108 real-world trials spanning twelve tasks and three robot instances, reducing failure rates by 20x and 15x relative to strong VLA and WAM baselines. The basic harness supplies no grasping, pushing, or placing skills; the agent develops its own strategies, such as searching for hidden objects, using objects as tools, and calibrating its cameras. With the addition of a persistent memory store, the agent can also learn from experience: an augmented harness with a memory representation that is carried across episodes lowers the failure rate on RoboDojo bimanual manipulation tasks by 4.6x relative to zero-shot deployment. Our analysis suggests that AMPs are substantially more general and robust than specialist manipulation policies, providing a promising foundation for robot manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.09892v1
- Authors: Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi, Fahad Islam, Xueting Li, Jean-Baptiste Regli, Kejia Ren, Petr Švec, David J. Yoon, Matthias Müller, Vladlen Koltun
- Published: 2026-11-06T18:59:34Z
- Age days: 3

</details>
