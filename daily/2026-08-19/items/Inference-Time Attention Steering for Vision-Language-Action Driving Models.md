---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17095v1"
published: "2026-08-17T20:03:38Z"
age_days: 1
score: 34
created: 2026-08-19
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Inference-Time Attention Steering for Vision-Language-Action Driving Models

> [!summary] 一句话结论（基于摘要）
> We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone.

## 关键点

- **问题**：Vision-language-action (VLA) driving models couple a reasoning stage with a diffusion-based trajectory decoder, but do not give a direct way to redirect attention toward safety-critical actors at inference time without retraining.
- **创新点 / 方法**：We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Inference-Time Attention Steering for Vision-Language-Action Driving Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) driving models couple a reasoning stage with a diffusion-based trajectory decoder, but do not give a direct way to redirect attention toward safety-critical actors at inference time without retraining. We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone. It is applied as a fail open forward pre-hook with no weight changes. On 50 lane-change scenarios from the Physical AI World Model Synthetic dataset. The trajectory decoder shows a monotonic dose response in the bias magnitude, separate from a paired zero bias control at every tested magnitude. It reaches $\approx 17$\,cm mean displacement with lateral shifts up to $\sim 140$\ cm at the clamp. A layer ablation places the action-relevant signal in late layers, where the effect increases with the number of hooked layers (2.0cm for the first 8 layers; 67.6cm for all 36). A per call injection audit explains why the Chain-of-Causation text never changes. The mask based bias never reaches the reasoning pathway in this serving stack, so the invariance is verified exposure, not robustness. Steered trajectories tend to shift toward the attended actor, suggesting the bias governs where the model looks rather than encoding a target behavior.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17095v1
- Authors: Darshan Nagendra Prasad, Lars Ullrich, Knut Graichen
- Published: 2026-08-17T20:03:38Z
- Age days: 1

</details>
