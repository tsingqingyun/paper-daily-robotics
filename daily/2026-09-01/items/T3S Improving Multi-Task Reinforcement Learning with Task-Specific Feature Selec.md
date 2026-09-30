---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.30765v1"
published: "2026-08-31T13:30:06Z"
age_days: 0
score: 28
created: 2026-09-01
concepts: ["机器人学习", "具身智能评测与基准"]
---

# T3S: Improving Multi-Task Reinforcement Learning with Task-Specific Feature Selector and Scheduler

> [!summary] 先说人话（基于摘要）
> T3S 用任务专属软掩码减少多任务表征冲突，并由调度器优先训练进度低、学习慢的任务，联合解决“共享什么”和“先学什么”。

## 这篇到底在做什么

- **卡在哪里**：多任务强化学习通常让所有任务共享同一组参数，却没有决定哪些特征应跨任务共享，导致任务间干扰、学习效率下降；固定或均匀采样也可能忽略落后任务。
- **关键解法**：输入任务标识和共享表征，hypernetwork 生成任务特定软掩码并筛出专属特征；调度器根据任务进度（如成功率）和学习速度决定采样概率，二者越低越容易被选择。区别于全量参数共享，它做软特征隔离并自适应安排训练任务。
- **拿什么证明**：摘要称在多种机器人操作任务上持续优于最先进 MTRL 算法，但未给出环境、成功率、样本效率或提升数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习，它提供较通用的负迁移治理方案，适合任务分布不均、难度差异大的多技能训练；对 VLA、世界模型或具身基准没有直接贡献。
- **先别急着信**：需核查掩码是否真正减少干扰而非增加容量，以及逆进度、逆学习速度调度会不会过度消耗训练在难以学习的任务上。
- **判断**：多任务 RL 研究者可读方法与调度消融；在缺少摘要数字的情况下，创新性和收益仍需与强基线细看。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/T3S Improving Multi-Task Reinforcement Learning with Task-Specific Feature Selec.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multi-task reinforcement learning (MTRL) is a technique to train multiple tasks simultaneously, where previous works usually train a single model to solve different tasks by sharing parameters across various tasks. However, these methods are faced with inter-task interference since what parameters should be shared across tasks is not addressed, dramatically reducing learning efficiency. To solve these problems, we propose a novel MTRL framework called Task-Specific feature Selector and Scheduler (T3S), which consists of two components: a feature selector and a task scheduler. Specifically, the feature selectors employ hypernetworks to construct task-specific soft masks, which can be applied by globally shared representation to construct task-specific features. The task scheduler selects tasks for learning through two metrics, where the selection probability is inversely proportional to task progress (e.g., success rate) and task learning speed. Experimental results show that T3S consistently outperforms the state-of-the-art MTRL algorithms on various robotics manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.30765v1
- Authors: Yuanqiang Yu, Tianpei Yang, Yongliang Lv, Yan Zheng, Jianye Hao
- Published: 2026-08-31T13:30:06Z
- Age days: 0

</details>
