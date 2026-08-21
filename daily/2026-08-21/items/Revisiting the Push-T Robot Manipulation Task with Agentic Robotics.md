---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18227v1"
published: "2026-08-18T18:16:15Z"
age_days: 2
score: 41
created: 2026-08-21
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics

> [!summary] 一句话结论（基于摘要）
> Results suggest that the agent found the 2D gym simulation online, and used sim experiments to learn push mechanics, iteratively optimizing to achieve 100% success rate using 46% fewer steps than the best diffusion policy trained with 200 human demonstrations.

## 关键点

- **问题**：Push-T is an iconic benchmark for learning manipulation policies from human demonstrations.
- **创新点 / 方法**：The robot must use a single point of contact to push a T-shaped block into a target pose.
- **证据**：Results suggest that the agent found the 2D gym simulation online, and used sim experiments to learn push mechanics, iteratively optimizing to achieve 100% success rate using 46% fewer steps than the best diffusion policy trained with 200 human demonstrations.
- **局限**：In this short paper, we revisit the Push-T task in the context of emerging advances in Agentic Robotics where an LLM coding agent -- Claude Code with Fable 5 -- is prompted to create an algorithmic solution that does not require any demonstration data.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Revisiting the Push-T Robot Manipulation Task with Agentic Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Push-T is an iconic benchmark for learning manipulation policies from human demonstrations. The robot must use a single point of contact to push a T-shaped block into a target pose. In this short paper, we revisit the Push-T task in the context of emerging advances in Agentic Robotics where an LLM coding agent -- Claude Code with Fable 5 -- is prompted to create an algorithmic solution that does not require any demonstration data. We study how effective the agentic coding loop can solve the Push-T task, and compare the resulting code as policy with the visuomotor imitation learning policy. Results suggest that the agent found the 2D gym simulation online, and used sim experiments to learn push mechanics, iteratively optimizing to achieve 100% success rate using 46% fewer steps than the best diffusion policy trained with 200 human demonstrations. The coding agent also solve extensions from T to the full alphabet (Push-A to Push-Z) using a self generated curriculum and generated simulation code for the Franka and UR5 robot arms in 3D cross-embodiment simulations with visual feedback. Videos, policies and details will be posted online.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18227v1
- Authors: Shuangyu Xie, Kaiyuan Chen, Ken Goldberg
- Published: 2026-08-18T18:16:15Z
- Age days: 2

</details>
