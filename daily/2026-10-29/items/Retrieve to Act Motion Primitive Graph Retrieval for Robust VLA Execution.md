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
url: "https://arxiv.org/abs/2610.37215v1"
published: "2026-10-27T13:28:33Z"
age_days: 1
score: 34
created: 2026-10-29
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Retrieve to Act（R2A）在视觉干扰让VLA动作跑偏时，从成功示范构成的运动图中找合适的后续，再与原动作融合。它用运动几何定位执行进度，原VLA保持冻结。

## 问题

任务和目标没变，换光照、背景或相机角度却可能让空间动作出错。枚举所有视觉变化再微调不现实；单纯按图像相似度检索，又容易受同样干扰，还混淆“现在做到哪里”和“接下来该怎么动”。[S3](https://arxiv.org/html/2610.37215v1#S1.p1.1) [S4](https://arxiv.org/html/2610.37215v1#S1.p2.1) [S5](https://arxiv.org/html/2610.37215v1#S1.p3.1) 本文要利用示范中仍然有效的几何与时序关系。

### 用一个例子理解

理解用例（非论文实验）：背景换成花纹后，VLA搬盒路线开始偏移；R2A输入近期机械臂运动和当前预测，在图中定位到搬运阶段，取出兼容后续，再逐维融合成执行动作。若出现图中没有的新障碍，仅检索旧路线未必足够。

## 创新点或方法

旧做法从视觉快照找相似示范；本文离线把成功运动片段建成图，节点存姿态、状态和变化，边存时空关系。推理先用扩散模块把异常初始状态拉回训练分布，再将近期状态与VLA当前预测构成几何查询，由查询条件GNN定位并检索后续。逐维门控融合检索动作和原动作，保留局部反应能力。[S6](https://arxiv.org/html/2610.37215v1#S1.p4.1) [S18](https://arxiv.org/html/2610.37215v1#S3.SS2.p2.1) 检索路径不用图像特征，但查询含VLA预测，不能理解成整套系统摆脱视觉。附加模块需要学习，具体训练损失在所给节选中未说明。

### 方法如何工作

1. 离线把成功示范组织成运动图，保留片段间的顺序与几何联系。
2. 回合开始时校正异常初始状态，为后续匹配建立更接近训练经验的起点。
3. 用近期状态和VLA预测构造查询，在图中定位当前进度并寻找兼容后续。
4. 逐维融合检索参考与原预测，输出修正动作，并随执行更新查询。

### 必要术语

- 运动原语图：连接成功运动片段的图；本文用其同时表达执行位置和后续关系。
- 查询条件GNN：随当前查询调整图上信息传递的网络；用于动态定位和检索。
- 逐维门控：分别决定各动作维度如何融合两种来源；避免整段机械替换原动作。

## 证据

LIBERO-Plus七类扰动下，加入R2A后GR00T N1.7从77.1%到89.0%，StableVLA从78.1%到89.5%，π0.5从85.9%到90.4%。[S22](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p3.1) RoboTwin2.0-Plus中π0.5从56.8%到66.2%，初始状态扰动从34.2%到75.9%。[S24](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.fig1.1) 同一LIBERO-10比较中，π0.5加R2A为86.3%，加SDN为83.8%，但传感器噪声下SDN更好。[S26](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.fig1.2) 真机最高增加40个百分点来自摘要，所给节选缺任务细节、试验次数和分项结果；这些数字不能跨论文直接排名。

## 局限

作者明确承认图中没有场景几何，新障碍要靠VLA输出传递；图外的新恢复序列如何生成仍不清楚，门控也可能应付不了超出训练扰动的错误。[S32](https://arxiv.org/html/2610.37215v1#S6.p2.1) 我的待核查问题是初始状态校正与图检索各占多少增益，尤其最大提升集中在初始状态扰动，不能全部解释为抵抗视觉噪声。

- **判断**：值得读到图结构、初始校正和门控消融；它适合检验已有运动经验能否稳定执行，但不能当通用避障或恢复机制。

## 研究关联

值得借鉴的是把成功经验保留为可查询的结构，而非全部压进策略参数。若任务已有可复用示范、执行几何仍可信，检索“适合接下去的动作”可能比继续修补视觉特征更直接。

### 下一步读哪里

沿[S18](https://arxiv.org/html/2610.37215v1#S3.SS2.p2.1)核查查询窗口、建边规则和门控训练目标，再查初始校正的独立消融与检索延迟；结合[S32](https://arxiv.org/html/2610.37215v1#S6.p2.1)检查无匹配示范、新障碍和图外恢复时如何处理。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.37215v1
- 获取时间：2026-10-29T00:42:07.262137+00:00
- [S1] [Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution · 正文段落 1](https://arxiv.org/html/2610.37215v1#abstract1.1)
- [S2] [Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution · 正文段落 2](https://arxiv.org/html/2610.37215v1#abstract1.2)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.37215v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.37215v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.37215v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.37215v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.37215v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.37215v1#S1.F1)
- [S9] [Test-Time Robustness of VLA Policies. · 正文段落 9](https://arxiv.org/html/2610.37215v1#S2.SS0.SSS0.Px1.p1.1)
- [S10] [Test-Time Robustness of VLA Policies. · 正文段落 10](https://arxiv.org/html/2610.37215v1#S2.SS0.SSS0.Px1.p2.1)
- [S11] [Retrieval-Augmented Robot Learning. · 正文段落 11](https://arxiv.org/html/2610.37215v1#S2.SS0.SSS0.Px2.p1.1)
- [S12] [Retrieval-Augmented Robot Learning. · 正文段落 12](https://arxiv.org/html/2610.37215v1#S2.SS0.SSS0.Px2.p2.1)
- [S13] [Graph-Structured and Relational Retrieval. · 正文段落 13](https://arxiv.org/html/2610.37215v1#S2.SS0.SSS0.Px3.p1.1)
- [S14] [Graph-Structured and Relational Retrieval. · 正文段落 14](https://arxiv.org/html/2610.37215v1#S2.SS0.SSS0.Px3.p2.1)
- [S15] [3.1 Preliminaries & Problem Formulation · 正文段落 15](https://arxiv.org/html/2610.37215v1#S3.SS1.p1.1)
- [S16] [3.1 Preliminaries & Problem Formulation · 正文段落 16](https://arxiv.org/html/2610.37215v1#S3.SS1.p2.1)
- [S17] [3.2 R2A Overview · 正文段落 17](https://arxiv.org/html/2610.37215v1#S3.SS2.p1.1)
- [S18] [3.2 R2A Overview · 正文段落 19](https://arxiv.org/html/2610.37215v1#S3.SS2.p2.1)
- [S19] [Main Results. · 正文段落 54](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p1.1)
- [S20] [Main Results. · 正文段落 55](https://arxiv.org/html/2610.37215v1#S5.T1)
- [S21] [Main Results. · 正文段落 57](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p2.1)
- [S22] [Main Results. · 正文段落 58](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p3.1)
- [S23] [Main Results. · 正文段落 59](https://arxiv.org/html/2610.37215v1#S5.T2)
- [S24] [Main Results. · 正文段落 60](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.fig1.1)
- [S25] [Main Results. · 正文段落 61](https://arxiv.org/html/2610.37215v1#S5.T3)
- [S26] [Main Results. · 正文段落 62](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.fig1.2)
- [S27] [Main Results. · 正文段落 64](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p4.1)
- [S28] [Main Results. · 正文段落 65](https://arxiv.org/html/2610.37215v1#S5.F3)
- [S29] [Main Results. · 正文段落 66](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p5.1)
- [S30] [Main Results. · 正文段落 68](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p7.1)
- [S31] [Ablation Study. · 正文段落 75](https://arxiv.org/html/2610.37215v1#S5.F4)
- [S32] [6 Conclusion and Discussion · 正文段落 79](https://arxiv.org/html/2610.37215v1#S6.p2.1)
- [S33] [6 Conclusion and Discussion · 正文段落 80](https://arxiv.org/html/2610.37215v1#S6.p3.1)
- [S34] [C.1 Implementation details · 正文段落 107](https://arxiv.org/html/2610.37215v1#A3.T6)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Retrieve to Act Motion Primitive Graph Retrieval for Robust VLA Execution.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies demonstrate remarkable semantic generalization, yet remain highly vulnerable to out-of-distribution (OOD) visual shifts during execution. While existing test-time methods attempt to suppress spurious visual cues, they fundamentally overlook the rich, uncorrupted kinematic priors embedded in the policy's own training experience. We introduce Retrieve to Act (R2A), a test-time scaling framework that formulates OOD robustness purely as a geometric motion primitive retrieval problem. R2A bypasses fragile visual features by structuring successful training demonstrations into an offline spatiotemporal motion primitive graph. During inference, a query-dependent Graph Neural Network dynamically localizes the robot's ongoing execution within this graph, retrieving structurally compatible future motion primitives. These retrieved geometric priors are then seamlessly harmonized with the frozen VLA's predicted actions via a learned, dimension-wise gating mechanism, adaptively rectifying erroneous spatial trajectories while preserving the policy's local reactivity. Extensive experiments across three state-of-the-art VLA architectures, GR00T N1.7, $π_{0.5}$, and StableVLA, demonstrate that R2A consistently and significantly enhances robustness against diverse contextual perturbations. R2A achieves absolute success rate improvements of up to +12% in simulation benchmarks (LIBERO-Plus, RoboTwin2.0-Plus) and +40% in real-world deployments, without requiring any finetuning of the base policies. Project page: https://retrieve2act.github.io/r2a/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37215v1
- Authors: Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen, Duc-Duy Nguyen, Hung T. Ho, Linh Dang Le, Trong-Bao Ho, Thien-Loc Ha, Tan Q. Nguyen, Tuan Dam, Vu N. Duong, Daniel Sonntag, Ngan Le, Khoa D. Doan, Jan Peters, An Thai Le, Duy M. H. Nguyen, Vien Anh Ngo
- Published: 2026-10-27T13:28:33Z
- Age days: 1

</details>
