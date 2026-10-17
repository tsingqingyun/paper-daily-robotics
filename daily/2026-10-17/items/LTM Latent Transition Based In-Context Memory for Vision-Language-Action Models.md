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
url: "https://arxiv.org/abs/2610.21362v1"
published: "2026-10-15T06:41:20Z"
age_days: 1
score: 31
created: 2026-10-17
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> Latent Transition Memory（LTM）让 VLA 记住“刚才发生了什么变化”，而不只是保留历史画面。它把连续观察间的变化编码成紧凑记忆，接到 π₀.₅ 上，并用缓存支持逐步推理。

## 问题

操作有时需要记住已经离开视野的互动，例如此前交换过什么、做过几次。只依靠当前观察无法恢复这些过程，而历史又必须装进有限上下文。摘要未展开既有记忆方法的具体缺陷，只说明本文不需要记忆专用语义标注或外部推理模型调用。

### 用一个例子理解

理解用例（非论文实验）：机器人先后把三个零件放入盒子，随后盒子移出视野；LTM 将每次放入造成的观察变化写成记忆，之后结合“已经放了几个”的要求与当前观察，输出继续拿取或停止的动作。

## 创新点或方法

相较于保留历史观察，LTM 保存相邻观察间的潜在转移。训练使用冻结的潜在动作编码器和轻量适配器，具体损失与策略更新范围未说明。推理随新观察增量形成记忆，并用因果 KV 缓存减少重复计算；延迟接纳记忆也有消融支持，但何时接纳的规则摘要未说明。紧凑转移能否保住任务所需细节，是方法成立的关键。

### 方法如何工作

1. 把相邻观察送入冻结编码器，提取两次观察之间的变化，作为待保存的历史内容。
2. 用轻量适配器把转移接入 VLA，使当前决策能够利用过去互动。
3. 按记忆接纳机制增量加入历史，并用因果 KV 缓存复用已有计算；接纳条件摘要只说明到此。
4. 在有限上下文中结合记忆与当前观察输出动作，通过压缩实验检查信息减少后的控制表现。

### 必要术语

- 潜在转移：用紧凑向量表示相邻观察的变化；是 LTM 保存的记忆单位。
- 冻结编码器：训练时不更新参数的编码模块；本文用它产生潜在转移。
- 因果 KV 缓存：保存历史注意力计算中的键和值；支持逐步加入信息时复用计算。
- 过程监督：对中间过程提供学习信号；摘要中的诊断用它考察时间组合能力。

## 证据

摘要报告，使用 DreamDojo 转移的 LTM-π 在 RoboMME、LIBERO-Mem 成功率为 58.54%、80.5%，在不使用外部推理模型或记忆专用标注的基线中最好。另一扩量设置把 RoboMME 示范增至十倍，成功率由 57.67% 到 87.50%，不应与前述 58.54% 混为同一条件。200 token 预算下为 84.00%，未压缩为 87.50%；真机计数从 11.25% 到 82.50%。均未给试验次数。

## 局限

摘要的消融支持转移内容具有超出时间提示的作用，但不等于任意事件细节都被保留。我的待核查问题是基准运行环境、编码器遗漏的细微变化，以及计数提升适用于哪些物体和干扰条件；不能把基准成绩都称为真机验证。

- **判断**：值得细读记忆接纳、压缩和 Cup Swap 诊断：它们决定这套方法何时真正记住了过程，以及何时仍依赖额外监督。

## 研究关联

可借鉴的是围绕状态变化组织历史：如果任务关心交换、拿放、次数，转移可能比重复画面更节省上下文。但记忆表示仍需和过程监督配合；摘要中的 Cup Swap 诊断提示，仅压缩历史并不自动解决时间顺序组合。

### 下一步读哪里

先核查转移编码是否包含足够的顺序信息，再看延迟接纳与 200 token 压缩规则；实验应分清不同示范规模的设置，并检查 Cup Swap 的过程监督具体提供了什么。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/LTM Latent Transition Based In-Context Memory for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation often requires remembering interactions that are no longer visible. We introduce Latent Transition Memory (LTM), which stores history as compact latent transitions between consecutive observations. Instantiated on $π_{0.5}$ as LTM-$π$, our method uses a frozen latent action encoder, a lightweight adapter, and causal KV caching for incremental inference without memory-specific semantic annotations or external reasoning-model calls. With DreamDojo transitions, LTM-$π$ achieves 58.54% success on RoboMME and 80.5% on LIBERO-Mem, performing best among baselines without external reasoning models or memory-specific annotations. Ablations support the contribution of transition content beyond temporal cues and the efficiency of delayed memory admission. Scaling RoboMME demonstrations tenfold improves success from 57.67% to 87.50%, while a Cup Swap diagnostic highlights the role of process supervision in temporal composition. Under a 200-token memory budget, success remains 84.00%, versus 87.50% without compression. Finally, real-robot counting success improves from 11.25% to 82.50%. Together, these results demonstrate the effectiveness, scalability, and efficiency of latent transition memory, highlighting its capacity for complex temporal information, bounded-context operation, and real-world robotic control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21362v1
- Authors: Qixin Sun, WenLong Gao, Xiansheng Chen, Zhongyuan Wang, Si Liu, Pengwei Wang
- Published: 2026-10-15T06:41:20Z
- Age days: 1

</details>
