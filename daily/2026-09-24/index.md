---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-09-24
---

# 2026-09-24 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天最值得关注的是两条线：一条把 VLA 的薄弱环节拆成可干预的执行机制，包括专家接管、安全回退、力觉条件化和物理一致的示教；另一条重新审视高成功率究竟掩盖了什么，集中检查语言依赖、物理变化、多视角一致性和推理延迟。建议优先细读这些机制与评测协议，再看统一模型的总分；摘要中的单项成绩不足以直接支持跨论文排名。
> **趋势**：这一批工作共同表明，机器人能力需要从平均任务成功率进一步拆解到理解、接触、恢复和部署条件。模型侧则更多采用通用策略与专门模块协作，并按数据所能提供的监督信号分配训练职责。

- **规模**：2365 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、多模态基础模型 16、视觉语言动作模型 VLA 13、世界模型 10、智能体 Agent 9、机器人学习 8、Sim2Real 2、AI 核心知识地图 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection](items/MATE%20Multi-Agent%20Virtual%20Teleoperation%20Platform%20for%20Humanoid%20Collaboration%20Data.md)

> MATE 让异地操作者在同一个物理仿真环境里共同操控人形机器人，降低多人、多机器人协作示范的采集门槛。配套的 EAIS 则优先抽取推进任务和发生关键交互的片段来训练策略。

- **为什么值得读**：对协作机器人学习和 VLA 研究者，价值在于提供可扩展的联合示范采集路径，并把多智能体之间的交互时刻作为明确的学习对象。
- **证据**：数据集包含 24.1 小时、2,500 个联合回合和五类长时程任务。摘要报告了模仿学习与 VLA 策略评测，以及无需真实微调的虚拟示范到实体人形机器人的零样本迁移，但未给出成功率或采集效率数字。
- **判断**：做多机器人数据或协作 VLA 的研究者值得细读平台与采样设计，实体协作泛化结论需以全文为准。

### 2. [MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation](items/MedVLA%20A%20Hierarchical%20Vision-Language-Action%20Framework%20for%20Closed-Loop%20Precision.md)

> MedVLA 把医疗机器人控制拆成高层多模态推理与底层受约束的功能执行，使模型既能选择动作，也能调用闭环操作所需的系统功能。

- **为什么值得读**：对 VLA 和智能体研究者，这是把推理、工具调用和机器人执行统一到任务流程中的具体案例，也提示精密任务评测需要检查动作接口是否匹配实际需求。
- **证据**：在相同初始条件下进行了 100 次闭环柔性电极植入试验，MedVLA 成功率为 95.0%，OpenVLA 为 8%，π₀ 为 15%。摘要还报告不同多模态骨干微调后均有提升，但未量化安全性与稳定性。
- **判断**：值得细读执行接口和对照设置，95% 成功率是明确结果，但不足以单独支持可部署医疗系统的判断。

### 3. [MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence](items/MachEmbodied-U0%20Unified%20Understanding%20and%20Generation%20Model%20for%20Embodied%20Intellig.md)

> MachEmbodied-U0（ME-U0）尝试让机器人同时理解下一步要做什么、在哪里操作、场景将怎样变化，并据此生成动作。它用 Mixture-of-Transformers 连接理解与生成专家，把语义定位和视觉动力学一起纳入控制。

- **为什么值得读**：对世界模型与 VLA 研究者，它提供了将任务理解、几何运动预测和动作学习放进同一模型的具体架构，并展示这些中间能力可以单独迁移。
- **证据**：预训练使用约 4,200 小时机器人与第一视角示范。RoboDojo 平均分为 17.66，LIBERO 和 LIBERO-Plus 平均成功率分别为 99.0% 和 82.5%；另报告真实操作验证及无对应下游监督的子任务、可供性和视觉动力学零样本能力。
- **判断**：值得深入阅读架构与训练目标，尤其关注理解和动力学能力如何实际改善控制，而不只看 LIBERO 分数。

### 4. [HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments](items/HOTICE%20Whole-Body%20Humanoid%20Object%20Transportation%20in%20Cluttered%20Environments.md)

> HOTICE 让人形机器人搬着物体穿过拥挤环境，同时照顾身体和货物的避障。它把上下肢控制分给两个强化学习智能体，再将多个场景专家蒸馏成一个部署策略。

- **为什么值得读**：对全身机器人学习与 Sim2Real 研究者，价值在于把载荷几何纳入控制目标，并提供高维控制的分解方法。这里的双智能体指控制分工，摘要未体现世界模型贡献。
- **证据**：在 MuJoCo 和真实 Unitree G1 上评估了不同形状物体的杂乱场景搬运。摘要报告未见环境泛化、全身协调和 sim2real 效果，未给出可核查的结果数字。
- **判断**：做全身搬运值得细读势场与上下身协调机制，效果强弱仍需查看量化评测。

### 5. [RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy](items/RouteRLT%20Learning%20When%20and%20Which%20RL%20Specialist%20Should%20Control%20a%20Vision-Language-.md)

> RouteRLT 学习让通用 VLA 在精密阶段把控制权交给合适的 RL 专家，并处理切换抖动和动作块衔接。它重点解决的是何时接管、由谁接管。

