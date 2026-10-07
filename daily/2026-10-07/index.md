---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-07
---

# 2026-10-07 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：怎样让机器人策略获得真正可执行的动作，而不把基础模型的能力当作部署保证。先读 ESP，理解如何用训练目标换掉反复采样；再读 SMART，看接触约束如何进入示范生成；最后读 WareFly-VLA，检查单帧动作预测和闭环飞行之间的距离。若更关心现有导航策略的改造，优先读 PG-VP；若想比较学习策略和程序策略，读 BiGym 2.0 的共同控制接口与分任务结果。
> **趋势**：前五篇的共同线索：这些论文把注意力放在策略与执行之间的具体接口：动作分布、接触约束、身体控制器、时间信息和额外传感器。共同证据说明，模型总体成绩之外，还必须检查它看到了什么、动作如何执行，以及评测是否覆盖实际运行中的反馈。

- **规模**：2296 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 21、多模态基础模型 15、视觉语言动作模型 VLA 13、机器人学习 10、世界模型 9、智能体 Agent 9、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses](items/WareFly-VLA%20A%20Vision-Language-Action%20Framework%20for%20UAV%20Navigation%20and%20Human%20Trac.md)

> WareFly-VLA 让无人机根据工人外观描述在仓库里找人、靠近和跟随，并用人工飞行示范比较现有 VLA。它最有用的发现是：看懂当前画面不等于知道怎样飞，单帧策略尤其难学好侧移和升降。

- **能借鉴什么**：值得借鉴的是先检查输入是否足以确定动作，再考虑加大模型。侧移可能取决于目标正在往哪走；当前帧即使认对人，也未必提供这个信息。
- **值得读吗**：值得读数据采集和评测协议，尤其用于避免把逐帧拟合成绩误当成飞行能力；时间瓶颈的解释需要继续验证。

<details><summary>实验依据</summary>

