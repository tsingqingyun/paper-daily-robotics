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
url: "https://arxiv.org/abs/2610.37037v1"
published: "2026-10-27T11:11:53Z"
age_days: 1
score: 27
created: 2026-10-29
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception

> [!summary] 这篇论文到底做了什么（基于摘要）
> ZwZ2 通过训练模型把图中不同位置的事实接起来，改善多模态理解。关键是 EvidenceConnect：用局部放大图生成必须比较、汇总或串联多处证据的问题，再筛掉答案不可靠或无需这些证据的问题。

## 问题

空间判断和多模态长上下文理解，都需要找到相关事实、认准事实属于谁，再组合关系作答；直接为这些任务制作高质量训练数据很贵。本文把训练目标移到它们共享的“连接证据”能力上。摘要没有说明具体哪种既有数据合成方法失败，明确指出的是定向数据难做、成本高。

### 用一个例子理解

理解用例（非论文实验）：输入一张货架图和问题“红盒与蓝盒中，哪个更靠近标价最低的商品？”模型先识别价格及对应商品，再定位两个盒子并比较距离，最后输出盒子名称；只认颜色或只读价格都不够。

## 创新点或方法

旧思路是围绕下游任务造题；本文改为围绕单张图中有关联的区域造题，训练可复用的证据组合能力。合成时使用放大视图辅助出题，用独立 VLM 的答案一致性筛查参考答案，再移除选定区域：如果仍能答对，就丢弃该题。随后以这些数据进行 RLVR 训练。放大视图明确用于数据合成；训练输入的具体组织、推理时是否存在额外裁图流程，摘要未说明，不能仅凭方法名判断。

### 方法如何工作

1. 从单张图选取相关区域并生成放大视图，让出题过程能利用局部细节。
2. 围绕区域之间的比较、汇总或关系链生成问答，使答案需要组合事实。
3. 用独立 VLM 的一致性检查答案，再用区域移除测试剔除证据依赖不足的问题。
4. 用保留数据进行 RLVR 训练得到 ZwZ2，再检查能力能否迁移到未定向合成数据的任务；具体训练配置摘要未说明。

### 必要术语

- 连接证据：找到事实、对应实体并组合关系；它是本文希望跨任务复用的训练目标。
- 区域消融：移除选定图像区域后重新检查答案；用于筛除不依赖这些区域的问题。
- RLVR：用可验证奖励进行强化学习；本文用于问答数据训练，但奖励实现未说明。

## 证据

摘要报告了细粒度感知、空间感知，以及具身空间推理、多模态长上下文、智能体任务和一般视觉推理上的改善，并称合成数据未针对下游基准定制。但没有给出基准名称、模型规模、对比设置、指标或增幅。因此目前支持“作者报告跨任务收益”，还不能判断收益大小，也不能确认是哪项筛选机制带来的。

## 局限

多个模型同意一个答案，并不保证答案正确；移除区域后答不出，也不足以证明模型学会了预期的关系推理。这是我会核查的有效性问题。摘要中的跨任务改善，也不能直接外推为真实机器人执行能力提高。

- **判断**：值得细读数据生成和筛选部分；它最可借鉴的是如何制造并检验证据依赖，效果强度则需看完整实验。

## 研究关联

值得借鉴的是，把昂贵的任务数据需求拆成一个更容易合成的共享能力。若多个任务都卡在组合分散事实，可以先训练这种组合动作；区域移除测试还提供了一个具体检查：题目是否真的需要指定证据。

### 下一步读哪里

我会先核查区域如何关联、移除后如何判定答案仍成立，以及 RLVR 的奖励与训练输入；再看等量数据对照、筛选消融和各类任务分别改善多少。当前没有正文节选可定位。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Zooming without Zooming v2 From Seeing Details to Connecting Evidence for Genera.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for these tasks remains difficult and costly. Our key insight is that these tasks share an underlying capability, which we call connecting evidence: identifying relevant visual facts, binding them to the correct entities, recovering their relations, and composing them into an answer. Crucially, targeted training data are far easier to synthesize for this capability than for these tasks themselves. To strengthen this capability, we propose EvidenceConnect, an easy-to-implement data synthesis framework that uses zoomed views of related regions within a single image to generate questions requiring comparison, aggregation, or chaining of visual evidence. To ensure quality, a reference answer is retained only when independent VLMs agree on it, and region-ablation tests discard questions whose answer survives the removal of selected regions. We then train base VLMs on the resulting data with RLVR, obtaining Zooming without Zooming v2 (ZwZ2). Although the synthesized data are not tailored to any downstream benchmark, ZwZ2 improves fine-grained and spatial perception, with further gains on embodied spatial reasoning, multimodal long-context understanding, multimodal agent tasks, and general visual reasoning. These results establish EvidenceConnect as an effective framework for supervising evidence connection and suggest that strengthening this shared capability leads to more generalizable multimodal perception.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37037v1
- Authors: Lai Wei, Yatai Li, Liangbo He, Jun Lan, Renjie Gu, Linhan Cao, Junkai Lin, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang
- Published: 2026-10-27T11:11:53Z
- Age days: 1

</details>
