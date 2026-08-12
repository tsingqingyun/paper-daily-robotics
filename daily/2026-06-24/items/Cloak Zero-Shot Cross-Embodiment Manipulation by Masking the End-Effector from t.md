---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22836v1"
published: "2026-06-22T04:16:05Z"
age_days: 1
score: 40
created: 2026-06-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA

> [!summary] 一句话结论（基于摘要）
> We demonstrate the recipe with Cloak-VLA, a VLA trained with Cloak on a single parallel-jaw gripper dataset.

## 关键点

- **问题**：We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist camera.
- **创新点 / 方法**：We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist camera.
- **证据**：We demonstrate the recipe with Cloak-VLA, a VLA trained with Cloak on a single parallel-jaw gripper dataset.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/Cloak Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from t.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model
with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist
camera. The end-effector occupies a large and consistent region of the wrist view and
masking it allows for embodiment-agnostic visual reasoning. Cloak renders a mask in
simulation from the robot's known geometry, accurately and in real time, with no
segmentation or generative models. During training, we augment the mask so the model
generalizes to embodiments unseen at training time. We demonstrate the recipe with
Cloak-VLA, a VLA trained with Cloak on a single parallel-jaw gripper dataset. No data of
new embodiments is ever collected. Cloak-VLA transfers zero-shot to various unseen
embodiments, including another gripper, another arm, and a five-fingered hand, while
preserving the source embodiment's performance. By decoupling the wrist view from its
own embodiment, Cloak allows data to outlive the hardware it was collected on.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22836v1
- Authors: Michael Piseno, Guy Tevet, C. Karen Liu
- Published: 2026-06-22T04:16:05Z
- Age days: 1

</details>
