---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19710v1"
published: "2026-08-20T07:09:37Z"
age_days: 2
score: 28
created: 2026-08-22
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions

> [!summary] 一句话结论（基于摘要）
> Under extreme combined degradation, the DINOv2 baseline achieves 0.4610 balanced accuracy, while degradation-aware visual-sonar fusion reaches 0.6152, a 33.5% relative improvement.

## 关键点

- **问题**：Reliable underwater robotic perception remains difficult because optical imagery degrades under turbidity, wavelength-dependent attenuation, low illumination, scattering, and blur.
- **创新点 / 方法**：Our method trains the fusion mechanism across the full range of degradation while keeping the visual and sonar encoders frozen, allowing modality contributions to adapt without fine-tuning the pretrained backbone.
- **证据**：Under extreme combined degradation, the DINOv2 baseline achieves 0.4610 balanced accuracy, while degradation-aware visual-sonar fusion reaches 0.6152, a 33.5% relative improvement.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degra.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable underwater robotic perception remains difficult because optical imagery degrades under turbidity, wavelength-dependent attenuation, low illumination, scattering, and blur. Although sonar provides complementary information that is less affected by optical visibility, prior visual-sonar research has largely focused on feature alignment and nominal detection performance. We investigate cross-modal robustness as visual reliability deteriorates and assess whether pretrained visual foundation-model representations can be complemented by sonar under severe degradation. We use frozen DINOv2 as the visual encoder and construct a controlled five-level benchmark ranging from clean to extreme visual conditions. We compare conventional visual detection, frozen foundation-model representations, sonar context, fixed multimodal fusion, clean-trained adaptive gating, and degradation-aware gated fusion. Our method trains the fusion mechanism across the full range of degradation while keeping the visual and sonar encoders frozen, allowing modality contributions to adapt without fine-tuning the pretrained backbone. Under extreme combined degradation, the DINOv2 baseline achieves 0.4610 balanced accuracy, while degradation-aware visual-sonar fusion reaches 0.6152, a 33.5% relative improvement. The learned sonar contribution increases from 14.2% under clean conditions to 41.3% under extreme degradation, demonstrating adaptive redistribution of cross-modal reliance. Fusion provides the largest gains under severe turbidity and blur, whereas color attenuation alone yields little additional benefit. These results show that foundation-model representations remain valuable but insufficient under severe information loss, and that explicitly adapting fusion to modality reliability can improve robust underwater multimodal perception.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19710v1
- Authors: Mohammad Arif Ul Alam
- Published: 2026-08-20T07:09:37Z
- Age days: 2

</details>
