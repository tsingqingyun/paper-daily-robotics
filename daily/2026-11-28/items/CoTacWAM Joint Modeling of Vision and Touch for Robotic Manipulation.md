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
url: "https://arxiv.org/abs/2611.34117v1"
published: "2026-11-25T10:18:08Z"
age_days: 2
score: 25
created: 2026-11-28
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CoTacWAM: Joint Modeling of Vision and Touch for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> CoTacWAM 让腕部相机和触觉传感器共同描述夹爪附近发生的接触，同时保留各自独有的线索。模型用这些信息学习动作，并在独立检测器确认失败后据此修正。

## 问题

操纵接近物体时，腕部图像能看到局部几何，触觉能报告实际发生的接触。只依靠一路，可能看得见对齐情况却不知道是否碰到，也可能感到碰撞却看不清局部布局。当某一路信号缺失，策略还得利用剩下的输入继续工作。摘要未说明各个既有基线具体怎样融合这两路信号。

### 用一个例子理解

理解用例（非论文实验）｜夹爪把插销送入孔。头部相机给出工件位置，腕部图像显示插销与孔口的偏移，触觉显示插销是否已顶到孔边。策略用当前可用的证据给出下一步动作。若独立检测器判定插入失败，局部接触表示可以为下一次调整提供条件。

## 创新点或方法

CoTacWAM 把腕部视觉和触觉中指向同一次接触的线索联系起来，同时保留每路输入特有的证据。训练时，模型把这种局部表示与头部相机提供的全局场景信息一起用于预测式动作学习。推理时，动作可由当前可用的输入组合提供条件。若独立检测器判定一次尝试失败，这个表示还用于后续修正。如何构造共享表示、训练时如何处理缺失输入，以及修正动作怎样生成，摘要未说明。

### 方法如何工作

1. 用腕部图像获取局部几何，用触觉获取物理接触信号，为同一次交互提供互补证据。
2. 学习能联系两路信号共同含义的表示，同时保留各自独有的信息，使可用输入组合都能描述局部交互。
3. 将局部表示与头部视角的场景信息一起用于预测式动作学习，使策略兼顾接触和任务位置。
4. 部署时由独立检测器判定尝试是否失败，确认失败后用接触表示为修正动作提供条件。修正机制摘要只说明到此。

### 必要术语

- 共享接触语义：视觉与触觉对同一次接触提供的共同信息；模型用它联系两路观测。
- 模态独有证据：某种传感器特别能提供的信息；这里包括腕部视觉的局部几何和触觉记录的物理接触。

## 证据

摘要报告了四项真机任务。作者称，CoTacWAM 在常规操纵和局部输入缺失的评估中取得所测方法里的最佳表现，自主重试又带来进一步收益。摘要未列任务名称、基线名称、缺失了哪路输入、具体指标或变化幅度。结果支持所测任务内对输入缺失的鲁棒性，至于不同组件分别贡献多少，需要看对照设置。

## 局限

这里有真机证据，适用范围取决于四项任务及缺失设置。要判断共享接触表示是否带来提升，需要核对基线是否有同等传感器和重试预算，以及有无拆开比较融合方式、失败检测器和重试。缺失输入的表现也不能直接推到信号延迟或传感器误读。

- **判断**：值得读共享信息与独有信息的学习方式，再看缺失输入和重试的对照。这两处决定哪些收益可以归到接触表示。

## 研究关联

如果两个传感器观察的是同一次物理事件，可以同时利用它们的重合和互补信息。共享线索能让策略在一路缺失时保留部分判断依据，独有线索则有助于区分诸如看起来已对齐、实际却已顶住这样的情况。

### 下一步读哪里

查视觉与触觉怎样对齐到同一次接触、哪些监督保留各自独有的信息，再看缺失模式是否在训练中出现。读真机评估时，核对首次成功与允许重试后的结果如何统计。

- **概念**：视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：25
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/CoTacWAM Joint Modeling of Vision and Touch for Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present CoTacWAM, a world-action model that learns shared contact semantics between wrist vision and touch, achieving the best observed performance in our nominal manipulation and missing-input evaluations. The two modalities observe the same local interaction through different signals: wrist images reveal nearby geometry, while touch records physical contact. Our approach connects their common contact meaning while preserving the evidence unique to each modality, giving the policy a joint description of interaction across available input combinations. This representation supports predictive action learning alongside head-view scene context and conditions corrections after an independent detector confirms a failed attempt. Experiments across four real-world tasks demonstrate improved manipulation performance over the evaluated baselines, robustness to missing local observations, and further gains from autonomous retries.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34117v1
- Authors: Lei Jin, Yiding Ma, Zhuohang Li, Jiachen Liu, Zibo Zhu, Kairui Liu, Chen Gao, Wei Wu, Yong Li
- Published: 2026-11-25T10:18:08Z
- Age days: 2

</details>
