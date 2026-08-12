---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17970v1"
published: "2026-07-20T14:10:19Z"
age_days: 1
score: 30
created: 2026-07-22
concepts: ["多模态基础模型", "机器人学习"]
---

# MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

> [!summary] 一句话结论（基于摘要）
> We demonstrate that MEVION enables data collection for object manipulation tasks not previously possible and supports imitation learning-based motion generation.

## 关键点

- **问题**：However, due to its limited ability to generate high forces and speeds, it is difficult to handle heavy objects or perform fast manipulations.
- **创新点 / 方法**：To address this, we developed MEVION, a low-cost and open-source dual-arm robot data collection system capable of generating greater force and speed.
- **证据**：We demonstrate that MEVION enables data collection for object manipulation tasks not previously possible and supports imitation learning-based motion generation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-22/MEVION Low-Cost Open-Source Data Collection System for Powerful and High-Speed D.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The global competition for developing robotic foundation models is intensifying. Among
the data collection systems used for dual-arm robots, ALOHA is representative of being
low-cost and open-source, and is widely adopted by researchers as a de facto standard.
However, due to its limited ability to generate high forces and speeds, it is difficult
to handle heavy objects or perform fast manipulations. To address this, we developed
MEVION, a low-cost and open-source dual-arm robot data collection system capable of
generating greater force and speed. All parts of this robot can be sourced through
e-commerce, and by extensively utilizing sheet metal welding, its large body structure
is constructed with a small number of components at low cost, while also simplifying
assembly. MEVION is equipped with four 6-DoF arms with parallel grippers. Each arm
weighs 7.0 kg and has a maximum torque of 60 Nm, and the entire system can be
constructed for about USD 14,000. The elbow joint adopts a closed-link mechanism similar
to those used in quadruped robots, which reduces the distal mass and enables higher
force and speed output at the end-effector. We demonstrate that MEVION enables data
collection for object manipulation tasks not previously possible and supports imitation
learning-based motion generation. All hardware and software of this work are included in
the Supplementary Materials or https://github.com/haraduka/mevion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17970v1
- Authors: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida, Jihoon Oh, Temma Suzuki, Shintaro Inoue, Keita Yoneda, Ayumu Iwata, Kei Okada
- Published: 2026-07-20T14:10:19Z
- Age days: 1

</details>
