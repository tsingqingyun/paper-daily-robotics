---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25785v1"
published: "2026-09-22T07:20:02Z"
age_days: 1
score: 32
created: 2026-09-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation

> [!summary] 先说人话（基于摘要）
> VisForce 把当前指尖力和目标指尖力画在对应图像位置上，让 VLA 同时看到在哪里接触、现在用多大力、希望用多大力。

## 问题

灵巧手操作中，力通常作为独立状态或专用表示输入，难以显式对应到视觉中的具体接触位置，增加了视觉与力信息融合的难度。

## 创新点或方法

在当前腕部图像和任务目标图像上渲染指尖对齐的力提示，再通过目标条件交叉注意力融合两类表示并生成动作。与独立力向量输入相比，核心变化是显式建立力与图像位置的关联。

## 证据

使用 UR10 和 RH56F1 灵巧手进行真实实验。目标力增大时握力响应一致；鸡蛋和牙膏管抓取抬升成功率为 70% 和 80%；杯子插入/瓶子倾倒、夹面包及滑移调制插孔任务最终成功率分别为 70%、55% 和 40%。

## 局限

摘要未给出试验次数和相对基线收益；需核查目标图像、目标力的指定方式，以及提升是否确实来自空间对齐。

- **判断**：值得阅读表示设计和真实失败案例，现有结果支持可行性，但还不足以认定可靠的通用灵巧操作能力。

## 研究关联

对多模态 VLA 研究者，它提供了将力反馈接入视觉表示的直接方案，适合研究接触位置与力目标如何共同影响动作。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/VisForce Visual Grounding of Current and Desired Forces for Goal-Conditioned Dex.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have emerged as general-purpose robotic manipulation policies. However, in dexterous hand manipulation, contact forces are typically provided as separate states or force-specific representations, making it difficult to explicitly represent the spatial correspondence between force and their corresponding visual locations. In this work, we propose VisForce, which visually grounds the current and desired forces at their corresponding fingertip locations. VisForce renders current and desired visual force cues on the current wrist image and a task-specific goal image, and combines the two representations through goal-conditioned cross-attention to generate force-aware actions. We evaluate VisForce using a real UR10 robot equipped with an RH56F1 dexterous hand through force-conditioned grasping and three multi-stage manipulation tasks. In force-conditioned grasping experiments, VisForce exhibited a consistent grip-force response as the desired force increased, and achieved grasp-and-lift success rates of 70% and 80% for an egg and a toothpaste tube, respectively. It further achieved final success rates of 70%, 55%, and 40% on cup insertion/bottle pouring, tong-assisted bread transfer, and slip-modulated peg-in-hole, respectively. These results show that fingertip-aligned visual force representations can be effectively used for force-aware conditioning in VLA-based dexterous hand manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25785v1
- Authors: Jung-Woo Lee, Soo-Chul Lim
- Published: 2026-09-22T07:20:02Z
- Age days: 1

</details>
