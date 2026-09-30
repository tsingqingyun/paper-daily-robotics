---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.25757v2"
published: "2026-08-26T13:05:29Z"
age_days: 3
score: 32
created: 2026-08-30
concepts: ["智能体 Agent", "视觉语言动作模型 VLA"]
---

# LM-X: Explainable Action Modeling with Progress, Event, and Uncertainty Prediction for Generalist Robot Manipulation

> [!summary] 先说人话（基于摘要）
> LM-X让 VLA 在出动作时同步预测进度 RTG、下一语义事件 ETG 和动作不确定性，并让这些显式状态反过来条件化动作，而非事后生成解释。

## 问题

长时程 VLA通常只学短时动作，单一动作目标要隐式承担任务进度、中间意图和局部可靠性，执行时这些状态又不可见，既削弱控制也妨碍诊断。

## 创新点或方法

输入视觉语言观测，在线输出 RTG、ETG、带异方差的动作流及动作。三种监督分别覆盖任务、事件和运动尺度，并直接参与动作生成；区别于纯动作头或控制完成后的文本解释。

## 证据

五任务预训练门控实验中，完整模型比纯动作骨干高 16.0 点，比最佳单头版本高 10.8 点。随后用 64 张 B200 训练 20 天，数据超过 2 万小时且含逾 1000 小时失败轨迹；RoboTwin2.0 为 74.1% 对 55.4%，七项真机任务为 68.6% 对 50.7%。


## 局限

需全文核查这些信号的标注来源与校准度；相关曲线符合直觉，并不自动证明解释忠实或具有因果作用。

- **判断**：值得精读监督定义、预训练门控和解释忠实性实验；性能与可观测控制状态的结合很有研究价值。

## 研究关联

对 VLA 与 Agent 研究者，显式进度、事件和可靠性信号既可增强长时程控制，也可能为监控、恢复和人机协作提供可直接消费的内部状态。

- **概念**：智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/LM-X Explainable Action Modeling with Progress, Event, and Uncertainty Predictio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist vision--language--action (VLA) policies learn long-horizon behavior mainly through short-horizon action prediction and reveal little beyond sampled commands. This creates two coupled bottlenecks: a single action target must implicitly absorb task progress, intermediate intent, and local reliability, while these control states remain hidden during execution. Inspired by functional principles of biological sensorimotor control, we introduce LM-X , which organizes prediction across task, event, and motor scales without claiming anatomical correspondence. Three explicitly supervised signals are emitted online and directly condition action generation: return-to-go (RTG) measures visible task progress, event-to-go (ETG) identifies the next semantic transition, and heteroscedastic action flow estimates local reliability through propagated variance. Explanation is therefore intrinsic to control rather than generated post hoc. Before a costly 20-day pretraining run on 64 NVIDIA B200 GPUs, a controlled five-task pretraining gate verifies the design: the complete model improves success by 16.0 points over the action-only backbone and by 10.8 points over the strongest single-head variant. We then train LM-X on more than 20,000 hours of real-robot trajectories, including over 1,000 hours of failed policy rollouts. LM-X achieves 74.1\% across 50 randomized-hard RoboTwin2.0 tasks versus 55.4\% for GR00T N1.7, and 68.6\% versus 50.7\% across seven real-robot tasks. RTG tracks semantic progress and visible regression, while variance rises during hesitation and oscillatory control. These results show that explicit multi-timescale predictive state can strengthen control while exposing interpretable internal estimates.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.25757v2
- Authors: Jin Lou, Zhiyuan Jing, Andong Chen, Xupeng Wang, Yuan Xu, Yuexuan Li, Xingdong Zhu, Zhijie Zhu, Yingwei Ji, Wenpeng Nie, Yufei Liu, Boyang Xing, Lei Jiang, Yan Cui, Ying Chu, Jingxuan Zhu, Jingyi Li, Liangliang Chen, Jinyan Liu, Zhiqi Song, Jidong Zhang, Hongming Li, Yuchen Zhu
- Published: 2026-08-26T13:05:29Z
- Age days: 3

</details>
