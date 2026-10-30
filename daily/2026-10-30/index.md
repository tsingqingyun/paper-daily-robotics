---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-10-30
---

# 2026-10-30 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人已经学会正常操作后，怎样在状态偏离、画面变化和任务持续增加时仍然选对动作。先读 RePO-VLA，理解如何把失败和纠正过程变成训练信号；再读 R2A，看冻结基础策略后如何借用历史运动修正轨迹；若关注人类视频如何参与动作学习，读 ThinkWorld，重点检查“预测结果吻合”能否可靠地监督动作推理。
> **趋势**：前五篇的共同线索：这些论文共同关注如何利用成功示范之外的信息：ThinkWorld 利用视频中的状态变化，RePO-VLA 利用失败与恢复轨迹，R2A 检索已有运动经验。另一个共同方向是把选择过程显式组织起来，例如 HIDRA 的专家路由和 The Trinity 的能力树，但摘要尚不足以判断这些结构各自带来的独立收益。

- **规模**：2688 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、智能体 Agent 13、多模态基础模型 12、世界模型 8、视觉语言动作模型 VLA 8、机器人学习 7、Sim2Real 2
- **源异常**：2
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](items/ThinkWorld%20World%20Imagination%20Reinforces%20Chain-of-Dynamics%20Reasoning.md)

> ThinkWorld 想让机器人从没有动作标注的人类视频里学习：先用 Chain-of-Dynamics（CoD）表示一段动作将怎样改变场景，再奖励那些能预测对实际变化的 CoD。关键是让人和机器人的经验都通过“世界怎么变了”来监督同一种动作推理表示。

- **能借鉴什么**：可以借鉴的是：缺少动作标签时，先寻找跨身体可观察的结果，再用结果约束中间动作表示。如果视频能清楚呈现物体状态变化，这条路线值得尝试；前提是预测准确确实对应可执行的运动，而不是仅仅猜中了最终画面。
- **值得读吗**：值得读方法部分，重点追踪“视频结果怎样变成 CoD 的奖励、CoD 怎样落成动作”这两处连接，它们决定整条路线是否成立。

<details><summary>实验依据</summary>

摘要报告在仿真和真机上验证了人到机器人的迁移，以及未见任务和环境下的泛化。但没有提供任务名称、基线、成功率、试验次数或消融数字。因此目前只能确认作者报告了这几类验证，无法判断收益大小，也不能确定收益主要来自人类视频、CoD 表示还是强化学习。

</details>

### 2. [RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models](items/RePO-VLA%20Recovery-Driven%20Policy%20Optimization%20for%20Vision-Language-Action%20Models.md)

> RePO-VLA 教机器人在操作偏离后接着把事情做成：把纠正轨迹单独拿出来学，再给正常、失败和恢复动作标上进展价值。部署时用固定的高价值 token 引导动作，无需额外的在线失败检测器或启发式重试。

- **能借鉴什么**：值得借鉴的是失败数据的使用粒度：一次失败执行不必整条判废，前段可能正确，后段可能已经恢复。将这些阶段区分开，才能教会策略“当前该继续、纠偏还是退出某种动作”，而不把错误和修正混学。
- **值得读吗**：优先细读数据切片和价值标签设计，因为最值得复用的是怎样把失败经历整理成有效监督，数字收益还需要结合基线与错误设置判断。

<details><summary>实验依据</summary>

摘要报告在仿真及真机双臂任务上测试，并引入带标准化错误注入的 FRBench。对抗条件下，平均成功率从 20% 升至 75%；扩大规模的真机试验最高达到 80%（均来自摘要）。但摘要未指明 20% 对应哪个基线、平均覆盖哪些任务，也没有错误类型、样本量和方差。80% 是另一项最高结果，不能与平均 75% 直接合并比较。

</details>

### 3. [The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](items/The%20Trinity%20Capability-Driven%20Recursive%20Self-Improvement%20for%20Multimodal%20Agents.md)

> The Trinity 按“任务需要什么能力”组织智能体改进：Creator 造可验证的简化练习环境，Explorer 改进可复用的执行模块，Evolver 根据执行记录重整能力分类。它希望同一能力在不同任务间复用，减少逐个造环境、逐个修改智能体执行系统的成本。

- **能借鉴什么**：这里可借鉴的做法是先找共同能力，再设计练习。如果表面不同的任务都要求检查前置条件、记住中间状态或验证执行结果，就可能用较便宜的可验证环境练习共同部分，再回原任务检验迁移。共同能力是否识别准确，是这种节省能否实现的前提。
- **值得读吗**：值得先读能力树构建和迁移实验；只有看清“共同能力”怎样被验证，才能判断复杂的演化流程是否带来了可复用收益。

