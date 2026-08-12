---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20207v1"
published: "2026-07-22T14:27:45Z"
age_days: 2
score: 25
created: 2026-07-25
concepts: ["多模态基础模型", "世界模型"]
---

# SeededGrasp: Language-Guided Grasping in Complex Scenes with Multiple Embodiments

> [!summary] 一句话结论（基于摘要）
> Experimental results demonstrate that our approach outperforms existing baselines, achieving 72% success in simulation and 78% in real- world grasping experiments.

## 关键点

- **问题**：Vision-language models (VLMs) offer a natural way to specify these requirements using language, but existing approaches either use a VLM to predict the grasp directly with limited spatial awareness, or train the VLM together with the grasping model, which requires significantly more data and compute.
- **创新点 / 方法**：Experimental results demonstrate that our approach outperforms existing baselines, achieving 72% success in simulation and 78% in real- world grasping experiments.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：These limitations impede performance and have prevented scaling to multiple embodiments in complex scenes.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/SeededGrasp Language-Guided Grasping in Complex Scenes with Multiple Embodiments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Practical robotic grasping in complex scenes requires both 3D spatial reasoning and
alignment with task-specific requirements. Vision-language models (VLMs) offer a natural
way to specify these requirements using language, but existing approaches either use a
VLM to predict the grasp directly with limited spatial awareness, or train the VLM
together with the grasping model, which requires significantly more data and compute.
These limitations impede performance and have prevented scaling to multiple embodiments
in complex scenes. We address this by proposing SeededGrasp, a novel data-efficient
framework that enables a VLM to predict a seed point to be used as conditioning for a
subsequent lightweight grasp-generation model. Our architecture decouples high-level
semantic reasoning from low-level geometric execution, enabling multi-embodiment support
while bypassing the need for expensive end-to-end training. To enable training such
models, we release the first multi-embodiment tabletop grasping dataset comprising over
2.5M grasps in cluttered scenes. Experimental results demonstrate that our approach
outperforms existing baselines, achieving 72% success in simulation and 78% in real-
world grasping experiments. See our project site for data and code: https://uoft-
isl.github.io/seeded-grasp/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20207v1
- Authors: Yang Xu, Gurpreet Singh Mukker, Raymond Wang, Jasper Gerigk, Maria Attarian, Igor Gilitschenski
- Published: 2026-07-22T14:27:45Z
- Age days: 2

</details>
