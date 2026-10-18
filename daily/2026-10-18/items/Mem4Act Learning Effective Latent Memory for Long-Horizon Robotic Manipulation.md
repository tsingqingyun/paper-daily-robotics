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
url: "https://arxiv.org/abs/2610.22323v1"
published: "2026-10-15T17:51:58Z"
age_days: 2
score: 28
created: 2026-10-18
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Mem4Act: Learning Effective Latent Memory for Long-Horizon Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Mem4Act 把历史压成固定大小的潜在记忆，让机器人在关键信息被遮住后仍能行动。它不仅训练“怎样压缩”，还用历史问答和视觉特征重建训练“该记什么”，再让动作策略学习使用这些记忆。

## 问题

任务要求记住早先看到的颜色、位置或操作顺序。直接输入全部历史会让上下文越来越长；抽帧、压缩或语言总结可能漏掉以后才有用的细节。更隐蔽的问题是，许多即时动作无需记忆，只用动作损失训练时，策略可能一直忽略历史 [S2](https://arxiv.org/html/2610.22323v1#S1.p1.1) [S3](https://arxiv.org/html/2610.22323v1#S1.p2.1) [S4](https://arxiv.org/html/2610.22323v1#S1.F1) [S5](https://arxiv.org/html/2610.22323v1#S1.p3.1)。

### 用一个例子理解

理解用例（非论文实验）：先看到红蓝方块分别被不透明杯盖住 → 编码器保留颜色与位置的历史证据 → 收到“拿出红色方块”后，策略结合当前杯子位置选择正确杯子，无需当前画面再次显示颜色。

## 创新点或方法

本文先让记忆槽在较细时间窗口内读取历史，再跨更大窗口整合，减少只关注相似时段的问题。训练先用历史 QA 和多个关键帧的 DINO 特征重建建立记忆，再联合训练记忆与动作；记忆通过交叉注意力调节动作专家特征。推理时从保留历史构建记忆，结合当前观察和指令生成动作块，不需要现场回答问题或重建图像 [S10](https://arxiv.org/html/2610.22323v1#S2.p3.1) [S11](https://arxiv.org/html/2610.22323v1#S2.F2) [S12](https://arxiv.org/html/2610.22323v1#S3.SS1.p1.1) [S13](https://arxiv.org/html/2610.22323v1#S3.SS1.p1.2) [S14](https://arxiv.org/html/2610.22323v1#S3.SS1.p2.1) [S15](https://arxiv.org/html/2610.22323v1#S3.SS2.p1.1) [S16](https://arxiv.org/html/2610.22323v1#S3.SS3.p2.1) [S17](https://arxiv.org/html/2610.22323v1#S3.SS3.p3.1) [S18](https://arxiv.org/html/2610.22323v1#S3.SS3.p4.1) [S19](https://arxiv.org/html/2610.22323v1#S3.SS4.p1.1)。

### 方法如何工作

1. 把历史画面压成视觉 token，加入本体状态和时间信息，使事件可被区分。
2. 先分时间窗口汇总，再扩大整合范围，得到固定大小记忆。
3. 先训练记忆回答历史问题并重建关键帧特征，让它保存语义与视觉证据。
4. 联合训练动作策略读取并利用记忆；推理时用新历史更新记忆并生成后续动作。

### 必要术语

- 潜在记忆：学习得到的向量集合；承载历史信息而非直接展示旧画面。
- 多粒度时间聚合：先看局部时段再汇总更长时间；帮助有限容量覆盖历史。
- DINO特征重建：从记忆恢复视觉编码器的特征；监督视觉结构而非逐像素复原。
- 记忆优先训练：先把记忆学好，再联合学动作；减少策略从一开始就忽略历史的机会。

## 证据

RoboMME 的16项仿真任务各50次，成功率49.88%，比最强 FrameSamp+Modul 高5.37个百分点 [S34](https://arxiv.org/html/2610.22323v1#S4.SS2.p1.1)。RMBench 九项任务各100次，单一共享策略达61.0%，NativeMEM为48.7%；需多次历史观察的任务上分别为41.3%和14.8% [S35](https://arxiv.org/html/2610.22323v1#S4.SS2.p2.1) [S36](https://arxiv.org/html/2610.22323v1#S4.T2) [S37](https://arxiv.org/html/2610.22323v1#S4.T2.4.1)。四项 YAM 双臂真机任务各50次，摘要报告平均81.5%；节选未给真机对照表数值 [S1](https://arxiv.org/html/2610.22323v1#abstract1.1) [S33](https://arxiv.org/html/2610.22323v1#S4.SS1.p5.1) [S39](https://arxiv.org/html/2610.22323v1#S4.T3)。这些结果支持所测记忆任务的收益，但总体分数不能单独证明每项设计各自的作用。

## 局限

固定的是提供给动作策略的512个记忆 token，不代表历史存储和编码成本永远固定；实现仍保留并采样历史帧 [S7](https://arxiv.org/html/2610.22323v1#S1.p5.1) [S10](https://arxiv.org/html/2610.22323v1#S2.p3.1) [S32](https://arxiv.org/html/2610.22323v1#S4.SS1.p4.1)。我的待核查问题是更长流程的遗忘、QA标注成本，以及细粒度视觉信息是否被采样跳过。RMBench 的 Observe 任务为22%，低于 NativeMEM 的44%，也说明收益并非逐项成立 [S37](https://arxiv.org/html/2610.22323v1#S4.T2.4.1)。

- **判断**：值得深入方法与消融：它把“记住”和“用上”分开训练，证据覆盖面较清楚，但要核算完整历史处理成本。

## 研究关联

最值得借鉴的是先把记忆训练成有用的信息载体，再要求策略依赖它。若当前动作无法区分两段历史，而后续决策需要区分，额外监督历史事实和视觉证据能补上动作损失缺少的信号。

### 下一步读哪里

先对照 [S10](https://arxiv.org/html/2610.22323v1#S2.p3.1) [S11](https://arxiv.org/html/2610.22323v1#S2.F2) [S12](https://arxiv.org/html/2610.22323v1#S3.SS1.p1.1) [S13](https://arxiv.org/html/2610.22323v1#S3.SS1.p1.2) [S14](https://arxiv.org/html/2610.22323v1#S3.SS1.p2.1) [S15](https://arxiv.org/html/2610.22323v1#S3.SS2.p1.1) [S16](https://arxiv.org/html/2610.22323v1#S3.SS3.p2.1) [S17](https://arxiv.org/html/2610.22323v1#S3.SS3.p3.1) [S18](https://arxiv.org/html/2610.22323v1#S3.SS3.p4.1) 检查时间窗口、QA生成和关键帧选择，再核查分阶段训练是否在相同总预算下改善记忆使用；结合 [S32](https://arxiv.org/html/2610.22323v1#S4.SS1.p4.1) 查看历史上限，并寻找编码耗时、删记忆和错记忆干预结果。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.22323v1
- 获取时间：2026-10-18T03:39:27.587784+00:00
- [S1] [Mem4Act: Learning Effective Latent Memory for Long-Horizon Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2610.22323v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.22323v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.22323v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.22323v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.22323v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.22323v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.22323v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.22323v1#S1.I1.i3)
- [S9] [2 Related Work · 正文段落 11](https://arxiv.org/html/2610.22323v1#S2.p1.1)
- [S10] [2 Related Work · 正文段落 13](https://arxiv.org/html/2610.22323v1#S2.p3.1)
- [S11] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.22323v1#S2.F2)
- [S12] [3.1 Problem Formulation · 正文段落 15](https://arxiv.org/html/2610.22323v1#S3.SS1.p1.1)
- [S13] [3.1 Problem Formulation · 正文段落 17](https://arxiv.org/html/2610.22323v1#S3.SS1.p1.2)
- [S14] [3.1 Problem Formulation · 正文段落 18](https://arxiv.org/html/2610.22323v1#S3.SS1.p2.1)
- [S15] [3.2 Structured Memory Formation · 正文段落 19](https://arxiv.org/html/2610.22323v1#S3.SS2.p1.1)
- [S16] [3.3 Memory-Specific Supervision · 正文段落 27](https://arxiv.org/html/2610.22323v1#S3.SS3.p2.1)
- [S17] [3.3 Memory-Specific Supervision · 正文段落 28](https://arxiv.org/html/2610.22323v1#S3.SS3.p3.1)
- [S18] [3.3 Memory-Specific Supervision · 正文段落 31](https://arxiv.org/html/2610.22323v1#S3.SS3.p4.1)
- [S19] [3.4 Memory-Conditioned Action Policy · 正文段落 37](https://arxiv.org/html/2610.22323v1#S3.SS4.p1.1)
- [S20] [3.4 Memory-Conditioned Action Policy · 正文段落 38](https://arxiv.org/html/2610.22323v1#S3.E7)
- [S21] [3.4 Memory-Conditioned Action Policy · 正文段落 39](https://arxiv.org/html/2610.22323v1#S3.SS4.p1.2)
- [S22] [3.4 Memory-Conditioned Action Policy · 正文段落 40](https://arxiv.org/html/2610.22323v1#S3.SS4.p2.1)
- [S23] [3.4 Memory-Conditioned Action Policy · 正文段落 41](https://arxiv.org/html/2610.22323v1#S3.E8)
- [S24] [3.4 Memory-Conditioned Action Policy · 正文段落 42](https://arxiv.org/html/2610.22323v1#S3.SS4.p2.2)
- [S25] [3.4 Memory-Conditioned Action Policy · 正文段落 43](https://arxiv.org/html/2610.22323v1#S3.SS4.p3.1)
- [S26] [3.4 Memory-Conditioned Action Policy · 正文段落 44](https://arxiv.org/html/2610.22323v1#S3.E9)
- [S27] [3.4 Memory-Conditioned Action Policy · 正文段落 45](https://arxiv.org/html/2610.22323v1#S3.SS4.p3.2)
- [S28] [4.1 Experimental Setup · 正文段落 49](https://arxiv.org/html/2610.22323v1#S4.SS1.p1.1)
- [S29] [4.1 Experimental Setup · 正文段落 50](https://arxiv.org/html/2610.22323v1#S4.SS1.p2.1)
- [S30] [4.1 Experimental Setup · 正文段落 51](https://arxiv.org/html/2610.22323v1#S4.SS1.p3.1)
- [S31] [4.1 Experimental Setup · 正文段落 52](https://arxiv.org/html/2610.22323v1#S4.F3)
- [S32] [4.1 Experimental Setup · 正文段落 53](https://arxiv.org/html/2610.22323v1#S4.SS1.p4.1)
- [S33] [4.1 Experimental Setup · 正文段落 54](https://arxiv.org/html/2610.22323v1#S4.SS1.p5.1)
- [S34] [4.2 Main Results · 正文段落 55](https://arxiv.org/html/2610.22323v1#S4.SS2.p1.1)
- [S35] [4.2 Main Results · 正文段落 58](https://arxiv.org/html/2610.22323v1#S4.SS2.p2.1)
- [S36] [4.2 Main Results · 正文段落 59](https://arxiv.org/html/2610.22323v1#S4.T2)
- [S37] [4.2 Main Results · 正文段落 60](https://arxiv.org/html/2610.22323v1#S4.T2.4.1)
- [S38] [4.2 Main Results · 正文段落 61](https://arxiv.org/html/2610.22323v1#S4.F4)
- [S39] [4.2 Main Results · 正文段落 63](https://arxiv.org/html/2610.22323v1#S4.T3)
- [S40] [C.4 Real-world Baselines · 正文段落 144](https://arxiv.org/html/2610.22323v1#A3.SS4.p5.2)
- [S41] [D.2 Real-world Inference Efficiency · 正文段落 154](https://arxiv.org/html/2610.22323v1#A4.SS2.p2.1)
- [S42] [D.3 Real-World Failure Analysis · 正文段落 172](https://arxiv.org/html/2610.22323v1#A4.SS3.p6.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/Mem4Act Learning Effective Latent Memory for Long-Horizon Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon robotic manipulation fundamentally requires memory: agents must retain task-relevant information from past observations and interactions and use it to guide future actions. Existing approaches typically preserve raw historical observations, compressed visual tokens, or language summaries, but these representations either expose the action policy to increasingly long histories or risk discarding task-relevant temporal, semantic, and perceptual information. We introduce Mem4Act, a framework for learning effective latent memory as a fixed-size representation explicitly optimized for long-horizon robotic control. Mem4Act addresses three coupled challenges: how to efficiently cover long histories, what information memory should retain, and how to ensure the policy actually relies on memory. To this end, it organizes history via multi-granularity temporal aggregation, preserves complementary semantic and perceptual information through question-answering supervision and key-frame DINO feature reconstruction, and employs memory-first two-stage training to encourage greater use of memory by the action policy. The resulting memory captures both high-level task state and fine-grained perceptual evidence while providing a bounded interface to the action policy. Across RoboMME, RMBench, and four real-world manipulation tasks, Mem4Act achieves state-of-the-art performance on memory-dependent control, with success rates of 49.88%, 61.0%, and 81.5%, respectively. Extensive ablations further demonstrate the importance of temporal aggregation, complementary memory supervision, and memory-first training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22323v1
- Authors: Yun Zhang, Zhiyu Huang, Tianhui Cai, Chen Tang, Wei Wang, Jiaqi Ma
- Published: 2026-10-15T17:51:58Z
- Age days: 2

</details>
