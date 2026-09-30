---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04193"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-09-05
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> GIFT 针对“视觉特征丰富但不够能控”的 action-sufficiency gap，在中间层加入几何对齐、可供性预测和目标区域重建监督。它能套在 VLA、直接动作 WAM 和逆动力学 WAM 上，而不改变各自的动作输出形式。

## 问题

视觉语言预训练与世界建模保留了大量语义和动态信息，却可能遗漏运动可行性、指令相关实体和目标区域，同时携带控制无关冗余。现有动作或视觉预测目标并不能保证中间特征足以支持精确操作。

## 创新点或方法

GIFT 将几何、可供性和目标位置三类控制相关结构变成训练期约束，作用于模型中间特征；分别实例化到 VLA、直接动作世界—动作模型和逆动力学版本，关键差异是增强内部表示而不统一或替换原有动作头。

## 证据

LIBERO-Plus 零样本迁移中，三种版本分别达79.6%、72.6%、87.8%，较对应基线高4.6、12.6、5.2点；RoboCasa 分别达61.4%、83.6%、82.3%，提升12.6、9.0、8.4点。摘要还报告在关节物体及未见视觉、空间扰动下收益较大。


## 局限

需核查三类监督标签如何获得、训练期额外成本，以及不同模块的独立贡献；这些决定方法能否方便迁移到新数据。

- **判断**：值得精读，因其跨三类动作建模方式都有量化收益；重点应看监督构造和公平对照，而非只看最终分数。

## 研究关联

它给 VLA 和世界模型研究者一个可复用原则：不要只扩大视觉表征，而要显式约束中间特征保留动作所需的几何与任务结构。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/GIFT Guided Intermediate Feature Training via Action-Oriented Structural Supervi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04193v1 Announce Type: new Abstract: Vision-language pre-training and predictive world modeling provide robot policies with rich semantic and dynamic visual features, but their native action and visual-prediction objectives may omit critical physical and task structure while retaining control-irrelevant visual redundancy. We call this mismatch between visual richness and control utility the action-sufficiency gap. We investigate whether this gap can be bridged by guiding intermediate features to preserve three control-relevant structure in robotic manipulation: geometry governing motion feasibility, affordance encoding instruction-relevant entities, and goals grounding instructions in task-relevant regions. To this end, we present GIFT (Guided Intermediate Feature Training), an architecture-flexible framework for learning intermediate features that translates these structures into training-time constraints through geometry alignment, affordance prediction, and goal-region reconstruction. We instantiate GIFT in a Vision-Language-Action (VLA) policy, a direct-action World-Action Model (WAM), and an inverse-dynamics WAM while retaining each model's action formulation. Under zero-shot transfer to LIBERO-Plus, GIFT-VLA, GIFT-WAM-Fast, and GIFT-WAM-IDM outperform StarVLA-OFT, Fast-WAM, and Fast-WAM-IDM by 4.6, 12.6, and 5.2 points, reaching 79.6%, 72.6%, and 87.8%, respectively. On RoboCasa, the three GIFT variants reach 61.4%, 83.6%, and 82.3%, outperforming their counterparts by 12.6, 9.0, and 8.4 points, respectively. Together, these results establish learning functionally structured intermediate features as a reusable principle across model-specific action formulations, with especially large gains on articulated-object tasks and high-precision real-world manipulation under unseen visual and spatial perturbations. Project page: https://openphoenix-team.github.io/GIFT-pages.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04193
- Authors: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Chaoyue Li, Qichao Zhang, Haoran Li, Zhongpu Xia, Ya-Qin Zhang, Shuicheng Yan, Dongbin Zhao
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
