---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-29
---

# 2026-10-29 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：怎样让 VLA 的动作依据超出当前图像，同时保住执行速度和任务意图。想理解无动作标签视频如何变成训练信号，先读 ThinkWorld 的 CoD 与未来匹配奖励；关心执行中绕障又能继续完成任务，读 VLA-Stem 的轨迹引导与恢复训练；想复用已有成功示范纠正视觉干扰，读 R2A 的几何检索及其适用边界。另需先纠正输入：Tokens of Motion 的 abstract 描述 AFIL，与标题及正文节选中的 M-PACT 不符，以下按相互一致的标题和正文讲解。
> **趋势**：前五篇的共同线索：这些论文都在给直接生成动作的 VLA 增加中间依据：未来变化、可复用运动片段，或执行时的参考轨迹。它们把部分学习负担放在训练阶段或独立模块中，但解决的是不同问题：学到更多行为、抵抗视觉变化和避碰，不能用同一个成功率概括。

- **规模**：2495 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 14、多模态基础模型 12、机器人学习 12、视觉语言动作模型 VLA 11、世界模型 10、智能体 Agent 6、AI 核心知识地图 1、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](items/ThinkWorld%20World%20Imagination%20Reinforces%20Chain-of-Dynamics%20Reasoning.md)

> ThinkWorld 让机器人从人类视频学习“怎样的运动会带来怎样的变化”：先把动作写成 Chain-of-Dynamics（CoD）运动 token，再奖励那些能预测出视频真实后续的 CoD。未来预测只用于训练，部署时不生成未来视频。

- **能借鉴什么**：值得借鉴的是：先用少量有动作含义的数据约束表示，再用大量视频的真实后续筛选这种表示。这样，“能预测变化”才有机会成为动作学习信号，而不是把所有视觉变化都叫动作。
- **值得读吗**：值得深入读奖励设计和组件消融，因为关键在于未来匹配是否真的约束了动作，而非仅增加一个预测任务。

<details><summary>实验依据</summary>

