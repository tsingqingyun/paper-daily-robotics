---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-13
---

# 2026-10-13 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先解决的问题是：机器人成功率的变化，究竟来自更好的动作学习、对场景关系的理解，还是训练时保住了有用的表示？优先读 Spa-Bench，看如何用同场景直接指令拆开“选错目标”和“动作做不好”；接着读 RARA，理解少量示范适配时该保留哪些旧经验；若关注如何扩大训练数据，再读 LAPT-Scale，重点看固定机器人数据后的扩量实验与计算量对照。
> **趋势**：前五篇的共同线索：这些论文都在细化动作成功背后的学习信号：RARA选择相关旧经验，LAPT-Scale和Evo-World强调视觉变化中的运动，Spa-Bench则用受控实验检查空间语言是否真正指导动作。JoyInside进一步把执行反馈和当前目标纳入训练，但其工具调用指标与真机案例需要分别理解。

- **规模**：2433 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、多模态基础模型 14、视觉语言动作模型 VLA 14、世界模型 13、机器人学习 11、智能体 Agent 6、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation](items/RARA%20Robust%20Policy%20Fine-Tuning%20through%20Retrieval-Anchored%20Representation%20Alignme.md)

> RARA让机器人用少量示范学新任务时，先借用预训练中相似技能的内部表示，再一边学新动作、一边保住这些旧经验。关键是只保护与目标任务相关的示范，而不是把整个模型拉回原样。

- **能借鉴什么**：值得借鉴的是把“保住预训练知识”改成“保住当前任务需要的经验”。当旧数据中确有同类技能时，可以先解决视觉表示的对应关系，再学习动作，而不必把旧动作全部混入模仿目标。
- **值得读吗**：值得读到损失和消融：它给出了明确的选择性约束办法，但收益能否复现取决于旧数据是否提供合适参照。

<details><summary>实验依据</summary>

