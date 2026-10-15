---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.18792"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 42
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SEAR: Self-Evolving Agentic Robotics

> [!summary] 这篇论文到底做了什么（基于摘要）
> SEAR 让语言模型写控制代码、在线控制或自行微调 VLA，并保留有效技能和经验。它更关键的贡献是检验：后续任务做得更好，究竟来自经验积累，还是更多重试和计算时间。

## 问题

机器人智能体可以不断测试和修改方案，但成绩提高不一定代表学到了可迁移经验。反复尝试、熟悉任务、读取额外仿真状态和扩大预算都会影响结果；SEAR 要区分这些因素，并检查经验能否跨任务、模拟器和真机使用。

### 用一个例子理解

理解用例（非论文实验）：智能体输入抓取任务和测试反馈，修改控制代码并保留有效例程；新任务调用这些例程输出控制动作。再与同预算、清空经验的智能体比较，检验保留内容是否带来收益。

## 创新点或方法

与只看最终成功率相比，SEAR 让智能体保留技能与记忆，并设置控制条件检查它们是否有效。执行有三种模式：写代码作为策略、直接在控制循环中行动，以及作为研究者微调 VLA。前两种主要通过尝试和保留经验改进，第三种涉及模型训练；后续任务再使用积累的结果。具体记忆格式、筛选规则和各模式接口，摘要未说明。

### 方法如何工作

1. 给智能体任务、工具和反馈，使它能产生并测试控制方案。
2. 根据执行结果修改代码或行为，或在自动研究模式中微调 VLA，形成候选改进。
3. 保留有效技能与记忆，为后续任务提供可复用经验；筛选细节未说明。
4. 与重试、预算和信息条件的对照比较，再测跨任务与真机迁移，区分经验收益和其他因素。

### 必要术语

- 代码即策略：生成的程序控制机器人；SEAR 将其作为一种执行模式。
- 智能体即策略：模型在线参与控制决策；SEAR 用它与先写代码的方式比较。
- 保留经验：把此前有效技能或记忆带到后续任务；本文检验它是否真正有用。
- 特权仿真状态：现实感知未必能直接获得的模拟器内部信息；本文把它作为需要控制的因素。

## 证据

摘要给出的评估规模是七个前沿语言模型、330 项仿真任务、五项实体任务及累计超过四年的智能体运行时间。报告的发现包括：较难任务更受益于长会话，较易任务短尝试重开效果相当；控制代码和共享例程能够迁移，任务专用方案则不行。真机中，自行设计练习与新的人类设计场景存在表现差距。摘要未给成功率、误差或显著性，规模数字不能替代收益大小。

## 局限

作者明确报告了真机练习与新场景的表现差距，这是迁移边界。我的待核查问题是各模式能访问哪些状态和工具，以及文本模型与多模态模型的输入条件；文本模型表现接近，不能推出视觉普遍无用。

- **判断**：优先读评估控制与迁移实验，价值在于帮助辨认真正的经验收益，而具体模式选择仍需看模型和任务条件。

## 研究关联

最可借鉴的是评价设计：比较保留经验与重新开始，并控制预算和任务条件，才能判断系统是否持续学习。它也提示应区分可复用控制例程与针对单个场景的解法，后者成功不等于可迁移技能。

### 下一步读哪里

我会检查经验保留与重试对照如何匹配预算，任务难度如何定义，以及跨模拟器和真机实验中的感知接口、工具权限和新场景选择规则。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/SEAR Self-Evolving Agentic Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.18792v1 Announce Type: new Abstract: Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy (code-as-policy), acts live in the control loop (agent-as-policy), or works as a researcher that fine-tunes a vision-language-action model (auto-research). The benchmark adds controls that separate retained experience from repeated attempts, familiar tasks, privileged simulator state, larger budgets, and luck. Across seven frontier language models, 330 simulated and five physical tasks, and over four years of agent runtime, we highlight three findings. First, the learning curve of a robotic agent depends both on the overall time budget and the task difficulty relative to model capability. Harder tasks make longer sessions worthwhile; on easier tasks, re-rolling short attempts does just as well. Second, control code and shared routines transfer across tasks and simulators, while task-specific solutions do not. On a real robot, we observe a performance gap between agent-designed practice and novel human-designed scenes. Third, different models evolve more effectively in different ways. Some do best acting live, others writing code first. And a text-only model keeps pace with a comparable multimodal one: perception helps with error assessment, but agentic reasoning and tool use can matter more. We release the benchmark and codebase to support future research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.18792
- Authors: Xinyi Wang, Bangzheng Li, Hanyu Wang, Lin Zhang, Andrea Yaoyun Cui, Zhenggang Tang, Shyamal Buch, Dejia Xu
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
