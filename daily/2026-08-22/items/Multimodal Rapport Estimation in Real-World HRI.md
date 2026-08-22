---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18401v1"
published: "2026-08-19T00:15:22Z"
age_days: 3
score: 24
created: 2026-08-22
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Multimodal Rapport Estimation in Real-World HRI

> [!summary] 一句话结论（基于摘要）
> The results show that, in real-world HRI, zero-shot LLMs achieve strong performance, while audio and visual models tend to provide complementary information.

## 关键点

- **问题**：Evaluating interaction quality in real-world HRI is an important challenge.
- **创新点 / 方法**：If interaction quality can be estimated reliably, the results can be used to improve dialogue strategies and ultimately enable robots to adapt their behavior autonomously.
- **证据**：The results show that, in real-world HRI, zero-shot LLMs achieve strong performance, while audio and visual models tend to provide complementary information.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Multimodal Rapport Estimation in Real-World HRI.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Evaluating interaction quality in real-world HRI is an important challenge. If interaction quality can be estimated reliably, the results can be used to improve dialogue strategies and ultimately enable robots to adapt their behavior autonomously. However, existing automatic evaluation methods have been developed primarily in controlled laboratory settings, and it remains unclear whether they can be directly applied to real-world environments, where users are free to disengage and multi-party participation may arise naturally. In this study, we investigate the automatic estimation of third-party-rated rapport scores using 62 sessions of multimodal recordings collected in a Japanese drugstore. We compare zero-shot LLMs, pretrained text, audio, and visual models, and their prediction-level fusion. The results show that, in real-world HRI, zero-shot LLMs achieve strong performance, while audio and visual models tend to provide complementary information. In particular, Gemini 2.5 Flash performs strongly as a single model, and a fusion model combining Gemini (text) with HuBERT and V-JEPA performs best overall. Further analyses showed that estimation performance varied across interaction-duration and group-size conditions. These findings suggest that rapport estimation in real-world HRI requires evaluation and model design that account for contextual variability beyond that assumed in laboratory settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18401v1
- Authors: Akihiro Sakuramoto, Takato Hayashi, Ryo Miyoshi, Yuki Okafuji, Shogo Okada
- Published: 2026-08-19T00:15:22Z
- Age days: 3

</details>
