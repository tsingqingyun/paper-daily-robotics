---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25414v1"
published: "2026-05-25T04:30:51Z"
age_days: 1
score: 28
created: 2026-05-26
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# How to Mitigate the Distribution Shift Problem in Robotics Control: A Robust and Adaptive Approach Based on Offline to Online Imitation Learning

> [!summary] 一句话结论（基于摘要）
> Through extensive evaluations in MuJoCo environments, we demonstrate that our method exhibits better robustness to distribution shift and better adaptation performance to online environments than the baseline algorithms, which indicates superior performance o…

## 关键点

- **问题**：Distribution shift in imitation learning refers to the problem that the agent cannot plan proper actions for a state that has not been visited during the training.
- **创新点 / 方法**：In this paper, we propose a robust offline to adaptive online imitation learning framework that handles the distribution shift problem in a lifelong, multi-phase scheme.
- **证据**：Through extensive evaluations in MuJoCo environments, we demonstrate that our method exhibits better robustness to distribution shift and better adaptation performance to online environments than the baseline algorithms, which indicates superior performance of our framework against the distribution shift.
- **局限**：Distribution shift in imitation learning refers to the problem that the agent cannot plan proper actions for a state that has not been visited during the training.

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/How to Mitigate the Distribution Shift Problem in Robotics Control A Robust and.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Distribution shift in imitation learning refers to the problem that the agent cannot
plan proper actions for a state that has not been visited during the training. This
problem can be largely attributed to the inherently narrow state-action coverage
provided by expert demonstrations over the full environment. In this paper, we propose a
robust offline to adaptive online imitation learning framework that handles the
distribution shift problem in a lifelong, multi-phase scheme. In the offline learning
phase, we leverage supplementary demonstrations to broaden the state-action coverage of
the policy by utilizing a discriminator to effectively train the policy with
supplementary demonstrations, thereby enhancing the robustness of the policy to
distribution shift. In the subsequent online inference phase, our framework detects the
occurrence of distribution shift and conducts self-supervised imitation learning from
online experiences to adapt the policy to the online environments. Through extensive
evaluations in MuJoCo environments, we demonstrate that our method exhibits better
robustness to distribution shift and better adaptation performance to online
environments than the baseline algorithms, which indicates superior performance of our
framework against the distribution shift.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25414v1
- Authors: Hyung-Suk Yoon, Seung-Woo Seo
- Published: 2026-05-25T04:30:51Z
- Age days: 1

</details>
