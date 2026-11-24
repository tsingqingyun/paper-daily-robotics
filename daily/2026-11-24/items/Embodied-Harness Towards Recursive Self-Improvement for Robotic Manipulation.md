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
url: "https://arxiv.org/abs/2611.27689v1"
published: "2026-11-20T14:55:07Z"
age_days: 3
score: 35
created: 2026-11-24
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Embodied-Harness 让 Actor 操作机器人，让 Reflector 根据动作、反馈和现场变化写下以后能用的操作规则。后续尝试复用这些规则，模型参数保持冻结。

## 问题

多步操作中，智能体要记住做到了哪一步、哪些前置条件已满足，以及环境被前几步怎样改变。失败结果往往只告诉你动作没成，无法直接指出是定位错、顺序错还是条件没满足。即使某轮找到了原因，后续尝试也可能读不到这条经验。[S4](https://arxiv.org/html/2611.27689v1#S1.p3.1)[S12](https://arxiv.org/html/2611.27689v1#S3.SS3.p1.1)

### 用一个例子理解

理解用例（非论文实验）——机器人要先拉开抽屉再放入积木。第一次夹爪返回动作完成，但相机显示抽屉只开了一条缝，积木随后放不进去。Reflector 据此写下「放入前确认开口足够」的操作提示。下次 Actor 做完拉开动作就检查开口，必要时再拉，随后才放积木。

## 创新点或方法

普通执行过程容易把进度和诊断散在交互记录里。这里 Actor 一边做动作，一边把已完成子目标、待办和约束压成短期记忆，同时保留观测、状态、动作与反馈作为证据。Reflector 根据这些记录定位可疑错误，把诊断写成后续可用的操作指导，逐轮修订长期经验。执行侧根据观测与记忆选动作，尝试之间更新的是记忆和指导，无需训练模型权重。[S1](https://arxiv.org/html/2611.27689v1#abstract1.1)[S10](https://arxiv.org/html/2611.27689v1#S3.SS1.p4.2) [S11](https://arxiv.org/html/2611.27689v1#S3.SS2.p3.1) [S12](https://arxiv.org/html/2611.27689v1#S3.SS3.p1.1) [S13](https://arxiv.org/html/2611.27689v1#S3.I1.i2) [S14](https://arxiv.org/html/2611.27689v1#S3.I1.i3)[S39](https://arxiv.org/html/2611.27689v1#S4.SS4.p1.1)

### 方法如何工作

1. Actor 读取任务和观测，选取动作，并记录执行前后的状态与反馈，留下可回查的证据。
2. 把已完成和待完成的子目标压成简短进度，让后续动作能接上当前任务状态。
3. Reflector 回看轨迹，把可能导致失败的动作或缺失的检查写成可执行指导。
4. 后续尝试读取相关经验并按新反馈修订，让下一轮可以沿用已验证过的操作判断。

### 必要术语

- 短期工作记忆：本轮的进度、约束和交互摘要；帮助 Actor 选下一步。
- 长期经验记忆：跨尝试保存的操作指导；供后续执行与反思调用。
- 证据约束的反思：依据观测、动作与反馈提出诊断；用来把失败描述转成可检查的操作建议。

## 证据

RoboTwin 2.0 从干净到随机化场景的仿真中，零示范、同用 GPT-6 Astra 时，成功率为 82.4%，RoboDawn 为 53.2%。RoboSPA L5 空间子集为 94.0% 对 65.6%，长流程为 59.5% 对 41.4%，摘要的 76.7% 是 RoboSPA 汇总。RMBench 记忆任务为 94.4%，比 MaP-WAM 高 11.1 个百分点。Piper 真机三项任务各 10 回合，平均成功率为 96.7%，π₀.₅ 为 40.0%。[S1](https://arxiv.org/html/2611.27689v1#abstract1.1)[S16](https://arxiv.org/html/2611.27689v1#S3.T1.4) [S17](https://arxiv.org/html/2611.27689v1#S4.SS1.p1.1) [S18](https://arxiv.org/html/2611.27689v1#S4.SS1.p2.1) [S19](https://arxiv.org/html/2611.27689v1#S4.T2) [S20](https://arxiv.org/html/2611.27689v1#S4.T2.2) [S21](https://arxiv.org/html/2611.27689v1#S4.T3) [S22](https://arxiv.org/html/2611.27689v1#S4.T3.2)[S25](https://arxiv.org/html/2611.27689v1#S4.T6.fig1.1)[S33](https://arxiv.org/html/2611.27689v1#S4.SS2.p5.1)

## 局限

作者把跨任务和跨机器人复用、减少执行与反思开销留给后续工作。[S40](https://arxiv.org/html/2611.27689v1#S5.p1.1) 我会核查反思轮次用过哪些案例，评估实例是否独立，以及同推理预算下还能保留多少增幅。真机数字只覆盖所测的三项任务。

- **判断**：值得读到去掉短期记忆和去掉 Reflector 的两项消融，再看逐轮曲线，才能区分本轮记得住和下轮借得到经验的收益。[S27](https://arxiv.org/html/2611.27689v1#S4.T6.fig2.1)[S39](https://arxiv.org/html/2611.27689v1#S4.SS4.p1.1)

## 研究关联

执行日志可以直接参与下次决策。如果失败与某个可复查的前置条件有关，例如动作发出前物体姿态就不对，那么一条带检查动作的指导会比笼统记录「上次放置失败」更容易复用。

### 下一步读哪里

用 [S10](https://arxiv.org/html/2611.27689v1#S3.SS1.p4.2) [S11](https://arxiv.org/html/2611.27689v1#S3.SS2.p3.1) [S12](https://arxiv.org/html/2611.27689v1#S3.SS3.p1.1) 对照轨迹证据和进度摘要，再看 [S27](https://arxiv.org/html/2611.27689v1#S4.T6.fig2.1)[S39](https://arxiv.org/html/2611.27689v1#S4.SS4.p1.1) 的消融与迭代结果。进一步核查经验怎样检索、相互冲突的规则怎样更新，以及反思时允许访问哪些试次。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.27689v1
- 获取时间：2026-11-24T01:58:56.740788+00:00
- [S1] [Embodied-Harness: Towards Recursive Self- Improvement for Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2611.27689v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.27689v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.27689v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.27689v1#S1.p3.1)
- [S5] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.27689v1#S1.p5.1)
- [S6] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.27689v1#S1.I1.i3)
- [S7] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.27689v1#S1.I1.i4)
- [S8] [2.1 End-to-End Models for Robotic Manipulation · 正文段落 12](https://arxiv.org/html/2611.27689v1#S2.SS1.p1.1)
- [S9] [2.2 Agentic Frameworks for Robotic Manipulation · 正文段落 13](https://arxiv.org/html/2611.27689v1#S2.SS2.p1.1)
- [S10] [3.1 Framework Overview · 正文段落 25](https://arxiv.org/html/2611.27689v1#S3.SS1.p4.2)
- [S11] [3.2 Hierarchical Memory Architecture · 正文段落 28](https://arxiv.org/html/2611.27689v1#S3.SS2.p3.1)
- [S12] [3.3 Evidence-based Experience Reflection · 正文段落 45](https://arxiv.org/html/2611.27689v1#S3.SS3.p1.1)
- [S13] [3.3 Evidence-based Experience Reflection · 正文段落 51](https://arxiv.org/html/2611.27689v1#S3.I1.i2)
- [S14] [3.3 Evidence-based Experience Reflection · 正文段落 52](https://arxiv.org/html/2611.27689v1#S3.I1.i3)
- [S15] [3.4 Recursive Harness Self-Improvement · 正文段落 63](https://arxiv.org/html/2611.27689v1#S3.T1)
- [S16] [3.4 Recursive Harness Self-Improvement · 正文段落 64](https://arxiv.org/html/2611.27689v1#S3.T1.4)
- [S17] [4.1 Experimental Setup · 正文段落 65](https://arxiv.org/html/2611.27689v1#S4.SS1.p1.1)
- [S18] [4.1 Experimental Setup · 正文段落 66](https://arxiv.org/html/2611.27689v1#S4.SS1.p2.1)
- [S19] [4.2 Main Results · 正文段落 67](https://arxiv.org/html/2611.27689v1#S4.T2)
- [S20] [4.2 Main Results · 正文段落 68](https://arxiv.org/html/2611.27689v1#S4.T2.2)
- [S21] [4.2 Main Results · 正文段落 69](https://arxiv.org/html/2611.27689v1#S4.T3)
- [S22] [4.2 Main Results · 正文段落 70](https://arxiv.org/html/2611.27689v1#S4.T3.2)
- [S23] [4.2 Main Results · 正文段落 71](https://arxiv.org/html/2611.27689v1#S4.T4)
- [S24] [4.2 Main Results · 正文段落 73](https://arxiv.org/html/2611.27689v1#S4.T6.fig1)
- [S25] [4.2 Main Results · 正文段落 74](https://arxiv.org/html/2611.27689v1#S4.T6.fig1.1)
- [S26] [4.2 Main Results · 正文段落 75](https://arxiv.org/html/2611.27689v1#S4.T6.fig2)
- [S27] [4.2 Main Results · 正文段落 76](https://arxiv.org/html/2611.27689v1#S4.T6.fig2.1)
- [S28] [4.2 Main Results · 正文段落 77](https://arxiv.org/html/2611.27689v1#S4.SS2.p1.1)
- [S29] [4.2 Main Results · 正文段落 78](https://arxiv.org/html/2611.27689v1#S4.SS2.p2.1)
- [S30] [4.2 Main Results · 正文段落 79](https://arxiv.org/html/2611.27689v1#S4.F2)
- [S31] [4.2 Main Results · 正文段落 80](https://arxiv.org/html/2611.27689v1#S4.SS2.p3.1)
- [S32] [4.2 Main Results · 正文段落 81](https://arxiv.org/html/2611.27689v1#S4.SS2.p4.1)
- [S33] [4.2 Main Results · 正文段落 82](https://arxiv.org/html/2611.27689v1#S4.SS2.p5.1)
- [S34] [4.2 Main Results · 正文段落 83](https://arxiv.org/html/2611.27689v1#S4.F3)
- [S35] [4.2 Main Results · 正文段落 84](https://arxiv.org/html/2611.27689v1#S4.SS2.p6.1)
- [S36] [4.2 Main Results · 正文段落 88](https://arxiv.org/html/2611.27689v1#S4.F6)
- [S37] [4.3 Ablation Studies · 正文段落 89](https://arxiv.org/html/2611.27689v1#S4.SS3.p1.1)
- [S38] [4.3 Ablation Studies · 正文段落 90](https://arxiv.org/html/2611.27689v1#S4.SS3.p2.1)
- [S39] [4.4 In-Depth Analysis · 正文段落 92](https://arxiv.org/html/2611.27689v1#S4.SS4.p1.1)
- [S40] [5 Conclusion · 正文段落 94](https://arxiv.org/html/2611.27689v1#S5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/Embodied-Harness Towards Recursive Self-Improvement for Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that improves manipulation by refining the execution harness without updating model parameters. The Actor interacts with the environment through a robot-control interface, while the Reflector converts execution evidence into reusable operational guidance. Hierarchical Memory Architecture maintains short-term execution context and long-term experiential knowledge to support execution and reflection. Evidence-based Experience Reflection grounds failure diagnosis in observed interactions, while Recursive Harness Self-Improvement refines operational guidance across successive attempts. Experiments on RoboTwin 2.0, RoboSPA, and RMBench demonstrate the effectiveness of Embodied-Harness in generalization under environmental variations, spatial reasoning, long-horizon planning, and memory-dependent manipulation. Our method achieves success rates of 82.4%, 76.7%, and 94.4% on the three benchmarks, respectively. Real-world evaluation further yields an average success rate of 96.7% across three manipulation tasks. These results highlight the potential of Embodied-Harness to improve robotic manipulation through experience-driven harness self-improvement.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27689v1
- Authors: Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang, Yueting Zhuang
- Published: 2026-11-20T14:55:07Z
- Age days: 3

</details>
