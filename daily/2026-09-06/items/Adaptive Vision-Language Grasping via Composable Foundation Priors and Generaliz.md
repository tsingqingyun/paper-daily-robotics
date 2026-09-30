---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04096"
published: "Sat, 05 Sep 2026 00:00:00 -0400"
age_days: 0
score: 24
created: 2026-09-06
concepts: ["多模态基础模型", "世界模型"]
---

# Adaptive Vision-Language Grasping via Composable Foundation Priors and Generalizable Grasp Synthesis

> [!summary] 先说人话（基于摘要）
> AdaRoboVLG 把“怎么稳定抓”与“当前任务该抓哪里、何时抓”拆开：通用基础策略负责跨机械手的可行抓取，基础模型模块提供可组合的空间、认知和时间先验。

## 这篇到底在做什么

- **卡在哪里**：任务是让不同机械手在上下文、杂乱和动态环境中完成功能性抓取。现有 VLG 往往把基础模型与端到端抓取策略紧耦合，任务变化或基础模型升级时可能需要重训，也不利于跨手泛化。
- **关键解法**：基础策略通过显式运动学映射生成抓取候选，并用基于力闭合的稳定性估计进行评价；专用基础模型模块输出任务相关先验，再组合进候选合成过程。输出是适配具体语境的抓取方案，关键差异是更新任务理解模块时无需改造或重训底层抓取策略。
- **拿什么证明**：摘要称仿真和真实实验显示基础策略学习高效且可跨手泛化，三类先验能分别和联合解决代表性挑战，并在不低于 SOTA 抓取合成表现的情况下支持杂乱动态环境；未给出成功率等数字。

## 值不值得读

- **和你的研究有什么关系**：对多模态机器人研究者，这是比端到端 VLA 更易维护的接口设计：语言视觉模型负责语义先验，几何与力学模块守住物理可行性。它也为世界模型研究提供了将时间先验接入动作合成的具体位置。
- **先别急着信**：需核查跨越了哪些机械手、先验错误时系统如何退化，以及“无需重训”是否覆盖所有组合场景；摘要没有足够细节。
- **判断**：值得抓取与 VLA 系统研究者精读架构和真实实验，重点看模块解耦是否确实带来跨手、跨任务收益。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-06/Adaptive Vision-Language Grasping via Composable Foundation Priors and Generaliz.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04096v1 Announce Type: cross Abstract: This paper proposes AdaRoboVLG, a task-adaptive Vision-Language-Grasp (VLG) framework that supports generalizable grasp synthesis across different robotic hands. Unlike existing VLG methods that tightly couple foundation models with end-to-end grasp policies, AdaRoboVLG learns an efficient generalizable base policy that generates and evaluates physically feasible grasp candidates through explicit kinematic mapping and force-closure-based stability estimation, while offloading task-dependent understanding to specialized foundation-model modules. These modules provide composable priors that are integrated into the grasp synthesis process, enabling contextually adaptive grasp synthesis without retraining the underlying grasp policy. Through extensive simulation and real-world experiments, we demonstrate that (i) the base policy exhibits efficient learning and strong cross-hand generalization, (ii) the framework effectively incorporates spatial, cognitive, and temporal priors to address three representative grasping challenges without compromising grasp synthesis performance compared to state-of-the-art methods, and (iii) these priors can operate jointly to enable functional grasping in cluttered and dynamic environments. These results indicate that decoupling physical grasp synthesis from task-dependent understanding provides a scalable paradigm for robotic grasping, allowing future advances in foundation models to be directly translated into improved grasp capabilities without redesigning or retraining the underlying grasp policy. Supplementary videos are available at https://adarobovlg.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04096
- Authors: Sixu Yan, Shikang Wang, Binhua Huang, Xuanlai Tang, Guohua Fan, Fan Huang, Haoxuan Li, Yongkang Li, Yuhan Li, Bencheng Liao, Zeyu Zhang, Wenyu Liu, Hangxin Liu, Xinggang Wang
- Published: Sat, 05 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
