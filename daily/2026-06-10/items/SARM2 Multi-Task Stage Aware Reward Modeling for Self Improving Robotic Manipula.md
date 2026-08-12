---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10305v1"
published: "2026-06-09T01:46:23Z"
age_days: 0
score: 37
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> On a 10-task benchmark, RM reduces value-estimation MSE by 80% over the strongest baselines; when used in SPIRAL, it improves task success from around 50% to near-perfect performance on Folding Shorts (58% to 100%) and Cleaning Whiteboard (50% to 90%), showin…

## 关键点

- **问题**：Fine-tuning vision-language-action (VLA) policies for long-horizon manipulation still relies heavily on behavior cloning, which requires costly high-quality demonstrations and keeps policies near the demonstration distribution.
- **创新点 / 方法**：We introduce RM, a multi-task stage-aware reward model that combines an action-primitive-based stage estimator with a multi-gate Mixture-of-Experts (MMoE) value head to produce dense per- step rewards across manipulation tasks.
- **证据**：On a 10-task benchmark, RM reduces value-estimation MSE by 80% over the strongest baselines; when used in SPIRAL, it improves task success from around 50% to near-perfect performance on Folding Shorts (58% to 100%) and Cleaning Whiteboard (50% to 90%), showing that high-quality dense rewards are key to a stable robot…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Fine-tuning vision-language-action (VLA) policies for long-horizon manipulation still
relies heavily on behavior cloning, which requires costly high-quality demonstrations
and keeps policies near the demonstration distribution. Reward models can reduce this
dependence by reweighting demonstrations and providing dense supervision for on-robot
reinforcement learning (RL), but they must be dense, accurate, and general. Existing
methods fall short: task-specific stage-aware models are accurate but require per-task
annotations, while general vision-language-model (VLM) reward models are broadly
applicable but too coarse for fine-grained long-horizon progress. We introduce RM, a
multi-task stage-aware reward model that combines an action-primitive-based stage
estimator with a multi-gate Mixture-of-Experts (MMoE) value head to produce dense per-
step rewards across manipulation tasks. Building on RM, we further propose SPIRAL (Self-
Policy Improvement via Reward-Aligned Learning), an on-policy reward-guided framework
that improves VLA policies from cheap autonomous rollouts. On a 10-task benchmark, RM
reduces value-estimation MSE by 80% over the strongest baselines; when used in SPIRAL,
it improves task success from around 50% to near-perfect performance on Folding Shorts
(58% to 100%) and Cleaning Whiteboard (50% to 90%), showing that high-quality dense
rewards are key to a stable robot data flywheel. Project website: https://qianzhong-
chen.github.io/sarm2.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10305v1
- Authors: Qianzhong Chen, Hau Zheng, Justin Yu, Suning Huang, Jiankai Sun, Ken Goldberg, Chuan Wen, Pieter Abbeel, Yide Shentu, Philipp Wu, Mac Schwager
- Published: 2026-06-09T01:46:23Z
- Age days: 0

</details>
