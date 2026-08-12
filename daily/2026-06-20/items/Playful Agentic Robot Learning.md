---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19419v1"
published: "2026-06-17T17:55:23Z"
age_days: 2
score: 33
created: 2026-06-20
concepts: ["智能体 Agent", "机器人学习"]
---

# Playful Agentic Robot Learning

> [!summary] 一句话结论（基于摘要）
> We introduce RATs, Robotics Agent Teams designed for play-time skill acquisition.

## 关键点

- **问题**：Current agentic robot systems can write executable Code-as-Policy programs, observe feedback, and revise behavior across multiple attempts, but they remain largely task- driven: reusable skills are acquired only after explicit instructions.
- **创新点 / 方法**：We introduce RATs, Robotics Agent Teams designed for play-time skill acquisition.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/Playful Agentic Robot Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Current agentic robot systems can write executable Code-as-Policy programs, observe
feedback, and revise behavior across multiple attempts, but they remain largely task-
driven: reusable skills are acquired only after explicit instructions. We study Playful
Agentic Robot Learning, where an embodied coding agent uses self-directed play as a
continual skill-learning stage before downstream tasks arrive. We introduce RATs,
Robotics Agent Teams designed for play-time skill acquisition. During play, RATs
proposes novel yet learnable exploratory tasks, plans and executes robot-code policies,
verifies intermediate progress, diagnoses failures, retries with dense, step-level
feedback, and distills successful executions into a persistent code skill library. At
test time, the agent reuses relevant skills from this frozen library to help solve new
tasks. Experiments in LIBERO-PRO and MolmoSpaces show that play-learned skills improve
held-out downstream tasks over no-play and random-play baselines, with 20.6 and 17.0
percentage-point gains over CaP-Agent0 on LIBERO-PRO and MolmoSpaces, respectively.
Moreover, the learned skills can be plugged into other inference-time Code-as-Policy
agents by simply retrieving them into the context, improving RoboSuite and real-world
transfer by 8.9 and 8.8 points, respectively, without finetuning the underlying model.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19419v1
- Authors: Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, Raj Saravanan, Shaofeng Yin, Justin Yu, Dantong Niu, Zirui Wang, Roei Herzig, Ken Goldberg, Yutong Bai, David M. Chan, Ion Stoica, Angjoo Kanazawa, Jiahui Lei, Haiwen Feng, Trevor Darrell
- Published: 2026-06-17T17:55:23Z
- Age days: 2

</details>
