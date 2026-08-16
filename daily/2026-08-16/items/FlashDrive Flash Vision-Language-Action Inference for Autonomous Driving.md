---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12932v1"
published: "2026-08-13T08:10:54Z"
age_days: 3
score: 24
created: 2026-08-16
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving

> [!summary] 一句话结论（基于摘要）
> Applied to Alpamayo 1.5-10B with W4A8 quantization, FlashDrive reduces end-to-end latency from 717ms to 151ms (4.7x) while leaving accuracy essentially unchanged: minADE6@6.4s shifts by only 0.08m, minADE1 improves, and closed-loop collision and off-road rate…

## 关键点

- **问题**：Vision-Language-Action (VLA) models promise to bring end-to-end reasoning to autonomous driving, but their computational cost remains far too high for real-time control.
- **创新点 / 方法**：We propose FlashDrive, an algorithm-system co-design framework that targets all four stages simultaneously.
- **证据**：Applied to Alpamayo 1.5-10B with W4A8 quantization, FlashDrive reduces end-to-end latency from 717ms to 151ms (4.7x) while leaving accuracy essentially unchanged: minADE6@6.4s shifts by only 0.08m, minADE1 improves, and closed-loop collision and off-road rates improve in simulation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/FlashDrive Flash Vision-Language-Action Inference for Autonomous Driving.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models promise to bring end-to-end reasoning to autonomous driving, but their computational cost remains far too high for real-time control. The core challenge is structural: VLA inference is not a single bottleneck but a cascade of four. Visual encoding wastes compute on overlapping video frames; language-model prefill recomputes context that could be carried over from the previous timestep; reasoning tokens are generated serially despite low entropy; and flow-matching denoising applies uniform compute to a non-uniform velocity field. Addressing any one stage in isolation leaves the others untouched. We propose FlashDrive, an algorithm-system co-design framework that targets all four stages simultaneously. Our key insight is that each bottleneck admits a distinct, lightweight algorithmic shortcut: temporal overlap enables streaming KV-cache reuse across frames; the low per-token entropy and strong intra-block correlations of driving-domain reasoning make a non-autoregressive diffusion drafter highly effective for speculative decoding; and the velocity field's structure---sharp at the endpoints, flat in the middle---permits adaptive step caching that concentrates compute where it matters. Layered on system-level CUDA Graph compilation and kernel fusion, these techniques compound. Applied to Alpamayo 1.5-10B with W4A8 quantization, FlashDrive reduces end-to-end latency from 717ms to 151ms (4.7x) while leaving accuracy essentially unchanged: minADE6@6.4s shifts by only 0.08m, minADE1 improves, and closed-loop collision and off-road rates improve in simulation. By raising a 10B-parameter reasoning VLA from 1.4~Hz to 6.6~Hz on a single GPU, FlashDrive moves end-to-end autonomous driving substantially closer to real-time deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12932v1
- Authors: Zekai Li, Yihao Liang, Hongfei Zhang, Jian Chen, Yesheng Liang, Zhijian Liu
- Published: 2026-08-13T08:10:54Z
- Age days: 3

</details>
