---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12859v1"
published: "2026-06-11T03:42:33Z"
age_days: 1
score: 31
created: 2026-06-13
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots

> [!summary] 一句话结论（基于摘要）
> The overall task completion score improves by 80.2\% compared to the single-head $π_{0.5}$ policy, effectively mitigating the heterogeneous coordinated control conflicts of composite robots.

## 关键点

- **问题**：Aerial manipulation systems have long suffered from representation coupling in end-to- end control, as platform-level Unmanned Aerial Vehicle (UAV) movement and end-effector- level arm manipulation differ substantially in action scale, dynamics, and control objectives.
- **创新点 / 方法**：In this paper, we propose AIR-VLA+, a flow matching action generation architecture specifically designed for aerial manipulation, featuring cascaded dual- action decoders and an asymmetric feature-level Mixture of Experts (MoE).
- **证据**：The overall task completion score improves by 80.2\% compared to the single-head $π_{0.5}$ policy, effectively mitigating the heterogeneous coordinated control conflicts of composite robots.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Aerial manipulation systems have long suffered from representation coupling in end-to-
end control, as platform-level Unmanned Aerial Vehicle (UAV) movement and end-effector-
level arm manipulation differ substantially in action scale, dynamics, and control
objectives. In this paper, we propose AIR-VLA+, a flow matching action generation
architecture specifically designed for aerial manipulation, featuring cascaded dual-
action decoders and an asymmetric feature-level Mixture of Experts (MoE). We construct
cascaded manipulation and movement decoders, allowing the UAV to unidirectionally
observe the manipulator's intent during movement to achieve workflow coordination, while
isolating the impact of UAV movement information backpropagation on arm manipulation
stability. Addressing the characteristic that UAV movement is highly dependent on high-
level semantics and responsible for task state transitions in aerial manipulation, we
design an input feature enhancement module for the UAV movement decoder. This module
introduces an implicit visual grasp projector to perceive the interaction state between
the gripper and the object, and injects compressed global semantic features. Within the
UAV movement decoder, we deploy an implicit MoE architecture, enabling different
movement experts to spontaneously exhibit capacity inclinations for various task stages
during training. Through dense soft blending computation on the feature manifold, the
UAV movement is endowed with stronger task-stage adaptability. Experiments on the
standardized AIR-VLA benchmark demonstrate that our method comprehensively surpasses all
baselines with an overall average score of 48.0. The overall task completion score
improves by 80.2\% compared to the single-head $π_{0.5}$ policy, effectively mitigating
the heterogeneous coordinated control conflicts of composite robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12859v1
- Authors: Jianli Sun, Bin Tian, Qiyao Zhang, Zijian Liu, Yutong Wang, Zhiyong Cui, Bai Li, Yisheng Lv, Yonglin Tian
- Published: 2026-06-11T03:42:33Z
- Age days: 1

</details>
