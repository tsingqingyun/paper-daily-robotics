---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37181v1"
published: "2026-09-29T10:05:10Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation

> [!summary] 先说人话（基于摘要）
> EgoHumanoid-V2 把第一视角人类示范转成人形机器人的全身协同技能。它先修正运动学参考，再按动力学细化动作，同时处理人和机器人外观、视角的差异。

## 问题

人类示范能低成本覆盖丰富场景与全身动作，但直接迁移时存在动作和视觉形态差异。此前第一视角迁移主要在解耦控制下研究场景泛化，对协同全身技能的直接迁移覆盖不足。

## 创新点或方法

以人类示范为监督，通过由粗到细的动作对齐，在保持全身协调的同时提高末端位姿精度。机器人手臂渲染和训练图像增强用于缩小视觉形态差距，随后用对齐数据训练 VLA。

## 证据

在四项真实任务上，无目标任务机器人示范的 VLA 实现零样本技能迁移。摘要称任务得分与遥操作数据训练的策略相当、采集成本更低，但未给出可核查的结果数字。

## 局限

需核查动力学细化使用哪些机器人信息，以及“得分相当”和“成本更低”的统计口径；摘要没有量化这两项结论。

- **判断**：做全身 VLA 或人类示范迁移者值得精读动作对齐，其他读者可先看四项真实任务的边界。

## 研究关联

对人形 VLA 和机器人学习，重点是人类数据能否直接监督协同控制，而不仅提供场景信息；若对齐过程可复用，有助于减少目标任务遥操作需求。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/EgoHumanoid-V2 Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation. Prior work on egocentric transfer has emphasized scene generalization in loco-manipulation under decoupled control, leaving direct transfer of coordinated whole-body skills less explored. We present EgoHumanoid-V2, the first egocentric human-to-humanoid skill transfer framework for coordinated whole-body loco-manipulation. At its core, coarse-to-fine action alignment combines kinematic reference correction with dynamics-aware refinement. It improves end-effector pose accuracy while preserving whole-body coordination. We also use robot-arm rendering and training-time image augmentation to reduce the visual embodiment gap and improve viewpoint robustness. On four real-world tasks, vision-language-action (VLA) policies trained on aligned human data show zero-shot skill transfer without target-task robot demonstrations. Task scores are comparable to those of policies trained on teleoperation data at a lower collection cost. These results support human data as direct skill supervision.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37181v1
- Authors: Jin Chen, Yiming Jiang, Chongyang Xu, Modi Shi, Shijia Peng, Li Chen, Tianyu Li, Mu Xu, Yilun Chen, Steven Hoi, Hongyang Li
- Published: 2026-09-29T10:05:10Z
- Age days: 0

</details>
