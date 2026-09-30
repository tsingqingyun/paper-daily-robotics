---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02885"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-09-04
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Discriminative World Models for Web Agents

> [!summary] 先说人话（基于摘要）
> 该论文认为网页世界模型不应只逼真预测下一页，还必须让不同候选动作产生的预测状态容易区分。它用predicted-state matching训练世界模型辨认真实后继状态与其他动作分支，从而改善PRM排序和测试时选行动作。

## 问题

传统下一状态监督只生成HTML或AXTree等固定表示，却没有直接优化候选动作间的判别性；下游排序器即使拿到看似合理的预测，也可能无法区分哪个动作更好。

## 创新点或方法

从WebArena Go-Browse轨迹构造分支数据，每个决策点包含多个备选动作及其后继状态；训练时要求预测表示匹配真实动作结果并排除其他分支。输出的判别式状态表示供PRM式排序器在测试时评价候选动作，区别于单纯重建下一状态。

## 证据

在留出的predicted-state matching基准上优于监督式下一状态模型；在WebPRMBench上超过动作式PRM及加入传统世界模型的PRM；用于WebArena-Lite测试时动作选择后提升端到端成功率。摘要未给出可核查的结果数字。


## 局限

证据来自网页Agent，摘要未说明判别目标是否牺牲状态生成的完整性，也未验证对连续机器人动力学的适用性。

- **判断**：做测试时搜索、PRM或决策型世界模型者值得精读；核心训练目标简洁且下游链路完整，但机器人价值仍待验证。

## 研究关联

对Agent与世界模型研究者，它明确指出预测目标应与决策用途对齐：用于选动作的状态表示首先要能区分分支。这一原则也可迁移到机器人规划中的候选动作评估。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/Discriminative World Models for Web Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02885v1 Announce Type: new Abstract: Recent web agents use world models for test-time action selection by sampling candidate actions, predicting the resulting web states, and ranking them with a ranker model or a Process Reward Model (PRM). These world models are typically trained via supervised next-state prediction to generate fixed representations like HTML or AXTree snapshots. However, this objective is misaligned with the downstream ranker, which relies on predicted states being discriminative across candidates to accurately score them. To address this, we introduce predicted-state matching, a training objective where the predicted representation must distinguish the true resulting state from those reached by alternative actions. We train these models using a branching web-agent dataset derived from WebArena Go-Browse trajectories, where every decision point contains multiple alternative actions and their resulting states. Experiments on our held-out predicted-state matching benchmark show that our approach outperforms world models trained with supervised next-state prediction. We further show that our approach improves PRM-style action ranking on WebPRMBench compared with action-only PRMs and PRMs augmented with supervised-next-state world models. Finally, on WebArena-Lite, using our world model for test-time action selection improves end-to-end task success. Our project page is available at: https://dhruvpendharkar.github.io/dwm/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02885
- Authors: Kelvin Li, Dhruv Pendharkar, Anish Pahilajani, Chuyi Shang, Leon Oks, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
