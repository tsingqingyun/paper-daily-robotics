---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14267v1"
published: "2026-06-12T08:49:53Z"
age_days: 2
score: 30
created: 2026-06-15
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# FloVerse: Floor Plan-Guided Multi-Modal Navigation

> [!summary] 一句话结论（基于摘要）
> To bridge this gap, we introduce FloVerse, a new task for floor plan-guided embodied navigation that unifies PointNav, ObjectNav, and ImageNav.

## 关键点

- **问题**：While prior work has explored floor plan-guided navigation, it has focused mainly on PointNav and a limited set of environments.
- **创新点 / 方法**：To bridge this gap, we introduce FloVerse, a new task for floor plan-guided embodied navigation that unifies PointNav, ObjectNav, and ImageNav.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/FloVerse Floor Plan-Guided Multi-Modal Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Floor plans encapsulate compact spatial priors, enabling agents to navigate unseen
scenes more efficiently. While prior work has explored floor plan-guided navigation, it
has focused mainly on PointNav and a limited set of environments. To bridge this gap, we
introduce FloVerse, a new task for floor plan-guided embodied navigation that unifies
PointNav, ObjectNav, and ImageNav. To support FloVerse, we assemble FloVerse-1.6K, a
large-scale dataset of 1.6K scenes from HM3D and Gibson 4+, paired with corresponding
floor plans, comprising 240K expert trajectories and 12M RGBD frames. We further propose
ThreeDiff, a two-stage imitation learning policy comprising a planner, a diffusion-based
multimodal goal-reasoning module trained via masked-modality modeling, and a refiner, a
depth-based trajectory-refinement module for safe execution. Extensive experiments
demonstrate that (1) floor-plan priors improve navigation performance across all goal
modalities, and (2) ThreeDiff implicitly captures spatial information from floor plans.
These results underscore the effectiveness of spatial priors and validate our proposed
unified approach for floor plan-guided embodied navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14267v1
- Authors: Weiqi Huang, Shuangyi Dong, Jiaxin Li, Yifei Guo, Zan Wang, Wei Liang
- Published: 2026-06-12T08:49:53Z
- Age days: 2

</details>
