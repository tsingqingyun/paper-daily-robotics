---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-26
---

# 2026-11-26 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先解决一个问题：怎样判断视觉信息真的帮机器人做对了动作？想把普通视频用进训练，先读 CamAct 的动作掩码和腕部相机消融。想定位空间操作失败，读 RoboARC 怎样分别补回位姿和形状。想在执行前拦截危险动作，读 WAtcher 在同一策略上开关 Safe-Guard 的对照。
> **趋势**：前五篇的共同线索：DataForgeVLA 从生成视频恢复关节目标，CamAct 从走路视频恢复相机运动，WAtcher 用预测画面帮助判断候选动作的风险。RoboARC 和 RoboDojo-Mirror 则用受控评测追问视觉信息究竟在哪里失效：是缺少规划所需的几何，还是看到了形似目标、却无法接触的倒影。

- **规模**：2617 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 19、多模态基础模型 17、机器人学习 14、视觉语言动作模型 VLA 13、世界模型 10、智能体 Agent 7、AI 核心知识地图 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training](items/DataForgeVLA%20Fully%20Synthetic%20Manipulation%20Demonstrations%20for%20Vision-Language-Act.md)

> DataForgeVLA 用已有遥操作数据打底：先摆出新的机器人与物体起始姿态，再生成操作视频，从画面反推关节动作，给机器人策略提供新的训练示范。

- **能借鉴什么**：如果已有少量标定好的示范，而缺的是新起始摆位，可以先控制首帧几何，再让视频模型生成后续运动。这样能主动指定要补采的场景，同时把实测问题落到关节标签是否足以训练策略。
- **值得读吗**：值得读到动作导出和真机协议，尤其要看从视频恢复的姿态怎样变成控制目标。

<details><summary>实验依据</summary>

