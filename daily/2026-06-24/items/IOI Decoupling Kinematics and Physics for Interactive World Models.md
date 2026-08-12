---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23296v1"
published: "2026-06-22T13:09:34Z"
age_days: 1
score: 35
created: 2026-06-24
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# IOI: Decoupling Kinematics and Physics for Interactive World Models

> [!summary] 一句话结论（基于摘要）
> IOI achieves state-of-the-art simulation performance and robust zero-shot generalization to unseen OOD tasks.

## 关键点

- **问题**：However, purely data-driven methods struggle to ensure precise control alignment and physically plausible visual feedback due to a lack of explicit structural constraints.
- **创新点 / 方法**：To address this, we propose IOI, a hybrid interactive world model integrating analytical kinematic priors with learned physical dynamics.
- **证据**：IOI achieves state-of-the-art simulation performance and robust zero-shot generalization to unseen OOD tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/IOI Decoupling Kinematics and Physics for Interactive World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Developing generalist embodied agents requires interactive environments providing
visually realistic feedback and accurate action-conditioned dynamics. Interactive world
models address this by simulating such complex dynamics. However, purely data-driven
methods struggle to ensure precise control alignment and physically plausible visual
feedback due to a lack of explicit structural constraints. To address this, we propose
IOI, a hybrid interactive world model integrating analytical kinematic priors with
learned physical dynamics. Unlike data-driven approaches prone to spatiotemporal drift,
IOI introduces explicit kinematic guidance, computing forward kinematics from action
sequences for accurate motion trajectories. These trajectories are rendered into
synchronized front, side, and top orthographic projections, eliminating the need for
extrinsic camera calibration. A Multi-view Kinematic Aggregation and Injection module
fuses these geometric cues and injects them into the video generator, providing
geometry-consistent guidance. Conditioning video generation on these deterministic
trajectories establishes a synergy between the analytical simulator and the world model.
Decoupling deterministic motion into the kinematic prior frees the generator to model
stochastic physical interactions. Experiments on the RoboTwin benchmark validate IOI
across kinematic fidelity, out-of-distribution (OOD) generalization, and policy
evaluation. IOI achieves state-of-the-art simulation performance and robust zero-shot
generalization to unseen OOD tasks. Furthermore, IOI serves as a reliable policy
evaluator, yielding success rates closely aligning with ground-truth physics simulators.
On real-world platforms, policies trained on IOI-synthesized data match those trained on
teleoperation demonstrations, solidifying its practical value for embodied policy
learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23296v1
- Authors: Chengyu Bai, Peidong Jia, Tiecheng Guo, Yukai Wang, Rui Ma, Fangyuan Zhao, Chunkai Fan, Xiaobao Wei, Jintao Chen, Hao Wang, Ying Li, Xiaozhu Ju, Jian Tang, Shanghang Zhang
- Published: 2026-06-22T13:09:34Z
- Age days: 1

</details>
