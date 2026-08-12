---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18840v1"
published: "2026-07-21T08:25:37Z"
age_days: 0
score: 40
created: 2026-07-22
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory

> [!summary] 一句话结论（基于摘要）
> In this paper, we introduce WorldScape Policy 2.0, a controllable WAM with reasoning-augmented long short-term memory.

## 关键点

- **问题**：However, existing WAMs are constrained by limited temporal context, coarse episode-level language supervision, and predominantly text-only conditioning, which hinder task-progress tracking and fine- grained language-video-action grounding while limiting visual-context reasoning and cross-embodiment transfer.
- **创新点 / 方法**：In this paper, we introduce WorldScape Policy 2.0, a controllable WAM with reasoning-augmented long short-term memory.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) offer a promising paradigm for robotic manipulation by
jointly modeling visual state transitions and robot actions. However, existing WAMs are
constrained by limited temporal context, coarse episode-level language supervision, and
predominantly text-only conditioning, which hinder task-progress tracking and fine-
grained language-video-action grounding while limiting visual-context reasoning and
cross-embodiment transfer. In this paper, we introduce WorldScape Policy 2.0, a
controllable WAM with reasoning-augmented long short-term memory. Its causal short-term
visual memory supplies recent observations as DiT prefill to preserve local interaction
dynamics, while its long short-term event memory organizes historical VLM outputs into
global-history, local-active, and event-boundary representations for progress-aware
retrieval. The retrieved history augments perception and autoregressively generated
planning tokens, yielding an implicit subgoal condition for autonomous planning;
semantic forcing further transfers event-level instruction semantics into this latent
planning pathway. To establish fine-grained multimodal controllability, we construct
ManipEvent-5M, an event-grounded embodied pretraining dataset containing nearly 5
million event segments with aligned action trajectories, episode-level task
instructions, segment-level subtask captions, goal images, and video demonstrations.
These designs provide a unified interface for autonomous planning from high-level
instructions and controllable execution from fine-grained text, goal-image, or video-
context prompts. Experiments in both simulation and real-world platforms demonstrate
superior capabilities in long-horizon autonomous planning, fine-grained instruction
following and in-context adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18840v1
- Authors: Haisheng Su, Zongdai Liu, Xin Jin, Haoxuan Dou, Chengming Hu, Baorun Li, Zhanwang Liu, Ruiyan Xu, Jianjie Fang, Xin Zhang, Zhenjie Yang, Xue Yang, Chen Gao, Junchi Yan, Yong Li, Wei Wu
- Published: 2026-07-21T08:25:37Z
- Age days: 0

</details>
