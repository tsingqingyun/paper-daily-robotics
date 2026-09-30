---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10506v1"
published: "2026-09-09T17:41:38Z"
age_days: 1
score: 32
created: 2026-09-11
concepts: ["智能体 Agent", "世界模型"]
---

# DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation

> [!summary] 先说人话（基于摘要）
> Across spatially diverse reach, orientation-intensive angled-reach, and multi-goal grasp-and-lift tasks, DUET-DINO consistently outperforms single-view and independent dual-view baselines, achieving 92% success on reach, 72.5% on angled-reach, and 60.0% on li…

## 问题

However, their predictions for fine-grained spatial and rotational actions are unreliable for full 7-DoF end-effector control.

## 创新点或方法

To address this gap, we introduce DUET-DINO, a simultaneous cross-view latent world model that jointly learns action-conditioned predictions from static side- and wrist-camera observations through cross-view conditioning.

## 证据

Across spatially diverse reach, orientation-intensive angled-reach, and multi-goal grasp-and-lift tasks, DUET-DINO consistently outperforms single-view and independent dual-view baselines, achieving 92% success on reach, 72.5% on angled-reach, and 60.0% on lift tasks.


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/DUET-DINO Simultaneous Cross-View World Modeling for Latent Planning in Robot Ma.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action-conditioned latent world models predict future visual representations, enabling zero-shot goal-conditioned robot planning and control. However, their predictions for fine-grained spatial and rotational actions are unreliable for full 7-DoF end-effector control. To address this gap, we introduce DUET-DINO, a simultaneous cross-view latent world model that jointly learns action-conditioned predictions from static side- and wrist-camera observations through cross-view conditioning. By exploiting complementary global scene and gripper-centric information, DUET-DINO enables latent planning over the full 7-DoF action space. Across spatially diverse reach, orientation-intensive angled-reach, and multi-goal grasp-and-lift tasks, DUET-DINO consistently outperforms single-view and independent dual-view baselines, achieving 92% success on reach, 72.5% on angled-reach, and 60.0% on lift tasks. DUET-DINO is trained from scratch on DROID and RoboArena datasets and generalizes robustly under visual distribution shifts. We further show that while V-JEPA 2 wrist-view predictions underestimate visual dynamics induced by fine-grained actions, DINOv3 predictions better capture action-conditioned scene changes, leading to stronger downstream planning. The code and model checkpoints will be open-sourced. Project page: https://utn-air.github.io/DUET-DINO

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10506v1
- Authors: Nisarga Nilavadi, Ralf Römer, Moritz Reuss, Michael Krawez, Tobias Jülg, Angela P. Schoellig, Rudolf Lioutikov, Wolfram Burgard
- Published: 2026-09-09T17:41:38Z
- Age days: 1

</details>
