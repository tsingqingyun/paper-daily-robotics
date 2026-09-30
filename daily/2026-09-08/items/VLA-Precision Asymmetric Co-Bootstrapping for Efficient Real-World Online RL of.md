---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04355"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-09-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> VLA-Precision 让机器人通过真实试错提高精密操作的稳定性。ACoB 先用干预引导行为学习，再逐步校准价值估计；ACoB-Stream 则降低大模型在线学习的系统开销。

## 这篇到底在做什么

- **卡在哪里**：预训练 VLA 在高精度、可重复操作中仍不可靠；真实在线 RL 又受到价值信号失准引起的策略漂移，以及大模型吞吐不足的限制。
- **关键解法**：早期干预改善策略及经验质量，随后结合全局回报传播和局部偏好排序校准价值，用相对动作优势进行参考策略约束下的更新；配套不变状态解耦和按需流式架构。
- **拿什么证明**：在四类、九项高精度化学任务及四种机器人形态上，报告平均成功率 98.3%、每任务 45.8 分钟、单回合 27.6 秒；执行速度为 VLA 和 RL 基线的 1.2 倍、1.8 倍，吞吐与计算效率提升最高 10.9 倍。

## 值不值得读

- **和你的研究有什么关系**：直接关联 VLA 真机后训练：同时处理策略稳定性和实验周转速度，适合精密操作研究者重点参考。
- **先别急着信**：需核查干预用量、45.8 分钟的统计口径及 10.9 倍对应的配置；这些决定结果能否迁移到自己的实验条件。
- **判断**：优先精读算法、干预协议和计时口径；摘要给出的精度与时间结果都足够具体。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/VLA-Precision Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04355v1 Announce Type: new Abstract: Pretrained vision-language-action (VLA) models enable broad manipulation but remain unreliable in tasks demanding precision and repeatability. Applying real-world online reinforcement learning (RL) to VLA post-training enables autonomous trial-and-error improvement beyond demonstrations alone, but exposes two bottlenecks: 1) unreliable value signals can induce policy drift; 2) large-VLA overhead constrains throughput and sample efficiency. To address these challenges, we present VLA-Precision, an efficient real-world online RL framework featuring the Asymmetric Co-Bootstrapping (ACoB) algorithm and the ACoB-Stream architecture. Specifically, ACoB establishes asymmetric co-bootstrapping across timescales: early intervention-guided behavioral learning rapidly improves policy performance while enhancing online experience quality. As autonomous experience accumulates, global return propagation and local preference ranking progressively calibrate value estimates, yielding relative action advantages for reference-regularized policy improvement while suppressing drift. To enable ACoB on large VLAs, we develop ACoB-Stream, a closed-loop experience--policy architecture that establishes invariant-state decoupling and on-demand streaming as design principles, delivering up to 10.9$\times$ improvements in throughput and computational efficiency. Extensive evaluations on nine high-precision chemistry tasks across four categories and four robot embodiments show that VLA-Precision achieves 98.3\% mean success rate in 45.8 min/task, with 27.6 s episodes running at 1.2$\times$ and 1.8$\times$ the speeds of VLA and RL baselines. Resources are available at https://vla-precision.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04355
- Authors: Chenyu Su, Zhaolong Shen, Yuan Qian, Chen Qian, Rui Zhang, Feng Yan, Weixing Chen, Fei Zhang, Jiamin Wang, Shuang Cong, Weiwei Shang
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
