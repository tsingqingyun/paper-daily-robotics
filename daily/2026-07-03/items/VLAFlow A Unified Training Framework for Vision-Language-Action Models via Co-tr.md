---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01586v1"
published: "2026-07-02T01:38:16Z"
age_days: 1
score: 35
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment

> [!summary] 一句话结论（基于摘要）
> In contrast, language supervision helps preserve vision-language generalization, while future latent alignment improves state-transition and action- outcome modeling.

## 关键点

- **问题**：Vision-language-action models (VLAs) have recently advanced robotic manipulation, yet the effects of different robot-data pre-training paradigms remain difficult to compare because existing models often differ in architecture, data, action space, and evaluation protocol.
- **创新点 / 方法**：We present VLAFlow (Vision-Language-Action Flow), a unified flow-matching framework for controlled comparison of VLA training objectives.
- **证据**：In contrast, language supervision helps preserve vision-language generalization, while future latent alignment improves state-transition and action- outcome modeling.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/VLAFlow A Unified Training Framework for Vision-Language-Action Models via Co-tr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action models (VLAs) have recently advanced robotic manipulation, yet
the effects of different robot-data pre-training paradigms remain difficult to compare
because existing models often differ in architecture, data, action space, and evaluation
protocol. We present VLAFlow (Vision-Language-Action Flow), a unified flow-matching
framework for controlled comparison of VLA training objectives. Using a heterogeneous
robot corpus, OXEMix, containing approximately 5,000 hours of data from DROID, OpenX-
Embodiment, OpenX-Augmented, and RoboCOIN, we evaluate four paradigms under the same
pi0-style architecture, shared VLM backbone, action expert, and 14-dimensional action
space: action-only modeling (MindPI), language-supervised co-training (MindLPI), future
latent alignment (MindWPI), and their combination (MindLWPI). Experiments on LIBERO,
LIBERO-Plus, and SimplerEnv show that action-only pre-training is sensitive to
heterogeneous data. In contrast, language supervision helps preserve vision-language
generalization, while future latent alignment improves state-transition and action-
outcome modeling. By combining both signals, MindLWPI achieves the most stable overall
transfer performance across benchmarks. These results suggest a meta-action space view:
language and future latent representations provide complementary intermediate
constraints that make heterogeneous action supervision smoother and more transferable.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01586v1
- Authors: Guoyang Xia, Fengfa Li, Hongjin Ji, Lei Ren, Fangxiang Feng, Kun Zhan, Yan Xie
- Published: 2026-07-02T01:38:16Z
- Age days: 1

</details>
