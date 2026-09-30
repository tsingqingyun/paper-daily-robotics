---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04030"
published: "Sat, 05 Sep 2026 00:00:00 -0400"
age_days: 0
score: 24
created: 2026-09-06
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# IRWOZ 2.0: A Large Language Model-driven Dialogue Dataset for Industrial Robot Conversations

> [!summary] 先说人话（基于摘要）
> IRWOZ 2.0 用 Mistral/Claude-3.5 辅助生成并结合人工修正、自动去错，清理和扩充工业机器人对话数据，以提升对话状态跟踪。

## 这篇到底在做什么

- **卡在哪里**：任务是工业人机对话中的状态跟踪；原始 IRWOZ 的对话状态和话语含有大量噪声，直接限制模型准确理解当前任务状态。
- **关键解法**：数据集覆盖装配、配送、定位和搬迁四个工业域，共 390 段对话。它以 LLM 增强生成扩充内容，再用人工纠正和自动拼写清理提高质量；输出是面向工业 HRI 的精炼对话及状态标注，而非新机器人策略。
- **拿什么证明**：GPT-2 的 BLEU-4 从原版 IRWOZ 的 0.1651 提升至 0.5604；摘要称基准实验显示对话状态跟踪显著改善。

## 值不值得读

- **和你的研究有什么关系**：它为具身智能评测补充了工业对话状态数据，可用于测试语言模型能否稳定追踪机器人任务约束；但摘要没有表明其包含视觉输入，因此对“多模态”研究的直接价值有限。
- **先别急着信**：需查全文确认 BLEU-4 的具体预测对象及评测协议，因为 BLEU 并不能单独说明结构化状态是否正确；还需区分数据清理和 LLM 生成各自的贡献。
- **判断**：做工业 HRI 数据或状态跟踪者值得看数据规范和错误分析；若关注端到端具身控制，读摘要和数据卡即可。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-06/IRWOZ 2.0 A Large Language Model-driven Dialogue Dataset for Industrial Robot Co.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04030v1 Announce Type: new Abstract: IRWOZ has improved industrial human-robot interaction (HRI) dialogue systems through domain-specific annotations. However, its initial version contains substantial noise in dialogue states and utterances, limiting state-tracking accuracy. We introduce IRWOZ 2.0, which addresses these limitations through large language model (LLM) enhanced generation (Mistral/Claude-3.5) and quality refinements. Our improved dataset expands to 390 dialogues across 4 industrial domains (Assembly, Delivery, Position, Relocation), featuring manual corrections and automated typo removal. Benchmark experiments on dialogue state tracking demonstrate significant improvements, with GPT-2's BLEU-4 score increasing from 0.1651 to 0.5604 compared to original IRWOZ. To support industrial HRI research, we publicly released IRWOZ 2.0 dataset at https://ieee-dataport.org/documents/irwoz-20-large-language-model-driven-dialogue-dataset-industrial-robot-conversations

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04030
- Authors: Chen Li, Dimitrios Chrysostomou
- Published: Sat, 05 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
