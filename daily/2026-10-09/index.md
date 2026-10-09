---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-09
---

# 2026-10-09 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人缺的是哪些信息，以及怎样把这些信息变成可执行的改进。想研究有限试错预算怎么分配，先读 EmbodiedRSI 的配对实验和选实验规则；想弄清触觉收益来自数据还是接入方式，对照读 TouchScale 与 OpenViTac；想理解视频预测怎样真正带动动作，重点读 VPP2 的分阶段训练。HuMBLE 则适合检查另一种路径：训练时借助完整示范，部署时只留下简洁的控制接口。
> **趋势**：前五篇的共同线索：这些论文都在处理“已有能力怎样变成可靠执行”：补充操作视频或触觉监督、保留人体动作风格，或通过有目的的试验修正执行层。共同点是把学习过程拆开，让额外信息在合适阶段发挥作用；各篇实验并不能支持某一种路线普遍优于其他路线。

- **规模**：2404 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 23、世界模型 12、多模态基础模型 12、智能体 Agent 12、视觉语言动作模型 VLA 6、机器人学习 5、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution](items/EmbodiedRSI%20Active%20Continual%20Robot%20Learning%20Through%20Hypothesis-Guided%20Co-Evoluti.md)

> EmbodiedRSI 不改机器人基础模型，而是改围绕它运行的代码、技能和记忆。关键是每次试验先问“这次能分清哪些改进是否有效”，再按信息收益与成本决定试什么。

- **能借鉴什么**：可借鉴的是把失败后的修改写成可区分的假设，并用同起点对照检验。试错昂贵、候选改动相互影响时，这比凭一次成功保留修改更可靠。
- **值得读吗**：值得读到选实验规则和消融结果，因为真正有用的贡献是试验分配与归因，而不只是成功率。

<details><summary>实验依据</summary>

