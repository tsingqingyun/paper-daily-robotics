---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19659v1"
published: "2026-09-17T03:59:11Z"
age_days: 0
score: 29
created: 2026-09-18
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# EmbodiedMind: Adaptive Data Curation and Prefix-Tree Reinforcement Learning for Efficient Embodied Intelligence

> [!summary] 先说人话（基于摘要）
> EmbodiedMind从挑选训练样本、平衡不同任务和细分长程决策奖励三方面提高训练效率；其中Trie-GRPO用动作前缀树区分前面做对与后面做错的步骤。

## 问题

具身模型训练存在低信息样本浪费、异质任务梯度贡献失衡，以及整条轨迹奖励把后续失败归咎于所有前序令牌的问题。

## 创新点或方法

RSFT过滤低信息样本建立行为先验；IR-GRPO用按难度分层的任务队列与混合奖励调节训练；Trie-GRPO在动作前缀树上估计步骤级优势，细化长程规划的信用分配。

## 证据

摘要报告18个基准平均性能70.02%，声称达到最优平均水平，并在长程规划准确率上显著超过其他具身基础模型；未列分项数值。

## 局限

需核查18个基准的构成与平均口径，以及三阶段分别带来的收益；摘要没有量化计算资源节省。

- **判断**：值得重点读Trie-GRPO与阶段消融，整体最优和高效训练的判断需等分项结果与成本对照。

## 研究关联

对具身Agent和机器人学习，价值是把训练数据利用与长程信用分配放在一起处理，适合多任务规划训练参考。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/EmbodiedMind Adaptive Data Curation and Prefix-Tree Reinforcement Learning for E.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Training embodied foundation models typically requires massive-scale datasets and extensive computational resources, yet often suffers from three critical limitations: (1) inefficient sample utilization due to low-informative samples; (2) imbalanced gradient contributions across heterogeneous tasks; and (3) severe credit assignment problem in long-horizon planning, where trajectory-level rewards indiscriminately penalize all tokens. To address these issues, we propose an efficient training paradigm that achieves state-of-the-art average performance through strategic data selection and hierarchical policy optimization. Our approach consists of three synergistic stages. First, Rejection Sampling-based Fine-Tuning (RSFT) filters out low-informative samples to establish robust behavioral priors while preventing distributional collapse. Second, Iterative Rejection GRPO (IR-GRPO) employs task-specific queues stratified by difficulty to keep datasets balanced across reinforcement learning iterations, coupled with a hybrid reward mechanism for precise cross-task feedback. Third, to enhance long-horizon task planning, we introduce Trie-GRPO, a novel reinforcement learning algorithm based on action prefix trees, which enables step-level advantage estimation. This resolves the credit assignment problem by isolating intermediate correct decisions from downstream errors, while effectively balancing exploration efficiency and depth compared to conventional search trees. As a result, EmbodiedMind achieves a state-of-the-art average performance of 70.02% across 18 benchmarks, and significantly outperforms other embodied foundation models in long-horizon task planning accuracy. Our project will be released for reproducibility.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19659v1
- Authors: Feifan Wang, Zongbing Zhang, Yu Zhang, Lingfeng Wang, Yurui Zhu, Jin Deng, Mingliang Zhang, Zhengguang Gao, Yongcheng Wang, Jin Xu, Ri Yang
- Published: 2026-09-17T03:59:11Z
- Age days: 0

</details>
