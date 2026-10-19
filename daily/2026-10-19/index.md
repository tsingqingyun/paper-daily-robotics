---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-19
---

# 2026-10-19 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人怎样把一次执行中的信息变成下一次更可靠的动作，以及多机器人怎样在动作生成时真正协调。想理解“不更新权重也能学习”，先读 RAX，重点看程序和经验如何积累；想解决实际推理延迟，读 MambaAct，它直接改造反复运行的动作模块；想理解多臂协作，读 VLA-Fabric，再用 CoEvolve 对照“学习表示交换”和“执行后修改协作代码”的区别。
> **趋势**：前五篇的共同线索：这些论文把注意力从单个模型的能力，移向能力怎样被持续调用：通过可复用程序、持久记忆、较轻的动作模块或跨策略信息交换。现有结果也反复提醒：局部动作正确、信息更多或模型更大，都不能自动保证长任务成功。

- **规模**：2450 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 17、智能体 Agent 15、具身智能评测与基准 13、视觉语言动作模型 VLA 13、世界模型 11、机器人学习 8、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Scaling Online Exploration for Robot Agents](items/Scaling%20Online%20Exploration%20for%20Robot%20Agents.md)

> RAX 让编码智能体直接操作机器人，边试边改控制程序，再把成功经验保存成能重复运行的技能。它的学习主要发生在代码、笔记和技能库里，底层语言模型权重不变。

- **能借鉴什么**：值得借鉴的是把成功经验存成带前提条件和检查点的可执行程序。若机器人接口稳定、能承担反复试验成本，这让后续任务可以复用已验证行为，而不必把每次改进都变成权重训练。[S11、S17]
- **值得读吗**：值得细读程序形成和评估协议：真正有启发的是把在线试错变成可复用闭环代码，效果大小则必须连同输入和预算一起看。

<details><summary>实验依据</summary>

