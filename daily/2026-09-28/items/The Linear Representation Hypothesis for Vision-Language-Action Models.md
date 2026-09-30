---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30996v1"
published: "2026-09-25T08:41:36Z"
age_days: 3
score: 28
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# The Linear Representation Hypothesis for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> 这篇工作为 VLA 的线性探测与线性干预建立理论形式：不仅问内部表示能读出什么，还问沿某个方向改变策略能否可预测地影响未来物理量。验证目前在构造的导航系统中完成。

## 问题

具身系统中，表示影响动作，动作改变物理状态，状态又影响下一时刻表示。只研究静态语义属性的线性读出，无法直接描述这种闭环动力学。

## 创新点或方法

基于 signature 构建统一表示与策略的理论：证明存在可线性探测候选动作轨迹下未来关注量的表示；以 signature 广义线性模型描述随机动作块，使自然参数空间中的线性路径对应未来关注量期望的单调变化。

## 证据

在平面控制仿射导航实验中构造显式 oracle 表示，验证预期的线性探测和干预机制。摘要未给出可核查的结果数字，也未报告真实预训练 VLA 上的验证。

## 局限

存在性结果和人为构造的 oracle 表示，不等于实际训练的 VLA 自然具备这种结构；需核查定理假设与真实策略的距离。

- **判断**：做表示理论或内部干预的人值得精读假设与证明，应用团队读结论和验证边界即可。

## 研究关联

对 VLA 表示与世界模型研究者，它帮助区分“读出物理信息”和“控制未来物理量”两个问题，为内部表示干预提供明确的理论目标。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/The Linear Representation Hypothesis for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs). A growing body of work has begun extending this perspective to vision-language-action (VLA) models, but the dynamical nature of embodied interaction introduces an additional challenge. Unlike semantic attributes commonly studied in LLMs, such as gender or language, a physical quantity of interest (QoI) in a VLA evolves jointly with the system dynamics: the representation influences the actions selected by the policy, which alter the physical state and, in turn, the next representation. In this paper, we develop a theoretical, signature-based formulation of the LRH for VLA that unifies representations and policies. On the representation side, we establish the existence of representations from which the future evolution of a QoI under a candidate action trajectory can be recovered via linear probing. On the policy side, we introduce a signature generalized linear model for stochastic action chunks. This structure yields a monotonic change in the expected future QoI along linear paths in natural parameter space, enabling linear steering. We construct an explicit oracle representation in a planar control-affine navigation experiment and verify the predicted linear probing and steering mechanisms.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30996v1
- Authors: Minseok Jeong, Hyewon Choi, Hiroyasu Tsukamoto, SooJean Han
- Published: 2026-09-25T08:41:36Z
- Age days: 3

</details>
