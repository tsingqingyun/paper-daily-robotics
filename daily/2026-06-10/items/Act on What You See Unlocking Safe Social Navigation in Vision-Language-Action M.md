---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10495v1"
published: "2026-06-09T07:18:01Z"
age_days: 0
score: 34
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> On SCAND and real-world deployment, SALSA reduces near-collisions by 86.4% and improves social counterfactual accuracy from 53% to 93%, demonstrating that safer social navigation can be achieved by teaching VLA policies to act on representations they already…

## 关键点

- **问题**：We show that pretrained Vision-Language-Action (VLA) models already encode pedestrian-object distinctions and future collision signals in their internal representations, but behavior cloning fails to translate these signals into socially appropriate actions.
- **创新点 / 方法**：To address this mismatch, we propose SALSA, a two- stage annotation-free post-training framework: (1) social behavioral alignment bridges intermediate-layer social features to the action head and trains on counterfactual human-object scene pairs to break visual saliency shortcuts; (2) temporal safety alignment provide…
- **证据**：On SCAND and real-world deployment, SALSA reduces near-collisions by 86.4% and improves social counterfactual accuracy from 53% to 93%, demonstrating that safer social navigation can be achieved by teaching VLA policies to act on representations they already possess.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/Act on What You See Unlocking Safe Social Navigation in Vision-Language-Action M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safe social navigation requires robots to distinguish people from ordinary obstacles and
to react before danger becomes imminent. We show that pretrained Vision-Language-Action
(VLA) models already encode pedestrian-object distinctions and future collision signals
in their internal representations, but behavior cloning fails to translate these signals
into socially appropriate actions. To address this mismatch, we propose SALSA, a two-
stage annotation-free post-training framework: (1) social behavioral alignment bridges
intermediate-layer social features to the action head and trains on counterfactual
human-object scene pairs to break visual saliency shortcuts; (2) temporal safety
alignment provides automatically generated future-risk supervision to enable
anticipatory collision avoidance. On SCAND and real-world deployment, SALSA reduces
near-collisions by 86.4% and improves social counterfactual accuracy from 53% to 93%,
demonstrating that safer social navigation can be achieved by teaching VLA policies to
act on representations they already possess. These results show that pretrained VLA
policies can be adapted for safer social navigation by better aligning their latent
representations with action generation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10495v1
- Authors: Qingzi Wang, Xiyang Wu, Guangyao Shi, Dianwei Chen, Xianfeng Yang, Dinesh Manocha
- Published: 2026-06-09T07:18:01Z
- Age days: 0

</details>
