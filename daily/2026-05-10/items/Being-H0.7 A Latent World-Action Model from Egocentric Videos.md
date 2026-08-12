---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2605.00078v1"
published: "2026-04-30T14:16:15Z"
age_days: 
score: 31
created: 2026-05-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Being-H0.7: A Latent World-Action Model from Egocentric Videos

> [!summary] 一句话结论（基于摘要）
> Experiments across six simulation benchmarks and diverse real-world tasks show that Being-H0.7 achieves state-of-the-art or comparable performance, combining the predictive benefits of world models with the efficiency and deployability of direct VLA policies.

## 关键点

- **问题**：Visual-Language-Action models (VLAs) have advanced generalist robot control by mapping multimodal observations and language instructions directly to actions, but sparse action supervision often encourages shortcut mappings rather than representations of dynamics, contact, and task progress.
- **创新点 / 方法**：We present Being-H0.7, a latent world-action model that brings future-aware reasoning into VLA-style policies without generating future frames.
- **证据**：Experiments across six simulation benchmarks and diverse real-world tasks show that Being-H0.7 achieves state-of-the-art or comparable performance, combining the predictive benefits of world models with the efficiency and deployability of direct VLA policies.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-10/Being-H0.7 A Latent World-Action Model from Egocentric Videos.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual-Language-Action models (VLAs) have advanced generalist robot control by mapping
multimodal observations and language instructions directly to actions, but sparse action
supervision often encourages shortcut mappings rather than representations of dynamics,
contact, and task progress. Recent world-action models introduce future prediction
through video rollouts, yet pixel-space prediction is a costly and indirect substrate
for control, as it may model visual details irrelevant to action generation and
introduces substantial training or inference overhead. We present Being-H0.7, a latent
world-action model that brings future-aware reasoning into VLA-style policies without
generating future frames. Being-H0.7 inserts learnable latent queries between perception
and action as a compact reasoning interface, and trains them with a future-informed
dual-branch design: a deployable prior branch infers latent states from the current
context, while a training-only posterior branch replaces the queries with embeddings
from future observations. Jointly aligning the two branches at the latent reasoning
space leads the prior branch to reason future-aware, action-useful structure from
current observations alone. At inference, Being-H0.7 discards the posterior branch and
performs no visual rollout. Experiments across six simulation benchmarks and diverse
real-world tasks show that Being-H0.7 achieves state-of-the-art or comparable
performance, combining the predictive benefits of world models with the efficiency and
deployability of direct VLA policies.

### 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2605.00078v1
- Authors: Hao Luo, Wanpeng Zhang, Yicheng Feng, Sipeng Zheng, Haiweng Xu, Chaoyi Xu, Ziheng Xi, Yuhui Fu, Zongqing Lu
- Published: 2026-04-30T14:16:15Z
- Age days: 

</details>
