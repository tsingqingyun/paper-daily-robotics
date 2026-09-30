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
url: "https://arxiv.org/abs/2609.37089v1"
published: "2026-09-29T09:16:49Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Real2Gym: Building Gyms from Videos, Bringing Skills to Robots

> [!summary] 这篇论文到底做了什么（基于摘要）
> Real2Gym 先照示范视频搭一个能实际执行动作的仿真练习场，让智能体在里面试错，把成功步骤和失败后的补救办法存下来，再带到真机使用。它积累的是可复用流程和操作代码，底层大模型权重不变。

## 问题

视频展示了动作长什么样，却没有直接给出可试错的环境、可执行的物理交互和可复用经验。具体瓶颈是如何把视觉重建接到真实控制上：场景看起来像原视频，还不够证明示范动作在其中能执行。摘要未具体分析某类既有方法的失效原因。

### 用一个例子理解

理解用例（非论文实验）：输入把积木放入盒子的视频；系统建出可交互场景，智能体运行抓放代码并记录抓空后的重试方法；真机面对盒子位置变化时，依据观测调用物体相对运动和恢复流程完成操作。

## 创新点或方法

相对直接依据输入生成执行决策，Real2Gym 加入仿真建场和经验积累阶段。Real2Sim 重建可编辑场景，对齐物体与相机，用物理引擎执行验证示范或重定向动作，并生成经过可行性检查的任务变化。智能体随后编写操作阶段代码，观察结果，把成功和失败整理成可复用经验。部署时通过共享感知控制接口使用这些经验，按当前观测调整运动。这里的经验学习不依赖底层权重更新；基础模型原有训练未说明。

### 方法如何工作

1. 从视频重建并对齐场景，得到可编辑环境，为后续动作验证提供对象和空间关系。
2. 实际运行示范或重定向动作，并检查任务变化的可行性，筛查视觉合理但物理不可执行的情况。
3. 生成并执行操作代码，根据成功与失败提炼流程和恢复策略，使试错结果能被复用。
4. 经共享接口将经验用于仿真和真机，并按当前观测适配运动，连接环境内学习与现实执行。

### 必要术语

- Real2Sim2Real：从现实建立仿真，再把其中获得的技能用于现实；本文的整体流程。
- 物体相对运动：相对目标物体而非固定世界坐标描述动作；用于随观测适配位置变化。
- 经验蒸馏：把多次尝试整理成可复用知识；本文指流程和策略整理，不必然指权重训练。

## 证据

摘要称，在构建的环境中，相对 GPT-6 Astra Direct Mode，成功率提高 16.7%，策略执行 token 约减少 74.9%；在真实 Franka 的四项任务中，执行成功率提高 33.3%。成功率增幅未说明是相对百分比还是百分点，也未给绝对成功率、试验次数及任务清单。重建高保真的结论未附具体指标；执行 token 减少也不能等同于包含建场成本的总成本减少。

## 局限

作者未明确列出剩余局限。我会重点核查：重建需多少人工协助、摩擦和接触参数如何获得、经验是否跨物体有效。整体对比无法单独证明重建、记忆或接口中哪一项造成提升；仿真收益和四项真机收益必须分别解释。

- **判断**：如果任务需要反复试错而真机尝试昂贵，这篇值得读；先查建场需要多少人工，以及仿真里练出的补救办法能否覆盖真实失败。

## 研究关联

视频除了能当模仿样本，还可以用来搭一个允许反复尝试的环境；有了它，就能在上真机前积累恢复失败的办法。判断这条路线是否值得投入，要把重建场景和前期探索的开销算进去，执行时少用 token 并不等于总成本更低。

### 下一步读哪里

下一步核查场景重建的输入要求、物理验证通过标准、失败经验怎样转为程序，以及 Direct Mode 对比是否共享感知和控制能力；特别查看全部建场与探索开销。

- **概念**：多模态基础模型 智能体 Agent 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Real2Gym Building Gyms from Videos, Bringing Skills to Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world videos provide rich demonstrations of manipulation, but turning them into reusable robot skills requires visually aligned environments, executable physical interactions, and mechanisms for learning from experience. We introduce Real2Gym, an agentic Real2Sim2Real framework that turns human and robot demonstrations into interactive simulation gyms and brings skills acquired in simulation to physical robots. The Real2Sim module reconstructs editable scenes, aligns objects and cameras with the input, validates demonstrated or retargeted actions through native physics execution, and generates task-conditioned variations with action-feasibility checks. Within these environments, the agent generates executable code for manipulation stages, observes their outcomes, and distills successful attempts and failures into reusable task procedures, object-relative motions, and recovery strategies. Through a shared perception-and-control interface, these skills guide subsequent execution in simulation and on real robots, with motions adapted to current observations and no updates to the underlying model weights. Extensive evaluations demonstrate that Real2Gym enables high-fidelity simulation environment reconstruction, outperforming GPT-6 Astra Direct Mode by 16.7% in success rate with approximately 74.9% fewer policy-execution tokens across these environments, while exceeding it by 33.3% in physical robot execution success rate across four tasks on a real Franka robot.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37089v1
- Authors: Kerui Ren, Yingxiang Xu, Kaiwen Song, Linning Xu, Bo Dai, Mulin Yu, Tao Lu
- Published: 2026-09-29T09:16:49Z
- Age days: 0

</details>
