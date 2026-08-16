---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.11204v1"
published: "2026-08-11T17:59:13Z"
age_days: 4
score: 24
created: 2026-08-16
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning

> [!summary] 一句话结论（基于摘要）
> On a suite of four simulated surgical manipulation tasks, video pretraining improves the average success rate from 63.5% to 77.8%, including an absolute gain of 20 percentage points on PegTransfer, with the largest improvements on contact-rich and bimanual ta…

## 关键点

- **问题**：Learning reliable surgical manipulation policies is bottlenecked by the scarcity of action-labeled demonstrations: teleoperated surgical robot (e.g., dVRK) trajectories with synchronized kinematics are costly to collect, while surgical tasks demand precise contact handling, long-horizon reasoning, and bimanual coordin…
- **创新点 / 方法**：To answer it, we introduce the Surgical World-Action Model (Surgical WAM), a unified generative model built on Cosmos Policy that jointly predicts future endoscopic observations and executable surgical robot action chunks.
- **证据**：On a suite of four simulated surgical manipulation tasks, video pretraining improves the average success rate from 63.5% to 77.8%, including an absolute gain of 20 percentage points on PegTransfer, with the largest improvements on contact-rich and bimanual tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Surgical WAM A World-Action Model for Data-Efficient Surgical Robot Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning reliable surgical manipulation policies is bottlenecked by the scarcity of action-labeled demonstrations: teleoperated surgical robot (e.g., dVRK) trajectories with synchronized kinematics are costly to collect, while surgical tasks demand precise contact handling, long-horizon reasoning, and bimanual coordination. Endoscopic video is comparatively inexpensive and abundant relative to synchronized video--kinematics trajectories, and a natural way to exploit it is to learn world models of surgical scenes. However, existing surgical world models use video primarily for simulation or policy evaluation, and rarely translate the learned dynamics into closed-loop control. This gap raises our central question: under a fixed budget of action-labeled demonstrations, does action-free video pretraining improve closed-loop surgical manipulation? To answer it, we introduce the Surgical World-Action Model (Surgical WAM), a unified generative model built on Cosmos Policy that jointly predicts future endoscopic observations and executable surgical robot action chunks. Surgical WAM first learns surgical visual dynamics from action-free video and is then fine-tuned on the fixed action-labeled budget; at deployment, it acts as a closed-loop, receding-horizon controller that executes a short prefix of each predicted action chunk and replans from the resulting observation. On a suite of four simulated surgical manipulation tasks, video pretraining improves the average success rate from 63.5% to 77.8%, including an absolute gain of 20 percentage points on PegTransfer, with the largest improvements on contact-rich and bimanual tasks. These results demonstrate that action-free video provides transferable visual dynamics priors for learning surgical robot control with limited action supervision, positioning data-efficient video pretraining as a practical path toward scaling up surgical robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.11204v1
- Authors: Wenrui Bao, Tianyun Jiang, Zhiben Chen, Ser-Nam Lim, Peter D. Peng, Yuzhang Shang
- Published: 2026-08-11T17:59:13Z
- Age days: 4

</details>
