---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23147v1"
published: "2026-06-22T10:47:12Z"
age_days: 1
score: 32
created: 2026-06-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Empirical results demonstrate that Assistron significantly improves task success rates over pure autonomous baselines while significantly reducing human cognitive and physical workload compared to traditional teleoperation, offering a scalable, smooth, and ef…

## 关键点

- **问题**：Our approach is grounded in two core principles: (1)~minimizing human cognitive and physical effort by leveraging VLA- driven autonomy for macro-movements, and (2)~prioritizing human intervention specifically at critical failure points.
- **创新点 / 方法**：We propose Assistron, a shared autonomy model that leverages Vision-Language-Action (VLA) models to assist the user in daily activities.
- **证据**：Empirical results demonstrate that Assistron significantly improves task success rates over pure autonomous baselines while significantly reducing human cognitive and physical workload compared to traditional teleoperation, offering a scalable, smooth, and effortless paradigm for assistive manipulation.
- **局限**：Critically, our formulation eliminates the need for VLA fine-tuning, protecting its broad behavioral priors from catastrophic forgetting and ensuring the model does not become a narrow specialist.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We propose Assistron, a shared autonomy model that leverages Vision-Language-Action
(VLA) models to assist the user in daily activities. Our approach is grounded in two
core principles: (1)~minimizing human cognitive and physical effort by leveraging VLA-
driven autonomy for macro-movements, and (2)~prioritizing human intervention
specifically at critical failure points. Driven by the user's verbal language commands,
Assistron utilizes the VLA to autonomously execute macro-reaching trajectories, saving
users' effort. In contact-rich interactions where VLAs tend to fail, Assistron employs a
phase-aware interaction detection mechanism and solicits the user to intervene, in turn
adjusting the VLA's action generation via flow matching guidance. Critically, our
formulation eliminates the need for VLA fine-tuning, protecting its broad behavioral
priors from catastrophic forgetting and ensuring the model does not become a narrow
specialist. We validate our approach on a comprehensive multi-task scene recovery
benchmark encompassing diverse daily manipulation skills. Empirical results demonstrate
that Assistron significantly improves task success rates over pure autonomous baselines
while significantly reducing human cognitive and physical workload compared to
traditional teleoperation, offering a scalable, smooth, and effortless paradigm for
assistive manipulation. The code is available in
https://github.com/mousecpn/Assistron.git.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23147v1
- Authors: Pinhao Song, Ze Fu, Yutong Hu, Renaud Detry
- Published: 2026-06-22T10:47:12Z
- Age days: 1

</details>
