---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12515v1"
published: "2026-08-12T18:47:43Z"
age_days: 3
score: 24
created: 2026-08-16
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?

> [!summary] 一句话结论（基于摘要）
> However, \textit{Qwen-VL} with an advanced prompt achieves substantially higher recall for high-danger cases than the other models.

## 关键点

- **问题**：However, \textit{Qwen-VL} with an advanced prompt achieves substantially higher recall for high-danger cases than the other models.
- **创新点 / 方法**：Assessing proxemic danger from a robot's egocentric perspective is critical for safe embodied navigation in human environments and requires both visual and contextual reasoning.
- **证据**：However, \textit{Qwen-VL} with an advanced prompt achieves substantially higher recall for high-danger cases than the other models.
- **局限**：An analysis of person localization further shows that correct danger classification does not correspond to better spatial grounding, indicating that a model may produce a useful safety label without attending to the relevant region of the scene.

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Assessing proxemic danger from a robot's egocentric perspective is critical for safe embodied navigation in human environments and requires both visual and contextual reasoning. We evaluate three opensource vision-language models (VLMs) (\textit{InternVL}, \textit{Qwen-VL}, and \textit{SmolVLM}) on the classification of egocentric robot images into four danger levels, comparing three prompting strategies and two rounds of QLoRA fine-tuning against a stratified random baseline. Without fine-tuning, all models perform near the baseline, while fine-tuning yields only modest overall improvements. However, \textit{Qwen-VL} with an advanced prompt achieves substantially higher recall for high-danger cases than the other models. An analysis of person localization further shows that correct danger classification does not correspond to better spatial grounding, indicating that a model may produce a useful safety label without attending to the relevant region of the scene. These results show that current VLMs remain limited in fine-grained proxemic reasoning and spatial grounding, although targeted prompting and fine-tuning can improve high-danger detection in selected models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12515v1
- Authors: Vladyslava Rudas, Dmytro Kuzmenko
- Published: 2026-08-12T18:47:43Z
- Age days: 3

</details>
