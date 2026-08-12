---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18363v1"
published: "2026-06-16T18:09:26Z"
age_days: 2
score: 38
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Guava: An Effective and Universal Harness for Embodied Manipulation

> [!summary] 一句话结论（基于摘要）
> In this work, we present Guava, a harness framework for embodied tool use developed through systematic exploration of the design space of agent workflows, action spaces, and observation spaces.

## 关键点

- **问题**：However, it remains unclear what makes an effective harness for embodied manipulation, and to what extent such a harness can unlock embodied capabilities in a wide range of reasoning models.
- **创新点 / 方法**：In this work, we present Guava, a harness framework for embodied tool use developed through systematic exploration of the design space of agent workflows, action spaces, and observation spaces.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Language models trained on large-scale vision-language data have demonstrated strong
potential for embodied agents. Harnessing models through embodied tools use offers a
promising alternative to end-to-end vision-language-action systems by combining high-
level reasoning with external modules for perception, planning, and control. However, it
remains unclear what makes an effective harness for embodied manipulation, and to what
extent such a harness can unlock embodied capabilities in a wide range of reasoning
models. In this work, we present Guava, a harness framework for embodied tool use
developed through systematic exploration of the design space of agent workflows, action
spaces, and observation spaces. Our study identifies three key ingredients for effective
embodied agents: iterative perception-reasoning-action loops, semantic action
abstractions, and multimodal observations. To understand whether these design principles
are universal even to small models, we develop an end-to-end training pipeline that
distills embodied manipulation capabilities into a 4B open-source model using fewer than
2K trajectories collected entirely in simulation. Experimental results in both
simulation and real-world environments show performance comparable to frontier
proprietary models while exhibiting strong generalization to unseen objects, novel
instructions, and long-horizon tasks. Results suggest that a well-designed harness can
serve as a scalable, model-agnostic interface for embodied manipulation, enabling strong
emergent embodied capabilities in compact open-source models with minimal training data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18363v1
- Authors: Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou, Jia-Bin Huang, Furong Huang, Jiayuan Mao
- Published: 2026-06-16T18:09:26Z
- Age days: 2

</details>
