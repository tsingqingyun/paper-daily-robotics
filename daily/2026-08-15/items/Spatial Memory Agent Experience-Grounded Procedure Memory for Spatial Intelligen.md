---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12743v1"
published: "2026-08-13T02:42:35Z"
age_days: 2
score: 33
created: 2026-08-15
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence

> [!summary] 一句话结论（基于摘要）
> Across five representative spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and the best accuracy among the evaluated methods in most of the 20 evaluations, establishing a practical parameter-update-free…

## 关键点

- **问题**：Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants.
- **创新点 / 方法**：We present \textbf{Spatial Memory Agent (SMA)}, an \textbf{experience-grounded runtime framework} that converts verified spatial experience into reusable transferable lessons.
- **证据**：Across five representative spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and the best accuracy among the evaluated methods in most of the 20 evaluations, establishing a practical parameter-update-free path for spatial self-evolution across the evaluated frozen…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/Spatial Memory Agent Experience-Grounded Procedure Memory for Spatial Intelligen.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants. To improve the spatial reasoning ability of VLM agents, existing work has mainly followed two lines. One line uses post-training methods, such as supervised fine-tuning and reinforcement learning. Another line adopts an agentic paradigm in which the model calls external spatial tools, such as depth estimation and 3D reconstruction tools, to gather intermediate spatial evidence. We study a complementary and underexplored route: Can a frozen VLM agent improve its spatial reasoning through \textbf{parameter-update-free self-evolution}, without depending on external expert spatial tools at inference time? We present \textbf{Spatial Memory Agent (SMA)}, an \textbf{experience-grounded runtime framework} that converts verified spatial experience into reusable transferable lessons. In a verifiable spatial environment, SMA queries the frozen VLM, obtains a predicted answer and reward, and uses \textbf{verifier-guided reflection} to distill compact transferable lessons from spatial experience. SMA further assigns each lesson a \textbf{Transfer Reliability Score (TRS)}, which is initialized uniformly and calibrated from later retrieval outcomes as visit evidence of future transfer reliability. During \textbf{read-only deployment}, SMA retrieves lessons by semantic filter and similarity-TRS combined ranking, allowing the retrieved memory to guide frozen model inference. Across five representative spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and the best accuracy among the evaluated methods in most of the 20 evaluations, establishing a practical parameter-update-free path for spatial self-evolution across the evaluated frozen model scales and environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12743v1
- Authors: Haokai Zhang, Yuhang Ding, Yunshu Zhou, Xinze Du, Shengtao Zhang, Zhiyue Zhao, Yuling Xi, Hao Chen
- Published: 2026-08-13T02:42:35Z
- Age days: 2

</details>
