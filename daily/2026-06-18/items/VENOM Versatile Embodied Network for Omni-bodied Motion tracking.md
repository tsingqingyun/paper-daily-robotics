---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.16696v1"
published: "2026-06-15T13:31:37Z"
age_days: 2
score: 35
created: 2026-06-18
concepts: ["多模态基础模型", "世界模型", "机器人学习"]
---

# VENOM: Versatile Embodied Network for Omni-bodied Motion tracking

> [!summary] 一句话结论（基于摘要）
> This work proposes VENOM, a cross-embodiment full-body motion tracking model for humanoids in simulation.

## 关键点

- **问题**：Achieving expert-level expressive full-body motion tracking across multiple humanoids solely from demonstration data remains a challenging and relatively an underexplored problem in humanoid robot learning.
- **创新点 / 方法**：This work proposes VENOM, a cross-embodiment full-body motion tracking model for humanoids in simulation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[机器人学习]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-18/VENOM Versatile Embodied Network for Omni-bodied Motion tracking.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Achieving expert-level expressive full-body motion tracking across multiple humanoids
solely from demonstration data remains a challenging and relatively an underexplored
problem in humanoid robot learning. Cross-embodiment motion tracking policies are mostly
trained by decoupling the control problem into upper and lower body control. This work
proposes VENOM, a cross-embodiment full-body motion tracking model for humanoids in
simulation. VENOM is a GPT-based motion tracker trained on multiple humanoid data that
can track the entire body without the requirement to split into upper and lower body
control. We curate a multi-humanoid motion tracking dataset called the VENOM dataset
that contains states, actions, and rewards and train VENOM and the baselines on this
dataset. In this letter, we evaluate VENOM's performance against baselines and show that
we can achieve a stable motion tracker across different humanoids more capable than an
MLP trained on multiple humanoid data with supervised learning alone, and also show that
despite lack of reward feedback, VENOM closely matches the tracking capability of
experts that were trained using asymmetric-actor critic reinforcement learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.16696v1
- Authors: Siddharth Padmanabhan, Kazuki Miyazawa, Takato Horii
- Published: 2026-06-15T13:31:37Z
- Age days: 2

</details>
