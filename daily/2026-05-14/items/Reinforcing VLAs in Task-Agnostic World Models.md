---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12334v1"
published: "2026-05-12T16:16:15Z"
age_days: 1
score: 33
created: 2026-05-14
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Reinforcing VLAs in Task-Agnostic World Models

> [!summary] 一句话结论（基于摘要）
> We propose RAW-Dream (Reinforcing VLAs in task-Agnostic World Dreams), a new paradigm that completely disentangles world model learning from downstream task dependencies.

## 关键点

- **问题**：However, while using imagined trajectories reduces the sample complexity of policy training, existing methods still heavily rely on task- specific data to fine-tune both the world and reward models, fundamentally limiting their scalability to unseen tasks.
- **创新点 / 方法**：We propose RAW-Dream (Reinforcing VLAs in task-Agnostic World Dreams), a new paradigm that completely disentangles world model learning from downstream task dependencies.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Post-training Vision-Language-Action (VLA) models via reinforcement learning (RL) in
learned world models has emerged as an effective strategy to adapt to new tasks without
costly real-world interactions. However, while using imagined trajectories reduces the
sample complexity of policy training, existing methods still heavily rely on task-
specific data to fine-tune both the world and reward models, fundamentally limiting
their scalability to unseen tasks. To overcome this, we argue that world and reward
models should capture transferable physical priors that enable zero-shot inference. We
propose RAW-Dream (Reinforcing VLAs in task-Agnostic World Dreams), a new paradigm that
completely disentangles world model learning from downstream task dependencies. RAW-
Dream utilizes a world model pre-trained on diverse task-free behaviors for predicting
future rollouts, and an off-the-shelf Vision-Language Model (VLM) for reward generation.
Because both components are task-agnostic, VLAs can be readily finetuned for any new
task entirely within this zero-shot imagination. Furthermore, to mitigate world model
hallucinations, we introduce a dual-noise verification mechanism to filter out
unreliable rollouts. Extensive experiments across simulation and real-world settings
demonstrate consistent performance gains, proving that generalized physical priors can
effectively substitute for costly task-dependent data, offering a highly scalable
roadmap for VLA adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12334v1
- Authors: Yucen Wang, Rui Yu, Fengming Zhang, Junjie Lu, Xinyao Qin, Tianxiang Zhang, Kaixin Wang, Li Zhao
- Published: 2026-05-12T16:16:15Z
- Age days: 1

</details>
