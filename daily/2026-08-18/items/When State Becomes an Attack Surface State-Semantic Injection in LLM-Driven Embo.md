---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16806v1"
published: "2026-08-17T17:02:07Z"
age_days: 0
score: 35
created: 2026-08-18
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents

> [!summary] 一句话结论（基于摘要）
> Traditional LLM Agents typically obtain information through webpages, documents, databases, or external tools and generate corresponding invocation sequences according to user goals; when this technology is further integrated with robotic systems, large langu…

## 关键点

- **问题**：Large Language Models (LLMs) have demonstrated capabilities in in-context learning, task decomposition, step-by-step reasoning, and code generation, driving their gradual evolution from text generation models into the core of agents capable of perceiving environments, invoking tools, and executing tasks.
- **创新点 / 方法**：Traditional LLM Agents typically obtain information through webpages, documents, databases, or external tools and generate corresponding invocation sequences according to user goals; when this technology is further integrated with robotic systems, large language models begin to undertake functions such as task underst…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/When State Becomes an Attack Surface State-Semantic Injection in LLM-Driven Embo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large Language Models (LLMs) have demonstrated capabilities in in-context learning, task decomposition, step-by-step reasoning, and code generation, driving their gradual evolution from text generation models into the core of agents capable of perceiving environments, invoking tools, and executing tasks. Traditional LLM Agents typically obtain information through webpages, documents, databases, or external tools and generate corresponding invocation sequences according to user goals; when this technology is further integrated with robotic systems, large language models begin to undertake functions such as task understanding, high-level planning, and behavioral decision-making. SayCan combines the task reasoning capability of language models with the affordances of robotic skills, while Code as Policies and ProgPrompt generate robot task plans through policy code and programmatic prompting, respectively, and VoxPoser uses language models and vision-language models to construct three-dimensional value maps to guide robotic manipulation \cite{6,7,8,9}. Vision-language-action models such as PaLM-E, RT-2, and GR00T N1 further strengthen the connection among language, visual perception, and robotic actions \cite{10,11,12}. In such LLM-driven embodied agents, the model not only needs to understand user instructions, but also needs to combine scene states, object attributes, spatial relations, and execution feedback to complete task grounding, and then hand the generated action plan to skill libraries, motion planners, or controllers for execution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16806v1
- Authors: Jiawei Liu, Jiacheng Guo, Tian Zhang, Yiwei Xu, Juan Wang, Jinlin Fan, Bowen Xiao, Chi Guo, Keyan Guo, Hongxin Hu
- Published: 2026-08-17T17:02:07Z
- Age days: 0

</details>
