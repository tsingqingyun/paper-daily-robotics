---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.22894"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 30
created: 2026-09-08
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-Based Humanoid Control

> [!summary] 先说人话（基于摘要）
> SCRIPT 让物理仿真人形角色按语言要求运动，同时兼顾动作质量和长期稳定性。它联合建模动作、状态与文本，再用物理和文本奖励后训练。

## 问题

现有语言控制方法难以同时满足语义表达、物理可行性和长时程稳定控制。

## 创新点或方法

JAST-DiT 将动作、物理状态和文本作为独立 token 流进行联合注意力建模；历史条件保留密集近期信息和稀疏远期信息，RLHR 通过流采样中的可学习噪声及混合奖励优化策略。

## 证据

报告文本对齐、运动质量和物理真实性优于既有方法；在 1,200 小时 MotionMillion 上观察到模型扩大带来的持续增益，摘要未给出性能提升数字。


## 局限

评测描述集中在物理仿真，不能据此推断真机可用性；需核查长期稳定性与奖励设计。

- **判断**：做人形仿真控制值得精读架构与后训练，真机研究者宜将其视为待验证的方法来源。

## 研究关联

对语言驱动机器人学习和长时程控制有方法参考；动作与状态联合建模也值得世界模型研究者关注，但摘要未证明独立的环境预测能力。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/SCRIPT Scalable Diffusion Policy with Multi-stage Training for Language-driven P.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.22894v3 Announce Type: replace-cross Abstract: Controlling physics-based humanoids from natural-language instructions is a critical step toward general-purpose embodied agents. However, existing methods remain constrained by a tension between semantic expressiveness and physical feasibility, often failing to jointly achieve faithful instruction following, high-quality motion, and stable long-horizon control. We propose SCRIPT, a scalable diffusion policy with a multi-stage training framework for language-driven physics-based humanoid control. The core of SCRIPT is a Joint Action-State-Text Diffusion Transformer (JAST-DiT), which represents actions, physical states, and text as dedicated token streams and couples them through joint attention, enabling direct interaction between language semantics and control dynamics. To stabilize autoregressive control, we introduce a nonlinear history conditioning mechanism, which preserves the dense recent context and samples increasingly sparse cues from long-term history. Beyond supervised imitation pre-training, we propose a post-training stage, further improving the performance using Reinforcement Learning with Hybrid Rewards (RLHR). By injecting learnable noise into the flow-sampling process, RLHR effectively improves motion quality and instruction following within closed-loop simulations using hybrid physical feedback and text rewards. Quantitative evaluations demonstrate that SCRIPT outperforms prior state-of-the-art methods, with gains across text alignment, motion quality, and physical realism metrics. Furthermore, scaling studies on the 1200-hour MotionMillion dataset demonstrate consistent performance gains with model scaling, highlighting SCRIPT's robust scalability for large-scale pre-training. Our code will be publicly available for future research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.22894
- Authors: Jingyan Zhang, Han Liang, Ruichi Zhang, Bin Li, Juze Zhang, Xin Chen, Jingya Wang, Lan Xu, Jingyi Yu
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
