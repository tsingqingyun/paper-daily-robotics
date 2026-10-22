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
url: "https://arxiv.org/abs/2610.27865"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 36
created: 2026-10-22
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇用 Agent2Act 给四个模型接上共同的观察、动作和反馈接口，在 RoboColiseum 比较机器人任务表现。共同结果是指令理解和空间推理较强，一般操作仍较弱，而且执行接口的设计也会影响成绩。

## 问题

多模态模型能谈论机器人任务，不代表能可靠控制机器人。真正难点是跨模型、任务和执行设置判断能力：如果各模型接收到的信息、可调用动作和反馈不同，成功率还会混入接口差异。

### 用一个例子理解

理解用例（非论文实验）：输入桌面观察与“把左边积木放进盒子”；模型通过共享接口选取并执行动作，收到新观察后继续决策；输出最终放置结果。相同任务下，可比较模型是否理解目标，以及反馈后能否纠正失败。

## 创新点或方法

研究用 Agent2Act 将 GPT-6 Astra、GPT-6.1 Sol、Claude Opus 5.5、Gemini 4 Argon 接入统一评测环境，在指令遵循、空间推理、一般操作和鲁棒性四条赛道上比较。摘要未报告模型再训练；主要干预发生在推理执行和评测条件。另在选定任务上比较接口组件，考察成功率、规划成本和执行时间。

### 方法如何工作

1. 把任务分成四条赛道，分别测量理解、空间判断、操作和抗扰动表现。
2. 通过 Agent2Act 提供共享观察、执行及反馈接口，减少模型比较中的接口差异。
3. 按共同任务设置和评分标准运行四个模型，得到各赛道表现。
4. 在选定任务改变接口组件，检查成功率、成本与时间如何变化；再用 Astra 案例探索额外场景。

### 必要术语

- 控制接口（harness）：连接模型决策与机器人执行的软件；Agent2Act 在本文承担这一角色。
- 鲁棒性：条件受到扰动后仍能完成任务的程度；本文将其单列为一条赛道。
- 机器人形态：机器人身体与执行器的构成；本文的 Astra 案例包含跨形态操作。

## 证据

摘要称四个模型均有较高指令遵循分数，其中三个接近满分，空间推理较强，一般操作分数低于其余三条赛道。所测配置中，Astra 在指令遵循和鲁棒性领先，Opus 在空间推理、一般操作及总分领先。没有具体分数、样本量和误差范围。Astra 另有全身协调、跨机器人形态、精细操作、灵巧手和真机案例；这些案例不能替代四模型在所有场景的统一比较。

## 局限

作者把排名限定在所测配置内，这个边界必须保留。不同赛道分数的量尺和难度如何校准需要核查，不能仅凭分数高低量化理解与执行之间的差距。真机案例也不足以建立四模型的真机排名。

- **判断**：值得读任务定义和接口组件实验，模型名次只适合连同配置一起参考；最有用的是找到理解转成可靠动作时卡在哪里。

## 研究关联

值得借鉴的是同时看模型与接口：统一接口帮助比较模型，接口组件实验则提醒我们，最终成功率也是系统设计的结果。若模型理解正确却反复执行失败，应检查动作接口和反馈是否足以支撑修正。

### 下一步读哪里

我会核查四赛道评分规则、模型输入和动作预算是否一致、失败如何归类，再看组件比较具体改了什么。对真机部分，应检查案例数量、重复次数以及与主评测设置的差异。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/Frontier LLMs Enter the World of Robotics A Cross-Model Evaluation on RoboColise.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.27865v1 Announce Type: new Abstract: Recent studies have explored the potential of multimodal large language models for robot control, yet the models' embodied capabilities remain insufficiently characterized across models, tasks, and execution settings. We conduct a multidimensional comparative evaluation on RoboColiseum across four tracks: Instruction Following, Spatial Reasoning, General Manipulation, and Robustness. We implement Agent2Act, a control harness that integrates GPT-6 Astra, GPT-6.1 Sol, Claude Opus 5.5, and Gemini 4 Argon into the evaluation environment through shared observation, action execution, and feedback interfaces. Under common task settings and scoring criteria, all four models exhibit a consistent capability profile: high instruction-following scores, with three approaching perfect performance; strong spatial reasoning; and general manipulation scores below those of the other three tracks. Within the evaluated configurations, Astra leads instruction following and robustness, while Opus leads spatial reasoning, general manipulation, and overall performance. These results reveal complementary strengths across models and a persistent gap between task understanding and reliable physical execution. Component comparisons on selected tasks further show that harness design affects task success, planning cost, and execution time. Additionally, case studies with Astra examine whole-body coordination, manipulation across robot embodiments, precision manipulation, dexterous-hand manipulation, and real-robot tasks, providing further insight into the model's capabilities and limitations across embodied tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.27865
- Authors: Da Huang, Jichao Wang, Junhui Wu, Tong Ran, Linting Guo, Siying Zhang, Chuang Men, Sukai Wang, Yue Zhou, Maoqing Yao, Mo Wu
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
