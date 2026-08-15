---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.11769v1"
published: "2026-08-12T08:13:44Z"
age_days: 2
score: 38
created: 2026-08-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Policy-Induced Hand Priors in Humanoid Dual-Arm Manipulation: Diagnosing and Mitigating Initial-Pose Dependence

> [!summary] 一句话结论（基于摘要）
> Evaluations across multiple policies and 17 initial configurations reveal strong initial-pose--policy interactions: the same pose produces substantially different success rates across policies, while a single policy exhibits large performance variation across…

## 关键点

- **问题**：Vision-language-action (VLA) policies are expected to operate robustly across variations in the robot's initial configuration, yet aggregate task success can conceal pose-specific failures and inappropriate hand selection.
- **创新点 / 方法**：This work investigates initial-pose dependence in VLA-based humanoid dual-arm manipulation.
- **证据**：Evaluations across multiple policies and 17 initial configurations reveal strong initial-pose--policy interactions: the same pose produces substantially different success rates across policies, while a single policy exhibits large performance variation across poses.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/Policy-Induced Hand Priors in Humanoid Dual-Arm Manipulation Diagnosing and Miti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies are expected to operate robustly across variations in the robot's initial configuration, yet aggregate task success can conceal pose-specific failures and inappropriate hand selection. This work investigates initial-pose dependence in VLA-based humanoid dual-arm manipulation. We characterize the initial-condition-dependent early hand preference as a policy-induced hand prior and quantify it using HandPriorScore, residual hand bias, and target responsiveness. Evaluations across multiple policies and 17 initial configurations reveal strong initial-pose--policy interactions: the same pose produces substantially different success rates across policies, while a single policy exhibits large performance variation across poses. Specific initial arm configurations can suppress or induce an asymmetric hand preference, with the resulting effect varying in direction and strength across policies. Wrist-camera observations also influence hand selection and task performance. Expanding initial-pose coverage in the training dataset substantially improves robustness, while targeted augmentation around a low-performing configuration increases its success rate. Comparisons across training configurations show that sufficient exposure to the target simulation task is beneficial, whereas the effect of real or auxiliary data depends on pose coverage, simulation ratio, and observation availability. These findings characterize a pose-conditioned hand prior, identify a localized initial arm configuration as a causal handle on hand-selection behavior, and demonstrate how data coverage and training composition affect initial-pose robustness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.11769v1
- Authors: Chaeyeon Jung, Juyoun Park
- Published: 2026-08-12T08:13:44Z
- Age days: 2

</details>
