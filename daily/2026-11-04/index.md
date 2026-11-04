---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-11-04
---

# 2026-11-04 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：复杂机器人任务失败时，究竟该补哪一层——遮挡推理、工具调度、空间约束，还是动作生成？想理解“先想几步再动”，读 SCOUT，重点看隐藏几何如何进入搜索；想判断现成模块能否支撑通用机器人，读 MAESTRO，重点看工具库与调度机制的消融；想从较小的策略改动入手，读 ODE Policy，重点核查连续动作生成的收益和比较条件。以下均依据提供的摘要解读，未获得正文节选。
> **趋势**：前五篇的共同线索：这组论文共同提示：复杂任务的改进可以来自对决策过程加入明确结构，例如物体关系、工具调用、空间能量、动作动力学或意图表示。它们分别改变不同环节，摘要中的结果尚不能支持这些做法能够直接叠加，或彼此替代。

- **规模**：4875 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 19、具身智能评测与基准 18、视觉语言动作模型 VLA 18、智能体 Agent 15、机器人学习 10、世界模型 9、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts](items/SCOUT%20Planning%20under%20Occlusion%20via%20Object-Centric%20World%20Model%20Rollouts.md)

> SCOUT 让机器人在杂乱场景里先推测被挡住的空间，再试算搬动物体的后果。LLM 负责提出少量候选动作，物体级世界模型和树搜索负责检查这些动作是否真的有助于接近目标。

- **能借鉴什么**：值得借鉴的是把“生成可考虑的动作”和“验证动作后果”拆开。当候选组合很多、错误又主要来自遮挡几何时，可以让语言模型压缩搜索范围，再用更贴近物理状态的预测筛选。
- **值得读吗**：值得读方法和误差分析，重点判断物体关系是否真正改善搜索，以及收益能否抵偿规划时间。

<details><summary>实验依据</summary>

摘要报告 Reveal、Placement 两类任务，对比 VLA 策略、具身智能体和 3D 世界模型，称长时序遮挡推理任务收益明显；还报告了杂乱货架上的真机验证。但未给出具体基线名称、评价指标、成功率、样本量和规划耗时。因此能确认作者报告了跨方法比较及真机测试，尚不能量化优势或判断实时性。

</details>

### 2. [MAESTRO: Orchestrating Robotics Modules with Coding Agents for Zero-Shot Generalist Robots](items/MAESTRO%20Orchestrating%20Robotics%20Modules%20with%20Coding%20Agents%20for%20Zero-Shot%20Generali.md)

> MAESTRO 让视觉语言模型写机器人程序，调用已有的感知、规划和控制工具完成任务。它的关键不只是工具多，而是执行后检查结果，失败后重新规划。

- **能借鉴什么**：这篇让“模块能力如何变成整机能力”成为可检验的问题。已有感知和控制工具时，值得同时设计调用流程、结果检查和失败恢复，而非仅增加函数接口。
- **值得读吗**：值得细读调度机制和工具扩充消融，它们比单个成功演示更能解释这条路线何时有效。

<details><summary>实验依据</summary>

摘要称，在其桌面对比中，不调用 VLA 工具的 MAESTRO 零样本达到或超过先进 VLA，并展示多种移动操作任务。消融以平均任务进展衡量：完整调度机制下，扩充工具库有帮助；缺少该机制时，加工具不能可靠改善进展。摘要未提供具体任务清单、基线型号、分数和重复次数。跨试次改代码、借 VLA 加速及生成数据属于案例展示，证据强度需与主比较分开。

</details>

### 3. [OmniGuide: Universal Spatial Guidance Fields for Enhancing Generalist Robot Policies](items/OmniGuide%20Universal%20Spatial%20Guidance%20Fields%20for%20Enhancing%20Generalist%20Robot%20Polic.md)

> OmniGuide 把不同来源的空间建议写成三维空间里的“吸引”和“排斥”能量，再用它们引导 VLA 采样动作。这样，已有策略可以借助额外模型提供的空间或语义判断，选择更合适的动作。

- **能借鉴什么**：具体启示是：外部知识未必都要重新灌进策略参数，也可以先转换成动作生成能使用的约束。当任务要求能被表达为“靠近哪里、避开哪里”时，这种统一接口值得尝试。
- **值得读吗**：值得读能量构造与采样实现；方法是否实用，取决于指导信号能否低成本转成准确约束。

