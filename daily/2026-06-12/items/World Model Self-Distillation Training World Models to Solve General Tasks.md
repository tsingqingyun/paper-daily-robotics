---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12072v1"
published: "2026-06-10T13:40:19Z"
age_days: 1
score: 31
created: 2026-06-12
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# World Model Self-Distillation: Training World Models to Solve General Tasks

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12072v1
- Authors: Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan, Paolo Favaro
- Published: 2026-06-10T13:40:19Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
