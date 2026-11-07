---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-07
---

# 2026-11-07 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人策略究竟该从预训练模型继承什么，以及怎样让训练信号真正服务于控制。先读 La-JEPA，理解如何保留视觉知识、重新设计小策略；再读 Concertina，对照理解让共享骨干直接生成连续动作的另一条路线；若更关心执行中何时介入，读 VLA-Tug，重点看失败前监督和校准失效边界。
> **趋势**：前五篇的共同线索：这些工作共同把注意力从模型规模转向监督和执行路径：未来预测、物理坐标误差、空间教师分别约束策略学什么，失败探针和类型契约则约束何时报警、如何执行。但各篇的数据、预训练和评测协议不同，不能据此直接排总榜。

- **规模**：2437 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、多模态基础模型 16、机器人学习 13、世界模型 12、视觉语言动作模型 VLA 10、智能体 Agent 9、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [La-JEPA: Compact Robot Policies with Latent World Modeling](items/La-JEPA%20Compact%20Robot%20Policies%20with%20Latent%20World%20Modeling.md)

> La-JEPA 保留预训练视觉编码器，把负责控制的策略重新做小：训练时同时学习未来特征和动作，执行时只生成动作。关键是让预测未来的训练信号改善策略，而不让机器人每次行动前都生成未来。

- **能借鉴什么**：值得借鉴的是把“借用预训练表示”和“继承预训练策略架构”拆开。如果任务需要紧凑控制器，可以先比较好的视觉特征加小策略，再判断是否值得承担大生成骨干的成本。
- **值得读吗**：值得读到注意力掩码和消融：它最有用的贡献是解释为何训练时预测未来，可以帮助一个执行时不预测未来的小策略。

<details><summary>实验依据</summary>

