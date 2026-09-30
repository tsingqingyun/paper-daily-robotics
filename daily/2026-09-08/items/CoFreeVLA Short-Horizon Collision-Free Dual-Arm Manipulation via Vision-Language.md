---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2601.21712"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-09-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CoFreeVLA: Short-Horizon Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation

> [!summary] 先说人话（基于摘要）
> CoFreeVLA 为双臂 VLA 增加短期碰撞风险检查，在危险动作执行前拦截，并生成回到安全状态的动作。

## 这篇到底在做什么

- **卡在哪里**：端到端 VLA 对双臂及所持物体之间的自碰撞建模不足，限制协调操作的安全性与成功率。
- **关键解法**：风险估计器接收本体状态、视觉嵌入和候选动作序列，预测碰撞概率，用于动作门控、风险引导恢复和策略改进；先用模型生成的碰撞标签预训练，再用真机轨迹后训练。
- **拿什么证明**：覆盖五项双臂任务、六个 VLA 骨干，每个变体测试 30 次；任务平均碰撞率从 0.54 降至 0.23，成功率从 0.45 升至 0.61。

## 值不值得读

- **和你的研究有什么关系**：提供可附加到 VLA 的短时域风险预测思路，对双臂控制和动作候选评估有直接价值。
- **先别急着信**：干预后仍有 0.23 的平均碰撞率，不能把方法名理解为无碰撞保证；其范围也主要是短期自碰撞。
- **判断**：值得精读风险校准和恢复机制；结果显示实质改善，也清楚留下了较大的残余风险。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/CoFreeVLA Short-Horizon Collision-Free Dual-Arm Manipulation via Vision-Language.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2601.21712v3 Announce Type: replace Abstract: Vision Language Action (VLA) models enable instruction-following manipulation, yet their deployment on coordinated dual-arm platforms remains severely constrained by under-modeled self-collisions between manipulators and grasped objects. To address this critical safety gap, we propose CoFreeVLA, a novel framework that augments end-to-end VLA policies with a lightweight, short-horizon self-collision risk estimator. The estimator predicts collision likelihoods directly from proprioceptive states, visual embeddings, and candidate action sequences. Deeply integrated into the closed-loop control system, this estimator proactively gates risky commands, autonomously synthesizes recovery trajectories to safe states via risk-guided adjustments, and biases policy refinement for safer rollouts. To ensure robust calibration, the estimator utilizes a two-stage training pipeline, pre-training with model-based synthetic collision labels, followed by post-training on real-robot rollouts. Across five bimanual tasks, six VLA backbones, and 30 trials per variant, the task-averaged collision rate decreases from 0.54 to 0.23, while the task-averaged success rate increases from 0.45 to 0.61. Compared to representative baselines, CoFreeVLA substantially reduces self-collision frequencies and improves overall task success rates, providing a crucial step toward the safe deployment of foundational models in multi-arm continuous control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2601.21712
- Authors: Yaohua Liu, Binkai Ou, Hengjun Zhang
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
