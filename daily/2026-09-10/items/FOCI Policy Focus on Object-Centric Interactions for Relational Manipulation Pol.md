---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08743v1"
published: "2026-09-08T13:35:56Z"
age_days: 1
score: 25
created: 2026-09-10
concepts: ["世界模型", "机器人学习"]
---

# FOCI Policy: Focus on Object-Centric Interactions for Relational Manipulation Policies

> [!summary] 先说人话（基于摘要）
> FOCI Policy 把操作技能压缩成关键交互时段里物体之间的相对运动，希望少学一些无关轨迹，也减少对场景摆放和机器人形态的依赖。

## 这篇到底在做什么

- **卡在哪里**：物体中心操作策略有助泛化，但已有表示要么过简、刻画不了交互动力学，要么过密、学习效率低；许多刚性关系操作的关键只发生在短暂交互阶段。
- **关键解法**：从示范自动提取紧凑交互片段，并用任务相关物体之间的相对 SE(3) 运动表示技能，同时进行时间和空间抽象，区别于直接预测机器人动作或建模密集物体轨迹。
- **拿什么证明**：在 RLBench、COLOSSEUM 和真实任务上，报告以明显更少训练数据获得较强表现，比较对象包括物体中心与动作中心策略。摘要未给出可核查的成功率或数据量数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习研究者，这是研究数据效率和跨配置泛化的明确归纳偏置；对世界模型，可启发任务相关交互表示，但摘要未展示预测模型用途。
- **先别急着信**：方法动机明确限定于刚性关系操作，需核查交互片段提取和相对运动到可执行机器人动作的衔接。
- **判断**：值得精读表示与控制接口，若数据效率收益在公平设置下成立，实用价值较高。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/FOCI Policy Focus on Object-Centric Interactions for Relational Manipulation Pol.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object-centric manipulation policies improve generalization by modeling object motion instead of directly predicting robot actions. However, existing methods are often limited by representations which are either too simplistic to capture interaction dynamics or too dense to learn efficiently. We observe that many rigid relational manipulation tasks are governed by short interaction phases where the relative motion between task-relevant objects is tightly constrained. Based on this observation, we propose \textsc{Foci Policy}, an interaction-centric framework that achieves a two-fold abstraction: (1) temporally, by automatically extracting compact interaction segments from demonstrations;(2) spatially, by representing skills as relative $SE(3)$ motion between task-relevant objects, yielding invariance to scene configurations and robot embodiment. Experiments on RLBench, COLOSSEUM, and real-world tasks show that \textsc{Foci Policy} achieves strong performance with substantially less training data than prior object-centric and action-centric policies. These results suggest that modeling object-object interactions provides a simple and efficient inductive bias for rigid relational manipulation. Project page: \href{https://fitz0401.github.io/foci-page/}{fitz0401.github.io/foci-page/}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08743v1
- Authors: Ze Fu, Pinhao Song, Yutong Hu, Renaud Detry
- Published: 2026-09-08T13:35:56Z
- Age days: 1

</details>