<details><summary>实验依据</summary>

摘要称，演化后的 Harness 在 28 个训练基准上平均提高 34 点，在 18 个未见基准上提高 26 点，后者包含两个真实世界具身任务。摘要没有说明具体评分单位、初始对照、各基准权重和搜索成本，不能将“点”自动理解为成功率百分点。结果支持作者报告了跨基准收益，但不能据此判断每项能力或每个任务都改善。

</details>

### 4. [HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](items/HIDRA%20Hierarchical%20Dual-Routing%20Attention%20for%20Replay-Free%20Lifelong%20Imitation%20Lea.md)

> HIDRA 处理机器人持续学习时“已有专家还在，却越来越选不准”的问题。它先按指令找专家，再结合当前情境细化选择，并约束检索键的位置关系，减少新任务训练对旧选择规则的干扰。

- **能借鉴什么**：这篇提醒我们把“技能丢了”和“技能没被选中”分开检查。如果持续学习系统通过多个专家保留技能，先稳定入口的检索关系，可能比单纯增加专家更有效；这一启示适用于路由确实构成瓶颈的情形。
- **值得读吗**：如果关心持续学习中的专家误选，值得细读双层路由和键约束；若只关心最终成功率，先看资源匹配的比较是否成立。

<details><summary>实验依据</summary>

摘要报告在多个 LIBERO 套件上比较，包括任务序列更异质、语言指令被改写的困难变体；对照涵盖不重放和使用重放的基线。作者称 AUC、前向迁移更好，遗忘较低，在高干扰和语言变化下收益更强。但没有数值、基线名称及资源预算，无法量化优势。提供的证据属于仿真基准，摘要没有报告真机实验。

</details>

### 5. [Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution](items/Retrieve%20to%20Act%20Motion%20Primitive%20Graph%20Retrieval%20for%20Robust%20VLA%20Execution.md)

> Retrieve to Act（R2A）在 VLA 执行时检索训练示范中的运动片段，用历史几何经验修正当前动作。基础 VLA 保持冻结，另一个学到的门控按动作维度决定该借用多少检索结果。

- **能借鉴什么**：可借鉴的是把已有示范当作执行时可查询的运动资源，而不只当作训练材料。当主要变化来自画面、所需运动仍被历史经验覆盖时，检索几何片段可能是一条有用的补偿路径。
- **值得读吗**：值得细读查询定位、坐标对齐和逐维门控，这三处决定它能否在视觉变化时真正提供可靠的运动修正。

<details><summary>实验依据</summary>

摘要报告在 GR00T N1.7、π₀.₅ 和 StableVLA 三种架构上测试，仿真涉及 LIBERO-Plus、RoboTwin2.0-Plus。成功率绝对增幅最高为仿真 12 个百分点、真机 40 个百分点（摘要）。这些是最高增幅，不代表平均收益；摘要没有提供各模型基线成功率、扰动明细和试验次数。证据支持对所测情境扰动的改善，不能直接扩展到新动力学或新技能。

</details>

## 扫读 7 篇

