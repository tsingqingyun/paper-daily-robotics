---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29596v1"
published: "2026-08-30T06:36:42Z"
age_days: 2
score: 32
created: 2026-09-01
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Towards a Systems Foundation for Agentic Skills: Architecture, Lifecycle, and Security

> [!summary] 先说人话（基于摘要）
> 这是一篇 agentic skills 系统化论文：把技能定义为连接高层规划与确定性执行环境的外置程序知识，并用九阶段生命周期统一讨论发现、编写、检索、执行、适应、评测和安全。

## 这篇到底在做什么

- **卡在哪里**：长程 LLM Agent 面临可靠性、上下文消耗和执行稳定性瓶颈，单体提示和无状态工具调用难以扩展；技能生态又缺少统一架构、生命周期和安全治理框架。
- **关键解法**：论文不提出单个控制模型，而是给出参考架构：技能以可复用、可执行、可移植制品存在，并在自主发现、表示、存储、路由、编排、执行修复、终身适应、实证评估和安全治理九个阶段流转，同时分析市场、注册表与攻击面。
- **拿什么证明**：摘要只报告完成了形式化、架构划分、实现分类和开放问题梳理，没有实验、基准或可核查结果数字。

## 值不值得读

- **和你的研究有什么关系**：对具身 Agent 研究者，它有助于设计机器人技能的封装、路由、验证与治理层；对世界模型或低层机器人学习没有直接算法收益。
- **先别急着信**：论文的“基础范式”定位主要是概念性主张，需核查分类是否覆盖真实系统，以及是否有可执行规范或实证比较支撑。
- **判断**：适合做 Agent 系统或技能平台的人通读并用作设计检查表；寻找新机器人算法或定量突破者可只读架构与安全章节。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/Towards a Systems Foundation for Agentic Skills Architecture, Lifecycle, and Sec.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous large language model (LLM) agents increasingly face reliability, context consumption, and execution stability bottlenecks when deployed on complex, long-horizon tasks. While monolithic prompt engineering and stateless tool-calling paradigms struggle to scale, the field is rapidly converging toward \emph{agentic skills}: modular procedural abstractions that externalize execution knowledge into reusable, executable, and portable artifacts. This paper establishes a unified systems foundation and reference architecture for the agentic skills ecosystem. We formalize skills as externalized procedural knowledge bridging high-level cognitive planning with deterministic execution environments, and systematically delineate the architecture across a nine-stage lifecycle: autonomous discovery, authoring and representation formats, memory storage, dynamic retrieval and routing, composition and orchestration, execution and repair, lifelong adaptation, empirical evaluation, and security governance. We further examine marketplace dynamics, public registries, and emerging adversarial threat vectors, alongside runtime verification and defense mechanisms. Finally, we categorize system implementations across software engineering, operating system navigation, embodied robotics, and scientific discovery, while highlighting critical open challenges in continual learning and benchmark realism. This work establishes agentic skills as a foundational paradigm for building scalable, robust, and verifiable autonomous language agents.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29596v1
- Authors: Sanket Badhe, Deep Shah, Priyanka Tiwari, Nehal Kathrotia
- Published: 2026-08-30T06:36:42Z
- Age days: 2

</details>
