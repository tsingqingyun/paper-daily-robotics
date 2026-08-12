---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13548v1"
published: "2026-05-13T13:55:37Z"
age_days: 0
score: 41
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# AttenA+: Rectifying Action Inequality in Robotic Foundation Models

> [!summary] 一句话结论（基于摘要）
> Specifically, it improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to 92.4% (+0.6%) on RoboTwin 2.0.

## 关键点

- **问题**：This "flat" training paradigm, inherited from language modeling, remains indifferent to the underlying physical hierarchy of manipulation.
- **创新点 / 方法**：To rectify this, we introduce AttenA+, an architecture-agnostic framework that prioritizes kinematically critical segments via velocity-driven action attention.
- **证据**：Specifically, it improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to 92.4% (+0.6%) on RoboTwin 2.0.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/AttenA+ Rectifying Action Inequality in Robotic Foundation Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Existing robotic foundation models, while powerful, are predicated on an implicit
assumption of temporal homogeneity: treating all actions as equally informative during
optimization. This "flat" training paradigm, inherited from language modeling, remains
indifferent to the underlying physical hierarchy of manipulation. In reality, robot
trajectories are fundamentally heterogeneous, where low-velocity segments often dictate
task success through precision-demanding interactions, while high-velocity motions serve
as error-tolerant transitions. Such a misalignment between uniform loss weighting and
physical criticality fundamentally limits the performance of current Vision-Language-
Action (VLA) models and World-Action Models (WAM) in complex, long-horizon tasks. To
rectify this, we introduce AttenA+, an architecture-agnostic framework that prioritizes
kinematically critical segments via velocity-driven action attention. By reweighting the
training objective based on the inverse velocity field, AttenA+ naturally aligns the
model's learning capacity with the physical demands of manipulation. As a plug-and-play
enhancement, AttenA+ can be integrated into existing backbones without structural
modifications or additional parameters. Extensive experiments demonstrate that AttenA+
significantly elevates the ceilings of current state-of-the-art models. Specifically, it
improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to
92.4% (+0.6%) on RoboTwin 2.0. Real-world validation on a Franka manipulator further
showcases its robustness and cross-task generalization. Our work suggests that mining
the intrinsic structural priors of action sequences offers a highly efficient, physics-
aware complement to standard scaling laws, paving a new path for general-purpose robotic
control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13548v1
- Authors: Daojie Peng, Fulong Ma, Jiahang Cao, Qiang Zhang, Xupeng Xie, Jian Guo, Ping Luo, Andrew F. Luo, Boyu Zhou, Jun Ma
- Published: 2026-05-13T13:55:37Z
- Age days: 0

</details>
