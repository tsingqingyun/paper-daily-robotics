---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.38078v1"
published: "2026-09-29T17:36:40Z"
age_days: 0
score: 39
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation

> [!summary] 先说人话（基于摘要）
> MotorMind 让通用 VLM 看观察、下中层动作指令，再根据执行反馈调整操作。它依靠确定性控制接口、异步监控和后台记忆更新，无需为任务专门训练策略。

## 问题

专门训练的 VLA 在新任务、新环境中零样本泛化有限，也难直接吸收通用 VLM 的能力提升。已有 VLM 机器人系统又常依赖动作专家、编码智能体或额外定位工具，增加系统复杂度和成本。

## 创新点或方法

将 VLM 提议的中层动作映射为确定性机器人控制，把执行反馈持续送回推理环路，并异步监控和更新记忆。核心差异是通过动作接口连接通用 VLM 与机器人，不依赖额外学习型动作专家或定位工具。

## 证据

LIBERO-PRO 基础套件成功率为 66.7%，扰动下为 53.8%；所评测既有零样本方法分别最高为 13.3% 和 19.2%。真实 xArm6 在直接操作与人为扰动设置中平均成功率为 95%；更强 VLM 进一步提升表现。

## 局限

需核查中层动作接口内置了多少任务知识，以及真实任务覆盖范围；95% 成功率只代表摘要所述测试设置。

- **判断**：值得精读动作接口与失败分析，它直接关系到通用 VLM 能承担多大比例的机器人控制工作。

## 研究关联

对研究 VLM Agent 与 VLA 分工的人，提供了可检验的替代路线：通用模型负责中层决策，确定性控制负责落地。摘要还将剩余失败定位到视觉定位、具身推理和动作知识。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/MotorMind Scaffolding General Vision Language Models for Zero-Shot Robot Manipul.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have advanced robotic manipulation, but their zero-shot generalization in new tasks and environments remains limited, and their reliance on specialized training keeps them from benefiting directly from rapidly advancing general-purpose vision-language models (VLMs). In parallel, recent agentic robotic systems leverage VLMs for high-level reasoning or coding agents for robot control, but often depend on extensive external models and tools, introducing additional complexity and cost. This motivates us to ask: Can a general-purpose VLM itself operate a robot more like the human teleoperator by reasoning directly from observations, issuing actions, and continuously adapting to execution feedback, without relying on external models such as learned action experts, coding agents or grounding tools like SAM3? In this work, we introduce MotorMind, a robot manipulation harness that connects VLM-proposed mid-level actions to deterministic robot control and feedback, with asynchronous monitoring and background memory updates. Without task-specific policy training, coding agents, or additional grounding tools such as SAM3, MotorMind achieves 66.7% success on the base LIBERO-PRO suites and 53.8% under perturbations, compared with at most 13.3% and 19.2%, respectively, for the prior zero-shot methods we evaluate. The same interface reaches 95% average success on a real xArm6 robot across direct manipulation and human-perturbation settings. Replacing the backbone with a stronger VLM further improves performance, while the remaining failures - primarily due to visual grounding, embodied reasoning, and action knowledge - decrease as VLM capability improves. These results show that a general-purpose VLM, when equipped with an appropriate mid-level action representation and asynchronous execution harness, can perform effective zero-shot robotic manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38078v1
- Authors: Bingxuan Li, Siqi Song, Yizhuo Wu, Jiarui Yao, Tong Zhang, Huan Zhang
- Published: 2026-09-29T17:36:40Z
- Age days: 0

</details>
