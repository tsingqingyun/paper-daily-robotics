---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15701v1"
published: "2026-07-17T07:23:54Z"
age_days: 2
score: 30
created: 2026-07-20
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RAVEN: Reinforcement-Adaptive Visibility-Graph Planning for Robust Humanoid Navigation with Collision-Free MPC

> [!summary] 一句话结论（基于摘要）
> We propose RAVEN, a hierarchical reinforcement learning (RL)-MPC framework for robust humanoid navigation.

## 关键点

- **问题**：Humanoid navigation in dynamic environments requires long-horizon planning while respecting short-horizon dynamic and safety constraints.
- **创新点 / 方法**：We propose RAVEN, a hierarchical reinforcement learning (RL)-MPC framework for robust humanoid navigation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/RAVEN Reinforcement-Adaptive Visibility-Graph Planning for Robust Humanoid Navig.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid navigation in dynamic environments requires long-horizon planning while
respecting short-horizon dynamic and safety constraints. Classical visibility-graph
planners combined with model predictive control (MPC) can efficiently generate
collision-free trajectories, but their performance depends on manually tuned parameters
and accurate system modeling. In real robotic systems, control delays, state-estimation
noise, and locomotion uncertainties can cause overshoot and constraint violations even
when the nominal path is geometrically optimal. We propose RAVEN, a hierarchical
reinforcement learning (RL)-MPC framework for robust humanoid navigation. Unlike prior
approaches that use learning to tune cost weights or replace planning entirely, RAVEN
employs RL to adapt the geometric construction of a visibility-graph planner by
modifying obstacle inflation and related graph parameters. By directly reshaping the
free-space geometry, the learned planner alters the topology of the global path to
compensate for delay and tracking imperfections. A collision-free MPC layer then tracks
the planned trajectory while explicitly enforcing velocity bounds and obstacle-avoidance
constraints. By training under realistic delays and observation noise, RAVEN learns
planning adaptations that improve robustness while retaining explicit long-horizon
geometric planning and constrained optimization, in contrast to end-to-end learning
approaches. We evaluate RAVEN against a manually tuned visibility-graph MPC baseline and
a pure RL navigation policy. Results demonstrate reduced overshoot near obstacles,
improved robustness in narrow passages, and more reliable navigation under delay and
noise. These findings indicate that reinforcement-adaptive graph construction combined
with constrained MPC provides an effective and interpretable alternative to end-to-end
learning for robust humanoid navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15701v1
- Authors: Ruochen Hou, Shiqi Wang, Beom Jun Kim, Hanzhang Fang, Mehak Singal, Dennis W. Hong
- Published: 2026-07-17T07:23:54Z
- Age days: 2

</details>
