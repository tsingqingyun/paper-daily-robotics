---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37089v1"
published: "2026-09-29T09:16:49Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Real2Gym: Building Gyms from Videos, Bringing Skills to Robots

> [!summary] 先说人话（基于摘要）
> Real2Gym 把示范视频变成机器人能反复试错的交互式仿真环境，再把成功和失败整理成可复用技能。它通过代码执行、物理检查和共享控制接口，将仿真经验带到真实机器人，且不更新底层模型权重。

## 问题

视频里看起来合理的动作，并不自动构成可执行技能：还需要视觉对齐的场景、可信的物理交互和经验复用机制。单靠观看示范无法完成这条链路。

## 创新点或方法

重建可编辑场景并对齐物体与相机，用物理执行验证示范或重定向动作，再生成通过可行性检查的任务变体。智能体编写分阶段操作代码，从结果中提炼流程、相对物体运动和恢复策略，并按当前观察调整执行。

## 证据

摘要报告在重建环境中，相比 GPT-6 Astra Direct Mode 成功率提高 16.7%，策略执行 token 约减少 74.9%；真实 Franka 四项任务的执行成功率提高 33.3%。摘要未明确两项成功率增幅是否指百分点。

## 局限

需核查场景重建与技能探索的成本是否计入比较，以及成功率增幅口径；策略执行 token 的减少不等于总计算成本同比下降。

- **判断**：值得细读技能提炼、失败恢复和成本统计，实机四任务结果提供了依据，但迁移广度仍需全文判断。

## 研究关联

对 Agent 和 Sim2Real，价值是把环境重建与经验提炼连成闭环，让视频成为可练习、可复用的技能来源。它提供的是交互仿真和程序经验路径，摘要未描述生成式世界模型。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Real2Gym Building Gyms from Videos, Bringing Skills to Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world videos provide rich demonstrations of manipulation, but turning them into reusable robot skills requires visually aligned environments, executable physical interactions, and mechanisms for learning from experience. We introduce Real2Gym, an agentic Real2Sim2Real framework that turns human and robot demonstrations into interactive simulation gyms and brings skills acquired in simulation to physical robots. The Real2Sim module reconstructs editable scenes, aligns objects and cameras with the input, validates demonstrated or retargeted actions through native physics execution, and generates task-conditioned variations with action-feasibility checks. Within these environments, the agent generates executable code for manipulation stages, observes their outcomes, and distills successful attempts and failures into reusable task procedures, object-relative motions, and recovery strategies. Through a shared perception-and-control interface, these skills guide subsequent execution in simulation and on real robots, with motions adapted to current observations and no updates to the underlying model weights. Extensive evaluations demonstrate that Real2Gym enables high-fidelity simulation environment reconstruction, outperforming GPT-6 Astra Direct Mode by 16.7% in success rate with approximately 74.9% fewer policy-execution tokens across these environments, while exceeding it by 33.3% in physical robot execution success rate across four tasks on a real Franka robot.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37089v1
- Authors: Kerui Ren, Yingxiang Xu, Kaiwen Song, Linning Xu, Bo Dai, Mulin Yu, Tao Lu
- Published: 2026-09-29T09:16:49Z
- Age days: 0

</details>