<details><summary>实验依据</summary>

摘要报告仿真和真机实验，覆盖多种指导来源，涉及 π₀.₅、GR00T N1.6 等通用策略，以成功率和安全率评价，称均有明显改善；与针对特定来源设计的既有方法相比达到或超过其表现。未给出数值、任务明细、安全判定标准或推理耗时，因此尚不能判断收益大小、代价和适用任务边界。

</details>

### 4. [ODE Policy: Robot Learning via Action Dynamics, Not Actions](items/ODE%20Policy%20Robot%20Learning%20via%20Action%20Dynamics%2C%20Not%20Actions.md)

> ODE Policy 学习动作应当怎样变化，再从上一个动作积分得到下一个动作。它把动作连续性直接放进生成过程，并用一个轻量分支保留同一任务的多种动作方式。

- **能借鉴什么**：值得借鉴的是把时间连续性作为输出结构，而不只靠示范或额外惩罚学习。如果动作抖动和生成成本是主要问题，可以先检查动作头的参数化方式，而不必首先扩大主干模型。
- **值得读吗**：值得深入读动作场定义和公平对比设置，因为它改动的位置明确，且摘要给出了学习速度与执行速度两类可检验收益。

<details><summary>实验依据</summary>

摘要称覆盖单臂、双臂、灵巧操作、行走和行走操作，与 14 个基线比较。在模仿学习中，相对 flow matching，训练一个 epoch 后，成功、泛化和模式均衡分别为 5.9、5.4、3.9 倍，动作生成速度为 10.8 倍；这些均来自摘要，不能视为所有实验的统一倍数。摘要另报告 14 项真机任务中成功率最高，并称在 RL 中加速 SuperMimic、使动作更平滑。各指标定义、绝对值及 RL 提速数值未提供。

</details>

### 5. [GazeVLA: Learning Human Intention for Robotic Manipulation](items/GazeVLA%20Learning%20Human%20Intention%20for%20Robotic%20Manipulation.md)

> GazeVLA 用人的注视线索表示“正在关注和准备操作什么”，帮助机器人从人类示范学习。推理时，它用思维链式过程连接意图与动作，尝试缩小人和机器人身体不同带来的迁移困难。

- **能借鉴什么**：可借鉴的是迁移表示的选择：人和机器人可能无法共享动作坐标，却可以共享当前关注的对象或操作目标。寻找这种既连接任务、又贴近动作的中间表示，可能比直接对齐肢体运动更合适。
- **值得读吗**：值得先读意图表示与注视消融；只有确认收益确实来自可迁移的注视信息，才能判断方法是否适合复用。

<details><summary>实验依据</summary>

摘要报告仿真与真机实验，称在不同身体形态下完成长时序、精细任务，相比基线表现更好，并能迁移到未见设置。但没有列出机器人型号、任务、基线名称、评价指标或数值。因此现有材料只能支持作者报告了这些比较，不能量化注视贡献，也不能分离意图建模与推理过程各自的作用。

</details>

## 扫读 7 篇

