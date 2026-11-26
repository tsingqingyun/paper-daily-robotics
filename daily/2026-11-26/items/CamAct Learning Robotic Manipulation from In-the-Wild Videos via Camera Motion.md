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
url: "https://arxiv.org/abs/2611.34257v1"
published: "2026-11-25T12:19:59Z"
age_days: 0
score: 38
created: 2026-11-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> CamAct 让机器人策略从普通走路视频里学视角怎样随运动变化。它把离线恢复的相机位移和转向放进独立的动作维度，与真实机器人动作共用网络训练。

## 问题

机械臂需要从图像和指令预测接下来的动作，但真机示范采集贵，还受机器人硬件约束。以往借用第一人称视频时，通常要找人确实在摆弄物体的片段。CamAct 问的是，只有街景或室内走动的视频，能否提供与腕部视角变化有关的训练信号。[S3](https://arxiv.org/html/2611.34257v1#S1.p1.1) [S4](https://arxiv.org/html/2611.34257v1#S1.p2.1) [S5](https://arxiv.org/html/2611.34257v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）——输入一帧走廊视频，离线轨迹给出随后几步的前移和转向，只训练相机运动输出。另一条样本输入机械臂腕部画面和“把方块放进碗里”，只用录到的真实动作训练控制输出。上机时使用后者对应的输出控制机械臂。

## 创新点或方法

通常从人的操作中找动作标签，CamAct 改为跟踪拍摄者的相机，把轨迹切成以每一步当前朝向为基准的前移、左移和转向。走路帧配空指令，机器人样本配任务指令，两者共用 StarVLA 的视觉语言主干和流匹配动作头。输出把机器人控制维度和相机运动维度拼接起来，每条样本只给自己有标签的维度算损失。这样，视频能更新共享参数，机器人示范仍负责教实际控制。部署时输入机器人视图和任务指令，使用输出中的机器人动作部分。[S15](https://arxiv.org/html/2611.34257v1#S3.SS1.p1.1) [S16](https://arxiv.org/html/2611.34257v1#S3.SS1.p1.2) [S17](https://arxiv.org/html/2611.34257v1#S3.SS1.p2.1) [S18](https://arxiv.org/html/2611.34257v1#S3.SS2.SSS0.Px1.p1.1) [S19](https://arxiv.org/html/2611.34257v1#S3.SS2.SSS0.Px3.p2.2) [S20](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px1.p1.1) [S21](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px2.p2.2)[S24](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p1.1) [S25](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p2.1) [S26](https://arxiv.org/html/2611.34257v1#S3.E4) [S27](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p3.1) [S28](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px1.p1.1)

### 方法如何工作

1. 离线恢复走路视频的相机轨迹，从原本无机器人标签的帧里提取运动目标。
2. 用每一步自身朝向表达局部位移和转角，让样本摆脱拍摄起点与全局朝向的影响。
3. 把视频和机器人样本交给同一网络，各自只在有标签的输出维度计算误差。
4. 上机用当前机器人图像和指令生成动作块，取机器人控制维度执行。

### 必要术语

- 伪动作：从视频估算出来的运动标签；这里指相机的平面位移与转向。
- 损失掩码：指定哪些输出计入训练误差；本文用它让两类样本监督各自有标签的维度。
- 流匹配：学习把噪声逐步变成连续输出；这里用于生成一段未来动作。

## 证据

与同更新步数的纯机器人 StarVLA-GR00T 对比，仿真每任务跑 50 次，LIBERO 总成功率从 96.40% 到 98.10%，RoboCasa 365 从 22.96% 到 29.32%。LIBERO-Plus 零样本从 71.90% 到 74.49%。真机 Franka 的四项任务各用 50 条示范单独微调，再各跑 16 次，平均成功率从 54.69% 到 68.75%。真机结果支持整套联合训练流程在这些任务上的收益。[S23](https://arxiv.org/html/2611.34257v1#S3.T1.5)[S28](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px1.p1.1) [S29](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px2.p1.1) [S30](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p1.1) [S31](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p2.1) [S32](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p3.1) [S33](https://arxiv.org/html/2611.34257v1#S4.T2) [S34](https://arxiv.org/html/2611.34257v1#S4.T2.5) [S35](https://arxiv.org/html/2611.34257v1#S4.SS2.SSS0.Px1.p1.1)[S38](https://arxiv.org/html/2611.34257v1#S4.SS2.SSS0.Px2.p1.1)[S47](https://arxiv.org/html/2611.34257v1#A1.SS3.p1.1)

## 局限

作者发现 LIBERO 仅用腕部相机时提升 2.10 个百分点，仅用外部相机时下降 1.90 个百分点，收益取决于观察视角。RoboCasa 的去运动和空白图像消融支持两类信号都有用，具体学到了什么空间表征仍待验证。真机两组从各自的 LIBERO 检查点开始，CamAct 又在真机微调时继续混入视频，我会查两个阶段各自贡献多少。[S41](https://arxiv.org/html/2611.34257v1#S4.SS3.SSS0.Px1.p2.1)[S44](https://arxiv.org/html/2611.34257v1#S4.T4.5) [S45](https://arxiv.org/html/2611.34257v1#S4.SS3.SSS0.Px2.p2.1)[S47](https://arxiv.org/html/2611.34257v1#A1.SS3.p1.1)

- **判断**：值得读到损失掩码和相机视角消融，直接看动作空间不同的数据怎样共训，以及什么配置下会出现负收益。

## 研究关联

设计辅助任务时，可以先找两类数据共有的可预测变化。走路和抓放都可能让相机相对场景移动，于是能让整个网络学习这种变化，同时把具体的夹爪控制交给有机器人标签的样本。

### 下一步读哪里

结合 [S19](https://arxiv.org/html/2611.34257v1#S3.SS2.SSS0.Px3.p2.2) [S20](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px1.p1.1) [S21](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px2.p2.2) [S22](https://arxiv.org/html/2611.34257v1#S3.T1) [S23](https://arxiv.org/html/2611.34257v1#S3.T1.5) [S24](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p1.1) [S25](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p2.1) [S26](https://arxiv.org/html/2611.34257v1#S3.E4) [S27](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p3.1) [S28](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px1.p1.1) 查相机轨迹如何定尺度、怎样过滤不可靠片段，以及采样比例变化时收益是否稳定。[S49](https://arxiv.org/html/2611.34257v1#A2.p1.1) [S50](https://arxiv.org/html/2611.34257v1#A2.T6) 指向直接对齐动作维度和冻结主干的补充消融，所给节选只有表题。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34257v1
- 获取时间：2026-11-26T03:57:02.593358+00:00
- [S1] [CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion · 正文段落 1](https://arxiv.org/html/2611.34257v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.34257v1#S1.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.34257v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.34257v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.34257v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.34257v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.34257v1#S1.I1.i2)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.34257v1#S1.I1.i3)
- [S9] [2.1 Vision-Language-Action Models · 正文段落 11](https://arxiv.org/html/2611.34257v1#S2.SS1.p1.1)
- [S10] [2.1 Vision-Language-Action Models · 正文段落 12](https://arxiv.org/html/2611.34257v1#S2.SS1.p2.1)
- [S11] [2.2 Learning Robotic Manipulation from Videos · 正文段落 13](https://arxiv.org/html/2611.34257v1#S2.SS2.p1.1)
- [S12] [2.2 Learning Robotic Manipulation from Videos · 正文段落 14](https://arxiv.org/html/2611.34257v1#S2.SS2.p2.1)
- [S13] [3 Methodology · 正文段落 15](https://arxiv.org/html/2611.34257v1#S3.p1.1)
- [S14] [3 Methodology · 正文段落 16](https://arxiv.org/html/2611.34257v1#S3.F2)
- [S15] [3.1 Problem Formulation · 正文段落 17](https://arxiv.org/html/2611.34257v1#S3.SS1.p1.1)
- [S16] [3.1 Problem Formulation · 正文段落 19](https://arxiv.org/html/2611.34257v1#S3.SS1.p1.2)
- [S17] [3.1 Problem Formulation · 正文段落 20](https://arxiv.org/html/2611.34257v1#S3.SS1.p2.1)
- [S18] [Video Data. · 正文段落 21](https://arxiv.org/html/2611.34257v1#S3.SS2.SSS0.Px1.p1.1)
- [S19] [Constructing Pseudo-Actions. · 正文段落 26](https://arxiv.org/html/2611.34257v1#S3.SS2.SSS0.Px3.p2.2)
- [S20] [Policy Architecture. · 正文段落 28](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px1.p1.1)
- [S21] [Action Representation. · 正文段落 32](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px2.p2.2)
- [S22] [Action Representation. · 正文段落 33](https://arxiv.org/html/2611.34257v1#S3.T1)
- [S23] [Action Representation. · 正文段落 34](https://arxiv.org/html/2611.34257v1#S3.T1.5)
- [S24] [Joint Training. · 正文段落 35](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p1.1)
- [S25] [Joint Training. · 正文段落 36](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p2.1)
- [S26] [Joint Training. · 正文段落 37](https://arxiv.org/html/2611.34257v1#S3.E4)
- [S27] [Joint Training. · 正文段落 39](https://arxiv.org/html/2611.34257v1#S3.SS3.SSS0.Px3.p3.1)
- [S28] [Experimental Setup. · 正文段落 43](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px1.p1.1)
- [S29] [Benchmarks and Evaluation. · 正文段落 44](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px2.p1.1)
- [S30] [Main Results. · 正文段落 45](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p1.1)
- [S31] [Main Results. · 正文段落 46](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p2.1)
- [S32] [Main Results. · 正文段落 47](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p3.1)
- [S33] [Main Results. · 正文段落 48](https://arxiv.org/html/2611.34257v1#S4.T2)
- [S34] [Main Results. · 正文段落 49](https://arxiv.org/html/2611.34257v1#S4.T2.5)
- [S35] [Experimental Setup. · 正文段落 50](https://arxiv.org/html/2611.34257v1#S4.SS2.SSS0.Px1.p1.1)
- [S36] [Experimental Setup. · 正文段落 51](https://arxiv.org/html/2611.34257v1#S4.F3)
- [S37] [Experimental Setup. · 正文段落 52](https://arxiv.org/html/2611.34257v1#S4.F4)
- [S38] [Results. · 正文段落 53](https://arxiv.org/html/2611.34257v1#S4.SS2.SSS0.Px2.p1.1)
- [S39] [4.3 Ablation Studies · 正文段落 54](https://arxiv.org/html/2611.34257v1#S4.SS3.p1.1)
- [S40] [Effect of Observation Views. · 正文段落 55](https://arxiv.org/html/2611.34257v1#S4.SS3.SSS0.Px1.p1.1)
- [S41] [Effect of Observation Views. · 正文段落 56](https://arxiv.org/html/2611.34257v1#S4.SS3.SSS0.Px1.p2.1)
- [S42] [Effect of Observation Views. · 正文段落 57](https://arxiv.org/html/2611.34257v1#S4.T3)
- [S43] [Effect of Video Supervision. · 正文段落 60](https://arxiv.org/html/2611.34257v1#S4.T4)
- [S44] [Effect of Video Supervision. · 正文段落 61](https://arxiv.org/html/2611.34257v1#S4.T4.5)
- [S45] [Effect of Video Supervision. · 正文段落 62](https://arxiv.org/html/2611.34257v1#S4.SS3.SSS0.Px2.p2.1)
- [S46] [5 Conclusion · 正文段落 74](https://arxiv.org/html/2611.34257v1#S5.p1.1)
- [S47] [A.3 Real-World Experimental Setup · 正文段落 83](https://arxiv.org/html/2611.34257v1#A1.SS3.p1.1)
- [S48] [A.3 Real-World Experimental Setup · 正文段落 84](https://arxiv.org/html/2611.34257v1#A1.SS3.p2.1)
- [S49] [Appendix B Additional Ablation Results · 正文段落 85](https://arxiv.org/html/2611.34257v1#A2.p1.1)
- [S50] [Appendix B Additional Ablation Results · 正文段落 86](https://arxiv.org/html/2611.34257v1#A2.T6)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/CamAct Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models benefit from large, diverse datasets for robotic manipulation, yet collecting robot demonstrations remains costly. Recent work has explored egocentric videos as a source of supervision, primarily drawing on demonstrations of human-object interaction. We show that in-the-wild videos can improve robotic manipulation even when they contain no demonstrations of object manipulation. Specifically, camera motion recovered from these videos provides an additional source of motion supervision that complements robot demonstrations. Building on this finding, we introduce CamAct, which incorporates this camera-motion supervision into VLA policies alongside robot demonstrations, extending the use of human videos for manipulation learning beyond object interactions. Experiments show that incorporating this video supervision during fine-tuning improves success rates from 96.40% to 98.10% on LIBERO and from 22.96% to 29.32% on RoboCasa 365. The resulting policy also demonstrates strong results in out-of-distribution generalization on LIBERO-Plus and real-world manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34257v1
- Authors: Haoming Gu, Yunpeng Qing, Zhi Hou, Weinan Zhang
- Published: 2026-11-25T12:19:59Z
- Age days: 0

</details>
