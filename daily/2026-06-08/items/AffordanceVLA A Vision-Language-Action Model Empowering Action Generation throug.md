---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06155v1"
published: "2026-06-04T13:28:51Z"
age_days: 3
score: 42
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on simulation and real-world demonstrate that AffordanceVLA achieves strong performance across diverse manipulation scenarios.

## 关键点

- **问题**：However, the structural mismatch between VLM semantic spaces and embodied control policies often hinders the learning of precise perception--action mappings.
- **创新点 / 方法**：To address this challenge, we propose \textbf{AffordanceVLA}, a unified framework that introduces structured affordance forecasting as a task-oriented intermediate representation to establish a more precise and robust perception--action mapping.
- **证据**：Extensive experiments on simulation and real-world demonstrate that AffordanceVLA achieves strong performance across diverse manipulation scenarios.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/AffordanceVLA A Vision-Language-Action Model Empowering Action Generation throug.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models leverage the rich world knowledge of pretrained
vision-language models (VLMs) to enable instruction-following robotic manipulation.
However, the structural mismatch between VLM semantic spaces and embodied control
policies often hinders the learning of precise perception--action mappings. To address
this challenge, we propose \textbf{AffordanceVLA}, a unified framework that introduces
structured affordance forecasting as a task-oriented intermediate representation to
establish a more precise and robust perception--action mapping. Specifically, we
progressively model manipulation priors through three complementary components: 1)
\textbf{Which2Act} for object-centric grounding via visual latent prediction to suppress
distractions; 2) \textbf{Where2Act} for 2D interaction localization via affordance map
estimation; and 3) \textbf{How2Act} for 3D geometric reasoning to guide manipulation
policies. These affordance cues provide spatially grounded, semantically conditioned,
and action-coupled intermediate representations, thereby naturally bridging vision,
language and action. We integrate these modules into a Mixture-of-Transformer (MoT)
architecture with specialized experts and train the model using a three-stage training
strategy with a progressive data curriculum. To overcome the scarcity of dense
affordance labels in robotic datasets, we also develop a robust automated data
augmentation pipeline. Extensive experiments on simulation and real-world demonstrate
that AffordanceVLA achieves strong performance across diverse manipulation scenarios.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06155v1
- Authors: Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
- Published: 2026-06-04T13:28:51Z
- Age days: 3

</details>
