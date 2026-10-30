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
url: "https://arxiv.org/abs/2610.37037"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-10-30
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception

> [!summary] 这篇论文到底做了什么（基于摘要）
> EvidenceConnect 用同一张图里的相关局部生成必须综合多处证据才能回答的问题，再用这些题训练出 ZwZ2。关键是既检查答案是否可信，也检查题目是否真的需要所选区域。

## 问题

空间理解和多模态长上下文任务都需要找到相关事实、认清事实属于谁，再把关系接起来，但直接为这些任务制作高质量训练数据很贵。本文尝试训练更容易合成数据的共同能力：连接证据，而不是逐个下游任务制作专门题库。

### 用一个例子理解

理解用例（非论文实验）：输入一张货架图和“哪层红盒子比蓝盒子多”；模型分别识别各层两种盒子、绑定层位、比较数量，输出层号。造题时可移除相关层区域，检查答案是否仍能被猜出。

## 创新点或方法

与直接围绕目标任务造题相比，EvidenceConnect 从单图的相关区域取得放大视图，生成比较、汇总或串联视觉证据的问题。独立 VLM 对答案达成一致才保留参考答案；随后移除选定区域，若问题依然能答对，就丢弃它，以减少只靠局部线索或捷径作答的题。训练阶段用这些数据做 RLVR，得到 ZwZ2。放大视图用于数据合成；摘要未说明推理是否裁图、如何输入图像，不能把标题当作实现细节。

### 方法如何工作

1. 从同一图像选取相关区域并获得放大视图，为细节明确且有关联的题目提供素材。
2. 生成需要比较、汇总或串联证据的问题，使回答必须处理区域间关系。
3. 用独立 VLM 的答案一致性筛选参考答案，降低错误监督的风险。
4. 移除选定区域测试问题，丢弃仍能作答的题，以筛除证据需求不足的样本。
5. 用保留数据进行 RLVR 训练得到 ZwZ2；摘要只说明到此，未交代奖励和优化细节。

### 必要术语

- 证据连接：找到视觉事实、绑定对象并组合关系；在本文中是希望跨任务迁移的能力。
- 区域消融：移除选定图像区域再测试；在本文中检查题目是否依赖这些证据。
- RLVR：使用可验证奖励的强化学习；在本文中用于训练基础 VLM，具体验证规则未说明。

## 证据

摘要报告细粒度与空间感知改善，并在具身空间推理、多模态长上下文、智能体任务和一般视觉推理上获得收益；合成数据没有针对这些下游基准定制。未提供具体基准、基础模型规模、比较方法、指标和数值，因而支持的是作者报告了跨任务收益，尚不能衡量幅度或确认各组件的贡献。

## 局限

多个模型同意答案仍可能共享错误，移除区域后答不出也不自动证明学会了正确推理。我会核查移除操作是否引入额外干扰，以及跨任务收益是否经过数据重叠和等训练预算控制；摘要没有提供这些信息。

- **判断**：值得细读造题和筛题流程，因为可迁移的核心经验在于怎样制造需要连接证据的监督，而不只是增加视觉问答数量。

## 研究关联

这里可借鉴的是先找多个任务共享的可训练动作，再为它造题。尤其是区域移除检查：题目提到了多处对象，不代表回答真的需要它们；训练数据应检查必要证据是否实际参与了求解。

### 下一步读哪里

优先核查区域如何选择、移除后怎样判断仍可作答、RLVR 奖励如何计算，以及取消答案共识或区域筛选后结果如何；再看跨任务评测是否覆盖不同基础模型。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/Zooming without Zooming v2 From Seeing Details to Connecting Evidence for Genera.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.37037v1 Announce Type: cross Abstract: Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for these tasks remains difficult and costly. Our key insight is that these tasks share an underlying capability, which we call connecting evidence: identifying relevant visual facts, binding them to the correct entities, recovering their relations, and composing them into an answer. Crucially, targeted training data are far easier to synthesize for this capability than for these tasks themselves. To strengthen this capability, we propose EvidenceConnect, an easy-to-implement data synthesis framework that uses zoomed views of related regions within a single image to generate questions requiring comparison, aggregation, or chaining of visual evidence. To ensure quality, a reference answer is retained only when independent VLMs agree on it, and region-ablation tests discard questions whose answer survives the removal of selected regions. We then train base VLMs on the resulting data with RLVR, obtaining Zooming without Zooming v2 (ZwZ2). Although the synthesized data are not tailored to any downstream benchmark, ZwZ2 improves fine-grained and spatial perception, with further gains on embodied spatial reasoning, multimodal long-context understanding, multimodal agent tasks, and general visual reasoning. These results establish EvidenceConnect as an effective framework for supervising evidence connection and suggest that strengthening this shared capability leads to more generalizable multimodal perception.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37037
- Authors: Lai Wei, Yatai Li, Liangbo He, Jun Lan, Renjie Gu, Linhan Cao, Junkai Lin, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
