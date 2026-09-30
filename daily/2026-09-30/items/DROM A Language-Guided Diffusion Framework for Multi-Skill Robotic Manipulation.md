---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37348v1"
published: "2026-09-29T12:15:48Z"
age_days: 0
score: 34
created: 2026-09-30
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# DROM: A Language-Guided Diffusion Framework for Multi-Skill Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> DROM 用少量示范扩增出多技能轨迹，再让一个语言条件扩散策略生成所需动作。长任务由大语言模型拆成技能序列，交给统一策略执行。

## 问题

有限示范难以覆盖多种操作技能、不同空间位置和长任务组合。涉及朝向约束的动作也难通过传统规划或硬编码控制器逐项设计。

## 创新点或方法

用动态运动基元 DMP 扩增专家示范，在 Motion Planning Diffusion 上加入语言交叉注意力，输出符合指定技能的轨迹。高层 LLM 负责将请求分解为技能序列，底层统一生成模型负责各段运动。

## 证据

在 Franka Emika Panda、FANUC CRX25ia 和 MuJoCo 中验证；摘要称优于 Motion Planning Diffusion 与行为克隆，能泛化多技能并组合执行长任务。摘要未给出可核查的结果数字。

## 局限

需核查少量示范具体是多少、DMP 扩增覆盖哪些变化，以及任务成功主要依赖技能生成还是高层分解。

- **判断**：做小样本技能学习者值得读扩增和轨迹条件化方法，泛化强度需等全文量化结果再判断。

## 研究关联

对机器人学习和层级 Agent，价值是将示范扩增、语言选技能和长任务编排连起来。摘要没有学习环境演化模型，因此与世界模型研究的直接关系较弱。

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/DROM A Language-Guided Diffusion Framework for Multi-Skill Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning robust manipulation policies for diverse, long-horizon tasks from limited demonstrations remains a fundamental challenge in robotics. We present DROM, a language-guided diffusion framework that enables robots to learn, represent, and compose multiple manipulation skills within a single generative policy. DROM leverages Dynamic Movement Primitives (DMPs) to augment a small set of expert demonstrations into expressive multi-skill datasets, substantially reducing data collection while improving spatial generalization beyond the demonstrated workspace. Building upon Motion Planning Diffusion (MPD), we extend the diffusion architecture to support language-conditioned multi-skill trajectory generation through cross-attention, allowing a single model to generate skill-consistent motions for a diverse set of manipulation primitives, including orientation-sensitive behaviors that are difficult to design using conventional motion planning or hard-coded controllers. For long-horizon manipulation, a large language model decomposes high-level operator requests into executable sequences of skills, enabling natural language interaction and autonomous task execution. We validate DROM on a Franka Emika Panda robot, a FANUC CRX25ia robot, and in MuJoCo simulation across a wide range of manipulation tasks. Experimental results demonstrate that DROM outperforms Motion Planning Diffusion and Behavior Cloning baselines, achieves robust multi-skill generalization, and composes learned skills to reliably execute long-horizon manipulation tasks from natural language instructions using only a limited number of human demonstrations. Datasets, simulation environments, and more at https://github.com/automation-robotics-machines/drom.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37348v1
- Authors: Vincenzo Pomponi, Rocco Felici, Paolo Franceschi, Stefano Baraldo, Oliver Avram, Loris Roveda, Luca Maria Gambardella, Anna Valente
- Published: 2026-09-29T12:15:48Z
- Age days: 0

</details>
