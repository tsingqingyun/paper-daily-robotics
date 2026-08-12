---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18610v1"
published: "2026-06-17T02:15:46Z"
age_days: 1
score: 47
created: 2026-06-19
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation

> [!summary] 一句话结论（基于摘要）
> Across seven real-world vision-language-action policies, SC3-Eval attains a closed-loop Pearson correlation of $0.929$ and MMRV of $0.119$, outperforming three strong prior video-model-based baselines, and generalizes to new tasks.

## 关键点

- **问题**：Evaluating generalist robot manipulation policies in the real world is expensive, slow, and difficult to scale.
- **创新点 / 方法**：Action-conditioned video world models offer a scalable alternative by simulating policy rollouts.
- **证据**：Across seven real-world vision-language-action policies, SC3-Eval attains a closed-loop Pearson correlation of $0.929$ and MMRV of $0.119$, outperforming three strong prior video-model-based baselines, and generalizes to new tasks.
- **局限**：First, forward-inverse dynamics consistency jointly trains the model to predict frames from actions and to recover actions from frames, anchoring generated rollouts to a physically plausible action manifold and counteracting the drift a forward-only model cannot penalize.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：47
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Evaluating generalist robot manipulation policies in the real world is expensive, slow,
and difficult to scale. Action-conditioned video world models offer a scalable
alternative by simulating policy rollouts. Autoregressive rollouts accumulate
compounding errors, observations across multiple camera views must remain mutually
consistent, and the evaluator must generalize to policies whose behaviors lie outside
the training distribution. We address these challenges with SC3-Eval, a self-consistent
video generation recipe that adapts a pre-trained video foundation model into an
accurate policy evaluator by enforcing three complementary forms of consistency. First,
forward-inverse dynamics consistency jointly trains the model to predict frames from
actions and to recover actions from frames, anchoring generated rollouts to a physically
plausible action manifold and counteracting the drift a forward-only model cannot
penalize. Second, cross-view consistency trains the model to inpaint each camera view
from the other, keeping the multi-camera observation coherent over long rollouts without
any explicit memory mechanism. Third, test-time consistency reuses the inverse dynamics
mode at inference as a per-action-chunk uncertainty signal that terminates rollouts
whose generated frames drift away from the requested actions. We also demonstrate
SC3-Eval rollouts reproduce the failure modes that policies exhibit in real-world
rollouts, supporting fine-grained diagnostic comparison rather than aggregate ranking
alone. Across seven real-world vision-language-action policies, SC3-Eval attains a
closed-loop Pearson correlation of $0.929$ and MMRV of $0.119$, outperforming three
strong prior video-model-based baselines, and generalizes to new tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18610v1
- Authors: Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi, XuDong Wang, Sergey Levine, Zhaoshuo Li, Jinwei Gu, Florian Shkurti, Ming-Yu Liu, Quan Vuong
- Published: 2026-06-17T02:15:46Z
- Age days: 1

</details>
