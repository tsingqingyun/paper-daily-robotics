---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22913v1"
published: "2026-06-22T06:53:58Z"
age_days: 2
score: 30
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving

> [!summary] 一句话结论（基于摘要）
> Our method achieves state-of-the-art performance on the NAVSIM benchmark in both PDMS and EPDMS.

## 关键点

- **问题**：However, most existing approaches directly generate the final trajectory without explicitly examining its future consequences, which limits their reliability in complex and dynamic environments.
- **创新点 / 方法**：To address this limitation, we propose IRR-Drive (Intend, Reflect, Refine), an adaptive multimodal reflection framework for autonomous driving.
- **证据**：Our method achieves state-of-the-art performance on the NAVSIM benchmark in both PDMS and EPDMS.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving
by incorporating reasoning for better interpretability and planning quality. However,
most existing approaches directly generate the final trajectory without explicitly
examining its future consequences, which limits their reliability in complex and dynamic
environments. To address this limitation, we propose IRR-Drive (Intend, Reflect,
Refine), an adaptive multimodal reflection framework for autonomous driving.
Specifically, to tightly couple high-level reasoning with physical constraints, IRR-
Drive first generates a preliminary textual intention and anticipates potential
interactions by predicting future semantic bird's-eye view (BEV) representations. This
dual-modality (Text + BEV) reflection space explicitly models anticipated scene
evolution, enabling the model to rigorously self-correct and refine its initial intent
before generating the final trajectory. Furthermore, to balance planning performance and
computational efficiency, we construct reflection-oriented training data and design an
adaptive reflection reward, enabling the model to adaptively select its reasoning mode
according to scene complexity. Instead of using reasoning primarily as an auxiliary
interpretation, IRR-Drive directly integrates an adaptive reflection mechanism into the
planning framework, enabling grounded, decision-aware trajectory correction that is
driven by scene complexity. Our method achieves state-of-the-art performance on the
NAVSIM benchmark in both PDMS and EPDMS. Extensive experiments demonstrate the
effectiveness of our multimodal reflection framework and validate the efficacy of the
proposed adaptive reflection strategy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22913v1
- Authors: Zisheng Chen, Yuping Qiu, Jianhua Han, Tao Tang, Xiuwei Chen, Likui Zhang, Ying-Cong Chen, Hang Xu, Xiaodan Liang
- Published: 2026-06-22T06:53:58Z
- Age days: 2

</details>
