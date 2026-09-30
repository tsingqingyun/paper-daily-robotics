---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26720"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-08-29
concepts: ["AI 核心知识地图"]
---

# Parameter Efficient Continual Learning for Sparse Event-Based Transformers

> [!summary] 先说人话（基于摘要）
> sLoTh冻结稀疏脉冲视觉Transformer主干，只更新seLoRA注意力低秩参数和共享神经元阈值，用不到1%的参数完成无回放持续学习。

## 这篇到底在做什么

- **卡在哪里**：机器人和边缘设备的数据持续变化，却受内存与能耗限制；普通ViT的参数高效持续学习仍依赖稠密计算，而稀疏事件模型如何避免遗忘尚缺研究。
- **关键解法**：输入持续到来的分类数据流，保持预训练稀疏事件Transformer主干不变，通过可扩展高效低秩注意力更新和共享阈值调制适配新任务，不保存回放缓冲区。输出是持续更新的分类模型。
- **拿什么证明**：在CIFAR-100、Tiny-ImageNet、ImageNet-100和ImageNet-R、最多100个任务上取得有竞争力的无回放类别增量和在线持续学习表现；更新参数少于1%，能耗约比稠密ViT低6.5倍。

## 值不值得读

- **和你的研究有什么关系**：对资源受限机器人感知有实际价值，尤其适合事件相机和在线适配；它与VLA或世界模型没有直接联系。
- **先别急着信**：需全文核查能耗估算或测量方式，以及“有竞争力”在准确率、遗忘和任务顺序上的具体含义。
- **判断**：做事件视觉或边缘持续学习值得精读；其他具身方向了解参数高效适配思路即可。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/Parameter Efficient Continual Learning for Sparse Event-Based Transformers.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.26720v1 Announce Type: new Abstract: Robotic and edge intelligence systems operate in dynamic environments where data arrives continuously, requiring models to adapt while preserving previously learned knowledge under strict memory and energy constraints. While parameter-efficient fine-tuning has shown promise for continual learning with vision transformers, conventional architectures rely on dense computation and remain costly for real-world deployment. Sparse event-based vision transformers provide energy-efficient event-driven computation, yet their continual learning capabilities remain largely unexplored. We here introduce sLoTh, a parameter-efficient continual learning framework for pretrained sparse event-based (spiking) vision transformers. sLoTh freezes the backbone and restricts plasticity to scalable-efficient low-rank attention updates (seLoRA) and shared neuronal threshold modulation, enabling adaptation without replay buffers by updating less than 1% of model parameters. Experiments across CIFAR-100, Tiny-ImageNet, ImageNet-100, and ImageNet-R with up to 100 tasks demonstrate competitive rehearsal-free performance in class-incremental learning and online continual learning, while enabling approximately 6.5x lower energy consumption than conventional dense vision transformers.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26720
- Authors: Vaishnavi Nagabhushana, Kartikay Agrawal, Ayon Borthakur
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
