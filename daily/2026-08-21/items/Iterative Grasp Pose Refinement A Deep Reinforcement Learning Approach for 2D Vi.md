---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17628v1"
published: "2026-08-18T10:44:58Z"
age_days: 2
score: 27
created: 2026-08-21
concepts: ["机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Iterative Grasp Pose Refinement: A Deep Reinforcement Learning Approach for 2D Vision

> [!summary] 一句话结论（基于摘要）
> Experiments conducted on 300 objects from the Dex-Net dataset using a UR5 manipulator demonstrate the framework's effectiveness, achieving a 100% success rate on objects previously deemed ungraspable by geometrical methods.

## 关键点

- **问题**：The findings underscore the effectiveness of reinforcement learning in addressing challenges in robotic grasping, offering a scalable and adaptable solution for contact-rich manipulation tasks.
- **创新点 / 方法**：This work proposes a reinforcement learning-based framework for robotic grasp refinement, integrating keypoint-based object representations with a Deep Q-Network (DQN).
- **证据**：Experiments conducted on 300 objects from the Dex-Net dataset using a UR5 manipulator demonstrate the framework's effectiveness, achieving a 100% success rate on objects previously deemed ungraspable by geometrical methods.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Iterative Grasp Pose Refinement A Deep Reinforcement Learning Approach for 2D Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Developing robots capable of understanding and manipulating objects requires compact, interpretable, and generalizable representations. This work proposes a reinforcement learning-based framework for robotic grasp refinement, integrating keypoint-based object representations with a Deep Q-Network (DQN). Using 2D overhead images captured in a simulated environment, a geometric-based algorithm generates initial grasp candidates, which are iteratively refined by the proposed framework, transforming failed grasps into successful ones. Experiments conducted on 300 objects from the Dex-Net dataset using a UR5 manipulator demonstrate the framework's effectiveness, achieving a 100% success rate on objects previously deemed ungraspable by geometrical methods. The framework's sim-to-real transferability is further validated through physical experiments on a Delta parallel robot, where a refined grasp successfully manipulates an object that was previously ungraspable. The findings underscore the effectiveness of reinforcement learning in addressing challenges in robotic grasping, offering a scalable and adaptable solution for contact-rich manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17628v1
- Authors: Amir Arsalan Nematollahi, Shayan Ahmadi, Mehdi Tale Masouleh, Ahmad Kalhor
- Published: 2026-08-18T10:44:58Z
- Age days: 2

</details>
