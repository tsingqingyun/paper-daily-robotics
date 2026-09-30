---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.01679"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-09-04
concepts: ["多模态基础模型", "智能体 Agent"]
---

# A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference

> [!summary] 先说人话（基于摘要）
> 这篇综述用反馈驱动的测试时智能（TTI）统一理解部署期自我改进：一类利用测试信号改变模型状态，另一类通过采样、工具和额外计算改进输出，并讨论二者在混合系统中的合流。

## 这篇到底在做什么

- **卡在哪里**：测试时适应、测试时学习和测试时扩展分散在不同社区，术语和关注点不一，使研究者难以比较它们如何使用反馈、是否更新模型以及如何消费推理资源。
- **关键解法**：综述建立统一概念框架，区分并连接三类测试时机制，整理视觉、语言、多模态、生成模型、机器人和医疗中的方法、应用及开放问题。其作用对象是已有文献体系，输出是分类法与研究路线图，而非新策略模型。
- **拿什么证明**：这是综述性工作；摘要只说明覆盖主要方法范式、代表应用和开放挑战，没有报告新实验或可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对Agent与具身研究者，这一框架可帮助区分在线参数更新、记忆积累、搜索采样和工具调用，便于设计会在部署中利用反馈改进的机器人系统。其价值主要是统一语言与研究问题。
- **先别急着信**：摘要无法显示文献覆盖范围、纳入标准及分类边界，是否真正调和各社区定义需要核查正文和参考文献。
- **判断**：需要搭建测试时自适应研究地图的人值得通读；寻找新算法或实证结论者可先读分类图和开放问题。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/A Survey on Self-Improving Test-Time Intelligence Feedback-Driven Adapting, Lear.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.01679v1 Announce Type: new Abstract: The ability of AI systems to improve their behavior during deployment is becoming increasingly important. As inference moves beyond the static execution of a fixed trained model, a growing body of work studies how models can refine their behavior on the fly by exploiting test-time information and additional computation. These developments have largely evolved along two directions: methods that modify the model's state using test-time signals, and methods that improve predictions through extra inference-time resources such as more sampling and tool use. However, these directions are often studied in separate communities with different terminology, making their connections harder to see. In this survey, we present feedback-driven Test-Time Intelligence (TTI) as a unified perspective for understanding such deployment-time improvement. We use this view to relate test-time adaptation, test-time learning, and test-time scaling, highlighting both their distinctions and their growing overlap in hybrid systems. This unified framework helps connect previously fragmented ideas and provides a clearer conceptual foundation for studying inference-time self-improvement. We review major methodological paradigms, representative applications, and open challenges across vision, language, multimodal learning, generative models, robotics, and healthcare. Our goal is to provide a coherent foundation and research roadmap for the study of self-improving AI systems at test time.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.01679
- Authors: Shuaicheng Niu, Guohao Chen, Yaofo Chen, Zhiquan Wen, Jinwu Hu, Zeshuai Deng, Deyu Chen, Shuhai Zhang, Renjie Chen, Zihao Lian, Shoukai Xu, Gang Dai, Yunbei Zhang, Wei Luo, Yifan Zhang, Mingkui Tan, Cheng Deng
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
