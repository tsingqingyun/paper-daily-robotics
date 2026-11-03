---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-03
---

# 2026-11-03 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看一个问题：怎样让模型的知识真正改善机器人执行，而不被延迟、错误反馈或动作接口抵消。先读 CaPtain，看长串操作只有最终成败时，怎样把训练信号分到具体动作；再读 REA，看慢推理怎样与快控制协作，以及哪些收益其实来自事先选对策略；最后读 TRACE，看任务成功率提高后，怎样查出并修补随之增加的碰撞风险。
> **趋势**：前五篇的共同线索：这几篇共同强调：模型之外的信息接口也决定执行效果，包括每次调用的物理回执、策略交接时的完成判断，以及动作执行前的目标风险。另一条有依据的趋势是把丰富监督放在训练阶段，再让部署时的表示或控制回路保持简洁；但各篇实验支持的迁移范围差别很大。

- **规模**：2509 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、多模态基础模型 14、世界模型 10、智能体 Agent 10、视觉语言动作模型 VLA 8、机器人学习 5
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents](items/CaPtain%20A%20Pipeline%20for%20Post-Training%20Code-as-Policy%20Robot%20Agents.md)

> CaPtain 让小视觉语言模型自己写代码完成抓取和放置，而不是只调用现成抓取技能。关键是训练时让一个能读取仿真物理状态的评价器，判断每次调用是否让任务更接近成功；部署时则只保留看图、写代码和读取执行回执的模型。

- **能借鉴什么**：值得借鉴的是把“决策时能看见什么”和“训练时怎样判断进展”分开。只要仿真物理状态可靠，就可以用它教会基于图像的策略，而不必让部署系统依赖这些隐藏信息。
- **值得读吗**：值得深入读信用分配和评价器输入设计：它最有借鉴性的地方，是怎样避免把长过程中的观察、耗时和真正物理进展混为一谈。

<details><summary>实验依据</summary>

