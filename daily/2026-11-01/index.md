---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-01
---

# 2026-11-01 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先解决的问题是：机器人学习缺的究竟是更多数据，还是能保留接触、任务进度和动作差异的数据与表示？先读 TouchBridge，看怎样把人的接触经验变成可训练的机器人示范；再读 BURGER，看怎样排除视觉捷径、拆开语言理解与动作生成的失败；若重点是长任务控制，读 HiFOR，检查预测未来之后如何挑出当前动作真正需要的信息。
> **趋势**：前五篇的共同线索：这些论文都在细化“给机器人更多信息”：数据侧强调可控生成、接触保留和独立核验，策略侧强调历史、未来及动作结构。共同指向的是信息如何进入学习和控制；现有证据仍分别受限于绘画、特定仿真或少量真机任务。

- **规模**：2405 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、多模态基础模型 14、世界模型 13、视觉语言动作模型 VLA 13、机器人学习 9、智能体 Agent 8、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing](items/BURGER%20Benchmarking%20and%20Understanding%20Robotic%20Generalization%20via%20Embodied%20Drawin.md)

> BURGER 让机器人从白纸开始按语言画画，用自动生成的多种画法测试 VLA 是否听懂对象和位置关系、能否学会多种动作路线。巧处是初始画面完全相同，模型必须依靠指令决定画什么。

- **能借鉴什么**：值得借鉴的是先设计能排除捷径的任务，再谈数据规模。固定起点、允许多个正确解、分别检查成品与轨迹，能帮助判断模型究竟理解了要求，还是只复现常见动作。
- **值得读吗**：值得细读任务设计与评价方法；它最有用的地方是把 VLA 的失败拆开看，而非给通用操作能力排总榜。

<details><summary>实验依据</summary>

