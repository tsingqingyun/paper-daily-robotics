---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04030v1"
published: "2026-09-03T16:08:57Z"
age_days: 3
score: 24
created: 2026-09-07
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# IRWOZ 2.0: A Large Language Model-driven Dialogue Dataset for Industrial Robot Conversations

> [!summary] 先说人话（基于摘要）
> IRWOZ 2.0 用Mistral和Claude-3.5辅助生成，再经人工修正与自动去错，清理并扩充工业机器人对话数据，重点改善对话状态跟踪。

## 问题

原IRWOZ的对话状态和话语含有大量噪声，限制工业HRI系统的状态跟踪准确性。

## 创新点或方法

数据集通过LLM增强生成、人工纠正和自动拼写错误清理，扩展为装配、配送、定位和搬运四个工业领域的390段对话；输出是可用于工业对话状态跟踪的新版语料。

## 证据

IRWOZ 2.0含390段对话和4个领域。基准中GPT-2的BLEU-4由原数据上的0.1651提升到0.5604；数据集已公开。


## 局限

BLEU-4是否足以代表对话状态跟踪质量值得核查，还需确认新旧数据比较是否控制了训练规模及人工修正带来的信息变化。

- **判断**：工业HRI对话研究者可深入看标注规范；其他机器人学习读者了解数据资源即可。

## 研究关联

对工业人机交互和语言控制接口研究者，它提供了更干净的领域数据；对视觉动作策略和世界模型的直接价值有限。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/IRWOZ 2.0 A Large Language Model-driven Dialogue Dataset for Industrial Robot Co.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

IRWOZ has improved industrial human-robot interaction (HRI) dialogue systems through domain-specific annotations. However, its initial version contains substantial noise in dialogue states and utterances, limiting state-tracking accuracy. We introduce IRWOZ 2.0, which addresses these limitations through large language model (LLM) enhanced generation (Mistral/Claude-3.5) and quality refinements. Our improved dataset expands to 390 dialogues across 4 industrial domains (Assembly, Delivery, Position, Relocation), featuring manual corrections and automated typo removal. Benchmark experiments on dialogue state tracking demonstrate significant improvements, with GPT-2's BLEU-4 score increasing from 0.1651 to 0.5604 compared to original IRWOZ. To support industrial HRI research, we publicly released IRWOZ 2.0 dataset at https://ieee-dataport.org/documents/irwoz-20-large-language-model-driven-dialogue-dataset-industrial-robot-conversations

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04030v1
- Authors: Chen Li, Dimitrios Chrysostomou
- Published: 2026-09-03T16:08:57Z
- Age days: 3

</details>
