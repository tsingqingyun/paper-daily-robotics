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
url: "https://arxiv.org/abs/2609.37655v1"
published: "2026-09-29T14:17:49Z"
age_days: 0
score: 31
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "Sim2Real", "具身智能评测与基准"]
---

# Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding

> [!summary] 这篇论文到底做了什么（基于摘要）
> 想批量教模型判断“谁离门更近”，就别让大模型自己猜答案。Exemplar2VQA 给它几个题目样例，让智能体写代码调用几何工具，在仿真场景中算出答案，再拿这些问答训练视觉模型。

## 问题

任务是为多模态模型提供复杂且可扩展的三维空间问答训练数据。人工标注成本高，直接让 LLM 编写问答又容易算错几何关系，导致规模扩大时正确性难保证；本文尝试同时处理数据数量与答案可靠性。

### 用一个例子理解

理解用例（非论文实验）：输入范例“哪把椅子离门最近？”及一个仿真房间→智能体生成调用位置与距离函数的代码→程序计算各候选距离→输出房间图像、问题和答案，供视觉问答模型训练。

## 创新点或方法

旧做法由人逐条标注或让 LLM 直接生成答案；本文让协作智能体围绕静态、以物体为中心的查询范例编写生成代码，并调用几何工具库算出结果。范例规定问题形式，程序负责空间运算，再扩展到大量仿真样本。训练阶段用生成的室内合成数据微调 Qwen2.5-VL；问答模型推理时如何使用这些能力，摘要未描述额外流程，也未说需要保留多智能体生成系统。

### 方法如何工作

1. 从静态空间查询范例确定问题模式，使生成任务有明确的语义目标。
2. 协作智能体结合几何工具库编写代码，把需要精确计算的部分交给程序。
3. 在仿真环境执行代码并扩展问答样本，形成合成训练数据；自动质检细节摘要未说明。
4. 用室内合成数据微调视觉语言模型，再在不同场景基准测试，检查能力是否超出训练环境。

### 必要术语

- Exemplar：用来示范问题形式的样例；本文以此启动和扩展数据生成。
- 确定性执行：按固定程序计算结果；本文用它替代语言模型直接猜几何答案。
- Sim2Real：把仿真中获得的能力迁移到真实数据或环境；本文摘要主要提供空间问答迁移层面的描述。

## 证据

摘要报告，仅使用该框架生成的室内合成数据微调 Qwen2.5-VL 3B/7B，在多种基准上取得显著提升，并扩展到室外和混合场景基准。但未提供基准名称、分数、对比方法、数据规模及重复实验，因此无法估计收益大小。结果支持合成空间问答训练具有迁移价值；作者将其定位为缩小 Sim2Real 差距，摘要本身未给机器人闭环控制证据。

## 局限

作者明确说明：摘要未列出；它明确描述的是静态、物体中心问题。我的待核查问题：代码错误如何发现，范例多样性是否限制问题范围，以及模型是否学到模板捷径。确定性执行只保证相同输入得到相同结果，不能自动保证程序和场景标注正确。

- **判断**：缺空间理解训练数据，值得看它的生成代码和质检办法。摘要称只用室内合成数据也改善了室外问答，但没有给出提升数字，也没有验证机器人实际操作。

## 研究关联

如果需要大量有标准答案的空间题，可以让语言模型负责出题、程序负责算答案。前提是拿得到可信的场景坐标，也要检查代码有没有把题意写错；否则只是把人工标注错误换成了批量程序错误。

### 下一步读哪里

下一步核查智能体分工、可访问的场景真值、几何工具支持范围、错误程序筛查和数据去重；迁移实验需查看真实图像来源、测试题型及其与生成模板的重合度。

- **概念**：多模态基础模型 智能体 Agent Sim2Real 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Exemplar2VQA A Scalable Exemplar-Driven Visual Question Answering Generation Fra.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Advancing spatial intelligence in Multimodal Large Language Models (MLLMs) is bottlenecked by the scarcity of complex, scalable 3D question-answer (QA) data. While manual annotation is labor-intensive, directly utilizing LLMs to synthesize these QA pairs often fails due to their inherent deficiencies in spatial and geometric computation. We introduce Exemplar2VQA, a scalable exemplar-driven visual question answering generation framework that rapidly synthesizes large-scale spatial QA pairs in simulated environments via multi-agent coding. By equipping collaborative agents with a meticulously designed library of geometric utilities, Exemplar2VQA bypasses LLMs' spatial reasoning flaws through deterministic code execution. Crucially, the framework exhibits remarkable versatility: taking diverse static object-centric spatial query templates as exemplars, it seamlessly and autonomously scales them into massive, high-fidelity synthetic datasets. Fine-tuning Qwen2.5-VL (3B/7B) exclusively on Exemplar2VQA-generated synthetic indoor data yields significant performance improvements across various diverse benchmarks. Furthermore, its effectiveness is not limited to in-domain indoor datasets but also robustly extends to outdoor and mixed-scene benchmarks. These results establish Exemplar2VQA as a scalable and powerful paradigm for bridging the sim-to-real gap in Embodied AI. Our code is at https://github.com/yingjiayu12/Exemplar2VQA

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37655v1
- Authors: Jiayu Ying, Qijian Tian, Ruijie Xu, Xinnan Zhu, Daoguo Dong, Jiachen Xu, Xin Tan
- Published: 2026-09-29T14:17:49Z
- Age days: 0

</details>
