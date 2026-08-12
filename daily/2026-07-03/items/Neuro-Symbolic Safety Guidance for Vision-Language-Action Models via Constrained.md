---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01378v1"
published: "2026-07-01T18:41:33Z"
age_days: 1
score: 40
created: 2026-07-03
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching

> [!summary] 一句话结论（基于摘要）
> On the SafeLIBERO benchmark, our method achieves 82.8% collision avoidance and 81.6% task success, a 6.3% and 19.8% improvement respectively over single- step methods, with the largest gains on long-horizon tasks where compounding distribution shift is most p…

## 关键点

- **问题**：Vision-Language-Action (VLA) models have demonstrated promising generalization capabilities across robotic manipulation tasks, yet their real-world deployment remains limited by the lack of effective safety measures.
- **创新点 / 方法**：In this paper, we propose a neuro-symbolic safety guidance mechanism for flow matching based VLAs that enables predictive collision avoidance.
- **证据**：On the SafeLIBERO benchmark, our method achieves 82.8% collision avoidance and 81.6% task success, a 6.3% and 19.8% improvement respectively over single- step methods, with the largest gains on long-horizon tasks where compounding distribution shift is most pronounced.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have demonstrated promising generalization
capabilities across robotic manipulation tasks, yet their real-world deployment remains
limited by the lack of effective safety measures. Specifically, existing safety measures
only prevent collisions caused by the robot's next action. In this paper, we propose a
neuro-symbolic safety guidance mechanism for flow matching based VLAs that enables
predictive collision avoidance. Flow matching based VLAs determine the next actions by
predicting a trajectory (a sequence of actions) through an iterative neural flow
matching process. Our method formulates safety enforcement as a minimum-norm constrained
optimization problem that corrects safety violations during the denoising process of
noisy intermediate trajectory predictions. By analyzing predicted trajectories and
applying corrections during iterative denoising, our approach anticipates collisions
before they become unavoidable. This interleaving of symbolic constraint satisfaction
with neural trajectory generation enables predictive collision avoidance rather than
reactive intervention. On the SafeLIBERO benchmark, our method achieves 82.8% collision
avoidance and 81.6% task success, a 6.3% and 19.8% improvement respectively over single-
step methods, with the largest gains on long-horizon tasks where compounding
distribution shift is most pronounced. Video demonstrations of our approach are included
on our project page at https://willenglish.tech/SafetyGuidedFlowMatching/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01378v1
- Authors: William English, Hao Zheng, Rickard Ewetz
- Published: 2026-07-01T18:41:33Z
- Age days: 1

</details>
