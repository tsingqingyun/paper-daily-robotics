---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13757v1"
published: "2026-05-13T16:38:05Z"
age_days: 0
score: 35
created: 2026-05-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FrameSkip: Learning from Fewer but More Informative Frames in VLA Training

> [!summary] 一句话结论（基于摘要）
> Across RoboCasa-GR1, SimplerEnv, and LIBERO, FrameSkip improves the success-retention trade-off over full-frame training and simpler frame selection variants, achieving a macro-average success rate of 76.15% across the three benchmarks compared with 66.50% fo…

## 关键点

- **问题**：Vision-Language-Action (VLA) policies are commonly trained from dense robot demonstration trajectories, often collected through teleoperation, by sampling every recorded frame as if it provided equally useful supervision.
- **创新点 / 方法**：We introduce FrameSkip, a data-layer frame selection framework that scores trajectory frames using action variation, visual-action coherence, task-progress priors, and gripper-transition preservation, then remaps training samples toward high-importance frames under a target retention ratio.
- **证据**：Across RoboCasa-GR1, SimplerEnv, and LIBERO, FrameSkip improves the success-retention trade-off over full-frame training and simpler frame selection variants, achieving a macro-average success rate of 76.15% across the three benchmarks compared with 66.50% for full-frame training while using a compressed trajectory vi…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies are commonly trained from dense robot
demonstration trajectories, often collected through teleoperation, by sampling every
recorded frame as if it provided equally useful supervision. We argue that this
convention creates a temporal supervision imbalance: long low-change segments dominate
the training stream, while manipulation-critical transitions such as alignment, contact,
grasping, and release appear only sparsely. We introduce FrameSkip, a data-layer frame
selection framework that scores trajectory frames using action variation, visual-action
coherence, task-progress priors, and gripper-transition preservation, then remaps
training samples toward high-importance frames under a target retention ratio. Because
FrameSkip operates only in the dataloader, it leaves the VLA architecture, action head,
training objective, and inference procedure unchanged. Across RoboCasa-GR1, SimplerEnv,
and LIBERO, FrameSkip improves the success-retention trade-off over full-frame training
and simpler frame selection variants, achieving a macro-average success rate of 76.15%
across the three benchmarks compared with 66.50% for full-frame training while using a
compressed trajectory view that retains 20% of unique frames in the main setting.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13757v1
- Authors: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Changti Wu, Hang Yuan, Haishan Liu, Bailing Wang, Cong Huang, Kai Chen
- Published: 2026-05-13T16:38:05Z
- Age days: 0

</details>
