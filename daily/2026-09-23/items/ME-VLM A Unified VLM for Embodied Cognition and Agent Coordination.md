---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24526v1"
published: "2026-09-21T12:59:59Z"
age_days: 1
score: 33
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# ME-VLM:A Unified VLM for Embodied Cognition and Agent Coordination

> [!summary] 先说人话（基于摘要）
> ME-VLM希望把物理场景理解、规划和数字Agent能力装进同一个视觉语言模型。它先分别强化两类专家，再通过多教师蒸馏合并能力，并优化小版本的端侧推理。

## 问题

物理环境中的决策不仅需要识别图像和语言，还要考虑环境约束与执行反馈；摘要将这些能力的统一作为目标，但未明确诊断已有方案的具体失败机制。

## 创新点或方法

提供4B和35B-A3B版本，训练数据包含执行观察与反馈；经过具身能力注入、具身与多模态Agent专家分别RL训练，再做多教师在线策略蒸馏。端侧采用视觉token压缩、W4A8量化及软硬件协同优化。

## 证据

摘要称在具身、Agent、自动驾驶和导航任务上具有竞争力，但未给准确率数字。4B版本在M100上的预填充延迟从400毫秒降至188毫秒。

## 局限

预填充延迟不等于完整决策延迟；能力整合是否优于单独专家，需要全文基准和对照结果支持。

- **判断**：先读训练流程和评测表，现有摘要不足以判断其具身能力优势。

## 研究关联

对多模态基础模型和Agent研究，价值在于专家能力合并及端侧部署；摘要没有证明它能直接产生机器人动作。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/ME-VLM A Unified VLM for Embodied Cognition and Agent Coordination.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physical AI requires models to ground visual and linguistic understanding in real-world environments while accounting for environmental constraints and execution feedback. We introduce MachEmbodied-VLM (ME-VLM), a unified vision-language model with two variants, 4B and 35B-A3B, that brings together embodied cognition and multimodal agent capabilities. Our work emphasizes physical perception and spatiotemporal reasoning, together with planning, interaction, and outcome assessment in both digital and physical environments. We construct training data spanning embodied and multimodal agent tasks, including execution observations and feedback to support outcome assessment and decision refinement. The training pipeline comprises embodied capability injection, separate reinforcement learning of embodied and multimodal-agent experts, and multi-teacher on-policy distillation that consolidates their complementary capabilities into a single model. Experiments show competitive performance on both embodied and agent benchmarks, as well as on autonomous-driving and embodied-navigation tasks. For edge deployment, visual token compression, W4A8 quantization, and hardware--software co-optimization enable on-device inference of the 4B variant on the M100, reducing prefill latency from 400 ms to 188 ms. Project Page: https://machembodied.com/ME-Brain/ME-VLM.html Code Repository: https://github.com/MachEmbodied/ME-VLM

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24526v1
- Authors: Foundation Model, Li Auto Inc
- Published: 2026-09-21T12:59:59Z
- Age days: 1

</details>
