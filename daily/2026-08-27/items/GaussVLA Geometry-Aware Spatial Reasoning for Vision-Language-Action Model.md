---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.24959v1"
published: "2026-08-25T06:28:28Z"
age_days: 2
score: 32
created: 2026-08-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model

> [!summary] 先说人话（基于摘要）
> GaussVLA 用 Gaussian Spatial Tokenizer 把语义和深度特征提升为紧凑3D Gaussian token，再用 DA-CoT 在语言与流时间条件下进行非自回归几何推理。

## 这篇到底在做什么

- **卡在哪里**：普通VLA的2D patch token缺乏内在几何结构；稠密单目深度只给每像素标量，不能表达表面方向和几何置信度，限制空间操作推理。
- **关键解法**：GST融合冻结的语义、深度特征形成3D Gaussian，并用学习查询池化几何显著区域；Mamba骨干中的DA-CoT对这些token进行结构化、非自回归推理，输出动作。区别是组织3D几何，而非简单拼接深度图。
- **拿什么证明**：仅用2亿参数在LIBERO平均成功率达93.5%，Spatial套件达100%；相对SpatialVLA的平均成功率提升19.7%，并称仿真和真机空间操作表现强。

## 值不值得读

- **和你的研究有什么关系**：它提供了参数较小的几何增强VLA方案，对需要视角、深度和精确空间关系的操作任务有直接价值。
- **先别急着信**：摘要未给出真机数字，也未说明19.7%是相对提升还是百分点之外的具体基线；DA-CoT是否贡献独立于Gaussian表示需看消融。
- **判断**：值得精读GST与DA-CoT消融；LIBERO Spatial结果突出，但更应关注跨视角和真实深度误差下是否稳健。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/GaussVLA Geometry-Aware Spatial Reasoning for Vision-Language-Action Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models encode visual observations as flat 2D patch tokens that carry no intrinsic geometric structure, and augmenting them with dense monocular depth injects per-pixel scalar values that encode neither surface orientation nor geometric confidence. This leaves the policy with limited structured spatial reasoning for action prediction. We propose GaussVLA, a Mamba-based VLA that incorporates two custom modules: Gaussian Spatial Tokenizer (GST) to lift frozen semantic and depth features into compact 3D Gaussian tokens, pools geometrically salient regions with learned queries, and \emph{Depth-Aware Chain-of-Thought (DA-CoT)} that performs structured, non-autoregressive geometric reasoning under language and flow-time conditioning. Across both simulation and real-world evaluations, GaussVLA demonstrates strong spatial-manipulation performance while remaining parameter-efficient. On LIBERO, it achieves 93.5% average success and 100.0% success on the Spatial suite with only 200M parameters, improving over SpatialVLA by 19.7% relative average success while remaining significantly more parameter-efficient.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.24959v1
- Authors: Md Selim Sarowar, Md Tanvir Islam, Sungho Kim, Sangtae Ahn
- Published: 2026-08-25T06:28:28Z
- Age days: 2

</details>
