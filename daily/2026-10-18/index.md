---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-18
---

# 2026-10-18 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看三个问题：机器人怎样记住当前画面里没有的信息，怎样从有限示范获得可用经验，以及遇到外力时怎样调整动作。先读 Mem4Act，理解如何分别训练记忆的覆盖、内容和使用；再读 DSP，看同一个玩耍策略怎样同时承担采数据和缩小规划搜索范围两项工作，但要特别检查其结果与结论的冲突；若关心人机接触，读 C-GMT 的教师构造与参考动作适配，理解如何把“准确跟踪”和“适当退让”分开处理。
> **趋势**：前五篇的共同线索：这些论文中反复出现的做法，是保留已有执行能力，把新的适应能力放到记忆、候选动作或参考动作这一层。它们提供的证据各有边界：日常流程、记忆操作、接触控制和生成后训练，不能合并成一种通用能力已经得到验证。

- **规模**：2449 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 20、智能体 Agent 14、机器人学习 11、世界模型 10、多模态基础模型 6、Sim2Real 2、视觉语言动作模型 VLA 2
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [An Agentic Framework for Proactive Robots with Procedural Assistance Memory](items/An%20Agentic%20Framework%20for%20Proactive%20Robots%20with%20Procedural%20Assistance%20Memory.md)

> PAM 让机器人根据“这个人平时怎样做事”决定何时帮忙，而不只凭眼前画面猜需求。它把习惯写成活动阶段、阶段内规则和切换条件，每天复盘后改记忆，再交给 VLA 执行动作。

- **能借鉴什么**：值得借鉴的是给规则加上“在哪个阶段有效”。当同一视觉线索反复出现、却需要不同回应时，阶段化记忆比不断追加触发规则更容易消除歧义。
- **值得读吗**：值得读方法和记忆消融：它清楚展示了个人习惯如何进入决策，但尚不能据此判断长期家庭服务的可靠性。

<details><summary>实验依据</summary>

