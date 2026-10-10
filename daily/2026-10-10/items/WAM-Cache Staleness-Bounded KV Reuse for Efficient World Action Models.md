---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.11401v1"
published: "2026-10-08T07:33:59Z"
age_days: 1
score: 36
created: 2026-10-10
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# WAM-Cache: Staleness-Bounded KV Reuse for Efficient World Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> WAM-Cache 把世界动作模型上一轮的视觉 KV 表示留下来，每轮只更新部分位置，减少重复计算。它发现更新优先级应同时看动作专家关注哪里、视觉信息哪里意外变化，并限制缓存最多能用多久。

## 问题

世界动作模型每次执行一段动作前，都让视频 DiT 把当前观察编码成各层 KV，供动作专家读取；这部分预填充计算占据主要成本。摘要指出，已有无需训练的加速方法仍完整计算它。只刷新视觉变化大的位置也不够，即使能准确预知 KV 变化，表现仍明显低于完整计算基线。

### 用一个例子理解

理解用例（非论文实验）：机器人夹住杯子靠近托盘，背景电视画面持续变化。缓存保留部分背景表示，优先刷新动作专家读取的杯沿和托盘附近信息，同时更新视觉意外变化处；过旧表示强制刷新，再由动作专家输出下一段动作。

## 创新点或方法

旧做法每轮重算全部视觉表示；WAM-Cache 跨动作块保留各层 KV，只重算稀疏的一组 token。选择时合并动作专家的交叉注意力与视觉潜表示的意外变化：前者提示动作依赖哪里，后者提示哪里出现新信息。再加入严格年龄上限，防止缓存长期不更新而累积误差。它无需重新训练，在推理期间管理缓存；选择规则、刷新比例和年龄阈值未说明。

### 方法如何工作

1. 保存上一动作块的各层 KV，为下一轮提供可复用的视觉表示。
2. 结合动作专家注意力与视觉意外变化选出刷新位置，将计算分配给行动依赖和新出现的信息。
3. 把超过年龄上限的位置加入刷新集合，避免误差跨轮积累。
4. 重算选中位置并复用其余 KV，供动作专家预测下一段动作；稀疏计算实现细节未说明。

### 必要术语

- KV 缓存：注意力机制读取的键和值表示；本文跨控制轮次复用它们。
- 预填充：先把观察计算成供动作专家读取的表示；它是本文要减少的主要计算。
- 交叉注意力：动作专家选择读取视觉信息的权重；本文用它帮助确定刷新位置。
- 缓存年龄：某份表示距上次更新经过的轮数；本文限制它以抑制陈旧误差。

## 证据

摘要报告，在 Fast-WAM 上，跨 RoboTwin 2.0、LIBERO 和现实实验，视频 DiT 预填充 FLOPs 减少 32%—42%。仿真策略表现与完整计算基线相差 0.7—1.8 个百分点，真机相差 2.5 个百分点；摘要未写明该百分点指标名称及完整分项。结果支持特定模型上的计算量与表现折中，不能把局部 FLOPs 降幅直接当作整机控制速度提升。

## 局限

摘要明确报告了只依赖视觉或 KV 漂移的局限，但没有证明注意力就是信息重要性的因果度量。我会核查接触瞬间和场景突变时的误差，以及获取刷新信号本身的成本。真机结果只支持提供的实验范围。

- **判断**：值得读到刷新规则和实际延迟实验，因为它提供了明确的加速机制，但部署收益还取决于硬件与缓存管理开销。

## 研究关联

它改变了缓存更新的判断标准：画面里变化最大的区域，未必是动作最需要的信息。若下游任务会选择性读取上游表示，更新预算可以优先分给这些依赖位置，再用新信息与时间限制补足遗漏。

### 下一步读哪里

核查注意力信号来自哪一轮、稀疏重算如何保持各层一致，以及年龄限制怎样设定。重点看端到端延迟、显存开销和突然运动场景，再确认百分点对应的指标及各任务结果。

- **概念**：世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/WAM-Cache Staleness-Bounded KV Reuse for Efficient World Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) enable generalist robot manipulation by conditioning an action expert on representations from a pretrained video Diffusion Transformer (DiT). In closed-loop control, the video DiT runs at every chunk to encode the current observation into layerwise key-value (KV) pairs that the action expert queries. This prefill dominates the per-chunk computational cost, yet existing training-free accelerations leave it fully dense. We present WAM-Cache, a training-free framework that retains layerwise key-value representations across chunks and recomputes only a sparse refresh set of tokens. Crucially, we find that the intuitive heuristic of refreshing visually drifted tokens plateaus far below the dense baseline, even with an oracle predicting ground-truth KV drift. Downstream action accuracy is instead governed by where the action expert attends, not by what moved. WAM-Cache therefore selects the refresh set by uniting the action expert's cross-attention with visual latent surprise, complemented by a strict age bound that suppresses compounding error. On Fast-WAM, WAM-Cache cuts video DiT prefill FLOPs by 32-42% across RoboTwin 2.0, LIBERO, and real-world experiments, while staying within 0.7-1.8 percentage points of the dense policy in simulation and 2.5 points on a real robot.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.11401v1
- Authors: Kai Ding, Yang He, Ruijie Quan, Yi Yang
- Published: 2026-10-08T07:33:59Z
- Age days: 1

</details>
