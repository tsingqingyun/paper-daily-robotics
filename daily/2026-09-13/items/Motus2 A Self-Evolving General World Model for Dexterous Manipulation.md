---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.30237"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 33
created: 2026-09-13
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Motus2: A Self-Evolving General World Model for Dexterous Manipulation

> [!summary] 先说人话（基于摘要）
> Motus2让同一个共享权重模型既提出动作、预测动作后果，又评价预测结果，以此形成灵巧操作的决策与学习闭环。它还将第一人称数据、机器人数据和触觉反馈纳入系统。

## 问题

目标是让具身系统通过预测与评价持续改善策略。摘要认为，现有世界模型通常只给模拟器附加动作输出头，没有把行动、预测和评价真正耦合为策略改进闭环。

## 创新点或方法

共享权重模型提供策略、动作条件模拟器和值模型三个接口：策略生成候选动作块，模拟器预测视觉后果，评价器评分。专家示范用于动作学习，失败与次优交互用于动力学和值学习；数据从单目、双目第一人称数据扩展到机器人适配。

## 证据

摘要描述了滑动窗口上下文的扩展研究、触觉接入，以及双目视觉、双臂、双灵巧手平台上的系统实现；摘要未给出可核查的结果数字。


## 局限

需核查预测和评价如何具体产生学习更新，以及连续改进是否有实验支撑；系统组成和数据扩展本身不足以证明“自我进化”。

- **判断**：值得读架构与训练流程，暂将其视为系统路线提案，效果判断应等待全文结果。

## 研究关联

对世界模型和VLA研究者，值得关注的是三个接口如何共享表示，以及失败轨迹如何进入策略改进过程，而非只被过滤掉。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/Motus2 A Self-Evolving General World Model for Dexterous Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.30237v2 Announce Type: replace-cross Abstract: General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-evolving general world model for dexterous manipulation. Motus2 advances world modeling through model scaling and data scaling. For model scaling, a single model with shared weights exposes three control interfaces: a policy (world-action model), a simulator (action-conditioned world model), and an evaluator (value model). The policy proposes candidate action chunks, the simulator predicts their visual consequences, and the evaluator assesses the predicted outcomes. Their coupling forms a closed decision-and-learning loop for policy improvement. This formulation uses curated expert demonstrations for action learning, while failed and suboptimal interactions provide valuable evidence for dynamics modeling and value learning. For data scaling, Motus2 progresses from large-scale monocular egocentric data to synchronized stereo egocentric data, followed by robot-domain adaptation with robot trajectories and supplementary human-robot alignment data. Motus2 further studies global-autoregressive and hybrid-memory extensions of its sliding-window context, adds tactile feedback for contact-aware control, and is instantiated on a fully biomimetic platform with stereo vision, dual arms, dual dexterous hands, and tactile sensing. Together, egocentric data scaling and closed-loop general world model scaling provide a general path toward self-evolving dexterous manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.30237
- Authors: Hongzhe Bi, Zihao Zhou, Yihang Tang, Jingrui Pang, Shuhe Huang, Haitian Liu, Runqing Wang, Shuai Huang, Yichen Wang, Yiming Cheng, Ruowen Zhao, Zhenghua Li, Hengkai Tan, Xiaolong Liu, Jinhui Wan, Jiabao Liu, Min Zhao, Fan Bao, Jun Zhu
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
