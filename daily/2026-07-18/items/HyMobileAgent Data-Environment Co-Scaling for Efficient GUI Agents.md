---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14548v1"
published: "2026-07-16T04:12:42Z"
age_days: 1
score: 29
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents

> [!summary] 一句话结论（基于摘要）
> Rather than relying solely on model scaling, we develop a joint data and environment centric scaling framework to address the key bottlenecks of mobile interaction.

## 关键点

- **问题**：Our framework integrates a GUI perception flywheel combining mock-interface synthesis, rejection sampling, and icon-specific augmentation; a knowledge pipeline that transforms tutorial videos into structured interaction data; a million-scale action data pipeline deployed across more than 2000 sandbox and real-device i…
- **创新点 / 方法**：Rather than relying solely on model scaling, we develop a joint data and environment centric scaling framework to address the key bottlenecks of mobile interaction.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As large multimodal models move from understanding content to operating on digital
environments, mobile GUI has emerged as a challenging and consequential testbed for
digital embodied intelligence. Mobile agents operate under three coupled constraints:
precise perception of complex interfaces, scalable acquisition of high-quality
interaction data, and robust long-horizon decision making under compounding execution
errors. This report presents HyMobileAgent, a mobile GUI agent built on Hy3.0-VL-A3B, a
vision-native foundation model featuring native any-resolution input, an A3B-scale
deployment budget, and a 32K context window to model extended interaction histories.
Rather than relying solely on model scaling, we develop a joint data and environment
centric scaling framework to address the key bottlenecks of mobile interaction. Our
framework integrates a GUI perception flywheel combining mock-interface synthesis,
rejection sampling, and icon-specific augmentation; a knowledge pipeline that transforms
tutorial videos into structured interaction data; a million-scale action data pipeline
deployed across more than 2000 sandbox and real-device instances with automated failure
attribution; the PhoneWorld Mock App Factory, providing a resettable training
environment with 34 mock applications and over 34000 tasks; and a structured Planning-
and-Reflection mechanism with explicit dead-loop detection for reliable long-horizon
execution. We also introduce a progressive training recipe consisting of mid-training,
supervised fine-tuning, and reinforcement learning with task-specific reward designs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14548v1
- Authors: Hy Vision Team, Huawen Shen, Zhengyang Tang, Shangpin Peng, Liang Wu, Anran Zhang, Weinong Wang, Yiduo Guo, Chenxin Li, Zhengyao Fang, Yang Ding, Junyi Li, Fei Tang, Zheng Ruan, Yi Zhang, Xingran Zhou, Dingchen Yang, Sunqi Fan, Zhiyi Wan, Han Hu, Xin Lai, Pengyuan Lyu, Chengquan Zhang
- Published: 2026-07-16T04:12:42Z
- Age days: 1

</details>
