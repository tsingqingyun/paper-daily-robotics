---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13040v1"
published: "2026-06-11T08:20:42Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# RoboProcessBench: Benchmarking Process-Aware Understanding in Vision-Language Robotic Manipulation

## 为什么重要

自动筛选分数：25

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Vision-language models (VLMs) are increasingly explored as visual critics, reward
generators, and failure detectors in robotic manipulation. These roles implicitly
require models to judge not only final task success, but also how a manipulation
execution is physically and temporally progressing. However, existing evaluations fail
to test whether VLMs possess fine-grained process understanding. To address this gap, we
present RoboProcessBench, a benchmark for process-aware understanding in vision-language
robotic manipulation. RoboProcessBench decomposes such capability into two complementary
dimensions, \emph{static monitoring} and \emph{dynamic reasoning}, instantiated as 12
diagnostic question families covering phase, contact, motion, coordination, primitive-
local progress, temporal order, outcome, and primitive-level transitions. Built from
physically grounded execution traces, the curated benchmark corpus ProcessData contains
\textasciitilde 58k question-answer pairs across 260 manipulation tasks, which is
further split into ProcessData-SFT and ProcessData-Eval for post-training and evaluation
purposes. Extensive evaluation of various VLMs on ProcessData-Eval reveals broad
limitations across 12 diagnostic task families, suggesting current models still lack
robust process-aware understanding of manipulation executions. But with ProcessData-SFT,
the post-trained \textit{Qwen2.5-VL-7B} and \textit{InternVL-3-8B} exhibit consistent
gains on local state, motion, progress, and primitive-aware cues. These results
demonstrate that RoboProcessBench serves as both an evaluation benchmark and a learnable
supervision source for developing VLMs capable of monitoring and evaluating robotic
manipulation processes. Project webpage:
\href{https://processbench-2026.github.io/RoboProcessBench-
Web/}{https://processbench-2026.github.io}.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13040v1
- Authors: Dayu Xia, Yue Shi, Yao Mu, Huiting Ji, Chaofan Ma, Yingjie Zhou, Hua Chen, Yang Liu, Jiezhang Cao, Guangtao Zhai
- Published: 2026-06-11T08:20:42Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
