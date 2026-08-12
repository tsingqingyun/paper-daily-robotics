---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10366v1"
published: "2026-06-09T03:25:02Z"
age_days: 0
score: 34
created: 2026-06-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation

> [!summary] 一句话结论（基于摘要）
> Simulation has become an essential tool for evaluating and improving vision-language- action (VLA) policies, offering scalable, reproducible, and controllable alternatives to costly real-world robot evaluation.

## 关键点

- **问题**：We conduct a systematic study across multiple simulation platforms, VLA policies, tasks, and perturbation factors, measuring whether simulated evaluation preserves real-world conclusions in terms of policy ranking consistency, performance correlation, and perturbation-wise failure patterns.
- **创新点 / 方法**：Simulation has become an essential tool for evaluating and improving vision-language- action (VLA) policies, offering scalable, reproducible, and controllable alternatives to costly real-world robot evaluation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：This analysis allows us to characterize the limitations of existing simulators and identify what kinds of simulation signals are more aligned with real-world deployment.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Simulation has become an essential tool for evaluating and improving vision-language-
action (VLA) policies, offering scalable, reproducible, and controllable alternatives to
costly real-world robot evaluation. Recent simulation benchmarks have made substantial
progress on realism and diversity, yet these platforms have not been widely adopted as
reliable proxies for real-world policy evaluation. In this work, we investigate this
issue through the lens of sim-and-real correlation. We conduct a systematic study across
multiple simulation platforms, VLA policies, tasks, and perturbation factors, measuring
whether simulated evaluation preserves real-world conclusions in terms of policy ranking
consistency, performance correlation, and perturbation-wise failure patterns. This
analysis allows us to characterize the limitations of existing simulators and identify
what kinds of simulation signals are more aligned with real-world deployment. We further
examine how users should exploit simulation for policy improvement, including when
simulator-based finetuning is beneficial and how the amount of post-training data
affects sim-and-real alignment. Overall, our work provides a unified framework for
measuring, interpreting, and improving the usefulness of simulation for VLA policies,
offering guidance both for simulator designers and for practitioners who use simulation
as part of the policy development pipeline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10366v1
- Authors: Shuo Wang, Hanyuan Xu, Yingdong Hu, Fanqi Lin, Yang Gao
- Published: 2026-06-09T03:25:02Z
- Age days: 0

</details>
