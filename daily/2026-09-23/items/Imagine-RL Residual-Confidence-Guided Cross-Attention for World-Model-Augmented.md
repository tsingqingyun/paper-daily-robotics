---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24033v1"
published: "2026-09-21T02:59:08Z"
age_days: 1
score: 38
created: 2026-09-23
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning

> [!summary] 先说人话（基于摘要）
> Imagine-RL在强化学习评价动作时，先预测它可能带来的视觉和接触后果。它还根据过去的预测误差降低不可靠未来信息的权重，避免评价器盲信世界模型。

## 问题

接触操作的动作质量取决于后续视觉和力矩变化，但已有噪声空间RL的评价器大多未利用这些后果。

## 创新点或方法

冻结视觉—力矩潜在世界模型，为候选动作块自回归预测未来特征；当前图像、状态和动作形成查询，通过交叉注意力读取历史与未来，上一窗口预测残差提供逐token置信先验。评价器指导actor，VLA和世界模型保持冻结。

## 证据

4项真实机器人任务，每项评测50次，使用100条RL轨迹；平均成功率相对DSRL和VLA基线的提升分别写为23.6%和60%。

## 局限

摘要没有明确提升数字是相对比例还是百分点，也未说明100条轨迹的任务分配；过去残差能否反映当前未来预测的可靠性需核查。

- **判断**：值得精读评价器与置信机制，先确认指标口径再判断样本效率优势。

## 研究关联

为世界模型辅助VLA后训练提供了明确用途：改善动作评价，并把预测可靠性纳入决策。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Imagine-RL Residual-Confidence-Guided Cross-Attention for World-Model-Augmented.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences. Existing noise-space reinforcement learning efficiently steers a frozen Vision-Language-Action (VLA) policy, but its critics largely ignore these consequences. We present Imagine-RL, which augments noise-space VLA post-training with action-conditioned visual-torque imagination. For each candidate action chunk, a frozen visual-torque latent world model (VTLWM) autoregressively predicts compact future representations without pixel reconstruction. A current image-state-action query attends to observed histories and predicted futures, while previous-window prediction residuals provide token-wise confidence priors that suppress unreliable future tokens. By combining current evidence with predicted consequences, the action critic better evaluates candidate actions and supervises the actor, while the VLA and VTLWM remain frozen. Across four real-robot tasks with 50 evaluation trials per task, Imagine-RL uses only 100 RL trajectories and improves the average success rate by (23.6%) over DSRL and by (60%) over VLA baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24033v1
- Authors: Kejia Hu, Wentong Zhai, Bo Zhao, Shuai Liang
- Published: 2026-09-21T02:59:08Z
- Age days: 1

</details>
