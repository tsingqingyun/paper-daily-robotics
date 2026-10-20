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
url: "https://arxiv.org/abs/2607.06678"
published: "Mon, 19 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> NativeMEM 把每个相机的每张历史画面压成一个 token，再放进 VLA 输入，让动作决策能直接查看过去。它复用模型自己的视觉编码器，目标是同时保留较长历史和高频更新能力。

## 问题

长程操作可能需要记住已经离开视野的信息，只看当前图像不足以判断下一步。但持续输入大量历史图像会增加计算负担，降低更新速度。摘要指出，依靠外部记忆管理的现有方法，往往限制可保留的历史长度或预训练策略的反应能力；它没有逐项说明各对照方法怎样管理记忆。

### 用一个例子理解

理解用例（非论文实验）：输入是“把刚才看见的红块放进盒子”和当前画面；红块已被遮挡，策略读取此前画面的压缩 token，利用历史信息决定动作，输出抓取与放置指令。此例只说明历史可能怎样帮助决策。

## 创新点或方法

旧做法依赖外部记忆管理；NativeMEM 改用 VLA 自带的视觉编码器，将每个历史帧的每个视角压缩为一个记忆 token，追加到输入序列，让策略通过注意力读取历史。压缩减少历史占用，复用已有编码器则避免另设外部规划器或全新初始化的记忆模块。训练分两阶段：先冻结 VLA，在需要记忆的数据上受其监督训练通用记忆 tokenizer；随后解冻 VLA，做任务微调。推理时持续编码历史并生成动作。摘要未说明压缩操作、历史淘汰规则及监督损失。

### 方法如何工作

1. 收集需要记忆的数据，冻结 VLA 来监督记忆 tokenizer，使压缩表示适配已有策略。
2. 把每张历史画面的每个相机视角编码成一个 token，减少保存和读取历史的输入负担。
3. 解冻 VLA 做任务微调，让策略学习结合当前观测与压缩历史选择动作。
4. 推理时更新历史 token 并追加到输入，让后续动作使用过去信息；历史保留上限摘要未说明。

### 必要术语

- 记忆 token：历史画面的紧凑表示；本文每帧每视角生成一个。
- 记忆 tokenizer：把历史视觉内容转换成 token 的组件；本文先训练它与冻结策略对齐。
- 冻结与解冻：暂停或恢复参数更新；本文用这两阶段分别训练记忆接口和任务策略。

## 证据

摘要报告仿真成功率从 32.4% 提高到 84.0%，真机成功率最高达到 98.7%，并称推理延迟与 GPU 显存使用保持较低；使用 20% 训练数据时，仍能取得与既有方法有竞争力的结果。输入未给出任务名称、机器人配置、对照名称、样本次数或延迟与显存数值。仿真前后数字与真机最高值属于不同表述，不能拼成同一组增幅；20% 数据结果也不能默认等于前述全部成绩。

## 局限

一个 token 能保留哪些细节，是关键待核查问题：细小物体变化、接触过程或短暂事件可能要求不同信息。摘要没有证明这些情况必然失败，也未说明历史不断增长时的处理方式；“低延迟”需要结合历史长度与相机数判断。

- **判断**：值得读到 tokenizer 的监督方式和记忆消融实验：它给出了直接的工程思路，但性能与成本能否同时成立，需要任务和历史规模的细节支撑。

## 研究关联

给策略增加记忆时，值得先检查能否把历史压成模型已有输入体系能使用的表示。训练顺序也值得借鉴：先让压缩表示适配冻结策略，再共同微调，有望减少新记忆接口与原有动作能力之间的不匹配。

### 下一步读哪里

优先核查冻结 VLA 如何监督 tokenizer、单 token 压缩保留什么，以及去掉历史后的对照。再检查仿真与真机任务、20% 数据的具体设置，并查看延迟和显存随历史长度、相机数怎样变化。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-20/NativeMEM Native Memory Compression for Long-Horizon Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2607.06678v2 Announce Type: replace Abstract: How can pretrained Vision-Language-Action (VLA) models retain long-horizon visual histories with high-frequency updates without sacrificing efficiency? Existing approaches rely on external memory management, which restrains either the memory horizon or the reactiveness of pretrained policies. To this end, we present NativeMEM, a VLA policy that features long-term and real-time updated memory. At its core is an efficient memory encoding scheme, Native Memory Compression, which repurposes the VLA's own vision encoder to compress each historical frame from each camera view into a single token. Appended to the input sequence, these memory tokens enable the pretrained VLA to attend over long-term history with negligible latency overhead, requiring neither an external planner nor a freshly initialized memory module. To align the memory tokens with the pretrained policy, we first develop a generic memory tokenizer under the supervision of a frozen VLA on memory-demanding data, and then unfreeze the VLA for task-specific fine-tuning. NativeMEM consistently outperforms prior methods, boosting success rates from 32.4% to 84.0% in simulation and up to 98.7% on real robots, while maintaining low inference latency and GPU memory usage. Notably, NativeMEM exhibits high data efficiency by achieving competitive results with prior arts using only 20% of the training data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.06678
- Authors: Ziye Wang, Modi Shi, Chaojun Ni, Jiazhi Yang, Mengdi Li, Zhizhong Su, Tianwei Lin, Hongyang Li
- Published: Mon, 19 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
