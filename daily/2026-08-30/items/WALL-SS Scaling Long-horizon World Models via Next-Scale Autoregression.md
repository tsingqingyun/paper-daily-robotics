---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26239v1"
published: "2026-08-26T17:57:12Z"
age_days: 3
score: 26
created: 2026-08-30
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression

> [!summary] 先说人话（基于摘要）
> WALL-SS用“逐尺度自回归”生成机器人视觉未来：时间上交错动作与观测，空间上从粗到细生成，并用压缩记忆和 dream forcing 支撑分钟级流式模拟。

## 这篇到底在做什么

- **卡在哪里**：片段式未来预测难同时满足动作—后果耦合、可变时长、连续交互和奖励优化；长时自回归还会因上下文膨胀、自生成误差和动作漂移而失稳。
- **关键解法**：将轨迹表示为因果交错的观测—动作序列，每帧按尺度从粗到细生成。尺度对齐动作条件强化动作影响；近程保留精细记忆、远程压缩，scale-wise dream forcing适应自生成上下文，再以动作跟随和长期一致性奖励做 on-policy alignment。
- **拿什么证明**：摘要称其改善动作跟随和轨迹准确性，可在有界内存下进行连贯的分钟级流式 rollout；on-policy alignment持续减少动作漂移和长期不一致。未给出指标数字。

## 值不值得读

- **和你的研究有什么关系**：对世界模型和机器人学习者，它把长时生成、流式状态复用与奖励对齐放进同一自回归框架，适合模拟、策略评估和视觉想象。
- **先别急着信**：需核查分钟级“连贯”是否对应任务和物理正确，而非仅视觉稳定；摘要也未说明生成速度是否足以闭环。
- **判断**：世界模型研究者值得精读尺度层级和对齐目标；结论强度要等定量长时评测确认。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/WALL-SS Scaling Long-horizon World Models via Next-Scale Autoregression.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generative world models provide robots with predictive models of how the world evolves under interaction, with growing potential for simulation, planning, policy evaluation, and robot learning. Beyond clip-level future prediction, a unified generative formulation should relate actions to consequences, support flexible horizons and continuous interaction, and enable reward-driven optimization. We introduce WALL-SS, a world model that generates visual futures through Scale-wise autoregressive Scaling, enabling action-controllable and long-horizon robotic simulation. WALL-SS represents embodied trajectories as causal sequences of temporally interleaved observations and actions, making action-dependent state transitions explicit while naturally supporting variable-length generation, streaming extension through reusable causal states, and direct optimization through sequence probabilities. To make this formulation effective over long horizons, we generate each future observation in a coarse-to-fine manner and develop three complementary components within the same hierarchy. Action-conditioned next-scale prediction injects scale-aligned action representations to improve action-future coupling and model both successful and failed behaviors. Scale-compressed long-horizon memory retains recent interactions at fine resolution while compressing distant observations and actions, with scale-wise dream forcing enhancing robustness to self-generated context. Finally, on-policy alignment optimizes autoregressive visual dynamics with action-following and long-term consistency rewards while preserving the pretrained visual distribution. Experiments show that WALL-SS improves action following and trajectory accuracy, supports coherent minute-long streaming rollout under bounded memory, and consistently benefits from on-policy alignment in reducing action drift and long-horizon inconsistency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26239v1
- Authors: Maeve Zhang, Rain Sun, Xiang Wang, Cyril Zhang, Shalfun Li, Meng Cao, Howard Lu, Ethan Chen, Harry Jhou, KZ Zheng, Lights Shi, Regis Cheng, Lorenzin, Robert Wang, Victor Yao, Gody Li, Elise Mon, Yohann Tang, Ryan Yu, PS Zhang, Vincent Chen, Hang Su, Roy Gan, Hao Wang, Qian Wang
- Published: 2026-08-26T17:57:12Z
- Age days: 3

</details>