在留出的 LIBERO 初始状态上，240 回合的 host 成功率由 SFT 的55.4%升至73.8%，strict 成功率由52.1%升至67.5%。LIBERO-PRO 三套测试为78.5%，全部四套为68.6%，二者不能混用。[S22](https://arxiv.org/html/2610.40799v1#S4.T1.15) 对几种扰动仍有增益，支持其超出训练初始布局的适应能力；但这些任务家族的成绩不等于任意机器人迁移。真机完成任务仅有定性描述，节选未给回合数和成功率。[S7](https://arxiv.org/html/2610.40799v1#S1.p5.1)

</details>

### 2. [REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control](items/REA%20A%20Routed%20Embodied%20Agent%20Runtime%20for%20Asynchronous%20Brain-Cerebellum%20Control.md)

> REA 解决的是慢模型与快控制器怎样配合：先根据开发回合选好策略，让它按自己的速度执行，在交接处再决定是否换策略。它用历史成功记录、完成判断和共同恢复预算，减少等待、漏检失败及无休止重试。

- **能借鉴什么**：如果已有几种能力互补的控制器，可以先测清“什么任务交给谁”，再考虑增加在线推理。REA 的主结果表明，在这个策略库里，事先选择可靠且较短的程序，已经解释了大部分收益。
- **值得读吗**：值得细读路由消融和对齐协议；主结果支持减少不必要在线推理，但不能把所有收益归给异步视觉判断。

<details><summary>实验依据</summary>

LIBERO-Pro 的60任务、3,000测试回合中，REA-M 为95.9%，最佳单方法为94.7%，每次成功步数从1,343降至1,003。[S26](https://arxiv.org/html/2610.42053v1#S4.T1.11) [S27](https://arxiv.org/html/2610.42053v1#S4.SS2.p1.1) 但该主结果使用异常门，不包含视觉判断；仅路由记忆已至少达到95.7%。视觉判断在另一个 ASPIRE 对照中增加3.1个百分点，却需2.1倍的每次成功耗时。[S29](https://arxiv.org/html/2610.42053v1#S4.SS4.p1.1) 独立100回合 RoboTwin 研究中，VLA和VLA+代码分别为84%、86%，单 VLA 为80%。[S8](https://arxiv.org/html/2610.42053v1#S1.SS0.SSS0.Px1.p1.1)

</details>

### 3. [Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space](items/Nexus-VLA%20Bridging%20Human%20and%20Robot%20Experiences%20via%20a%20Shared%20Hierarchical%20Semanti.md)

> Nexus-VLA 用人类视频帮助机器人学动作，但不要求把人手动作硬变成机器人关节动作。它把“做什么、操作哪里、怎样移动、怎样接触”共同压入一个内部表示，再让这个表示直接参与连续动作生成。

- **能借鉴什么**：值得借鉴的是为跨来源数据寻找多层、可共用的监督，再让最终动作目标约束表示。这样既不用假装人手就是机器人关节，也不必把语义预测变成部署时额外执行的一串步骤。
- **值得读吗**：值得读到动作表示和损失实现：真正关键的是人类数据怎样进入同一个动作学习目标，以及缺失的机器人控制标签怎样被正确屏蔽。

<details><summary>实验依据</summary>

主仿真覆盖 RoboCasa-GR1 的24项人形操作任务，使用24,000条机器人轨迹和21,446段筛选后人类视频；摘要报告成功率80.5%。[S22](https://arxiv.org/html/2610.42021v1#S4.SS1.p1.1) [S23](https://arxiv.org/html/2610.42021v1#S4.SS1.p2.1) 更能解释机制的是消融：相同层级监督下，独立表示改成统一潜在表示，成功率由76.92%升至78.25%；固定该设计再加人类共训，升至80.17%。[S25](https://arxiv.org/html/2610.42021v1#S4.SS3.p1.1) [S26](https://arxiv.org/html/2610.42021v1#S4.SS3.p2.1) 真机标准及四种 OOD 设置平均74.0%，但节选未给试验数。[S30](https://arxiv.org/html/2610.42021v1#S4.SS6.p2.1) 主结果与消融的不同数值应分别理解。

</details>

### 4. [When the Past Shapes Action: Understanding Embodied Memory](items/When%20the%20Past%20Shapes%20Action%20Understanding%20Embodied%20Memory.md)

> 这篇综述把机器人记忆问题改写成：下一次决策需要哪条过去的信息，它还是否有效，怎样才能取出来。它按需求和存储方式两条线梳理方法，并提醒读者：任务做得久、总成功率高，都不足以证明系统真的使用了记忆。

- **能借鉴什么**：最实用的启示是先构造一个“没有过去就无法答对”的决定，再设计记忆。否则增加历史输入带来的收益，可能来自更多计算、额外训练或任务进度提示，而不是保存了关键经历。
- **值得读吗**：值得重点读评测部分，并据此检查自己的“记忆有效”结论；它的主要用途是让历史依赖变得可检验，而不是推荐某个万能存储模块。

<details><summary>实验依据</summary>

节选提供的是机制和评测协议分析，没有该综述自己的成功率对照。比如固定窗口内仍能看到线索，不证明线索移出窗口后还能记住；一次预测多步动作，也不扩大可回看的历史。[S14](https://arxiv.org/html/2610.41688v1#S2.SS2.p2.1) [S15](https://arxiv.org/html/2610.41688v1#S2.SS2.p3.1) 作者建议保持当前观察和目标相近，改变合理的先前经历，使正确动作随之改变，再匹配骨干、接口和观察权限比较。[S23](https://arxiv.org/html/2610.41688v1#S6.p1.1) 这给出较强的验证原则，但不是新记忆结构优于旧结构的实证。

</details>

### 5. [TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking](items/TRACE%20Target-State%20Risk-Aligned%20Conditional%20Execution%20for%20Embodied%20Tracking.md)

> TRACE 发现，把跟人策略训练得更坚持，可能让原本丢人的失败变成撞人的失败。它保留训练后的策略，仅在目标状态显示高风险时缩小下一步平移，让机器人继续转向观察，同时减少危险接近。

- **能借鉴什么**：当 RL 延长了任务坚持时间，应检查失败类型是否只是发生转移。若风险集中在少数状态，可以尝试保留主策略、单独校准执行门控；这里的证据比“整体慢一点更安全”更具体。
- **值得读吗**：值得细读配对评测和减速对照：它既说明怎样修补策略副作用，也示范了怎样排除评测波动与普通减速这两种替代解释。

<details><summary>实验依据</summary>

在修正后的 EVT-Bench 评测器、相同1,380回合和五次训练运行下，干扰跟踪碰撞率从 SFT 的11.01%升至 PPO 的13.78%，加 TRACE 后降至9.83%；配对成功率和跟随率另增2.03、2.14个百分点。[S15](https://arxiv.org/html/2610.41275v1#S4.SS1.SSS0.Px3.p1.1) [S16](https://arxiv.org/html/2610.41275v1#S4.SS2.p1.1) [S17](https://arxiv.org/html/2610.41275v1#S4.T1.1.1) [S18](https://arxiv.org/html/2610.41275v1#S4.T1) 同等减速、随机介入和延迟风险控制未复现改善，支持介入时机的作用。[S19](https://arxiv.org/html/2610.41275v1#S4.SS4.SSS0.Px1.p1.1) 同时评测的碰撞下降为3.77个百分点，相同策略空对照仅0.29个百分点。[S9](https://arxiv.org/html/2610.41275v1#S1.I1.i3)

</details>

## 扫读 7 篇

- [STAR: Steering Action Representations during Inference](items/STAR%20Steering%20Action%20Representations%20during%20Inference.md) — STAR 要解决的是：VLA 越接近输出动作，内部表示反而可能丢掉与任务有关的物体信息。它不重新训练模型，而是在推理时平滑后几层的表示更新，让较早层中与物体有关的更新方向继续影响最终动作。
- [From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation](items/From%20Teleoperation%20to%20Long-Horizon%20Dexterity%20Evaluating%20Visuomotor%20Skills%20and%20Of.md) — 这篇研究用大量真机试验追问：五指手能否抓住并插入 RJ45 接头，究竟由哪些设计决定？结果把重点指向观测与动作的表示方式，同时发现验证损失和多数离线指标难以预测实际成功。
- [Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation](items/Learning%20from%20Physical%20Experience%20Context-Space%20Adaptation%20for%20Robotic%20Manipulat.md) — LEXP 让机器人把做过的事转化成下次行动可用的经验：解释执行证据，提炼带适用条件的教训，再把相关教训送回行动上下文。它固定模型权重和动作接口，通过改变模型接下来看到的信息来适应任务。
- [Sensorium: An Open-Source Multimodal Data Collection and Curation Library for Embodied Surgical AI](items/Sensorium%20An%20Open-Source%20Multimodal%20Data%20Collection%20and%20Curation%20Library%20for%20Emb.md) — Sensorium 把手术机器人及传感器的数据采集、处理、标注和数据集整理接成一条可配置流程。它是数据工具库，目标是降低不同硬件配置下反复搭建采集流程的成本。
- [Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos](items/Movens-Zero%20Scaling%20Humanoid%20Motion%20Foundation%20Models%20with%20Large-Scale%20Human%20Vid.md) — Movens-Zero 把网络人类视频转成经过机器人动作处理的数据，再训练同一个动作专家根据文字、语音、音乐或视频生成运动。执行时，它把相互重叠的动作片段接起来，并持续接收新指令和机器人状态，以支持连续控制。
- [OpenVIO: A Versatile Open-Source Visual-Inertial Odometry System](items/OpenVIO%20A%20Versatile%20Open-Source%20Visual-Inertial%20Odometry%20System.md) — OpenVIO 是一套把相机与惯性测量结合起来、估计机器人自身运动的开源系统，支持针孔、鱼眼和拼接后的 360° 图像。摘要强调的是可使用、可研究的完整系统，而没有给出一种新估计算法的具体机制。
- [Hierarchical World Models with Implicit Dynamics](items/Hierarchical%20World%20Models%20with%20Implicit%20Dynamics.md) — ID-WM 把长任务规划拆成“哪些中间状态可以到达”和“用什么动作到达”两件事。高层先挑可行的状态转移，低层再把转移落实成动作，从而避免高层搜索被固定技能绑住。

## 其余存档 12 篇

- [RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory](items/RoboArchitect%20Automating%20the%20Design%20of%20Robotic%20Agents%20with%20Persistent%20Memory.md) · 智能体 Agent 具身智能评测与基准
- [SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models](items/SACQ%20Structure-Aware%20Codebook%20Quantization%20for%20Ultra-Low-Bit%20Vision-Language-Act.md) · 多模态基础模型 视觉语言动作模型 VLA
- [MolmoSpaces-CommonSense: Evaluating Commonsense in Robotic Manipulation Policies](items/MolmoSpaces-CommonSense%20Evaluating%20Commonsense%20in%20Robotic%20Manipulation%20Policies.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos](items/HandMimicX%20Learning%20Human-Like%20Dexterous%20Manipulation%20via%20an%20Object-Centric%20Poli.md) · 世界模型 机器人学习 具身智能评测与基准
- [VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression](items/VLA%20Policies%20Do%20Not%20Know%20When%20Not%20to%20Act%20Unintended%20Task%20Execution%20and%20Start%20Sup.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA
- [TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](items/TinyAstral%20Transferring%20Self-Evolving%20Harnesses%20to%20Tiny%20Generalist%20Manipulation.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [ROSTrans: Empirically Benchmarking LLMs for ROS1-to-ROS2 Migration](items/ROSTrans%20Empirically%20Benchmarking%20LLMs%20for%20ROS1-to-ROS2%20Migration.md) · 多模态基础模型 具身智能评测与基准
- [Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics](items/Cross-Embodiment%20Motion%20Planning%20by%20Coupling%20Body-Agnostic%20World%20Model%20with%20Diff.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [FlapSim: A Composable MuJoCo Simulation Platform and Reduced-Order Aerodynamic Model Hierarchy for Flapping-Wing Robotics](items/FlapSim%20A%20Composable%20MuJoCo%20Simulation%20Platform%20and%20Reduced-Order%20Aerodynamic%20Mo.md) · 世界模型 机器人学习 具身智能评测与基准
- [ROOF: Learning Humanoid Fall Recovery under Overhead Constraints](items/ROOF%20Learning%20Humanoid%20Fall%20Recovery%20under%20Overhead%20Constraints.md) · 世界模型 机器人学习
- [META-Robot: Self-Cognition and Capability Scaling in Agentic Robots](items/META-Robot%20Self-Cognition%20and%20Capability%20Scaling%20in%20Agentic%20Robots.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices](items/RTPolicy%20Real-Time%20%2832.9%20Hz%29%20Multi-View%20Visuomotor%20Policy%20for%20Robotic%20Manipulati.md) · 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2509
- 入选条目：24
- 回填已见条目：0
- 最高分论文：CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents
- 最高分论文发布时间：2026-10-29T18:01:07Z
- 主要技术对象分类：具身智能评测与基准 17、多模态基础模型 14、世界模型 10、智能体 Agent 10、视觉语言动作模型 VLA 8、机器人学习 5
- 信息源错误：0
- 自动恢复信息源：0

</details>
