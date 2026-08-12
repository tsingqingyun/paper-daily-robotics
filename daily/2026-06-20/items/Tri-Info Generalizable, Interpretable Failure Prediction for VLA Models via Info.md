---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19998v1"
published: "2026-06-18T09:34:22Z"
age_days: 1
score: 30
created: 2026-06-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "Sim2Real", "具身智能评测与基准"]
---

# Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory

> [!summary] 一句话结论（基于摘要）
> Moreover, Tri-Info transfers across architectures, environments, and the sim-to- real gap without retraining, reaching 83\% accuracy on real-world tasks where prior detectors collapse to chance.

## 关键点

- **问题**：Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet they remain black boxes whose physical interactions can cause irreversible harm, making generalizable and interpretable failure detection essential.
- **创新点 / 方法**：We observe that successful and failed rollouts carry systematically different information-theoretic signatures.
- **证据**：Moreover, Tri-Info transfers across architectures, environments, and the sim-to- real gap without retraining, reaching 83\% accuracy on real-world tasks where prior detectors collapse to chance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/Tri-Info Generalizable, Interpretable Failure Prediction for VLA Models via Info.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet
they remain black boxes whose physical interactions can cause irreversible harm, making
generalizable and interpretable failure detection essential. We observe that successful
and failed rollouts carry systematically different information-theoretic signatures.
Building on this, we formalize VLA control as a closed-loop information pipeline and
derive the Triple Information-theoretic (Tri-Info) signals that capture whether actions
remain diverse, temporally consistent, and coupled to state transitions. Across six VLA
models and three benchmark environments, Tri-Info matches the strongest baselines in-
domain. Moreover, Tri-Info transfers across architectures, environments, and the sim-to-
real gap without retraining, reaching 83\% accuracy on real-world tasks where prior
detectors collapse to chance. This establishes Tri-Info as a simple yet powerful method
that not only detects failures with strong cross-domain generalization, but also
delivers interpretable diagnostics of the underlying failure modes.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19998v1
- Authors: Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang, Zhengyang Hu, Yanchao Yang
- Published: 2026-06-18T09:34:22Z
- Age days: 1

</details>
