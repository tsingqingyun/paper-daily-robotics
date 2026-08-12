---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12366v1"
published: "2026-06-10T17:34:25Z"
age_days: 1
score: 32
created: 2026-06-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies

> [!summary] 一句话结论（基于摘要）
> Comprehensive experiments validate that APT achieves consistent gains on unseen instructions and compositional tasks.

## 关键点

- **问题**：Vision-Language-Action (VLA) models that couple pretrained Vision-Language Models (VLMs) with continuous action experts have achieved strong manipulation performance, yet generalization to out-of-distribution (OOD) language instructions remains poor.
- **创新点 / 方法**：A known challenge is the structural imbalance in VLA data, where language is far less diverse than visual and action content, making policies prone to visual shortcuts.
- **证据**：Comprehensive experiments validate that APT achieves consistent gains on unseen instructions and compositional tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/APT Action Expert Pretraining Improves Instruction Generalization of Vision-Lang.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models that couple pretrained Vision-Language Models (VLMs)
with continuous action experts have achieved strong manipulation performance, yet
generalization to out-of-distribution (OOD) language instructions remains poor. A known
challenge is the structural imbalance in VLA data, where language is far less diverse
than visual and action content, making policies prone to visual shortcuts. While
discrete-action methods mitigate this through vision-language co-training, continuous
action experts lack such protection: they start from random initialization and learn
entirely from imbalanced data, producing noisy gradients that corrupt the VLM and fail
to exploit its language capability. We address this from a Bayesian perspective,
factorizing the policy into a language-agnostic Vision-Action (VA) prior and a language-
conditioned VLA likelihood, and propose APT, a two-stage training method emphasizing
Action expert PreTraining. In Stage 1, the action expert is pretrained as a VA prior on
vision-action pairs from a frozen VLM, bypassing the language imbalance. In Stage 2,
language tokens are injected through a gated fusion mechanism that integrates VLM
features while preserving the learned visuomotor prior. APT applies to mainstream VLA
architectures, including the $π$ and GR00T-style architectures. Comprehensive
experiments validate that APT achieves consistent gains on unseen instructions and
compositional tasks. Project Page: https://xukechun.github.io/papers/APT/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12366v1
- Authors: Kechun Xu, Zhenjie Zhu, Anzhe Chen, Rong Xiong, Yue Wang
- Published: 2026-06-10T17:34:25Z
- Age days: 1

</details>
