---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.30536v1"
published: "2026-08-31T10:03:48Z"
age_days: 0
score: 31
created: 2026-09-01
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks

> [!summary] 先说人话（基于摘要）
> Behavior-Skill 把长程任务拆成可恢复、可独立执行和判定的技能实例，使 VLA 评测能定位“具体哪种技能失败”，而不只看整段任务成败。

## 问题

长程移动操作由多个子技能串联，现有基准主要依赖完整 rollout 和任务级汇总指标，导致中间失败难以观察，无法形成可操作的能力诊断。

## 创新点或方法

每个实例将技能指令与对齐的观测—动作片段配对，并附带可恢复中间状态和技能成功条件，以保证在有效前置条件下独立评测；同时提供轨迹级和技能级指标。与全任务评测相比，它隔离子技能并形成细粒度能力画像。

## 证据

基准含 235,492 个技能实例，来自 10,000 条示范、50 个家庭任务和 34 类语义技能。对 π₀.₅、GR00T 等 VLA 的完整 50 任务实验显示失败在技能间高度不均匀，接触丰富型操作是持续瓶颈；未给各模型具体分数。


## 局限

独立技能评测可能弱化技能衔接、误差累积和恢复能力，需结合完整轨迹指标理解，不能替代端到端任务成功率。

- **判断**：强烈建议 VLA 评测和数据研究者精读；它未必给出新策略，却提供了比总成功率更有行动价值的故障定位工具。

## 研究关联

它能帮助 VLA 和机器人学习团队把模型迭代从追逐单一总成功率转成针对失败技能补数据、改策略或加触觉，也为长程评测提供诊断层。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/Behavior-Skill A Fine-Grained Benchmark for Evaluating Vision-Language-Action Po.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable execution of long-horizon mobile manipulation tasks remains challenging because overall task success depends on the successful completion of multiple constituent skills. Existing benchmarks, however, still rely primarily on full-task rollouts and aggregate task-level metrics, making intermediate failures difficult to observe and analyze. We present Behavior-Skill, a benchmark that reformulates the learning and evaluation of long-horizon tasks around executable constituent skills. It contains 235,492 skill instances from 10,000 demonstrations across 50 household tasks and 34 semantic skill categories. Each instance pairs a skill instruction with an aligned observation-action segment, and is further associated with a restorable intermediate state and a skill success condition to enable independent evaluation under valid preconditions. We further introduce trajectory-level and skill-level metrics to characterize policy capability beyond aggregate task success. Extensive experiments across representative VLA policies including pi0.5 and GR00T on the complete 50-task benchmark show that failures are highly non-uniform across skills, with contact-rich manipulation skills forming persistent bottlenecks. These results demonstrate that Behavior-Skill complements full-task evaluation by exposing intermediate capability profiles for analyzing and improving long-horizon VLA policies. Behavior-Skill is publicly available at https://github.com/nubot-nudt/Behavior-Skill.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.30536v1
- Authors: Chunyun Ma, Lun Luo, Xingjian Luo, Xiexing Feng, Hang Zhang, Wei Liu, Feng Qiao, Yaonan Wang, Huimin Lu, Xieyuanli Chen
- Published: 2026-08-31T10:03:48Z
- Age days: 0

</details>
