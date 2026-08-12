---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14375v1"
published: "2026-06-12T12:06:41Z"
age_days: 2
score: 34
created: 2026-06-15
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models

> [!summary] 一句话结论（基于摘要）
> We propose Elastic Queries Reinforcement Learning (EQRL), a framework that makes each VLA policy query elastic.

## 关键点

- **问题**：This rigidity ignores the uneven difficulty of robot control: contact-rich or uncertain states may need more computation and fresher feedback, while easier states can often be handled with fewer inference steps and longer open-loop execution.
- **创新点 / 方法**：We propose Elastic Queries Reinforcement Learning (EQRL), a framework that makes each VLA policy query elastic.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/Elastic Queries Reinforcement Learning Self-Aware Policy Execution for VLA Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models are powerful action generators for robot
manipulation, but they are typically executed with fixed inference and replanning
schedules. This rigidity ignores the uneven difficulty of robot control: contact-rich or
uncertain states may need more computation and fresher feedback, while easier states can
often be handled with fewer inference steps and longer open-loop execution. We propose
Elastic Queries Reinforcement Learning (EQRL), a framework that makes each VLA policy
query elastic. A lightweight latent-schedule adaptor jointly selects the latent input,
denoising budget, and action chunk length, without fine-tuning the underlying VLA model.
To make scheduling difficulty-aware, EQRL trains a critic over the joint latent-schedule
action and derives a state difficulty signal from critic ensemble disagreement. This
signal guides compute toward difficult states, while a learned residual allows task-
driven correction. We formulate variable chunk execution as query-level macro-action RL
with chunk-dependent discounting and an amortized number-of-function-evaluations (NFE)
budget. Across simulation and real-robot manipulation, EQRL reduces amortized inference
cost while preserving or improving task success.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14375v1
- Authors: Ge Wang, Xinyu Tan, Xiang Li, Man Luo, Chengsi Yao, Shenhao Yan, Jiahao Yang, Fan Feng, Honghao Cai, Xiangyuan Wang, Zhixin Mai, Yiming Zhao, Yatong Han, Zhen Li
- Published: 2026-06-12T12:06:41Z
- Age days: 2

</details>
