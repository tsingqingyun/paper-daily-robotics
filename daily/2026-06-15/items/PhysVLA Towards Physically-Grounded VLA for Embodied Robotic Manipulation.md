---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13886v1"
published: "2026-06-11T20:23:09Z"
age_days: 3
score: 36
created: 2026-06-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Evaluated across OpenVLA, OpenVLA-OFT, Force-VLA, and Generalist-VLA on LIBERO-Spatial with a 7-DoF Franka Panda, the framework delivers absolute success rate increases of up to 17% and stability increases of up to 19% with no per-task regressions, improves t…

## 关键点

- **问题**：However, because they are trained primarily to fit behavioural demonstration data, they do not explicitly enforce fundamental physical principles such as rigid-body dynamics or contact constraints.
- **创新点 / 方法**：To bridge this gap, we introduce PhysVLA (Physics-VLA), a plug-and-play, inference-time framework designed to wrap any frozen VLA backbone without retraining, fine-tuning, or weight access, with less than 1 ms of overhead per control step.
- **证据**：Evaluated across OpenVLA, OpenVLA-OFT, Force-VLA, and Generalist-VLA on LIBERO-Spatial with a 7-DoF Franka Panda, the framework delivers absolute success rate increases of up to 17% and stability increases of up to 19% with no per-task regressions, improves trajectory efficiency by up to 15% across all four backbones…
- **局限**：This exposes a critical physics gap: standard temporal smoothing applied on top of single- step or chunked VLAs trades trajectory quality for added failures that short-term memory cannot resolve.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/PhysVLA Towards Physically-Grounded VLA for Embodied Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models excel at mapping visual inputs and natural language
instructions directly to robotic control policies. However, because they are trained
primarily to fit behavioural demonstration data, they do not explicitly enforce
fundamental physical principles such as rigid-body dynamics or contact constraints. This
exposes a critical physics gap: standard temporal smoothing applied on top of single-
step or chunked VLAs trades trajectory quality for added failures that short-term memory
cannot resolve. To bridge this gap, we introduce PhysVLA (Physics-VLA), a plug-and-play,
inference-time framework designed to wrap any frozen VLA backbone without retraining,
fine-tuning, or weight access, with less than 1 ms of overhead per control step. PhysVLA
intercepts the predicted control action, captures only the simulator or system state,
and applies a dual-layered correction: (i) a phase-aware finite-state machine that
structures discrete task segments (approach, grasp, transport, and place), and (ii) a
selective Euler-Lagrange gate that activates only when a dynamics oracle detects
kinodynamic inconsistency. Evaluated across OpenVLA, OpenVLA-OFT, Force-VLA, and
Generalist-VLA on LIBERO-Spatial with a 7-DoF Franka Panda, the framework delivers
absolute success rate increases of up to 17% and stability increases of up to 19% with
no per-task regressions, improves trajectory efficiency by up to 15% across all four
backbones, and shows up to a 10x improvement in trajectory jerk robustness on a
Robosuite Lift cross-simulator sweep. We further validate the framework on a real Agilex
Piper arm with a pick-and-place task, confirming that PhysVLA transfers to physical
hardware without retraining, with success-rate improvements of up to 50%, establishing
physical awareness as a composable, backbone-agnostic runtime module.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13886v1
- Authors: Namai Chandra, Shriram Damodaran, Lin Wang
- Published: 2026-06-11T20:23:09Z
- Age days: 3

</details>
