---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11767v1"
published: "2026-06-10T07:46:38Z"
age_days: 1
score: 35
created: 2026-06-12
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning

> [!summary] 一句话结论（基于摘要）
> The deployed policy achieves a 27\% real-world grasp success rate across all 20 objects, without real-world grasping demonstrations or visual input.

## 关键点

- **问题**：Nevertheless, learning such tactile-only policies for real robots remains challenging due to the tactile sim-to-real gap and the limited expressiveness of sparse tactile signals.
- **创新点 / 方法**：To bridge this gap, we propose a framework for tactile-only blind grasping that is deployable on a physical multi-fingered robotic hand.
- **证据**：The deployed policy achieves a 27\% real-world grasp success rate across all 20 objects, without real-world grasping demonstrations or visual input.
- **局限**：Nevertheless, learning such tactile-only policies for real robots remains challenging due to the tactile sim-to-real gap and the limited expressiveness of sparse tactile signals.

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Blind grasping with a dexterous hand is a crucial manipulation capability. Nevertheless,
learning such tactile-only policies for real robots remains challenging due to the
tactile sim-to-real gap and the limited expressiveness of sparse tactile signals. To
bridge this gap, we propose a framework for tactile-only blind grasping that is
deployable on a physical multi-fingered robotic hand. Our approach combines three key
components. First, we introduce a Real2Sim tactile calibration pipeline that constructs
a contact-calibrated digital-twin simulator capable of reproducing real tactile signals.
Second, we improve the expressiveness of sparse tactile observations using a layout-
aware tactile encoder, which incorporates sensor-geometry priors through self-supervised
pretraining. Third, to improve generalization to unseen objects, we train object-
specific reinforcement-learning experts in the calibrated simulator and aggregate their
successful grasp trajectories into a tactile-conditioned Diffusion Policy. We evaluate
our method on a physical LEAP Hand equipped with distributed tactile sensing across 10
seen and 10 unseen objects. The deployed policy achieves a 27\% real-world grasp success
rate across all 20 objects, without real-world grasping demonstrations or visual input.
Simulation ablations show that layout-aware tactile pretraining improves grasping
performance, while sensing-level evaluations confirm that Real2Sim calibration increases
the consistency of tactile contact events between simulation and hardware. Together,
these results suggest that contact-event calibration, geometry-aware tactile
representation learning, and diffusion-based policy aggregation provide an effective
path toward tactile-only blind grasping on real dexterous robotic hands. Project
page:Dex-Blind-Grasp.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11767v1
- Authors: Shengcheng Luo, Xiyan Huang, Zhe Xu, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
- Published: 2026-06-10T07:46:38Z
- Age days: 1

</details>
