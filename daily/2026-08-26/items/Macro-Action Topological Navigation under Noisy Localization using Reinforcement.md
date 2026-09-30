---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.23055v1"
published: "2026-08-24T09:57:43Z"
age_days: 1
score: 28
created: 2026-08-26
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Macro-Action Topological Navigation under Noisy Localization using Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> We build an agent that does it anyway, estimating its own pose from the camera alone.

## 关键点

- **问题**：Navigating large, photorealistic 3D apartments from raw pixels is widely considered infeasible for plain reinforcement learning.
- **创新点 / 方法**：We build an agent that does it anyway, estimating its own pose from the camera alone.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Macro-Action Topological Navigation under Noisy Localization using Reinforcement.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Navigating large, photorealistic 3D apartments from raw pixels is widely considered infeasible for plain reinforcement learning. We build an agent that does it anyway, estimating its own pose from the camera alone. The agent has to reach several target objects in sequence, and their positions change between episodes, so it must explore to find them. It builds on our earlier object-centric topological controller, which still read the agent's true pose and its object detections from the simulator. Here we replace that true pose with an onboard, object-centric estimate. For each object we keep a bank of ORB features that, when the object is seen again, yield a rough pose measurement, which a minimal Extended Kalman Filter (EKF) fuses with a motion model. As on a real robot, the executed motions are noisy. The estimate drifts, but the agent and the nearby objects drift together, so a locally consistent pose is enough to follow each short edge and then home in visually on the target, which lets us replace full SLAM with a much smaller model, closer to how biological navigation appears to work. In the photorealistic Habitat simulator, the agent reaches its target objects from vision alone, with a pose that only needs to be locally consistent.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.23055v1
- Authors: Simon Hakenes, Tobias Glasmachers
- Published: 2026-08-24T09:57:43Z
- Age days: 1

</details>
