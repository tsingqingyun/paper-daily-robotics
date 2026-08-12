---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24472v1"
published: "2026-06-23T12:02:36Z"
age_days: 1
score: 37
created: 2026-06-25
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> We propose G$^3$VLA, a camera-aware geometric module that injects calibrated structure into the visual-token stream of a pretrained VLA without altering its action space or imitation objective, combining intrinsic-conditioned ray embeddings, projective positi…

## 关键点

- **问题**：Vision-language-action (VLA) models have made rapid progress in generalist robot manipulation by harnessing semantic knowledge from pretrained vision-language backbones, but their visual tokens remain grounded in 2D image coordinates rather than the calibrated geometry of the robot's cameras -- a mismatch especially p…
- **创新点 / 方法**：We propose G$^3$VLA, a camera-aware geometric module that injects calibrated structure into the visual-token stream of a pretrained VLA without altering its action space or imitation objective, combining intrinsic-conditioned ray embeddings, projective positional encoding (PRoPE), and bidirectional cross-view fusion.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have made rapid progress in generalist robot
manipulation by harnessing semantic knowledge from pretrained vision-language backbones,
but their visual tokens remain grounded in 2D image coordinates rather than the
calibrated geometry of the robot's cameras -- a mismatch especially pronounced in multi-
camera setups, where views are coupled by known intrinsics and extrinsics yet processed
as independent images. We propose G$^3$VLA, a camera-aware geometric module that injects
calibrated structure into the visual-token stream of a pretrained VLA without altering
its action space or imitation objective, combining intrinsic-conditioned ray embeddings,
projective positional encoding (PRoPE), and bidirectional cross-view fusion. Geometric
supervision is provided either from ground-truth point maps when available, or from
confidence-gated $π^3$X teacher predictions, requiring no depth sensors or manual
annotations. Instantiated on $π_0$, G$^3$VLA yields consistent gains across the LIBERO
suites, RoboCasa24, RoboTwin2.0, and real-robot settings, with the largest improvements
on spatially and object-sensitive tasks. We further validate on $π_{0.5}$ and GR00T 1.5,
with results suggesting that geometric transfer is most effective when geometry-aware
tokens have direct access to the action generation pathway. Our project page is at
https://sites.google.com/view/g3vla

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24472v1
- Authors: Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, Fares Abu-Dakka, Li Guo
- Published: 2026-06-23T12:02:36Z
- Age days: 1

</details>
