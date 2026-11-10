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
url: "https://arxiv.org/abs/2611.08698v1"
published: "2026-11-05T20:54:52Z"
age_days: 4
score: 42
created: 2026-11-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> VICTR 让机器人从示范里找“现在这一步该参考哪一段”，而不只找画面最像的一段。IC-VFE 同时看参考示范、指令和当前观察，估计任务进度，再检索相应阶段的片段帮助 π₀.₅ 生成动作。

## 问题

新任务反复微调成本高，因此已有方法把检索到的示范片段放进策略上下文。但同一场景在抓取前后可能非常相似，视觉最近的片段未必对应当前执行阶段。[S4](https://arxiv.org/html/2611.08698v1#S1.p2.1) 单靠指令估计进度，也要求模型事先理解新任务；参考示范则能具体告诉它任务如何展开。

### 用一个例子理解

理解用例（非论文实验）：输入“把圆环套上柱子”、当前图像和示范池；IC-VFE 判断当前已经抓住圆环，检索接近柱子的片段，策略据此生成下一段动作，而不是取回画面相似的抓取前片段。

## 创新点或方法

旧做法按视觉相似度检索；VICTR 先用参考视频建立任务进度坐标，再按阶段选示范，也可融合视觉相似度。[S12](https://arxiv.org/html/2611.08698v1#S3.F2) IC-VFE 用语义进度标注训练，策略则用真实进度检索出的上下文学习动作生成。部署时两者权重固定，改用估计进度检索。[S15](https://arxiv.org/html/2611.08698v1#S3.SS4.p1.1) 每个任务提供一个示范池，最短示范作进度参考，全部示范提供候选片段；“不用新任务微调”仍需要新任务示范。[S14](https://arxiv.org/html/2611.08698v1#S3.SS1.p2.1)

### 方法如何工作

1. 为任务准备示范池并切成动作块，选最短示范作参考，为新任务提供执行过程。
2. IC-VFE 对当前观察和候选片段估计相对进度，建立可比较的阶段位置。
3. 检索进度接近的片段，可加入视觉匹配，减少阶段相同但空间状态不同的问题。
4. 策略结合当前状态和检索上下文生成动作，执行后重新估计进度，全程无需更新参数。

### 必要术语

- 上下文学习：部署时从输入示例调整行为；本文不为新任务更新模型参数。
- IC-VFE：结合参考示范估计进度的模型；本文用其输出驱动检索。
- 任务进度：按语义里程碑衡量完成程度；本文不把它简单等同于经过时间。
- 域外任务：训练时未见的任务；本文包括新物体、技能组合和语义迁移，仍在同一环境。

## 证据

测试使用固定配置的 YOR 双臂真机，含 8 个域内和 8 个域外任务，每任务 10 次运行。[S17](https://arxiv.org/html/2611.08698v1#S4.p2.1) [S18](https://arxiv.org/html/2611.08698v1#S4.p3.1) [S24](https://arxiv.org/html/2611.08698v1#S4.p8.1) 摘要报告域外成功率从微调 π₀.₅ 的 6.2% 到 23.8%，进度从 28.9% 到 55.5%。但 [S9](https://arxiv.org/html/2611.08698v1#S1.I1.i3) 另报成功率 2.7%／15.0%／25.0%，[S3](https://arxiv.org/html/2611.08698v1#S1.F1) 的进度数字也不同，节选未解释口径差异。这些结果支持该设置下进度检索有帮助，精确增益必须核对。

## 局限

作者明确承认域外绝对成功率仍低，所有实验处于同一物理环境，整段视频压缩还会牺牲空间细节。[S26](https://arxiv.org/html/2611.08698v1#S5.p1.1) 因此域外任务不能解读为新环境泛化；进度估计也不是经校准的成功概率。[S11](https://arxiv.org/html/2611.08698v1#S2.p2.1)

- **判断**：值得读透进度估计与检索接口，但应先核对互相不一致的主结果数字，再判断提升幅度。

## 研究关联

检索的相似性应该服务于下一步决策：当任务包含状态转换时，“做到哪一步”可能比“长得多像”更有用。可以借鉴先学习阶段对齐，再让动作模型参考片段，而不是直接复制示范动作。

### 下一步读哪里

从 [S14](https://arxiv.org/html/2611.08698v1#S3.SS1.p2.1) [S15](https://arxiv.org/html/2611.08698v1#S3.SS4.p1.1) 查清参考视频、候选片段和训练进度标签的区别，再核对 [S3](https://arxiv.org/html/2611.08698v1#S1.F1) [S9](https://arxiv.org/html/2611.08698v1#S1.I1.i3) [S24](https://arxiv.org/html/2611.08698v1#S4.p8.1) [S26](https://arxiv.org/html/2611.08698v1#S5.p1.1) 的统计口径。重点检查进度误差如何影响检索、融合视觉是否更稳，以及示范采集成本。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.08698v1
- 获取时间：2026-11-10T00:15:39.059557+00:00
- [S1] [VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models · 正文段落 1](https://arxiv.org/html/2611.08698v1#abstract1.1)
- [S2] [I Introduction · 正文段落 2](https://arxiv.org/html/2611.08698v1#S1.p1.1)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2611.08698v1#S1.F1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2611.08698v1#S1.p2.1)
- [S5] [I Introduction · 正文段落 5](https://arxiv.org/html/2611.08698v1#S1.p3.1)
- [S6] [I Introduction · 正文段落 6](https://arxiv.org/html/2611.08698v1#S1.p4.1)
- [S7] [I Introduction · 正文段落 8](https://arxiv.org/html/2611.08698v1#S1.I1.i1)
- [S8] [I Introduction · 正文段落 9](https://arxiv.org/html/2611.08698v1#S1.I1.i2)
- [S9] [I Introduction · 正文段落 10](https://arxiv.org/html/2611.08698v1#S1.I1.i3)
- [S10] [II Related Work · 正文段落 11](https://arxiv.org/html/2611.08698v1#S2.p1.1)
- [S11] [II Related Work · 正文段落 12](https://arxiv.org/html/2611.08698v1#S2.p2.1)
- [S12] [III Methodology · 正文段落 14](https://arxiv.org/html/2611.08698v1#S3.F2)
- [S13] [III-A VICTR Overview · 正文段落 15](https://arxiv.org/html/2611.08698v1#S3.SS1.p1.1)
- [S14] [III-A VICTR Overview · 正文段落 18](https://arxiv.org/html/2611.08698v1#S3.SS1.p2.1)
- [S15] [III-D IC-VLA Training Objective · 正文段落 54](https://arxiv.org/html/2611.08698v1#S3.SS4.p1.1)
- [S16] [IV Experiments and Results · 正文段落 55](https://arxiv.org/html/2611.08698v1#S4.p1.1)
- [S17] [IV Experiments and Results · 正文段落 56](https://arxiv.org/html/2611.08698v1#S4.p2.1)
- [S18] [IV Experiments and Results · 正文段落 57](https://arxiv.org/html/2611.08698v1#S4.p3.1)
- [S19] [IV Experiments and Results · 正文段落 58](https://arxiv.org/html/2611.08698v1#S4.p4.1)
- [S20] [IV Experiments and Results · 正文段落 59](https://arxiv.org/html/2611.08698v1#S4.F4)
- [S21] [IV Experiments and Results · 正文段落 60](https://arxiv.org/html/2611.08698v1#S4.F5)
- [S22] [IV Experiments and Results · 正文段落 61](https://arxiv.org/html/2611.08698v1#S4.p6.1)
- [S23] [IV Experiments and Results · 正文段落 62](https://arxiv.org/html/2611.08698v1#S4.p7.1)
- [S24] [IV Experiments and Results · 正文段落 63](https://arxiv.org/html/2611.08698v1#S4.p8.1)
- [S25] [IV Experiments and Results · 正文段落 67](https://arxiv.org/html/2611.08698v1#S4.T1)
- [S26] [V Limitations and Future Work · 正文段落 83](https://arxiv.org/html/2611.08698v1#S5.p1.1)
- [S27] [V Limitations and Future Work · 正文段落 84](https://arxiv.org/html/2611.08698v1#S5.p2.1)
- [S28] [-B Pilot Study: GPT-6 Astra as an In-Context Policy · 正文段落 93](https://arxiv.org/html/2611.08698v1#A0.SS2.p1.1)
- [S29] [-B Pilot Study: GPT-6 Astra as an In-Context Policy · 正文段落 94](https://arxiv.org/html/2611.08698v1#A0.SS2.p2.1)
- [S30] [-B Pilot Study: GPT-6 Astra as an In-Context Policy · 正文段落 95](https://arxiv.org/html/2611.08698v1#A0.SS2.p3.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-10/VICTR Value-Informed In-Context Learning for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advances in robot foundation models have highlighted the potential of in-context learning (ICL) for adapting robot behavior from demonstrations without further fine-tuning. Previous work has used retrieval-based post-training to equip pretrained vision-language-action (VLA) models with the capability for ICL by teaching them to condition action predictions on retrieved visually-relevant demonstration chunks. However, the effectiveness of retrieval hinges on selecting context relevant to the current execution stage, which visual similarity alone may not capture. We introduce VICTR, a framework enabling in-context learning in VLAs via progress-informed context retrieval built around an In-Context Value Function Estimator (IC-VFE). IC-VFE conditions on a reference demonstration video, a language instruction and the current observation to estimate task-relative progress. By conditioning progress estimation on a reference demonstration, IC-VFE can align the current state with a demonstrated execution even for tasks unseen during training. VICTR uses the estimated progress to select demonstration chunks at corresponding stages of execution and supplies them to a $π_{0.5}$ policy post-trained for in-context action generation. On unseen out-of-domain real-world manipulation tasks, VICTR raises the success rate from 6.2% for a fine-tuned $π_{0.5}$ baseline to 23.8% and more than doubles the task progress rate, from 28.9% to 55.5%. Project page with code, data and videos: https://ai4ce.github.io/VICTR/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08698v1
- Authors: Luca Macesanu, Tianluo Zhang, Aditya Patil, Archit Sharma, Kevin Angers, Christopher M. Clark, Chen Feng, Juexiao Zhang
- Published: 2026-11-05T20:54:52Z
- Age days: 4

</details>
