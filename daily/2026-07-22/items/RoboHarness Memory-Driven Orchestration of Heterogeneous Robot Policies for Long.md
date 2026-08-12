---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18060v1"
published: "2026-07-20T15:27:13Z"
age_days: 1
score: 29
created: 2026-07-22
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning

> [!summary] 一句话结论（基于摘要）
> We propose RoboHarness, a unified framework that encapsulates independently developed robot control systems as reusable agentic skills.

## 关键点

- **问题**：Long-horizon robotic tasks require diverse capabilities that no single policy can reliably provide.
- **创新点 / 方法**：We propose RoboHarness, a unified framework that encapsulates independently developed robot control systems as reusable agentic skills.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-22/RoboHarness Memory-Driven Orchestration of Heterogeneous Robot Policies for Long.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon robotic tasks require diverse capabilities that no single policy can
reliably provide. Heterogeneous policies offer complementary strengths, but
orchestrating them requires reasoning over uncertain capability boundaries and cross-
policy distribution mismatch, which are largely overlooked by existing planning methods
built on homogeneous, predefined skills with fixed applicability. We propose
RoboHarness, a unified framework that encapsulates independently developed robot control
systems as reusable agentic skills. Although instantiated in this work with VLAs, RL
policies, and task-and-motion planning (TAMP) systems, RoboHarness is designed as a
general framework compatible with a broader range of robot policies, such as navigation
policies, model predictive controllers, and world-action models. RoboHarness uses multi-
modal execution memory and online evidence to characterize policy capability boundaries
for capability-aware decomposition and routing. To stabilize policy handoffs, its Memory
Bridge retrieves execution trajectories associated with the next policy, estimates its
in-distribution state region, and guides the robot toward that region without joint
policy retraining. Extensive experiments on three public benchmarks, 500 customized
tasks, and 135 real-robot experiments demonstrate effective capability-aware routing and
stable policy orchestration, yielding substantial improvements in zero-shot long-horizon
planning and out-of-distribution robustness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18060v1
- Authors: Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao, Zhanguang Zhang, Mark Coates, Tongtong Cao, Yingxue Zhang
- Published: 2026-07-20T15:27:13Z
- Age days: 1

</details>
