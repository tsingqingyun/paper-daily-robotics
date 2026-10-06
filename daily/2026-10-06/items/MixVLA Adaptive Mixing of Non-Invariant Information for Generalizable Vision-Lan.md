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
url: "https://arxiv.org/abs/2610.02898v1"
published: "2026-10-02T06:44:43Z"
age_days: 3
score: 35
created: 2026-10-06
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MixVLA: Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> MixVLA 不把环境易变信息全部丢掉，而用 AMI 在训练时混合这部分特征，削弱策略对特定外观的依赖。再把混合特征与较稳定特征一起用于动作预测，保留可能有用的信息。

## 问题

VLA 在训练场景表现好，换灯光、背景或视角就可能失效，因为任务线索和环境相关性混在一起。扩充数据贵，专门增加几何模块又限制适用范围；只保留不变特征也可能丢掉动作预测所需的补充线索 [S3](https://arxiv.org/html/2610.02898v1#S1.p2.1) [S5](https://arxiv.org/html/2610.02898v1#S1.p3.1)。

### 用一个例子理解

理解用例（非论文实验）：输入“拿红杯子”的画面，训练时保留当前稳定分支，却把易变分支与另一示范混合，再预测原动作；目标是避免只凭某种背景决定抓哪里。实际混合是否改变颜色语义需核查。

## 创新点或方法

先分别训练普通策略和带信息瓶颈约束的策略，后者压缩观测信息但仍需预测动作；再通过权重运算构造补充分支 [S12](https://arxiv.org/html/2610.02898v1#S3.F2) [S15](https://arxiv.org/html/2610.02898v1#S3.SS2.SSS0.Px1.p1.4) [S16](https://arxiv.org/html/2610.02898v1#S3.SS2.SSS0.Px2.p1.1)。第二阶段随机配对批内样本，只混合非不变特征，保持当前样本的不变特征和动作目标，用原动作损失训练 [S17](https://arxiv.org/html/2610.02898v1#S3.SS3.SSS0.Px1.p1.1) [S18](https://arxiv.org/html/2610.02898v1#S3.SS4.SSS0.Px1.p1.1) [S19](https://arxiv.org/html/2610.02898v1#S3.SS4.SSS0.Px2.p1.1) [S20](https://arxiv.org/html/2610.02898v1#S3.E10) [S21](https://arxiv.org/html/2610.02898v1#S3.SS4.SSS0.Px2.p1.2)。所给节选没有完整权重运算式、混合系数规则或推理流程，不能擅自补成直接相减或测试时继续随机混合。

### 方法如何工作

1. 用相同域内数据训练普通分支与信息瓶颈分支，分别取得丰富表示和压缩表示。
2. 通过权重运算构造补充分支，尝试找回压缩时未保留的信息；具体公式未提供。
3. 随机配对样本并混合补充特征，扰动样本特有相关性，同时固定稳定特征。
4. 融合两类特征预测原动作，用行动目标判断混合后哪些信息仍可用；部署步骤需另核查。

### 必要术语

- 信息瓶颈：限制表示保留多少输入信息，同时要求能预测动作；本文用它鼓励稳定线索。
- 非不变信息：会随环境变化的特征；本文认为其中也可能有有用线索。
- AMI：自适应非不变信息混合；本文用它在训练中约束易变特征。

## 证据

用 LIBERO 训练，在 LIBERO-Plus 测未见扰动；还测试 RoboTwin 清洁训练到随机场景，以及真机 [S30](https://arxiv.org/html/2610.02898v1#S4.p6.1)。OpenVLA-OFT 上，LIBERO-Plus 总成功率从 69.6% 到 76.2%，但相机扰动从 56.4% 降至 49.6% [S24](https://arxiv.org/html/2610.02898v1#S4.T1.4.1)；域内从 97.1% 到 96.7% [S32](https://arxiv.org/html/2610.02898v1#S4.SS1.p1.1)。相对仅信息瓶颈，作者报告 LIBERO-Plus 再增 4.0、RoboTwin C2R 再增 2.8 个百分点 [S33](https://arxiv.org/html/2610.02898v1#S4.SS2.p1.1)。真机取面包任务各测十次，灯光扰动下为 60% 对 20%，属初步证据 [S36](https://arxiv.org/html/2610.02898v1#S4.SS3.SSS0.Px2.p1.1) [S37](https://arxiv.org/html/2610.02898v1#S4.SS3.SSS0.Px2.p2.1)。

## 局限

作者明确大视角变化的几何问题不能靠特征混合充分解决 [S41](https://arxiv.org/html/2610.02898v1#A4.SS0.SSS0.Px1.p1.1)。我的待核查问题是权重构造是否真能分离信息，以及混合不同任务特征是否引入错误线索；性能改善本身不能证明得到因果不变表示。“无需额外数据”也不等于免费：两个分支各训练 100K 步 [S31](https://arxiv.org/html/2610.02898v1#S4.p7.1)。

- **判断**：值得读到完整 AMI 公式和部署实现：核心思路有依据，但相机退步与额外训练成本必须一起评估。

## 研究关联

启示是易变信息不等于无用信息：与其强迫策略完全忽略它，可以打乱其稳定对应关系，让模型学会更谨慎地使用。适合外观变化明显、但又不能丢失全部细节的任务。

### 下一步读哪里

先补齐权重构造、AMI 系数和推理路径，再检查拼接表示如何兼容原动作头 [S18](https://arxiv.org/html/2610.02898v1#S3.SS4.SSS0.Px1.p1.1)；重点比较仅信息瓶颈消融 [S33](https://arxiv.org/html/2610.02898v1#S4.SS2.p1.1) 与相机扰动失败 [S41](https://arxiv.org/html/2610.02898v1#A4.SS0.SSS0.Px1.p1.1)，不要只看总分。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.02898v1
- 获取时间：2026-10-06T00:12:10.927257+00:00
- [S1] [MixVLA: Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Language-Action Models · 正文段落 1](https://arxiv.org/html/2610.02898v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.02898v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.02898v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.02898v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.02898v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.02898v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.02898v1#S1.I1.i1)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.02898v1#S1.I1.i3)
- [S9] [2.1 Vision-Language-Action Model · 正文段落 11](https://arxiv.org/html/2610.02898v1#S2.SS1.p1.1)
- [S10] [2.2 Generalization in Robotic Manipulation · 正文段落 12](https://arxiv.org/html/2610.02898v1#S2.SS2.p1.1)
- [S11] [2.2 Generalization in Robotic Manipulation · 正文段落 13](https://arxiv.org/html/2610.02898v1#S2.SS2.p2.1)
- [S12] [3 Method · 正文段落 14](https://arxiv.org/html/2610.02898v1#S3.F2)
- [S13] [VLA policy. · 正文段落 15](https://arxiv.org/html/2610.02898v1#S3.SS1.SSS0.Px1.p1.1)
- [S14] [Invariant and non-invariant factors. · 正文段落 16](https://arxiv.org/html/2610.02898v1#S3.SS1.SSS0.Px2.p1.1)
- [S15] [Invariant Net via Information Bottleneck. · 正文段落 23](https://arxiv.org/html/2610.02898v1#S3.SS2.SSS0.Px1.p1.4)
- [S16] [Non-Invariant Net via Weight Subtraction. · 正文段落 24](https://arxiv.org/html/2610.02898v1#S3.SS2.SSS0.Px2.p1.1)
- [S17] [In-batch Pairing. · 正文段落 30](https://arxiv.org/html/2610.02898v1#S3.SS3.SSS0.Px1.p1.1)
- [S18] [Fusion and Prediction. · 正文段落 39](https://arxiv.org/html/2610.02898v1#S3.SS4.SSS0.Px1.p1.1)
- [S19] [Stage-2 Training Objective. · 正文段落 40](https://arxiv.org/html/2610.02898v1#S3.SS4.SSS0.Px2.p1.1)
- [S20] [Stage-2 Training Objective. · 正文段落 41](https://arxiv.org/html/2610.02898v1#S3.E10)
- [S21] [Stage-2 Training Objective. · 正文段落 42](https://arxiv.org/html/2610.02898v1#S3.SS4.SSS0.Px2.p1.2)
- [S22] [4 Experiment · 正文段落 43](https://arxiv.org/html/2610.02898v1#S4.F3)
- [S23] [4 Experiment · 正文段落 44](https://arxiv.org/html/2610.02898v1#S4.T1)
- [S24] [4 Experiment · 正文段落 45](https://arxiv.org/html/2610.02898v1#S4.T1.4.1)
- [S25] [4 Experiment · 正文段落 46](https://arxiv.org/html/2610.02898v1#S4.p1.1)
- [S26] [4 Experiment · 正文段落 47](https://arxiv.org/html/2610.02898v1#S4.p2.1)
- [S27] [4 Experiment · 正文段落 48](https://arxiv.org/html/2610.02898v1#S4.p3.1)
- [S28] [4 Experiment · 正文段落 49](https://arxiv.org/html/2610.02898v1#S4.p4.1)
- [S29] [4 Experiment · 正文段落 50](https://arxiv.org/html/2610.02898v1#S4.p5.1)
- [S30] [4 Experiment · 正文段落 51](https://arxiv.org/html/2610.02898v1#S4.p6.1)
- [S31] [4 Experiment · 正文段落 52](https://arxiv.org/html/2610.02898v1#S4.p7.1)
- [S32] [4.1 Robustness to Unseen Distribution Shifts · 正文段落 55](https://arxiv.org/html/2610.02898v1#S4.SS1.p1.1)
- [S33] [4.2 Understanding the Role of Non-Invariant Information · 正文段落 62](https://arxiv.org/html/2610.02898v1#S4.SS2.p1.1)
- [S34] [Applicability across policy architectures. · 正文段落 68](https://arxiv.org/html/2610.02898v1#S4.SS3.SSS0.Px1.p1.1)
- [S35] [Applicability across policy architectures. · 正文段落 69](https://arxiv.org/html/2610.02898v1#S4.F5)
- [S36] [Robustness in real-world manipulation. · 正文段落 70](https://arxiv.org/html/2610.02898v1#S4.SS3.SSS0.Px2.p1.1)
- [S37] [Robustness in real-world manipulation. · 正文段落 71](https://arxiv.org/html/2610.02898v1#S4.SS3.SSS0.Px2.p2.1)
- [S38] [5 Conclusion · 正文段落 78](https://arxiv.org/html/2610.02898v1#S5.p1.1)
- [S39] [A.1 Invariant Representation via Information Bottleneck · 正文段落 88](https://arxiv.org/html/2610.02898v1#A1.SS1.p3.1)
- [S40] [A.1 Invariant Representation via Information Bottleneck · 正文段落 90](https://arxiv.org/html/2610.02898v1#A1.SS1.p3.2)
- [S41] [Limitations under Large Geometric Shifts. · 正文段落 180](https://arxiv.org/html/2610.02898v1#A4.SS0.SSS0.Px1.p1.1)
- [S42] [Future Research Directions. · 正文段落 183](https://arxiv.org/html/2610.02898v1#A4.SS0.SSS0.Px2.p3.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/MixVLA Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Lan.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have achieved remarkable advances in robotic manipulation, yet their zero-shot generalization under out-of-distribution (OOD) conditions remains limited. These models often entangle task-relevant invariant structure with environment-specific non-invariant factors, causing policies to rely on spurious appearance cues during action prediction. In this work, we propose \textbf{MixVLA}, a model-agnostic training framework that improves the generalization of VLA models without requiring additional OOD data or architectural modifications. The key component of MixVLA is \textbf{Adaptive Mixing of Non-Invariant Information (AMI)}. AMI stochastically mixes non-invariant representations to regularize distribution-specific variability while preserving complementary predictive cues. The mixed non-invariant features are then fused with invariant representations for final action prediction, resulting in improved robustness without sacrificing policy expressiveness. Extensive experiments across challenging manipulation settings, including LIBERO, LIBERO-Plus, the RoboTwin perturbation suite, and real-world tasks, demonstrate that MixVLA improves overall zero-shot robustness while retaining strong in-domain performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02898v1
- Authors: Pingrui Zhang, Yu Zhang, Pengyuan Wu, Bin Wang, Haoming Song, Xianqiang Gao, ZhaxiZhuoma, Zhigang Wang, Dong Wang, Bin Zhao, Xuelong Li
- Published: 2026-10-02T06:44:43Z
- Age days: 3

</details>
