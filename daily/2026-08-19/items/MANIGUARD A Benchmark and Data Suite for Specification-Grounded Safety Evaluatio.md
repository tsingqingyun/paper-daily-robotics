---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17386v1"
published: "2026-08-18T05:27:35Z"
age_days: 0
score: 32
created: 2026-08-19
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline.

## 关键点

- **问题**：Benchmarking zero-shot and fine-tuned VLAs across more than 23,000 rollouts, we find: (i) safety must be evaluated independently of task success, as 6-21% of successful rollouts violate the specification; (ii) fine-tuning on our suite raises safe task completion from near zero to 7.5-29.8% and engaged-and-safe behavio…
- **创新点 / 方法**：We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Benchmarking zero-shot and fine-tuned VLAs across more than 23,000 rollouts, we find: (i) safety must be evaluated independently of task success, as 6-21% of successful rollouts violate the specification; (ii) fine-tuning on our suite raises safe task completion from near zero to 7.5-29.8% and engaged-and-safe behavio…

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/MANIGUARD A Benchmark and Data Suite for Specification-Grounded Safety Evaluatio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Foundation-model policies for robotic manipulation are advancing rapidly on task success, but rigorous evaluation of whether they succeed safely is still lacking. We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline. ManiGuard-Bench organizes six contact-rich household task families into 200 locked base tasks along a skill $\times$ constraint taxonomy, with safety specified independently of task success. Each task is evaluated under one in-distribution and four single-axis out-of-distribution perturbations that hold the safety specification fixed, giving 1,000 locked scenarios. Every rollout is runtime-checked by LTL$_f$-grounded automaton monitors over physics-grounded predicates rather than learned classifiers or LLM judges, in simulation and on a physical Franka platform. The pipeline pairs an automated motion-planning generator with human teleoperation, annotated by the same per-step monitor, and directly supports safety-aware fine-tuning; we release 8,000 safety-annotated demonstrations, 40 per base task. Benchmarking zero-shot and fine-tuned VLAs across more than 23,000 rollouts, we find: (i) safety must be evaluated independently of task success, as 6-21% of successful rollouts violate the specification; (ii) fine-tuning on our suite raises safe task completion from near zero to 7.5-29.8% and engaged-and-safe behavior from 16-40% to 51-72%; but (iii) a gap remains that scaling demonstrations does not close, with 21-42% of engaged rollouts still violating, two of six families below 2% safe success for every policy, and these failures persisting under distribution shift and on hardware.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17386v1
- Authors: Yiyan Peng, Philip Wang, Simon Sinong Zhan, Yiqi Lyu, Zhenyang Ni, Jixin Yan, Fiorelli Wong, Ruochen Jiao, Hang Yin, Xinyu Cao, Huajie Shao, Manling Li, Ruohan Zhang, Qi Zhu
- Published: 2026-08-18T05:27:35Z
- Age days: 0

</details>
