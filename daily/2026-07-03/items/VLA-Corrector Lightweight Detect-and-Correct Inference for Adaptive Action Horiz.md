---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01804v1"
published: "2026-07-02T07:18:53Z"
age_days: 1
score: 39
created: 2026-07-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon

> [!summary] 一句话结论（基于摘要）
> To address this limitation, we propose VLA-Corrector, a lightweight corrective inference framework for action-chunked VLA policies.

## 关键点

- **问题**：However, this "predict-then-blindly-execute" paradigm sacrifices closed-loop reactivity: in contact- rich physical interactions, even small local perturbations can rapidly amplify within the open-loop blind spot, leading to compounding errors and ultimately task failure.
- **创新点 / 方法**：To address this limitation, we propose VLA-Corrector, a lightweight corrective inference framework for action-chunked VLA policies.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/VLA-Corrector Lightweight Detect-and-Correct Inference for Adaptive Action Horiz.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) foundation models have recently achieved strong progress in
embodied intelligence. To reduce policy-call frequency while preserving temporal
coherence, most generative policies adopt an action chunk mechanism, executing multiple
future actions in an open-loop manner under a fixed action horizon. However, this
"predict-then-blindly-execute" paradigm sacrifices closed-loop reactivity: in contact-
rich physical interactions, even small local perturbations can rapidly amplify within
the open-loop blind spot, leading to compounding errors and ultimately task failure. To
address this limitation, we propose VLA-Corrector, a lightweight corrective inference
framework for action-chunked VLA policies. Without modifying the backbone policy
weights, VLA-Corrector introduces a lightweight Latent-space Vision Monitor (LVM) that
continuously compares predicted and actual visual feature evolution, enabling online
detection of visual dynamics deviations. Once persistent deviation is detected, the
system triggers a truncation event, discards the remaining stale actions, and invokes
corrective replanning via Online Gradient Guidance (OGG). The detect-and-correct
mechanism of VLA-Corrector naturally induces an event-triggered adaptive action horizon:
it preserves long-horizon execution when the current chunk remains reliable, and invokes
short-horizon corrective replanning when execution begins to drift. In doing so, VLA-
Corrector mitigates the trade-off imposed by static horizons between execution
robustness and policy-call frequency. It can be integrated into different VLA models
without further retraining the VLA backbone, interrupting compounding errors while
preserving much of the efficiency benefit of action chunking and substantially improving
robustness in long-horizon, contact-rich robotic manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01804v1
- Authors: Yi Pan, Miao Pan, Qi Lu, Jiaming Huang, Man Zhang, Siteng Huang, Xin Li, Jie Zhang, Yongliang Shen, Xuhong Zhang, Wenqi Zhang
- Published: 2026-07-02T07:18:53Z
- Age days: 1

</details>
