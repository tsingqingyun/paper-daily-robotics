---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19661v1"
published: "2026-08-20T05:56:25Z"
age_days: 2
score: 25
created: 2026-08-22
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms

> [!summary] 一句话结论（基于摘要）
> For the ASV we further demonstrate a Vision language model (VLM)-assisted semantic-mapping pipeline that extracts obstacles and environmental context from satellite imagery, nautical charts, and forecast Application Programming Interface (API) instead of onbo…

## 关键点

- **问题**：In five benchmark missions per platform, both vehicles reach every goal with zero predicted collisions, and both transfer to GazeboSim under ocean current, waves, and thruster dynamics, remaining collision-free and cutting GazeboSim goal-distance error versus the ungrounded baseline by 70-82% (ASV) and roughly 93% (AU…
- **创新点 / 方法**：We proposed the use of a world model to expand the capabilities of Large Language model-based planners.
- **证据**：For the ASV we further demonstrate a Vision language model (VLM)-assisted semantic-mapping pipeline that extracts obstacles and environmental context from satellite imagery, nautical charts, and forecast Application Programming Interface (API) instead of onboard sensors, reaching 96% navigability accuracy as a drop-in…
- **局限**：Large language models can turn a natural-language mission into a sequence of robot actions, but they do not have a sense of physics: they cannot judge how long a command should run, or whether it will make the robot drift into an obstacle.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large language models can turn a natural-language mission into a sequence of robot actions, but they do not have a sense of physics: they cannot judge how long a command should run, or whether it will make the robot drift into an obstacle. We proposed the use of a world model to expand the capabilities of Large Language model-based planners. Our method has three components: a physics-grounded neural world model, a three-phase gradient-based trajectory optimizer, and a Model Predictive Controller (MPC)-style closed-loop replanner with a trust-region guard. The language model decides what to do, and the world model decides how long, whether that means driving eight thrusters through 6 DOF or two differential thrusters through 3 DOF. We evaluate two marine vehicle classes operating near offshore wind infrastructure: a 6-DOF Autonomous Underwater Vehicle (AUV) and a 3-DOF differential-drive Autonomous Surface Vehicle (ASV). In five benchmark missions per platform, both vehicles reach every goal with zero predicted collisions, and both transfer to GazeboSim under ocean current, waves, and thruster dynamics, remaining collision-free and cutting GazeboSim goal-distance error versus the ungrounded baseline by 70-82% (ASV) and roughly 93% (AUV), after a residual fine-tuning pass that separately reduces surrogate rollout Root Mean Square Error (RMSE) by 60% (AUV) and 69% (ASV). For the ASV we further demonstrate a Vision language model (VLM)-assisted semantic-mapping pipeline that extracts obstacles and environmental context from satellite imagery, nautical charts, and forecast Application Programming Interface (API) instead of onboard sensors, reaching 96% navigability accuracy as a drop-in replacement for hand-specified obstacle geometry.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19661v1
- Authors: Markus Buchholz, Ignacio Carlucho, Yvan R. Petillot
- Published: 2026-08-20T05:56:25Z
- Age days: 2

</details>
