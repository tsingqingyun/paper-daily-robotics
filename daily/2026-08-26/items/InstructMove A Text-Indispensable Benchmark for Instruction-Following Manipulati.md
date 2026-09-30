---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.22990v1"
published: "2026-08-24T08:53:41Z"
age_days: 1
score: 43
created: 2026-08-26
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# InstructMove: A Text-Indispensable Benchmark for Instruction-Following Manipulation

> [!summary] 一句话结论（基于摘要）
> We introduce InstructMove, a text-indispensable benchmark for instruction-following manipulation.

## 问题

Vision-language-action (VLA) models have made general-purpose robot manipulation increasingly plausible by conditioning robot actions on natural-language instructions.

## 创新点或方法

We introduce InstructMove, a text-indispensable benchmark for instruction-following manipulation.

## 证据

摘要未报告明确实验结论；需阅读全文核查。

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/InstructMove A Text-Indispensable Benchmark for Instruction-Following Manipulati.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have made general-purpose robot manipulation increasingly plausible by conditioning robot actions on natural-language instructions. A key test of such generality is whether policies actually follow language instructions. Yet many manipulation benchmarks leave this ability underdetermined: the intended object or destination is often visually salient or uniquely feasible, allowing policies to succeed without grounding the instruction. We argue that instruction-following evaluation should be text-indispensable: multiple actions should be visually and physically plausible, while only one should be consistent with the language instruction. We introduce InstructMove, a text-indispensable benchmark for instruction-following manipulation. InstructMove instantiates this principle in pick-and-place scenes with semantic distractors, decomposing instruction following into category identification, attribute discrimination, spatial reasoning, and compositional pick-and-place. InstructMove supports a train-eval protocol with InstructMove training data and held-out evaluation tasks, with additional diagnostics for language dependence. Experiments with representative VLA policies show that InstructMove provides a controlled testbed for diagnosing visual shortcuts and that InstructMove simulation data can improve real-world instruction-following manipulation performance. Code: https://github.com/HorizonRobotics/RoboOrchardSim

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.22990v1
- Authors: Mengao Zhao, Ziang Li, Chaodong Huang, Mengchen Ma, Haoyi Jiang, Yiwei Jin, Xinjie Wang, Yun Du, Xuewu Lin, Taojun Ding, Hongyu Xie, Jackson Jiang, Chunlei Yu, Kaihua Zhang, Lichao Huang, Liu Liu, Tianwei Lin, Zhizhong Su
- Published: 2026-08-24T08:53:41Z
- Age days: 1

</details>
