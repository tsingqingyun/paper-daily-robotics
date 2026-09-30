---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.25395"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 26
created: 2026-09-05
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# A Taxonomy of Construction Task Activities for Robot Workers

> [!summary] 先说人话（基于摘要）
> TARCAT 把建筑工人的复杂任务拆成41种动作原语，并允许将带参数的原语序列组合成可复用技能。它为收集示范、定义机器人能力和检索技能库提供统一的人类可读词汇。

## 问题

VLA 虽可能扩大机器人技能范围，但建筑部署首先缺少精确的工作活动清单，以及完成每项活动所需能力的共同定义；没有这种结构，数据、硬件需求和技能库难以对应。

## 创新点或方法

作者从七类高就业建筑职业的91项 O*NET 任务及30段实作教学视频中归纳分类，形成12组、三大类共41个动作原语，并给出参数化序列组合机制；部分原语在 DOBOT CR3 与 CRAFT 手上演示。

## 证据

分类依据包括91项职业任务和30段视频，产出41个原语、12组、三类；摘要仅称演示了部分原语，没有报告覆盖率、评审一致性或机器人成功率。


## 局限

需核查分类的完整性、不同标注者能否一致使用，以及41个原语是否足以组合现实建筑流程；少量机器人演示不能证明可部署性。

- **判断**：做建筑机器人或技能库工程者值得通读并评估分类；算法研究者可把它当任务本体参考，无需期待性能突破。

## 研究关联

对建筑机器人、VLA 和技能型 Agent，它能帮助结构化示范标签、能力需求与可检索技能库，适合作为领域数据和任务规划的中间语言。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/A Taxonomy of Construction Task Activities for Robot Workers.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.25395v2 Announce Type: replace Abstract: Recent vision-language-action models offer a path toward robots with broader repertoires than conventional task-specific systems. Construction deployment, however, requires a precise inventory of worker activities and the capabilities needed to execute them. We present TARCAT, an occupation-grounded taxonomy derived from 91 O*NET tasks across seven high-employment construction occupations and 30 instructional videos of physical work. TARCAT defines 41 action primitives in 12 groups and three classes and provides a mechanism for composing parameterized primitive sequences into reusable skills. This human-interpretable structure can organize demonstrations, specify robot requirements, and support coding agents that retrieve and extend skill libraries. We also demonstrate selected primitives on a DOBOT CR3 arm with a CRAFT hand. TARCAT thereby provides a common vocabulary for analyzing human work and developing general-purpose construction robots. Annotations are available at https://github.com/AICPS/TARCAT-Taxonomy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.25395
- Authors: Sadman Sakib, Zhangyi None Peng, Yujie Pang, Yu Otsuki, Mohammad Abdullah Al Faruque
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
