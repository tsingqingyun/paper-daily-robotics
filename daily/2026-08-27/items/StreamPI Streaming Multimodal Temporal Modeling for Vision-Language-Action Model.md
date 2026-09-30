---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26067v1"
published: "2026-08-26T17:33:19Z"
age_days: 0
score: 38
created: 2026-08-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> StreamPI 在不增加参数的情况下，把单帧 VLA 改成流式时序模型：帧内视觉—语言双向融合，跨帧因果注意力，并始终以指令作为语义锚点。

## 问题

π0.5等单帧VLA不能保留历史观测，记忆与精细空间判断受限；同步训练和真实机器人异步取帧之间还存在部署落差。

## 创新点或方法

每个“视觉观测—指令”对作为时间单元，单元内双向注意、单元间因果注意；随机间隔流式训练覆盖不同取帧节奏，并利用LLM骨干的长度外推继承单帧权重，支持单帧或多帧推理。

## 证据

摘要称在记忆依赖、精细感知真机任务及LIBERO上均超过π0.5，但未给出可核查的结果数字；仅举例每3帧取一次可获得更快、更平滑执行。


## 局限

“零新增参数”不等于零新增计算；长上下文的显存、延迟和长度外推稳定性在摘要中没有量化。

- **判断**：值得读注意力掩码与部署实现，但在缺少定量成功率和延迟数据前，不宜接受其效率优势。

## 研究关联

它是把时序记忆加入现有VLA的低改造成本方案，也直接触及机器人异步传感和控制节奏这一常见部署问题。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/StreamPI Streaming Multimodal Temporal Modeling for Vision-Language-Action Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored temporal modeling. It treats each (visual observation, language instruction) pair as an atomic temporal unit: bidirectional attention within each pair enables cross-modal fusion, while causal attention across pairs preserves autoregressive streaming inference. This ensures the language instruction serves as a persistent semantic anchor throughout task execution. To bridge the gap between synchronous training and asynchronous real-robot deployment, we introduce a andom-interval streaming training strategy: a proper inter-frame interval (e.g., every 3 frames) enables faster and smoother action execution. Beyond this, randomizing the interval further improves robustness to frame-timing perturbations, supporting asynchronous deployment in practice. Furthermore, by leveraging the length extrapolation capability of the LLM backbone, StreamPI seamlessly inherits pretrained single-frame weights and supports flexible single-frame and multi-frame inference. Experiments on real-robot tasks spanning memory-dependent and precise perception scenarios, as well as the simulation benchmark LIBERO, demonstrate that StreamPI outperforms pi0.5 across diverse tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26067v1
- Authors: Zhe Liu, Jinghua Hou, Yuxiang Lu, Zhenya Yang, Xianzhe Fan, Junwei Luo, Junyi Li, Ruihua Han, Zhi Hou, Hengshuang Zhao
- Published: 2026-08-26T17:33:19Z
- Age days: 0

</details>