仿真覆盖多种机器人，探索和未见场景评估分开。[S12](https://arxiv.org/html/2610.22496v1#S1.p9.1) 平均领先 37.4 个百分点是五个基准相对最强既有学习策略的等权差值，不是相对所有智能体方法；其中 DexJoCo 只取双臂任务，LIBERO-Pro 对比 VPP2。换成全部任务或更强编码智能体，差值不同。[S25](https://arxiv.org/html/2610.22496v1#S13.p1.1) [S26](https://arxiv.org/html/2610.22496v1#S13.p2.1) 真机为 Franka、RB-Y1，报告五项桌面任务及长程移动操作，但节选未给逐项成功率。HumanoidArena 使用每任务三条遥操作示范，不能把全部实验统称零示范。[S12](https://arxiv.org/html/2610.22496v1#S1.p9.1)

</details>

### 2. [From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models](items/From%20Sliding%20Windows%20to%20Self-evolving%20Lifelong%20Memory%20A%20Dual-perspective%20Survey.md)

> 这篇 VLA 记忆综述讨论机器人怎样把过去的信息留到以后使用，而不只依赖眼前一小段观测。它按记忆覆盖范围和保留时间组织已有方法，但摘要没有给出各类别的具体定义。

- **能借鉴什么**：具体启示是先判断“需要记住什么、记多久”，再选存储方案。只需记住本次任务进度，与需要跨天复用操作经验，涉及不同的写入、遗忘和检索要求；把它们都处理成长上下文，容易掩盖真正需求。这是从分类轴得到的设计启示，并非摘要验证过的性能收益。
- **值得读吗**：适合先读分类定义和系统比较表，帮助明确记忆需求；仅凭摘要，还不适合据此选择实现路线。

<details><summary>实验依据</summary>

摘要报告的主要观察是：架构越复杂，开源成熟度通常越低。这是综述对代表系统的归纳，不是统一机器人实验中的性能结论。输入没有文献数量、检索时间范围、纳入标准、复杂度与成熟度评分，也没有任务、基线或成功率。因此可以把它作为寻找设计路线的地图，暂不能据此判断哪种记忆最好，或复杂架构是否导致开源不足。

</details>

### 3. [MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models](items/MambaAct%20Efficient%20Mamba%20Action%20Experts%20for%20Flow-Matching%20Vision-Language-Action.md)

> MambaAct 把 π₀.₅ 中反复生成动作的 Transformer 模块换成更小的 Mamba，并把视觉语言信息压成可重复使用的条件信号。它主要减少每次去噪的计算量，同时保留原有多步动作生成方式。

- **能借鉴什么**：若性能瓶颈在重复计算的动作头，值得先测它的耗时，再考虑替换架构。这篇说明可以保留已有视觉语言表征，通过重训较轻动作路径获得收益；“动作专家缩小十倍”则不代表整个模型或系统加速十倍。
- **值得读吗**：值得读到实现与匹配消融：加速证据清楚，但应把适用范围限定在已测动作路径和部署条件。

<details><summary>实验依据</summary>

匹配 π₀.₅ 基线、三个微调种子下，LIBERO 平均成功率从 96.72±0.14% 到 97.80±0.43%；动作专家从 311.5M 缩到 29.7M，总模型只从 3.62B 到 2.96B。[S30](https://arxiv.org/html/2610.22951v1#S4.SS1.SSS1.p1.1) H100 上去噪延迟降 64.8%，端到端降 52.9%。真机两个 UR5 任务每项用 112 条示范，OOD 每项 52 次测试；倒螺母评分从 86.5% 到 95.2%，放管从 76.9% 到 82.7%，端到端约降三分之一。真机指标含半分奖励，不能视为完整成功比例。[S24](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px4.p1.1) [S27](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px4.p3.1) [S36](https://arxiv.org/html/2610.22951v1#S4.SS1.SSS3.p1.1) [S37](https://arxiv.org/html/2610.22951v1#S4.T4) [S38](https://arxiv.org/html/2610.22951v1#S4.T4.2.1) [S39](https://arxiv.org/html/2610.22951v1#S4.T4.3.1)

</details>

### 4. [CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots](items/CoEvolve%20Self-Evolving%20Code%20Policies%20from%20Skills%20to%20Strategies%20for%20Humanoid%20Robo.md)

> CoEvolve 让两台机器人保留已有运动技能，由模型编写并修改“怎样一起搬”的协作代码。执行不合格时，它根据物理检查结果限定修改策略、角色关系或参数，再从仿真检查点重试。

- **能借鉴什么**：值得借鉴的是失败诊断应对应可控修改范围：转弯失败可能要换支撑角色，而不是只缩小转角。另一个启示是把动作被接受与任务真正推进分开统计；安全可执行的小动作，也可能让系统一直停在同一阶段。[S27]
- **值得读吗**：值得细读结构化修复与验证逻辑，作为协作代码设计案例；真机可用性仍取决于感知、精确控制和实际恢复能力。

<details><summary>实验依据</summary>

MuJoCo 中两台 G1 搬运自由支撑的 0.5kg 刚体；基础任务要求放置、释放并直立撤离。[S20](https://arxiv.org/html/2610.23288v1#S4.SS1.SSS0.Px1.p1.1) 三种模型各五次，共完成 8/15：GPT、Gemini 各 3/5，Claude 2/5。[S18](https://arxiv.org/html/2610.23288v1#S4.T1.2) [S19](https://arxiv.org/html/2610.23288v1#S4.T1) GPT 条件下四个外部基线和两个组件变体均为 0/5，完整方法 3/5。[S25](https://arxiv.org/html/2610.23288v1#S4.T2.2) 但作者说明部分比较的运行配置、预算或继续条件不同，因此结果支持系统能完成任务，不能直接证明每个组件的独立因果收益。[S7](https://arxiv.org/html/2610.23288v1#S1.p5.1)

</details>

### 5. [VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents](items/VLA-Fabric%20Learning%20Interaction%20for%20Composable%20Multi-Arm%20VLA%20Agents.md)

> VLA-Fabric 给每条机械臂保留一套完整 VLA，同时让它们在内部交换信息，共同决定动作。关键不只是共享画面，而是在共享上下文、同伴内部表示和动作生成阶段分别学习怎样配合。

- **能借鉴什么**：具体启示是按物理依赖设计通信：并行放置可能不需要很多交流，递物则需要知道对方是否能接住，共同托举还要使动作相容。结果更支持“耦合方式决定信息需求”，而不是机械臂越多就一定越需要更强通信。[S25、S34]
- **值得读吗**：值得读到交互接口和训练对照：它对“完整策略之间怎样协作”给出了实证，但规模扩展仍应按具体任务评估。

<details><summary>实验依据</summary>

真机覆盖三臂放篮、三臂接力、四臂接力和四臂套框；每任务收集 50 条示范，每种策略测试 25 次。[S26](https://arxiv.org/html/2610.23018v1#S6.p1.1) 相比独立训练策略，Full 成功率依次为 72→88%、16→56%、40→72%、36→60%。[S33](https://arxiv.org/html/2610.23018v1#S6.T3.2) 仿真还做固定权重的推理期通路移除，显示不同任务依赖不同信息；但临时关闭训练时用过的通路，与从头训练无通信策略是两种比较，不能混用。[S21](https://arxiv.org/html/2610.23018v1#S4.T1.2) [S22](https://arxiv.org/html/2610.23018v1#S4.SS2.p2.1) [S41](https://arxiv.org/html/2610.23018v1#A1.SS5.p2.1)

</details>

## 扫读 7 篇

- [NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models](items/NestedVLA%20Learning%20to%20Consolidate%20and%20Generate%20Skills%20for%20Vision-Language-Action.md) — NestedVLA 想把分别学会的机器人技能装进同一个系统，又避免合并权重时互相破坏。它用任务条件驱动超网络，为当前任务生成动作专家参数，同时保留冻结的基础 VLA 和各任务压缩后的视觉语言残差。
- [Unifying Embodied Foundation Models via a Model-to-Policy Formulation](items/Unifying%20Embodied%20Foundation%20Models%20via%20a%20Model-to-Policy%20Formulation.md) — 这篇用 model-to-policy 表述说明：无论模型输出动作 token，还是同时生成视频和动作，都可以拆成“模型产生什么”和“怎样变成机器人动作”两部分。它提供共同的数学语言，摘要没有提出新的控制算法或报告性能提升。
- [Has GPT-6-Astra Achieved Embodied Intelligence?](items/Has%20GPT-6-Astra%20Achieved%20Embodied%20Intelligence.md) — 这份报告检查 GPT-6-Astra 在机器人任务中能做什么，以及这些能力能否实际部署。它把允许示范和更多执行步数的基准测试，与真机成本及持续流逝的现实时间放在一起考察，结论是能力表现与实用性之间仍有明显距离。
- [LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence](items/LAW%20Unifying%20Language%2C%20Action%2C%20and%20World%20Modeling%20for%20Agentic%20Physical%20Intellige.md) — LAW 让语言模型持续判断子任务进度，再据此规划剩余步骤、评价和融合世界动作模型提出的动作。它的关键是让“现在该完成什么”直接参与动作选择，而不只依赖对未来画面和动作的联合预测。
- [Pedicel-Targeted Strawberry Harvesting via Imitation Learning on a Low-Cost Teleoperated Robotic Arm](items/Pedicel-Targeted%20Strawberry%20Harvesting%20via%20Imitation%20Learning%20on%20a%20Low-Cost%20Tele.md) — 这篇用 ACT 模仿人类遥操作，让低成本机械臂学习抓草莓果梗，并在 Jetson AGX Orin 上自主运行。它展示了从示范到部署的可复现流程，但摘要给出的量化结果主要是训练损失和运行频率，还不能证明采摘可靠性。
- [Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization](items/Enhancing%20Visual%20Task-Redirection%20Attacks%20on%20Vision-Language-Action%20Models%20via%20C.md) — TRACO 让视觉攻击跟着机器人实际走到的状态更新目标，并集中修正任务卡住的位置。它解决的是：攻击改变了前面的动作，后面继续照原定动作目标优化，可能越匹配越偏离攻击任务。
- [Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation](items/Look%20Before%20You%20Act%20Bridging%20Active%20Perception%20and%20Vision-Language-Action%20Models.md) — ActiveAlign 解决“相机找到了好视角，机械操作却变差”的问题：它让 VLA 在主动观察结束后的状态上重新学习接着操作。关键不是只增加可见性，而是让训练起点匹配真正的执行起点。

## 其余存档 12 篇

- [GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation](items/GRASP%20Global-Local%20Representation%20Alignment%20and%20Spatial-Physical%20Grounding%20for%20B.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors](items/Sample-Efficient%20Reinforcement%20Learning%20for%20Policy%20Improvement%20via%20Flow-Reversed.md) · 机器人学习 具身智能评测与基准
- [Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems](items/Beyond%20Success%20Rate%20Interventional%20Evaluation%20of%20Memory%20in%20Vision-Language-Actio.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration](items/InstAgent%20A%20Recursively%20Self-Improving%20Agent%20Operating%20System%20for%20Heterogeneous.md) · 多模态基础模型 智能体 Agent
- [No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?](items/No%20Eyes%2C%20No%20Problem%20What%20Does%20Touch%20Contribute%20to%20Blind%20Baoding%20Ball%20Manipulatio.md) · 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation](items/AWAM%20Active%20Trajectory-Conditioned%20View%20Imagination%20for%20Robust%20Robot%20Manipulatio.md) · 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](items/ORD-WM%20Learning%20Object-Centric%20Rigid%20Dynamics%20for%203D%20World%20Modeling%20in%20Robotic%20M.md) · 智能体 Agent 世界模型
- [Foundation Models for Autonomous Space Robotics: Architectures, Physical Adaptation, and Validation](items/Foundation%20Models%20for%20Autonomous%20Space%20Robotics%20Architectures%2C%20Physical%20Adaptati.md) · 多模态基础模型 智能体 Agent 世界模型
- [When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models](items/When%20Plans%20Change%2C%20Remember%20Replanning-Guided%20Visual%20Memory%20for%20Vision-Language-.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [TriSAR-3D and PaintFusion: A Novel Trimodal LiDAR-RGB-Thermal Dataset and Method for 3D Person Detection in Search and Rescue](items/TriSAR-3D%20and%20PaintFusion%20A%20Novel%20Trimodal%20LiDAR-RGB-Thermal%20Dataset%20and%20Method.md) · 多模态基础模型
- [Not All Actions Contribute Equally: Learning Precise Progress Estimation from Imprecise Demonstrations](items/Not%20All%20Actions%20Contribute%20Equally%20Learning%20Precise%20Progress%20Estimation%20from%20Imp.md) · 世界模型 机器人学习 具身智能评测与基准
- [MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection](items/MobileInject%20Evaluating%20Reasoning-to-Action%20Security%20of%20MLLM-Based%20Mobile%20Agents.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2450
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Scaling Online Exploration for Robot Agents
- 最高分论文发布时间：2026-10-15T18:00:28Z
- 主要技术对象分类：多模态基础模型 17、智能体 Agent 15、具身智能评测与基准 13、视觉语言动作模型 VLA 13、世界模型 11、机器人学习 8、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
