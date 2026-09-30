---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.22629v1"
published: "2026-08-23T22:25:33Z"
age_days: 2
score: 35
created: 2026-08-26
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Enhancing Sim2Real Transfer for Torque-Controlled Robots through Real2Sim Dynamics Estimation and Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Our results demonstrate a significant improvement in tracking accuracy and policy robustness after parameter tuning, with smooth policy transfer from simulation to the Real-World across multiple target-reaching tasks.

## 关键点

- **问题**：Transferring reinforcement learning policies from simulation to Real-World robots remains a major challenge, particularly when dealing with low-level torque control, where even small modelling inaccuracies can lead to unstable or unsafe behaviours.
- **创新点 / 方法**：In this work, we propose a Real2Sim2Real pipeline that improves Sim2Real transfer for torque-controlled robotic arms by combining trajectory matching, parameter optimization via genetic algorithms, and domain randomization.
- **证据**：Our results demonstrate a significant improvement in tracking accuracy and policy robustness after parameter tuning, with smooth policy transfer from simulation to the Real-World across multiple target-reaching tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Enhancing Sim2Real Transfer for Torque-Controlled Robots through Real2Sim Dynami.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Transferring reinforcement learning policies from simulation to Real-World robots remains a major challenge, particularly when dealing with low-level torque control, where even small modelling inaccuracies can lead to unstable or unsafe behaviours. In this work, we propose a Real2Sim2Real pipeline that improves Sim2Real transfer for torque-controlled robotic arms by combining trajectory matching, parameter optimization via genetic algorithms, and domain randomization. Using the 7-DOF Franka Emika Panda robot, we first identify friction, inertia, and gravity compensation parameters by minimizing the error between real and simulated joint trajectories. These calibrated dynamics are then used to train a TQC-based reinforcement learning agent in simulation. The trained policy is evaluated in both Gazebo and MuJoCo environments, and finally deployed on the real robot. Our results demonstrate a significant improvement in tracking accuracy and policy robustness after parameter tuning, with smooth policy transfer from simulation to the Real-World across multiple target-reaching tasks. This work highlights the effectiveness of accurate physical modelling in enabling stable and generalizable torque-based reinforcement learning policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.22629v1
- Authors: Davide Bargellini, Alex Pasquali, Andrea Govoni, Riccardo Zanella, Gianluca Palli
- Published: 2026-08-23T22:25:33Z
- Age days: 2

</details>
