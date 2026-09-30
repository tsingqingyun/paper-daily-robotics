---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29772v1"
published: "2026-08-30T13:01:32Z"
age_days: 1
score: 33
created: 2026-09-01
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Self-Aware Active Learning Enables Continual Improvement in Autonomous Driving

> [!summary] 先说人话（基于摘要）
> SAGE 让自动驾驶系统判断“何时自己不够可靠”：世界模型产生 fear（短期风险与不确定性）和 curiosity（新颖度）信号，动态触发专家接管并用高价值轨迹继续学习。

## 这篇到底在做什么

- **卡在哪里**：自动驾驶在熟悉条件下可靠，但罕见分布漂移和长尾事件会导致突然失败；被动学习系统既不知道能力边界，也不会及时求助或把危险经历转为有针对性的改进。
- **关键解法**：输入在线观测和世界模型预测，输出风险、好奇度及是否交权。curiosity 动态校准 fear 阈值，超阈值时切换专家或后备策略并用接管轨迹做聚焦模仿学习；fear 同时进入策略优化与评估作为安全约束，区别于固定阈值接管或无选择地收集数据。
- **拿什么证明**：在仿真路线迁移、Waymo 日志场景、CARLA 遮挡危险和真实移动机器人导航上，摘要称其提高新颖及安全关键场景鲁棒性、减少安全违规，同时保持与强基线相当的任务表现；未给具体数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习和具身 Agent，它提供了部署后选择性学习的闭环范式：把不确定性、风险干预和数据采集统一起来，而不是盲目在线探索。
- **先别急着信**：需核查 fear 的校准、专家可用性及误触发代价；摘要也无法说明安全提升是否依赖特定后备策略。
- **判断**：值得精读干预规则和适应协议；其价值在“会求助再学习”的系统机制，不能只看平均驾驶性能。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/Self-Aware Active Learning Enables Continual Improvement in Autonomous Driving.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning-based autonomous driving (AD) systems can perform reliably in familiar conditions, yet rare distribution shifts and long-tail events remain a major source of abrupt failure. A central limitation is that most agents learn primarily from passive experience and lack mechanisms to estimate when their competence is insufficient, seek timely assistance, and convert safety-critical encounters into targeted improvement. Here we present self-aware guided exploration (SAGE), an active learning framework for post-training adaptation in AD. SAGE learns a predictive world model that generates two online intrinsic signals: fear, which estimates short-horizon predictive risk and model uncertainty, and curiosity, which measures novelty through prediction error. Curiosity adaptively calibrates the intervention threshold for fear, allowing the agent to regulate risk in a context-dependent manner. When predicted fear exceeds this adaptive threshold, the agent transfers control to an expert or fallback policy and uses the resulting takeover trajectories for focused imitation learning. In parallel, fear is integrated into policy optimization and evaluation as a safety-oriented constraint to reduce performance regressions during adaptation. We evaluate SAGE in simulated route-transfer tasks, Waymo-based logged driving scenarios, CARLA occlusion hazards, and real-world mobile robot navigation tests. Across these settings, SAGE improves robustness in novel and safety-critical scenarios, reduces safety violations, and maintains task performance comparable to strong baseline policies. These results suggest that agents can improve after initial training by estimating the limits of their competence, requesting guidance when needed, and learning selectively from rare high-value events.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29772v1
- Authors: Dong Hu, Chao Huang, Carman K. M. Lee, Dimitrios Kanoulas
- Published: 2026-08-30T13:01:32Z
- Age days: 1

</details>
