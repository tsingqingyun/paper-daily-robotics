---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07089v1"
published: "2026-06-05T09:35:48Z"
age_days: 2
score: 29
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning

> [!summary] 一句话结论（基于摘要）
> Experiments on both simulated and real-world embodied tasks show that AdaWAM substantially improves inference efficiency while outperforming state-of-the-art embodied policies.

## 关键点

- **问题**：World Action Models (WAMs) offer a promising approach to embodied intelligence, yet existing methods rely heavily on video prediction as action priors and lack adaptive multimodal reasoning, limiting their effectiveness on long-horizon, complex tasks.
- **创新点 / 方法**：Motivated by this observation, we propose \textbf{AdaWAM}, a world action model with adaptive multimodal reasoning abilities.
- **证据**：Experiments on both simulated and real-world embodied tasks show that AdaWAM substantially improves inference efficiency while outperforming state-of-the-art embodied policies.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) offer a promising approach to embodied intelligence, yet
existing methods rely heavily on video prediction as action priors and lack adaptive
multimodal reasoning, limiting their effectiveness on long-horizon, complex tasks. We
observe that WAMs require different multimodal reasoning modes under different execution
contexts: textual reasoning is essential during task transitions to guide high-level
action prediction, while visual reasoning is critical during fine-grained manipulation
for precise control. Motivated by this observation, we propose \textbf{AdaWAM}, a world
action model with adaptive multimodal reasoning abilities. AdaWAM integrates a
lightweight dynamic router that autonomously triggers textual or visual reasoning as
needed during task execution. Experiments on both simulated and real-world embodied
tasks show that AdaWAM substantially improves inference efficiency while outperforming
state-of-the-art embodied policies. Codes and demos are available at:
https://adawam.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07089v1
- Authors: Yinzhou Tang, Jingbo Xu, Yu Shang, Zihao Song, Chen Gao, Wei Wu, Yong Li
- Published: 2026-06-05T09:35:48Z
- Age days: 2

</details>