真机在双臂 YAM 上做颜色匹配、挂杯、物体分类，比较 Diffusion Policy、MolmoAct2、LaWAM。ThinkWorld 共成功112/120次，微平均93.3%，MolmoAct2为60.0%；其中分布内60/60、分布外52/60。[S27](https://arxiv.org/html/2610.37666v1#A2.SS3.p1.1) [S30](https://arxiv.org/html/2610.37666v1#A2.T6.6.1) [S31](https://arxiv.org/html/2610.37666v1#A3.SS1.p1.1) 这支持指定外观、类别及轨迹变化下的适应能力。烤箱和抽屉技能组合提供定性成功展示，不能据此估计组合成功率。[S32](https://arxiv.org/html/2610.37666v1#A3.SS1.p2.1) 仿真消融虽有说明，所给节选没有数值。

</details>

### 2. [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](items/PDRVLA%20A%20Vision-Language-Action%20Model%20with%20Physical%20Dynamics%20Representations.md)

> PDRVLA 把预测未来所需的信息压进少量 physical tokens，让动作模型利用这些信息，却不用在控制时生成视频。它同时学习未来外观、深度和光流，并在预训练中借助冻结的视频模型提供监督。

- **能借鉴什么**：可以借鉴的是把昂贵预测器当训练工具，把执行时真正需要的信息压进小表示。若已有视频训练数据又受控制延迟限制，联合预测外观、空间和运动，比只要求重建画面更值得检查。
- **值得读吗**：值得细读训练目标和同条件消融；四项仿真成绩支持方法可用，但尚不足以说明优势主要来自物理表示。

<details><summary>实验依据</summary>

四项测试均为仿真。LIBERO、LIBERO-Plus、RoboTwin 2.0、SimplerEnv成功率分别为99.3%、89.9%、93.6%、81.5%；对照Qwen-RobotManip前三项为99.1%、89.0%、93.0%，InternVLA-A1.5四项为98.9%、84.8%、93.2%、80.8%。[S42](https://arxiv.org/html/2610.37381v1#S5.T5.2) LIBERO共2000回合，Plus有10030个案例。[S36](https://arxiv.org/html/2610.37381v1#S5.SS1.p1.1) [S37](https://arxiv.org/html/2610.37381v1#S5.SS1.p2.1) 总体领先，但LIBERO长任务97.6%，低于LingBot-VA的98.5%。[S43](https://arxiv.org/html/2610.37381v1#S5.SS2.SSS0.Px1.p1.1) 基线来自各自论文和协议，不能把差距全归因于物理模块。[S40](https://arxiv.org/html/2610.37381v1#S5.SS2.p1.1)

</details>

### 3. [VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning](items/VLA-Stem%20A%20Lightweight%20Safety%20Mechanism%20for%20Vision-Language-Action%20Models%20via%20Re.md)

> VLA-Stem 在冻结的 VLA 后面接一个执行策略：把原动作当路线参考，遇到障碍时允许绕行、减速或等待，再继续任务。它学习保持路线的空间意图，而不是死守每个时刻的原动作。

- **能借鉴什么**：值得借鉴的是把“要去哪里”和“此刻怎么安全走”分开，并训练偏离后的恢复。执行修正不能只优化当下距离障碍多远，还要考虑是否保留后续任务可完成的状态。
- **值得读吗**：值得读到轨迹奖励和教师训练细节，因为其核心贡献是同时保住避障与任务连续性，而非单独降低碰撞率。

<details><summary>实验依据</summary>

ManiSkill中测试PickCube、Object Stowing、StackCube，各含正常、静态、动态场景，每个设置3200回合。对比原VLA、避障数据微调、VLSA安全过滤器。[S23](https://arxiv.org/html/2610.37378v1#S4.SS1.p1.1) [S24](https://arxiv.org/html/2610.37378v1#S4.SS1.p2.1) [S25](https://arxiv.org/html/2610.37378v1#S4.SS1.p3.1) [S26](https://arxiv.org/html/2610.37378v1#S4.SS1.p4.1) [S27](https://arxiv.org/html/2610.37378v1#S4.SS1.p5.1) 六个受限设置的平均无碰撞任务成功率为52.8%，最强安全基线23.7%（摘要）。PickCube静态场景中，VLSA-ARM碰撞率22.53%，略低于Stem的23.16%，但成功率仅15.16%，Stem为52.19%。[S22](https://arxiv.org/html/2610.37378v1#S4.T1.2.1) 这说明只看少碰撞会误判任务效果。真机结果在所给材料中只有定性结论。

</details>

### 4. [Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer](items/Tokens%20of%20Motion%20Primitive%20Motion%20Learning%20for%20Human-Humanoid%20Skill%20Transfer.md)

> M-PACT 把人手运动拆成可复用的局部表示，再用小型机器人专用解码器把它们变成运动。输入 abstract 实为另一方法 AFIL；这里依据与标题一致的正文[S1]及后续节选解释 M-PACT。

- **能借鉴什么**：可以借鉴的是把可复用表示固定下来，只重新学习身体相关的实现映射。它把“词汇迁移失败”和“新机器人解码失败”拆开检查，也避免每换身体就重学整套运动表示。
- **值得读吗**：值得深入读表示与解码分离的实验；目前最扎实的结论是运动词汇可复用，完整操作能力应另查闭环量化证据。

<details><summary>实验依据</summary>

在EgoDex学习表示，HoloAssist测试冻结迁移，HumanoidEveryday适配机器人解码器。后者的端点平移、旋转、开合中位误差为3.442厘米、0.901度、0.229厘米；平移按人等效尺度报告。开合归一化误差1.388，反而不如保持不变。[S24](https://arxiv.org/html/2610.37330v1#S4.p3.1) [S27](https://arxiv.org/html/2610.37330v1#S4.T1.2.1) 分段对比中，学习分段的平移误差3.022厘米，固定窗口3.451厘米，但各方法目标片段不同，且学习版本为单种子前期模型。[S28](https://arxiv.org/html/2610.37330v1#S4.SS1.p2.1) [S29](https://arxiv.org/html/2610.37330v1#S4.T2) [S30](https://arxiv.org/html/2610.37330v1#S4.T2.2) 真机有重建、迁移及闭环操作定性展示，不能据此推出任务成功率。[S31](https://arxiv.org/html/2610.37330v1#S4.SS3.p1.1) [S32](https://arxiv.org/html/2610.37330v1#S4.SS3.p2.1)

</details>

### 5. [Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution](items/Retrieve%20to%20Act%20Motion%20Primitive%20Graph%20Retrieval%20for%20Robust%20VLA%20Execution.md)

> Retrieve to Act（R2A）在视觉干扰让VLA动作跑偏时，从成功示范构成的运动图中找合适的后续，再与原动作融合。它用运动几何定位执行进度，原VLA保持冻结。

- **能借鉴什么**：值得借鉴的是把成功经验保留为可查询的结构，而非全部压进策略参数。若任务已有可复用示范、执行几何仍可信，检索“适合接下去的动作”可能比继续修补视觉特征更直接。
- **值得读吗**：值得读到图结构、初始校正和门控消融；它适合检验已有运动经验能否稳定执行，但不能当通用避障或恢复机制。

<details><summary>实验依据</summary>

LIBERO-Plus七类扰动下，加入R2A后GR00T N1.7从77.1%到89.0%，StableVLA从78.1%到89.5%，π0.5从85.9%到90.4%。[S22](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.p3.1) RoboTwin2.0-Plus中π0.5从56.8%到66.2%，初始状态扰动从34.2%到75.9%。[S24](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.fig1.1) 同一LIBERO-10比较中，π0.5加R2A为86.3%，加SDN为83.8%，但传感器噪声下SDN更好。[S26](https://arxiv.org/html/2610.37215v1#S5.SS0.SSS0.Px1.fig1.2) 真机最高增加40个百分点来自摘要，所给节选缺任务细节、试验次数和分项结果；这些数字不能跨论文直接排名。

</details>

## 扫读 7 篇

- [GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation](items/GAWM%20A%20Compact%20Latent%20World-Action%20Model%20for%20Multi-Task%20Robot%20Manipulation.md) — GAWM 让机器人先在压缩的视觉特征里预测“接下来场景会怎样”，再结合现在和未来的特征输出一段动作。它用冻结的 DINOv3 和轻量预测器，把世界预测接入不足 100M 参数的操作模型。
- [Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well](items/Pushing%20Dexterity%20and%20Safety%20for%20In-Hand%20Object%20Pose%20Reaching%20That%20Works%20Remarka.md) — 这篇让 LEAP 多指手连续把手中物体移到指定位置和朝向，并额外学习一个可调保守程度的残差安全过滤器来减少掉落。关键是把“完成目标”和“避免掉落”分别处理，再在真机上量化两者的取舍。
- [Ego-CEVR: Learning Cross-Embodiment Visual Representations from Human Egocentric Videos](items/Ego-CEVR%20Learning%20Cross-Embodiment%20Visual%20Representations%20from%20Human%20Egocentric.md) — Ego-CEVR 把“看懂任务进展”和“看清手边怎么接触”分开学习：前者从第一视角视频预测未来，后者从机器人腕部观察和动作标签学习。策略通过独立通路同时读取两种表示。
- [Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration using Deep Pixel-Point Correspondences](items/Generalizable%20Target-Less%20Joint%20Intrinsic-Extrinsic%20Camera-LiDAR%20Calibration%20usi.md) — 这篇从原始相机图像和激光雷达扫描出发，同时估计相机内部参数、镜头畸变以及两传感器的相对位置和朝向。关键是让像素与点云的匹配网络适应不同内参和畸变，再交替做匹配与几何优化。
- [When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies](items/When%2C%20Where%2C%20and%20What%20to%20Correct%20Human-Guided%20Adaptive%20Residual%20Correction%20for%20R.md) — ARC 专门修补机器人策略在精细操作处的局部失误，保留原策略不动，只学习附加纠正。人类纠正用来指出何时介入、往哪些方向探索，最终纠正动作由强化学习的任务奖励决定。
- [World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer](items/World%20Dreamer%20v5-lite%20A%20Multi-Robot%20World%20Action%20Model%20with%20One%20Dreamer.md) — World Dreamer v5-lite 让多个机器人先把看到的东西放进同一份有空间坐标的状态，再分别决定动作。巧处是让机器人共享观察、交换与姿态有关的信息，同时保留各自动作输出，避免把多摄像头画面简单堆在一起。
- [Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](items/Pretraining%20Knows%20What%2C%20Simulation%20Teaches%20How%20Compositional%20Generalization%20in%20a.md) — ZAP 把“理解要做什么”和“学会怎么动”分开：借用预训练视觉语言模型的理解能力，再通过简单仿真任务训练机器人操作。它通过工具接口控制机器人，训练期间不使用真实机器人数据。

## 其余存档 12 篇

- [Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling](items/Learning%20Quality-Controllable%20Robot%20Policies%20with%20Iterative%20Hindsight%20Relabeling.md) · 机器人学习 具身智能评测与基准
- [Vision-Language-Action or World-Action? Just Action Models](items/Vision-Language-Action%20or%20World-Action%20Just%20Action%20Models.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision](items/Omni-IGN%20Onboard%20Image-Goal%20Navigation%20for%20Drones%20with%20Omnidirectional%20Vision.md) · 智能体 Agent 机器人学习 Sim2Real 具身智能评测与基准
- [4D Reconstruction with Events & RGB](items/4D%20Reconstruction%20with%20Events%20%26%20RGB.md) · 具身智能评测与基准
- [CARD: Contact-Anchored Retargeting for Dexterous Manipulation](items/CARD%20Contact-Anchored%20Retargeting%20for%20Dexterous%20Manipulation.md) · 世界模型 机器人学习
- [GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers](items/GRAFT%20Geometry-Aware%20Residual%20Adaptation%20for%20Foundation%20Trackers.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- [SVIn+: Multi-Modal Framework for Robust Underwater State Estimation using 3D Sonar, Visual-Inertial, Water-Pressure, and DVL](items/SVIn%2B%20Multi-Modal%20Framework%20for%20Robust%20Underwater%20State%20Estimation%20using%203D%20Sona.md) · AI 核心知识地图
- [EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance](items/EgoThumb%20A%20Vision-Driven%20Supernumerary%20Robotic%20Thumb%20for%20Autonomous%20Grasp%20and%20Ho.md) · 机器人学习
- [Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](items/Zooming%20without%20Zooming%20v2%20From%20Seeing%20Details%20to%20Connecting%20Evidence%20for%20Genera.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [Remember Where You Walk: Learning Spatial Memory for End-to-End Legged Robot Exploration](items/Remember%20Where%20You%20Walk%20Learning%20Spatial%20Memory%20for%20End-to-End%20Legged%20Robot%20Expl.md) · 智能体 Agent 机器人学习
- [When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate](items/When%20Black-Box%20Robot%20Policies%20Fail%20Online%20Sensor%20Diagnosis%20and%20Repair%20with%20a%20Tra.md) · 多模态基础模型 视觉语言动作模型 VLA
- [SWIM: Learning What Matters from Behaviors for JEPA World Models](items/SWIM%20Learning%20What%20Matters%20from%20Behaviors%20for%20JEPA%20World%20Models.md) · 智能体 Agent 世界模型

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2495
- 入选条目：24
- 回填已见条目：0
- 最高分论文：ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning
- 最高分论文发布时间：2026-10-27T17:59:52Z
- 主要技术对象分类：具身智能评测与基准 14、多模态基础模型 12、机器人学习 12、视觉语言动作模型 VLA 11、世界模型 10、智能体 Agent 6、AI 核心知识地图 1、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
