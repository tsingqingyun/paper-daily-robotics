---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20118v1"
published: "2026-06-18T11:41:25Z"
age_days: 1
score: 33
created: 2026-06-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation

> [!summary] 一句话结论（基于摘要）
> Fine-tuning a VLA on data augmented by our method improves success rates by 16.5% relative to the state-of-the-art baseline on novel objects, while preserving in- distribution performance.

## 关键点

- **问题**：The standard remedy is to collect multi-view teleoperation data for every failure case, but this scales poorly in both cost and time.
- **创新点 / 方法**：We introduce Pose6DAug, a failure-driven data augmentation framework that turns a policy's own successful episodes into targeted demonstrations for its failure modes, without any new data collection.
- **证据**：Fine-tuning a VLA on data augmented by our method improves success rates by 16.5% relative to the state-of-the-art baseline on novel objects, while preserving in- distribution performance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/Pose6DAug Physically Plausible Multi-view Object Swapping for Robot Data Augment.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies have shown strong potential for general-purpose
manipulation, yet they often fail on novel, out-of-distribution objects whose appearance
or geometry deviates from the training distribution. The standard remedy is to collect
multi-view teleoperation data for every failure case, but this scales poorly in both
cost and time. We introduce Pose6DAug, a failure-driven data augmentation framework that
turns a policy's own successful episodes into targeted demonstrations for its failure
modes, without any new data collection. Our key insight is that each successful episode
already encodes a physically valid action trajectory together with calibrated multi-view
observations. By swapping only the manipulated object while preserving this trajectory,
we obtain new and physically grounded demonstrations. However, naive 2D video editing
breaks multi-view consistency and physical plausibility, particularly under heavy
occlusion and egocentric viewpoints. Our method instead operates directly in 3D,
anchoring the target object with an explicit mesh driven by a temporally coherent 6D
pose trajectory, ensuring geometrically consistent renderings across all camera views.
Fine-tuning a VLA on data augmented by our method improves success rates by 16.5%
relative to the state-of-the-art baseline on novel objects, while preserving in-
distribution performance. These results show that multi-view and physically consistent
augmentation is a practical path to scalable VLA generalization.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20118v1
- Authors: Jonghoon Lee, Seong Hyeon Park, Byungwoo Jeon, Minha Lee, Jinwoo Shin
- Published: 2026-06-18T11:41:25Z
- Age days: 1

</details>
