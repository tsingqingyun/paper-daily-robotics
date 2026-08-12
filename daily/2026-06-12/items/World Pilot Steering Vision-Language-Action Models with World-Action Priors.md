---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12403v1"
published: "2026-06-10T17:59:08Z"
age_days: 1
score: 39
created: 2026-06-12
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# World Pilot: Steering Vision-Language-Action Models with World-Action Priors

> [!summary] 一句话结论（基于摘要）
> World Pilot attains a state-of-the-art Total success rate of 84.7% on the LIBERO-Plus zero-shot OOD benchmark and the highest success rate on every real-robot setting across four manipulation tasks, with the largest margins under shifts in viewpoint, geometry…

## 关键点

- **问题**：This grounding, however, is built on static image-text pairs, whereas manipulation is a continuous, contact-rich process whose dynamics this pretraining cannot capture.
- **创新点 / 方法**：We present World Pilot, a VLA framework that augments the policy with priors from a World- Action Model (WAM), routed into the decision chain through two complementary pathways.
- **证据**：World Pilot attains a state-of-the-art Total success rate of 84.7% on the LIBERO-Plus zero-shot OOD benchmark and the highest success rate on every real-robot setting across four manipulation tasks, with the largest margins under shifts in viewpoint, geometry, deformable state, and pose.
- **局限**：This grounding, however, is built on static image-text pairs, whereas manipulation is a continuous, contact-rich process whose dynamics this pretraining cannot capture.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models inherit semantic grounding from large-scale
pretraining and perform competently across in-distribution manipulation tasks. This
grounding, however, is built on static image-text pairs, whereas manipulation is a
continuous, contact-rich process whose dynamics this pretraining cannot capture. We
present World Pilot, a VLA framework that augments the policy with priors from a World-
Action Model (WAM), routed into the decision chain through two complementary pathways.
Latent Steering conditions the perception layer on a scene-evolution latent, and Action
Steering supplies an anticipated trajectory as a motion prior to the action generator.
Together the two priors equip the VLA with an anticipated view of the scene and a
trajectory-level motion hint alongside its semantic conditioning, and the scene-
evolution prior remains effective even when supplied by a video-pretrained world model
that has not been action-post-trained. World Pilot attains a state-of-the-art Total
success rate of 84.7% on the LIBERO-Plus zero-shot OOD benchmark and the highest success
rate on every real-robot setting across four manipulation tasks, with the largest
margins under shifts in viewpoint, geometry, deformable state, and pose. Project
Website: https://world-pilot.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12403v1
- Authors: Zefu Lin, Rongxu Cui, Junjia Xu, Xiaojuan Jin, Wenling Li, Lue Fan, Zhaoxiang Zhang
- Published: 2026-06-10T17:59:08Z
- Age days: 1

</details>
