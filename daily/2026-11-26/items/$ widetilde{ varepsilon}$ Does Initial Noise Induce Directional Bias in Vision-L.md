---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.33816v1"
published: "2026-11-25T05:46:45Z"
age_days: 0
score: 31
created: 2026-11-26
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# $\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?

> [!summary] 这篇论文到底做了什么（基于摘要）
> 同样的观测和指令，换一次初始噪声，扩散式 VLA 生成的动作就可能整体偏向另一边。ε̃ 在训练时让正负噪声生成相近动作，在推理时去掉噪声沿时间维度的平均值。

## 问题

扩散式 VLA 从随机噪声出发，生成接下来一段连续动作。如果动作块持续往同一方向偏，等机器人执行出偏差再纠正，原来的操作机会可能已经错过。已有做法会搜索更有利的初始噪声，但负责生成动作的模型仍然对种子敏感。论文要处理的是这种敏感性，尤其是整段动作的方向偏移。

### 用一个例子理解

理解用例（非论文实验）。机械臂收到把插头送到插座前的指令，模型拿到相机画面和一段随机噪声。假设这份噪声在负责横向运动的维度上平均偏正，先从每个时间步减去该平均值，再让模型生成接近动作。输出仍是一整段运动指令。这里要理解的是采样时去掉了哪种共同偏移，动作能否对准仍由模型和观测决定。

## 创新点或方法

作者观察到，动作偏移的方向和初始噪声在时间上的平均方向高度一致。于是训练时，在相同条件下用 ε 和 −ε 两份初始噪声生成动作，并约束两份动作预测接近。两份噪声的时间均值方向相反，这个约束会惩罚随噪声翻转的动作差异。推理时则直接从噪声的每个时间步减去同一个时间均值，让噪声仍可逐步变化，但去掉整段共有的偏移。摘要未说明一致性施加在哪个预测量上，也未说明损失如何加权。

### 方法如何工作

1. 对同一组输入改变初始噪声，观察生成动作的偏移，并检查它是否与噪声的时间均值对齐。
2. 训练时成对使用 ε 和 −ε，约束两份动作预测接近，以减弱模型对噪声符号翻转的响应。
3. 推理时沿时间维度计算噪声均值，并从每步减掉它，再生成动作块，以去掉噪声中贯穿整段的偏移。

### 必要术语

- 对偶噪声：一份噪声和它逐元素取负后的副本。在本文中，两份输入用来构造一致性训练对。
- 噪声的时间均值：对动作块中各时间步的噪声取平均。在本文中，它表示初始噪声在各动作维度上的整段偏移。

## 证据

摘要报告，方法在仿真基准上减小了动作偏差并改善了任务表现，但没有给出基准名称、对比方法、动作偏差的定义或具体数值。真机实验中，π₀.₅ 的平均任务成功率由 40% 升至 68%，也是摘要给出的结果。这个对照支持整套方法在所测真机任务上有效，摘要没有拆开报告训练约束和推理去均值各自贡献了多少。

## 局限

摘要没有交代真机任务构成、重复次数或成功率波动。噪声均值与动作方向的对齐是一项观察，整套干预后的成功率是另一项结果。要判断去均值本身是否带来真机收益，以及噪声的其他时间结构是否也会引起偏差，还需看分别控制两项改动的实验。

- **判断**：值得读到噪声与动作偏移的测量定义以及两项改动的消融，因为这决定了只改采样能解决多少问题。

## 研究关联

如果同一输入换种子后，生成结果总是整段平移，值得检查误差是否集中在某个可直接测量的分量上。这里可以借鉴的是先定位动作对随机输入的哪一部分最敏感，再决定把约束加在训练还是采样环节。

### 下一步读哪里

先查作者如何从动作中定义方向偏移，以及如何测量它与噪声均值的对齐。再找原模型、只改训练、只改推理和两项合用的对照，并核查真机提高是否集中于少数任务。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/$ widetilde{ varepsilon}$ Does Initial Noise Induce Directional Bias in Vision-L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action models (VLAs) have widely adopted diffusion-based action generation for continuous robot motions, enabling fine-grained control across diverse tasks. However, recent studies have shown that their performance is highly sensitive to initial noise, with resulting action errors that make recovery difficult during execution. Existing approaches search for favorable noise initializations to improve performance, yet the action expert itself remains sensitive to noise. In this work, we reveal that initial noise induces a consistent directional bias in action space that closely aligns with the noise's temporal mean. We thus introduce a simple yet effective framework that improves robustness to initial noise through interventions during both training and inference. During training, we enforce consistent action predictions from antithetic noise pairs $(ε, -ε)$ and, at inference, remove the noise's temporal mean. Our method substantially reduces action deviation and improves task performance across simulation benchmarks. In real-robot experiments, our method increases the average task success rate of $π_{0.5}$ from 40% to 68%, with more stable and consistent execution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33816v1
- Authors: Junmyeong Lee, Dongmin Shin, Wooseok Jeon, JunGyu Lee, Seunghyun Shin, Hae-Gon Jeon
- Published: 2026-11-25T05:46:45Z
- Age days: 0

</details>
