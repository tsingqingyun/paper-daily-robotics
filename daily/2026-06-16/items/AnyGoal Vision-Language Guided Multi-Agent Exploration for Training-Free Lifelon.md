---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13878v1"
published: "2026-06-11T20:07:34Z"
age_days: 4
score: 22
created: 2026-06-16
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# AnyGoal: Vision-Language Guided Multi-Agent Exploration for Training-Free Lifelong Navigation

> [!summary] 一句话结论（基于摘要）
> The BVM maintains a per-pixel (mu, sigma^2) posterior over goal relevance, updated via precision-weighted fusion of VLM scores through a depth-cone mask, and is never reset between subtasks, yielding lifelong evidence accumulation.

## 关键点

- **问题**：Modular pipelines such as Modular GOAT are bottlenecked by closed-set object detection recall, while 3D snapshot-memory systems (e.g.
- **创新点 / 方法**：We present AnyGoal, a training-free multi- robot architecture that places a Vision-Language Model (VLM) at the core of frontier- based exploration and coordinates agents through a shared 2D Gaussian Bayesian Value Map (BVM).
- **证据**：The BVM maintains a per-pixel (mu, sigma^2) posterior over goal relevance, updated via precision-weighted fusion of VLM scores through a depth-cone mask, and is never reset between subtasks, yielding lifelong evidence accumulation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end navigation policies trained on large simulation corpora degrade sharply when
transferred to out-of-distribution scenes, categories, or goal modalities. Modular
pipelines such as Modular GOAT are bottlenecked by closed-set object detection recall,
while 3D snapshot-memory systems (e.g. 3D-Mem) accumulate dense, view-dependent
representations that are heavy to maintain. We present AnyGoal, a training-free multi-
robot architecture that places a Vision-Language Model (VLM) at the core of frontier-
based exploration and coordinates agents through a shared 2D Gaussian Bayesian Value Map
(BVM). The BVM maintains a per-pixel (mu, sigma^2) posterior over goal relevance,
updated via precision-weighted fusion of VLM scores through a depth-cone mask, and is
never reset between subtasks, yielding lifelong evidence accumulation. Frontiers are
ranked by a convex blend of a VLM-as-judge softmax and a Bayesian UCB term on the BVM. A
greedy allocator with spatial-separation penalty and commitment hysteresis distributes
frontiers across agents without a centralized controller. On the full GOAT-Bench val
unseen split (360 episodes, 2,669 subtasks), our dual-agent system achieves 52.4%
Subtask SR at 12.7% SPL--state of the art under the strict physical regime (discrete
0.25 m steps, no teleportation, 42 deg HFOV) and a +27.5 pp improvement over Modular
GOAT (24.9%). Single-agent AnyGoal achieves 41.9% Subtask SR, showing gains arise from
the decision architecture. A four-way perception ablation shows that open-vocabulary
detectors shift the dominant failure mode from exploration to goal verification.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13878v1
- Authors: MoniJesu James, Marcelino Julio Fernando, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- Published: 2026-06-11T20:07:34Z
- Age days: 4

</details>
