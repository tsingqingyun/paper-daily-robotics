---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14047v2"
published: "2026-07-15T17:16:24Z"
age_days: 2
score: 28
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment

> [!summary] 一句话结论（基于摘要）
> We present Zero2Skill, a human-robot symbiotic agentic system in which corrections are retained and reused across rounds.

## 关键点

- **问题**：Existing pipelines reduce human effort via self-resetting, VLM verification, or language-guided correction, yet episode-scoped fixes must be reissued whenever the same failure recurs, so oversight cost grows with session length rather than with the number of distinct problems.
- **创新点 / 方法**：We present Zero2Skill, a human-robot symbiotic agentic system in which corrections are retained and reused across rounds.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/Zero2Skill Bootstrapping Robot Skills through Autonomous Data Collection, Traini.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous data collection governs the volume and quality of real-world trajectories for
manipulation policy learning. Existing pipelines reduce human effort via self-resetting,
VLM verification, or language-guided correction, yet episode-scoped fixes must be
reissued whenever the same failure recurs, so oversight cost grows with session length
rather than with the number of distinct problems. We present Zero2Skill, a human-robot
symbiotic agentic system in which corrections are retained and reused across rounds. The
collection loop collects, verifies, and resets autonomously, pausing for a remote
operator only when a phase exhausts an explicit retry budget. An LLM parser maps each
natural-language utterance to a structured adjustment stored in Corrective Memory, so
addressed failure modes typically need not be corrected again under the same conditions.
On a real-robot desktop-clearing testbed, Zero2Skill matches teleoperation episode
success while reducing human working time to 16%. Language corrections improve verifier-
human agreement in all four evaluated settings and raise average single-attempt success
from 12.5% to 47.5% (arm-selection: 20.0% to 50.0%). Policies fine-tuned on Zero2Skill
data match teleoperation-trained policy success at a fraction of collection human cost.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14047v2
- Authors: Boyuan Wang, Zhenyuan Zhang, Zhiqin Yang, Peijun Gu, Shuya Wang, Xiaofeng Wang, Xianghui Ze, Yifan Chang, Guosheng Zhao, Jiangnan Shao, Guan Huang, Hengyu Liu, Yonggang Zhang, Wei Xue, Chunyuan Guan, Chenglin Pu, Yike Guo, Xingang Wang, Zheng Zhu
- Published: 2026-07-15T17:16:24Z
- Age days: 2

</details>
