---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.01596v1"
published: "2026-09-01T17:58:07Z"
age_days: 1
score: 33
created: 2026-09-03
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

> [!summary] 先说人话（基于摘要）
> Facet-0 面向亚毫米装配，不只预测动作，还预测动作将引发的腕部力／力矩，并用 Action-Wrench Critic 区分进度相似但接触后果不同的动作。它再通过受限轻量 actor 做在机适配。

## 这篇到底在做什么

- **卡在哪里**：精密装配同时要求空间精度、柔顺接触和接触失败恢复；仅看视觉或任务进度的策略难以辨别看似相近、实际受力后果不同的动作，通用策略也难覆盖零件特定动力学。
- **关键解法**：模型对齐因果 wrench 历史、视觉语言语义和运动状态，用 flow matching 联合生成动作块及预期未来腕部 wrench；部署轨迹训练分布式 critic，阶段奖励和接触选择性信用分配聚焦关键接触，冻结表征上的受限 actor 负责适配。
- **拿什么证明**：在跨3种本体和多个制造单元的 ManuFacet-1K 1000小时力同步数据上训练；5项亚毫米计算机装配任务平均成功率82%，最强基线15%，定位精度0.5毫米，指令延迟50毫秒。

## 值不值得读

- **和你的研究有什么关系**：它把接触后果建模纳入基础策略与 RL 后训练，对机器人学习和世界模型研究者提供了比纯 RGB 动力学更贴近精密装配的预测对象。
- **先别急着信**：82%来自“受限且任务适配”的系统，不能据此判断基础模型本身的零样本能力；五项同类装配任务之外的泛化需核查。
- **判断**：今天最值得精读的方法之一，尤其应看 critic 训练、接触信用分配和基线公平性；其绝对提升很大，但归因必须谨慎。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Facet-0 A Robotic Foundation Model for Contact-Rich Precise Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world robotic assembly at sub-millimeter tolerances demands spatial precision, compliant interaction, and robustness to contact failures. We present Facet-0, a robotic foundation model that predicts and values the contact consequences of its actions. Facet-0 unifies multimodal representation learning and reinforcement learning (RL) post-training around a joint action-wrench proposal: a causal wrench history is aligned with vision-language semantics and kinematic state, and flow matching generates each action chunk together with the future wrist-wrench profile it is expected to induce. Deployment rollouts train a distributional Action-Wrench Critic to distinguish motions with similar task progress but different contact outcomes, while phase-aware rewards and contact-selective credit concentrate policy improvement on decisive interactions. To accommodate part-specific dynamics, a lightweight bounded actor reuses the frozen representation for on-robot adaptation; RL remains defined over executable Cartesian actions, while an auxiliary wrench head preserves predictive, non-commanded action-contact coupling. Trained on ManuFacet-1K, a 1,000-hour force-synchronized corpus spanning three embodiments and multiple manufacturing cells, the bounded task-adapted system reaches 82% mean success on five sub-millimeter computer-assembly tasks, compared with 15% for the strongest baseline, with 0.5 mm placement accuracy and 50 ms command latency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.01596v1
- Authors: Haoyuan Deng, Haichao Liu, Wenkai Guo, Yuan Ling, Zaijia Yang, Yuanjiang Xue, Haosheng Sun, Liangzi Wang, Ziwei Wang
- Published: 2026-09-01T17:58:07Z
- Age days: 1

</details>
