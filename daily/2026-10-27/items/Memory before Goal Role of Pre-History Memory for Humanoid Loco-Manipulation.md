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
url: "https://arxiv.org/abs/2610.31166v1"
published: "2026-10-22T12:24:25Z"
age_days: 4
score: 44
created: 2026-10-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> WholeBodyMem 给人形机器人保存“目标动作开始之前发生过什么”的记忆。它跟踪任务物体，在物体发生事件时留下关键画面，让动作模型能利用已经消失或被转身甩出视野的线索。

## 问题

机器人可能先看到某个位置闪灯，再转身取物，最后根据闪灯位置放置物体。此时当前画面无法给出答案。长历史成本高且淹没短暂线索，压缩可能丢细节，固定间隔采样可能直接漏掉事件；走动的相机还会把自身运动误当成物体变化。[S2](https://arxiv.org/html/2610.31166v1#S1.p1.1) [S8](https://arxiv.org/html/2610.31166v1#S2.SS2.p1.1)

### 用一个例子理解

理解用例（非论文实验）：机器人看到左侧桌位短暂亮灯，随后转身拿杯子；系统保存亮灯事件画面，返回时动作专家读取它，输出走向左侧桌位并放杯的动作。

## 创新点或方法

旧做法只看当前帧或均匀留帧；本文用冻结的 SAM3 跟踪指定物体，先补偿相机运动，再根据物体事件在线选帧。动作专家通过交叉注意力读取历史画面，以及编码物体外观、位置和时间的对象令牌。[S17](https://arxiv.org/html/2610.31166v1#S4.SS2.p3.1) [S19](https://arxiv.org/html/2610.31166v1#S4.SS3.p1.1) [S23](https://arxiv.org/html/2610.31166v1#S4.SS3.p5.1) 训练按任务微调，结合动作学习与答案分类监督，视觉语言骨干冻结；推理时只读取当时已经发生的历史，不依赖未来画面。[S25](https://arxiv.org/html/2610.31166v1#S4.SS4.p1.1)

### 方法如何工作

1. 依据任务短语跟踪物体，并补偿相机运动，避免把转身当成物体事件。
2. 用已经观察到的事件选择关键帧，在有限预算中保留决定答案的细节。
3. 把历史画面和对象信息交给动作专家，使未来动作能读取当前视野外的线索。
4. 训练时同时监督动作与答案，推理时在线更新记忆并生成全身动作。

### 必要术语

- 非马尔可夫：只看现在不足以确定正确动作；本文任务需要过去的线索。
- 因果更新：只使用截至当前已经看到的信息；本文用于在线维护记忆。
- 交叉注意力：让一组表示查询另一组信息；本文让动作令牌读取历史画面。

## 证据

六项仿真记忆任务中，成功率为 72.6%，无记忆基座为 29.1%，均匀记忆为 44.4%；记忆决策准确率为 93.7%。[S37](https://arxiv.org/html/2610.31166v1#S5.SS3.p1.1) 六项 G1 真机任务每种策略每任务测试 10 次，WholeBodyMem 成功 53/60，无记忆基座为 22/60。[S38](https://arxiv.org/html/2610.31166v1#S5.SS5.p1.1) [S41](https://arxiv.org/html/2610.31166v1#S5.SS5.p4.1) 标准 SIMPLE 成功率也由 70.2% 升至 86.9%。[S36](https://arxiv.org/html/2610.31166v1#S5.SS2.p1.1) 但仿真测试仍在训练分布内；均匀记忆还同时缺少对象令牌和决策头，整体差距不能全部归因于选帧。[S13](https://arxiv.org/html/2610.31166v1#S3.I1.i6) [S33](https://arxiv.org/html/2610.31166v1#S5.SS1.p3.1)

## 局限

作者明确指出：物体从未被检测到时就会漏记线索，跟踪增加推理成本，仿真示范由脚本生成且存在仿真到现实差距。[S42](https://arxiv.org/html/2610.31166v1#S6.p1.1) 另需核查真机低频跟踪能否捕捉更短事件，以及组件消融分别支持多大贡献；真机主要对比无记忆基座。

- **判断**：值得细读记忆选择、组件消融和评测设计：它把“需要记忆”变成了可以单独检验的任务条件。

## 研究关联

值得借鉴的是按“哪些事件会改变后续答案”设计记忆，而不是单纯延长上下文。把记对答案和操作成功分开评估，也能区分机器人究竟忘了线索，还是记住了却没执行好。

### 下一步读哪里

看事件规则如何分配有限帧预算，并核查消融能否隔离选帧、对象令牌与决策头的作用。[S29](https://arxiv.org/html/2610.31166v1#S5.I1.ix3) 同时对照训练方案 [S25](https://arxiv.org/html/2610.31166v1#S4.SS4.p1.1) 与真机跟踪频率 [S32](https://arxiv.org/html/2610.31166v1#S5.SS1.p2.1)，检查部署成本和漏检风险。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.31166v1
- 获取时间：2026-10-27T00:26:54.298111+00:00
- [S1] [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation · 正文段落 1](https://arxiv.org/html/2610.31166v1#abstract1.1)
- [S2] [I Introduction · 正文段落 2](https://arxiv.org/html/2610.31166v1#S1.p1.1)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2610.31166v1#S1.F1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2610.31166v1#S1.F2)
- [S5] [I Introduction · 正文段落 8](https://arxiv.org/html/2610.31166v1#S1.I1.i2)
- [S6] [I Introduction · 正文段落 9](https://arxiv.org/html/2610.31166v1#S1.I1.i3)
- [S7] [II-A Whole-Body Humanoid Loco-Manipulation VLAs · 正文段落 11](https://arxiv.org/html/2610.31166v1#S2.SS1.p1.1)
- [S8] [II-B Memory and Datasets for Robot Policies · 正文段落 12](https://arxiv.org/html/2610.31166v1#S2.SS2.p1.1)
- [S9] [III Memory-Dependent Loco-Manipulation Benchmark · 正文段落 15](https://arxiv.org/html/2610.31166v1#S3.T1.3)
- [S10] [III-A Task Definition · 正文段落 16](https://arxiv.org/html/2610.31166v1#S3.SS1.p1.1)
- [S11] [III-A Task Definition · 正文段落 17](https://arxiv.org/html/2610.31166v1#S3.SS1.p2.1)
- [S12] [III-B Data Generation · 正文段落 18](https://arxiv.org/html/2610.31166v1#S3.SS2.p1.1)
- [S13] [III-B Data Generation · 正文段落 24](https://arxiv.org/html/2610.31166v1#S3.I1.i6)
- [S14] [III-C Data Analysis · 正文段落 30](https://arxiv.org/html/2610.31166v1#S3.T3.2)
- [S15] [III-C Data Analysis · 正文段落 31](https://arxiv.org/html/2610.31166v1#S3.T3.3)
- [S16] [IV-A Preliminaries: Whole-Body VLA Policies · 正文段落 32](https://arxiv.org/html/2610.31166v1#S4.SS1.p1.1)
- [S17] [IV-B Object-Guided Memory Selection · 正文段落 36](https://arxiv.org/html/2610.31166v1#S4.SS2.p3.1)
- [S18] [IV-B Object-Guided Memory Selection · 正文段落 38](https://arxiv.org/html/2610.31166v1#S4.F4)
- [S19] [IV-C Memory Cross-Attention in the Action Expert · 正文段落 40](https://arxiv.org/html/2610.31166v1#S4.SS3.p1.1)
- [S20] [IV-C Memory Cross-Attention in the Action Expert · 正文段落 43](https://arxiv.org/html/2610.31166v1#S4.SS3.p2.2)
- [S21] [IV-C Memory Cross-Attention in the Action Expert · 正文段落 46](https://arxiv.org/html/2610.31166v1#S4.SS3.p3.2)
- [S22] [IV-C Memory Cross-Attention in the Action Expert · 正文段落 49](https://arxiv.org/html/2610.31166v1#S4.SS3.p4.2)
- [S23] [IV-C Memory Cross-Attention in the Action Expert · 正文段落 50](https://arxiv.org/html/2610.31166v1#S4.SS3.p5.1)
- [S24] [IV-C Memory Cross-Attention in the Action Expert · 正文段落 51](https://arxiv.org/html/2610.31166v1#S4.SS3.p6.1)
- [S25] [IV-D Training Details · 正文段落 53](https://arxiv.org/html/2610.31166v1#S4.SS4.p1.1)
- [S26] [V Experiments · 正文段落 54](https://arxiv.org/html/2610.31166v1#S5.p1.1)
- [S27] [V Experiments · 正文段落 55](https://arxiv.org/html/2610.31166v1#S5.I1.ix1)
- [S28] [V Experiments · 正文段落 56](https://arxiv.org/html/2610.31166v1#S5.I1.ix2)
- [S29] [V Experiments · 正文段落 57](https://arxiv.org/html/2610.31166v1#S5.I1.ix3)
- [S30] [V Experiments · 正文段落 58](https://arxiv.org/html/2610.31166v1#S5.I1.ix4)
- [S31] [V-A Setup · 正文段落 59](https://arxiv.org/html/2610.31166v1#S5.SS1.p1.1)
- [S32] [V-A Setup · 正文段落 60](https://arxiv.org/html/2610.31166v1#S5.SS1.p2.1)
- [S33] [V-A Setup · 正文段落 61](https://arxiv.org/html/2610.31166v1#S5.SS1.p3.1)
- [S34] [V-A Setup · 正文段落 62](https://arxiv.org/html/2610.31166v1#S5.SS1.p4.1)
- [S35] [V-A Setup · 正文段落 63](https://arxiv.org/html/2610.31166v1#S5.T4)
- [S36] [V-B Results on Standard Loco-Manipulation Tasks (Q1) · 正文段落 66](https://arxiv.org/html/2610.31166v1#S5.SS2.p1.1)
- [S37] [V-C Results on Memory-Dependent Tasks (Q2) · 正文段落 67](https://arxiv.org/html/2610.31166v1#S5.SS3.p1.1)
- [S38] [V-E Real-World Experiments (Q4) · 正文段落 73](https://arxiv.org/html/2610.31166v1#S5.SS5.p1.1)
- [S39] [V-E Real-World Experiments (Q4) · 正文段落 74](https://arxiv.org/html/2610.31166v1#S5.SS5.p2.1)
- [S40] [V-E Real-World Experiments (Q4) · 正文段落 75](https://arxiv.org/html/2610.31166v1#S5.SS5.p3.1)
- [S41] [V-E Real-World Experiments (Q4) · 正文段落 76](https://arxiv.org/html/2610.31166v1#S5.SS5.p4.1)
- [S42] [VI Limitations and Conclusion · 正文段落 77](https://arxiv.org/html/2610.31166v1#S6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/Memory before Goal Role of Pre-History Memory for Humanoid Loco-Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.31166v1
- Authors: Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
- Published: 2026-10-22T12:24:25Z
- Age days: 4

</details>
