---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09771v1"
published: "2026-08-10T15:58:39Z"
age_days: 0
score: 53
created: 2026-08-11
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> We propose SLIM (Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction policy.

## 关键点

- **问题**：Vision-language-action policies rely on large multimodal backbones to jointly perform perception, language conditioning, and action generation at every control step.
- **创新点 / 方法**：We propose SLIM (Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction policy.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：53
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-11/SLIM-0.5B Learning Action-Grounded Predictive Latents for Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action policies rely on large multimodal backbones to jointly perform
perception, language conditioning, and action generation at every control step. Much of
this capacity supports open-domain semantics, whereas continuous robot manipulation
primarily requires compact representations of observations, actions, and the transitions
induced by actions. Pixel-level world models provide another route, but predicting
visual details irrelevant to control can be unnecessarily expensive. We propose SLIM
(Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction
policy. SLIM learns action-grounded predictive latents that capture both action-
conditioned future transitions and the actions that explain observed changes. SLIM
learns these representations through self-supervised masked trajectory prediction,
combining action reconstruction with future-latent prediction. A compact Mixture-of-
Transformers (MoT) backbone models interactions between observation latents and action
tokens. The resulting policy is trained with flow matching for language-conditioned
action generation. Across simulation benchmarks and real-world evaluation, SLIM matches
or exceeds representative large-scale VLA and world-action-model baselines with fewer
parameters, no additional embodied pretraining, lower inference latency, and
substantially lower GPU memory usage.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09771v1
- Authors: Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou
- Published: 2026-08-10T15:58:39Z
- Age days: 0

</details>
