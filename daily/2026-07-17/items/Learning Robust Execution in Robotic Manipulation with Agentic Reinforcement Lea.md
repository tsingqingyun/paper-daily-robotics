---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13818v1"
published: "2026-07-15T13:25:52Z"
age_days: 1
score: 40
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> We evaluate the proposed method on the LIBERO benchmark, achieving up to a 13.7% improvement in success rate under standard settings and up to a 39.2% improvement under disturbance settings, demonstrating substantially enhanced execution robustness.

## 关键点

- **问题**：Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors, which can easily destabilize execution and lead to task failure.
- **创新点 / 方法**：In this paper, we propose: (1) two complementary metrics to assess execution quality at runtime, and (2) an agentic reinforcement learning framework that learns to restore effective execution through high-level decision-making rather than directly learning low-level actions.
- **证据**：We evaluate the proposed method on the LIBERO benchmark, achieving up to a 13.7% improvement in success rate under standard settings and up to a 39.2% improvement under disturbance settings, demonstrating substantially enhanced execution robustness.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Lea.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon
execution, and compounding errors, which can easily destabilize execution and lead to
task failure. Although recent vision-language-action (VLA) models exhibit strong
generalization, they typically lack explicit mechanisms to assess execution stability
and to recover when execution deviates from its nominal behavior. In this paper, we
propose: (1) two complementary metrics to assess execution quality at runtime, and (2)
an agentic reinforcement learning framework that learns to restore effective execution
through high-level decision-making rather than directly learning low-level actions. In
this framework, an agentic policy reasons over recent execution history and selects
among a small set of execution modes to regulate the execution process. Under execution
degradation, it triggers appropriate recovery mechanisms to restore the robot to
previously visited nominal states, enabling the task to continue. We evaluate the
proposed method on the LIBERO benchmark, achieving up to a 13.7% improvement in success
rate under standard settings and up to a 39.2% improvement under disturbance settings,
demonstrating substantially enhanced execution robustness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13818v1
- Authors: Xiaopeng Zhang, Yueyang Weng, Qi Liu, Yongjin Mu, Yanjie Li
- Published: 2026-07-15T13:25:52Z
- Age days: 1

</details>
