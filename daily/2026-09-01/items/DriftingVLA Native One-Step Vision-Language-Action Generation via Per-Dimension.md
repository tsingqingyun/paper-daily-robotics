---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29749v1"
published: "2026-08-30T12:21:44Z"
age_days: 1
score: 31
created: 2026-09-01
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# DriftingVLA: Native One-Step Vision-Language-Action Generation via Per-Dimension Temporal Drifting

> [!summary] 先说人话（基于摘要）
> DriftingVLA 用 distribution-drifting 目标直接学习噪声到完整动作块的一步映射；PDTD 再把每个动作维度的整段时间轨迹作为独立 drifting 单元，细化不同控制维度的分布。

## 问题

传统 flow-based VLA 虽能生成连续动作，却要多步积分和迭代精炼每个动作块，增加在线控制延迟。直接一步生成又需同时保持不同动作维度的语义和分布特性。

## 创新点或方法

训练时，PDTD 分别塑造各动作维度的时间轨迹分布；推理时仍由共享 VLA 联合输出完整动作块，以保留跨维依赖。关键差异是原生学习一步噪声—动作映射，而不是训练 flow field 后在部署时积分。

## 证据

LIBERO 成功率 98.32%，RoboTwin 2.0 为 81.09%，六个真实单臂和双臂任务平均 77.67%，优于所评估的多步 flow 策略和一步 VLA 基线；动作块生成加速 3.36 倍。


## 局限

需核查 3.36 倍加速的硬件和端到端控制占比，以及按维分解训练在强耦合双臂动作中的收益是否稳定。

- **判断**：值得精读，证据在本批推理加速论文中较完整；特别应比较其原生一步方案与 AdaVLA 的免训练自适应路线。

## 研究关联

它直接改善 VLA 实时部署的速度—性能权衡，并提供区别于事后蒸馏或动态减步的原生一步训练路线。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/DriftingVLA Native One-Step Vision-Language-Action Generation via Per-Dimension.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Conventional flow-based vision-language-action (VLA) models support expressive continuous action generation but rely on multi-step refinement to produce each action chunk, increasing latency in online robot control. To address this issue, we introduce DriftingVLA, a native one-step VLA that generates a complete action chunk with a single action-expert forward pass. Rather than learning a flow field that requires iterative integration at inference, DriftingVLA uses a distribution-drifting objective to learn a direct noise-to-action-chunk mapping for one-step deployment. Since robot action dimensions carry distinct control semantics and distributional characteristics, we further introduce Per-Dimension Temporal Drifting (PDTD). PDTD treats the complete temporal trajectory of each action dimension as a separate drifting unit, enabling finer-grained modeling and shaping of dimension-specific action distributions. This per-dimension decomposition applies only to the training objective; the shared VLA model still generates the complete action chunk jointly, thereby preserving cross-dimensional dependencies. DriftingVLA achieves 98.32% success on LIBERO, 81.09% on RoboTwin 2.0, and 77.67% across six real-world single- and dual-arm tasks, outperforming the evaluated multi-step flow policy and one-step VLA baselines. Native one-step deployment also delivers a 3.36-fold speedup in action-chunk generation, eliminating iterative refinement without sacrificing control performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29749v1
- Authors: Yuxuan Gao, Shiqi Zhang, Yedong Shen, Yifan Duan, Wenhao Yu, Xin Zhang, Siyuan Cao, Jiajun Deng, Yanyong Zhang
- Published: 2026-08-30T12:21:44Z
- Age days: 1

</details>
