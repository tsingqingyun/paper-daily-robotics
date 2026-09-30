---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04096v1"
published: "2026-09-03T17:03:11Z"
age_days: 3
score: 24
created: 2026-09-07
concepts: ["多模态基础模型", "世界模型"]
---

# Adaptive Vision-Language Grasping via Composable Foundation Priors and Generalizable Grasp Synthesis

> [!summary] 先说人话（基于摘要）
> AdaRoboVLG 把通用物理抓取与任务语义理解拆开：基础策略用运动学映射和力闭合估计生成稳定抓取，基础模型模块只提供可组合的空间、认知和时间先验。

## 这篇到底在做什么

- **卡在哪里**：现有VLG常把基础模型与端到端抓取策略紧耦合，换机器人手或任务理解模块时可能需要重训，也难同时保证语义适配和物理可行性。
- **关键解法**：输入包括场景与任务相关先验，输出适配不同机械手的抓取。基础策略显式生成并评估物理可行候选；专门基础模型模块提供可组合先验并注入候选选择，无需重训底层抓取策略。
- **拿什么证明**：摘要称仿真和真实实验显示基础策略学习高效且可跨手泛化；空间、认知、时间先验分别应对三类挑战，性能不逊于先进方法，并可联合用于拥挤动态环境的功能性抓取。未给成功率或样本效率数字。

## 值不值得读

- **和你的研究有什么关系**：它为多模态基础模型接入机器人抓取提供模块化路线：未来升级语义模型时，无需重新设计物理抓取核心。
- **先别急着信**：需核查所谓“不重训”覆盖哪些任务变化、先验模块如何产生可靠信号，以及跨手泛化涉及多大形态差异。
- **判断**：做通用抓取或模块化基础模型控制者值得看系统接口和跨手实验；定量证据需阅读全文确认。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Adaptive Vision-Language Grasping via Composable Foundation Priors and Generaliz.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This paper proposes AdaRoboVLG, a task-adaptive Vision-Language-Grasp (VLG) framework that supports generalizable grasp synthesis across different robotic hands. Unlike existing VLG methods that tightly couple foundation models with end-to-end grasp policies, AdaRoboVLG learns an efficient generalizable base policy that generates and evaluates physically feasible grasp candidates through explicit kinematic mapping and force-closure-based stability estimation, while offloading task-dependent understanding to specialized foundation-model modules. These modules provide composable priors that are integrated into the grasp synthesis process, enabling contextually adaptive grasp synthesis without retraining the underlying grasp policy. Through extensive simulation and real-world experiments, we demonstrate that (i) the base policy exhibits efficient learning and strong cross-hand generalization, (ii) the framework effectively incorporates spatial, cognitive, and temporal priors to address three representative grasping challenges without compromising grasp synthesis performance compared to state-of-the-art methods, and (iii) these priors can operate jointly to enable functional grasping in cluttered and dynamic environments. These results indicate that decoupling physical grasp synthesis from task-dependent understanding provides a scalable paradigm for robotic grasping, allowing future advances in foundation models to be directly translated into improved grasp capabilities without redesigning or retraining the underlying grasp policy. Supplementary videos are available at https://adarobovlg.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04096v1
- Authors: Sixu Yan, Shikang Wang, Binhua Huang, Xuanlai Tang, Guohua Fan, Fan Huang, Haoxuan Li, Yongkang Li, Yuhan Li, Bencheng Liao, Zeyu Zhang, Wenyu Liu, Hangxin Liu, Xinggang Wang
- Published: 2026-09-03T17:03:11Z
- Age days: 3

</details>
