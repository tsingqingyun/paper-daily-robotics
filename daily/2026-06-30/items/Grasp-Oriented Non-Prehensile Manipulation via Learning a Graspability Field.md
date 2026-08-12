---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30474v1"
published: "2026-06-29T15:33:27Z"
age_days: 0
score: 29
created: 2026-06-30
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Grasp-Oriented Non-Prehensile Manipulation via Learning a Graspability Field

> [!summary] 一句话结论（基于摘要）
> Non-prehensile manipulation is often used as a preparatory step for robotic grasping, yet existing approaches typically require a predefined target object pose.

## 关键点

- **问题**：In practice, however, objects admit multiple graspable configurations and the desired pose is not known in advance.
- **创新点 / 方法**：Non-prehensile manipulation is often used as a preparatory step for robotic grasping, yet existing approaches typically require a predefined target object pose.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Non-prehensile manipulation is often used as a preparatory step for robotic grasping,
yet existing approaches typically require a predefined target object pose. In practice,
however, objects admit multiple graspable configurations and the desired pose is not
known in advance. We reformulate non-prehensile manipulation for grasping as optimizing
an object centric graspability objective rather than reaching a specific pose. We
construct a graspable set from synthesized grasps and define a graspability field that
measures how suitable an object configuration is for successful grasp execution. The
scalar measure provides a dense learning signal for reinforcement learning and
determines when to terminate manipulation. This yields a closed-loop manipulation-to-
grasp pipeline driven by a single policy. Experiments in simulation and on a real robot
show that the policy reliably reconfigures objects into graspable states and transitions
to grasping without external planners or manually specified stopping conditions. The
predicted graspability distance correlates with real world grasp success, which
indicates that the learned representation captures grasp feasibility of object
configurations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30474v1
- Authors: Licheng Zhong, Gim Hee Lee
- Published: 2026-06-29T15:33:27Z
- Age days: 0

</details>
