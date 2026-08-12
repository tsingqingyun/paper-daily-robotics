---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12072v1"
published: "2026-06-10T13:40:19Z"
age_days: 1
score: 31
created: 2026-06-12
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# World Model Self-Distillation: Training World Models to Solve General Tasks

> [!summary] 一句话结论（基于摘要）
> We propose a scalable framework that elicits task-solving ability in such models by combining self-distillation with reinforcement learning.

## 关键点

- **问题**：Pretrained video generators are promising visual world models that exhibit emergent task-solving abilities; however, their reliance on detailed textual descriptions limits their direct use for planning and decision-making.
- **创新点 / 方法**：We propose a scalable framework that elicits task-solving ability in such models by combining self-distillation with reinforcement learning.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/World Model Self-Distillation Training World Models to Solve General Tasks.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pretrained video generators are promising visual world models that exhibit emergent
task-solving abilities; however, their reliance on detailed textual descriptions limits
their direct use for planning and decision-making. Existing approaches either outsource
this reasoning to language or vision-language models, or rely on supervised fine-tuning
with paired task-execution videos, which are costly to collect and difficult to scale.
We propose a scalable framework that elicits task-solving ability in such models by
combining self-distillation with reinforcement learning. Given an unlabeled scene image,
a vision-language model generates a candidate task and a detailed step-by-step solution.
The solution conditions a pretrained video diffusion model, the Demonstrator; we distill
its behavior into an Executor conditioned only on the image and a short task prompt.
This transfers execution knowledge from caption-guided generation to instruction-
conditioned task solving without curated task-video supervision. We further improve the
Executor with reinforcement learning from VLM feedback, exploiting the asymmetry between
judging whether a sampled video satisfies a task and generating the solution.
Experiments on our proposed WorldTasks-Benchmark and the DreamGen robotics benchmark
show that the Executor surpasses the Demonstrator under our VLM-based evaluation
protocol and transfers competitively to robotic tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12072v1
- Authors: Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan, Paolo Favaro
- Published: 2026-06-10T13:40:19Z
- Age days: 1

</details>
