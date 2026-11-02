---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-02
---

# 2026-11-02 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先追问：生成模型给出的未来，怎样才算有用、可信且经得起检验？想理解如何把视觉预测变成可用几何，先读 WorldFlow 的联合生成与消融；想控制模型已有能力，读 Q-adaptive，看它怎样逐步测量推理对动作的影响；想设计更难被表面结果蒙混的评测，读 WorldProbe 的空间记忆测试和 PaperBenchX 的干净重放。
> **趋势**：前五篇的共同线索：这些论文共同把关注点从“输出看起来合理”推进到“生成过程是否受控、结果是否可核验”：视频要对应三维运动和持久空间，动作引导要尊重生成机制，科学结论要由可重放的证据支撑。各篇实验支持的是这些具体环节，尚不能合起来证明通用物理理解或可靠自主科研。

- **规模**：2505 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 19、世界模型 10、智能体 Agent 9、多模态基础模型 5、机器人学习 5、视觉语言动作模型 VLA 3、AI 核心知识地图 2
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](items/WorldFlow%20Joint%20Video%20and%203D%20Motion%20Prediction%20via%20Large-Scale%20Pretraining.md)

> WorldFlow 同时生成未来视频和指定三维点的运动轨迹，让“画面怎么变”和“物体实际往哪里走”一起学习。关键是把三维位移也变成生成单元，与视频共享注意力和去噪过程。

- **能借鉴什么**：值得借鉴的是：需要几何输出时，可以把几何直接纳入生成目标，同时利用视频监督，而不必把生成像素当作必经中间结果。同一生成器的视频交给追踪器，轨迹仍逊于直接输出，进一步支持这个选择。[S32]
- **值得读吗**：值得读到联合生成、查询点编码和受控消融：它较清楚地证明了视频监督能帮助轨迹预测，但控制收益仍待验证。

<details><summary>实验依据</summary>

