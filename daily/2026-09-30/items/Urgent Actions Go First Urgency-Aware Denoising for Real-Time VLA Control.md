---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37772v1"
published: "2026-09-29T15:13:14Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control

> [!summary] 先说人话（基于摘要）
> Urgency-Aware Denoising（UAD）让马上要执行的动作先完成去噪并交给机器人，后面的动作在后台继续细化。它利用动作按顺序执行的特点降低等待时间，再修复提前释放带来的误差与轨迹不一致。

## 问题

扩散和流匹配 VLA 需要多轮去噪才能输出动作块，拖慢实时控制。已有加速把整块动作当成统一计算单元，忽视块内动作实际执行时间不同。

## 创新点或方法

按动作紧急程度分配去噪步数，将尾部计算与真实执行重叠。Trajectory Reconciliation 重建统一内部状态演化，且不增加模型评估次数；Ghost Action Correction 利用不实际执行的延续动作补偿提前释放误差。

## 证据

摘要报告跨多种 VLA 架构、仿真基准和真实操作任务评测，平均动作可用延迟最高加速 1.89 倍，并保持与采用最优去噪预算的原始推理相近的成功率；成功率与延迟权衡优于所比较加速基线。

## 局限

1.89 倍对应平均动作可用延迟，不能直接解释为整项任务提速；需核查紧急动作误差、控制周期和成功判定如何共同评估。

- **判断**：值得精读调度与两种修正机制，并结合本期基准审计论文检查其成功率与延迟口径。

## 研究关联

对实时 VLA，提供了利用执行时序重新安排推理计算的方法，适合关注动作块等待问题的研究者。摘要未验证世界模型应用，不能直接外推。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Urgent Actions Go First Urgency-Aware Denoising for Real-Time VLA Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Diffusion and flow-matching Vision-Language-Action (VLA) policies generate action chunks through iterative denoising, incurring substantial inference latency that severely limits real-time robotic control. Existing acceleration methods treat an action chunk as a monolithic computational unit, ignoring a crucial physical reality of receding-horizon control: actions are generated jointly but consumed sequentially, resulting in inherently heterogeneous execution urgencies. We exploit this asymmetry to introduce Urgency-Aware Denoising (UAD), a novel inference-time framework that allocates denoising computation according to when each action is physically needed. UAD releases time-critical urgent actions after fewer denoising steps while overlapping the continued background refinement of tail actions with physical execution. However, heterogeneous denoising introduces two key challenges: early-release errors in urgent actions and trajectory inconsistency in tail actions. UAD elegantly resolves both through two core mechanisms: Trajectory Reconciliation, which reconstructs unified internal state evolution to restore joint denoising coherence without additional model evaluations, and Ghost Action Correction, which leverages non-executed ghost continuations to dynamically compensate for early-release errors across remaining executable actions. Extensive evaluations across multiple VLA architectures, simulation benchmarks, and real-world manipulation tasks demonstrate that UAD achieves up to a 1.89x speedup in average action availability latency while maintaining comparable success rates to vanilla inference with optimal denoising budget, offering a more favorable success-latency trade-off than state-of-the-art VLA acceleration baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37772v1
- Authors: Zibo Wang, Haochen Han, Pengzhen Ren, Mingtong Dai, Fangming Liu
- Published: 2026-09-29T15:13:14Z
- Age days: 0

</details>
