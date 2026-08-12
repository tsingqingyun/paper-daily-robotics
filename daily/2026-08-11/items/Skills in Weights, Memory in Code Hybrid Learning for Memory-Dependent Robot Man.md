---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09410v1"
published: "2026-08-10T10:35:47Z"
age_days: 0
score: 45
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> On RoboMemArena, HyMeS improves mean cumulative success from 52.5% to 66.2% and mean task success from 41.3% to 60.1% over pi0.5, while outperforming PrediMem by 4.5 points in cumulative success and 14.5 points in task success.

## 关键点

- **问题**：However, real-world manipulation is often non-Markovian, requiring robots to retain and reason over task-relevant information from long-horizon interaction histories to determine the next action.
- **创新点 / 方法**：To address this challenge, we propose HyMeS, a hybrid learning framework that leverages the reasoning and memory-management capabilities of coding agents to steer a Markovian VLA for memory-dependent manipulation.
- **证据**：On RoboMemArena, HyMeS improves mean cumulative success from 52.5% to 66.2% and mean task success from 41.3% to 60.1% over pi0.5, while outperforming PrediMem by 4.5 points in cumulative success and 14.5 points in task success.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：45
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-11/Skills in Weights, Memory in Code Hybrid Learning for Memory-Dependent Robot Man.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Modern vision-language-action (VLA) policies have acquired broad manipulation skills,
but typically generate each action chunk from the current observation or a short fixed-
length history. However, real-world manipulation is often non-Markovian, requiring
robots to retain and reason over task-relevant information from long-horizon interaction
histories to determine the next action. To address this challenge, we propose HyMeS, a
hybrid learning framework that leverages the reasoning and memory-management
capabilities of coding agents to steer a Markovian VLA for memory-dependent
manipulation. Specifically, HyMeS learns low-level motor skills through gradient-based
imitation learning, while a coding agent acquires high-level memory-management
strategies through heuristic learning by iteratively updating an executable heuristic
system from rollout feedback. Furthermore, we close the loop between steering and
execution through multimodal stage-completion verification, which updates memory using
proprioceptive signals and multi-frame VLM judgments. Compared with end-to-end memory-
augmented VLAs, HyMeS requires demonstrations only for reusable motor skills rather than
for every history-dependent task configuration, enabling data-efficient compositional
generalization. On RoboMemArena, HyMeS improves mean cumulative success from 52.5% to
66.2% and mean task success from 41.3% to 60.1% over pi0.5, while outperforming PrediMem
by 4.5 points in cumulative success and 14.5 points in task success.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09410v1
- Authors: Yunhao Zhao, Zhenyang Ni, Haoyang Chen, Ruohan Zhang, Qi Zhu
- Published: 2026-08-10T10:35:47Z
- Age days: 0

</details>