仿真覆盖 LIBERO-Plus、RoboTwin 2.0；[S6](https://arxiv.org/html/2611.08156v1#S1.p4.1) 报告在无具身预训练组领先，部署参数约为次优策略的四分之一，相对 Fast-WAM 最多快 5 倍，但节选未给仿真成功率全表。真机四项任务中，La-JEPA 平均成功次数为 17.50/20，π0.5 为 17.25/20，Fast-WAM 为 16.00/20；策略调用延迟分别为 25.16、71.89、88.09 毫秒。[S18](https://arxiv.org/html/2611.08156v1#S5.T5) [S19](https://arxiv.org/html/2611.08156v1#S5.T5.2) [S20](https://arxiv.org/html/2611.08156v1#S5.SS5.p1.1) 这支持有限任务上的竞争力，延迟也不是控制闭环周期。

</details>

### 2. [Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](items/Concertina%20Embodying%20Manipulation%20and%20Cognition%20in%20One%20Diffusion%20Vision-Language.md)

> Concertina 让同一个扩散视觉语言骨干直接生成连续动作，不再另接动作生成专家。每个控制时刻的完整动作压成一个连续 token，再由共享 Transformer 按时间块恢复轨迹。

- **能借鉴什么**：可借鉴的不是单纯删除动作头，而是让表示、损失和生成方式一致：连续动作进入骨干，误差也在物理坐标计算。尤其要检查不同坐标的数值尺度，否则很小的平移数值会让训练忽略实际重要的位置误差。
- **值得读吗**：值得细读动作表示、分块训练和坐标权重；其说服力在于展示共享骨干怎样承担控制，而非“认知与动作统一”的命名。

<details><summary>实验依据</summary>

仿真中，常规 LIBERO 的 2,000 回合成功率为 98.15%，X-VLA 为 98.1%；LIBERO-Plus 为 85.9%，EFFVLA 为 79.8%。CALVIN 在未见环境 D 的 1,000 条指令链上平均完成 4.142 项，高于 LLaDA-VLA 的 4.01，但低于 X-VLA 的 4.43。[S13](https://arxiv.org/html/2611.07513v1#S4.SS1.p1.1) [S15](https://arxiv.org/html/2611.07513v1#S4.SS2.p1.1) [S16](https://arxiv.org/html/2611.07513v1#S4.T2.2.1) 受控训练实验中，物理坐标加权且启用状态遮蔽时，AvgLen 从 0.406 到 1.837。[S18](https://arxiv.org/html/2611.07513v1#S4.SS3.SSS0.Px2.p1.1) 这支持共享骨干可行，也说明训练配方很关键。

</details>

### 3. [Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing](items/Failure%20Prediction%20and%20Classification%20in%20Vision-Language-Action%20Models%20Via%20Calib.md)

> VLA-Tug 在机器人策略的内部表示上训练小探针，提前判断会不会失败、可能怎样失败。关键改动是学习失败发生前的信号，并同时校准误报和提前检出要求。

- **能借鉴什么**：最值得借鉴的是把监督标签对准介入时机：如果目标是预防事故，就要用事故之前的证据训练和评估。另一个实用点是允许校准回答“现有模型无法满足要求”，而不是强行给出一个看似可靠的阈值。
- **值得读吗**：值得读到标签定义、校准拒绝条件和逐设置结果；它对“报警是否来得及”的处理，比摘要中的最高提升更值得关注。

<details><summary>实验依据</summary>

研究覆盖两个 VLA、两个仿真环境的 228 个任务及 8 个真机任务。[S10](https://arxiv.org/html/2611.08425v1#S1.p5.1) 未见任务六种设置中四种领先；相对 SAFE-LSTM，提前检测曲线面积在 new-task 为 −1%，new-skill 为 +30%，并非全面领先。[S32](https://arxiv.org/html/2611.08425v1#S6.F5) [S33](https://arxiv.org/html/2611.08425v1#S6.SS1.SSS0.Px4.p1.1) 已见任务所有获认证运行满足双目标；未见任务中 FPR、提前 TPR 目标分别在 40–86%、57–90% 的运行成立。[S34](https://arxiv.org/html/2611.08425v1#S6.I1.i1) 探针每步低于 1 毫秒。[S11](https://arxiv.org/html/2611.08425v1#S1.I1.i1)

</details>

### 4. [Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems](items/Don%27t%20Prompt%20Your%20Agents.%20Equip%20Them%20Skillware%20as%20a%20Modular%20Standard%20for%20Soverei.md)

> Skillware 把反复需要的执行逻辑做成带类型契约、版本和测试的软件包，让模型主要负责选能力、填参数。它把临场写代码改成调用已准备好的程序，并在执行前检查参数和约束。

- **能借鉴什么**：可以借鉴的是先划清稳定算法与开放判断：校验、计算、格式转换等已有明确规则的工作，应尽量交给可测试程序。模型继续处理意图与工具选择，既节省生成，也让错误更容易定位到参数、选择或程序本身。
- **值得读吗**：值得按工程设计文档读契约和运行时，实验结论则应先复核基准口径及普通工具组的配置，暂不接受普遍确定性的强结论。

<details><summary>实验依据</summary>

Skillware-Bench 的模拟工作流比较现场写代码、普通工具调用、完整 Skillware 三组。通过率依次为 58.2%、71.4%、91.8%；普通工具组参数错误率为 14.2%，完整组为 0.0%，安全拦截率从 82.6% 到 92.4%。[S42](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.Px1.p1.1) 另有每次成功调用 token 中位数从 5,520 到 1,620 的结果。[S19](https://arxiv.org/html/2611.07652v1#S5.SS3.p4.1) 这些支持封装与执行检查在该基准有效，尚不能证明跨领域普遍可靠或机器人能力。

</details>

### 5. [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](items/SLA%20Scaling%20Spatial-Language-Action%20Model%20via%20Continual%20Pre-training.md)

> SLA 在继续训练 π0.5 时，让内部视觉特征同时向冻结的三维感知教师学习，再把这种监督保留到下游适配。部署时移除教师和辅助模块，策略仍按原来的方式生成动作。

- **能借鉴什么**：可借鉴的是把训练时可获得、部署时不方便获得的信息转成表示监督。数据集几何标注不齐全时，也不必一律丢弃：教师可以利用已有标注，策略则学习部署时实际可用的视觉输入。
- **值得读吗**：值得读到数据统一、门控和双阶段消融；它提供了一条不增加部署结构、却能利用异构几何监督的具体路线。

<details><summary>实验依据</summary>

LIBERO-Plus 的 10,030 次评估成功率为 87.4%；RoboTwin Clean2Random 为 72.3%；RoboCasa-Panda 每任务用 50 条下游示范达到 68.4%。真机 RoboDojo-Real 三种机器人上，SLA 为 33.9%，π0.5 为 12.8%；八种自建部署条件平均为 83.8%，高出 π0.5 24.0 个百分点。[S9](https://arxiv.org/html/2611.08373v1#S1.p6.1) 后者按对象计成功，不能当作整回合成功率。[S26](https://arxiv.org/html/2611.08373v1#S4.SS1.p6.1) 结果支持多种场景的有效性，单个机制贡献还需消融。

</details>

## 扫读 7 篇

- [Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](items/Open-HumanWAM%20An%20Open%20Recipe%20for%20Scaling%20Human%20and%20Robot%20Experience%20for%20Embodied.md) — Open-HumanWAM 研究怎样把大量人类第一视角操作视频变成机器人可用的经验：先整理手部运动和语言标注，再比较纯人类数据与人机混合预训练。关键在于把数据规模、训练配方和机器人闭环表现放到一起验证。
- [AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction](items/AffectiveVLA%20Safe%20and%20Intent-Aware%20VLA%20Control%20for%20Human-Humanoid%20Social%20Interac.md) — AffectiveVLA 让人形机器人先判断人是否想握手、碰拳或拥抱，再决定是否启动 VLA 动作。它同时用接触顺应控制和独立语音停止机制，分别处理误启动与接触中的控制问题。
- [Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks](items/Kinematic%20Hypothesis%20Context%20Embodiment-Conditioned%20Learned%20Video%20Coding%20for%20Ban.md) — Kinematic Hypothesis Context 利用机器人关节状态、机体模型和相机标定，先预测机器人运动会怎样改变画面，再辅助视频压缩。接收端能自行重建的视觉变化，就不必完全依赖图像码流传过去，从而给远程策略保留更多有效信息。
- [OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions](items/OopsieRecover%20Learning%20Transferable%20VLA%20Corrections%20from%20Semantic%20Interventions.md) — OopsieRecover 不只让 VLA 记住“这个画面下应该怎么纠正”，而是从少量纠正示范推断为什么原行为不合适。它把推断出的知识转成空间表示和条件代价，用来引导策略避开同类错误。
- [Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement](items/Learning%20the%20Task%20or%20Learning%20the%20Verifier%20Rethinking%20Criteria%20Exposure%20in%20Embod.md) — Criteria Exposure 追问：让具身编程智能体看到成功判定规则后，它学会的是完成任务，还是满足检查条件？受控实验发现，原规则下的分数优势经不起符合原指令的小幅规则改动，跨任务迁移也较差。
- [Learning Robotic World Models with Semantic and Visual Feedback](items/Learning%20Robotic%20World%20Models%20with%20Semantic%20and%20Visual%20Feedback.md) — RoboImagine让机器人世界模型针对同一组观察、动作和指令生成多个未来，再同时按“任务进展是否合理”和“画面是否准确”比较它们。它用这些比较继续训练模型，解决只学像素容易忽略任务、只看语义又容易放过画面错误的问题。
- [MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation](items/MOMASPLAT%20Dynamic%20Novel-View%20Demonstration%20Augmentation%20for%20Mobile%20Manipulation.md) — MOMASPLAT把已有操作示范重新制作成“机器人从其他底座位置观察并执行”的训练样本，连物体接触后的运动也一起重建。关键是既改画面，也按运动学变换动作，让新视角下看到的操作与要执行的动作对应。

## 其余存档 12 篇

- [RoboARCade: Benchmarking Agentic Robot Control](items/RoboARCade%20Benchmarking%20Agentic%20Robot%20Control.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation](items/TactileLab%20Sim-to-Real%20Dexterous%20Robot%20Manipulation%20with%20Efficient%20Shear-Sensiti.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习 Sim2Real
- [Social Humanoid: Socially Responsive Human-Humanoid Interaction](items/Social%20Humanoid%20Socially%20Responsive%20Human-Humanoid%20Interaction.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [AffordJEV: Affordance Grounding by Confirming Candidate Regions](items/AffordJEV%20Affordance%20Grounding%20by%20Confirming%20Candidate%20Regions.md) · 多模态基础模型
- [Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token Reduction and Physics-Aware Augmentation](items/Towards%20Real-Time%20Full-Waveform%20LiDAR%20Transformers%20via%20Intensity-Guided%20Token%20Re.md) · 具身智能评测与基准
- [Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging](items/Efficient%20Diffusion%20Policy%20Fine%20Tuning%20with%20Latent%20Noise%20Representation%20Bridging.md) · 机器人学习
- [T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models](items/T3R%20Training-Free%20Two-Stage%20Token%20Refinement%20Towards%20Efficient%20and%20Robust%20VLA%20Mo.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation](items/Spatial-UMI-Dream%20Scaling%20World%20Action%20Models%20with%20Metric%20Geometry%20for%20UMI%20Manip.md) · 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines](items/RM-VLM%20From%20Natural-Language%20Task%20Descriptions%20to%20Vision-Grounded%20Reward%20Machine.md) · 多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- [Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation](items/Semantics-to-Contact%20A%20Stagewise%20Framework%20for%20Robust%20Contact-Rich%20Manipulation.md) · 多模态基础模型 世界模型 机器人学习 具身智能评测与基准
- [MAC-v2: Long-horizon model-based value expansion from pixels](items/MAC-v2%20Long-horizon%20model-based%20value%20expansion%20from%20pixels.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [GPWM: Modeling the World as 3D Particle Motion](items/GPWM%20Modeling%20the%20World%20as%203D%20Particle%20Motion.md) · 智能体 Agent 世界模型

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2437
- 入选条目：24
- 回填已见条目：0
- 最高分论文：La-JEPA: Compact Robot Policies with Latent World Modeling
- 最高分论文发布时间：2026-11-05T15:16:38Z
- 主要技术对象分类：具身智能评测与基准 16、多模态基础模型 16、机器人学习 13、世界模型 12、视觉语言动作模型 VLA 10、智能体 Agent 9、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
