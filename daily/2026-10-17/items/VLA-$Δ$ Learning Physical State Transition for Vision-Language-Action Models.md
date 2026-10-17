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
url: "https://arxiv.org/abs/2610.21306v1"
published: "2026-10-15T05:54:21Z"
age_days: 1
score: 35
created: 2026-10-17
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> VLA-Δ 在训练时明确教模型“当前到未来发生了什么物理变化”，再让它学习动作。推理时仍直接从当前观察生成动作，不需要额外预测一段未来再执行。

## 问题

直接用观察配示范动作训练，模型可能记住画面与动作的对应，却没有受到明确监督去区分动作造成的状态变化。已有语言推理或未来图像、潜变量预测虽然提供中间目标，摘要认为它们仍未直接监督物理状态转移本身。

### 用一个例子理解

理解用例（非论文实验）：输入抽屉画面与“拉开抽屉”；训练时同时提供抽屉由关闭到打开的变化目标和动作示范；部署时输入当前画面，直接输出拉动动作。

## 创新点或方法

旧做法监督“看到什么就做什么”，本文增加“状态怎样改变”的学习目标。作者构建大规模预训练数据，并生成覆盖任务相关语义与视觉运动变化的转移标注，试图让连续动作学习获得更直接的变化信号。关键区别是这些目标用于训练，推理不增加额外步骤。标注如何表示、由谁生成、怎样与动作损失结合，摘要均未说明，因此不能据此认定模型学到了完整物理动力学。

### 方法如何工作

1. 构建预训练数据，取得当前与未来状态之间可用于标注的变化信息。
2. 生成任务语义和视觉运动变化标签，把学习目标明确到状态转移。
3. 将转移监督用于动作学习；摘要只说明到此，未交代损失与网络连接。
4. 推理时从当前观察直接生成动作，省去额外中间预测流程。

### 必要术语

- 状态转移：当前状态到未来状态的变化；本文把它作为显式训练目标。
- 连续动作：位置等数值形式的控制输出；是转移监督要帮助学习的对象。
- 潜空间：模型内部的压缩表示空间；摘要用它说明部分已有未来预测方法的监督位置。

## 证据

摘要称，在 LIBERO 和 RoboTwin 上与当时最佳方法具有竞争力，真机实验超过 π₀.₅。它没有提供成功率、任务清单、试验次数或优势幅度，也没给出控制数据量后的对照。现有信息支持方法在这些评测中经过测试，但不足以判断收益大小、稳定性，或收益究竟来自转移监督还是新增预训练数据。

## 局限

我的首要待核查问题是“物理变化”具体包含哪些量。语义和视觉运动标注可能受到遮挡、视角变化影响，不能自动等同于接触力或因果动力学。摘要也不足以确认直接映射过拟合是否通过专门实验得到验证。

- **判断**：先读标注定义和受控消融；这是判断它提供了新监督信息，还是主要增加了数据的关键。

## 研究关联

可借鉴的是把动作学习的监督对象从动作标签扩展到动作所对应的变化。如果两张相似画面需要不同动作，明确区分“要让什么发生变化”可能比仅拟合示范动作更有帮助；前提是变化标注可靠且与控制相关。

### 下一步读哪里

下一步检查转移标注的时间跨度、坐标或语义表示，以及标注质量评估。实验上核查同数据、同算力下移除变化监督的结果，并查看真机相对 π₀.₅ 的逐任务差异。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/VLA-$Δ$ Learning Physical State Transition for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks. However, most VLAs directly map observations to demonstrated actions without explicit supervision of intermediate physical state changes, making them prone to overfitting observation-action correspondences. Some methods introduce intermediate reasoning or future-state prediction in language, visual, or latent spaces to guide action generation, but do not explicitly supervise the physical state transition itself. We therefore propose VLA-$Δ$, a general framework that uses physical changes between current and future states as explicit learning targets. To support this objective, we construct a large-scale pretraining dataset and derive physical state-transition annotations covering task-relevant semantics and visual motion changes, providing more direct supervision for continuous action generation. During inference, the model generates actions directly from current observations without additional inference overhead. VLA-$Δ$ achieves performance competitive with the state of the art on LIBERO and RoboTwin, and outperforms $π_{0.5}$ in real-robot experiments. Our code is available at https://github.com/ZJU-OmniAI/VLA-Delta

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21306v1
- Authors: Qi Lu, Jiarun Li, Ce Zhang, Miao Pan, Yi Pan, Xu Wang, Wenqi Zhang, Xuhong Zhang
- Published: 2026-10-15T05:54:21Z
- Age days: 1

</details>
