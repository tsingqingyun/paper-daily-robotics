---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13778v1"
published: "2026-05-13T16:57:51Z"
age_days: 0
score: 31
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs

> [!summary] 一句话结论（基于摘要）
> Experiments show that on LIBERO, FLASH largely preserves task performance by replacing many 58.0 ms full-inference rounds with speculative rounds as fast as 7.8 ms, lowering task-level average inference latency to 19.1 ms (3.04x speedup).

## 关键点

- **问题**：Diffusion-based vision-language-action models (dVLAs) are promising for embodied intelligence but are fundamentally limited in real-time deployment by the high latency of full inference.
- **创新点 / 方法**：We propose Realtime-VLA FLASH, a speculative inference framework that eliminates most full inference calls during replanning by introducing a lightweight draft model with parallel verification via the main model's Action Expert and a phase- aware fallback mechanism that reverts to the full inference pipeline when need…
- **证据**：Experiments show that on LIBERO, FLASH largely preserves task performance by replacing many 58.0 ms full-inference rounds with speculative rounds as fast as 7.8 ms, lowering task-level average inference latency to 19.1 ms (3.04x speedup).
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/Realtime-VLA FLASH Speculative Inference Framework for Diffusion-based VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Diffusion-based vision-language-action models (dVLAs) are promising for embodied
intelligence but are fundamentally limited in real-time deployment by the high latency
of full inference. We propose Realtime-VLA FLASH, a speculative inference framework that
eliminates most full inference calls during replanning by introducing a lightweight
draft model with parallel verification via the main model's Action Expert and a phase-
aware fallback mechanism that reverts to the full inference pipeline when needed. This
design enables low-latency, high-frequency replanning without sacrificing reliability.
Experiments show that on LIBERO, FLASH largely preserves task performance by replacing
many 58.0 ms full-inference rounds with speculative rounds as fast as 7.8 ms, lowering
task-level average inference latency to 19.1 ms (3.04x speedup). We additionally
demonstrate effectiveness on real-world conveyor-belt sorting, highlighting its
practical impact for latency-critical embodied tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13778v1
- Authors: Jiahui Niu, Kefan Gu, Yucheng Zhao, Shengwen Liang, Tiancai Wang, Xing Hu, Ying Wang, Huawei Li
- Published: 2026-05-13T16:57:51Z
- Age days: 0

</details>