RoboCasa365 仿真总体成功率为 77.0%，Harness VLA 为 63.6%；未见组合任务为 71.3% 对 40.1%，后者不是基线总体成绩 [S43](https://arxiv.org/html/2610.10498v1#S4.T1.4.1)。演化和评估使用互不重叠种子 [S29](https://arxiv.org/html/2610.10498v1#S4.SS1.p1.1)。LIBERO-Pro 为 86.8%，真机为 71.3% [S8](https://arxiv.org/html/2610.10498v1#S1.p5.1)，但节选缺少对应完整比较及真机试验数量。成绩支持执行层适应有效；学习效率表只有标题，不能据此量化节省多少试验。

</details>

### 2. [OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework](items/OpenViTac%20Learning%20and%20Benchmarking%20Visuo-Tactile%20Policies%20in%20a%20Unified%20Sim-and-.md)

> OpenViTac 把需要触觉的操作做成对应的仿真与真机测试；OpenVTLA 则把短时间触觉历史编码成小量 token，直接送进已有 VLA。它让“触觉有没有帮助”和“怎样接入触觉”更容易分开检验。

- **能借鉴什么**：接触状态随时间变化，未必能从一帧触觉图判断。这里值得尝试的是先用适合触觉历史的表示，再检验简单拼接是否已经足够，避免先增加复杂融合结构。
- **值得读吗**：值得读基准协议与受控表示实验；要复现最佳接入方式，还需核查参数更新范围和比较条件。

<details><summary>实验依据</summary>

每个任务单独训练策略，平均值为任务成功率的等权平均 [S35](https://arxiv.org/html/2610.10384v1#S4.SS1.p2.1)。仿真 OpenVTLA 为 68.7%，FTP-1 为 61.2%，最强 VLA 为 51.5% [S37](https://arxiv.org/html/2610.10384v1#S4.T2.8)；真机为 54.6%、51.9% 和 43.1% [S39](https://arxiv.org/html/2610.10384v1#S4.T3.8)。七种方法在八个共享任务上的两域平均分 Pearson r=0.967，支持相对排序一致 [S42](https://arxiv.org/html/2610.10384v1#S4.SS2.p3.1)。输入有冲突：引言的 WAM 成绩为仿真 53.3%、真机 48.5%，所给表格及结果段却不一致，因此不采用这组比较。

</details>

### 3. [Video Prediction Policy 2: Predict Better, Act Better](items/Video%20Prediction%20Policy%202%20Predict%20Better%2C%20Act%20Better.md)

> VPP2 先把视频模型训练成能按指令预测操作过程的模型，再压缩预测计算并接入动作专家。巧处是先学清完整动作事件，再统一预测时间尺度，避免视频先验在动作训练中被扰乱。

- **能借鉴什么**：值得借鉴的是区分两种学习目标：完整事件建立“这条指令会产生什么过程”，固定时长预测建立“接下来多久会发生什么”。这让语义学习和动作时间对齐各有合适的数据单位。
- **值得读吗**：值得深入读训练顺序和消融，因为它解释了视频先验如何变得可用，比只研究动作头更有启发。

<details><summary>实验依据</summary>

视频指令遵循测试中，人手/机器人得分分别为 0.80/0.90，Cosmos3-64B 为 0.70/0.78 [S38](https://arxiv.org/html/2610.10270v1#S4.T2.1)。真机 ALOHA 十类零样本任务平均成功率 58.5%，π₀.₅ 为 40.0%，Fast-WAM 为 20.5% [S6](https://arxiv.org/html/2610.10270v1#S1.p4.1)。专门后训练后，LIBERO-Pro 为 45.0% 对最强基线 11.0%，LIBERO-OOD 为 63.9%，RoboDojo 为 29.47% [S6](https://arxiv.org/html/2610.10270v1#S1.p4.1)。后三项不能当零样本结果；视频测试样本量和判定细节未提供。

</details>

### 4. [HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion](items/HuMBLE%20Human%20Motion-Driven%20Behavior%20Learning%20for%20Embodied%20Locomotion.md)

> HuMBLE 先让看得见完整人体参考动作的老师教会机器人自然走路，再把能力教给只看自身状态和速度指令的小策略。随后同时练习任意速度跟踪和人体动作模仿，扩展可控范围而保留步态风格。

- **能借鉴什么**：可借鉴的是先把“物理上实现示范”和“用少量指令重建协调动作”分开学，再用示范任务约束后续强化学习。模仿数据因此既提供起点，也在扩展能力时防止风格漂移。
- **值得读吗**：值得读到双任务微调与初始化细节，因为这才决定自然步态能否在数据外指令下保留下来。

<details><summary>实验依据</summary>

训练和主要定量测试在 Isaac Lab，部分响应、覆盖和鲁棒性测试另用 MuJoCo 验证；Atlas R1、D1 和 G1 有真机部署 [S11](https://arxiv.org/html/2610.10489v1#Sx2.p1.1) [S12](https://arxiv.org/html/2610.10489v1#Sx2.p2.1)。G1 仿真消融中，直接训练基线在三类动作的线速度、角速度和关节误差比 HuMBLE 先验高 16.36%、54.85%、70.87%，侧步还退化到近站立 [S20](https://arxiv.org/html/2610.10489v1#Sx2.SSx6.SSSx1.p4.1)。这支持蒸馏的作用，但不等于最终真机鲁棒性增益；所给节选缺最终跟踪、抗扰与计算开销数字。

</details>

### 5. [TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning](items/TouchScale%20500%20Hours%20of%20Human%20Vision%20and%20Touch%20for%20Visual-Tactile%20Learning.md)

> TouchScale 用统一设备记录大规模同步人类视频与双手压力，让模型学习画面背后的接触信息。机器人先用这些无动作标签的人类数据做视觉—触觉中间训练，再用机器人示范学控制，无需把人手动作转换成机器人动作。

- **能借鉴什么**：人类数据不必提供可直接执行的机器人动作，也能帮助控制学习：先用同步触觉让模型学会理解接触，再用少量机器人数据建立动作对应。统一采集还让规模实验更容易解释。
- **值得读吗**：值得读数据协议与机器人对照实验，因为它给出了不依赖人机动作对齐的数据利用路径，但规模结论仍有测试范围。

<details><summary>实验依据</summary>

未见传感器 EgoTactile 上，接触 IoU 从以 EgoTouch 训练的 0.134 到全量 TouchScale 的 0.383；同为 16 小时的 TouchScale 子集为 0.181 [S6](https://arxiv.org/html/2610.10288v1#S1.p3.1)。xArm6 与 Revo 2 手上四项任务各收集 50 个示范，中间训练使平均真机成功率从 22.5% 到 57.5% [S17](https://arxiv.org/html/2610.10288v1#S4.F5) [S18](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px3.p1.1)。规模从 20% 到全量时为 30.0%、32.5%、50.0%、50.0%、57.5%，是总体上升而非严格递增 [S19](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px4.p1.1)。测试轮数未在节选给出。

</details>

## 扫读 7 篇

- [Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving](items/Explicit%20Geometric%20Chain-of-Thought%20for%20Vision-Language-Action%20in%20Autonomous%20Dri.md) — GeoCoTDrive 让自动驾驶模型先圈出影响决策的画面区域，再从这些区域取三维几何信息来生成行驶轨迹。关键是把“看懂什么”接到“那里实际有什么空间约束”上。
- [RoboJEPA: Scaling Robotic Latent World Models](items/RoboJEPA%20Scaling%20Robotic%20Latent%20World%20Models.md) — RoboJEPA 在内部特征空间预测机器人行动后的未来，并研究投入更多计算后，这种预测和规划能力能否提前估算。它还展示了以一张目标图片为任务目标、直接在真机上规划的用法。
- [RoboQuest: Generalist Physical Agents that Search, Inspect and Test](items/RoboQuest%20Generalist%20Physical%20Agents%20that%20Search%2C%20Inspect%20and%20Test.md) — RoboQuest 检验机器人能否为了完成任务，主动找东西、检查隐藏属性、试用陌生工具，并根据证据调整行动。它揭示的瓶颈是：会执行动作，还不代表知道何时该继续探索。
- [Argos: Adapt Rich Geometric Priors for Generalizable Online Scene-Change-Detection](items/Argos%20Adapt%20Rich%20Geometric%20Priors%20for%20Generalizable%20Online%20Scene-Change-Detectio.md) — Argos 利用几何基础模型的空间知识，联合判断场景哪里变了、场景的三维结构是什么。Argos-SLAM 则把这种能力接到在线系统中，随环境变化更新地图。
- [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](items/Agentic%20RSR%20Real-to-Sim-to-Real%20through%20Scene%20Reconstruction%20and%20Execution-Groun.md) — Agentic RSR 把重建工作台、在仿真里写策略、再到真机执行连成一个由同一任务驱动的流程。它不仅追求场景看起来像，还检查任务交互，并让策略逐步改用真机能够获得的视觉信息。
- [Temporal Visuo-Tactile Learning for Dexterous Grasp Stability](items/Temporal%20Visuo-Tactile%20Learning%20for%20Dexterous%20Grasp%20Stability.md) — Temporal Visuo-Tactile 用抬起物体前的一段视觉、手部状态和指尖触觉，预测抬起后能否抓稳。关键是读取接触随时间的变化，再把预测器当作真机起抬的检查关口，不稳就重新抓。
- [RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments](items/RobotWorld%20Benchmarking%20Multimodal%20Agents%20for%20Robot%20Use%20Across%20Diverse%20Tasks%20and.md) — RobotWorld 检查通用多模态智能体能否通过机器人接口，把指令真正执行成物理任务。它同时看结果和执行轨迹，发现会搭建复杂感知控制流程，并不保证能持续跟住任务状态、纠错和正确判断完成。

## 其余存档 12 篇

- [Benchmarking Behavioral Steerability in Behavior Foundation Models](items/Benchmarking%20Behavioral%20Steerability%20in%20Behavior%20Foundation%20Models.md) · 多模态基础模型 具身智能评测与基准
- [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](items/Do%20Vision-Language-Action%20Models%20Understand%20Instructions%20A%20Mechanistic%20Interpret.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Self-correction Optimization for Interleaved Multimodal Generation](items/Self-correction%20Optimization%20for%20Interleaved%20Multimodal%20Generation.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [NeRFifyMesh: Optimizing Neural Radiance Fields from Textured Meshes for Robotics Scene Building](items/NeRFifyMesh%20Optimizing%20Neural%20Radiance%20Fields%20from%20Textured%20Meshes%20for%20Robotics.md) · 世界模型 具身智能评测与基准
- [Lifelong small-object navigation in changing object layouts: a benchmark and method](items/Lifelong%20small-object%20navigation%20in%20changing%20object%20layouts%20a%20benchmark%20and%20meth.md) · 智能体 Agent 具身智能评测与基准
- [ECHO: Embodied Camera Observations of Human Object Carrying](items/ECHO%20Embodied%20Camera%20Observations%20of%20Human%20Object%20Carrying.md) · 智能体 Agent 具身智能评测与基准
- [Decoding Neural Population Dynamics through Robotic Analog](items/Decoding%20Neural%20Population%20Dynamics%20through%20Robotic%20Analog.md) · 多模态基础模型 世界模型 机器人学习 具身智能评测与基准
- [ΔWAM: Distilling Action Tangent Fields into World Action Models](items/%CE%94WAM%20Distilling%20Action%20Tangent%20Fields%20into%20World%20Action%20Models.md) · 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Contact-Aware Imitation Learning Through Contact Factorization](items/Contact-Aware%20Imitation%20Learning%20Through%20Contact%20Factorization.md) · 机器人学习
- [Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation](items/Predicted%20Futures%20Are%20Not%20Enough%20Learning%20Executable%20Goals%20for%20Robot%20Manipulatio.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [Kuration SDK: Addressing the Virtual2Real Gap via Data Curation](items/Kuration%20SDK%20Addressing%20the%20Virtual2Real%20Gap%20via%20Data%20Curation.md) · 世界模型 具身智能评测与基准
- [RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment](items/RT-Safe%20Benchmarking%20Agent%20Safety%20in%20Real-Time%20Embodied%20Environment.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2404
- 入选条目：24
- 回填已见条目：0
- 最高分论文：EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution
- 最高分论文发布时间：2026-10-07T17:48:02Z
- 主要技术对象分类：具身智能评测与基准 23、世界模型 12、多模态基础模型 12、智能体 Agent 12、视觉语言动作模型 VLA 6、机器人学习 5、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
