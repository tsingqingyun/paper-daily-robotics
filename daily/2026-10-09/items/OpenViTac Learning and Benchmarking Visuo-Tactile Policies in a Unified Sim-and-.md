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
url: "https://arxiv.org/abs/2610.10384v1"
published: "2026-10-07T16:43:29Z"
age_days: 1
score: 40
created: 2026-10-09
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> OpenViTac 把需要触觉的操作做成对应的仿真与真机测试；OpenVTLA 则把短时间触觉历史编码成小量 token，直接送进已有 VLA。它让“触觉有没有帮助”和“怎样接入触觉”更容易分开检验。

## 问题

看得见物体不等于知道软硬、接触变化和受力。以往触觉方法使用不同传感器、任务和机器人，成绩难比较；纯视觉基准又不能检验这些能力 [S5](https://arxiv.org/html/2610.10384v1#S1.p2.1) [S6](https://arxiv.org/html/2610.10384v1#S1.p3.1)。

### 用一个例子理解

理解用例（非论文实验）：输入“轻拿一个软物体”、相机图像和连续触觉读数；历史编码呈现接触变化，VLA 联合理解后输出下一段动作，而不是只按物体外观决定操作。

## 创新点或方法

基准覆盖物性识别、易损物交互、接触操作和精密操作，并对齐两域任务与资产。模型比较从同一 π₀.₅ 出发，改变触觉表示和接入位置；OpenVTLA 选 AnyTouch2，将历史触觉投影后放到视觉 token 前，不另加触觉专家。训练是后训练，推理时共同处理视觉、语言与触觉；保留原通路不等于冻结全部参数，更新范围未说明。混合训练固定真实示范，按采样比例加入仿真示范，无需逐轨迹配对 [S20](https://arxiv.org/html/2610.10384v1#S3.SS2.p1.1) [S21](https://arxiv.org/html/2610.10384v1#S3.SS2.p2.1) [S22](https://arxiv.org/html/2610.10384v1#S3.SS2.p3.1) [S23](https://arxiv.org/html/2610.10384v1#S3.I1.ix1) [S24](https://arxiv.org/html/2610.10384v1#S3.I1.ix2) [S25](https://arxiv.org/html/2610.10384v1#S3.I1.ix3) [S26](https://arxiv.org/html/2610.10384v1#S3.I1.ix4) [S27](https://arxiv.org/html/2610.10384v1#S3.I1.ix5) [S28](https://arxiv.org/html/2610.10384v1#S3.SS2.p4.1) [S29](https://arxiv.org/html/2610.10384v1#S3.SS3.p1.1) [S30](https://arxiv.org/html/2610.10384v1#S3.SS3.p2.1) [S31](https://arxiv.org/html/2610.10384v1#S3.SS3.p3.1) [S32](https://arxiv.org/html/2610.10384v1#S3.E1) [S33](https://arxiv.org/html/2610.10384v1#S3.SS3.p3.2)。

### 方法如何工作

1. 建立任务对应的仿真和真机设置，并统一成功条件，使比较有共同含义。
2. 将短触觉历史压成 token，保留变化信息而不只看当前接触图。
3. 把 token 投影到 VLM 维度并前置，让原有动作通路利用触觉。
4. 固定真实数据与优化预算后加入仿真示范，检验额外仿真数据是否帮助真机学习。

### 必要术语

- VTLA：在视觉、语言到动作的策略里加入触觉；本文研究如何加入。
- Token 拼接：把触觉编码作为额外输入片段；让它进入原有模型处理。
- 仿真—真机对应：对齐任务和控制约定；不代表触觉读数完全相同。

## 证据

每个任务单独训练策略，平均值为任务成功率的等权平均 [S35](https://arxiv.org/html/2610.10384v1#S4.SS1.p2.1)。仿真 OpenVTLA 为 68.7%，FTP-1 为 61.2%，最强 VLA 为 51.5% [S37](https://arxiv.org/html/2610.10384v1#S4.T2.8)；真机为 54.6%、51.9% 和 43.1% [S39](https://arxiv.org/html/2610.10384v1#S4.T3.8)。七种方法在八个共享任务上的两域平均分 Pearson r=0.967，支持相对排序一致 [S42](https://arxiv.org/html/2610.10384v1#S4.SS2.p3.1)。输入有冲突：引言的 WAM 成绩为仿真 53.3%、真机 48.5%，所给表格及结果段却不一致，因此不采用这组比较。

## 局限

作者承认触觉渲染、传感器模型和校准仍有两域差距 [S47](https://arxiv.org/html/2610.10384v1#S5.p2.1)。精密操作收益也不稳定。融合表部分行同时换了编码器和融合方式，不能把差异完全归因于融合；高相关性不保证绝对成功率一致。

- **判断**：值得读基准协议与受控表示实验；要复现最佳接入方式，还需核查参数更新范围和比较条件。

## 研究关联

接触状态随时间变化，未必能从一帧触觉图判断。这里值得尝试的是先用适合触觉历史的表示，再检验简单拼接是否已经足够，避免先增加复杂融合结构。

### 下一步读哪里

优先看 [S21](https://arxiv.org/html/2610.10384v1#S3.SS2.p2.1) [S28](https://arxiv.org/html/2610.10384v1#S3.SS2.p4.1) [S44](https://arxiv.org/html/2610.10384v1#S4.SS3.p1.1) [S45](https://arxiv.org/html/2610.10384v1#S4.T4) [S46](https://arxiv.org/html/2610.10384v1#S4.T4.8)；核查各融合方案是否同编码器、同预算，以及混合训练的比例和实测增益，节选未提供这些结果。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.10384v1
- 获取时间：2026-10-09T00:15:44.164866+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.10384v1#p1.1)
- [S2] [OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework · 正文段落 2](https://arxiv.org/html/2610.10384v1#abstract1.1)
- [S3] [OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework · 正文段落 3](https://arxiv.org/html/2610.10384v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.10384v1#S1.p1.1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.10384v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.10384v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.10384v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.10384v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.10384v1#S1.I1.i1)
- [S10] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.10384v1#S1.I1.i2)
- [S11] [1 Introduction · 正文段落 14](https://arxiv.org/html/2610.10384v1#S1.I1.i3)
- [S12] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.10384v1#S2.p1.1)
- [S13] [2.1 Visuo-Tactile Robot Learning · 正文段落 16](https://arxiv.org/html/2610.10384v1#S2.SS1.p1.1)
- [S14] [2.2 Visuo-Tactile Datasets and Benchmarks · 正文段落 17](https://arxiv.org/html/2610.10384v1#S2.SS2.p1.1)
- [S15] [2.2 Visuo-Tactile Datasets and Benchmarks · 正文段落 18](https://arxiv.org/html/2610.10384v1#S2.F2.fig1)
- [S16] [2.2 Visuo-Tactile Datasets and Benchmarks · 正文段落 19](https://arxiv.org/html/2610.10384v1#S2.F2.fig2)
- [S17] [2.2 Visuo-Tactile Datasets and Benchmarks · 正文段落 20](https://arxiv.org/html/2610.10384v1#S2.F2.fig2)
- [S18] [2.2 Visuo-Tactile Datasets and Benchmarks · 正文段落 21](https://arxiv.org/html/2610.10384v1#S2.F2)
- [S19] [3.1 Benchmark · 正文段落 26](https://arxiv.org/html/2610.10384v1#S3.SS1.p4.1)
- [S20] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 28](https://arxiv.org/html/2610.10384v1#S3.SS2.p1.1)
- [S21] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 29](https://arxiv.org/html/2610.10384v1#S3.SS2.p2.1)
- [S22] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 30](https://arxiv.org/html/2610.10384v1#S3.SS2.p3.1)
- [S23] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 31](https://arxiv.org/html/2610.10384v1#S3.I1.ix1)
- [S24] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 32](https://arxiv.org/html/2610.10384v1#S3.I1.ix2)
- [S25] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 33](https://arxiv.org/html/2610.10384v1#S3.I1.ix3)
- [S26] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 34](https://arxiv.org/html/2610.10384v1#S3.I1.ix4)
- [S27] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 35](https://arxiv.org/html/2610.10384v1#S3.I1.ix5)
- [S28] [3.2 ADAPTING PRETRAINED VLAS TO TOUCH · 正文段落 36](https://arxiv.org/html/2610.10384v1#S3.SS2.p4.1)
- [S29] [3.3 Simulation–Real-World Co-training · 正文段落 37](https://arxiv.org/html/2610.10384v1#S3.SS3.p1.1)
- [S30] [3.3 Simulation–Real-World Co-training · 正文段落 38](https://arxiv.org/html/2610.10384v1#S3.SS3.p2.1)
- [S31] [3.3 Simulation–Real-World Co-training · 正文段落 39](https://arxiv.org/html/2610.10384v1#S3.SS3.p3.1)
- [S32] [3.3 Simulation–Real-World Co-training · 正文段落 40](https://arxiv.org/html/2610.10384v1#S3.E1)
- [S33] [3.3 Simulation–Real-World Co-training · 正文段落 41](https://arxiv.org/html/2610.10384v1#S3.SS3.p3.2)
- [S34] [4.1 Experimental Setup · 正文段落 42](https://arxiv.org/html/2610.10384v1#S4.SS1.p1.1)
- [S35] [4.1 Experimental Setup · 正文段落 43](https://arxiv.org/html/2610.10384v1#S4.SS1.p2.1)
- [S36] [4.1 Experimental Setup · 正文段落 44](https://arxiv.org/html/2610.10384v1#S4.T2)
- [S37] [4.1 Experimental Setup · 正文段落 45](https://arxiv.org/html/2610.10384v1#S4.T2.8)
- [S38] [4.1 Experimental Setup · 正文段落 46](https://arxiv.org/html/2610.10384v1#S4.T3)
- [S39] [4.1 Experimental Setup · 正文段落 47](https://arxiv.org/html/2610.10384v1#S4.T3.8)
- [S40] [4.2 Main Results · 正文段落 48](https://arxiv.org/html/2610.10384v1#S4.SS2.p1.1)
- [S41] [4.2 Main Results · 正文段落 49](https://arxiv.org/html/2610.10384v1#S4.SS2.p2.1)
- [S42] [4.2 Main Results · 正文段落 50](https://arxiv.org/html/2610.10384v1#S4.SS2.p3.1)
- [S43] [4.3 Understanding Tactile Adaptation in Pretrained VLAs · 正文段落 52](https://arxiv.org/html/2610.10384v1#S4.F4)
- [S44] [4.3 Understanding Tactile Adaptation in Pretrained VLAs · 正文段落 53](https://arxiv.org/html/2610.10384v1#S4.SS3.p1.1)
- [S45] [4.3 Understanding Tactile Adaptation in Pretrained VLAs · 正文段落 54](https://arxiv.org/html/2610.10384v1#S4.T4)
- [S46] [4.3 Understanding Tactile Adaptation in Pretrained VLAs · 正文段落 55](https://arxiv.org/html/2610.10384v1#S4.T4.8)
- [S47] [5 Conclusion, Limitations and Future Work · 正文段落 63](https://arxiv.org/html/2610.10384v1#S5.p2.1)
- [S48] [B.3 Data Collection Statistics · 正文段落 84](https://arxiv.org/html/2610.10384v1#A2.T2.st1)
- [S49] [B.3 Data Collection Statistics · 正文段落 86](https://arxiv.org/html/2610.10384v1#A2.T2.st2)
- [S50] [Appendix C Policy Implementation and Training Details · 正文段落 92](https://arxiv.org/html/2610.10384v1#A3.T4)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/OpenViTac Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world. However, despite the rapid progress of vision-tactile-language-action (VTLA) policies, there remains a lack of unified benchmarks for evaluating tactile-enabled robot manipulation across simulation and the real world. To address this gap, we introduce OpenViTac, a visuo-tactile manipulation benchmark for evaluating robot policies across simulation and the real world. OpenViTac organizes contact-rich manipulation into four tactile-relevant capability dimensions and provides paired simulation-real-world settings for consistent evaluation of VLA, WAM, and VTLA policies. Building upon this benchmark, we investigate how different tactile representations and integration strategies affect the performance of pretrained VLA models. Correspondingly, we introduce OpenVTLA, a tactile augmentation framework that combines the best-performing representation and integration strategy. Furthermore, we leverage the paired benchmark setting to study sim-real co-training and analyze factors affecting cross-domain policy learning. Together, OpenViTac provides a unified platform for evaluating and advancing visuo-tactile robot manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10384v1
- Authors: Yifan Wu, Qin Li, Nan Min, Guojin Zhong, Haoyu Zhao, Zhiyuan Li, Houze Xu, Shengqi Xu, Xingyao Lin, Zijie Diao, Zhaoxiang Liu, Shiguo Lian, Shunlin Lu, Shihao Zhao, Ziyi Ye, Zuxuan Wu, Yu-Gang Jiang
- Published: 2026-10-07T16:43:29Z
- Age days: 1

</details>
