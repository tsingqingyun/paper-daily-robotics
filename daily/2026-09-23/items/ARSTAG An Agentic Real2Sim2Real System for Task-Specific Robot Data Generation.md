---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24563v1"
published: "2026-09-21T13:25:05Z"
age_days: 1
score: 35
created: 2026-09-23
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation

> [!summary] 先说人话（基于摘要）
> ARSTAG把一张现场图片和一句任务描述转成机器人训练示范。多个语言Agent负责搭仿真场景、生成可执行轨迹和随机化数据，再将训练好的策略迁移到真实机器人。

## 问题

新操作任务往往需要手工工程或遥操作采集；即使使用仿真，建场景、设计专家行为和配置数据生成仍有显著的逐任务成本。

## 创新点或方法

分层Agent构造任务所需的仿真场景，生成机器人可行的示范，并进行保持任务一致性的随机化；协调Agent处理各阶段反馈和失败恢复。

## 证据

7项抓取、放置和堆叠任务上，生成数据支持3种视觉运动策略迁移至真实双臂机器人；π₀.₅平均真实成功率74.6%。消融显示任务一致随机化改善鲁棒性，数据增多时策略表现提升。

## 局限

需核查单图之外使用了哪些资产、机器人和环境先验，以及人工介入程度；摘要未量化端到端构建成本。

- **判断**：值得读系统实现与失败恢复流程，尤其适合关注逐任务数据生产成本的研究者。

## 研究关联

对Sim2Real与机器人学习，实际价值是降低任务数据生成中的工程负担，并把Agent用于训练流程自动化。

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/ARSTAG An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Adapting visuomotor policies to new manipulation tasks often requires substantial manual engineering or teleoperated data collection. Simulation can provide task-specific data at scale, but constructing the scene, designing expert behavior, and configuring data generation still require significant per-task effort. We present ARSTAG, an agentic Real2Sim2Real system that turns a single RGB image and a natural-language instruction directly into robot policy-learning data. A hierarchy of language agents constructs a task-scoped simulation scene, generates robot-feasible demonstrations, and expands the training distribution through task-consistent randomization, while a coordinator agent manages cross-stage feedback and recovery. Across seven manipulation tasks spanning grasping, placement, and stacking, the ARSTAG-generated demonstrations enable sim-to-real transfer of three visuomotor policy architectures to a dual-arm robot, with pi0.5 achieving an average real-world success rate of 74.6%. Ablations show that task-consistent randomization substantially improves robustness, and policy performance increases with generated dataset size. Project webpage: https://boweili666.github.io/ARSTAG/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24563v1
- Authors: Bowei Li, Yuner Zhang, Changliu Liu
- Published: 2026-09-21T13:25:05Z
- Age days: 1

</details>
