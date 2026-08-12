---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18747v1"
published: "2026-05-18T17:59:03Z"
age_days: 1
score: 30
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Code as Agent Harness

> [!summary] 一句话结论（基于摘要）
> Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering.

## 关键点

- **问题**：We further outline open challenges for harness engineering, including evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across multiple agents, human oversight for safety-critical actions, and extensions to multimodal environments.
- **创新点 / 方法**：Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent large language models (LLMs) have demonstrated strong capabilities in
understanding and generating code, from competitive programming to repository-level
software engineering. In emerging agentic systems, code is no longer only a target
output. It increasingly serves as an operational substrate for agent reasoning, acting,
environment modeling, and execution-based verification. We frame this shift through the
lens of agent harnesses and introduce code as agent harness: a unified view that centers
code as the basis for agent infrastructure. To systematically study this perspective, we
organize the survey around three connected layers. First, we study the harness
interface, where code connects agents to reasoning, action, and environment modeling.
Second, we examine harness mechanisms: planning, memory, and tool use for long-horizon
execution, together with feedback-driven control and optimization that make harness
reliable and adaptive. Third, we discuss scaling the harness from single-agent systems
to multi-agent settings, where shared code artifacts support multi-agent coordination,
review, and verification. Across these layers, we summarize representative methods and
practical applications of code as agent harness, spanning coding assistants, GUI/OS
automation, embodied agents, scientific discovery, personalization and recommendation,
DevOps, and enterprise workflows. We further outline open challenges for harness
engineering, including evaluation beyond final task success, verification under
incomplete feedback, regression-free harness improvement, consistent shared state across
multiple agents, human oversight for safety-critical actions, and extensions to
multimodal environments. By centering code as the harness of agentic AI, this survey
provides a unified roadmap toward executable, verifiable, and stateful AI agent systems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18747v1
- Authors: Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei, Jiaru Zou, Mengting Ai, Zhining Liu, Ting-Wei Li, Lingjie Chen, Yanjun Zhao, Ke Yang, Bingxuan Li, Cheng Qian, Gaotang Li, Xiao Lin, Zhichen Zeng, Ruizhong Qiu, Sirui Chen, Yifan Sun, Xiyuan Yang, Ruida Wang, Rui Pan, Chenyuan Yang, Dylan Zhang, Liri Fang, Zikun Cui, Yang Cao, Pan Chen, Dorothy Sun, Ren Chen, Mahesh Srinivasan, Nipun Mathur, Yinglong Xia, Hong Li, Hong Yan, Pan Lu, Lingming Zhang, Tong Zhang, Hanghang Tong, Jingrui He
- Published: 2026-05-18T17:59:03Z
- Age days: 1

</details>
