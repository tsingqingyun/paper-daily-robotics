---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02885v1"
published: "2026-09-02T17:59:40Z"
age_days: 0
score: 27
created: 2026-09-03
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Discriminative World Models for Web Agents

> [!summary] 先说人话（基于摘要）
> 论文认为 Web Agent 的世界模型不应只逼真预测下一状态，还应让不同候选动作的后果彼此可区分。Predicted-state matching 直接训练预测表征识别真实后继状态，从而改善 PRM 排序与最终任务成功。

## 问题

传统监督式下一状态预测生成 HTML 或 AXTree，却与下游 ranker 的需求错位：即便预测看似合理，只要不同候选动作的状态缺乏判别性，测试时选择仍会失败。

## 创新点或方法

作者从 WebArena Go-Browse 轨迹构造分支数据，每个决策点包含多个备选动作及真实结果；世界模型学习让正确后继状态区别于替代动作状态，再把预测状态交给 PRM 式排序器。

## 证据

在留出的 predicted-state matching 基准上优于监督下一状态模型；在 WebPRMBench 上优于纯动作 PRM 和加入监督世界模型的 PRM；在 WebArena-Lite 上提高端到端成功率。摘要未给数字。


## 局限

摘要没有说明判别性提升是否牺牲状态校准或跨网站泛化，也无法判断端到端收益大小。

- **判断**：值得精读目标函数和分支数据构造；这是对“预测得像”与“预测得有决策价值”之间差异的清晰论证。

## 研究关联

它对世界模型和 Agent 的实际启示是：训练目标应服务于行动选择，而非单独追求状态重建；这一原则也可能迁移到机器人候选动作评估。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Discriminative World Models for Web Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent web agents use world models for test-time action selection by sampling candidate actions, predicting the resulting web states, and ranking them with a ranker model or a Process Reward Model (PRM). These world models are typically trained via supervised next-state prediction to generate fixed representations like HTML or AXTree snapshots. However, this objective is misaligned with the downstream ranker, which relies on predicted states being discriminative across candidates to accurately score them. To address this, we introduce predicted-state matching, a training objective where the predicted representation must distinguish the true resulting state from those reached by alternative actions. We train these models using a branching web-agent dataset derived from WebArena Go-Browse trajectories, where every decision point contains multiple alternative actions and their resulting states. Experiments on our held-out predicted-state matching benchmark show that our approach outperforms world models trained with supervised next-state prediction. We further show that our approach improves PRM-style action ranking on WebPRMBench compared with action-only PRMs and PRMs augmented with supervised-next-state world models. Finally, on WebArena-Lite, using our world model for test-time action selection improves end-to-end task success. Our project page is available at: https://dhruvpendharkar.github.io/dwm/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02885v1
- Authors: Kelvin Li, Dhruv Pendharkar, Anish Pahilajani, Chuyi Shang, Leon Oks, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig
- Published: 2026-09-02T17:59:40Z
- Age days: 0

</details>
