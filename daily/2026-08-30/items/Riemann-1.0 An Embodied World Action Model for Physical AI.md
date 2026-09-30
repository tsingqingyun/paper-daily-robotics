---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27033v1"
published: "2026-08-27T12:21:26Z"
age_days: 2
score: 34
created: 2026-08-30
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Riemann-1.0: An Embodied World Action Model for Physical AI

> [!summary] 先说人话（基于摘要）
> Riemann-1.0试图用一个全因果自回归 World Action Model 同时承担机器人策略和动作条件世界模拟，并以渐进式预训练吸收人类、夹爪和多机器人数据。

## 问题

现有 WAM 常将动作与视频联合生成、先预测视频再动作，或分开建模，导致在线策略与世界模拟接口割裂；异构具身数据也难在同一目标下规模化。

## 创新点或方法

把多视角视觉、机器人状态和本体专属动作编码为统一因果序列，输出动作及随后的世界演化。渐进预训练在共享目标下依次整合第一视角人类视频、手持夹爪演示和异构机器人轨迹，区别于策略与模拟器分立的方案。

## 证据

基于超过 20 万小时交互数据；RoboTwin2.0、LIBERO、RoboCasa-365 成功率分别为 94.3%、99.0%、62.6%，后者超过此前最佳 8.4 个百分点。长时程真实操控 SR 85.0%、PSR 94.4%，SR 比最强开源基线高 15 个百分点。


## 局限

摘要未说明 20 万小时数据的组成、各阶段贡献及比较模型的数据规模；统一建模是否优于同规模解耦系统需看消融。

- **判断**：今天最值得阅读全文的规模化工作之一，但应重点审查数据公平性和“一个模型双重用途”的实证强度。

## 研究关联

对世界模型、VLA 和具身预训练研究者，它提供了统一策略—模拟器接口与大规模异构数据配方，也给出了高门槛基准结果。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Riemann-1.0 An Embodied World Action Model for Physical AI.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce Riemann-1.0, a fully causal autoregressive World Action Model for embodied intelligence. Riemann-1.0 jointly models multi-view visual observations, robot states, and embodiment-specific actions within a unified causal autoregressive sequence, representing robot actions and world evolution as causal state transitions. Unlike existing WAMs based on joint generation, video-first prediction, or decoupled modeling paradigms, Riemann-1.0 unifies online robot policy execution and action-conditioned world simulation within a single model, enabling it to function as both an executable robot policy and a multi-embodiment visual world simulator. To scale embodied experience across heterogeneous data sources, we further develop a progressive embodied pretraining framework that unifies learning from egocentric human videos, handheld-gripper demonstrations, and heterogeneous robot trajectories under a shared World Action Modeling objective. Built upon 200K+ hours of interaction data, Riemann-1.0 progressively transfers large-scale embodied experience into executable robot manipulation capabilities. Riemann-1.0 achieves state-of-the-art performance across both simulation benchmarks and real-world manipulation tasks. It achieves success rates of 94.3% on RoboTwin2.0, 99.0% on LIBERO, and 62.6% on the long-horizon compositional benchmark RoboCasa-365, outperforming the previous best method by 8.4% On long-horizon real-world manipulation tasks, Riemann-1.0 achieves a Success Rate (SR) of 85.0% and a Progress Success Rate (PSR) of 94.4%, exceeding the strongest open-source baseline by 15% in SR. These results demonstrate that unified World Action Modeling together with progressive embodied pretraining effectively transforms large-scale embodied experience into generalizable robot manipulation capabilities.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27033v1
- Authors: Haofeng Sun, Jiangbo Pei, Fei Kang, Zexiang Liu, Yaokun Li, Boyi Jiang, Hua Xue, Cindy Zhou, Wei Li, Yichen Wei, Mengyin An, Fanliang Zhao, Biao Jiang, Zile Wang, Yang Liu, Yangguang Li
- Published: 2026-08-27T12:21:26Z
- Age days: 2

</details>
