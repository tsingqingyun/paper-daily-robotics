---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04193v1"
published: "2026-09-03T17:59:03Z"
age_days: 3
score: 39
created: 2026-09-07
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> GIFT 通过几何对齐、可供性预测和目标区域重建，强迫 VLA/WAM 的中间特征保留真正与控制有关的结构，弥合“视觉丰富但动作信息不足”的 action-sufficiency gap。

## 这篇到底在做什么

- **卡在哪里**：视觉语言预训练和预测式世界模型包含丰富语义与动态信息，却可能遗漏运动可行性、指令相关物体和目标区域，同时保留大量控制无关视觉冗余，导致视觉能力不能直接转化为操作能力。
- **关键解法**：GIFT在训练期对中间特征施加三类结构监督：几何、可供性和目标区域；它分别接入VLA、直接动作WAM和逆动力学WAM而不改变各自的动作建模形式，因而强调可复用的特征约束而非统一动作头。
- **拿什么证明**：LIBERO-Plus零样本迁移中三种版本分别达79.6%、72.6%、87.8%，较对应基线高4.6、12.6、5.2点；RoboCasa分别达61.4%、83.6%、82.3%，提高12.6、9.0、8.4点。摘要还称铰接物体及未见视觉、空间扰动下的高精度真实操作收益尤其大。

## 值不值得读

- **和你的研究有什么关系**：对VLA和世界模型研究者，它提供了一个跨动作建模范式的中间表征训练原则，可用于把基础模型特征改造成更适合物理控制的特征。
- **先别急着信**：需从全文核查三类监督所需标注或估计信息，以及真实机器人结论的任务范围；摘要不足以判断收益主要来自哪项约束。
- **判断**：值得精读并重点看监督构造和消融；跨三种模型均有明确增益，使其比单一架构技巧更有复用价值。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/GIFT Guided Intermediate Feature Training via Action-Oriented Structural Supervi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language pre-training and predictive world modeling provide robot policies with rich semantic and dynamic visual features, but their native action and visual-prediction objectives may omit critical physical and task structure while retaining control-irrelevant visual redundancy. We call this mismatch between visual richness and control utility the action-sufficiency gap. We investigate whether this gap can be bridged by guiding intermediate features to preserve three control-relevant structure in robotic manipulation: geometry governing motion feasibility, affordance encoding instruction-relevant entities, and goals grounding instructions in task-relevant regions. To this end, we present GIFT (Guided Intermediate Feature Training), an architecture-flexible framework for learning intermediate features that translates these structures into training-time constraints through geometry alignment, affordance prediction, and goal-region reconstruction. We instantiate GIFT in a Vision-Language-Action (VLA) policy, a direct-action World-Action Model (WAM), and an inverse-dynamics WAM while retaining each model's action formulation. Under zero-shot transfer to LIBERO-Plus, GIFT-VLA, GIFT-WAM-Fast, and GIFT-WAM-IDM outperform StarVLA-OFT, Fast-WAM, and Fast-WAM-IDM by 4.6, 12.6, and 5.2 points, reaching 79.6%, 72.6%, and 87.8%, respectively. On RoboCasa, the three GIFT variants reach 61.4%, 83.6%, and 82.3%, outperforming their counterparts by 12.6, 9.0, and 8.4 points, respectively. Together, these results establish learning functionally structured intermediate features as a reusable principle across model-specific action formulations, with especially large gains on articulated-object tasks and high-precision real-world manipulation under unseen visual and spatial perturbations. Project page: https://openphoenix-team.github.io/GIFT-pages.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04193v1
- Authors: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Chaoyue Li, Qichao Zhang, Haoran Li, Zhongpu Xia, Ya-Qin Zhang, Shuicheng Yan, Dongbin Zhao
- Published: 2026-09-03T17:59:03Z
- Age days: 3

</details>
