---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02034v1"
published: "2026-07-02T11:01:20Z"
age_days: 0
score: 30
created: 2026-07-03
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# ComplexMimic: Human-Scene Interaction Imitation in Complex 3D Environments

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on three benchmark datasets demonstrate that our approach outperforms current state-of-the-art methods.

## 关键点

- **问题**：However, most existing methods focus on simplified scene settings, leaving complex environments largely unexplored, which limits their applicability in real-world scenarios.
- **创新点 / 方法**：To address this challenge, we propose ComplexMimic, a framework that reconstructs diverse HSI by interpreting imperfect MoCap data.
- **证据**：Extensive experiments on three benchmark datasets demonstrate that our approach outperforms current state-of-the-art methods.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physics-based Human-Scene Interaction (HSI) imitation learning is crucial for embodied
intelligence as it bridges the gap between kinematic 3D motions and real-world dynamics.
However, most existing methods focus on simplified scene settings, leaving complex
environments largely unexplored, which limits their applicability in real-world
scenarios. In this paper, we focus on HSI mimicry in complex environments. Under this
complex setting, we observe an inherent trade-off between successfully performing
interaction and maintaining natural, physically plausible motions. To address this
challenge, we propose ComplexMimic, a framework that reconstructs diverse HSI by
interpreting imperfect MoCap data. First, we introduce a Dual Flow Strategy, which
learns two complementary experts: an imitation expert for accurate motion tracking and
an interaction expert for collision-aware adaptation in complex scenes. Second, naive
multi-expert distillation, which treats all experts equally, often under-samples
challenging behaviors, limiting effective learning. To mitigate this issue, we propose a
difficulty-aware distillation strategy that adaptively weights supervision and
prioritizes hard-yet-learnable trajectories guided by failure statistics and learning
progress signals. Extensive experiments on three benchmark datasets demonstrate that our
approach outperforms current state-of-the-art methods. Our implementation is available
at https://github.com/LuPan23/ComplexMimic.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02034v1
- Authors: Lu Pan, Hongwei Zhao
- Published: 2026-07-02T11:01:20Z
- Age days: 0

</details>
