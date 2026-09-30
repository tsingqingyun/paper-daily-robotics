---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2504.13700"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-09-13
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Exploring Multimodal Prompt for Visualization Authoring with Large Language Models

> [!summary] 先说人话（基于摘要）
> VisPilot让用户同时用文字、草图和直接修改图表来表达可视化需求，减少纯语言难以说明位置和局部对象的问题。

## 问题

可视化创作中的空间约束、局部引用和设计偏好难以用自然语言精确表达，模型容易误解含糊或不完整的指令，增加反复修改。

## 创新点或方法

先研究模型如何解释歧义文本，再将视觉提示加入创作界面；用户通过文字、草图及对已有图表的直接操作提供意图，系统据此辅助生成和修改可视化。

## 证据

受控用户研究与专家评价表明，多模态提示有助于表达空间约束、局部引用和设计偏好，任务效率与纯文本提示相当；摘要未给出可核查的结果数字。


## 局限

需核查样本规模、意图表达改善的测量方式和模型设置；效率相当并不支持效率提升的结论。

- **判断**：关注多模态人机接口可读用户研究，具身算法研究者略读设计启示即可。

## 研究关联

对多模态交互研究者有接口设计价值，可启发更精确的意图表达；它不是具身智能基准，对机器人学习没有直接实验证据。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/Exploring Multimodal Prompt for Visualization Authoring with Large Language Mode.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2504.13700v2 Announce Type: replace-cross Abstract: Recent advances in large language models (LLMs) have shown great potential in automating the process of visualization authoring through simple natural language utterances. However, instructing LLMs using natural language is limited in precision and expressiveness for conveying visualization intent, leading to misinterpretation and time-consuming iterations. To address these limitations, we conduct an empirical study to understand how LLMs interpret ambiguous or incomplete text prompts in the context of visualization authoring, and the conditions making LLMs misinterpret user intent. Informed by the findings, we introduce visual prompts as a complementary input modality to text prompts, which help clarify user intent and improve LLMs' interpretation abilities. To explore the potential of multimodal prompting in visualization authoring, we design VisPilot, which enables users to easily create visualizations using multimodal prompts, including text, sketches, and direct manipulations on existing visualizations. We evaluate VisPilot through a controlled user study and an expert evaluation. The results suggest that multimodal prompts facilitate users in communicating spatial constraints, local references, and design preferences while maintaining comparable task efficiency to text-only prompting. We further discuss when text, visual, and hybrid prompts are beneficial for visualization authoring, and summarize design implications for future human-AI authoring systems. All materials are available at https://osf.io/2qrak.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2504.13700
- Authors: Zhen Wen, Luoxuan Weng, Yinghao Tang, Runjin Zhang, Yuxin Liu, Bo Pan, Minfeng Zhu, Wei Chen
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
