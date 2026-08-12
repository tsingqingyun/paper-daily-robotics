---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13653v1"
published: "2026-07-15T09:55:45Z"
age_days: 1
score: 45
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation

> [!summary] 一句话结论（基于摘要）
> Experimental results demonstrate that our trained agent outperforms leading commercial closed-source VLMs on interactive tasks with a 56.9% success rate.

## 关键点

- **问题**：However, existing frameworks often rely on privileged simulator states or assume complete instructions, bypassing realistic deployment challenges.
- **创新点 / 方法**：To bridge this gap, we present REAL, an agentic framework for open-world mobile manipulation.
- **证据**：Experimental results demonstrate that our trained agent outperforms leading commercial closed-source VLMs on interactive tasks with a 56.9% success rate.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：45
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world deployment of embodied agents requires active exploration, visual grounding,
and interactive intent disambiguation. However, existing frameworks often rely on
privileged simulator states or assume complete instructions, bypassing realistic
deployment challenges. To bridge this gap, we present REAL, an agentic framework for
open-world mobile manipulation. REAL establishes sim-to-real-consistent environment APIs
without oracle perception and integrates a simulated user to enable human-in-the-loop
interaction. Within this environment, we design diverse task compositions to drive data
collection, supervised fine-tuning, and online reinforcement learning, systematically
optimizing agent performance. To comprehensively evaluate this approach, we introduce
REAL-Bench, a benchmark spanning 241 tasks across active exploration, visual
distraction, articulated manipulation, and interactive disambiguation. Experimental
results demonstrate that our trained agent outperforms leading commercial closed-source
VLMs on interactive tasks with a 56.9% success rate. Further empirical analysis reveals
that our hierarchical training pipeline successfully aligns the model's tool-use
capabilities while maintaining robust open-vocabulary reasoning under extended
exploration horizons. Finally, we deploy and evaluate our framework on a physical dual-
arm mobile robot, where it achieves a 78.3% end-to-end success rate over 60 real-world
episodes. These physical trials demonstrate robust zero-shot transferability to unseen
household scenarios, validating that our sim-to-real-consistent design successfully
bridges the reality gap for long-horizon mobile manipulation. Code is available at
https://github.com/InternRobotics/REAL.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13653v1
- Authors: Boyu Mi, Mengchen Ma, Yifei Yao, Xing Gao, Junting Chen, Yangzi Li, Zihou Zhu, Guohao Li, Zhenfei Yin, Tai Wang, Yao Mu, Jiangmiao Pang, Hanqing Wang
- Published: 2026-07-15T09:55:45Z
- Age days: 1

</details>
