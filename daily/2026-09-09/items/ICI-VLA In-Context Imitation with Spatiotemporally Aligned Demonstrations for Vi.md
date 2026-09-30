---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07581v1"
published: "2026-09-07T14:55:35Z"
age_days: 1
score: 36
created: 2026-09-09
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> ICI-VLA让固定策略在执行时检索几段与当前动作阶段、空间几何匹配的示范，再据此生成动作。适配靠上下文示例完成，无需现场更新策略参数。

## 问题

新操作场景通常需要额外梯度更新，在任务数据或计算有限时难以快速部署；检索示范还必须匹配当前子任务进度，避免策略直接照抄不适用的动作。

## 创新点或方法

保留文本—动作VLM原生文本生成接口，将长轨迹拆成带语义标签的短示范。RD-Encoder利用DTW挖掘正样本，学习时空对齐检索；Target Action Masking通过上下文损坏训练降低直接复制动作的倾向。

## 证据

平均成功率为LIBERO 97.7%、RoboTwin 2.0 60.4%；后者超过最高已报告基线平均值19.3个百分点。在4项实体任务上达到83.2%。


## 局限

需要核查测试时示范库的来源、规模以及与测试任务的重合关系，这是判断适配能力和成功率可比性的关键。

- **判断**：优先精读检索构造与评测划分，固定策略下的收益及实体实验使它值得深入复现。

## 研究关联

为VLA少样本适配提供可操作的检索路线，也提示机器人示范库应按子任务阶段与几何关系组织，而不只按语言语义索引。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/ICI-VLA In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies are commonly adapted to new manipulation settings through additional gradient updates, which limits rapid deployment when task-specific data or compute is scarce. We present ICI-VLA, a training and retrieval framework that equips a text-action VLM with few-shot test-time adaptation through in-context demonstrations. Unlike mainstream VLA designs based on action-specific multimodal fusion, ICI-VLA retains the native text-generation interface. ICI-VLA updates its parameters only during offline training; at inference, the policy remains fixed and conditions action generation on retrieved micro-demonstrations. The framework decomposes long trajectories into short, semantically labeled examples and trains an RD-Encoder with positives mined by Dynamic Time Warping (DTW), aligning the retrieved context with the phase and geometry of the current subtask. We further introduce Target Action Masking, a context-corruption objective designed to reduce direct action copying and increase reliance on the current observation. ICI-VLA reaches average success rates of 97.7% on LIBERO and 60.4% on RoboTwin 2.0, exceeding the highest reported baseline average on RoboTwin 2.0 by 19.3 percentage points. It also achieves 83.2% across four physical tasks. These results indicate that a fixed VLA policy can benefit from conditioning on spatiotemporally aligned demonstrations at test time.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07581v1
- Authors: Songhua Yang, Ziyu Liu, Xuetao Li, Ruqi Xiao, Kangxin Zhu, Miao Li
- Published: 2026-09-07T14:55:35Z
- Age days: 1

</details>
