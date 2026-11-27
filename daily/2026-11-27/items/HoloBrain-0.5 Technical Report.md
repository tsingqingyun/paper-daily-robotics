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
url: "https://arxiv.org/abs/2611.34449v1"
published: "2026-11-25T14:28:05Z"
age_days: 1
score: 39
created: 2026-11-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# HoloBrain-0.5 Technical Report

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> HoloBrain-0.5 先统一各机器人关节和工具坐标的写法，再让策略看着机身结构和标定相机生成动作。离散版在预训练仿真中学得更快，连续版在报告的真机后训练设置中表现更好。

## 问题

不同机器人的演示数据可能有不同关节数、机械连接、相机位置和坐标习惯。训练数据里同一个数值可能对应不同的物理动作，跨机器合训时，模型得同时学习任务和这些约定。HoloBrain-0 已用关节和正运动学提供几何线索，这版进一步统一坐标约定，并把机身结构显式交给策略 [S5](https://arxiv.org/html/2611.34449v1#S1.p2.1)[S15](https://arxiv.org/html/2611.34449v1#S3.p1.1) [S16](https://arxiv.org/html/2611.34449v1#S3.E1) [S17](https://arxiv.org/html/2611.34449v1#S3.p1.2) [S18](https://arxiv.org/html/2611.34449v1#S3.F2) [S19](https://arxiv.org/html/2611.34449v1#S3.SS1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）。两台机械臂都接到“把积木放入盒中”的指令，一台的腕关节原来绕局部 x 轴记账。先把两台机器的关节和工具坐标改成统一约定，再输入各自的关节图、状态和相机画面。策略据此为各台机器输出一段抓取和放置轨迹。

## 创新点或方法

先重写机器人描述，让旋转与平移关节按各自局部正 z 轴表示，并约定工具中心坐标的朝向。补偿挂接变换，让同一关节轨迹仍对应原来的实际运动。策略接收规范化的关节图、机器人状态、指令和标定后的相机观测。训练时，连续版学习把噪声逐步去成动作块，离散版先把动作压成由粗到细的编号，再学习按延迟顺序预测编号。推理时两条路线分别去噪或解码，输出连续动作轨迹。D-Init. 另复用离散版共享参数，再接扩散动作头训练 [S6](https://arxiv.org/html/2611.34449v1#S1.F1) [S7](https://arxiv.org/html/2611.34449v1#S1.p3.1) [S8](https://arxiv.org/html/2611.34449v1#S1.p4.1)[S18](https://arxiv.org/html/2611.34449v1#S3.F2)[S22](https://arxiv.org/html/2611.34449v1#S3.SS3.p4.1) [S23](https://arxiv.org/html/2611.34449v1#S3.SS3.p10.1)[S28](https://arxiv.org/html/2611.34449v1#S4.SS1.p3.1)。

### 方法如何工作

1. 统一关节和工具中心坐标，用补偿变换保留原始物理几何与运动。
2. 将机身关节图、当前状态及有标定参数的相机观测一同输入，让策略知道动作将由哪种机械结构执行。
3. 用异构示范训练动作生成器，连续版学去噪，离散版学预测分层量化得到的动作码。
4. 执行时把生成结果还原为动作轨迹，再用新观测做下一次预测。

### 必要术语

- URDF：描述机器人关节、连杆和坐标关系的文件；本文把它规范化后编码成策略可读的关节图。
- 工具中心点：夹爪等末端工具采用的参考位置和坐标系；本文统一其朝向约定。
- 残差有限标量量化：先把数值取到有限档位，再逐级编码余差；本文用它把动作块变成可预测的编号。

## 证据

六个闭环仿真设置的平均成功率，离散版为 56.77%，连续版为 49.71% [S25](https://arxiv.org/html/2611.34449v1#S4.SS1.p1.1) [S26](https://arxiv.org/html/2611.34449v1#S4.F11) [S27](https://arxiv.org/html/2611.34449v1#S4.SS1.p2.1)。真机按里程碑给进度分，七项任务直接运行的离散版平均为 87.76%，后训练后的连续版为 94.52%，对照 π₀.₅ 为 86.25% [S30](https://arxiv.org/html/2611.34449v1#S4.T2) [S31](https://arxiv.org/html/2611.34449v1#S4.T2.5.1) [S32](https://arxiv.org/html/2611.34449v1#S4.SS2.p1.1) [S33](https://arxiv.org/html/2611.34449v1#S4.SS2.p2.1)[S39](https://arxiv.org/html/2611.34449v1#A2.T9.5)。双臂十一项任务中，后训练的 D-Init. 为 79.07%，π₀.₅ 为 69.41% [S35](https://arxiv.org/html/2611.34449v1#S4.SS2.p4.1) [S36](https://arxiv.org/html/2611.34449v1#S4.T3) [S37](https://arxiv.org/html/2611.34449v1#S4.T3.5.1)。Piper 到 Piper-X 的五项迁移平均为 63.28%，条件是 Piper-X 上没有这些任务的示范。未纳入预训练的 G1 则用过目标机示范 [S3](https://arxiv.org/html/2611.34449v1#abstract1.2)[S9](https://arxiv.org/html/2611.34449v1#S1.p5.1)[S24](https://arxiv.org/html/2611.34449v1#S4.p1.1)。

## 局限

作者明确报告，离散版在七项真机任务的少样本后训练后，平均进度从 87.76% 降到 69.74%，原因仍待研究 [S34](https://arxiv.org/html/2611.34449v1#S4.SS2.p3.1)。整套系统同时改了几何表示、动作生成和训练规模，我会核查统一 URDF 单独贡献多少，以及相机标定偏差会怎样影响迁移。

- **判断**：先读 URDF 变换和真机评分协议，再看两种动作头的学习曲线；这三处决定了报告里的迁移成绩能怎么解读。

## 研究关联

跨机器人学习时，坐标转换可以先在数据管线中验证。关节和工具坐标的含义一致后，才容易检查共享策略究竟学会了可复用的动作规律，还是在适应各数据源的表达习惯。

### 下一步读哪里

用 [S18](https://arxiv.org/html/2611.34449v1#S3.F2) [S19](https://arxiv.org/html/2611.34449v1#S3.SS1.p2.1) 检查轴旋转、挂接补偿和手腕滚转的人工设定。接着对照 [S28](https://arxiv.org/html/2611.34449v1#S4.SS1.p3.1)[S31](https://arxiv.org/html/2611.34449v1#S4.T2.5.1)[S35](https://arxiv.org/html/2611.34449v1#S4.SS2.p4.1) 确认每项结果实际用了哪种策略、哪些训练数据，再用 [S39](https://arxiv.org/html/2611.34449v1#A2.T9.5) 核对部分完成能拿到多少分。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34449v1
- 获取时间：2026-11-27T02:55:41.598590+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.34449v1#p1.2)
- [S2] [\calmregularHoloBrain-0.5 Technical Report · 正文段落 2](https://arxiv.org/html/2611.34449v1#abstract1.1)
- [S3] [\calmregularHoloBrain-0.5 Technical Report · 正文段落 3](https://arxiv.org/html/2611.34449v1#abstract1.2)
- [S4] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 4](https://arxiv.org/html/2611.34449v1#S1.p1.1)
- [S5] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 5](https://arxiv.org/html/2611.34449v1#S1.p2.1)
- [S6] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 6](https://arxiv.org/html/2611.34449v1#S1.F1)
- [S7] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 7](https://arxiv.org/html/2611.34449v1#S1.p3.1)
- [S8] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 8](https://arxiv.org/html/2611.34449v1#S1.p4.1)
- [S9] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 9](https://arxiv.org/html/2611.34449v1#S1.p5.1)
- [S10] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 12](https://arxiv.org/html/2611.34449v1#S1.I1.i2)
- [S11] [\calmregularfnum@section1 \calmregularIntroduction · 正文段落 13](https://arxiv.org/html/2611.34449v1#S1.I1.i3)
- [S12] [\calmregularfnum@subsection2.1 \calmregularVision-Language-Action Models · 正文段落 14](https://arxiv.org/html/2611.34449v1#S2.SS1.p1.1)
- [S13] [\calmregularfnum@subsection2.1 \calmregularVision-Language-Action Models · 正文段落 15](https://arxiv.org/html/2611.34449v1#S2.SS1.p2.1)
- [S14] [\calmregularfnum@subsection2.2 \calmregularAction-Space Modeling · 正文段落 16](https://arxiv.org/html/2611.34449v1#S2.SS2.p1.1)
- [S15] [\calmregularfnum@section3 \calmregularMethod · 正文段落 18](https://arxiv.org/html/2611.34449v1#S3.p1.1)
- [S16] [\calmregularfnum@section3 \calmregularMethod · 正文段落 19](https://arxiv.org/html/2611.34449v1#S3.E1)
- [S17] [\calmregularfnum@section3 \calmregularMethod · 正文段落 20](https://arxiv.org/html/2611.34449v1#S3.p1.2)
- [S18] [\calmregularfnum@subsection3.1 \calmregularURDF Standardization · 正文段落 22](https://arxiv.org/html/2611.34449v1#S3.F2)
- [S19] [\calmregularfnum@subsection3.1 \calmregularURDF Standardization · 正文段落 23](https://arxiv.org/html/2611.34449v1#S3.SS1.p2.1)
- [S20] [\calmregularfnum@subsection3.2 \calmregularHoloBrain-0.5-Continuous · 正文段落 37](https://arxiv.org/html/2611.34449v1#S3.SS2.p1.1)
- [S21] [\calmregularfnum@subsection3.2 \calmregularHoloBrain-0.5-Continuous · 正文段落 39](https://arxiv.org/html/2611.34449v1#S3.SS2.p3.1)
- [S22] [\calmregularfnum@subsection3.3 \calmregularHoloBrain-0.5-Discrete · 正文段落 58](https://arxiv.org/html/2611.34449v1#S3.SS3.p4.1)
- [S23] [\calmregularfnum@subsection3.3 \calmregularHoloBrain-0.5-Discrete · 正文段落 72](https://arxiv.org/html/2611.34449v1#S3.SS3.p10.1)
- [S24] [\calmregularfnum@section4 \calmregularExperiments · 正文段落 83](https://arxiv.org/html/2611.34449v1#S4.p1.1)
- [S25] [\calmregularfnum@subsection4.1 \calmregularClosed-Loop Performance of Pretrained Models · 正文段落 84](https://arxiv.org/html/2611.34449v1#S4.SS1.p1.1)
- [S26] [\calmregularfnum@subsection4.1 \calmregularClosed-Loop Performance of Pretrained Models · 正文段落 85](https://arxiv.org/html/2611.34449v1#S4.F11)
- [S27] [\calmregularfnum@subsection4.1 \calmregularClosed-Loop Performance of Pretrained Models · 正文段落 86](https://arxiv.org/html/2611.34449v1#S4.SS1.p2.1)
- [S28] [\calmregularfnum@subsection4.1 \calmregularClosed-Loop Performance of Pretrained Models · 正文段落 87](https://arxiv.org/html/2611.34449v1#S4.SS1.p3.1)
- [S29] [\calmregularfnum@subsection4.1 \calmregularClosed-Loop Performance of Pretrained Models · 正文段落 88](https://arxiv.org/html/2611.34449v1#S4.SS1.p4.1)
- [S30] [\calmregularfnum@subsection4.1 \calmregularClosed-Loop Performance of Pretrained Models · 正文段落 89](https://arxiv.org/html/2611.34449v1#S4.T2)
- [S31] [\calmregularfnum@subsection4.1 \calmregularClosed-Loop Performance of Pretrained Models · 正文段落 90](https://arxiv.org/html/2611.34449v1#S4.T2.5.1)
- [S32] [\calmregularfnum@subsection4.2 \calmregularPost-Training Performance · 正文段落 91](https://arxiv.org/html/2611.34449v1#S4.SS2.p1.1)
- [S33] [\calmregularfnum@subsection4.2 \calmregularPost-Training Performance · 正文段落 92](https://arxiv.org/html/2611.34449v1#S4.SS2.p2.1)
- [S34] [\calmregularfnum@subsection4.2 \calmregularPost-Training Performance · 正文段落 93](https://arxiv.org/html/2611.34449v1#S4.SS2.p3.1)
- [S35] [\calmregularfnum@subsection4.2 \calmregularPost-Training Performance · 正文段落 94](https://arxiv.org/html/2611.34449v1#S4.SS2.p4.1)
- [S36] [\calmregularfnum@subsection4.2 \calmregularPost-Training Performance · 正文段落 95](https://arxiv.org/html/2611.34449v1#S4.T3)
- [S37] [\calmregularfnum@subsection4.2 \calmregularPost-Training Performance · 正文段落 96](https://arxiv.org/html/2611.34449v1#S4.T3.5.1)
- [S38] [\calmregularfnum@section5 \calmregularConclusion · 正文段落 111](https://arxiv.org/html/2611.34449v1#S5.p1.1)
- [S39] [Appendix B Real-Robot Evaluation Protocol · 正文段落 135](https://arxiv.org/html/2611.34449v1#A2.T9.5)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/HoloBrain-0.5 Technical Report.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present HoloBrain-0.5, a family of vision-language-action (VLA) models for manipulation across robot embodiments. The policies plan in a shared action space using robot state, kinematic structure, and calibrated camera observations. We standardize joint axes, coordinate frames, and tool-center points in robot descriptions (URDFs) and encode their kinematic graphs in a shared 3D representation. HoloBrain-0.5-Continuous generates action chunks by diffusion, while HoloBrain-0.5-Discrete uses residual finite scalar quantization (FSQ) and delayed autoregression. We pretrain both policies on over 10,000 hours of real-robot, simulation, and human-manipulation data spanning 15 embodiment categories. Across six closed-loop simulation settings, the discrete policy converges faster and reaches a higher mean success rate than the continuous policy (56.77% vs. 49.71%). On seven real-robot tasks, it achieves a mean progress score of 87.76% without task-specific post-training. After post-training, the continuous policy outperforms $π_{0.5}$ on the seven-task benchmark (94.52% vs. 86.25%) and an 11-task dual-arm benchmark (79.07% vs. 69.41%). The discrete-initialized continuous policy transfers five tasks zero-shot from Piper to Piper-X, scoring 63.28% on average. With target-robot demonstrations, the continuous policy scores 89.2% on Franka Panda and 92.94% on a mobile dual-arm platform. Although pretraining includes no Unitree G1 data, post-training with limited G1 demonstrations yields a mean progress score of 70.24% across three humanoid tasks, compared with 11.00% for $π_{0.5}$.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34449v1
- Authors: Xuewu Lin, Jiahao Wang, Jiawei Li, Mengdi Li, Zhengmao Sun, Yiwei Jin, Hongyu Xie, Zhengyang Feng, Kun Wu, Zihao Chen, Lianzhou Zhang, Lichao Huang, Zhizhong Su
- Published: 2026-11-25T14:28:05Z
- Age days: 1

</details>