- [RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions](items/RynnVLA-Latent%20Scaling%20Robotic%20Manipulation%20Foundation%20Models%20with%203D-Grounded%20L.md) — RynnVLA-Latent 想让没有机器人控制记录的视频也能用于训练机器人：先用 RynnLAM 从画面变化中提取带三维运动信息的潜在动作，再训练策略预测这些动作，最后适配具体机器人的控制指令。关键是尽量把物体运动与相机运动分开，避免把镜头变化学成操作动作。
- [OmniPiano: Diverse Dexterous Piano-Playing Challenges for Standard, Robust, Safe, and Multi-Agent RL](items/OmniPiano%20Diverse%20Dexterous%20Piano-Playing%20Challenges%20for%20Standard%2C%20Robust%2C%20Safe%2C.md) — OmniPiano 把机器人弹钢琴做成一套可配置的测试任务：从一只到五只 Shadow Hand，在同一任务家族里分别检查弹奏、抗扰动、安全和多手合作。它的主要贡献是统一比较条件，让“弹得对”和“受干扰后还能安全合作”可以分别检验。
- [MOST: Memory of Object States and Task Progress for Long-Horizon Mobile Manipulation](items/MOST%20Memory%20of%20Object%20States%20and%20Task%20Progress%20for%20Long-Horizon%20Mobile%20Manipulat.md) — MOST 让机器人记住“东西变成了什么状态、任务做到哪一步”，而不只是保留过去看过的画面。它用物体状态和子任务进度监督内部记忆，再直接用这份记忆生成动作，帮助机器人处理已经离开视野的信息。
- [VLALagBench: Understanding When and Why VLA Inference Latency Matters](items/VLALagBench%20Understanding%20When%20and%20Why%20VLA%20Inference%20Latency%20Matters.md) — VLALagBench 研究机器人“想得慢一点”究竟会损失多少成功率，并发现损失取决于任务、目标速度和策略。它还用少量校准数据拟合成功率，让推理系统可以按实际延迟和吞吐量选择执行配置。
- [ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning](items/ScheduleGen%20Demonstration%20Generation%20via%20Skill%20Scheduling%20for%20Multi-Arm%20Imitatio.md) — ScheduleGen 从少量示范生成多臂操作数据，但不只是改写各只手的运动：它把动作规划和技能排程一起处理，让多臂约束参与决定动作如何安排。目标是减少生成示范中的危险或失败行为，再用这些示范训练策略。
- [OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation](items/OpenHLM%20An%20Empirical%20Recipe%20for%20Whole-Body%20Humanoid%20Loco-Manipulation.md) — OpenHLM 要让人形机器人看图、听指令后协调全身行动，关键是开放全身关节的示教接口，再结合已有 VLA 预训练和 HuMI 数据共同训练。它的主要贡献是一套逐项比较得出的实践配方。
- [LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks](items/LOGIV%20Graph-Verified%20Execution%20with%20Causal%20Local%20Repair%20for%20Long-Horizon%20Robot%20T.md) — LOGIV 解决长任务中“前面做成的事后来又失效”的问题：把后续动作依赖的条件写进任务图，执行时持续检查，出错后沿依赖关系安排修复。它放在已有动作策略之上，无需增加可训练组件。

## 其余存档 12 篇

- [When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem](items/When%20Delay%20Meets%20Drift%20Physical%20Safety%20of%20Robot%20Foundation%20Models%20Is%20a%20Cross-Lay.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Tactile MNIST: Benchmarking Active Tactile Perception](items/Tactile%20MNIST%20Benchmarking%20Active%20Tactile%20Perception.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge](items/ActionFlow%20A%20Pipelined%20Action%20Acceleration%20for%20Vision%20Language%20Models%20on%20Edge.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- [TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning](items/TouchScale%20500%20Hours%20of%20Human%20Vision%20and%20Touch%20for%20Visual-Tactile%20Learning.md) · 具身智能评测与基准
- [Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](items/Auriga%20Technical%20Report%20A%20Task-Agnostic%20Agent%20Harness%20for%20Zero-Shot%20Embodied%20Man.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Vision-Language Models Are Joint Denoisers in Robotic Action Generation](items/Vision-Language%20Models%20Are%20Joint%20Denoisers%20in%20Robotic%20Action%20Generation.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](items/RoboColosseum%20Evaluating%20Physical%20Intelligence%20at%20Scale%20In-The-Wild.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies](items/Beyond%20Policy%20Patches%20Distilling%20RL%20Specialists%20into%20Vision-Language-Action%20Poli.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models](items/Route-Guided%20CBF-QP%20Repair%20for%20Safe%20Vision-Language-Action%20Models.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation](items/Dynamics-Aware%20Meta-Imitation%20for%20Generalization%20to%20Unseen%20Robotic%20Manipulation.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习
- [Labference: Benchmarking the Reasoning-Action Connection in Robotic Laboratories](items/Labference%20Benchmarking%20the%20Reasoning-Action%20Connection%20in%20Robotic%20Laboratories.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking](items/TRACE%20Target-State%20Risk-Aligned%20Conditional%20Execution%20for%20Embodied%20Tracking.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：4875
- 入选条目：24
- 回填已见条目：0
- 最高分论文：SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts
- 最高分论文发布时间：Tue, 03 Nov 2026 00:00:00 -0500
- 主要技术对象分类：多模态基础模型 19、具身智能评测与基准 18、视觉语言动作模型 VLA 18、智能体 Agent 15、机器人学习 10、世界模型 9、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: Remote end closed connection without response (after 1 attempts); recovered via 4/4 configured fallback feeds

</details>
