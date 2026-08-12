---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07107v1"
published: "2026-06-05T10:01:37Z"
age_days: 2
score: 31
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Experiments on LIBERO, SimplerEnv-WidowX, and real-world manipulation tasks show that action-token planning consistently improves over direct action generation, with the largest gains on long-horizon multi-stage tasks.

## 关键点

- **问题**：Most vision-language-action (VLA) models map observations directly to actions without explicit intermediate planning, which limits performance on long-horizon tasks where early mistakes compound.
- **创新点 / 方法**：We propose Coarse-to-Control, a plan-execute VLA that introduces planning natively in the action-token space.
- **证据**：Experiments on LIBERO, SimplerEnv-WidowX, and real-world manipulation tasks show that action-token planning consistently improves over direct action generation, with the largest gains on long-horizon multi-stage tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Most vision-language-action (VLA) models map observations directly to actions without
explicit intermediate planning, which limits performance on long-horizon tasks where
early mistakes compound. We propose Coarse-to-Control, a plan-execute VLA that
introduces planning natively in the action-token space. The key idea is to let the
policy first predict a compact sequence of coarse action tokens that summarize the
intended future trajectory, and then generate executable action tokens conditioned on
this plan. Because both planning and execution share a unified discrete action
vocabulary, the plan stays close to the control manifold and provides directly
actionable guidance rather than an abstract hint that must be translated back to motor
commands. Experiments on LIBERO, SimplerEnv-WidowX, and real-world manipulation tasks
show that action-token planning consistently improves over direct action generation,
with the largest gains on long-horizon multi-stage tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07107v1
- Authors: Jinhao Wu, Shiduo Zhang, Yicheng Liu, Xiaopeng Yu, Sixian Li, Siyin Wang, Hang Zhao, Jing Huo, Yang Gao, Jingjing Gong, Xipeng Qiu, Yu-Gang Jiang
- Published: 2026-06-05T10:01:37Z
- Age days: 2

</details>
