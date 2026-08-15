---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12313v1"
published: "2026-08-12T17:58:02Z"
age_days: 2
score: 28
created: 2026-08-15
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# AVA-Encoder: Towards Agent-Native Video Representation Learning

> [!summary] 一句话结论（基于摘要）
> Extensive experiments show that AVA-Encoder improves by 20.7 percentage points over the strongest external baseline.

## 关键点

- **问题**：Creative agents still lack an effective way to learn from high-quality human films, limiting their ability to produce cinematic-grade videos.
- **创新点 / 方法**：To address the challenge, we propose the Agentic Video Auto-Encoder (AVA-Encoder), a framework for learning agent-native video representations via agentic auto-encoding.
- **证据**：Extensive experiments show that AVA-Encoder improves by 20.7 percentage points over the strongest external baseline.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/AVA-Encoder Towards Agent-Native Video Representation Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Creative agents still lack an effective way to learn from high-quality human films, limiting their ability to produce cinematic-grade videos. A key challenge is the absence of a structured video representation that is both faithful to film content and directly usable for agentic reasoning and manipulation. To address the challenge, we propose the Agentic Video Auto-Encoder (AVA-Encoder), a framework for learning agent-native video representations via agentic auto-encoding. AVA-Encoder transforms a video into a knowledge graph (KG) representation and then reconstructs it back into video. Its hierarchy and state nodes store structured text, while a linked asset layer holds generated images, audio, and video. Typed edges preserve the relations between these text descriptions and assets in a form that agents can easily understand, query, and edit. The video reconstruction differences drive a textual-gradient optimization framework, which expresses evaluation feedback as natural-language update directions for Data-Independent Encoding Policy Pseudo-Training in the outer loop and optional Data-Dependent KG Representation Refinement in the test-time inner loop. Extensive experiments show that AVA-Encoder improves by 20.7 percentage points over the strongest external baseline. In the controlled policy-only setting, its pseudo-trained shot-level Agentic Video Encoder policy also outperforms a carefully human-tuned policy while using 74.3% fewer system-prompt tokens. We release the complete AVA-Encoder framework, a reliable agentic video reconstruction benchmark, and the first dataset of high-quality film KG representations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12313v1
- Authors: Chuyue Li, Jinpeng Yu, Haozhe Wang, Tian Xueyun, Zhijing Zhang, Bingnan Li, Shuqi Gu, Kan Ren, Jiaming Liu, Ruihua Hua
- Published: 2026-08-12T17:58:02Z
- Age days: 2

</details>
