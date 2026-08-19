---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17600v1"
published: "2026-08-18T10:07:17Z"
age_days: 0
score: 33
created: 2026-08-19
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> To address these gaps, we introduce LIBERO-VIFO, a benchmark to evaluate both the capability and safety of visual cue following in VLA models.

## 关键点

- **问题**：Visual cues are increasingly adopted to guide robot learning, but whether Vision-Language-Action (VLA) models can reliably follow authorized cues while disregarding unauthorized ones remains unclear.
- **创新点 / 方法**：To address these gaps, we introduce LIBERO-VIFO, a benchmark to evaluate both the capability and safety of visual cue following in VLA models.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Evaluating seven VLA models reveals that although visual cue understanding does not reliably translate into execution, current VLAs are able to execute cue-indicated tasks without language instruction, exposing an emerging risk of unauthorized visual cue following.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/LIBERO-VIFO Benchmarking the Capability and Safety of Visual Cue Following in Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual cues are increasingly adopted to guide robot learning, but whether Vision-Language-Action (VLA) models can reliably follow authorized cues while disregarding unauthorized ones remains unclear. Existing work covers only a narrow range of cue forms and focuses on final task success, providing only a coarse assessment of cue-following capability. Treating all visual cues as authorized also leaves safety risks of unauthorized following unexplored. To address these gaps, we introduce LIBERO-VIFO, a benchmark to evaluate both the capability and safety of visual cue following in VLA models. LIBERO-VIFO defines eight visual cue families spanning diverse forms. A total of four protocols in two parts are defined: Part I tests cue understanding and authorized following, while Part II evaluates unauthorized visual cue following under language-cue conflict and empty language conditions. Evaluating seven VLA models reveals that although visual cue understanding does not reliably translate into execution, current VLAs are able to execute cue-indicated tasks without language instruction, exposing an emerging risk of unauthorized visual cue following. Extended experiments on scene-instantiated cues, safety-critical settings, and real-robot deployment corroborate these findings. LIBERO-VIFO brings both the capability and safety of visual cue following into systematic evaluation, establishing visual-centric safety as a new perspective for the VLA community.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17600v1
- Authors: Zhengyan Qian, Rui Yan, Alex Jinpeng Wang, Jinhui Tang
- Published: 2026-08-18T10:07:17Z
- Age days: 0

</details>
