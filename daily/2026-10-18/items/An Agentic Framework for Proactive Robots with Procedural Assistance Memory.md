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
url: "https://arxiv.org/abs/2610.21211v1"
published: "2026-10-15T04:04:49Z"
age_days: 2
score: 30
created: 2026-10-18
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# An Agentic Framework for Proactive Robots with Procedural Assistance Memory

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PAM 让机器人根据“这个人平时怎样做事”决定何时帮忙，而不只凭眼前画面猜需求。它把习惯写成活动阶段、阶段内规则和切换条件，每天复盘后改记忆，再交给 VLA 执行动作。

## 问题

任务是在用户开口前递物、收拾，难点是同一物体在不同阶段意味着不同动作，同一行为对不同用户也可能意味着不同需求。固定流程方法不适合开放日常活动；零样本 VLM 缺少个人习惯，遇到歧义容易一直不行动 [S4](https://arxiv.org/html/2610.21211v1#S1.p2.1) [S5](https://arxiv.org/html/2610.21211v1#S1.p3.1) [S25](https://arxiv.org/html/2610.21211v1#S4.SS2.SSS0.Px1.p1.1)。

### 用一个例子理解

理解用例（非论文实验）：用户把杯子放下 → 预测器结合 PAM 判断仍处于泡茶阶段，而非收拾阶段 → 输出递茶包任务；若没有符合的阶段规则，则输出暂不行动。

## 创新点或方法

旧做法直接从观察推断任务；本文让预测器同时读观察和 PAM，用当前活动阶段约束可触发的帮助。部署时预测任务或 NO_ACT，执行器只负责指定技能；每天结束后，反思模型根据视频和反馈修改记忆。这里“不重训”指日常记忆更新：执行器此前仍需用示范微调 [S6](https://arxiv.org/html/2610.21211v1#S1.I1.i3) [S17](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px3.p1.1) [S35](https://arxiv.org/html/2610.21211v1#A1.SS3.SSS0.Px1.p1.1)。

### 方法如何工作

1. 读取近期画面与 PAM，得到当前活动阶段及相关规则，以减少仅凭物体猜需求的歧义。
2. 据此选择任务或 NO_ACT，把是否介入与具体动作执行分开。
3. VLA 接收任务指令并执行，使动作模型专注于已训练技能。
4. 日终复盘视频和反馈，修改规则与切换条件，供次日预测使用。

### 必要术语

- 有限状态机：用阶段及切换条件表示流程；PAM 借此限定规则的适用时机。
- NO_ACT：当前不需要帮助；避免把每帧都强行分配给某项任务。
- 首次触发延迟：从应当帮助到首次预测对应任务的时间；未触发时按用户自行完成的时刻计时。

## 证据

桌面早餐流程包含递麦片、递牛奶及餐后收拾。预测评测按视频帧分类，比较 LIT、事件触发 VLM、零样本 VLM和列表记忆，报告各类及宏平均 precision、recall、F1 [S15](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px1.p1.1) [S16](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px2.p1.1) [S17](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px3.p1.1) [S18](https://arxiv.org/html/2610.21211v1#S4.F5) [S19](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px4.p1.1) [S20](https://arxiv.org/html/2610.21211v1#S4.I2.i1) [S21](https://arxiv.org/html/2610.21211v1#S4.I2.i2) [S22](https://arxiv.org/html/2610.21211v1#S4.I2.i3) [S23](https://arxiv.org/html/2610.21211v1#S4.I2.i4)。FSM 版本首次触发延迟从首日约5秒降至第五日约1秒，但节选没有完整分类分数 [S26](https://arxiv.org/html/2610.21211v1#S4.SS2.SSS0.Px2.p1.1)。更换流程后，一次反思使其次日表现接近从头积累记忆的版本 [S28](https://arxiv.org/html/2610.21211v1#S4.SS3.SSS0.Px1.p2.1)。Franka 真机执行中，收牛奶为5/10，对比普通与推理版 VLA 均为0/10；递牛奶仍只有3/10 [S32](https://arxiv.org/html/2610.21211v1#S4.T1.4.1) [S34](https://arxiv.org/html/2610.21211v1#A1.SS3.p1.1)。预测及时与动作可靠是两件事。

## 局限

作者明确指出，更积极行动会降低 NO_ACT 召回率，误介入仍待减少 [S26](https://arxiv.org/html/2610.21211v1#S4.SS2.SSS0.Px2.p1.1)。我的核查重点是用户数量、反馈成本和连续运行表现；逐帧预测结果不能直接等同于完整服务成功率，流程切换实验也不足以证明任意习惯变化都能一次适应。

- **判断**：值得读方法和记忆消融：它清楚展示了个人习惯如何进入决策，但尚不能据此判断长期家庭服务的可靠性。

## 研究关联

值得借鉴的是给规则加上“在哪个阶段有效”。当同一视觉线索反复出现、却需要不同回应时，阶段化记忆比不断追加触发规则更容易消除歧义。

### 下一步读哪里

先核查 PAM 如何初始化、状态如何切换以及错误规则怎样删除或改写；结合 [S23](https://arxiv.org/html/2610.21211v1#S4.I2.i4) [S26](https://arxiv.org/html/2610.21211v1#S4.SS2.SSS0.Px2.p1.1) [S41](https://arxiv.org/html/2610.21211v1#A3.SS1.p1.1) [S42](https://arxiv.org/html/2610.21211v1#A3.SS1.SSS0.Px1.p1.1) 检查结构与持续更新各自的贡献，再查延迟统计和误介入案例。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.21211v1
- 获取时间：2026-10-18T03:39:24.880269+00:00
- [S1] [An Agentic Framework for Proactive Robots with Procedural Assistance Memory · 正文段落 1](https://arxiv.org/html/2610.21211v1#abstract1.1)
- [S2] [An Agentic Framework for Proactive Robots with Procedural Assistance Memory · 正文段落 2](https://arxiv.org/html/2610.21211v1#p2.1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.21211v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.21211v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.21211v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.21211v1#S1.I1.i3)
- [S7] [2.2 Proactive Assistance in Embodied HRI · 正文段落 13](https://arxiv.org/html/2610.21211v1#S2.SS2.p1.1)
- [S8] [3 Method · 正文段落 17](https://arxiv.org/html/2610.21211v1#S3.p1.1)
- [S9] [4 Experiments · 正文段落 26](https://arxiv.org/html/2610.21211v1#S4.p1.1)
- [S10] [4 Experiments · 正文段落 27](https://arxiv.org/html/2610.21211v1#S4.I1.i1)
- [S11] [4 Experiments · 正文段落 28](https://arxiv.org/html/2610.21211v1#S4.I1.i2)
- [S12] [4 Experiments · 正文段落 29](https://arxiv.org/html/2610.21211v1#S4.I1.i3)
- [S13] [4 Experiments · 正文段落 30](https://arxiv.org/html/2610.21211v1#S4.I1.i4)
- [S14] [4 Experiments · 正文段落 31](https://arxiv.org/html/2610.21211v1#S4.F4)
- [S15] [4.1 Experimental Setup · 正文段落 32](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px1.p1.1)
- [S16] [4.1 Experimental Setup · 正文段落 33](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px2.p1.1)
- [S17] [4.1 Experimental Setup · 正文段落 34](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px3.p1.1)
- [S18] [4.1 Experimental Setup · 正文段落 35](https://arxiv.org/html/2610.21211v1#S4.F5)
- [S19] [4.1 Experimental Setup · 正文段落 36](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px4.p1.1)
- [S20] [4.1 Experimental Setup · 正文段落 37](https://arxiv.org/html/2610.21211v1#S4.I2.i1)
- [S21] [4.1 Experimental Setup · 正文段落 38](https://arxiv.org/html/2610.21211v1#S4.I2.i2)
- [S22] [4.1 Experimental Setup · 正文段落 39](https://arxiv.org/html/2610.21211v1#S4.I2.i3)
- [S23] [4.1 Experimental Setup · 正文段落 40](https://arxiv.org/html/2610.21211v1#S4.I2.i4)
- [S24] [4.1 Experimental Setup · 正文段落 41](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px4.p2.1)
- [S25] [4.2 Proactive Prediction across Memory Designs · 正文段落 45](https://arxiv.org/html/2610.21211v1#S4.SS2.SSS0.Px1.p1.1)
- [S26] [4.2 Proactive Prediction across Memory Designs · 正文段落 46](https://arxiv.org/html/2610.21211v1#S4.SS2.SSS0.Px2.p1.1)
- [S27] [4.3 Memory Adaptation and Evolution · 正文段落 47](https://arxiv.org/html/2610.21211v1#S4.SS3.SSS0.Px1.p1.1)
- [S28] [4.3 Memory Adaptation and Evolution · 正文段落 48](https://arxiv.org/html/2610.21211v1#S4.SS3.SSS0.Px1.p2.1)
- [S29] [4.4 Comparison with Monolithic VLAs · 正文段落 51](https://arxiv.org/html/2610.21211v1#S4.SS4.p1.1)
- [S30] [4.4 Comparison with Monolithic VLAs · 正文段落 52](https://arxiv.org/html/2610.21211v1#S4.SS4.p2.1)
- [S31] [4.4 Comparison with Monolithic VLAs · 正文段落 53](https://arxiv.org/html/2610.21211v1#S4.T1)
- [S32] [4.4 Comparison with Monolithic VLAs · 正文段落 54](https://arxiv.org/html/2610.21211v1#S4.T1.4.1)
- [S33] [Appendix · 正文段落 59](https://arxiv.org/html/2610.21211v1#Ax1.p1.1)
- [S34] [A.3 Training and Deployment for VLAs · 正文段落 68](https://arxiv.org/html/2610.21211v1#A1.SS3.p1.1)
- [S35] [A.3 Training and Deployment for VLAs · 正文段落 69](https://arxiv.org/html/2610.21211v1#A1.SS3.SSS0.Px1.p1.1)
- [S36] [A.3 Training and Deployment for VLAs · 正文段落 70](https://arxiv.org/html/2610.21211v1#A1.SS3.SSS0.Px2.p1.1)
- [S37] [A.3 Training and Deployment for VLAs · 正文段落 71](https://arxiv.org/html/2610.21211v1#A1.SS3.SSS0.Px3.p1.1)
- [S38] [A.3 Training and Deployment for VLAs · 正文段落 72](https://arxiv.org/html/2610.21211v1#A1.SS3.SSS0.Px4.p1.1)
- [S39] [A.4 Hardware Setup · 正文段落 76](https://arxiv.org/html/2610.21211v1#A1.SS4.SSS0.Px3.p1.1)
- [S40] [Appendix B Per-task Results of VLM Proactiveness · 正文段落 81](https://arxiv.org/html/2610.21211v1#A2.SS0.SSS0.Px4.p1.1)
- [S41] [C.1 Effectiveness of Memory Evolution · 正文段落 89](https://arxiv.org/html/2610.21211v1#A3.SS1.p1.1)
- [S42] [C.1 Effectiveness of Memory Evolution · 正文段落 90](https://arxiv.org/html/2610.21211v1#A3.SS1.SSS0.Px1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/An Agentic Framework for Proactive Robots with Procedural Assistance Memory.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Proactive robots should anticipate user needs and provide assistance before being explicitly asked. A straightforward approach is to infer human intentions from commonsense knowledge, but the same observed behavior can imply different needs across users, potentially leading to unwanted assistance. We observe that everyday routines in the real world exhibit recurring patterns, so learning these patterns can reduce ambiguity in proactive decisions. Based on this, we propose a memory-based agentic framework in which a VLM task predictor reads a Procedural Assistance Memory (PAM) alongside the current observation to decide when to assist and what task to perform, and a VLA executor performs the predicted task. PAM is structured as a finite-state machine over activity phases, per-state assistance rules, and event-driven transitions; a reflection VLM revises PAM from each day's interaction trace without weight updates or retraining. In our 5-day desk-assistance evaluation, memory-free baselines remain conservative, with limited recall on proactive tasks. Our system improves consistently with accumulated experience, achieving the highest precision, recall, and F1 and reducing first-fire delay from approximately 5 seconds on Day 1 to 1 second by Day 5. Our approach also adapts to changes in the user's routine through continued memory reflection, recovering from memory--routine misalignment after a single memory update. The project page is available at https://davian-robotics.github.io/PAM/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21211v1
- Authors: Dohyun Lee, Minho Park, Jeonghoon Park, Dongyoon Hwang, Junha Hyung, Sungwon Hwang, Byungkun Lee, Jaegul Choo
- Published: 2026-10-15T04:04:49Z
- Age days: 2

</details>
