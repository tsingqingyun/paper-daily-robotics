---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27367"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 19
created: 2026-08-29
concepts: ["世界模型"]
---

# Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models

> [!summary] 先说人话（基于摘要）
> SCG让JEPA的ViT编码器从极小规模起步，按任务需要逐步加注意力头或Transformer层；每次扩容保持函数不变，试验无益便回滚。SIGReg用于防止表示维度坍塌。

## 这篇到底在做什么

- **卡在哪里**：固定尺寸JEPA编码器对简单任务配置过剩、复杂任务又容量不足，注意力头间还有明显冗余。预先按最大规模配置会浪费计算与数据，却缺乏可靠的动态扩容机制。
- **关键解法**：从1头、2层、28.3万参数编码器开始，任务无关的测试—验证机制选择加宽或加深；函数保持扩展使候选结构可安全试用。SIGReg约束语义维度统计独立并与预测目标对齐，扩展无益时回滚。
- **拿什么证明**：在60维多物体动力学任务上触发加深，预测损失比固定小模型改善20.3%，相较扩至固定大模型参数效率高56倍；二维导航中一次加宽比固定大模型改善23%。三个环境中均不弱于固定小模型，误扩展为零，函数保持比率1.0、绝对差0.0。

## 值不值得读

- **和你的研究有什么关系**：对JEPA世界模型，它提供按任务复杂度配置表示容量的可操作方案，可降低为未知任务预留最大网络的浪费。
- **先别急着信**：只有三个环境，且“任务无关”扩展判据仍依赖预测损失；需核查更复杂视觉任务、训练总成本和反复试扩的额外开销。
- **判断**：做高效JEPA或自适应架构值得精读，结果数字明确；是否能扩展到大规模真实视频仍是关键未知。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：19
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/Successive Capacity Growth Task-Complexity-Driven Width and Depth Expansion for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.27367v1 Announce Type: new Abstract: Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transformer blocks for higher-order semantic abstraction), driven by a task-agnostic test-and-verify mechanism that exploits function-preserving expansion to safely trial architectural changes and roll back if they do not improve prediction loss. The Sketched Isotropic Gaussian Regularizer (SIGReg) ensures that all learned semantic dimensions remain statistically independent and aligned with the predictive objective, preventing collapse even as the architecture grows. On a 60-dimensional multi-object dynamics task, SCG naturally triggers depth expansion, improving prediction loss by 20.3% over the fixed small baseline with 56 times greater parameter efficiency than scaling to the fixed large model; on a 2D navigation task, a single width expansion yields even an 23% improvement over the fixed large model. Across all three tested environments of increasing complexity, the adaptive encoder matches or exceeds the fixed small baseline, with zero false-positive expansions and bit-exact function preservation (ratio = 1.0, absolute difference = 0.0). The take-away is that JEPA world model encoders need not be pre-allocated at maximum capacity - they can grow successively as the task demands, achieving significant compute and data efficiency while maintaining representation quality.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27367
- Authors: Frederik Berenz
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
