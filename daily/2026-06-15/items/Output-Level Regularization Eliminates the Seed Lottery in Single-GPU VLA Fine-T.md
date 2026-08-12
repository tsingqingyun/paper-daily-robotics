---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13856v1"
published: "2026-06-11T19:33:11Z"
age_days: 3
score: 32
created: 2026-06-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning

> [!summary] 一句话结论（基于摘要）
> There is a hidden danger.

## 关键点

- **问题**：Fine-tuning a vision-language-action model (VLA-JEPA) on a single GPU should be simple: load a pretrained checkpoint, run training, deploy.
- **创新点 / 方法**：There is a hidden danger.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Fine-tuning a vision-language-action model (VLA-JEPA) on a single GPU should be simple:
load a pretrained checkpoint, run training, deploy. There is a hidden danger. Run the
same fine-tuning code thirteen times -- same data, same architecture, different random
seed -- and twelve runs produce a robot succeeding 91--94% of the time, while one run
silently degrades to 65.2%: a 29 pp gap with no error message, no warning, and no way to
predict which seed will fail. We call this the seed lottery. We trace the cause to
output collapse: the action predictor quietly learns to produce nearly identical outputs
regardless of what the robot sees. Existing weight-level methods (L2, EWC) are
structurally blind to this collapse -- they penalize weight changes, but collapse occurs
in directions weights can move freely without affecting outputs, a gap we formalize via
the Jacobian null-space. Across 7 methods x up to 13 seeds x 3 LIBERO benchmarks, three
output-level regularizers -- VICReg (n=12 seeds), Dropout (n=4), and a halved learning
rate (n=5) -- each eliminate every catastrophic seed (0/21 combined collapses vs. 1/13
Baseline; F(12,11)=28.7, p<0.001), while weight-level methods (L2, EWC) preserve the
lottery. The simplest fix is changing one number in your optimizer config.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13856v1
- Authors: Jeffrin Sam, Dzmitry Tsetserukou
- Published: 2026-06-11T19:33:11Z
- Age days: 3

</details>