单帧预测协议覆盖仿真 Sim7、真实交互 Real3 和空间指令 SpatialCog，对比直接轨迹生成及视频生成后追踪。三组 ADE 分别为0.051、0.081、0.060米，均优于所测学习方法，但 Real3 相对最强外部基线仅改善4.7%。同骨干、数据和优化的 flow-only 消融在 SpatialCog 的 ADE/FDE 为0.136/0.248米，联合生成降至0.060/0.078米，较直接支持视觉监督的作用。[S26](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p1.1) [S27](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p2.1) [S28](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p3.1) [S29](https://arxiv.org/html/2610.39278v1#S4.T1.3.1) [S30](https://arxiv.org/html/2610.39278v1#S4.T1) [S31](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px1.p1.1)

</details>

### 2. [Coupled Guidance for Flow Matching](items/Coupled%20Guidance%20for%20Flow%20Matching.md)

> Coupled Guidance 解决流匹配模型被外加约束引导后容易失稳的问题。它在调整预测结果的同时协调调整噪声端表示，避免采样偏离训练时学过的噪声—数据配对关系。

- **能借鉴什么**：可以借鉴的诊断顺序是：引导越强反而越差时，先检查它是否把生成过程带离训练分布，而不只调整约束权重。这里把问题落实到噪声端与数据端的配对，提供了比“梯度太大”更具体的解释。
- **值得读吗**：已有流匹配采样器需要加约束时，值得读到更新公式和稳定性分析；收益依赖具体引导算子，不能当作通用替换件。

<details><summary>实验依据</summary>

ManiSkill3 PickCube 策略在原环境成功率99.8%；添加障碍后，无引导约21%，朴素能量引导最高36%，耦合引导最高81%，表注说明测试256个环境种子。[S33](https://arxiv.org/html/2610.40109v1#S5.T2) [S34](https://arxiv.org/html/2610.40109v1#S5.SS1.p2.1) [S35](https://arxiv.org/html/2610.40109v1#S5.SS1.p3.1) 还测试 Adroit 四任务，以及 ImageNet-128、CelebA-HQ-256 的补全、超分和去模糊。图像节选给出方法间表现，但未提供数值表和具体指标名，无法量化这些收益。

</details>

### 3. [How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function](items/How%20Much%20Should%20a%20VLA%20Trust%20Its%20Reasoning%20Step-Level%20Guidance%20as%20a%20Measured%20Acti.md)

> CoC-CFG 不判断 VLA 的推理文字是真是假，而是逐步调节它对动作生成的影响。Q-adaptive guidance 在训练场景里逐个试验权重、测量最终计划得分，再训练小型价值模型选择权重。

- **能借鉴什么**：最值得借鉴的是利用生成器“可存档、可回到同一步”的性质做局部反事实实验。能直接完成分支并评分时，就能测量当前控制器下某一步的作用，减少用整段奖励猜测各步贡献的困难。
- **值得读吗**：值得细读价值标签的测量和保守更新：方法的说服力在可控分支实验，适用前提是生成过程可重置且训练评分可得。

<details><summary>实验依据</summary>

Alpasim 用120场景训练、358场景开环评估，第三阶段相对原策略降低位移成本16.5%；另300场景闭环通过262个，原策略252个，责任碰撞7次对13次。[S17](https://arxiv.org/html/2610.40002v1#S5.SS1.SSS0.Px1.p1.1) [S18](https://arxiv.org/html/2610.40002v1#S5.SS1.SSS0.Px2.p1.1) [S19](https://arxiv.org/html/2610.40002v1#S5.SS1.SSS0.Px3.p1.1) Waymo 留出帧上第二阶段 RFS 为8.3032，最佳固定权重8.2412、SAC 8.2783；隐藏测试整个系统为8.135159，对照已发表最高8.079。[S21](https://arxiv.org/html/2610.40002v1#S5.T3.6) [S22](https://arxiv.org/html/2610.40002v1#S5.T4) [S23](https://arxiv.org/html/2610.40002v1#S5.T4.6) [S24](https://arxiv.org/html/2610.40002v1#S5.SS2.SSS0.Px2.p1.1) [S25](https://arxiv.org/html/2610.40002v1#S5.SS2.SSS0.Px4.p1.1) RFS 是对人类评分轨迹的计划评价，不是道路事故率。

</details>

### 4. [PAPERBENCHX: Can AI Reproduce Science Across Disciplines?](items/PAPERBENCHX%20Can%20AI%20Reproduce%20Science%20Across%20Disciplines.md)

> PaperBenchX 检查智能体能否把跨学科论文中的关键实验变成别人可以重新运行的证据。它把提交物放进干净环境重跑，只给重新生成且符合科学要求的结果计分。

- **能借鉴什么**：可借鉴的是把“能重新运行”和“支持科学主张”拆开验证。给科研智能体设验收条件时，应同时要求原始输出、收敛记录和从输出推导结论的过程，避免一张像论文的图掩盖错误模型。
- **值得读吗**：值得读到任务合同、评分叶节点和失败案例：最有用的贡献是规定什么证据才算完成，而非单看排行榜。

<details><summary>实验依据</summary>

93项任务覆盖12个研究领域、10种环境，测试10个智能体配置。最佳配置平均部分得分59.08%，但仅13项超过严格大于90%的完整复现阈值，完整率13.98%；71项没有任何配置完成。[S7](https://arxiv.org/html/2610.39744v1#S1.p5.1) [S18](https://arxiv.org/html/2610.39744v1#S4.SS2.SSS0.Px1.p1.1) [S29](https://arxiv.org/html/2610.39744v1#A2.SS1.SSS0.Px1.p1.1) 平均建模、执行、验证得分分别62.73%、61.83%、42.91%，支持验证是突出薄弱环节，但未单独证明低分的因果来源。

</details>

### 5. [WorldProbe: When Video World Models Fall Apart under Long-Horizon Spatial Exploration](items/WorldProbe%20When%20Video%20World%20Models%20Fall%20Apart%20under%20Long-Horizon%20Spatial%20Explora.md)

> WorldProbe 让智能体边看新画面边选择相机动作，持续探索视频模型生成的世界。它检查的不只是画面清晰度，还包括转身重看、换角度观察和进入新区后，世界是否仍然自洽。

- **能借鉴什么**：值得借鉴的是把评测动作交给能根据结果继续探索的控制者：新出现一条走廊，就进去再回看，而不是只播放预设路线。这能把局部好看与空间持久性分开检验，也让失败更接近实际交互。
- **值得读吗**：值得读任务设计、记忆指标和筛选规则；它能揭露短视频评分遗漏的失败，但排名须结合控制与筛选误差理解。

<details><summary>实验依据</summary>

164个用例、10个公开模型，生成超过1600条轨迹、约800分钟视频，最长180秒（摘要）。局部评估报告均值与随时间斜率：LingBot-World v2 内容分7.55、斜率−0.015分/秒；Matrix-Game 3.0 视觉斜率虽为正，内容斜率仍为−0.051分/秒。[S14](https://arxiv.org/html/2610.39721v1#S4.T4) [S15](https://arxiv.org/html/2610.39721v1#S4.T4.4) [S16](https://arxiv.org/html/2610.39721v1#S4.SS1.p1.1) 长程节选描述物体消失、复制和身份漂移，但未给记忆与演化的数值表，不能据此量化谁最会维持世界。

</details>

## 扫读 7 篇

- [Utility-WAM: Correcting Future-Induced Action Changes](items/Utility-WAM%20Correcting%20Future-Induced%20Action%20Changes.md) — 让机器人先“想象未来”有时会把原本正确的动作带偏。Utility-WAM 修正未来信息引起的速度变化，并在预计无益时跳过视频生成，兼顾精细操作和推理开销。
- [DAWN: Diffusion-based Alignment and unfastening Workflow Network](items/DAWN%20Diffusion-based%20Alignment%20and%20unfastening%20Workflow%20Network.md) — DAWN 把机器人拆螺丝分成“对准并插入”和“施力旋出”，再用多模态检测判断何时切换。关键是先确认螺丝刀已经接合，再进入需要稳定力控制的阶段。
- [Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design](items/Improving%20Fine-Grained%20Manipulation%20through%20Demonstration%20Expansion%20and%20Executio.md) — DEED 同时处理“示范怎么扩充”和“预测动作怎么执行”：让训练数据覆盖不同指令与画面，再把动作块通过合适的控制转换和闭环重规划送到机器人。它提醒我们，精细操作成绩不能只归因于策略网络。
- [LLM-guided Planar Loco-Manipulation for Quadruped Robots](items/LLM-guided%20Planar%20Loco-Manipulation%20for%20Quadruped%20Robots.md) — 这篇让四足机器人把“挡路物可以推开”纳入导航计划。语言规划器同时选择技能、操作哪个物体和推到哪里，再交给强化学习控制器执行，而不是只输出移动方向。
- [Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment](items/Kinematic-Tactile%20Aligned%20Dexterous%20Retargeting%20with%20Contact%20Wrench%20Space%20Alignm.md) — 这篇不只把人的手势转换成机器人手势，还要传递“这样接触能对物体施加哪些力和力矩”。它用接触力旋量空间对齐两种手的受力能力，再把所需指尖力转换为可回放的关节位置修正。
- [Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory](items/Ask%20to%20Evolve%20A%20Unified%20Harness%20for%20Lifelong%20Embodied%20Navigation%20with%20Hybrid%20Act.md) — EvoLife 让导航智能体同时决定怎么走、何时求助，以及把什么经历记下来供下次使用。关键是把多种移动方式、主动交互和绑定地点的持久记忆放进同一个导航系统。
- [Cross-Controller Transfer via In-Context Behavior Adaptation](items/Cross-Controller%20Transfer%20via%20In-Context%20Behavior%20Adaptation.md) — Cross-Controller Transfer 用“发了什么动作、机器人实际怎么动”的示例，让同一个策略判断当前控制器的行为。它处理的是一个容易被忽视的数据冲突：相同动作数值，在不同控制器下可能代表不同运动。

## 其余存档 12 篇

- [Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection](items/Tactus%20Tactile%20%26%20Pose%20Sensing%20Glove%20for%20Natural%20Dexterity%20Data%20Collection.md) · 世界模型 机器人学习 具身智能评测与基准
- [A Tutorial on Shape Servoing of Deformable Objects-Part I: Fundamentals](items/A%20Tutorial%20on%20Shape%20Servoing%20of%20Deformable%20Objects-Part%20I%20Fundamentals.md) · AI 核心知识地图
- [AI for Science in Space: Orbital Laboratories, Planetary Fieldwork, and Embodied Autonomy](items/AI%20for%20Science%20in%20Space%20Orbital%20Laboratories%2C%20Planetary%20Fieldwork%2C%20and%20Embodied.md) · 具身智能评测与基准
- [Language-Grounded Force/Torque Pretraining for Extrinsic Contact Perception](items/Language-Grounded%20Force%20Torque%20Pretraining%20for%20Extrinsic%20Contact%20Perception.md) · 世界模型
- [Robotic Data Inoculation](items/Robotic%20Data%20Inoculation.md) · 机器人学习 具身智能评测与基准
- [Is It the Curriculum or Just the Easy Start? Benchmarking Unsupervised Environment Design on Quadrupeds](items/Is%20It%20the%20Curriculum%20or%20Just%20the%20Easy%20Start%20Benchmarking%20Unsupervised%20Environmen.md) · 世界模型 具身智能评测与基准
- [RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories](items/RFW-A%20Agentic%20Procedural%20Generation%20of%20400K%20Articulated%20Assets%20over%20500%20Categori.md) · 智能体 Agent 世界模型
- [SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU](items/SONIC-K1%20Porting%20a%20Universal%20Humanoid%20Motion%20Tracker%20to%20a%20Small%20Humanoid%20on%20a%20Si.md) · 世界模型 具身智能评测与基准
- [CuBot-STT: Simultaneously Transport and Tighten for Lattice-type Modular Reconfiguration Robot](items/CuBot-STT%20Simultaneously%20Transport%20and%20Tighten%20for%20Lattice-type%20Modular%20Reconfig.md) · 智能体 Agent 具身智能评测与基准
- [V-CAPE: Visual Consistency Assessment for Product Image Editing](items/V-CAPE%20Visual%20Consistency%20Assessment%20for%20Product%20Image%20Editing.md) · 多模态基础模型 具身智能评测与基准
- [Wizard: Manipulate Any World in Real Time via Agentic Control](items/Wizard%20Manipulate%20Any%20World%20in%20Real%20Time%20via%20Agentic%20Control.md) · 智能体 Agent 世界模型
- [RoboAtom: Large-scale Atomic-Action Supervision for Robot Learning](items/RoboAtom%20Large-scale%20Atomic-Action%20Supervision%20for%20Robot%20Learning.md) · 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2505
- 入选条目：24
- 回填已见条目：0
- 最高分论文：WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining
- 最高分论文发布时间：2026-10-29T03:30:27Z
- 主要技术对象分类：具身智能评测与基准 19、世界模型 10、智能体 Agent 9、多模态基础模型 5、机器人学习 5、视觉语言动作模型 VLA 3、AI 核心知识地图 2
- 信息源错误：0
- 自动恢复信息源：0

</details>
