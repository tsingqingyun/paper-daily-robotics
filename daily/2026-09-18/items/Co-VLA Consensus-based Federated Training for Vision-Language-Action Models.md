---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19923v1"
published: "2026-09-17T09:02:36Z"
age_days: 0
score: 31
created: 2026-09-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Co-VLA: Consensus-based Federated Training for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> Co-VLA让不同地点的机器人保留本地数据，通过ADMM共识优化协作训练一个VLA，目标是在数据不集中时接近集中训练效果。

## 问题

机器人数据分散在不同任务、设备和地点，集中收集成本高或不可行；各客户端数据分布又不同，使联邦训练不能忽略异质性。

## 创新点或方法

将ADMM共识优化用于客户端之间的模型协作，同一算法覆盖全模型训练、固定秩适配器和自适应秩适配器微调，不需要共享本地原始数据。

## 证据

摘要称全模型训练和参数高效微调都取得与集中训练相当的性能；摘要未给出可核查的结果数字。

## 局限

需核查客户端数量、分布差异、通信成本及“相当”的具体差距；不共享原始数据本身也不构成正式隐私保证。

- **判断**：有真实分布式数据需求时值得精读优化与通信设置，否则先看实验规模再判断优先级。

## 研究关联

对拥有分散机器人数据的VLA团队，这是训练组织方式上的直接参考，重点价值在于如何协调异质客户端。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Co-VLA Consensus-based Federated Training for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action models (VLAs) have emerged as a promising paradigm for general-purpose robot learning, with performance improving as models and datasets scale. Scaling robot data collection, however, remains challenging because data are naturally distributed across robots, tasks, and locations, making centralization costly or impractical. Federated learning offers a way to train on decentralized robot data, but applying it to VLAs requires accounting for heterogeneous robot client data distributions. We present Co-VLA, which applies consensus optimization using the Alternating Direction Method of Multipliers~(ADMM) to federated VLA training. We show that the same algorithm supports both full-model training and parameter-efficient fine-tuning with both fixed-rank and rank-adaptive adapters. The name Co-VLA reflects both consensus and collaboration: clients with different local robot datasets collaboratively train a shared model without sharing their data. Our experiments demonstrate that Co-VLA achieves performance comparable to centralized training in both full-model training and parameter-efficient fine-tuning settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19923v1
- Authors: Haolong Li, Guner Dilsad Er, Michael Muehlebach, Joerg Stueckler
- Published: 2026-09-17T09:02:36Z
- Age days: 0

</details>