数据含 132 个单物体、150 个组合任务，每任务 100 条，共 28,200 条仿真示范；比较 π₀、π₀.₅、π₀-FAST、OpenVLA 和 OpenVLA-OFT。[S6](https://arxiv.org/html/2610.40532v1#S1.p3.1) [S18](https://arxiv.org/html/2610.40532v1#S4.p2.1) 单物体评测选 10 类，每任务运行 10 次，以 DINOv3 衍生指标评分，并分析轨迹。[S6](https://arxiv.org/html/2610.40532v1#S1.p3.1) [S28](https://arxiv.org/html/2610.40532v1#A2.SS1.p3.1) 节选报告流匹配模型随数据增加总体改善、能组合熟悉对象，但难画训练外类别；未给各模型分数及人类评分一致性的数值。[S7](https://arxiv.org/html/2610.40532v1#S1.p4.1) Panda 真机展示补杯柄、跳过人已画好的车轮，支持闭环响应的存在，尚不能量化其可靠性。[S19](https://arxiv.org/html/2610.40532v1#S4.SS5.p1.1) [S20](https://arxiv.org/html/2610.40532v1#S4.SS5.p2.1)

</details>

### 2. [Gym-Anything for Robotics: Scaling physical simulations with digital agents](items/Gym-Anything%20for%20Robotics%20Scaling%20physical%20simulations%20with%20digital%20agents.md)

> Gym-Anything for Robotics 用编程智能体搭建机器人仿真，再让独立审查者查物理、任务和奖励漏洞。它还把仿真内部状态用于写教师代码，批量生成示范，训练部署时只看相机和自身状态的策略。

- **能借鉴什么**：可借鉴的关键是把“构造环境”和“证明环境可信”分开。若自动生成训练场，除了检查任务能完成，还要检查完成过程是否由机器人动作和物理机制导致，奖励是否真的对应目标。
- **值得读吗**：值得深读审查标准和特权状态转示范的流程；把“更真实”当作需要检查的主张，而非已由任务难度证明的事实。

<details><summary>实验依据</summary>

RoboWorld 包含 25 个仿真、25 个测试环境和 175 个训练环境。摘要报告最佳前沿模型测试成功率为零、平均奖励 0.06；较易的训练任务子集最高成功率为 32%。[摘要、S9] 每次尝试限三小时，过程中不提供奖励，最终分别统计完整成功与部分进度。[S20](https://arxiv.org/html/2610.40565v1#S6.SS1.SSS0.Px4.p1.1) 学习实验覆盖 11 个仿真；代码示范使 π₀.₅ 成功率从 0% 到 53%，对应两个礼盒任务，不能理解为全基准提升。[S17](https://arxiv.org/html/2610.40565v1#S5.p2.1) [S22](https://arxiv.org/html/2610.40565v1#S6.F7) [S25](https://arxiv.org/html/2610.40565v1#S6.SS3.p1.1) 这些都是仿真证据。

</details>

### 3. [PRIME W0: Physical Priors from World Models for Embodied Manipulation](items/PRIME%20W0%20Physical%20Priors%20from%20World%20Models%20for%20Embodied%20Manipulation.md)

> PRIME W0 给动作生成器同时补上历史画面、预测的未来画面和 VLM 各层信息，并用示范中的动作相关性塑造生成噪声。它想解决的是：只看眼前、只接收一份压缩语义，容易在长任务中丢失进度和协调。

- **能借鉴什么**：值得借鉴的是区分三类信息缺口：过去发生了什么、下一阶段可能怎样、动作各维应怎样协调。遇到长任务失败时，可以先判断缺哪类信息，再决定是否需要完整的世界模型，而不是一次堆上全部模块。
- **值得读吗**：值得重点读时间信息接口和消融；复现整套系统前，应先核实异步时延与训练数据条件。

<details><summary>实验依据</summary>

LIBERO 四套任务平均成功率为 99.1%，表内 EO-1 为 98.4%；Long 为 98.6%，EO-1 为 94.8%。[S30](https://arxiv.org/html/2610.39528v1#S4.SS2.p2.1) 在同数据的累加消融中，加入历史编码后 Long 从 81.6% 到 88.3%，再加异步未来图到 93.5%；完整模型真机平均为 78.1%。[S32](https://arxiv.org/html/2610.39528v1#S4.SS4.p1.1) [S33](https://arxiv.org/html/2610.39528v1#S4.T4) [S34](https://arxiv.org/html/2610.39528v1#S4.T4.7) 这支持组合设计在所测任务中的收益，但累加消融不能独立分离各模块及其交互；节选也未给真机任务明细、试验次数和误差。

</details>

### 4. [HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model](items/HiFOR%20Hierarchical%20Foresight%20with%20Action-Guided%20World%20Grounding%20for%20Vision-Langu.md)

> HiFOR 同时预测近期变化、中间里程碑和最终目标，再让正在生成的动作按需读取其中相关的时间、视角与区域。它的关键不是只增加未来预测，而是让未来信息随当前动作需求被选择。

- **能借鉴什么**：可借鉴的是把“预测得更多”和“控制时用得对”分开。若未来特征数量随视角和时间增长，保留它们的结构、让动作主动查询，可能比拼成一长串统一输入更合适。
- **值得读吗**：值得细读未来监督构造和检索机制；它给“预测怎样转为动作指导”提供了较清楚的设计与对照证据。

<details><summary>实验依据</summary>

LIBERO 每套评估 500 次，HiFOR 平均成功率 98.3%，π₀.₅ 为 96.9%；Long 分别为 95.8% 和 92.4%。[S22](https://arxiv.org/html/2610.40373v1#S4.SS1.p1.1) [S27](https://arxiv.org/html/2610.40373v1#S4.T2.8.1) RoboTwin 2.0 Hard 的 20 个任务每任务 100 次，平均为 49.40%，复现的 π₀.₅ 为 40.35%。[S22](https://arxiv.org/html/2610.40373v1#S4.SS1.p1.1) [S25](https://arxiv.org/html/2610.40373v1#S4.T1.7.1) [S28](https://arxiv.org/html/2610.40373v1#S4.SS1.p3.1) 六项 Piper 真机任务每项 50 次，平均 81.7%，比 π₀.₅ 高 11.0 个百分点。[S30](https://arxiv.org/html/2610.40373v1#S4.SS2.p1.1) [S32](https://arxiv.org/html/2610.40373v1#S4.SS2.p2.1) 全部未来层级基础上加入检索，RoboTwin 从 46.95% 到 49.40%，支持选择性读取的增益。[S34](https://arxiv.org/html/2610.40373v1#S4.T3.6.1)

</details>

### 5. [TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation](items/TouchBridge%20Tactile-Conditioned%20Human-to-Robot%20Transfer%20for%20Dexterous%20Manipulati.md)

> TouchBridge 把人手示范转换成机器人训练数据，核心 Tac-Retarget 不只对齐指尖姿势，还利用触觉保住接触区域及多个接触点的相对关系。这样无需为每件物体建模型或做仿真修正，也能迁移部分接触密集任务。

- **能借鉴什么**：启示是跨手型迁移应保留“交互中什么必须不变”。接触区域和接触点关系往往比绝对指尖坐标更接近任务要求，尤其适合姿势相似却总在接触时失败的情形。
- **值得读吗**：值得深读接触目标与硬件标定；它较具体地展示了触觉如何改善示范转换，而规模化收益仍需扩大验证。

<details><summary>实验依据</summary>

Moz1 双臂配 Wuji Hands，在翻书、拧灯泡、涂酱和抓蛋卷四项真机任务测试；每任务用 60 条示范微调 GR00T N1.7，评估 20 次。[S30](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS1.p1.1) [S31](https://arxiv.org/html/2610.40349v1#S4.F6) [S32](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS2.p1.1) [S33](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS4.p1.1) [S34](https://arxiv.org/html/2610.40349v1#S4.SS2.p1.1) [S35](https://arxiv.org/html/2610.40349v1#S4.T2) [S36](https://arxiv.org/html/2610.40349v1#S4.SS3.p1.1) 人类转换数据平均成功率 72.5%，等量遥操作数据为 77.5%；同训练条件下比 DexPilot、UniDex 高 25.0、42.5 个百分点。[S37](https://arxiv.org/html/2610.40349v1#S4.SS3.p2.1) [S41](https://arxiv.org/html/2610.40349v1#S4.SS4.SSS2.p1.1) 每条成功示范采集耗时 11.7 对 81.7 秒，约快 7 倍，计入失败和重置。[S31](https://arxiv.org/html/2610.40349v1#S4.F6) [S38](https://arxiv.org/html/2610.40349v1#S4.SS3.p3.1) 支持这组硬件和任务上的数据替代能力，尚非大规模跨手型验证。

</details>

## 扫读 7 篇

- [From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models](items/From%20Reasoning%20to%20Action%20Consequence-Grounded%20Alignment%20for%20Vision-Language-Acti.md) — CoRAct让机器人说出的行动理由真正约束动作：不仅检查“动作方向对不对”，还检查“做完后会不会到达预期位置”。它通过奖励引导动作生成的初始噪声，让生成结果更符合推理中的运动要求和路标点。
- [ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning](items/ScheduleGen%20Demonstration%20Generation%20via%20Skill%20Scheduling%20for%20Multi-Arm%20Imitatio.md) — ScheduleGen用少量已有示范生成多臂操作数据，同时安排各项技能怎样执行、何时执行。关键是把多臂约束纳入规划和调度，避免生成的示范看似完整，却让机械臂发生不安全或失败的行为。
- [LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks](items/LOGIV%20Graph-Verified%20Execution%20with%20Causal%20Local%20Repair%20for%20Long-Horizon%20Robot%20T.md) — LOGIV持续检查长任务依赖的物理条件，而不是把“某步做完了”视为永久有效。条件被破坏后，它沿任务图找出需要恢复的部分，并验证修复方案能否接回尚未完成的任务。
- [UMI-Live for In-The-Wild Bimanual Robotics Data Collection](items/UMI-Live%20for%20In-The-Wild%20Bimanual%20Robotics%20Data%20Collection.md) — UMI-Live把双手示范采集所需的硬件、定位、记录和数据处理整合起来，让人在实际场所演示操作后得到可训练数据。它的核心不是新动作模型，而是减少采集系统对外部追踪设备和场地内标定的依赖。
- [OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation](items/OpenFlyV2%20An%20onboard%20vision-language-action%20model%20for%20aerial%20perception%20and%20navi.md) — OpenFlyV2把看懂语言和环境、空间判断及飞行路点生成放进同一个机载模型。它用共享视觉语言表示、小型动作专家和时序信息复用，在受限算力上持续输出飞行指引。
- [Event2Reward: Learning Robotic Rewards from Progress Relations](items/Event2Reward%20Learning%20Robotic%20Rewards%20from%20Progress%20Relations.md) — Event2Reward 要让机器人分清“时间过去了”和“任务推进了”。它用示范时间确定进度尺度，再用停滞、倒退和恢复事件约束局部进度变化，把预测进度转成强化学习奖励。
- [Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models](items/Quantize%20by%20Doing%20Task-Guided%20Mixed-Precision%20Quantization%20of%20Vision-Language-Ac.md) — QbD-VLA 压缩视觉语言动作模型时，直接看机器人还能否完成任务，再决定各部分用多少位精度。它把不同部分量化后的相互影响也纳入选择，而不是只凭离线校准误差分配位宽。

## 其余存档 12 篇

- [LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](items/LucidLyra%20Feed-Forward%20Generative%203D%20Scene%20Reconstruction%20and%20Joint%20Understandin.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors](items/Continuous-Action%20World%20Models%20Learning%20Cross-Embodiment%20Spatiotemporal%20Dynamics.md) · 世界模型
- [Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles](items/Learning%20Safe%20Flow%20Matching%20Robot%20Policies%20from%20Binary%20Feasibility%20Oracles.md) · 多模态基础模型 视觉语言动作模型 VLA
- [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](items/Seeing%20and%20Imagining%20as%20One%20Unified%20Video%20Generation%20and%204D%20Perception%20for%20Embod.md) · 世界模型
- [EgoContact: Evaluating Physical Intelligence with Egocentric Video](items/EgoContact%20Evaluating%20Physical%20Intelligence%20with%20Egocentric%20Video.md) · 世界模型 具身智能评测与基准
- [Tracking Task Progress Through Errors and Recovery:A Benchmark and Recurrent Distributional Model](items/Tracking%20Task%20Progress%20Through%20Errors%20and%20Recovery%20A%20Benchmark%20and%20Recurrent%20Dis.md) · 智能体 Agent 具身智能评测与基准
- [SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing](items/SwapBot%20Tool-Centric%20Robot%20Manipulation%20via%20Interchangeable%20End-Effectors%20and%20Ta.md) · 机器人学习 具身智能评测与基准
- [JEDI: Joint-Embedding Demonstration Compression for In-Context Imitation Learning](items/JEDI%20Joint-Embedding%20Demonstration%20Compression%20for%20In-Context%20Imitation%20Learning.md) · 多模态基础模型 机器人学习 具身智能评测与基准
- [RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence](items/RoboSeed%20Multidimensional%20Evaluation%20of%20Vision-Language-Action%20and%20World-Action.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [LiDAR-SHIELD: A Fully Dockerized Adversarial Robustness Assessment Framework for LiDAR-Based 3D Perception Models](items/LiDAR-SHIELD%20A%20Fully%20Dockerized%20Adversarial%20Robustness%20Assessment%20Framework%20for.md) · 智能体 Agent 具身智能评测与基准
- [AegisFlow: Training-Free Non-Myopic Path-Safe Guided Flow Matching](items/AegisFlow%20Training-Free%20Non-Myopic%20Path-Safe%20Guided%20Flow%20Matching.md) · 智能体 Agent 具身智能评测与基准
- [Smooth Action Chunking Via Movement-Primitive Representations for Imitation Learning](items/Smooth%20Action%20Chunking%20Via%20Movement-Primitive%20Representations%20for%20Imitation%20Lear.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2405
- 入选条目：24
- 回填已见条目：0
- 最高分论文：BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing
- 最高分论文发布时间：2026-10-29T17:34:04Z
- 主要技术对象分类：具身智能评测与基准 18、多模态基础模型 14、世界模型 13、视觉语言动作模型 VLA 13、机器人学习 9、智能体 Agent 8、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
