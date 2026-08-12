---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06491v1"
published: "2026-06-04T17:59:40Z"
age_days: 3
score: 40
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies

> [!summary] 一句话结论（基于摘要）
> Experiments in simulation and on real-world tasks demonstrate that TempoVLA achieves flexible speed control in both directions, while VSTA additionally boosts the default $1\times$ performance via better data utilization.

## 关键点

- **问题**：Robot manipulation alternates between low-risk transit phases that call for fast execution and high-risk contact stages that demand slow, precise motion.
- **创新点 / 方法**：Yet existing Vision-Language-Action models (VLAs) only inherit a single fixed speed from training demonstrations.
- **证据**：Experiments in simulation and on real-world tasks demonstrate that TempoVLA achieves flexible speed control in both directions, while VSTA additionally boosts the default $1\times$ performance via better data utilization.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/TempoVLA Learning Speed-Controllable Vision-Language-Action Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot manipulation alternates between low-risk transit phases that call for fast
execution and high-risk contact stages that demand slow, precise motion. Yet existing
Vision-Language-Action models (VLAs) only inherit a single fixed speed from training
demonstrations. Prior efforts to accelerate VLAs through model compression, KV-cache
reuse, or reinforcement learning only shift the policy from one fixed speed to another,
and leave deceleration almost unexplored. We observe that the magnitude of each
predicted action already governs how fast the robot moves, opening a direct route to
controllable execution speed. We turn this observation into TempoVLA, a single VLA whose
execution speed is controlled by an explicit condition. TempoVLA combines two coupled
components. (1) A data-side Variable-Speed Trajectory Augmentation (VSTA) that re-times
demonstration to any target speed by merging or splitting actions while preserving its
motion semantics. (2) A model-side conditioning mechanism that feeds the speed to the
policy. Statistics show that VSTA reaches the requested speed with negligible motion
error. Experiments in simulation and on real-world tasks demonstrate that TempoVLA
achieves flexible speed control in both directions, while VSTA additionally boosts the
default $1\times$ performance via better data utilization. Furthermore, by cooperating
with a large multimodal model, TempoVLA realizes dynamic speed control, accelerating
through low-risk phases and decelerating for high-risk ones.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06491v1
- Authors: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding
- Published: 2026-06-04T17:59:40Z
- Age days: 3

</details>
