---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14218v1"
published: "2026-06-12T07:57:13Z"
age_days: 3
score: 23
created: 2026-06-16
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback

> [!summary] 一句话结论（基于摘要）
> We demonstrate that this combination of capabilities enables learning bimanual, whole-body, and active compliant policies that operate effectively in highly constrained spaces.

## 关键点

- **问题**：However, the majority of existing data collection pipelines still lack the ability to capture force and torque data for learning active compliant policies.
- **创新点 / 方法**：In this paper, we present Universal Manipulation Exoskeleton (UME), an upper-limb exoskeleton that provides real-time haptic torque feedback while recording whole-arm configurations and joint torque signals for teleoperation.
- **证据**：We demonstrate that this combination of capabilities enables learning bimanual, whole-body, and active compliant policies that operate effectively in highly constrained spaces.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

For robots to work safely in household environments, they need to be compliant and react
to torque and force feedback during contact. However, the majority of existing data
collection pipelines still lack the ability to capture force and torque data for
learning active compliant policies. In this paper, we present Universal Manipulation
Exoskeleton (UME), an upper-limb exoskeleton that provides real-time haptic torque
feedback while recording whole-arm configurations and joint torque signals for
teleoperation. With transparent torque feedback, human operators can even unsheathe
kinematically constrained objects while blindfolded. UME is low-cost, lightweight, and
portable. Equipped with an embedded IMU, it enables teleoperation for mobile
manipulation. With our proposed universal retargeting algorithm, UME can teleoperate a
range of robots, including the 7DoF OpenArm, 7DoF Franka, and 6DoF X-ARM. We demonstrate
that this combination of capabilities enables learning bimanual, whole-body, and active
compliant policies that operate effectively in highly constrained spaces. The learned
robust autonomous policies achieve high success rates across a variety of tasks,
including long-horizon mobile manipulation, force-mediated box flipping, visually
occluded box pushing, and space-constrained tabletop manipulation. Videos, code, and
additional information can be found at https://ume-exo.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14218v1
- Authors: Litian Liang, Jingxi Xu, Xinda Qi, Yujun Cai, Houzhu Ding, Luqi Wang, Zhixin Sun, Jyh-Herng Chow, Ming Yang, Mark Cutkosky
- Published: 2026-06-12T07:57:13Z
- Age days: 3

</details>
