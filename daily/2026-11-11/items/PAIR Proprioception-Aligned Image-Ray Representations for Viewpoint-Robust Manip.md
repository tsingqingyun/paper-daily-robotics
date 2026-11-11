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
url: "https://arxiv.org/abs/2611.11798v1"
published: "2026-11-09T02:54:44Z"
age_days: 1
score: 41
created: 2026-11-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PAIR 要解决的是：相机换个位置，机器人就不会操作了。它把图像与相机射线一起编码，再用机械臂自身状态判断哪些观测应该接近，让模型学会跨视角认出相近的机器人配置。

## 问题

同一抓取姿态从两侧拍，夹爪与物体的左右关系可能反转，但机器人需要执行的动作并没变。只加相机信息，没有教模型如何利用它；只按机器人状态拉近图像特征，又可能忽略投影差异，产生冲突监督。[S4](https://arxiv.org/html/2611.11798v1#S1.p2.1) [S5](https://arxiv.org/html/2611.11798v1#S1.p3.1) [S6](https://arxiv.org/html/2611.11798v1#S1.p4.1)

### 用一个例子理解

理解用例（非论文实验）：输入侧面图像、相机标定和机械臂状态；PAIR 用射线解释杯子与夹爪的投影关系，策略输出接近杯子的动作序列。换到另一侧相机时，目标仍是同一物理抓取动作。

## 创新点或方法

旧做法分别提供几何信息或做跨视角对齐；PAIR 把两件事合起来。它将基座坐标系和末端坐标系下的射线几何注入视觉 token，再按末端位置、朝向和夹爪宽度的相似性约束表示。训练同时学习模仿动作和表示对齐；推理时用图像、射线、机器人状态及任务条件预测动作序列，无须执行对比学习。[S2](https://arxiv.org/html/2611.11798v1#S0.F2) [S6](https://arxiv.org/html/2611.11798v1#S1.p4.1) [S12](https://arxiv.org/html/2611.11798v1#S3.SS1.p1.1) [S13](https://arxiv.org/html/2611.11798v1#S3.SS1.p2.1) [S14](https://arxiv.org/html/2611.11798v1#S3.SS3.p1.4) [S15](https://arxiv.org/html/2611.11798v1#S3.SS3.p3.3) [S16](https://arxiv.org/html/2611.11798v1#S3.F3) [S17](https://arxiv.org/html/2611.11798v1#S3.SS4.p1.1) [S18](https://arxiv.org/html/2611.11798v1#S3.SS4.p2.5)

### 方法如何工作

1. 将相机射线转换到基座和末端坐标系，使视觉位置带有机器人参照。[S2](https://arxiv.org/html/2611.11798v1#S0.F2)
2. 把射线特征注入图像 token，得到同时包含外观和观看几何的表示。[S15](https://arxiv.org/html/2611.11798v1#S3.SS3.p3.3)
3. 按末端位置、朝向及夹爪宽度衡量状态相似性，拉近相似观测、推远不同观测。[S17](https://arxiv.org/html/2611.11798v1#S3.SS4.p1.1) [S18](https://arxiv.org/html/2611.11798v1#S3.SS4.p2.5)
4. 联合动作模仿训练；部署时将学到的表示交给策略预测未来动作。[S6](https://arxiv.org/html/2611.11798v1#S1.p4.1) [S13](https://arxiv.org/html/2611.11798v1#S3.SS1.p2.1)

### 必要术语

- 本体感知：机器人测得的自身状态；本文用末端位置、朝向和夹爪宽度提供对齐依据。
- Plücker 坐标：描述空间直线方向与位置的方式；本文用来编码相机射线。
- 对比学习：让指定的相似样本表示接近、不同样本远离；本文的相似依据来自机器人状态。

## 证据

仿真覆盖 MimicGen、双臂 AlohaGym 和语言条件 LIBERO。LIBERO 中，SmolVLA 的平均成功率从无射线 BC 的 81.4%、有射线 BC 的 83.3%，升至 PAIR 加射线的 88.9%；结果采用三个种子、每种子五个检查点中的最高成功率。[S34](https://arxiv.org/html/2611.11798v1#S4.T4) [S35](https://arxiv.org/html/2611.11798v1#S4.T4.8.1) 真机为 FR3 三项桌面任务，每项每设置测试 30 次，最终完成率平均 57.8%，比无射线 BC 高 26.7 个百分点。[S39](https://arxiv.org/html/2611.11798v1#S4.SS6.p1.1) 这些支持所测相机变化下的收益，不能外推到任意遮挡或持续移动相机。

## 局限

作者明确指出效果依赖训练视角多样性，标定和采集增加成本，对齐也增加训练开销。[S41](https://arxiv.org/html/2611.11798v1#S6.p1.1) 我的待核查问题是：机器人姿态相似而物体位置不同，会不会被过度拉近？此外，本文假设相机在单次任务内固定。[S12](https://arxiv.org/html/2611.11798v1#S3.SS1.p1.1)

- **判断**：值得读方法和消融：重点是射线与本体状态如何互相补足，而最高检查点口径需要在比较时保留。

## 研究关联

值得借鉴的是：先让表示知道“这个像素从哪里看过来”，再要求它跨视角一致。已有相机标定和机器人状态、且部署视角会变化时，这比单独要求图像不变更有依据。

### 下一步读哪里

先看射线注入与状态配对规则。[S2](https://arxiv.org/html/2611.11798v1#S0.F2) [S17](https://arxiv.org/html/2611.11798v1#S3.SS4.p1.1) [S18](https://arxiv.org/html/2611.11798v1#S3.SS4.p2.5) 再核查未提供的相似度权重、损失权重、视角采样范围和检查点选择流程；用 [S33](https://arxiv.org/html/2611.11798v1#S4.T3.8.1) [S35](https://arxiv.org/html/2611.11798v1#S4.T4.8.1) 分开比较“只加射线”“只做对齐”和两者结合。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.11798v1
- 获取时间：2026-11-11T00:09:11.741499+00:00
- [S1] [PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation · 正文段落 1](https://arxiv.org/html/2611.11798v1#abstract1.1)
- [S2] [PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation · 正文段落 2](https://arxiv.org/html/2611.11798v1#S0.F2)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2611.11798v1#S1.p1.1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2611.11798v1#S1.p2.1)
- [S5] [I Introduction · 正文段落 5](https://arxiv.org/html/2611.11798v1#S1.p3.1)
- [S6] [I Introduction · 正文段落 6](https://arxiv.org/html/2611.11798v1#S1.p4.1)
- [S7] [I Introduction · 正文段落 7](https://arxiv.org/html/2611.11798v1#S1.p5.1)
- [S8] [II-A Vision Representations for Robotic Manipulation · 正文段落 8](https://arxiv.org/html/2611.11798v1#S2.SS1.p1.1)
- [S9] [II-A Vision Representations for Robotic Manipulation · 正文段落 9](https://arxiv.org/html/2611.11798v1#S2.SS1.p2.1)
- [S10] [II-B Rays as Positional Embeddings · 正文段落 10](https://arxiv.org/html/2611.11798v1#S2.SS2.p1.1)
- [S11] [III Method · 正文段落 11](https://arxiv.org/html/2611.11798v1#S3.p1.1)
- [S12] [III-A Problem Statement · 正文段落 12](https://arxiv.org/html/2611.11798v1#S3.SS1.p1.1)
- [S13] [III-A Problem Statement · 正文段落 13](https://arxiv.org/html/2611.11798v1#S3.SS1.p2.1)
- [S14] [III-C Ray Positional Encoding · 正文段落 26](https://arxiv.org/html/2611.11798v1#S3.SS3.p1.4)
- [S15] [III-C Ray Positional Encoding · 正文段落 32](https://arxiv.org/html/2611.11798v1#S3.SS3.p3.3)
- [S16] [III-C Ray Positional Encoding · 正文段落 33](https://arxiv.org/html/2611.11798v1#S3.F3)
- [S17] [III-D Supervised Contrastive Learning · 正文段落 34](https://arxiv.org/html/2611.11798v1#S3.SS4.p1.1)
- [S18] [III-D Supervised Contrastive Learning · 正文段落 45](https://arxiv.org/html/2611.11798v1#S3.SS4.p2.5)
- [S19] [IV Experiments · 正文段落 48](https://arxiv.org/html/2611.11798v1#S4.p1.1)
- [S20] [IV Experiments · 正文段落 49](https://arxiv.org/html/2611.11798v1#S4.I1.ix1)
- [S21] [IV Experiments · 正文段落 50](https://arxiv.org/html/2611.11798v1#S4.I1.ix2)
- [S22] [IV Experiments · 正文段落 51](https://arxiv.org/html/2611.11798v1#S4.I1.ix3)
- [S23] [IV-A Benchmarks · 正文段落 53](https://arxiv.org/html/2611.11798v1#S4.SS1.SSS0.Px1.p1.1)
- [S24] [IV-A Benchmarks · 正文段落 54](https://arxiv.org/html/2611.11798v1#S4.SS1.SSS0.Px2.p1.1)
- [S25] [IV-A Benchmarks · 正文段落 55](https://arxiv.org/html/2611.11798v1#S4.SS1.SSS0.Px3.p1.1)
- [S26] [IV-A Benchmarks · 正文段落 57](https://arxiv.org/html/2611.11798v1#S4.T1)
- [S27] [IV-A Benchmarks · 正文段落 59](https://arxiv.org/html/2611.11798v1#S4.T1.5.2)
- [S28] [IV-B Policy Architectures · 正文段落 62](https://arxiv.org/html/2611.11798v1#S4.SS2.p1.1)
- [S29] [IV-B Policy Architectures · 正文段落 63](https://arxiv.org/html/2611.11798v1#S4.SS2.SSS0.Px1.p1.1)
- [S30] [IV-B Policy Architectures · 正文段落 64](https://arxiv.org/html/2611.11798v1#S4.T2)
- [S31] [IV-B Policy Architectures · 正文段落 65](https://arxiv.org/html/2611.11798v1#S4.T2.5.1)
- [S32] [IV-B Policy Architectures · 正文段落 66](https://arxiv.org/html/2611.11798v1#S4.T3)
- [S33] [IV-B Policy Architectures · 正文段落 67](https://arxiv.org/html/2611.11798v1#S4.T3.8.1)
- [S34] [IV-B Policy Architectures · 正文段落 68](https://arxiv.org/html/2611.11798v1#S4.T4)
- [S35] [IV-B Policy Architectures · 正文段落 69](https://arxiv.org/html/2611.11798v1#S4.T4.8.1)
- [S36] [IV-D Training/Evaluation Protocol · 正文段落 75](https://arxiv.org/html/2611.11798v1#S4.SS4.p1.1)
- [S37] [IV-D Training/Evaluation Protocol · 正文段落 76](https://arxiv.org/html/2611.11798v1#S4.SS4.p2.1)
- [S38] [IV-E Simulation Results · 正文段落 77](https://arxiv.org/html/2611.11798v1#S4.SS5.p1.1)
- [S39] [IV-F Real-World Experiments · 正文段落 78](https://arxiv.org/html/2611.11798v1#S4.SS6.p1.1)
- [S40] [IV-F Real-World Experiments · 正文段落 79](https://arxiv.org/html/2611.11798v1#S4.F4)
- [S41] [VI Conclusion · 正文段落 95](https://arxiv.org/html/2611.11798v1#S6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-11/PAIR Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manip.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While imitation learning has made substantial progress toward generalizable robot manipulation through scaling, viewpoint robustness remains a major bottleneck. Visuomotor policies rely heavily on visual inputs, yet images provide an inherently ambiguous signal under viewpoint change: similar scenes may appear markedly different across viewpoints, while distinct states may share certain visual overlaps. A policy must therefore infer not only the task-relevant state, but also how it is visually projected under a particular camera configuration. This entanglement of viewpoint-dependent appearance and task-relevant state can make learning inefficient and limit generalization to unseen viewpoints. Recent work has begun to address this challenge through camera-ray conditioning and representation learning using geometric cues to induce invariance. However, providing camera information as additional context does not by itself ground visual representations in how the task scene is visually projected, while geometric alignment without camera context can introduce spurious correspondences by ignoring viewpoint-dependent projection. We propose PAIR, a contrastive learning framework that aligns joint image-ray representations using robot proprioception. PAIR encourages observations with similar robot states to remain close in representation space across viewpoints, providing a structured grounding signal for learning viewpoint-robust features. PAIR is a highly adaptable framework: it can be used to train Diffusion Policy (DP) or post-train vision-language-action (VLA) models. In simulated and real-world manipulation benchmarks with camera variation, PAIR consistently outperforms the behavior cloning baseline without ray conditioning by 12.7% and 26.7% points, respectively, demonstrating stronger generalization to unseen viewpoints. Project website: PAIRrobot.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.11798v1
- Authors: Sung-Wook Lee, Xuhui Kang, Dylan Losey, Yen-Ling Kuo
- Published: 2026-11-09T02:54:44Z
- Age days: 1

</details>
