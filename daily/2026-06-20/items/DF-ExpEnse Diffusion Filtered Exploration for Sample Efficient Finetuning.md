---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19656v1"
published: "2026-06-17T23:40:45Z"
age_days: 2
score: 30
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning

> [!summary] 一句话结论（基于摘要）
> We present DF-ExpEnse, an exploration technique that improves the quality of online experience collection, thus increasing finetuning sample-efficiency.

## 关键点

- **问题**：A natural recipe for intelligent robotic decision-making is initializing from pretrained generative control policies, which have summarized offline experience, and adapting them to self-collected online experience.
- **创新点 / 方法**：We present DF-ExpEnse, an exploration technique that improves the quality of online experience collection, thus increasing finetuning sample-efficiency.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A natural recipe for intelligent robotic decision-making is initializing from pretrained
generative control policies, which have summarized offline experience, and adapting them
to self-collected online experience. We present DF-ExpEnse, an exploration technique
that improves the quality of online experience collection, thus increasing finetuning
sample-efficiency. DF-ExpEnse leverages the multimodal modeling capabilities of the
generative control policy to create an expressive and tractably evaluatable candidate
set. It then utilizes an ensemble of critics to identify the action that best balances
quality with high exploration interest. In fleet settings, DF-ExpEnse further enables
cross-agent communication to facilitate collaborative exploration as a group. DF-ExpEnse
can be seamlessly integrated with existing strategies that finetune pretrained
generative control policies via reinforcement learning. We experimentally validate
consistent sample-efficiency benefits through DF-ExpEnse across a variety of
manipulation and locomotion tasks, compared to default finetuning and alternative action
selection schemes. Project can be found at https://df-expense.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19656v1
- Authors: Calvin Luo, Chen Sun, Shuran Song
- Published: 2026-06-17T23:40:45Z
- Age days: 2

</details>
