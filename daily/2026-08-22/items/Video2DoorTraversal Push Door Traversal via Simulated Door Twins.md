---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20251v1"
published: "2026-08-20T16:46:57Z"
age_days: 1
score: 25
created: 2026-08-22
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Video2DoorTraversal: Push Door Traversal via Simulated Door Twins

> [!summary] 一句话结论（基于摘要）
> With all perception and policy inference running onboard, the system achieves a 96.57% average success rate across five real doors and an 80.95% zero-shot success rate on structurally similar unseen doors, while completing the full approach, opening, and trav…

## 关键点

- **问题**：Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated base-arm control.
- **创新点 / 方法**：We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile manipulators.
- **证据**：With all perception and policy inference running onboard, the system achieves a 96.57% average success rate across five real doors and an 80.95% zero-shot success rate on structurally similar unseen doors, while completing the full approach, opening, and traversal sequence in approximately 13s on average.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Video2DoorTraversal Push Door Traversal via Simulated Door Twins.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated base-arm control. We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile manipulators. Given one RGB video of a real door, DoorTwin reconstructs an instance-aligned, articulated, and simulation-ready door twin with realistic geometry and appearance. A simulation-in-the-loop agent converts the recovered articulation into a parameterized skill program and iteratively refines failed rollouts to generate physically executable demonstrations. These demonstrations are used to train ArticuACT, a dual-depth policy that predicts coordinated base, arm, and gripper commands using robot-centric camera conditioning and interaction-aware supervision. With all perception and policy inference running onboard, the system achieves a 96.57% average success rate across five real doors and an 80.95% zero-shot success rate on structurally similar unseen doors, while completing the full approach, opening, and traversal sequence in approximately 13s on average. Project Page: https://video2doortraversal.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20251v1
- Authors: Xincheng Tang, Yiji Chen, Youhan Xie, Wanyu Li, Zhengjie Shu, Lai Jiang, Wenkang Hu, Yitong Li, Jinchuang Zhang, Xibin Song, Ruigang Yang
- Published: 2026-08-20T16:46:57Z
- Age days: 1

</details>
