---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20912v1"
published: "2026-07-23T04:46:19Z"
age_days: 1
score: 27
created: 2026-07-24
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# URF: A Unified Robot Control-Policy Framework for Stable Contact Aware Manipulation

> [!summary] 一句话结论（基于摘要）
> Across box-flipping and line-pressing tasks, URF achieves higher task success rates while reducing failure modes observed with admittance-only execution, including rapid force buildup, large force oscillations, tool breakage, and robot safety stops.

## 关键点

- **问题**：In rigid contact, this separation can be problematic: the same motion to a virtual target or compliant motion command can lead to unstable contact, tracking error, excessive loading, or tool damage, depending on the low-level controller.
- **创新点 / 方法**：In this paper, we propose a \textit{Unified Robot Control-Policy Framework} (URF), which connects compliant action prediction with unified impedance-admittance control.
- **证据**：Across box-flipping and line-pressing tasks, URF achieves higher task success rates while reducing failure modes observed with admittance-only execution, including rapid force buildup, large force oscillations, tool breakage, and robot safety stops.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning-based manipulation policies usually predict robot actions from sensory
observations and leave their execution to a separate low-level controller. In rigid
contact, this separation can be problematic: the same motion to a virtual target or
compliant motion command can lead to unstable contact, tracking error, excessive
loading, or tool damage, depending on the low-level controller. In this paper, we
propose a \textit{Unified Robot Control-Policy Framework} (URF), which connects
compliant action prediction with unified impedance-admittance control. Given multimodal
observations, URF predicts a virtual target, a stiffness matrix, and an impedance-
admittance switch ratio. The switch ratio determines when the controller should behave
more like admittance control for accurate motion tracking and when it should move toward
impedance control for safer rigid contact. Because demonstration data do not provide
ground-truth environment stiffness, we construct switch-ratio labels from measured
contact forces and use them to supervise controller-mode prediction. Across box-flipping
and line-pressing tasks, URF achieves higher task success rates while reducing failure
modes observed with admittance-only execution, including rapid force buildup, large
force oscillations, tool breakage, and robot safety stops. These results suggest that
contact-aware policies benefit from predicting not only compliant actions but also the
controller behavior used to execute them. Project page:
https://jiyou384.github.io/urf_project_page/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20912v1
- Authors: Jiyou Shin, Youngjin Seo, Jaeseog Won, Sungwon Seo, Hyunjun Kim, Seokmin Yoon, Tuan Luong, Hyungpil Moon
- Published: 2026-07-23T04:46:19Z
- Age days: 1

</details>
