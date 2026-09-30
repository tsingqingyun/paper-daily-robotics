---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24525v1"
published: "2026-09-21T12:59:57Z"
age_days: 1
score: 44
created: 2026-09-23
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Bridge3D: Enabling Vision-Language-Action Models to See and Act in 3D

> [!summary] 先说人话（基于摘要）
> Bridge3D让已有二维VLA既能看出三维结构，也能在生成动作时受到几何约束。关键是同时增强视觉特征，并把显式三维语义场接入动作去噪。

## 问题

二维观测为主的VLA难以完成精细空间操作；已有三维增强方法主要提供隐式空间先验，仍缺少直接指导动作的显式几何信息。

## 创新点或方法

Implicit Fusion把三维基础模型特征融入视觉token；Explicit Conditioning让动作去噪以三维语义场为条件，并采用逐层线性探测提高学习效率。

## 证据

RoboTwin 2.0上比π₀高14.0个百分点；真实实验比Spatial Forcing高11.7个百分点。摘要未提供绝对成功率。

## 局限

需核查两类几何指导各自的贡献、三维语义场如何获得，以及逐层线性探测具体如何参与训练。

- **判断**：值得读方法和消融，重点判断显式动作条件是否带来超出视觉特征增强的收益。

## 研究关联

适合希望保留预训练二维VLA、逐步加入三维能力的研究者，提供了分别作用于感知端和动作端的改造路径。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：44
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Bridge3D Enabling Vision-Language-Action Models to See and Act in 3D.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have demonstrated remarkable generalization in robotic manipulation via large-scale multimodal pretraining. However, VLA models are mainly trained on 2D-centric observations, which inherently constrains their capacity for precise spatial manipulation. Previous methods enhance 3D awareness by introducing implicit spatial priors, but still lack explicit geometry guidance. In this paper, we propose Bridge3D that integrates both implicit and explicit 3D geometry guidance into pre-trained 2D VLA models, enabling them to ''see'' and ''act'' in 3D. Bridge3D introduces two strategies: 1) Implicit Fusion, which enriches visual tokens with features from 3D foundation models to improve ''seeing'' in 3D; 2) Explicit Conditioning, which integrates action denoising with an explicit 3D semantic field to achieve ''acting'' in 3D. Furthermore, we utilize the proposed layer-wise linear probing to improve learning efficiency. Experiments show that Bridge3D achieves superior performance against state-of-the-art methods. On the RoboTwin 2.0 benchmark, Bridge3D exceeds $π_0$ by 14.0 percentage points, while in real-world experiments, it outperforms Spatial Forcing by 11.7 percentage points. These results demonstrate Bridge3D's strong capabilities in high-precision and spatial-sensitive manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24525v1
- Authors: Haoxuan Li, Sixu Yan, Lianghui Zhu, Xuanlai Tang, Shikang Wang, Xinggang Wang
- Published: 2026-09-21T12:59:57Z
- Age days: 1

</details>
