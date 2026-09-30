---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37602v1"
published: "2026-09-29T13:53:19Z"
age_days: 0
score: 35
created: 2026-09-30
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# When to Adapt: Multi-Signal Domain Shift Detection for Efficient Training-Free Adaptation in Open-Vocabulary Segmentation

> [!summary] 先说人话（基于摘要）
> 这项方法让开放词汇分割系统在环境确实变化时才启动适配，减少逐帧调整的成本。它联合监测画面变化、适配器失配和语义漂移，判断何时需要更新。

## 问题

长期运行的机器人会遇到域偏移，视觉基础模型的分割性能可能下降。已有免训练适配按每一帧执行，对资源有限的机器人硬件不够经济。

## 创新点或方法

利用连续帧的时间连贯性，组合三类互补变化信号，触发免训练持续测试时适配。干预对象是适配时机，关键差异是由变化检测决定更新，而非每帧固定适配。

## 证据

摘要报告在包含室内、室外环境和真实机器人数据的基准上，维持分割精度的同时显著减少适配次数；摘要未给出可核查的结果数字。

## 局限

需核查变化检测本身的开销、触发阈值和突变后的响应延迟；减少适配次数是否带来实际运行收益仍需全文数据。

- **判断**：做长期机器人感知者值得读触发机制和成本实验，纯动作策略研究者可略读。

## 研究关联

对依赖开放词汇感知的具身系统，提供了控制在线适配频率的方法。对 VLA 的价值主要在感知前端，摘要没有验证操作成功率。

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/When to Adapt Multi-Signal Domain Shift Detection for Efficient Training-Free Ad.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robust and reliable perception is essential for autonomous robots operating in real-world environments, particularly in long-term missions where environmental conditions may change significantly over time. Although recent advances in Visual Foundation Models (VFMs) have improved open-vocabulary semantic segmentation, these models can still suffer from domain shift, which can significantly degrade performance if they are not adapted to the current environment. Training-free domain adaptation is a relevant paradigm for adaptation, consisting of adjusting the model online using lightweight adapters. Recent approaches apply this on a per-frame basis, which is impractical for deployments on resource-constrained robotic hardware. To tackle this, we propose a multi-signal domain shift detection method for training-free continual test-time adaptation (TF-CTTA) in open-vocabulary segmentation. Our method leverages temporal coherence across consecutive frames by monitoring and combining complementary aspects of domain shift (visual change, adapter mismatch, and semantic drift) to trigger adaptation only when needed. We validate our approach on a benchmark including indoor and outdoor environments and using real robotic data. We demonstrate that our approach maintains segmentation accuracy while substantially reducing adaptations, making training-free adaptation practical and feasible for long-term, real-world robotic deployments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37602v1
- Authors: Michele Antonazzi, Alejandra C. Hernandez, José Araujo, Olov Andersson, Patric Jensfelt
- Published: 2026-09-29T13:53:19Z
- Age days: 0

</details>
