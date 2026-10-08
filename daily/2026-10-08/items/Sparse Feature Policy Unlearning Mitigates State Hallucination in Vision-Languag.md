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
url: "https://arxiv.org/abs/2610.09496v1"
published: "2026-10-07T05:52:02Z"
age_days: 0
score: 36
created: 2026-10-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> SOUL 针对“没抓住却继续搬运”这类状态幻觉，找出与错误和成功分别相关的内部稀疏特征。它训练策略压低前者、强化后者，把修正写进参数，推理时无需反复干预特征。

## 问题

机器人局部动作失败后，仍可能按未实现的状态继续执行，导致错误跨阶段传播。部署检测与恢复主要处理输出；直接让模型忘掉失败样本，又可能破坏失败轨迹中共用的有效技能。[S3](https://arxiv.org/html/2610.09496v1#S1.p2.1) [S10](https://arxiv.org/html/2610.09496v1#S2.SS1.p1.1) [S11](https://arxiv.org/html/2610.09496v1#S2.SS1.p2.1) [S12](https://arxiv.org/html/2610.09496v1#S2.SS2.p1.1)

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放进碗”；夹爪闭合却抓空，旧策略继续搬运。训练阶段用这类轨迹定位并抑制相关特征；输出是修改后的策略动作，至于是否重新抓取，提供材料没有保证。

## 创新点或方法

先把轨迹区分为无幻觉成功、幻觉失败和普通失败，用 SAE 拆解内部激活。遗忘目标不仅要与幻觉相关，还要区别于普通失败、少关联成功；保留目标则关联成功。训练时冻结 SAE，更新 VLA，惩罚遗忘特征激活并增强保留特征；部署使用修改后的策略。[S16](https://arxiv.org/html/2610.09496v1#S3.SS1.p1.2) [S23](https://arxiv.org/html/2610.09496v1#S4.p2.1) [S24](https://arxiv.org/html/2610.09496v1#S4.p3.1) [S25](https://arxiv.org/html/2610.09496v1#S4.E4) [S26](https://arxiv.org/html/2610.09496v1#S4.p3.2) [S27](https://arxiv.org/html/2610.09496v1#S4.E5) [S28](https://arxiv.org/html/2610.09496v1#S4.p3.3)

### 方法如何工作

1. 按实际机器人与物体状态标注三类轨迹，使幻觉失败与普通失败可比较。
2. 用 SAE 分解激活并比较关联，得到候选错误和成功特征。
3. 筛出幻觉特异且少关联成功的遗忘目标，同时建立保留目标，减少误伤。
4. 冻结 SAE 并更新策略参数，让错误特征受抑制、成功特征获强化。
5. 重新执行任务，同时检查幻觉减少与原成功行为保留，验证修正的代价。

### 必要术语

- 状态幻觉：按尚未实现的物理状态行动；本文要修正的持续错误。
- 稀疏自编码器：把密集激活拆成少量活跃特征；用于定位可干预目标。
- 选择性遗忘：训练模型减弱指定内部模式；本文同时设置成功保留目标。

## 证据

对照原策略与梯度上升遗忘：LIBERO-Plus/OpenVLA 幻觉率70%→44%，总成功26%→58%；RoboCasa/π₀.₅ 为40%→22.9%、41.9%→54.3%。梯度上升对照总成功降至0%和4.8%。[S30](https://arxiv.org/html/2610.09496v1#S4.T1.6.1) Franka真机跨两模型共50次执行，无幻觉成功平均增加20个百分点、幻觉失败减少22个百分点。[S43](https://arxiv.org/html/2610.09496v1#S5.SS2.p3.1) 结果支持这些设置下的选择性修正；节选未给仿真样本数与不确定性。

## 局限

注意力分散、特征激活与幻觉的共同出现是关联证据，不能单凭它们确认根因。作者报告保留89%的原成功行为，也意味着并非零损失。[S8](https://arxiv.org/html/2610.09496v1#S1.p4.1) 我的待核查问题是标签可靠性、特征跨任务稳定性，以及未见场景是否仍有效。

- **判断**：值得细读特征选择与行为保留实验，因为它把解释结果变成了训练目标，但需要确认修正没有只适配已知失败。

## 研究关联

可借鉴的是用普通失败作参照，避免把“任何失败都会激活的特征”误当幻觉目标；同时明确保留成功表示，比只压制错误更符合机器人技能相互耦合的现实。

### 下一步读哪里

先读[S23](https://arxiv.org/html/2610.09496v1#S4.p2.1) [S24](https://arxiv.org/html/2610.09496v1#S4.p3.1) [S25](https://arxiv.org/html/2610.09496v1#S4.E4) [S26](https://arxiv.org/html/2610.09496v1#S4.p3.2) [S27](https://arxiv.org/html/2610.09496v1#S4.E5) [S28](https://arxiv.org/html/2610.09496v1#S4.p3.3)确认遗忘和保留目标，再核查区域引导特征的构造与标注标准；结合[S44](https://arxiv.org/html/2610.09496v1#S5.F7)检查同初始条件下的保留与纠正，补查样本数、消融及未见任务结果。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.09496v1
- 获取时间：2026-10-08T01:54:44.438055+00:00
- [S1] [Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models · 正文段落 1](https://arxiv.org/html/2610.09496v1#abstract1.1)
- [S2] [I INTRODUCTION · 正文段落 2](https://arxiv.org/html/2610.09496v1#S1.p1.1)
- [S3] [I INTRODUCTION · 正文段落 3](https://arxiv.org/html/2610.09496v1#S1.p2.1)
- [S4] [I INTRODUCTION · 正文段落 4](https://arxiv.org/html/2610.09496v1#S1.F1.sf1)
- [S5] [I INTRODUCTION · 正文段落 5](https://arxiv.org/html/2610.09496v1#S1.F1.sf2)
- [S6] [I INTRODUCTION · 正文段落 7](https://arxiv.org/html/2610.09496v1#S1.F1)
- [S7] [I INTRODUCTION · 正文段落 8](https://arxiv.org/html/2610.09496v1#S1.p3.1)
- [S8] [I INTRODUCTION · 正文段落 9](https://arxiv.org/html/2610.09496v1#S1.p4.1)
- [S9] [I INTRODUCTION · 正文段落 12](https://arxiv.org/html/2610.09496v1#S1.I1.i3)
- [S10] [II-A Vision-Language-Action Models · 正文段落 13](https://arxiv.org/html/2610.09496v1#S2.SS1.p1.1)
- [S11] [II-A Vision-Language-Action Models · 正文段落 14](https://arxiv.org/html/2610.09496v1#S2.SS1.p2.1)
- [S12] [II-B Machine Unlearning · 正文段落 15](https://arxiv.org/html/2610.09496v1#S2.SS2.p1.1)
- [S13] [II-C Sparse Autoencoders · 正文段落 16](https://arxiv.org/html/2610.09496v1#S2.SS3.p1.1)
- [S14] [II-C Sparse Autoencoders · 正文段落 17](https://arxiv.org/html/2610.09496v1#S2.F2)
- [S15] [II-C Sparse Autoencoders · 正文段落 18](https://arxiv.org/html/2610.09496v1#S2.F2.6.1)
- [S16] [III-A What Is State Hallucination? · 正文段落 27](https://arxiv.org/html/2610.09496v1#S3.SS1.p1.2)
- [S17] [III-B Attention Analysis of Hallucinated and Normal Executions · 正文段落 28](https://arxiv.org/html/2610.09496v1#S3.SS2.p1.1)
- [S18] [III-B Attention Analysis of Hallucinated and Normal Executions · 正文段落 29](https://arxiv.org/html/2610.09496v1#S3.F3.3)
- [S19] [III-B Attention Analysis of Hallucinated and Normal Executions · 正文段落 33](https://arxiv.org/html/2610.09496v1#S3.F3.sf2)
- [S20] [III-B Attention Analysis of Hallucinated and Normal Executions · 正文段落 34](https://arxiv.org/html/2610.09496v1#S3.F3)
- [S21] [III-C Sparse Feature Characterization of State Hallucination · 正文段落 35](https://arxiv.org/html/2610.09496v1#S3.SS3.p1.1)
- [S22] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 47](https://arxiv.org/html/2610.09496v1#S4.p1.1)
- [S23] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 48](https://arxiv.org/html/2610.09496v1#S4.p2.1)
- [S24] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 49](https://arxiv.org/html/2610.09496v1#S4.p3.1)
- [S25] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 50](https://arxiv.org/html/2610.09496v1#S4.E4)
- [S26] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 51](https://arxiv.org/html/2610.09496v1#S4.p3.2)
- [S27] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 52](https://arxiv.org/html/2610.09496v1#S4.E5)
- [S28] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 53](https://arxiv.org/html/2610.09496v1#S4.p3.3)
- [S29] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 54](https://arxiv.org/html/2610.09496v1#S4.T1)
- [S30] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 55](https://arxiv.org/html/2610.09496v1#S4.T1.6.1)
- [S31] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 56](https://arxiv.org/html/2610.09496v1#S4.F5.3)
- [S32] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 57](https://arxiv.org/html/2610.09496v1#S4.F5.4)
- [S33] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 58](https://arxiv.org/html/2610.09496v1#S4.F5.sf1.3)
- [S34] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 59](https://arxiv.org/html/2610.09496v1#S4.F5.sf1)
- [S35] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 60](https://arxiv.org/html/2610.09496v1#S4.F5.sf2.3)
- [S36] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 61](https://arxiv.org/html/2610.09496v1#S4.F5.sf2)
- [S37] [IV Sparse Feature Policy Unlearning (SOUL) · 正文段落 62](https://arxiv.org/html/2610.09496v1#S4.F5)
- [S38] [V-B Main Results · 正文段落 66](https://arxiv.org/html/2610.09496v1#S5.SS2.p1.1)
- [S39] [V-B Main Results · 正文段落 67](https://arxiv.org/html/2610.09496v1#S5.F6.3)
- [S40] [V-B Main Results · 正文段落 68](https://arxiv.org/html/2610.09496v1#S5.F6.4)
- [S41] [V-B Main Results · 正文段落 73](https://arxiv.org/html/2610.09496v1#S5.F6)
- [S42] [V-B Main Results · 正文段落 74](https://arxiv.org/html/2610.09496v1#S5.SS2.p2.1)
- [S43] [V-B Main Results · 正文段落 75](https://arxiv.org/html/2610.09496v1#S5.SS2.p3.1)
- [S44] [V-B Main Results · 正文段落 78](https://arxiv.org/html/2610.09496v1#S5.F7)
- [S45] [V-C Analyses · 正文段落 81](https://arxiv.org/html/2610.09496v1#S5.T2.6.1)
- [S46] [VI Conclusion · 正文段落 86](https://arxiv.org/html/2610.09496v1#S6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Languag.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had been achieved. Our analyses find that state hallucination coincides with weakened attention to task-relevant visual regions, and a mechanistic interpretation via sparse autoencoders reveals that hallucination-associated sparse features are activated when these failures occur. Based on this analysis, we propose SOUL (Sparse feature pOlicy UnLearning), which selectively unlearns policy knowledge associated with state hallucination behaviors, where sparse features identified from hallucination failures and successful behaviors serve as explicit forgetting and retention targets, respectively. Experiments across VLA architectures in simulated and real-world environments show that our method substantially reduces hallucinated failures and improves task success without substantially compromising the existing manipulation capabilities. These results suggest that interpretable feature analysis provides a practical basis for selectively modifying undesirable knowledge in robot policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09496v1
- Authors: Jiho Lee, Jeongeun Park, Heayoun Choi, Taekyung Kim, Eunwoo Kim
- Published: 2026-10-07T05:52:02Z
- Age days: 0

</details>