- **为什么值得读**：对 VLA 与机器人学习研究者，它提供了保留通用策略、局部引入 RL 精度的模块化路径，切换边界处理也直接关系到闭环执行可靠性。
- **证据**：评测包括 LIBERO 多物体拾放和真实线缆拾取、端口插入。仿真中的学习路由优于基础 VLA，并达到使用特权阶段边界的路由表现；真实实验在操作者对齐的交接协议下验证了两类专家的自动路由。摘要未给出结果数字。
- **判断**：值得细读路由和动作交接实现，尤其适合已有通用策略、只想补强少数精密阶段的研究。

## 扫读 7 篇

- [SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation](items/SafeLoop%20Risk-Aware%20Rollback%20for%20Vision-Language-Action%20Manipulation.md) — SafeLoop 给现有 VLA 加一个外部安全控制器：预测碰撞或掉物风险，必要时退回最近的安全关节位置，再让原策略重新尝试。基础 VLA 参数保持不变。
- [TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models](items/TriWorldBench%20A%20Tri-View%20Consistency%20Perspective%20on%20Embodied%20World%20Models.md) — TRIWORLDBENCH 检查世界模型生成的头部、左腕和右腕视频是否描述同一次一致的操作，避免每个视角单看都合理、合起来却互相矛盾。
- [RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?](items/RoboTwin-Phys%20Do%20WAMs%20and%20VLAs%20Understand%20the%20Physical%20World.md) — RoboTwin-Phys 把物体质量、摩擦和关节动力学等物理变化纳入机器人评测，检查策略是否只能应付画面变化，却无法应付真实交互条件变化。
- [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](items/RoboFollow%20Unveiling%20the%20Instruction%20Following%20Mirage%20in%20Embodied%20Agents.md) — RoboFollow 检查机器人是否真的听懂指令：同一场景必须允许多种不同操作，才能排除模型只看画面就猜中任务的可能。
- [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](items/IndustrialVLA-Bench%20A%20Traceable%20Multi-Axis%20Evaluation%20of%20Open%20Robot%20Policy%20Model.md) — IndustrialVLA-Bench 用统一且可追溯的记录比较开放 VLA 与 WAM，发现基础任务分数接近时，鲁棒性和指令改写表现仍可能相差很大。
- [HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery](items/HABILIS%20Brain%200%20Geometry-Change%20Supervision%20for%20Vision-Language-Action%20and%20Resid.md) — GC-VLA 学习预测操作将引起的几何变化，而不只表示当前几何；GCRF 再利用闭环反馈训练一个受限的残差策略，在需要时修正动作。
- [Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation](items/Imperfection%20for%20Precision%20Upcycling%20Imperfect%20Data%20for%20High-Precision%20Robotic%20M.md) — ε4P 把两类不完美数据分工使用：目标任务的粗糙示范教模型做什么，其他任务的精细示范教模型怎样做得准。分工通过 flow matching 的不同噪声阶段实现。

## 其余存档 12 篇

- [Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes](items/Metric-Bench%20Exploring%20In-context%20Spatial%20Metric%20Reasoning%20in%20VLMs%20for%20Indoor%20Sc.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation](items/VisForce%20Visual%20Grounding%20of%20Current%20and%20Desired%20Forces%20for%20Goal-Conditioned%20Dex.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing](items/CableVLA%20Simulation-Privileged%20Global-Local%20Representation%20Learning%20for%20Cable%20Ro.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models](items/VLAQuantBench%20Closed-Loop%20Evaluation%20of%20Post-Training%20Quantization%20for%20Vision-La.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Generalizing Manipulation Skills with a Local Coding Agent](items/Generalizing%20Manipulation%20Skills%20with%20a%20Local%20Coding%20Agent.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering](items/Hierarchical%20Floorplan-Guided%20Vision-Language%20Exploration%20for%20Embodied%20Question.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers](items/The%20Cartesian%20Hand%20In-Hand%20Manipulation%20with%20All-Linear%20Fingers.md) · [[AI 核心知识地图]]
- [Norm2Tex: Augmenting Visuo-Tactile Simulations with Texture](items/Norm2Tex%20Augmenting%20Visuo-Tactile%20Simulations%20with%20Texture.md) · [[世界模型]] [[机器人学习]] [[Sim2Real]]
- [Benchmarking Robots for Everyday Environments: From Lab Experiments to Real-World Operations](items/Benchmarking%20Robots%20for%20Everyday%20Environments%20From%20Lab%20Experiments%20to%20Real-World.md) · [[具身智能评测与基准]]
- [PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning](items/PAKT%20Physically-Aligned%20Kinesthetic%20Teaching%20for%20Reinforcement%20Learning.md) · [[机器人学习]] [[具身智能评测与基准]]
- [MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts](items/MotionForge%20A%20Data%20Generation%20Pipeline%20and%20Large-Scale%20Benchmark%20for%20Long-Horizo.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation](items/SAM-V%20Geometry-Aware%20Segment%20Anything%20for%20Multi-View%20Instance%20Segmentation.md) · [[多模态基础模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2365
- 入选条目：24
- 回填已见条目：0
- 最高分论文：MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection
- 最高分论文发布时间：2026-09-22T14:45:17Z
- 主要技术对象分类：具身智能评测与基准 18、多模态基础模型 16、视觉语言动作模型 VLA 13、世界模型 10、智能体 Agent 9、机器人学习 8、Sim2Real 2、AI 核心知识地图 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
