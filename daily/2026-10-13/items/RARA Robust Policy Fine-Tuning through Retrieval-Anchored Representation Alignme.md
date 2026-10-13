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
url: "https://arxiv.org/abs/2610.13578v1"
published: "2026-10-09T13:31:20Z"
age_days: 3
score: 42
created: 2026-10-13
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RARA让机器人用少量示范学新任务时，先借用预训练中相似技能的内部表示，再一边学新动作、一边保住这些旧经验。关键是只保护与目标任务相关的示范，而不是把整个模型拉回原样。

## 问题

任务是把预训练策略适配到新操作。仅用目标示范模仿动作，可能学会训练场景，却在背景、视角或物体变化后失败；作者将其与预训练表示被改坏联系起来[S3](https://arxiv.org/html/2610.13578v1#S1.p1.1)。已有权重约束、模型合并或教师对齐能保留知识，但没有明确挑出哪些旧经验最值得保护[S4](https://arxiv.org/html/2610.13578v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入是新盒子的开盖示范和旧开盖数据；系统先找同类指令，再配对“夹住盖边”的动作阶段，完成对齐和微调；输出是在新盒子观测下生成开盖动作的策略。

## 创新点或方法

旧做法直接学目标动作；RARA先按指令找同类技能，再按短动作序列找相同阶段，让目标画面的表示靠近冻结预训练模型对这些旧画面的表示。随后用目标动作做行为克隆，同时约束旧示范表示的变化。巧处是约束落在旧示范上，目标表示仍能适应新场景。第一阶段只训练表示相关层与投影器；第二阶段按原策略的微调配置训练，部署丢弃投影器，只运行策略[S14](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px1.p1.1) [S15](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px2.p1.1) [S16](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px2.p2.2)。

### 方法如何工作

1. 把目标指令编码并检索相近旧示范，先限定技能类型，避免只因都向上抬就配错任务[S20](https://arxiv.org/html/2610.13578v1#S4.SS1.SSS0.Px1.p1.1)。
2. 比较短动作序列的DTW距离，得到相同运动阶段的正样本和不同阶段的负样本；旧动作仅用于配对[S21](https://arxiv.org/html/2610.13578v1#S4.SS1.SSS0.Px2.p1.1)。
3. 用对比学习拉近目标与冻结旧表示，同时锚定旧示范表示，获得适合目标场景的初始化[S13](https://arxiv.org/html/2610.13578v1#S4.p1.1) [S14](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px1.p1.1)。
4. 用目标动作微调并保留锚定约束，最后移除投影器，让部署直接输出机器人动作[S15](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px2.p1.1)。

### 必要术语

- 表示：模型内部对观测的编码；本文对齐和保护的对象。
- DTW：允许速度不同的序列对齐距离；用于匹配运动阶段。
- 锚定损失：惩罚旧示范表示偏离预训练值；防止相关经验被覆盖。

## 证据

测试覆盖Diffusion Policy的四个RoboTwin任务，以及GR00T的五个RoboCasa任务和四个Franka真机任务；OOD改变布局、背景、干扰物、视角或物体[S6](https://arxiv.org/html/2610.13578v1#S1.p4.1) [S32](https://arxiv.org/html/2610.13578v1#S5.I2.i1) [S33](https://arxiv.org/html/2610.13578v1#S5.I2.i2) [S34](https://arxiv.org/html/2610.13578v1#S5.I2.i3) [S35](https://arxiv.org/html/2610.13578v1#S5.I3.i1)。相对普通微调，平均成功率ID增加9.5个百分点、OOD增加13.6个百分点，并超过所比较基线[S6](https://arxiv.org/html/2610.13578v1#S1.p4.1)。这支持同机器人、同动作空间下的适配；节选未给各基线成绩、重复试验与不确定性，不能判断每个任务收益是否均匀。

## 局限

作者明确依赖预训练数据含有同类任务，实验主要研究同机器人与动作空间下的视觉变化[S36](https://arxiv.org/html/2610.13578v1#S6.p1.1)。我的待核查问题是：检索到语义相近但接触方式不同的示范时会怎样，以及两阶段各贡献多少；节选提到相关分析，但没有结果。

- **判断**：值得读到损失和消融：它给出了明确的选择性约束办法，但收益能否复现取决于旧数据是否提供合适参照。

## 研究关联

值得借鉴的是把“保住预训练知识”改成“保住当前任务需要的经验”。当旧数据中确有同类技能时，可以先解决视觉表示的对应关系，再学习动作，而不必把旧动作全部混入模仿目标。

### 下一步读哪里

先看[S19](https://arxiv.org/html/2610.13578v1#S4.SS1.p1.1) [S20](https://arxiv.org/html/2610.13578v1#S4.SS1.SSS0.Px1.p1.1) [S21](https://arxiv.org/html/2610.13578v1#S4.SS1.SSS0.Px2.p1.1) [S22](https://arxiv.org/html/2610.13578v1#S4.SS2.p1.1) [S23](https://arxiv.org/html/2610.13578v1#S4.SS2.SSS0.Px1.p1.1) [S24](https://arxiv.org/html/2610.13578v1#S4.SS2.SSS0.Px2.p1.1)的两级检索与正负配对，再核查锚定损失公式、检索数量和动作距离归一化；接着查[S7](https://arxiv.org/html/2610.13578v1#S1.p5.1)所述阶段消融、数据选择和层选择实验的实际结果。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.13578v1
- 获取时间：2026-10-13T00:21:43.610292+00:00
- [S1] [RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2610.13578v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.13578v1#S1.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.13578v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.13578v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.13578v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.13578v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.13578v1#S1.p5.1)
- [S8] [2 Related Work · 正文段落 8](https://arxiv.org/html/2610.13578v1#S2.p1.1)
- [S9] [2 Related Work · 正文段落 9](https://arxiv.org/html/2610.13578v1#S2.p2.1)
- [S10] [3 Problem Definition · 正文段落 10](https://arxiv.org/html/2610.13578v1#S3.p1.1)
- [S11] [3 Problem Definition · 正文段落 12](https://arxiv.org/html/2610.13578v1#S3.p1.2)
- [S12] [3 Problem Definition · 正文段落 14](https://arxiv.org/html/2610.13578v1#S3.p1.3)
- [S13] [4 RARA: Retrieval-Anchored Representation Alignment · 正文段落 15](https://arxiv.org/html/2610.13578v1#S4.p1.1)
- [S14] [4 RARA: Retrieval-Anchored Representation Alignment · 正文段落 16](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px1.p1.1)
- [S15] [4 RARA: Retrieval-Anchored Representation Alignment · 正文段落 17](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px2.p1.1)
- [S16] [4 RARA: Retrieval-Anchored Representation Alignment · 正文段落 20](https://arxiv.org/html/2610.13578v1#S4.SS0.SSS0.Px2.p2.2)
- [S17] [4 RARA: Retrieval-Anchored Representation Alignment · 正文段落 21](https://arxiv.org/html/2610.13578v1#S4.F2)
- [S18] [4.1 Retrieving Relevant Pre-training Demonstrations · 正文段落 22](https://arxiv.org/html/2610.13578v1#S4.F3)
- [S19] [4.1 Retrieving Relevant Pre-training Demonstrations · 正文段落 23](https://arxiv.org/html/2610.13578v1#S4.SS1.p1.1)
- [S20] [4.1 Retrieving Relevant Pre-training Demonstrations · 正文段落 24](https://arxiv.org/html/2610.13578v1#S4.SS1.SSS0.Px1.p1.1)
- [S21] [4.1 Retrieving Relevant Pre-training Demonstrations · 正文段落 25](https://arxiv.org/html/2610.13578v1#S4.SS1.SSS0.Px2.p1.1)
- [S22] [4.2 Aligning an Intermediate Representation · 正文段落 26](https://arxiv.org/html/2610.13578v1#S4.SS2.p1.1)
- [S23] [4.2 Aligning an Intermediate Representation · 正文段落 27](https://arxiv.org/html/2610.13578v1#S4.SS2.SSS0.Px1.p1.1)
- [S24] [4.2 Aligning an Intermediate Representation · 正文段落 28](https://arxiv.org/html/2610.13578v1#S4.SS2.SSS0.Px2.p1.1)
- [S25] [4.2 Aligning an Intermediate Representation · 正文段落 31](https://arxiv.org/html/2610.13578v1#S4.SS2.SSS0.Px3.p1.1)
- [S26] [5 Experiments · 正文段落 34](https://arxiv.org/html/2610.13578v1#S5.p1.1)
- [S27] [5 Experiments · 正文段落 35](https://arxiv.org/html/2610.13578v1#S5.I1.i1)
- [S28] [5 Experiments · 正文段落 36](https://arxiv.org/html/2610.13578v1#S5.I1.i2)
- [S29] [5 Experiments · 正文段落 37](https://arxiv.org/html/2610.13578v1#S5.I1.i3)
- [S30] [5 Experiments · 正文段落 38](https://arxiv.org/html/2610.13578v1#S5.I1.i4)
- [S31] [5.1 Setup · 正文段落 39](https://arxiv.org/html/2610.13578v1#S5.SS1.p1.1)
- [S32] [5.1 Setup · 正文段落 40](https://arxiv.org/html/2610.13578v1#S5.I2.i1)
- [S33] [5.1 Setup · 正文段落 41](https://arxiv.org/html/2610.13578v1#S5.I2.i2)
- [S34] [5.1 Setup · 正文段落 42](https://arxiv.org/html/2610.13578v1#S5.I2.i3)
- [S35] [5.1 Setup · 正文段落 44](https://arxiv.org/html/2610.13578v1#S5.I3.i1)
- [S36] [6 Conclusion · 正文段落 70](https://arxiv.org/html/2610.13578v1#S6.p1.1)
- [S37] [D.2 RoboTwin · 正文段落 109](https://arxiv.org/html/2610.13578v1#A4.T4)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/RARA Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignme.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Representation Alignment (RARA), a two-stage adaptation method, to address this issue. First, RARA retrieves representation features from pretraining with similar task intent and motion, and aligns the policy's representations of the target demonstrations with the pre-trained representations of the retrieved demonstrations. Second, RARA fine-tunes the policy on the target demonstrations while limiting how much its representations of the retrieved demonstrations change during fine-tuning. By reducing the representation mismatch before action learning and preserving pre-trained knowledge during adaptation, RARA limits unnecessary representation drift during fine-tuning. Experiments with Diffusion Policy and GR00T on 13 tasks in RoboTwin, RoboCasa, and on a real robot show that RARA improves the average success of fine-tuning by 9.5 points in-distribution and 13.6 points out-of-distribution, and outperforms all compared baselines. Project page: https://shua-kang.github.io/RARA_robot/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.13578v1
- Authors: Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo
- Published: 2026-10-09T13:31:20Z
- Age days: 3

</details>
