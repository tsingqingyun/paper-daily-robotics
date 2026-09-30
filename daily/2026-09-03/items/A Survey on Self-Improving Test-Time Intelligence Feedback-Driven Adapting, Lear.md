---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.01679v1"
published: "2026-09-01T11:41:39Z"
age_days: 1
score: 28
created: 2026-09-03
concepts: ["多模态基础模型", "智能体 Agent"]
---

# A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference

> [!summary] 先说人话（基于摘要）
> 这篇综述以反馈驱动的 Test-Time Intelligence 统一部署期自我改进：一类用测试时信号改变模型状态，另一类用更多采样、计算或工具提升预测。它进一步连接适应、学习和扩展及其混合形态。

## 问题

测试时适应、测试时学习和测试时扩展分散在不同社区、使用不同术语，导致研究者难以比较它们改变了什么、用了什么反馈、付出了哪些推理资源。

## 创新点或方法

文章建立反馈驱动 TTI 视角，按模型状态是否变化及额外推理资源的使用方式梳理主要范式、应用和开放问题，覆盖视觉、语言、多模态、生成、机器人和医疗。

## 证据

这是概念与文献综述；摘要未给出可核查的实验结果数字。


## 局限

统一框架是否真正给出可操作的比较维度，而非仅重新命名既有领域，需要从全文的分类边界和代表工作覆盖度判断。

- **判断**：适合通读框架图、术语定义和研究路线图；若已熟悉测试时方法，可重点检查它是否提出新的统一评价问题。

## 研究关联

对 Agent 和多模态系统研究者，这套分类可帮助区分在线参数更新、记忆积累、搜索采样和工具调用，并设计可比较的部署期自改进实验。

- **概念**：多模态基础模型 智能体 Agent
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/A Survey on Self-Improving Test-Time Intelligence Feedback-Driven Adapting, Lear.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The ability of AI systems to improve their behavior during deployment is becoming increasingly important. As inference moves beyond the static execution of a fixed trained model, a growing body of work studies how models can refine their behavior on the fly by exploiting test-time information and additional computation. These developments have largely evolved along two directions: methods that modify the model's state using test-time signals, and methods that improve predictions through extra inference-time resources such as more sampling and tool use. However, these directions are often studied in separate communities with different terminology, making their connections harder to see. In this survey, we present feedback-driven Test-Time Intelligence (TTI) as a unified perspective for understanding such deployment-time improvement. We use this view to relate test-time adaptation, test-time learning, and test-time scaling, highlighting both their distinctions and their growing overlap in hybrid systems. This unified framework helps connect previously fragmented ideas and provides a clearer conceptual foundation for studying inference-time self-improvement. We review major methodological paradigms, representative applications, and open challenges across vision, language, multimodal learning, generative models, robotics, and healthcare. Our goal is to provide a coherent foundation and research roadmap for the study of self-improving AI systems at test time.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.01679v1
- Authors: Shuaicheng Niu, Guohao Chen, Yaofo Chen, Zhiquan Wen, Jinwu Hu, Zeshuai Deng, Deyu Chen, Shuhai Zhang, Renjie Chen, Zihao Lian, Shoukai Xu, Gang Dai, Yunbei Zhang, Wei Luo, Yifan Zhang, Mingkui Tan, Cheng Deng
- Published: 2026-09-01T11:41:39Z
- Age days: 1

</details>
