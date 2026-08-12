---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09073v1"
published: "2026-08-10T03:23:26Z"
age_days: 1
score: 31
created: 2026-08-11
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Latent World Models with Monotone Planning Costs for Image-Goal Navigation

> [!summary] 一句话结论（基于摘要）
> On the GNM navigation dataset, our method outperforms Navigation World Models (NWM), DINO-WM, OmniVLA, and NoMaD, achieving state-of-the-art image-goal navigation performance while reducing orientation error by $2.7\times$ over the same-encoder DINO WM baseli…

## 关键点

- **问题**：Image-goal navigation with latent world models requires not only accurate future prediction, but also a planning cost that reliably ranks candidate action sequences.
- **创新点 / 方法**：To address this, we propose a latent world model built on a frozen DINO-family encoder and train it with two complementary objectives.
- **证据**：On the GNM navigation dataset, our method outperforms Navigation World Models (NWM), DINO-WM, OmniVLA, and NoMaD, achieving state-of-the-art image-goal navigation performance while reducing orientation error by $2.7\times$ over the same-encoder DINO WM baseline.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Image-goal navigation with latent world models requires not only accurate future
prediction, but also a planning cost that reliably ranks candidate action sequences. We
define the cost as the cosine distance between the predicted future embedding and the
goal embedding, and show that poor cost ordering can mislead sampling-based planners
such as Cross-Entropy Method (CEM). To address this, we propose a latent world model
built on a frozen DINO-family encoder and train it with two complementary objectives. An
autoregressive rollout loss reduces the gap between training and multi-step planning
rollouts, while a Monotone Cost Ranking (MCR) loss directly encourages increasingly
perturbed action sequences to receive higher planning costs. We also study InfoNCE-based
action-contrastive training and find that temporal permutation negatives distort the
latent geometry and degrade planning performance. On the GNM navigation dataset, our
method outperforms Navigation World Models (NWM), DINO-WM, OmniVLA, and NoMaD, achieving
state-of-the-art image-goal navigation performance while reducing orientation error by
$2.7\times$ over the same-encoder DINO WM baseline. We also deploy the model zero-shot
on a physical robot, where it follows goal-directed paths in unseen indoor and outdoor
environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09073v1
- Authors: Amirhosein Chahe, Siwei Cai, Lifeng Zhou
- Published: 2026-08-10T03:23:26Z
- Age days: 1

</details>
