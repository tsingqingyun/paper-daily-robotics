---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13395v1"
published: "2026-08-13T15:53:24Z"
age_days: 2
score: 26
created: 2026-08-16
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving

> [!summary] 一句话结论（基于摘要）
> Reinforcement learning improves autonomous-driving vision-language-action (VLA) models by evaluating trajectories sampled from the current policy.

## 关键点

- **问题**：When all sampled trajectories are poor, this relative signal can rank failures without identifying behavior outside the failed region.
- **创新点 / 方法**：We introduce FIRE-VLA, a failure-informed self-evolution framework that converts such unresolved failures into privileged supervision for the next policy.
- **证据**：Reinforcement learning improves autonomous-driving vision-language-action (VLA) models by evaluating trajectories sampled from the current policy.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/FIRE-VLA Failure-Informed Self-Evolution for Vision-Language-Action Models in Au.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning improves autonomous-driving vision-language-action (VLA) models by evaluating trajectories sampled from the current policy. Group relative policy optimization (GRPO) learns from reward differences within each rollout group. When all sampled trajectories are poor, this relative signal can rank failures without identifying behavior outside the failed region. We introduce FIRE-VLA, a failure-informed self-evolution framework that converts such unresolved failures into privileged supervision for the next policy. Low-reward, low-diversity groups trigger self-distillation from a frozen round-start copy of the same model. Teacher and student have the same parameter scale, but only the teacher observes the hidden future trajectory. Supervision follows the student's generated prefix and is restricted to answer tokens, while GRPO remains active for every group. The updated policy supplies the teacher for the next round, allowing the routed failure distribution to change with the policy without requiring a larger external teacher. Starting from the same Qwen2.5-VL-3B SFT checkpoint, the comparison matches student rollout and policy-update counts. On 6,019 examples from 150 held-out nuScenes scenes, FIRE-VLA retains comparable single-sample planning, reduces G=4 mean L2 from 1.848 to 1.500 m, and lowers evaluation-persistent failure prevalence from 13.03% to 11.20%. The reduction in mean error arises mainly from rare severe rollouts rather than uniform improvement across ordinary trajectories.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13395v1
- Authors: Hao Dou
- Published: 2026-08-13T15:53:24Z
- Age days: 2

</details>
