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
url: "https://arxiv.org/abs/2610.21985v1"
published: "2026-10-15T14:34:44Z"
age_days: 1
score: 39
created: 2026-10-17
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> VeriVLA 在策略拿不准时多生成几段候选动作，再用潜在世界模型预测哪段更能推进任务。它把随机采样变成选择机会，并用触发器控制额外计算。

## 问题

同一画面和指令，流式 VLA 换个随机种子就可能生成质量不同的动作；通常系统直接执行其中一次。插入等精细操作中，选错可能破坏后续状态。仅多采样还不够：需要判断何时值得采，以及怎样在执行前比较候选。

### 用一个例子理解

理解用例（非论文实验）：输入瓶口图像、机器人状态和“插入细棒”→两次采样在接近瓶口时分歧变大→扩充候选并预测各自未来进展→执行预计对准更好的动作，而不是直接采用第一段。

## 创新点或方法

旧做法只执行一次采样，或借 VLM、生成未来图像评分；本文先用两段动作测量段内变化和段间分歧，触发后扩充到候选池。JEPA 验证器预测动作引起的未来特征及任务进展增量，选最高者，无需重建像素。[S14](https://arxiv.org/html/2610.21985v1#S3.F3) [S18](https://arxiv.org/html/2610.21985v1#S3.SS2.p2.1) “免训练”仅指触发器：新环境仍需少量运行校准；验证器则用策略 rollout 和 Robometer 标签训练，测试时做选择。[S20](https://arxiv.org/html/2610.21985v1#S3.SS3.p3.1) [S27](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px2.p1.1)

### 方法如何工作

1. 从同一状态采两段动作并归一化，减少单纯运动速度对触发统计的影响。
2. 把段内变化和段间分歧放到环境校准分布中比较，决定是否投入更多采样。
3. 触发时扩充至10个候选，用动作条件预测器分段推演未来特征，再估计进展增量。[S22](https://arxiv.org/html/2610.21985v1#S3.SS4.SSS0.Px1.p2.1) [S27](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px2.p1.1)
4. 执行最高分候选；未触发时执行第一段样本，避免每步都付完整验证成本。

### 必要术语

- 动作块：一次生成的连续多步动作；本文在候选动作块之间选择。
- 潜在世界模型：预测压缩特征怎样随动作变化；本文用其评估后果。
- JEPA：预测未来表示而非还原像素的学习方式；本文据此减少验证中的图像生成负担。

## 证据

PiperX 真机上插笔、移液、放苹果，每方法每任务50次；平均阶段完成分由基础 π0.5 的50.8%升至65.5%，RoboMonkey 为56.0%，GPC-RANK 为52.8%。这是阶段加权完成分，不是整任务成功率。[S25](https://arxiv.org/html/2610.21985v1#S4.T1.6) [S26](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px1.p1.1) [S27](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px2.p1.1) [S28](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px3.p1.1) [S29](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px4.p1.1) RTX 4090 每次触发增加326毫秒，明确不含触发器延迟。[S30](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px5.p1.1) RoboTwin 五任务始终验证时，成功率在干净环境66.4%→73.6%，干净训练到随机测试62.8%→69.6%；后者不证明触发器也能直接迁移。[S33](https://arxiv.org/html/2610.21985v1#S4.SS2.SSS0.Px1.p1.1) [S34](https://arxiv.org/html/2610.21985v1#S4.T2) [S35](https://arxiv.org/html/2610.21985v1#S4.T2.7)

## 局限

作者指出候选多样性有限：验证器只能选已有候选，不能补出策略根本不会的动作；冻结视觉编码器也可能漏掉细微接触变化。[S43](https://arxiv.org/html/2610.21985v1#S5.p1.1) 高方差与失败的对应是经验相关性，不是危险证明。我的待核查问题是完整平均延迟、触发率及阈值迁移成本，不能把326毫秒视为所有决策的平均开销。

- **判断**：值得读到触发校准、验证器训练和延迟分析；核心吸引力是有选择地花计算，前提是候选池确实包含更好的动作。

## 研究关联

可以借鉴的是把“动作生成得不一致”用作计算分配信号，把“动作是否有用”交给另一个有动力学预测能力的模型判断。当现有策略偶尔能生成好动作、却经常选中坏样本时，这种方法尤其值得尝试。

### 下一步读哪里

查[S19](https://arxiv.org/html/2610.21985v1#S3.SS3.p2.1) [S20](https://arxiv.org/html/2610.21985v1#S3.SS3.p3.1) [S21](https://arxiv.org/html/2610.21985v1#S3.SS4.SSS0.Px1.p1.1) [S22](https://arxiv.org/html/2610.21985v1#S3.SS4.SSS0.Px1.p2.1)的归一化、百分位校准和分段预测；核查进展标签如何产生、验证数据怎样划分。[S42](https://arxiv.org/html/2610.21985v1#S4.T4.7)去掉世界模型后完成分65.5%→55.2%，应结合其训练控制条件判断预测机制贡献。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.21985v1
- 获取时间：2026-10-17T00:17:18.612017+00:00
- [S1] [VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models · 正文段落 1](https://arxiv.org/html/2610.21985v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.21985v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.21985v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.21985v1#S1.F2)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.21985v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.21985v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.21985v1#S1.I1.i1)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.21985v1#S1.I1.i2)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.21985v1#S1.I1.i3)
- [S10] [2 Related Work · 正文段落 12](https://arxiv.org/html/2610.21985v1#S2.SS0.SSS0.Px1.p1.1)
- [S11] [2 Related Work · 正文段落 13](https://arxiv.org/html/2610.21985v1#S2.SS0.SSS0.Px1.p2.1)
- [S12] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.21985v1#S2.SS0.SSS0.Px1.p3.1)
- [S13] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.21985v1#S2.SS0.SSS0.Px2.p1.1)
- [S14] [3 Method · 正文段落 16](https://arxiv.org/html/2610.21985v1#S3.F3)
- [S15] [3.1 Problem Formulation · 正文段落 17](https://arxiv.org/html/2610.21985v1#S3.SS1.p1.1)
- [S16] [3.1 Problem Formulation · 正文段落 19](https://arxiv.org/html/2610.21985v1#S3.SS1.p1.2)
- [S17] [3.2 Overview · 正文段落 25](https://arxiv.org/html/2610.21985v1#S3.SS2.p1.1)
- [S18] [3.2 Overview · 正文段落 26](https://arxiv.org/html/2610.21985v1#S3.SS2.p2.1)
- [S19] [3.3 Two-axis Trigger · 正文段落 30](https://arxiv.org/html/2610.21985v1#S3.SS3.p2.1)
- [S20] [3.3 Two-axis Trigger · 正文段落 35](https://arxiv.org/html/2610.21985v1#S3.SS3.p3.1)
- [S21] [3.4 Latent World Model Verifier · 正文段落 39](https://arxiv.org/html/2610.21985v1#S3.SS4.SSS0.Px1.p1.1)
- [S22] [3.4 Latent World Model Verifier · 正文段落 40](https://arxiv.org/html/2610.21985v1#S3.SS4.SSS0.Px1.p2.1)
- [S23] [4 Experiments · 正文段落 53](https://arxiv.org/html/2610.21985v1#S4.p1.1)
- [S24] [4 Experiments · 正文段落 54](https://arxiv.org/html/2610.21985v1#S4.T1)
- [S25] [4 Experiments · 正文段落 55](https://arxiv.org/html/2610.21985v1#S4.T1.6)
- [S26] [4.1 Real-world Experiments · 正文段落 56](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px1.p1.1)
- [S27] [4.1 Real-world Experiments · 正文段落 57](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px2.p1.1)
- [S28] [4.1 Real-world Experiments · 正文段落 58](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px3.p1.1)
- [S29] [4.1 Real-world Experiments · 正文段落 59](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px4.p1.1)
- [S30] [4.1 Real-world Experiments · 正文段落 60](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px5.p1.1)
- [S31] [4.1 Real-world Experiments · 正文段落 61](https://arxiv.org/html/2610.21985v1#S4.F5)
- [S32] [4.2 Simulation Results · 正文段落 62](https://arxiv.org/html/2610.21985v1#S4.SS2.p1.1)
- [S33] [4.2 Simulation Results · 正文段落 63](https://arxiv.org/html/2610.21985v1#S4.SS2.SSS0.Px1.p1.1)
- [S34] [4.2 Simulation Results · 正文段落 64](https://arxiv.org/html/2610.21985v1#S4.T2)
- [S35] [4.2 Simulation Results · 正文段落 65](https://arxiv.org/html/2610.21985v1#S4.T2.7)
- [S36] [4.2 Simulation Results · 正文段落 66](https://arxiv.org/html/2610.21985v1#S4.F6)
- [S37] [4.2 Simulation Results · 正文段落 67](https://arxiv.org/html/2610.21985v1#S4.SS2.SSS0.Px2.p1.1)
- [S38] [4.2 Simulation Results · 正文段落 68](https://arxiv.org/html/2610.21985v1#S4.T3)
- [S39] [4.2 Simulation Results · 正文段落 69](https://arxiv.org/html/2610.21985v1#S4.T3.7)
- [S40] [4.3.2 Effect of Predictor Pretraining · 正文段落 72](https://arxiv.org/html/2610.21985v1#S4.SS3.SSS2.p1.1)
- [S41] [4.3.2 Effect of Predictor Pretraining · 正文段落 73](https://arxiv.org/html/2610.21985v1#S4.T4)
- [S42] [4.3.2 Effect of Predictor Pretraining · 正文段落 74](https://arxiv.org/html/2610.21985v1#S4.T4.7)
- [S43] [5 Limitations and Future Work · 正文段落 81](https://arxiv.org/html/2610.21985v1#S5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/VeriVLA Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Mo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversibly disrupt task progress and lead to failure. To exploit policy stochasticity, we introduce a training-free two-axis trigger that uses two initial samples to measure within-chunk temporal variation and cross-sample variance, detecting the critical states. Once triggered, a JEPA-based latent world model ranks candidate action chunks by predicting action-conditioned future latent states and the corresponding changes in task progress. By operating in latent space, the verifier avoids pixel reconstruction and enables efficient and more accurate ranking. Across three real-world tasks, $\textit{i.e.,}$ pen insertion, pipetting, and apple placement), our method raises the average completion score from 50.8% to 65.5%, while adding 326 ms for sampling and verification per triggered decision on a single RTX 4090. Consistent gains are also observed in simulation, where the average success rate rises from 66.4% to 73.6% in the clean setting of RoboTwin 2.0, from 62.8% to 69.6% in its randomized setting, and from 96.9% to 97.6% on LIBERO.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21985v1
- Authors: Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, Zhe Liu, Hengshuang Zhao
- Published: 2026-10-15T14:34:44Z
- Age days: 1

</details>