桌面早餐流程包含递麦片、递牛奶及餐后收拾。预测评测按视频帧分类，比较 LIT、事件触发 VLM、零样本 VLM和列表记忆，报告各类及宏平均 precision、recall、F1 [S15](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px1.p1.1) [S16](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px2.p1.1) [S17](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px3.p1.1) [S18](https://arxiv.org/html/2610.21211v1#S4.F5) [S19](https://arxiv.org/html/2610.21211v1#S4.SS1.SSS0.Px4.p1.1) [S20](https://arxiv.org/html/2610.21211v1#S4.I2.i1) [S21](https://arxiv.org/html/2610.21211v1#S4.I2.i2) [S22](https://arxiv.org/html/2610.21211v1#S4.I2.i3) [S23](https://arxiv.org/html/2610.21211v1#S4.I2.i4)。FSM 版本首次触发延迟从首日约5秒降至第五日约1秒，但节选没有完整分类分数 [S26](https://arxiv.org/html/2610.21211v1#S4.SS2.SSS0.Px2.p1.1)。更换流程后，一次反思使其次日表现接近从头积累记忆的版本 [S28](https://arxiv.org/html/2610.21211v1#S4.SS3.SSS0.Px1.p2.1)。Franka 真机执行中，收牛奶为5/10，对比普通与推理版 VLA 均为0/10；递牛奶仍只有3/10 [S32](https://arxiv.org/html/2610.21211v1#S4.T1.4.1) [S34](https://arxiv.org/html/2610.21211v1#A1.SS3.p1.1)。预测及时与动作可靠是两件事。

</details>

### 2. [Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation](items/Compliant%20GMT%20Making%20General%20Motion%20Tracking%20Compliant%20via%20Residual%20Reference%20Ad.md)

> C-GMT 让人形机器人继续跟踪多种动作，同时在被拉推时适当退让。关键是先修改机器人要追踪的参考动作，再让擅长保持平衡的跟踪器执行，而不是让它硬顶原目标。

- **能借鉴什么**：当已有控制器善于跟踪而不善于接触，可以先改它追逐的目标，让退让成为一个可执行的新目标。前提是修改后的参考经过可行性检查，底层也确实承受得住负载。
- **值得读吗**：值得细读教师可行性筛选与适配器训练：分工很实用，但要连同底层微调成本和接触范围一起理解。

<details><summary>实验依据</summary>

在128段留出动作的跟踪测试中，双手拉力不超过60 N时，增强跟踪器成功率为0.867，原 SONIC 为0.820；无载荷时全局位置误差反而增加4.8厘米 [S16](https://arxiv.org/html/2610.22119v1#S3.T1.2.1) [S17](https://arxiv.org/html/2610.22119v1#S3.SS1.p7.1)。这检验的是底层抗载能力。柔顺性另在仿真站立中以外力/位移衡量，与站立专用 SoftMimic 接近，但节选没有具体误差 [S23](https://arxiv.org/html/2610.22119v1#S4.F3) [S24](https://arxiv.org/html/2610.22119v1#S4.SS1.p1.1) [S25](https://arxiv.org/html/2610.22119v1#S4.SS1.p2.1)。G1 真机有接触遥操作展示；走近并抬箱的 VLA 对照每条件50次，报告受扰时更好，却未提供成功率表值，也未在该段明确评测环境 [S26](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p1.1) [S27](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p2.1) [S28](https://arxiv.org/html/2610.22119v1#S4.T3) [S29](https://arxiv.org/html/2610.22119v1#S4.F8) [S30](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p3.1)。

</details>

### 3. [Reinforcement Learning-driven Diffusion Models: Language, Vision, and Beyond](items/Reinforcement%20Learning-driven%20Diffusion%20Models%20Language%2C%20Vision%2C%20and%20Beyond.md)

> 这是一篇梳理 RL 如何用于扩散模型的综述，不是一种新的生成模型。它的核心视角是：把逐步去噪看成决策过程，用最终结果的偏好或任务得分训练生成路径。

- **能借鉴什么**：读这篇最有用的方式，是先问“结果怎样评分，分数怎样归因到生成步骤”。同样叫 RL 后训练，有的主要学偏好，有的用可检查结果优化，还有的只在推理时选样；这个区别直接决定数据、算力和实现要求。
- **值得读吗**：适合按问题查阅的路线图；若要据此选算法，应追到原论文和受控实验，现有节选不足以支持性能排序。

<details><summary>实验依据</summary>

摘要声称在多个任务基准比较代表方法，但提供的节选没有这些实验的基准名称、模型配置、预算、指标或结果数值。因此只能确认其分类和方法解释，无法据此判断哪种后训练策略更有效。列出 PPO、GRPO 或 Diffusion-DPO，并不是它们在相同设置下优劣的实验证据。

</details>

### 4. [Dexterity from Supervised Play](items/Dexterity%20from%20Supervised%20Play.md)

> DSP 先模仿人类无指定目标的玩耍，让机器人自行积累接触数据，再学习动作会造成什么变化。执行目标时，同一玩耍策略提出候选动作，世界模型预测后果，MPC 选最接近目标的一段执行。

- **能借鉴什么**：巧处是同一个行为分布既提供训练数据，也限制规划搜索，让模型主要评估熟悉的接触动作。借鉴前应检查玩耍覆盖是否包含达成目标所需的关键接触，否则搜索很难凭空找到缺失动作。
- **值得读吗**：机制值得细读，尤其是动作先验与滚动规划；性能结论应等版本冲突和硬件评测口径澄清后再引用。

<details><summary>实验依据</summary>

Push-T 中，严格重叠阈值0.95下成功率为74%，同数据 hindsight BC 为36% [S41](https://arxiv.org/html/2610.22340v1#S4.SS2.SSS1.p1.1) [S46](https://arxiv.org/html/2610.22340v1#S4.T1.4.1)。仿真手内旋转在0.6 rad误差阈值下为91.4%，hindsight BC 为53.9%；PPO 用344M计数帧达到86.7%，DSP 为701K帧，约相差490倍 [S30](https://arxiv.org/html/2610.22340v1#S3.F5) [S39](https://arxiv.org/html/2610.22340v1#S4.SS1.SSS0.Px5.p1.1) [S42](https://arxiv.org/html/2610.22340v1#S4.SS2.SSS1.p2.1)。硬件段另报该阈值90.0% [S47](https://arxiv.org/html/2610.22340v1#S4.SS2.SSS2.p2.1)。但结论 [S54](https://arxiv.org/html/2610.22340v1#S6.p1.1) 又明确称硬件结果仍属暂定、需冻结协议和不确定性分析，并称部分定量结果待插入。这一内部冲突使真机结论不能按摘要直接采信。

</details>

### 5. [Mem4Act: Learning Effective Latent Memory for Long-Horizon Robotic Manipulation](items/Mem4Act%20Learning%20Effective%20Latent%20Memory%20for%20Long-Horizon%20Robotic%20Manipulation.md)

> Mem4Act 把历史压成固定大小的潜在记忆，让机器人在关键信息被遮住后仍能行动。它不仅训练“怎样压缩”，还用历史问答和视觉特征重建训练“该记什么”，再让动作策略学习使用这些记忆。

- **能借鉴什么**：最值得借鉴的是先把记忆训练成有用的信息载体，再要求策略依赖它。若当前动作无法区分两段历史，而后续决策需要区分，额外监督历史事实和视觉证据能补上动作损失缺少的信号。
- **值得读吗**：值得深入方法与消融：它把“记住”和“用上”分开训练，证据覆盖面较清楚，但要核算完整历史处理成本。

<details><summary>实验依据</summary>

RoboMME 的16项仿真任务各50次，成功率49.88%，比最强 FrameSamp+Modul 高5.37个百分点 [S34](https://arxiv.org/html/2610.22323v1#S4.SS2.p1.1)。RMBench 九项任务各100次，单一共享策略达61.0%，NativeMEM为48.7%；需多次历史观察的任务上分别为41.3%和14.8% [S35](https://arxiv.org/html/2610.22323v1#S4.SS2.p2.1) [S36](https://arxiv.org/html/2610.22323v1#S4.T2) [S37](https://arxiv.org/html/2610.22323v1#S4.T2.4.1)。四项 YAM 双臂真机任务各50次，摘要报告平均81.5%；节选未给真机对照表数值 [S1](https://arxiv.org/html/2610.22323v1#abstract1.1) [S33](https://arxiv.org/html/2610.22323v1#S4.SS1.p5.1) [S39](https://arxiv.org/html/2610.22323v1#S4.T3)。这些结果支持所测记忆任务的收益，但总体分数不能单独证明每项设计各自的作用。

</details>

## 扫读 7 篇

- [CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](items/CoWorld%20Reasoner%20Agentic%20Multimodal%20Reasoning%20with%20the%20Evolving%20Video%20World%20Mode.md) — CoWorld Reasoner 让视觉语言模型遇到看不清、看不全的问题时，自己决定是否调用视频世界模型补充视觉内容，并选择怎样生成、怎样使用。它还根据执行反馈修改工具、技能说明和代码，两个模型本身都不更新权重。
- [SPEAR: Selective Preference Elicitation with Adaptive Rewards for VLM-Guided Robotic Manipulation](items/SPEAR%20Selective%20Preference%20Elicitation%20with%20Adaptive%20Rewards%20for%20VLM-Guided%20Robo.md) — SPEAR 用视觉语言模型比较机器人行为的好坏，但先挑选既有学习价值、又容易看出差别的比较，减少昂贵的无效提问。训练起步时先用 VLM 合成的指导帮助探索，再转向偏好反馈细化奖励。
- [From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion](items/From%20Optical%20Flow%20to%20Safety%20Visual%20Safety%20Certification%20via%20Scale-Free%20Relative.md) — 这篇方法从单目图像的光流中估计相对运动，直接判断碰撞风险，不先重建障碍物的真实距离和速度。RV-C³BF 把估计误差纳入安全约束，再尽量少改动原控制指令来避碰。
- [CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation](items/CQDC-Warp%20GPU-Accelerated%20Differentiable%20Quasi-Dynamic%20Simulation%20for%20Contact-Ri.md) — CQDC-Warp 把可求梯度的准动态接触仿真放到 GPU 上并行运行，用于更快地规划复杂操作。规划前指定希望发生的接触并以软代价鼓励它，但实际接触几何和摩擦响应仍由仿真决定。
- [System1-Arena: Which Decisions Can Be Left to System 1?](items/System1-Arena%20Which%20Decisions%20Can%20Be%20Left%20to%20System%201.md) — System1-Arena 把决策统一成“给选项报概率”，比较一次前向计算的快速模型与生成推理过程的模型。它还让模型进入持续变化的环境，检验快速答题的优势是否能转化为连续行动成功。
- [SOMA: Stack-of-Objects Manipulation using a Quadruped Robot](items/SOMA%20Stack-of-Objects%20Manipulation%20using%20a%20Quadruped%20Robot.md) — SOMA 让没有机械臂的四足机器人用身体推动堆叠物体，并在移动时尽量避免上层滑落或倾倒。关键是把机身高度也交给策略控制，让机器人能够改变接触位置和用力姿态。
- [Uni-PNP: Unified Prehensile and Non-prehensile Policy Learning for Generalizable Object Pose Reaching](items/Uni-PNP%20Unified%20Prehensile%20and%20Non-prehensile%20Policy%20Learning%20for%20Generalizable.md) — Uni-PNP 用同一个策略学习推、翻、抓，把物体送到目标位置和朝向。它先学习不同几何接触会怎样带动物体，再通过从容易抓到难以抓取对象的训练安排，促使策略发现抓取以外的动作。

## 其余存档 12 篇

- [Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models](items/Do%20VLAs%20Really%20Follow%20Instructions%20Diagnosing%20How-Level%20Instruction%20Following%20in.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [CLIS-MPPI: Closed-Loop Model Predictive Path Integral Control With Initial-State Sampling Under Execution Delay](items/CLIS-MPPI%20Closed-Loop%20Model%20Predictive%20Path%20Integral%20Control%20With%20Initial-State.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation](items/Evo-DexBench%20Benchmarking%20Generalization%20across%20Related%20Tasks%20for%20Dexterous%20Mani.md) · 多模态基础模型 机器人学习 具身智能评测与基准
- [Learning Self-Orchestration in Decentralized Agent Swarms](items/Learning%20Self-Orchestration%20in%20Decentralized%20Agent%20Swarms.md) · 智能体 Agent 具身智能评测与基准
- [Robust Multi-Agent Pursuit with Preemptive Communication via Reachability-Based Control Barrier Functions](items/Robust%20Multi-Agent%20Pursuit%20with%20Preemptive%20Communication%20via%20Reachability-Based.md) · 智能体 Agent 具身智能评测与基准
- [MuSTMM: Learning Sound-Triggered Mobile Manipulation across Multiple Scenes](items/MuSTMM%20Learning%20Sound-Triggered%20Mobile%20Manipulation%20across%20Multiple%20Scenes.md) · 具身智能评测与基准
- [Constrained Multi-Agent Reinforcement Learning in Imagination](items/Constrained%20Multi-Agent%20Reinforcement%20Learning%20in%20Imagination.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [SpaceCache: Intermediate Feature Reuse for Efficient Semantic Segmentation on Point Cloud Streams](items/SpaceCache%20Intermediate%20Feature%20Reuse%20for%20Efficient%20Semantic%20Segmentation%20on%20Poi.md) · 具身智能评测与基准
- [MoCaP: Mobile Code-as-Policies for Zero-Shot Mobile Manipulation from Passive Human Videos](items/MoCaP%20Mobile%20Code-as-Policies%20for%20Zero-Shot%20Mobile%20Manipulation%20from%20Passive%20Hum.md) · 智能体 Agent 机器人学习
- [T2-z: Test-Time Optimization of Environment Latents for Robotic World Models](items/T2-z%20Test-Time%20Optimization%20of%20Environment%20Latents%20for%20Robotic%20World%20Models.md) · 世界模型
- [Progress Reward Model for Reinforcement Learning via Large Language Models](items/Progress%20Reward%20Model%20for%20Reinforcement%20Learning%20via%20Large%20Language%20Models.md) · 智能体 Agent 机器人学习
- [VP-EVT: Active Visibility Preservation for Embodied Visual Tracking](items/VP-EVT%20Active%20Visibility%20Preservation%20for%20Embodied%20Visual%20Tracking.md) · 智能体 Agent 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2449
- 入选条目：24
- 回填已见条目：0
- 最高分论文：An Agentic Framework for Proactive Robots with Procedural Assistance Memory
- 最高分论文发布时间：2026-10-15T04:04:49Z
- 主要技术对象分类：具身智能评测与基准 20、智能体 Agent 14、机器人学习 11、世界模型 10、多模态基础模型 6、Sim2Real 2、视觉语言动作模型 VLA 2
- 信息源错误：0
- 自动恢复信息源：0

</details>
