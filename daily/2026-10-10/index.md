---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-10
---

# 2026-10-10 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人已经会生成动作，为什么仍会选错、执行偏离或来不及纠正？先读 ManiUnit，学会把长任务失败拆成技能选择、起始状态和衔接问题；再读 HWAM，理解为什么动作指令不能代替实际身体运动；若关心动态场景中的闭环执行，读 REACT 的滚动缓冲与训练时序。ACT³ 和 NegaAlign 分别适合进一步检查信息融合位置和语言约束如何进入动作。
> **趋势**：前五篇的共同线索：这些论文都把动作失败背后容易被混在一起的因素单独处理：语义与动力学、技能与任务、动作参考与执行状态、规划时域与观测更新、肯定技能与否定约束。共同启示是先找准信息或监督应进入的位置，再决定是否需要增加模型能力。

- **规模**：2433 个候选 → 24 篇入选；回填 0 篇
- **主题**：视觉语言动作模型 VLA 18、具身智能评测与基准 17、多模态基础模型 16、世界模型 15、智能体 Agent 8、机器人学习 8、Sim2Real 2
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer](items/Rewiring%20Semantics%2C%20Dynamics%2C%20and%20Control%20A%20Simple%20yet%20Effective%20Action-Centric.md)

> ACT³ 让机器人既理解“要做什么”，又利用“接下来可能发生什么”来生成动作。巧处是两个信息来源各自计算，只让动作专家逐层读取并融合它们。

- **能借鉴什么**：值得借鉴的是把融合推迟到真正需要作决策的模块。已有两种预训练模型、却担心互相改坏表示时，可以尝试保留各自前向计算，让动作损失决定该读取什么；前向独立并不意味着训练时冻结。
- **值得读吗**：值得读到注意力连接、缓存和受控消融：可借鉴的是融合位置，但需核实它相对增加模型容量究竟贡献多少。

<details><summary>实验依据</summary>