Isaac Sim 中采集 507 段、8,504 个非终止转移；四模型共用 76 段留出轨迹 [S1](https://arxiv.org/html/2610.08526v1#abstract1.1) [S26](https://arxiv.org/html/2610.08526v1#S6.F8)。指标是动作 MAE 和 Pearson 相关系数，并比较训练动作均值基线 [S24](https://arxiv.org/html/2610.08526v1#S5.SS4.p3.1) [S25](https://arxiv.org/html/2610.08526v1#S5.SS4.p4.1)。1 FPS 下 π₀ 前进相关系数为 0.65，但侧移和升降 MAE 都未胜均值基线 [S27](https://arxiv.org/html/2610.08526v1#S6.SS1.p2.1)；10 FPS 下 π₀ 侧移略胜基线，升降与朝向仍未胜 [S28](https://arxiv.org/html/2610.08526v1#S6.SS1.p3.1)。这支持动作预测仍困难，不能解释为自主飞行成功率。

</details>

### 2. [SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining](items/SMART%20Zero-Shot%20Sim-to-Real%20Articulated%20Object%20Manipulation%20via%20Large-Scale%20Synt.md)

> SMART 把开门、拉抽屉这类必须沿关节运动的操作，做成能批量生成的仿真示范。关键是先标明可操作部件和运动约束，再让任务生成智能体组合技能，避免生成看似合理却无法保持接触的动作。

- **能借鉴什么**：可借鉴的是把任务生成建立在可执行的部件语义上：语言可以组合“抓、拉、转”，但每个动作必须有对应的物理约束。这样扩大数据时，增加的是有效交互，而不只是更多描述。
- **值得读吗**：值得深入读轨迹约束与质量筛选；零样本真机迁移很值得关注，但需拿到逐任务结果和数据配方后判断可复用程度。

<details><summary>实验依据</summary>

数据超过 100 万条示范，覆盖 44 种原子任务、5 种机器人配置和 2,507 个活动物体（摘要）。仿真测试使用 LIBERO、RoboCasa365，控制架构与下游训练配方，对比合成预训练、真实数据预训练和无第一阶段预训练 [S22](https://arxiv.org/html/2610.07652v1#S5.p1.1) [S23](https://arxiv.org/html/2610.07652v1#S5.SS1.p1.1) [S24](https://arxiv.org/html/2610.07652v1#S5.SS1.p2.1)。真机测试覆盖三个双臂平台、十二项任务，并对齐仿真与真实相机参数 [S25](https://arxiv.org/html/2610.07652v1#S6.p1.1) [S29](https://arxiv.org/html/2610.07652v1#S6.SS1.p1.1) [S31](https://arxiv.org/html/2610.07652v1#S6.SS1.p2.1)。材料报告正向迁移和规模趋势，但未给成功率、试验次数及曲线，无法量化收益或判断稳定性。

</details>

### 3. [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](items/BiGym%202.0%20Benchmarking%20Learned%20and%20Agent-Developed%20Policies%20for%20Humanoid%20Househo.md)

> BiGym 2.0 测的是人形机器人边走、边保持姿态、边做家务，而不是把身体当成平稳移动底座。它让学习策略和智能体编写的程序共用身体控制器，比较两条路线在哪些任务上可靠。

- **能借鉴什么**：程序能把两只手各自的目标和纠偏明确拆开，双手到达结果提示这种结构值得借鉴 [S26]。但接触搬运仍困难，说明可分解的视觉纠偏与持续接触不是同一类能力。
- **值得读吗**：值得读控制接口、重置协议和逐任务失败分析；九任务均值可以定位方向，但不足以宣判学习或写程序哪条路线更强。

<details><summary>实验依据</summary>

套件有 20 项任务，每项 60 段 VR 示范；主比较选九项（摘要）。π₀.₅ 九任务均值最高，两个编码智能体均值超过各示范驱动 RL，双手同时到达目标时也领先学习策略 [S26](https://arxiv.org/html/2610.07594v1#S4.SS1.p1.1) [S28](https://arxiv.org/html/2610.07594v1#S5.SS2.p1.1) [S31](https://arxiv.org/html/2610.07594v1#S7.p1.1)。但材料没有主结果表的具体成功率。非 VLA 学习方法用三次训练，π₀.₅ 每任务仅一次；程序用三个开发会话，隐藏种子评测 [S20](https://arxiv.org/html/2610.07594v1#S3.SS4.p2.1) [S24](https://arxiv.org/html/2610.07594v1#S3.SS5.p4.1)。这些结果支持任务间能力分化，不能外推到全部任务或真机。

</details>

### 4. [Seeing the Invisible: Physics-Guided Visual Prompting for Temperature- and Radiation-Aware VLA Navigation](items/Seeing%20the%20Invisible%20Physics-Guided%20Visual%20Prompting%20for%20Temperature-%20and%20Radiat.md)

> PG-VP 把传感器发现的热源或辐射风险画成相机画面里的虚拟障碍，让冻结的导航 VLA 用已有避障能力绕行。巧处是新增传感器只需接到风险判断，导航模型无需重新学习每种物理量。

- **能借鉴什么**：值得借鉴的是把新增信息转换成策略已经会响应的输入形式，而不是每次扩充模型。不过前提是这类视觉提示确实触发所需行为，且危险能及时、正确地定位。
- **值得读吗**：值得深入读风险触发和动态绘制机制：这是成本明确的接口改造，但成功率损失与触发延迟决定了它能用到哪里。

<details><summary>实验依据</summary>

OmniNav 在 R2R-CE、RxR-CE 未见环境中，正确引导比例为 84.9%、83.2%，导航成功率下降 6.8、7.9 个百分点（摘要）。该测试假设危险存在，主要检验虚拟墙是否能改变路线，未测试完整传感链 [S21](https://arxiv.org/html/2610.07558v1#S4.SS1.p1.1) [S22](https://arxiv.org/html/2610.07558v1#S4.SS1.p2.1)。真机四场景使用实际热源和辐射源，均完成导航 [S24](https://arxiv.org/html/2610.07558v1#S4.SS2.p1.1) [S25](https://arxiv.org/html/2610.07558v1#S4.SS2.p2.1)；最差 10% 轨迹指标改善汇总为热 63.45%、辐射 32.59% [S35](https://arxiv.org/html/2610.07558v1#S4.SS2.p4.1)。热指标是离热源距离，辐射指标是净计数率，不能统一解释为伤害风险下降。

</details>

### 5. [ESP: Energy-Score Policy for One-Step Multimodal Action Generation](items/ESP%20Energy-Score%20Policy%20for%20One-Step%20Multimodal%20Action%20Generation.md)

> ESP 用一次网络计算，把观察、指令和随机噪声直接变成一段动作。它用 energy score 同时鼓励贴近示范与保留合理差异，让一步生成不必退化成多个动作方案的平均值。

- **能借鉴什么**：可借鉴的是把“生成得快”和“能表达多种动作”拆开：多模态不必依赖反复采样过程，也可以由训练目标约束直接生成器。在动作头延迟占主要成本时，值得尝试这种替换。
- **值得读吗**：值得读懂损失公式并检查延迟测量，是一个机制清楚的一步动作生成方案；部署收益应结合训练成本和端到端耗时判断。

<details><summary>实验依据</summary>

TwoBranch 双分支回归中，ESP 命中率 96.2%，十步流匹配 97.1%，MSE 0.7%；这是单种子机制示例 [S19](https://arxiv.org/html/2610.07696v1#S3.F3) [S28](https://arxiv.org/html/2610.07696v1#S4.SS2.p2.1)。LIBERO 固定初始状态的六任务诊断中，ESP、XM、十步 Flow 分别成功 162/192、127/192、155/192 [S32](https://arxiv.org/html/2610.07696v1#S4.SS5.p2.1) [S33](https://arxiv.org/html/2610.07696v1#S4.SS5.p3.1) [S34](https://arxiv.org/html/2610.07696v1#S4.T3) [S35](https://arxiv.org/html/2610.07696v1#S4.T3.4)。Franka 真机关抽屉为 ESP 12/15、四步 Flow 8/15；完整拾放为 7/15、1/15 [S37](https://arxiv.org/html/2610.07696v1#S4.F6.2) [S38](https://arxiv.org/html/2610.07696v1#S4.F6) [S39](https://arxiv.org/html/2610.07696v1#S4.SS6.p1.1) [S40](https://arxiv.org/html/2610.07696v1#S4.SS6.p2.1)。材料未给延迟表数值，因此能确认动作头计算次数减少，不能量化端到端加速。

</details>

## 扫读 7 篇

- [VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation](items/VOMMI%20Collecting%20and%20Leveraging%20Portable%20Demonstrations%20for%20Mobile%20Manipulation.md) — VOMMI 想让人拿着普通 RGB 相机采集的移动操作演示，直接用于机器人的 VLA 后训练。关键是先修正视觉估计的运动轨迹，再把局部运动信息送入底盘动作分支，减少漂移造成的错误监督。
- [VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models](items/VLA-ACL%20Action-Consistent%20Visual%20Token%20Pruning%20for%20Efficient%20Vision-Language-Act.md) — VLA-ACL 学一个小型选择器，让 VLA 每次只看部分视觉 token，从而减少计算。它判断哪些信息能删的依据是：删完之后，机器人预测的动作还能不能接近完整画面下的动作。
- [DepthWorld: 3D World Model for Robot Manipulation](items/DepthWorld%203D%20World%20Model%20for%20Robot%20Manipulation.md) — DepthWorld 让机器人世界模型同时预测多视角 RGB 和深度，使未来画面带有可用的三维几何。它先把 DROID 校准成 DROID-3D，再用空间潜变量拼接加入深度预测，同时保持预训练 VAE 不变。
- [Fast Non-Parametric Heteroscedastic Imitation Learning With Geometric Priors](items/Fast%20Non-Parametric%20Heteroscedastic%20Imitation%20Learning%20With%20Geometric%20Priors.md) — 这篇用几何先验做非参数模仿学习，既预测机器人该怎样动，也估计不同位置上的动作不确定性。重点是正确处理位置与旋转的几何，并让轨迹能快速更新、随物体姿态调整。
- [Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution](items/Adapting%20Vision-Language-Action%20Models%20to%20Unknown%20Visual%20Disruptions%20During%20Exec.md) — SALT 用上一轮动作块中尚未执行的部分，监督当前 VLA 在画面受干扰后的预测。两轮计划覆盖同一段未来时间，因此旧计划可以暂时提供参照，并把修正沿后续重规划传下去。
- [MIM-VLA: Learning Physical Interaction Representations from Gripper Motor Feedback](items/MIM-VLA%20Learning%20Physical%20Interaction%20Representations%20from%20Gripper%20Motor%20Feedbac.md) — MIM-VLA 让机器人通过夹爪电机的反馈判断接触情况，补上单靠图像难以知道的物体阻力与抓握状态。它把近期电流、位置、速度和信号有效性压成一个交互向量，用来调整夹爪动作，也供模型比较不同物体的交互证据。
- [ViDAL: A Visual Dynamics-Grounded Action Latent Space for Vision-Language-Action Models](items/ViDAL%20A%20Visual%20Dynamics-Grounded%20Action%20Latent%20Space%20for%20Vision-Language-Action.md) — ViDAL 让压缩后的动作表示既能还原动作，也能对应动作将引起的场景变化。关键是训练 Action VAE 时同时约束动作重建和未来视觉动态，使机器人选择动作时用到的表示包含“做完会怎样”的信息。

## 其余存档 12 篇

- [Commit While Futures Agree: Consequence-Aware Adaptive Action Chunking for Robot Manipulation](items/Commit%20While%20Futures%20Agree%20Consequence-Aware%20Adaptive%20Action%20Chunking%20for%20Robot.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [ActTune: Action-Aware Precision and GPU Operating-Point Adaptation for Energy-Efficient Vision-Language-Action Inference](items/ActTune%20Action-Aware%20Precision%20and%20GPU%20Operating-Point%20Adaptation%20for%20Energy-Eff.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation](items/EmbodiedSmith%20Scaling%20Embodied%20Data%20through%20Recursive%20Self-Improvement%20Flywheel.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [StairVLA: Stage-Aware Hierarchical Action Generation for Vision-Language-Action Models](items/StairVLA%20Stage-Aware%20Hierarchical%20Action%20Generation%20for%20Vision-Language-Action%20M.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](items/OpenSplatGraph%20From%20Dense%20Semantic%20Maps%20to%20Structured%20Scene%20Graphs%20for%20Open-Voca.md) · 具身智能评测与基准
- [Towards Efficient Robotic Manipulation Models with Self-Recursive Pruning](items/Towards%20Efficient%20Robotic%20Manipulation%20Models%20with%20Self-Recursive%20Pruning.md) · 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Silicon Language: A Robot-Native Knowledge Exchange Framework for Heterogeneous Robots](items/Silicon%20Language%20A%20Robot-Native%20Knowledge%20Exchange%20Framework%20for%20Heterogeneous%20R.md) · 智能体 Agent 具身智能评测与基准
- [Task-Space Imitation Guidance for Efficient Reinforcement Learning](items/Task-Space%20Imitation%20Guidance%20for%20Efficient%20Reinforcement%20Learning.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation](items/PEARS%20Physical-Prior-Guided%20Efficient%20Adaptation%20via%20Failure%20Reasoning%20and%20Diffu.md) · 多模态基础模型 世界模型 机器人学习 具身智能评测与基准
- [Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and Reward Gating](items/Humanoid%20Horizon%20Extending%20Task%20Horizon%20in%20Whole-Body%20Loco-Manipulation%20via%20Para.md) · 智能体 Agent 具身智能评测与基准
- [Navigation with RF Cues: Embodied Perception Action under Multipath Uncertainty](items/Navigation%20with%20RF%20Cues%20Embodied%20Perception%20Action%20under%20Multipath%20Uncertainty.md) · 多模态基础模型 具身智能评测与基准
- [QF3: Fast Flow RL with Filtered Q-Gradients](items/QF3%20Fast%20Flow%20RL%20with%20Filtered%20Q-Gradients.md) · 机器人学习

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2296
- 入选条目：24
- 回填已见条目：0
- 最高分论文：WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses
- 最高分论文发布时间：2026-10-06T15:21:14Z
- 主要技术对象分类：具身智能评测与基准 21、多模态基础模型 15、视觉语言动作模型 VLA 13、机器人学习 10、世界模型 9、智能体 Agent 9、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
