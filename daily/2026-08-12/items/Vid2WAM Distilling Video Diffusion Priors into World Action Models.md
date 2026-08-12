---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08558v1"
published: "2026-08-09T08:02:49Z"
age_days: 2
score: 24
created: 2026-08-12
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Vid2WAM: Distilling Video Diffusion Priors into World Action Models

> [!summary] 一句话结论（基于摘要）
> Simulation and real-world experiments demonstrate that Vid2WAM improves novel-task generalization and data efficiency under limited expert demonstrations while preserving low-latency inference.

## 关键点

- **问题**：However, their scalability and generalization remain constrained by their reliance on costly expert demonstrations.
- **创新点 / 方法**：In this paper, we propose Vid2WAM, an offline distillation framework that transfers visual diffusion priors from a large video foundation model into a compact WAM student.
- **证据**：Simulation and real-world experiments demonstrate that Vid2WAM improves novel-task generalization and data efficiency under limited expert demonstrations while preserving low-latency inference.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) improve robot policy learning by jointly modeling future
visual dynamics and actions. However, their scalability and generalization remain
constrained by their reliance on costly expert demonstrations. We challenge this by
asking whether future supervision for WAMs must originate from target-task expert
trajectories. In this paper, we propose Vid2WAM, an offline distillation framework that
transfers visual diffusion priors from a large video foundation model into a compact WAM
student. Given an observation and language instruction, Vid2WAM distills supervision
through two complementary channels: task-conditioned future rollouts directly supervise
the student's future prediction branch, while an inverse dynamics model recovers
embodiment-specific pseudo-actions for action learning. To robustly integrate synthetic
and real supervision, we introduce source-aware residual action adaptation that learns
source-specific corrections around a shared action backbone and mitigates interference
from noisy pseudo-actions. During inference, both the video teacher and inverse dynamics
model are discarded, leaving only the WAM student for efficient deployment. Simulation
and real-world experiments demonstrate that Vid2WAM improves novel-task generalization
and data efficiency under limited expert demonstrations while preserving low-latency
inference.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08558v1
- Authors: Chenhao Qiu, Ruixiang Wang, Runyi Zhao, Sixu Lin, Songen Gu, Shufeng Nan, Guiliang Liu, Kui Jia, Yanwei Fu, Simo Wu
- Published: 2026-08-09T08:02:49Z
- Age days: 2

</details>
