---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10862v1"
published: "2026-06-09T13:39:49Z"
age_days: 0
score: 32
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination

> [!summary] 一句话结论（基于摘要）
> Experiments show that state-of-the-art VLAs suffer substantial performance degradation under occlusion.

## 关键点

- **问题**：This assumption often fails in realistic settings, where occlusion makes manipulation partially observable.
- **创新点 / 方法**：To address this issue, we propose \textbf{Viewpoint Imagination (VIM)}, which generates a complementary view from an occluded primary observation and conditions action prediction on both observed and imagined evidence.
- **证据**：Experiments show that state-of-the-art VLAs suffer substantial performance degradation under occlusion.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models achieve strong performance on standard manipulation
benchmarks, but most evaluations assume that task-relevant objects are fully visible.
This assumption often fails in realistic settings, where occlusion makes manipulation
partially observable. In this paper, we study \textit{scene-induced occlusion} as a
fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-
oriented extension of LIBERO. Experiments show that state-of-the-art VLAs suffer
substantial performance degradation under occlusion. To address this issue, we propose
\textbf{Viewpoint Imagination (VIM)}, which generates a complementary view from an
occluded primary observation and conditions action prediction on both observed and
imagined evidence. VIM improves robustness across task suites, occlusion types, and
severity levels without requiring additional cameras at deployment time, suggesting that
viewpoint imagination is an promising mechanism for perception completion in partially
observable manipulation. Our benchmark and corresponding code are available at:
\href{https://github.com/litsh/Libero-Occ}{https://github.com/litsh/Libero-Occ}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10862v1
- Authors: Taishan Li, Jiwen Zhang, Siyuan Wang, Xuanjing Huang, Zhongyu Wei
- Published: 2026-06-09T13:39:49Z
- Age days: 0

</details>