仿真覆盖 RoboCasa 厨房操作和 LIBERO，并在 LIBERO-Plus 上无额外微调测试；主要对照是同一训练评测流程中的 π₀.₅，但节选没有仿真成绩和消融数值 [S22](https://arxiv.org/html/2610.11416v1#S4.SS1.p1.1) [S23](https://arxiv.org/html/2610.11416v1#S4.SS1.p2.1) [S24](https://arxiv.org/html/2610.11416v1#S4.SS1.p3.1)。真机使用 CobotMagic 双臂平台，每任务每方法测试30次：叠碗为27/30对26/30，收集积木为25/30对22/30，插花为19/30对14/30 [S25](https://arxiv.org/html/2610.11416v1#S4.SS6.p1.1) [S26](https://arxiv.org/html/2610.11416v1#S4.T4) [S27](https://arxiv.org/html/2610.11416v1#S4.T4.2.1) [S28](https://arxiv.org/html/2610.11416v1#S4.SS6.p2.1)。这支持完整策略在这些任务上的观察优势，尚不足以单凭这些数字确认优势来自哪条连接。

</details>

### 2. [ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks](items/ManiUnit%20A%20Manipulation%20Skill%20Dataset%20and%20Benchmark%20for%20Long-Horizon%20Tasks.md)

> ManiUnit 把长任务拆成带明确指令的操作片段，并恢复操作开始时的仿真状态来单独考试。它要分清机器人究竟不会这个技能，还是选错阶段、或被上一阶段留下的姿态难住了。

- **能借鉴什么**：可以借鉴“每个阶段都有独立入口和出口判据”的诊断方式。这样改进后段技能时，不必先等前段全部成功；同时要把技能入口姿态作为测试变量，因为单项成功并不保证技能可串联。
- **值得读吗**：优先读数据切分和状态恢复方法：它最有用的贡献是让失败可定位，而完整任务组合仍是范围有限的验证。

<details><summary>实验依据</summary>

数据来自50项 BEHAVIOR-1K 活动，含137,899片段、21类技能和417子任务；Full 有1,260个仿真测试实例 [S5](https://arxiv.org/html/2610.12089v1#S1.p3.1)。成功要求局部目标连续满足十帧且不超时，成绩对技能类型等权平均 [S27](https://arxiv.org/html/2610.12089v1#S4.SS1.SSS0.Px2.p1.1)。Full 上 StarVLA-PI 从原始起点60.1%降到关节扰动26.5%，GR00T从63.5%降到28.2%，摘要概括为约56%的相对下降，并非下降56个百分点 [S20](https://arxiv.org/html/2610.12089v1#S4.F3.2.1)。两项活动中，同源 π₀.₅ 初始化、训练五轮的技能策略达78.7%，整任务策略49.3% [S29](https://arxiv.org/html/2610.12089v1#S4.SS3.p1.1) [S30](https://arxiv.org/html/2610.12089v1#S4.F4.2.1)；规划器组合后的整任务成功率为18.0%对4.0% [S6](https://arxiv.org/html/2610.12089v1#S1.p4.1)。

</details>

### 3. [Humanoid World Action Model With Joint State--Action Generation](items/Humanoid%20World%20Action%20Model%20With%20Joint%20State--Action%20Generation.md)

> HWAM 同时预测“让机器人怎样动”和“执行后身体实际会到哪里”。它再用正向、反向视觉预测训练这对轨迹，帮助高层策略学会低层控制造成的执行偏差。

- **能借鉴什么**：当动作还要经过会修改命令的控制层时，可以把“命令—实际响应”作为显式学习对象，避免让图像预测独自吸收全部偏差。但状态目标要与解释物理结果的训练任务配套，不能当作随手附加的输出。
- **值得读吗**：值得读到时间对齐和两因素消融：最有说服力的是联合状态目标依赖合适训练方式，而不是单纯多预测一种变量。

<details><summary>实验依据</summary>

LimX OLI 真机测试包括取糖果、物体收集和移动取毛绒玩具；对照含 π₀.₅、GR00T、Fast-WAM 等 [S25](https://arxiv.org/html/2610.12026v1#S4.SS2.p1.1) [S27](https://arxiv.org/html/2610.12026v1#S4.SS2.p2.1)。HWAM 成功率为70.6%、46.7%、73.3%，π₀.₅为62.5%、45.0%、60.7%；Fast-WAM 取糖果为43.3% [S31](https://arxiv.org/html/2610.12026v1#S4.T1.2)。这些是完整系统成绩。移动任务的匹配消融更关键：普通视频生成加策略训练下，加入状态目标从60.0%降至45.5%；三路径训练下则从55.0%升至73.3% [S35](https://arxiv.org/html/2610.12026v1#S4.T2.2)。证据支持状态目标与训练方式的配合，不能说加状态预测必然有益。

</details>

### 4. [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models](items/REACT%20Rolling%20Denoising%20and%20Dual%20Decoupling%20for%20Reactive%20Robot%20Control%20with%20VLA.md)

> REACT 不再每次丢掉旧计划、重新生成整段动作，而是保留一个持续修正的动作缓冲区。未来动作在逐渐接近执行时多次吸收新观测，兼顾长段运动的连贯性和及时纠正。

- **能借鉴什么**：值得借鉴的是保留未执行计划的中间状态，让新观测逐步修改它，而不是每次重新抽样整段动作。同时，实时控制应分别检查新信息进入频率和动作输出频率，单次推理耗时无法描述整个闭环。
- **值得读吗**：值得读到缓冲更新和线程调度实现：机制清楚且能直接启发闭环设计，但换骨干或调度需要重新验证。

<details><summary>实验依据</summary>

实验都基于 π₀.₅：RoboTwin 2.0 七项仿真任务含 Clean／Randomized，另有 ARX X5 和 Franka R3 真机六个平台任务组合 [S20](https://arxiv.org/html/2610.12007v1#S4.SS1.p1.1) [S21](https://arxiv.org/html/2610.12007v1#S4.SS1.p2.1)。不含双解耦的滚动版本仿真成功率49.71%／20.86%，长段基线37.43%／11.43%；真机总体65.7%对58.7% [S27](https://arxiv.org/html/2610.12007v1#S4.SS2.p2.1) [S28](https://arxiv.org/html/2610.12007v1#S4.SS2.p3.1)。仿真 jerk 为1064.7，低于频繁重规划的1463.7，却高于长段基线658.9。它支持更好的反应与平滑折中，并非全面最平滑。节选没有完整 REACT 的成绩、反应延迟和吞吐数值，不能拿上述数字代替。

</details>

### 5. [Tell Robot What Not to Do: A Negation Understanding Perspective](items/Tell%20Robot%20What%20Not%20to%20Do%20A%20Negation%20Understanding%20Perspective.md)

> NegaAlign 让已经会操作的 VLA 学会“做这件事，但排除那个对象或结果”。它用允许行为的肯定指令作老师，修正否定指令对应的语言和视觉表示，只训练少量插入层。

- **能借鉴什么**：如果机器人已经会执行允许的肯定操作，约束适配可以先尝试改变“它看中了什么”，而不必重学动作。关键条件是已有技能覆盖合法选项，并且能构造可信的允许与排除关系；这不是让模型凭空获得新技能。
- **值得读吗**：值得读到监督关系构造与视觉对齐消融：它展示了低成本复用肯定技能的路径，但适用范围取决于技能覆盖和未见约束测试。

<details><summary>实验依据</summary>

NegaBench 是 RoboTwin 仿真中的十场景、五类约束，成功同时要求完成任务和不违反排除条件 [S23](https://arxiv.org/html/2610.11952v1#S3.SS6.p1.1) [S24](https://arxiv.org/html/2610.11952v1#S4.SS1.p1.1)。π₀.₅ 否定成功率从2.60%升至88.45%，肯定成功率92.77%变为92.51%；直接用否定轨迹训练为88.60%，外部 Qwen 改写为55.70% [S26](https://arxiv.org/html/2610.11952v1#S4.T1.4.1)。NegaAlign 在 GR00T、π₀ 上也改善，但否定成绩57.75%、63.30%低于直接轨迹训练的68.85%、71.25%。摘要报告 π₀.₅ 真机12.4%升至88.8%，但没有给出真机任务、试验次数及协议，证据范围需保留。

</details>

## 扫读 7 篇

- [SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation](items/SimVLA%20Zero-Shot%20Sim-to-Real%20VLA%20Learning%20for%20Mobile%20Manipulation.md) — SimVLA 要让移动机器人只靠仿真数据学习，再直接去现实里补货、倒液体和清洁。关键是同时教它怎么行动、怎么看懂空间关系，并用策略在仿真中实际跑出来的数据继续训练。
- [VioLA: Learning Generalist Humanoid Control Policies from Human Data](items/VioLA%20Learning%20Generalist%20Humanoid%20Control%20Policies%20from%20Human%20Data.md) — VioLA 让通用人形策略预测身体和手部的运动潜变量，再交给预训练控制器执行。这样人的录像也能被编码成策略要预测的动作标签，缓解机器人示范少、关节控制难的问题。
- [ARC: A Reasoning Recipe for Robot Foundation Models](items/ARC%20A%20Reasoning%20Recipe%20for%20Robot%20Foundation%20Models.md) — ARC 从已有机器人示范自动补出解释：下一步为什么这样做、预计会产生什么效果，再训练现有模型使用这些解释控制机器人。巧处是把推理紧贴下一步动作，而非只让模型泛泛描述任务。
- [WAM-Cache: Staleness-Bounded KV Reuse for Efficient World Action Models](items/WAM-Cache%20Staleness-Bounded%20KV%20Reuse%20for%20Efficient%20World%20Action%20Models.md) — WAM-Cache 把世界动作模型上一轮的视觉 KV 表示留下来，每轮只更新部分位置，减少重复计算。它发现更新优先级应同时看动作专家关注哪里、视觉信息哪里意外变化，并限制缓存最多能用多久。
- [SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation](items/SpatialHarness%20Test-Time%20Spatial%20Scaffolding%20for%20Fine%20Robotic%20Manipulation.md) — SpatialHarness 在执行时维护一个与现实同步的模拟场景，渲染额外虚拟视角，让冻结的多模态策略看清关键空间关系。它针对的是精细操作时“现有相机没把关系展示清楚”的问题，无需微调策略或改变实体相机配置。
- [Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models](items/Recompose%20and%20Refine%20Latent%20Reasoning%20Flows%20for%20Vision-Language-Action%20Models.md) — FLOWMEM 让机器人保留成功执行时用过的内部推理片段，下次遇到相关情境时重新组合，再用当前观测修正。它要减少的是每次决定动作都从头构造相似推理的重复计算。
- [WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models](items/WARP-VLA%20Wrist-Camera%20Adaptation%20for%20View-Robust%20Policy%20Execution%20in%20Vision-Lang.md) — WARP-VLA 用多个专家学习不同腕部视角下的特征变换，再由路由器根据图像中的视角线索组合专家。这样，相机安装位置发生变化时，策略仍有机会正确理解物体与机械手的几何关系。

## 其余存档 12 篇

- [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](items/DreamTrue%20Action-Faithful%20Robot%20World%20Model%20with%20Counterfactual%20Post-Training.md) · 世界模型
- [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](items/RESETTLE%20Robotic%20Recovery%20through%20Disagreement-Triggered%20Retrieval%20and%20Efficient.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- [USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation](items/USDCraft%20Geometrically%20Grounded%20Programmatic%20Modeling%20of%20Articulated%203D%20Assets%20f.md) · 世界模型 Sim2Real 具身智能评测与基准
- [VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation](items/VersaCamVLA%20Camera-Configurable%20VLA%20Policies%20for%20Robotic%20Manipulation.md) · 多模态基础模型 视觉语言动作模型 VLA
- [Control-Ready Uncertainty for Trajectory Diffusion](items/Control-Ready%20Uncertainty%20for%20Trajectory%20Diffusion.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies](items/PLaW-VLA%20Predictive%20Latent%20World%20Modeling%20for%20Vision-Language-Action%20Policies.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning](items/Residual%20Modeling%20Closes%20the%20Regression%20and%20Generative%20Policy%20Gap%20in%20Robot%20Learn.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes](items/LIVIN%20Benchmarking%20Spatial%20and%20Embodied%20Intelligence%20in%20Digital%20Twins%20of%20Lived-I.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes](items/RoboAware%20Learning%20to%20Coordinate%20Embodied%20Skills%20from%20Counterfactual%20Outcomes.md) · 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [Being-M0.7: A Latent World-Action Model for Humanoid Robots](items/Being-M0.7%20A%20Latent%20World-Action%20Model%20for%20Humanoid%20Robots.md) · 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [PMTRM: Pseudo-Memory Temporal Re-encoding Module for Embodied Policy Learning](items/PMTRM%20Pseudo-Memory%20Temporal%20Re-encoding%20Module%20for%20Embodied%20Policy%20Learning.md) · 世界模型 具身智能评测与基准
- [Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](items/Embodied%20Turing%20Machines%20Stateful%20Code%20for%20Robot%20Recursive%20Self-Improvement.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2433
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer
- 最高分论文发布时间：2026-10-08T07:45:58Z
- 主要技术对象分类：视觉语言动作模型 VLA 18、具身智能评测与基准 17、多模态基础模型 16、世界模型 15、智能体 Agent 8、机器人学习 8、Sim2Real 2
- 信息源错误：0
- 自动恢复信息源：0

</details>
