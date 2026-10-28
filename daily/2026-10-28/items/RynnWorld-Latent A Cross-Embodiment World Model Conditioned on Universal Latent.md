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
url: "https://arxiv.org/abs/2610.36791v1"
published: "2026-10-27T07:54:16Z"
age_days: 0
score: 36
created: 2026-10-28
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RynnWorld-Latent 用视频中提取的潜在动作代替各机器人互不兼容的控制指令，学习“给定这些变化，未来画面怎样发展”。它还把这种可控生成用于制作机器人训练数据。

## 问题

只说“拿起杯子”无法指定何时夹紧、沿哪条轨迹移动；直接输入机器人指令，又会遇到关节数、坐标和控制频率不统一，人类视频还没有机器人指令。[S3](https://arxiv.org/html/2610.36791v1#S1.p1.1) [S4](https://arxiv.org/html/2610.36791v1#S1.p2.1) [S5](https://arxiv.org/html/2610.36791v1#S1.p3.1) [S6](https://arxiv.org/html/2610.36791v1#S1.p4.1) 难点是让异构视频共享细粒度动作条件，而不是只共享任务文字。

### 用一个例子理解

理解用例（非论文实验）：输入人手推盒子的视频；提取运动描述，把首帧人手替换为机器人夹爪，生成相似推盒过程，再配重定向指令；输出候选训练样本，仍须检查画面与指令是否一致。

## 创新点或方法

训练时，冻结RynnLAM，从相邻观察中提取有3D约束的潜在动作；视频骨干既接收全局动作token，也通过局部分支把动作对齐到对应未来视频潜变量。初始帧和动作保持干净，仅训练未来视频去噪。[S7](https://arxiv.org/html/2610.36791v1#S1.p5.1) [S10](https://arxiv.org/html/2610.36791v1#S1.I1.i1) [S17](https://arxiv.org/html/2610.36791v1#S3.SS4.p1.1) [S18](https://arxiv.org/html/2610.36791v1#S3.E5) [S19](https://arxiv.org/html/2610.36791v1#S3.SS4.p1.2) [S20](https://arxiv.org/html/2610.36791v1#S3.E6) [S21](https://arxiv.org/html/2610.36791v1#S3.SS4.p1.3) [S22](https://arxiv.org/html/2610.36791v1#S3.SS4.p2.1) 推理输入初始帧与动作序列生成未来；适配目标机器人后也可接收原生指令。另一条路线编辑源视频首帧，再沿原潜在动作生成新视频，另用重定向和逆运动学配上伪动作标签。[S8](https://arxiv.org/html/2610.36791v1#S1.p6.1) [S35](https://arxiv.org/html/2610.36791v1#S4.SS5.p2.1)

### 方法如何工作

1. 从异构视频提取潜在动作，得到不依赖原生关节定义的共享条件。
2. 把动作全局注入并局部对齐未来帧，训练视频模型按动作预测变化。
3. 在目标机器人上后训练，使模型接入该机器的实际控制指令。
4. 通过数字遥操作或首帧编辑生成视频动作对，过滤后用于策略训练，再以闭环执行检验用途。

### 必要术语

- 潜在动作：从观察变化中推断的紧凑描述；本文作为跨平台生成条件。
- 重定向：把源运动转换成目标机器可表达的动作；本文用它制作伪指令。
- 中训练：在目标任务微调前继续训练；本文用合成数据补充策略经验。

## 证据

预训练覆盖23个数据集、约5.535亿帧。[摘要] 公共基准和两种真机平台的保留示范用于评估视频预测；下游以π0、π0.5为基础，报告LIBERO系列及真机策略相对仅真实示范训练有所改善。[S9](https://arxiv.org/html/2610.36791v1#S1.p7.1) [S24](https://arxiv.org/html/2610.36791v1#S4.SS1.p2.1) [S25](https://arxiv.org/html/2610.36791v1#S4.SS1.p3.1) [S26](https://arxiv.org/html/2610.36791v1#S4.F4) 但输入没有提供预测指标名称、分数和策略增益，无法判断改善幅度。真机每任务35次试验；同首帧更换动作序列的可控性证据主要是定性展示。[S37](https://arxiv.org/html/2610.36791v1#S5.SS0.SSS0.Px1.p1.1)

## 局限

作者明确承认潜在动作可能混入相机和外观变化；生成观察与重定向指令分别产生，过滤不能保证两者物理一致。视频指标和定性跟随也不能证明因果识别；合成中训练同时增加数据和算力，当前比较未分离两者贡献。[S37](https://arxiv.org/html/2610.36791v1#S5.SS0.SSS0.Px1.p1.1)

- **判断**：值得读动作时间对齐与伪标签生成细节；判断价值应以闭环策略收益为主，不能只看生成视频。

## 研究关联

值得借鉴的是把“跨平台共享的运动描述”和“某台机器实际怎样执行”分开：前者吸收无动作标签的视频，后者在目标机器人适配时处理。不过制作训练数据仍需要可靠动作标签，生成画面并没有自动解决这个问题。

### 下一步读哪里

先看[S7](https://arxiv.org/html/2610.36791v1#S1.p5.1) [S21](https://arxiv.org/html/2610.36791v1#S3.SS4.p1.3)理解逐帧条件，再查[S35](https://arxiv.org/html/2610.36791v1#S4.SS5.p2.1)所指的重定向实现；下一步核查预测指标表、真机任务分数、筛选淘汰率，以及相同训练算力下的对照。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.36791v1
- 获取时间：2026-10-28T01:41:10.745034+00:00
- [S1] [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions · 正文段落 1](https://arxiv.org/html/2610.36791v1#abstract1.1)
- [S2] [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions · 正文段落 2](https://arxiv.org/html/2610.36791v1#abstract1.2)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.36791v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.36791v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.36791v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.36791v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.36791v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.36791v1#S1.p6.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.36791v1#S1.p7.1)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.36791v1#S1.I1.i1)
- [S11] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.36791v1#S1.I1.i3)
- [S12] [2.1 World Models · 正文段落 14](https://arxiv.org/html/2610.36791v1#S2.SS1.p1.1)
- [S13] [2.1 World Models · 正文段落 15](https://arxiv.org/html/2610.36791v1#S2.SS1.p2.1)
- [S14] [2.2 Latent Action Learning · 正文段落 16](https://arxiv.org/html/2610.36791v1#S2.SS2.p1.1)
- [S15] [2.2 Latent Action Learning · 正文段落 17](https://arxiv.org/html/2610.36791v1#S2.SS2.p2.1)
- [S16] [3 RynnWorld-Latent · 正文段落 18](https://arxiv.org/html/2610.36791v1#S3.F1)
- [S17] [3.4 Training Objective · 正文段落 36](https://arxiv.org/html/2610.36791v1#S3.SS4.p1.1)
- [S18] [3.4 Training Objective · 正文段落 37](https://arxiv.org/html/2610.36791v1#S3.E5)
- [S19] [3.4 Training Objective · 正文段落 38](https://arxiv.org/html/2610.36791v1#S3.SS4.p1.2)
- [S20] [3.4 Training Objective · 正文段落 39](https://arxiv.org/html/2610.36791v1#S3.E6)
- [S21] [3.4 Training Objective · 正文段落 40](https://arxiv.org/html/2610.36791v1#S3.SS4.p1.3)
- [S22] [3.4 Training Objective · 正文段落 41](https://arxiv.org/html/2610.36791v1#S3.SS4.p2.1)
- [S23] [4.1 Experimental Setup · 正文段落 54](https://arxiv.org/html/2610.36791v1#S4.SS1.p1.1)
- [S24] [4.1 Experimental Setup · 正文段落 55](https://arxiv.org/html/2610.36791v1#S4.SS1.p2.1)
- [S25] [4.1 Experimental Setup · 正文段落 56](https://arxiv.org/html/2610.36791v1#S4.SS1.p3.1)
- [S26] [4.1 Experimental Setup · 正文段落 57](https://arxiv.org/html/2610.36791v1#S4.F4)
- [S27] [4.1 Experimental Setup · 正文段落 58](https://arxiv.org/html/2610.36791v1#S4.I1.i1)
- [S28] [4.1 Experimental Setup · 正文段落 59](https://arxiv.org/html/2610.36791v1#S4.I1.i2)
- [S29] [4.1 Experimental Setup · 正文段落 60](https://arxiv.org/html/2610.36791v1#S4.SS1.p5.1)
- [S30] [4.1 Experimental Setup · 正文段落 61](https://arxiv.org/html/2610.36791v1#S4.SS1.p6.1)
- [S31] [4.1 Experimental Setup · 正文段落 62](https://arxiv.org/html/2610.36791v1#S4.I2.i1)
- [S32] [4.1 Experimental Setup · 正文段落 63](https://arxiv.org/html/2610.36791v1#S4.I2.i2)
- [S33] [4.1 Experimental Setup · 正文段落 64](https://arxiv.org/html/2610.36791v1#S4.SS1.p7.1)
- [S34] [4.5 Scalable Data Editing and Synthesis for Policy Learning · 正文段落 87](https://arxiv.org/html/2610.36791v1#S4.SS5.p1.1)
- [S35] [4.5 Scalable Data Editing and Synthesis for Policy Learning · 正文段落 88](https://arxiv.org/html/2610.36791v1#S4.SS5.p2.1)
- [S36] [4.5 Scalable Data Editing and Synthesis for Policy Learning · 正文段落 89](https://arxiv.org/html/2610.36791v1#S4.SS5.p3.1)
- [S37] [Limitations. · 正文段落 103](https://arxiv.org/html/2610.36791v1#S5.SS0.SSS0.Px1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/RynnWorld-Latent A Cross-Embodiment World Model Conditioned on Universal Latent.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface. This representation enables joint pretraining on human interaction videos, robot demonstrations, and simulation rollouts without requiring a common native action space. Built on a pretrained video transformer, RynnWorld-Latent combines global action tokens with an identity-initialized local pathway that aligns actions with future video latents. We pretrain on 23 datasets comprising approximately 553.5M frames and adapt the model to target robots through post-training. The framework supports two data-generation routes: digital teleoperation uses target robot commands to generate action-video demonstrations, while latent-action synthesis transfers source motion to an edited initial frame and pairs the resulting rollout with retargeted pseudo robot actions. Experiments show improved video prediction metrics on public benchmarks and two real-robot platforms, alongside qualitative action following when different action sequences share the same initial observation. Synthetic mid-training improves policy success rates on LIBERO and LIBERO-Plus, and both generation routes improve real-world policy success rates over real-demonstration-only training in the evaluated settings. These results support universal latent actions as a scalable interface for learning controllable visual dynamics across heterogeneous embodiments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36791v1
- Authors: Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li
- Published: 2026-10-27T07:54:16Z
- Age days: 0

</details>
