---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01595v1"
published: "2026-07-02T01:45:30Z"
age_days: 4
score: 24
created: 2026-07-06
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model

> [!summary] 一句话结论（基于摘要）
> Experiments on a real-world cloud fault injection dataset demonstrate that PASE significantly outperforms state-of-the-art methods, reducing average system recovery time by over 40% and improving fault detection accuracy in unknown fault scenarios.

## 关键点

- **问题**：As the scale and complexity of cloud-based AI systems continue to escalate, ensuring service reliability through rapid fault detection and adaptive recovery has become a critical challenge.
- **创新点 / 方法**：In this paper, we propose a paradigm shift with PASE, a Planning-Aware Semantic self-healing engine, a novel fault self- healing framework that reconceptualizes recovery as a neuro-symbolic program synthesis task.
- **证据**：Experiments on a real-world cloud fault injection dataset demonstrate that PASE significantly outperforms state-of-the-art methods, reducing average system recovery time by over 40% and improving fault detection accuracy in unknown fault scenarios.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As the scale and complexity of cloud-based AI systems continue to escalate, ensuring
service reliability through rapid fault detection and adaptive recovery has become a
critical challenge. While existing approaches integrate Large Language Models (LLMs) for
semantic understanding and Deep Reinforcement Learning (DRL) for policy optimization,
they often rely on sequential, loosely coupled architectures that underutilize the
generative and reasoning capabilities of LLMs. In this paper, we propose a paradigm
shift with PASE, a Planning-Aware Semantic self-healing engine, a novel fault self-
healing framework that reconceptualizes recovery as a neuro-symbolic program synthesis
task. PASE employs an LLM as a core Plan Synthesis Engine to generate structured
recovery plans from a library of semantic primitives. A Neural-Symbolic World Model
verifies plan feasibility through simulation, while a Meta-Prompt Optimizer, trained via
DRL, learns to generate optimal prompts that guide the LLM's planning process. This
tight reason-plan-verify-adapt loop enables dynamic, context-aware recovery strategy
generation beyond predefined action spaces. Experiments on a real-world cloud fault
injection dataset demonstrate that PASE significantly outperforms state-of-the-art
methods, reducing average system recovery time by over 40% and improving fault detection
accuracy in unknown fault scenarios. Our framework advances autonomous system management
by unifying LLM-based reasoning with model-assisted verification and meta-learned
guidance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01595v1
- Authors: Junyan Tan, Haoran Lin, Siyuan Guo, Yichen Fang, Xinyue Luo, Tianyu Shen, Zeyu Qiao
- Published: 2026-07-02T01:45:30Z
- Age days: 4

</details>
