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
url: "https://arxiv.org/abs/2610.21910v1"
published: "2026-10-15T13:59:15Z"
age_days: 2
score: 28
created: 2026-10-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness

> [!summary] 这篇论文到底做了什么（基于摘要）
> CoWorld Reasoner 让视觉语言模型遇到看不清、看不全的问题时，自己决定是否调用视频世界模型补充视觉内容，并选择怎样生成、怎样使用。它还根据执行反馈修改工具、技能说明和代码，两个模型本身都不更新权重。

## 问题

任务是从图像中推断运动、动作和视角变化，包括画面没有直接展示的情况。现有方法通常预先规定一种想象方式，例如始终生成新视角；但不同问题缺少的证据不同，固定流程限制了视频世界模型的用途。

### 用一个例子理解

理解用例（非论文实验）：输入一张被桌沿遮挡的物体照片，询问另一侧是否有把手；模型判断缺少视角信息，选择生成新视角，再结合生成内容回答并保留不确定性。这个例子也说明，想象出的把手不能直接当作真实观测。

## 创新点或方法

旧做法先定好生成流程，再让模型按流程回答；本文把多种视觉操作做成工具，用技能说明指导 VLM 判断是否需要想象、选什么操作、如何写生成请求及解释结果。另一个改动是根据执行反馈共同修订这些工具、说明和执行代码。这里的适应发生在运行机制层面，模型权重固定。推理时则按当前问题调用工具；摘要未说明具体操作清单、反馈来源和修订算法。

### 方法如何工作

1. 读取问题和已有图像，判断缺少哪类信息，以决定是否需要补充视觉内容。
2. 依照技能说明选择视觉操作并构造生成请求，让视频世界模型产出相关内容。
3. 解释生成内容并结合原始输入作答；摘要未说明证据冲突时如何处理。
4. 在演化阶段利用执行反馈修改工具、技能和代码，使后续调用方式发生变化，同时保持模型权重固定。

### 必要术语

- 视频世界模型：生成视觉变化的模型；本文把它用作补充推理材料的工具。
- Harness：连接模型、工具和执行规则的运行机制；本文主要修改这一层。
- 共同演化：依据反馈一起修订工具、技能与代码；本文不指两个模型共同更新权重。

## 证据

摘要报告七个基准，覆盖空间、时间与因果、感知推理，均与相同 VLM 的直接推理比较。最强版本在七项上都提高，MMSI、ERQA 的准确率相对增幅分别为 11.8%、13.0%，不是增加同等百分点；还在五项基准上超过五种使用相同骨干的演化基线。摘要未给绝对准确率、调用成本和各项消融，因此支持整体系统有效，尚不能单独确认哪种操作贡献最大。

## 局限

生成画面也可能把错误假设画得更可信。我的待核查问题是：系统怎样处理生成内容与原图冲突、怎样拒绝无用想象，以及收益能否抵消额外耗时。摘要中的因果推理成绩也不等于生成画面提供了真实干预证据。

- **判断**：值得细读工具调用与执行反馈部分，因为关键在于如何控制想象过程，而摘要还不足以复现这种控制。

## 研究关联

值得借鉴的是把“缺什么证据”变成显式决策。如果任务确实受限于视角或时间信息，可以研究让模型选择补充方式，而不是给每道题附加相同的生成步骤。

### 下一步读哪里

先核查工具支持哪些操作、技能如何约束调用，再看共同修订流程如何避免对评测题过拟合；实验优先找固定工具与演化工具的比较，以及生成次数、延迟和错误案例。

- **概念**：多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/CoWorld Reasoner Agentic Multimodal Reasoning with the Evolving Video World Mode.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating task-relevant visual content as additional evidence. However, existing approaches typically invoke a VWM through fixed pipelines centered on a predefined form of visual imagination, such as novel-view synthesis. To support flexible visual imagination for diverse reasoning tasks, we introduce CoWorld Reasoner, an agentic framework that uses a VWM as a unified visual reasoning engine. Its Video World Model-Driven Harness exposes multiple visual operations through tools and uses skills to guide the VLM in deciding whether to imagine, selecting an operation, constructing a generation request, and interpreting the resulting visual evidence. We further introduce VLM-VWM Harness Co-Evolution, which jointly revises tools, skills, and execution code based on execution feedback while keeping both model weights fixed. Across seven benchmarks spanning spatial intelligence, temporal and causal reasoning, and perceptual reasoning, CoWorld Reasoner outperforms direct reasoning with the same VLM. The strongest variant improves on all seven benchmarks, including relative accuracy gains of 11.8% on MMSI and 13.0% on ERQA, and outperforms all five evolving baselines using the same backbone across five benchmarks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21910v1
- Authors: Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li
- Published: 2026-10-15T13:59:15Z
- Age days: 2

</details>