数据有 340 段，覆盖八类物体，300 段通过筛选。[S27](https://arxiv.org/html/2611.34287v1#S3.SS2.p3.1) 两个预训练 GR00T N1.6 策略各微调 20,000 步，在同一真机奥利奥抓放协议下，合成组成功 16/20，105 段真实遥操作组成功 18/20。成功要求在 30 秒内抓起包装并放进目标盘，途中无重试或人工干预。这说明恢复出的标签能支持这一任务的真机执行。[S35](https://arxiv.org/html/2611.34287v1#S5.p1.1)

</details>

### 2. [CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion](items/CamAct%20Learning%20Robotic%20Manipulation%20from%20In-the-Wild%20Videos%20via%20Camera%20Motion.md)

> CamAct 让机器人策略从普通走路视频里学视角怎样随运动变化。它把离线恢复的相机位移和转向放进独立的动作维度，与真实机器人动作共用网络训练。

- **能借鉴什么**：设计辅助任务时，可以先找两类数据共有的可预测变化。走路和抓放都可能让相机相对场景移动，于是能让整个网络学习这种变化，同时把具体的夹爪控制交给有机器人标签的样本。
- **值得读吗**：值得读到损失掩码和相机视角消融，直接看动作空间不同的数据怎样共训，以及什么配置下会出现负收益。

<details><summary>实验依据</summary>

与同更新步数的纯机器人 StarVLA-GR00T 对比，仿真每任务跑 50 次，LIBERO 总成功率从 96.40% 到 98.10%，RoboCasa 365 从 22.96% 到 29.32%。LIBERO-Plus 零样本从 71.90% 到 74.49%。真机 Franka 的四项任务各用 50 条示范单独微调，再各跑 16 次，平均成功率从 54.69% 到 68.75%。真机结果支持整套联合训练流程在这些任务上的收益。[S23](https://arxiv.org/html/2611.34257v1#S3.T1.5)[S28](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px1.p1.1) [S29](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px2.p1.1) [S30](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p1.1) [S31](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p2.1) [S32](https://arxiv.org/html/2611.34257v1#S4.SS1.SSS0.Px3.p3.1) [S33](https://arxiv.org/html/2611.34257v1#S4.T2) [S34](https://arxiv.org/html/2611.34257v1#S4.T2.5) [S35](https://arxiv.org/html/2611.34257v1#S4.SS2.SSS0.Px1.p1.1)[S38](https://arxiv.org/html/2611.34257v1#S4.SS2.SSS0.Px2.p1.1)[S47](https://arxiv.org/html/2611.34257v1#A1.SS3.p1.1)

</details>

### 3. [RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints](items/RoboARC%20Physical%20Puzzles%20for%20Robotic%20Manipulation%20under%20Spatial%20Constraints.md)

> RoboARC 用必须沿特定路线运动的仿真谜题，测试机器人能否按眼前的几何解题。它在同一场景里切换可读完整状态、可重置的模式和仅凭传感器、单次执行的模式，再用补充信息实验定位卡点。

- **能借鉴什么**：调试精细操作时，可以固定同一道题和同一种判分，先补物体当前位置，再补形状，最后都补。若单独提供一项几乎无效，继续加同一类传感器之前，值得先查规划器是否同时缺另一项信息。
- **值得读吗**：优先读双模式协议和信息消融，分数最值得用来找精细操作卡在哪里。

<details><summary>实验依据</summary>

MuJoCo 中有三种机器人配置、六类约束和 90 题。七个编程智能体中，GPT-6 Astra 的特权和标准成功率分别为 86% 和 43%。四个零样本 VLA 在其 18 道单臂题上均未解出。对筛出的 15 道题，补物体位姿或零件形状分别增加 4 和 13 个百分点，两者同给使标准模式从 24% 到 60%。这组干预支持两种信息在所选题上能互补。[S2](https://arxiv.org/html/2611.33390v1#abstract1.1)[S19](https://arxiv.org/html/2611.33390v1#S3.SS2.SSS0.Px2.p1.1) [S20](https://arxiv.org/html/2611.33390v1#S4.SS1.SSS0.Px1.p1.1)[S23](https://arxiv.org/html/2611.33390v1#S6.p1.1)[S30](https://arxiv.org/html/2611.33390v1#A5.SS4.SSS0.Px4.p1.1)[S37](https://arxiv.org/html/2611.33390v1#A6.T16.5.1)

</details>

### 4. [Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](items/Embodied%20AI%20Fails%20the%20Mirror%20Test%20How%20a%20Simple%20Mirror%20Breaks%20Robot%20Policies.md)

> RoboDojo-Mirror 保持任务和策略固定，只改变镜面条件，再用同形状的不反光板检查实体障碍能解释多少失败。评测还观察机器人伸向哪里、碰到了什么，以定位倒影怎样干扰操作。

- **能借鉴什么**：测试策略能否处理视觉歧义时，可以找一种在物理上等价的场景改动做对照，再同时看成功率、末端轨迹和接触。比如同样抓空，手伸向倒影附近和手被障碍挡住，指向不同的修正方向。
- **值得读吗**：值得读到竖镜对照和轨迹诊断，单看成功率容易错过论文怎样区分障碍和视觉干扰。

<details><summary>实验依据</summary>

仿真八项任务、五个策略中，每种镜面条件都使各策略的汇总成功率下降，跨三种条件平均，降幅为 10.8–56.7 个百分点。竖镜对照中，50–88% 的镜面特有失败未记录到机器人碰板。真机 Franka 四项任务每个条件各测 10 次，π₀.₅ 在无镜、竖镜和镜桌下总体为 77.5%、52.5%、27.5%，FastWAM 为 60.0%、30.0%、10.0%。真机结果支持相同的下降方向。[S6](https://arxiv.org/html/2611.33010v1#S1.p6.1)[S24](https://arxiv.org/html/2611.33010v1#S4.SS1.p2.1)[S29](https://arxiv.org/html/2611.33010v1#S4.SS4.p2.1) [S30](https://arxiv.org/html/2611.33010v1#S4.F6) [S31](https://arxiv.org/html/2611.33010v1#S4.SS4.p3.1) [S32](https://arxiv.org/html/2611.33010v1#S4.T6) [S33](https://arxiv.org/html/2611.33010v1#S4.T6.5)[S45](https://arxiv.org/html/2611.33010v1#A3.SS2.p2.1) [S46](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px1.p1.1) [S47](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.1) [S48](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.2)

</details>

### 5. [WAtcher: Watching Ahead for Safe Robotic Manipulation with Efficient World-Action Models](items/WAtcher%20Watching%20Ahead%20for%20Safe%20Robotic%20Manipulation%20with%20Efficient%20World-Action.md)

> WAtcher 在每段候选动作执行前，先让世界动作模型预演这段动作的视觉后果。独立训练的 Safe-Guard 综合预览、当前画面、机器人状态和动作打分，风险过高就换成有限回退。

- **能借鉴什么**：如果现有策略能针对指定动作预测后果，就可以保留动作策略，用执行记录单独训练一道检查。这样能专门检验安全模块是否减少了危险，并量出它拦住正常动作的代价。
- **值得读吗**：值得读到候选动作条件下的第二次视频预测，以及同一策略开关检测器的对照。

<details><summary>实验依据</summary>

用 25,434 个标注窗口训练后，Safe-Guard 在 1,352 个盲测窗口上达 92.1% 平衡准确率，微调 8B 视觉语言模型为 89.4%。在训练任务的新场景闭环测试中，危险试验从 27.0% 降至 10.8%，任务成功率未下降。UR7e 的 60 场布置危险试验中，经真机数据适配的 Safe-Guard 将危险次数从 43 降到 6。另五项真机任务的成功率为启用时 74.0%、同一宿主关闭时 75.5%、π₀.₅ 为 59.5%。[S6](https://arxiv.org/html/2611.34124v1#S1.p4.1)[S25](https://arxiv.org/html/2611.34124v1#S4.p7.1)[S30](https://arxiv.org/html/2611.34124v1#S5.SS2.p1.1)[S37](https://arxiv.org/html/2611.34124v1#S5.SS6.p1.1)

</details>

## 扫读 7 篇

- [Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation](items/Aegis-VLA%20Reliability-Gated%20Action%20Refinement%20via%20a%20Trajectory%20World%20Model%20for%20D.md) — Aegis-VLA 让机械臂在目标持续移动时，有选择地修正基础 VLA 给出的动作。它用轨迹世界模型提出有限幅度的修正，再用可靠性门控决定采不采纳、采纳多少。
- [Hybrid AI for AI-Native RAN Control: A Functional Perspective](items/Hybrid%20AI%20for%20AI-Native%20RAN%20Control%20A%20Functional%20Perspective.md) — 这篇 Hybrid AI 综述按无线接入网控制中实际要完成的工作，把方法拆成表征与推理、预测与仿真、自适应控制、决策合成四类能力。这样可以对照不同系统各自负责哪段决策、怎样组合，以及缺少什么才能公平比较。
- [VidForce: Predicting Force-Aware Articulation by Observing Humans](items/VidForce%20Predicting%20Force-Aware%20Articulation%20by%20Observing%20Humans.md) — VidForce 从第三人称 RGB 视频一起估计物体交互的运动轨迹和用力曲线。它用少量实测力学出可重用的用力原型，再根据画面里的几何和语义线索调整原型，并联合细化轨迹与力。
- [WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics](items/WorldPhy%20Benchmarking%20Fine-Grained%20Physical%20Plausibility%20of%20World%20Models%20in%20Robo.md) — WorldPhy 检查机器人世界模型生成的视频能否在细节上符合物理约束。它用人工评分训练 WorldPhyReward，让评测器按六个物理维度和一个指令遵循维度分别给分并说明理由。
- [Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data](items/Integration%20of%20Vision-Language-Action%20Control%20for%20Autonomous%20Forklift%20Unloading.md) — 这项工作把主要从机械臂数据上预训练的视觉语言动作模型（VLA）适配到叉车卸货。作者用较多仿真示范配合少量真机示范训练，并在实体叉车上验证了卸货任务可以完成。
- [Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid](items/Learning%20a%20Whole-Body%20Pivot-Walking%20Gait%20for%20Heavy-Box%20Transport%20with%20a%20Humanoid.md) — 这篇 Pivot-Walking 工作让人形机器人用交替转动的方式向前挪重箱。它用一个强化学习策略同时管脚步、平衡和推箱，训练时按箱子的实际进度推进动作阶段，上真机时改用周期时钟。
- [Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models](items/Best-of-%24N%24%20Test-Time%20Steering%20Can%20Lead%20to%20Reward%20Hacking%20in%20Vision-Language-Act.md) — Best-of-N 让机器人从同一个策略多抽几套候选动作，再挑评分最高的一套。论文发现，打分器有误时，候选越多，越可能挑中一套被误打高分的动作。

## 其余存档 12 篇

- [Ground Your Steps: Optimizing Sampling Schedules in Flow Matching Robot Policies](items/Ground%20Your%20Steps%20Optimizing%20Sampling%20Schedules%20in%20Flow%20Matching%20Robot%20Policies.md) · 机器人学习 具身智能评测与基准
- [FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips](items/FlipVLA%20Backdoor%20Attacks%20on%20Vision-Language-Action%28VLA%29%20Models%20Only%20Through%20Bit.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action](items/Physicl%20Scenes%20An%20Artist-created%203D%20Dataset%20for%20Learning%20Perception%20and%20Action.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation](items/SEEK%20Self-Evolution%20through%20Execution%20Knowledge%20for%20Agentic%20Robot%20Manipulation.md) · 多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- [RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills](items/RegHarness%20Regulating%20What%20Code-as-Policy%20Agents%20Keep%20from%20Steps%20to%20Skills.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models](items/FreshVLA%20Frequency-Regularized%20Time%20Scale%20Hierarchical%20Latent%20Actions%20for%20Vision.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data](items/DexEngine%20Scaling%20Human%20Demonstrations%20into%20Physically%20Executable%20Whole-Robot%20Da.md) · 世界模型 机器人学习 具身智能评测与基准
- [Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers](items/Loop4D%20Embodied%20World%20Modeling%20with%204D%20VAEs%20and%20Looped%20Diffusion%20Transformers.md) · 世界模型
- [$\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?](items/%24%20widetilde%7B%20varepsilon%7D%24%20Does%20Initial%20Noise%20Induce%20Directional%20Bias%20in%20Vision-L.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction](items/Embodied-VGGT%20Preserving%20Reliable%20Local%20Geometry%20for%20Long-Sequence%20Reconstructio.md) · 具身智能评测与基准
- [Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures](items/Beyond%20the%20Happy%20Path%20Generalizing%20Robot%20World%20Models%20from%20Simulated%20Failures.md) · 世界模型 机器人学习
- [X-World: Transferring Video Priors to Cross-Embodiment Robot Control](items/X-World%20Transferring%20Video%20Priors%20to%20Cross-Embodiment%20Robot%20Control.md) · AI 核心知识地图

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2617
- 入选条目：24
- 回填已见条目：0
- 最高分论文：DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training
- 最高分论文发布时间：2026-11-25T12:41:23Z
- 主要技术对象分类：具身智能评测与基准 19、多模态基础模型 17、机器人学习 14、视觉语言动作模型 VLA 13、世界模型 10、智能体 Agent 7、AI 核心知识地图 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
