---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23085v1"
published: "2026-06-22T09:32:28Z"
age_days: 1
score: 39
created: 2026-06-24
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents

> [!summary] 一句话结论（基于摘要）
> We present Foresight, a failure detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model.

## 关键点

- **问题**：Long-horizon tasks are common in real-world robotic deployments, yet failure detection for such tasks remains underexplored.
- **创新点 / 方法**：We present Foresight, a failure detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/Foresight Failure Detection for Long-Horizon Robotic Manipulation with Action-Co.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon tasks are common in real-world robotic deployments, yet failure detection
for such tasks remains underexplored. Detecting failures in long-horizon robotic tasks
is particularly challenging because failure onset is often ambiguous and dense temporal
annotations are typically unavailable. We present Foresight, a failure detection
framework that monitors manipulation trajectories using latent representations from an
action-conditioned world model. Foresight is trained using only final task-level success
or failure labels. By leveraging predictive world-model embeddings, our method provides
a unified framework for failure detection across different policies. We further use
functional conformal prediction (FCP) to calibrate detection thresholds adaptively. We
evaluate Foresight with state-of-the-art vision-language-action policies in simulation
on LIBERO-Long, ManiSkill-Long, and BEHAVIOR-1K, compare it against state-of-the-
artfailure detection methods, and validate it on real robots with three long-horizon
tasks on a ReactorX-200 arm and one task on a Franka arm. Our results suggest that
action-conditioned world-model embeddings provide a scalable representation for reliable
failure monitoring in long-horizon manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23085v1
- Authors: Haoran Zhang, Yifu Lu, Boyang Wang, Xuhui Kang, Yen-Ling Kuo, Zezhou Cheng, Mengdi Wang, Odest Chadwicke Jenkins
- Published: 2026-06-22T09:32:28Z
- Age days: 1

</details>