- [RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](items/RoboAuto%20Autonomous%20Robot%20Program%20Search%20through%20Multi-Level%20Physical%20Understand.md) — RoboAuto 让机器人在修改控制程序前，先弄清物体怎么用、现场动作受什么限制、失败可能由什么造成。关键是把可执行技能和物理知识连起来，并主动设计小试验来排除不确定的解释。
- [TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation](items/TOPS%20Reshaping%20Flow%20Source%20and%20Transport%20for%20Multi-Task%20Robot%20Manipulation.md) — TOPS 改变流策略生成动作时“从哪里出发、沿途多快靠近目标”。它为不同任务准备不同的起始分布和变化节奏，让同一个网络用更少生成步骤完成多任务操作。
- [ActiveAlign: Aligning Egocentric Manipulation via Active Perception](items/ActiveAlign%20Aligning%20Egocentric%20Manipulation%20via%20Active%20Perception.md) — ActiveAlign 让机器人通过主动动手和触碰，校准现实场景与仿真场景的对应关系。Waving 用手部运动与可微渲染校准手眼关系，Touching 再用触觉修正物体位置，使细小目标的操作更准确。
- [Where Small Mistakes Matter: Quantifying State Criticality for Imitation Learning](items/Where%20Small%20Mistakes%20Matter%20Quantifying%20State%20Criticality%20for%20Imitation%20Learning.md) — SCRIM 给示范中的每个状态评估“这里稍微做错，后面会损失多少”。它训练一个专门制造小动作偏差的策略来找脆弱时刻，再用分数调整模仿训练权重或筛选示范。
- [VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware](items/VLA-HWBench%20Where%20the%20Time%20Goes%20When%20VLA%20Models%20Run%20on%20Edge%20Hardware.md) — VLA-HWBench 拆开测量 VLA 在机器人边缘硬件上的推理时间，发现动作如何生成比参数量更能解释快慢。它还显示，优化模型计算后，预处理和未融合算子可能成为下一处主要开销。
- [Evolving Agent Teams](items/Evolving%20Agent%20Teams.md) — Evolving Agent Teams（EAT）针对代码智能体反复修改却优化不动的问题，让主管诊断卡点、重新组织团队，并用持久文件保留历次经验。关键是让搜索方式随失败原因变化，而不只是继续生成更多代码。
- [When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies](items/When%2C%20Where%2C%20and%20What%20to%20Correct%20Human-Guided%20Adaptive%20Residual%20Correction%20for%20R.md) — Adaptive Residual Correction（ARC）让已经基本会做任务的机器人，只在容易失败的位置加上小幅动作修正。人类纠正负责提示何时介入、往哪些方向探索，最终修正动作由强化学习按任务奖励学出来。

## 其余存档 12 篇

- [AmaraSpatial-10K: A Spatially and Semantically Aligned 3D Dataset for Spatial Computing and Embodied AI](items/AmaraSpatial-10K%20A%20Spatially%20and%20Semantically%20Aligned%203D%20Dataset%20for%20Spatial%20Com.md) · 多模态基础模型 具身智能评测与基准
- [Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](items/Pretraining%20Knows%20What%2C%20Simulation%20Teaches%20How%20Compositional%20Generalization%20in%20a.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution](items/Making%20Self-Driving%20Laboratories%20Auditable%20A%20Unified%20Framework%20for%20Hybrid%20Action.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling](items/Learning%20Quality-Controllable%20Robot%20Policies%20with%20Iterative%20Hindsight%20Relabeling.md) · 机器人学习 具身智能评测与基准
- [Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](items/Zooming%20without%20Zooming%20v2%20From%20Seeing%20Details%20to%20Connecting%20Evidence%20for%20Genera.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation](items/Grasp-Then-Plan%20with%20Failure%20Attribution%20A%20Closed%20Two-Stage%20Framework%20for%20Precis.md) · 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction](items/What%20Makes%20Video%20World%20Model%20Latents%20Action-Relevant%20Prediction%20over%20Reconstruct.md) · 世界模型 具身智能评测与基准
- [Rollback: Experience Backtracking in World Models for Policy Improvement](items/Rollback%20Experience%20Backtracking%20in%20World%20Models%20for%20Policy%20Improvement.md) · 世界模型 机器人学习 具身智能评测与基准
- [cuArms: GPU-Accelerated Conflict-Based Planning for Multi-Arm Manipulation](items/cuArms%20GPU-Accelerated%20Conflict-Based%20Planning%20for%20Multi-Arm%20Manipulation.md) · 智能体 Agent
- [Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction](items/Adapting%20Video%20Models%20for%20Robot%20Control%20via%20Motion-guided%20Asymmetric%20Prediction.md) · 视觉语言动作模型 VLA 具身智能评测与基准
- [Legislating World-Model-Based Planning with Legal Reasoning](items/Legislating%20World-Model-Based%20Planning%20with%20Legal%20Reasoning.md) · 智能体 Agent 世界模型
- [Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure](items/Correction%20or%20Manipulation%20Measuring%20Epistemic%20Vigilance%20in%20LLM%20Agents%20Under%20Use.md) · 智能体 Agent 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2688
- 入选条目：24
- 回填已见条目：0
- 最高分论文：ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning
- 最高分论文发布时间：Thu, 29 Oct 2026 00:00:00 -0400
- 主要技术对象分类：具身智能评测与基准 17、智能体 Agent 13、多模态基础模型 12、世界模型 8、视觉语言动作模型 VLA 8、机器人学习 7、Sim2Real 2
- 信息源错误：1
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: HTTP Error 429: Unknown Error (after 1 attempts); recovered via 4/4 configured fallback feeds

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