测试覆盖Diffusion Policy的四个RoboTwin任务，以及GR00T的五个RoboCasa任务和四个Franka真机任务；OOD改变布局、背景、干扰物、视角或物体[S6](https://arxiv.org/html/2610.13578v1#S1.p4.1) [S32](https://arxiv.org/html/2610.13578v1#S5.I2.i1) [S33](https://arxiv.org/html/2610.13578v1#S5.I2.i2) [S34](https://arxiv.org/html/2610.13578v1#S5.I2.i3) [S35](https://arxiv.org/html/2610.13578v1#S5.I3.i1)。相对普通微调，平均成功率ID增加9.5个百分点、OOD增加13.6个百分点，并超过所比较基线[S6](https://arxiv.org/html/2610.13578v1#S1.p4.1)。这支持同机器人、同动作空间下的适配；节选未给各基线成绩、重复试验与不确定性，不能判断每个任务收益是否均匀。

</details>

### 2. [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](items/Spa-Bench%20A%20Real-Robot%20Benchmark%20for%20Spatial%20Grounding%20in%20Vision-Language-Action.md)

> Spa-Bench检查机器人是否真能按空间描述选目标和执行动作。它让物体、概念和动作分别在训练中出现，只留出新的组合，再用同场景直接点名目标的指令检查失败是否主要发生在空间理解上。

- **能借鉴什么**：最可借鉴的是失败诊断：同一场景、同一目标、同一运动，只改变是否需要解析空间描述。直接点名后能完成，比单看OOD下降更能说明问题出在目标解析或关系使用环节。
- **值得读吗**：值得优先读评测协议和任务级结果，因为它教你如何判断机器人究竟在哪一步失败，而不只是给模型排榜。

<details><summary>实验依据</summary>

SO-101真机数据含1200条示范和2892次评测；五个策略中，MolmoAct2、π₀.₅与GR00T-N1.7 F-LLM完成全套，每个900次[S9](https://arxiv.org/html/2610.12696v1#S1.p9.1) [S31](https://arxiv.org/html/2610.12696v1#S4.SS2.p1.1)。三者ID成功率67.5–73.3%，OOD为40.7–52.0%；匹配场景直接指令成功率81.7–89.2%[S10](https://arxiv.org/html/2610.12696v1#S1.p10.1)，对应优势为28.3–40.0个百分点（摘要）。评分是二元物理成功，并报告Wilson置信区间[S28](https://arxiv.org/html/2610.12696v1#S3.SS5.p2.1)。这支持被测系统存在空间落地瓶颈，不能推广为所有VLA都不懂空间。

</details>

### 3. [JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents](items/JoyInside-VLM-Agent%20Product-Conditioned%20Multimodal%20Policy%20Learning%20for%20Embodied.md)

> JoyInside-VLM-Agent训练一个能按产品能力办事、遇到目标变化或执行失败就修改决定的多模态智能体。其DPER用两种训练期额外信息判断每个生成token该受到多强的奖励更新，但不改变奖励原本鼓励或抑制它的方向。

- **能借鉴什么**：具体启示是把“知道产品不能做什么”和“失败后如何继续”放进训练轨迹，而不仅写在部署提示中。DPER还提供一个信用分配思路：额外证据调整更新强度，任务奖励继续决定更新方向。
- **值得读吗**：值得读数据闭环与DPER细节，但应把它视为交互策略训练方案；真机可靠性的证据目前主要是案例。

<details><summary>实验依据</summary>

相对基础Qwen3.5-35B-A3B和更大Qwen3.5-397B-A17B，BFCL v4为77.44，对照67.30与72.90；ToolBench为23.50，对照18.30与21.00。但MSAgent和ToolACE低于大模型[S39](https://arxiv.org/html/2610.12957v1#S5.T1.5)。BFCL按官方评分，其他三个公共集按完整工具调用序列精确匹配[S35](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px6.p1.1)。私有集领先评估基线，但包含固定参数下的技能指令优化[S32](https://arxiv.org/html/2610.12957v1#S5.SS1.SSS0.Px3.p1.1)。两次四足真机案例是定性展示，不能当长期完成率证据[S29](https://arxiv.org/html/2610.12957v1#S5.p1.1)。

</details>

### 4. [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos](items/LAPT-Scale%20Scaling%20Embodied%20Policies%20with%20Latent%20Action%20Pre-Training%20on%20Human%20Vi.md)

> LAPT-Scale先从人类视频的前后画面学出连续的“隐含动作”，用它预训练机器人策略，再用真实机器人数据把输出转成可执行动作。关键是让隐含动作同时解释视觉结构和运动，减少静态背景对训练的干扰。

- **能借鉴什么**：可借鉴的是把“视频里发生了什么变化”和“机器人该怎样驱动关节”分阶段学习。视频能先提供交互规律，机器人数据再建立控制对应；固定机器人数据的扩量实验比单纯跨模型排名更能检验视频是否有用。
- **值得读吗**：值得深入读到同架构对照和数据筛选，因为它较清楚地回答了“多看人类视频是否真能帮助机器人”，同时保留了必要的机器人对齐环节。

<details><summary>实验依据</summary>

LAM训练用23.3K小时视频，策略主实验用5.1K小时清洗子集，随后用250小时目标机器人数据对齐[S25](https://arxiv.org/html/2610.13732v1#S4.SS1.p1.1) [S26](https://arxiv.org/html/2610.13732v1#S4.SS1.p2.1)。固定机器人数据、架构与评测，视频从1K增至5K小时，真机成功率63.3%升至85.0%[S7](https://arxiv.org/html/2610.13732v1#S1.p5.1) [S37](https://arxiv.org/html/2610.13732v1#S4.SS3.p1.1)。同架构去掉视频预训练为55.0%，增加机器人训练以匹配计算量为53.3%，完整方案85.0%[S42](https://arxiv.org/html/2610.13732v1#S4.T4.2) [S50](https://arxiv.org/html/2610.13732v1#A5.SS1.p1.1)。三项原始真机任务各20次，JoyAI-RA平均80.0%，本文85.0%[S34](https://arxiv.org/html/2610.13732v1#S4.T3) [S35](https://arxiv.org/html/2610.13732v1#S4.T3.2)。这些对照支持视频监督的作用，但小样本不足以精确估计部署可靠性。

</details>

### 5. [Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision](items/Evo-World%20A%20Lightweight%20Vision-Language-Action%20Model%20with%20Future%20Motion%20Predicti.md)

> Evo-World让小型VLA额外预测“接下来哪里会怎样移动”，再用这个预测指导动作。它以光流表示提供训练监督，并阻断动作损失对运动分支的梯度，避免预测能力在学动作时被改坏。

- **能借鉴什么**：可借鉴的是先问辅助预测该突出什么，而不是默认预测完整未来图像。若控制主要依赖场景位移，运动监督可以给小策略提供信息；同时分开梯度，让动作网络学习使用预测，而不随意重写预测表示。
- **值得读吗**：值得读到预测目标对照与梯度设计：它清楚展示了运动监督如何接入小策略，但不能把它当成已验证的通用规划世界模型。

<details><summary>实验依据</summary>

Meta-World MT50难度层等权平均成功率91.1%，Evo-1为80.6%，FabriVLA为90.0%[S33](https://arxiv.org/html/2610.12936v1#S4.SS2.p1.1) [S34](https://arxiv.org/html/2610.12936v1#S4.T1) [S35](https://arxiv.org/html/2610.12936v1#S4.T1.8.1)；摘要的13.0%是相对提升，不能读成百分点。受控预测目标实验中，未来RGB编码比无预测高3.7个百分点，光流编码再高6.8个百分点[S42](https://arxiv.org/html/2610.12936v1#S5.SS1.p1.1) [S43](https://arxiv.org/html/2610.12936v1#S5.SS1.p2.1)。AgileX三任务各20次，平均成功率63.3%，π₀为51.7%，OpenVLA-OFT为23.3%；同H20、BF16部署下，本文显存2.54GB、推理6.16Hz[S38](https://arxiv.org/html/2610.12936v1#S4.SS3.p2.1) [S39](https://arxiv.org/html/2610.12936v1#S4.T2) [S40](https://arxiv.org/html/2610.12936v1#S4.T2.4)。结果支持所测配置的预测与效率优势。

</details>

## 扫读 7 篇

- [JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation](items/JitterVLA%20A%20Replay%20Benchmark%20for%20Motion%20Quality%20in%20VLA-Driven%20Human-Robot%20Manipu.md) — 机器人动作目标即使合理，发送得稀疏、延迟且忽快忽慢，也可能让机械臂突然抽动。JitterVLA 把同一批命令按同一到达时间重放给不同控制器，检查怎样接续目标才能减小抖动，以及要牺牲多少跟踪精度。
- [Forward Dynamics Models](items/Forward%20Dynamics%20Models.md) — FDM 让动作特征同时承担“选动作”和“预测动作之后世界怎样变化”两项任务，用真实未来纠正动作学习。执行时只生成动作，省去未来画面生成，也避免预测画面出错后再误导动作。
- [StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras](items/StereoEngine%20Scaling%20Stereo%20Bimanual%20Robot%20Data%20without%20Stereo%20Cameras.md) — StereoEngine 把单目操作视频变成左右眼视频，也能从仿真生成成对的逼真视图，为双臂策略补充立体训练数据。关键是分别处理换视角后露出的空缺，以及左右画面的一致性。
- [Noise Space Learning for VLA Adaptation](items/Noise%20Space%20Learning%20for%20VLA%20Adaptation.md) — NSL 冻结预训练 VLA，改学在当前情境下应该给它什么初始噪声，从而改变它最终生成的动作。它把任务适配入口放到噪声分布上，并用 PPO、SAC 和 AWR 分别实现学习。
- [Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](items/Beyond%20Successful%20Robot%20Demonstrations%20Learning%20from%20Human%20Interactions%20and%20Mode.md) — HF-WM 想让世界模型既利用人类操作视频，又能预测做错动作后的发展。它用稳定化的点运动连接人手与机器人经验，再对扰动动作生成的结果做奖励引导训练，补学失败过程。
- [OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models](items/OGPO%20Offline%20Goal-conditioned%20Policy%20Optimization%20for%20Recoverable%20Vision-Languag.md) — OGPO 想让机器人偏离示范路线后还能接着完成任务：它把离线示范改成“需要到达哪些关键状态”的训练材料，用到达这些状态的奖励优化 VLA，而不只是要求逐步复现专家动作。
- [Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models](items/Beyond%20Actions%20Learning%20Future%20Operation%20Targets%20for%20Vision-Language-Action%20Mode.md) — AFCE 让 VLA 先预测动作将带来的物理结果，再把这种预测解码成可执行动作。这个中间表示同时从示范动作、机器人的实际响应和视觉变化中学习，试图让策略知道一段动作究竟要完成什么。

## 其余存档 12 篇

- [Dream to Remember: Continual Steering of Generalist Robot Policies with World Models](items/Dream%20to%20Remember%20Continual%20Steering%20of%20Generalist%20Robot%20Policies%20with%20World%20Mod.md) · 世界模型 机器人学习
- [AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](items/AutoBio%2B%20Benchmarking%20Dexterous%20Manipulation%20with%20Dynamic%20Experimental%20Phenomena.md) · 智能体 Agent 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies](items/Evidence-Guided%20Counterfactual%20Learning%20for%20Long-Tailed%20Robotic%20Policies.md) · 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding](items/VLMs%20are%20Native%20Action%20Models%20Unleashing%20the%20Manipulation%20Capabilities%20of%20VLMs%20w.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation](items/Gamma%20Grounded%20Multi-Agent%20Memory%20with%20Mechanical%20Audit%20for%20Memory-Intensive%20Man.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Evo-RL: Iterative Robot Reinforcement Learning from Selective Experience](items/Evo-RL%20Iterative%20Robot%20Reinforcement%20Learning%20from%20Selective%20Experience.md) · 机器人学习 具身智能评测与基准
- [Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing](items/Mind%20the%20Spatial%20Gap%20A%20Benchmark%20for%20Geospatial%20Reasoning%20and%20Constrained%20Spatia.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [Visual-Wi-Fi Navigation to Signal-Emitting Devices](items/Visual-Wi-Fi%20Navigation%20to%20Signal-Emitting%20Devices.md) · 具身智能评测与基准
- [Sampling-based Kinodynamic Planning with World Models](items/Sampling-based%20Kinodynamic%20Planning%20with%20World%20Models.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding](items/Grounded-Dreamer%20Robot%20Learning%20from%20World%20Model%20Synthetic%20Data%20with%20Physical%20Gr.md) · 世界模型 机器人学习
- [ReAT: Residual Action Tokenization for Autoregressive Robot Policies](items/ReAT%20Residual%20Action%20Tokenization%20for%20Autoregressive%20Robot%20Policies.md) · 世界模型 具身智能评测与基准
- [REMM: Revisable Embodied Memory for Manipulation](items/REMM%20Revisable%20Embodied%20Memory%20for%20Manipulation.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2433
- 入选条目：24
- 回填已见条目：0
- 最高分论文：RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation
- 最高分论文发布时间：2026-10-09T13:31:20Z
- 主要技术对象分类：具身智能评测与基准 17、多模态基础模型 14、视觉语言动作模型 VLA 14、世界模型 13、机器人学习 11、智能体 Agent 6、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
