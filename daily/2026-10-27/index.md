---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-27
---

# 2026-10-27 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人做不好，究竟是示范覆盖不足、忘了关键事件，还是没有把指令落实到具体动作？先读 DiscoDemo，理解为什么“多种成功做法”可能比重复同一种示范更有用；再读 WholeBodyMem，看如何保存已经消失但仍决定动作的线索；若关心多技能连续执行，读 MAST-VLA，重点检查技能分工和空间提示分别解决什么错误。
> **趋势**：前五篇的共同线索：这些论文共同把注意力放到动作所需的信息上：示范是否覆盖不同成功路径、记忆是否留下决定性事件、视觉特征是否对应运动结构、指令是否明确约束技能与接触位置。已有结果支持这些方向在各自测试条件下有用，但离线误差、表征相关性和闭环成功率仍是不同证据，不能互相替代。

- **规模**：2385 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 22、视觉语言动作模型 VLA 16、具身智能评测与基准 15、机器人学习 14、智能体 Agent 10、世界模型 5、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning](items/DiscoDemo%20Discovering%20Efficient%20and%20Diverse%20Robot%20Demonstrations%20for%20Imitation%20L.md)

> DiscoDemo 让强化学习先探索同一任务的多种成功做法，再把这些行为收集成示范，供视觉动作策略模仿。关键是只有成功得到保障时才鼓励行为多样，避免为了“不同”而生成无用数据。

- **能借鉴什么**：可以借鉴的是改变采集目标：先问数据里有几种可靠的解法，再问一共有多少条轨迹。当同一任务允许不同接近方向、动作顺序或运动路径，且能可靠判断成功时，这种采集思路值得尝试。
- **值得读吗**：值得读到数据生成目标和配平实验：最有用的部分是如何让“成功且不同”成为可执行的采集标准。

<details><summary>实验依据</summary>

摘要报告四项操作任务：下游策略平均成功率在仿真中由最强基线的 40% 升至 62%，真机由 39% 升至 78%；还报告成功状态覆盖更广，并称该做法能与纠正性数据采集互补。这支持所测任务和该预训练 VLA 下的数据收益。摘要没有给出任务名称、基线身份、数据量配平、试验次数或波动范围，尚不能量化多样性本身贡献了多少。

</details>

### 2. [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation](items/Memory%20before%20Goal%20Role%20of%20Pre-History%20Memory%20for%20Humanoid%20Loco-Manipulation.md)

> WholeBodyMem 给人形机器人保存“目标动作开始之前发生过什么”的记忆。它跟踪任务物体，在物体发生事件时留下关键画面，让动作模型能利用已经消失或被转身甩出视野的线索。

- **能借鉴什么**：值得借鉴的是按“哪些事件会改变后续答案”设计记忆，而不是单纯延长上下文。把记对答案和操作成功分开评估，也能区分机器人究竟忘了线索，还是记住了却没执行好。
- **值得读吗**：值得细读记忆选择、组件消融和评测设计：它把“需要记忆”变成了可以单独检验的任务条件。

<details><summary>实验依据</summary>

六项仿真记忆任务中，成功率为 72.6%，无记忆基座为 29.1%，均匀记忆为 44.4%；记忆决策准确率为 93.7%。[S37](https://arxiv.org/html/2610.31166v1#S5.SS3.p1.1) 六项 G1 真机任务每种策略每任务测试 10 次，WholeBodyMem 成功 53/60，无记忆基座为 22/60。[S38](https://arxiv.org/html/2610.31166v1#S5.SS5.p1.1) [S41](https://arxiv.org/html/2610.31166v1#S5.SS5.p4.1) 标准 SIMPLE 成功率也由 70.2% 升至 86.9%。[S36](https://arxiv.org/html/2610.31166v1#S5.SS2.p1.1) 但仿真测试仍在训练分布内；均匀记忆还同时缺少对象令牌和决策头，整体差距不能全部归因于选帧。[S13](https://arxiv.org/html/2610.31166v1#S3.I1.i6) [S33](https://arxiv.org/html/2610.31166v1#S5.SS1.p3.1)

</details>

### 3. [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](items/Sensorimotor%20Alignment%20A%20Platonic%20Proxy%20for%20Embodied%20Policy%20Success.md)

> Sensorimotor Alignment（S²）用离线数据检查：模型认为相似的场景与指令，是否也对应相似的机器人运动。它比较两种空间里的近邻是否重合，用来优先筛选值得花钱做闭环测试的模型。

- **能借鉴什么**：可借鉴的判断标准是：用于控制的表征，应当按动作需求组织相似性。当候选模型很多、已有匹配机器人数据而部署昂贵时，可以先用这种指标缩小测试范围，再保留闭环验证作为最终判断。
- **值得读吗**：值得读到指标定义和稳健性检查，把它当候选排序与诊断工具；目前证据不足以把它当作训练目标或成功率替代品。

<details><summary>实验依据</summary>

12 个 VLA 的 S² 与 SimplerEnv 成功率相关系数为 0.717，模型自助法 95% 区间为 [0.436, 0.912]。[S18](https://arxiv.org/html/2610.31670v2#S3.SS1.p2.1) 八个原始 VLM 的得分与微调后成功率相关为 0.681，而 VQA 分数为 −0.154。[S19](https://arxiv.org/html/2610.31670v2#S3.SS1.p3.1) [S24](https://arxiv.org/html/2610.31670v2#S3.SS2.p2.1) 真机证据来自同一既有评测的五种策略、40 项任务，相关为 0.831，并非本文重新开展全部真机实验。[S21](https://arxiv.org/html/2610.31670v2#S3.SS1.p5.1) 这些结果支持筛选用途，不能证明提高 S² 就会提高成功率。

</details>

### 4. [From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot](items/From%20Tabletop%20to%20Walking%20Bot%20Deploying%20a%20VLA%20Model%20on%20a%20Legged%20Manipulator%20Robot.md)

> 这篇研究如何把 VLA 从固定桌面机械臂搬到会走的机器人上，让底盘、身体姿态和机械臂一起完成操作。重点是实际部署所需的数据覆盖、示范规范、模型选择和动作预测长度，而非一个在摘要中明确命名的新模型。

- **能借鉴什么**：这里值得借鉴的是诊断顺序：换到移动机器人后，先检查示范是否覆盖底座、姿态与物体的不同关系，再决定是否增加模型容量。预测动作看似合理与整机能完成任务之间，还隔着参考系、执行时序和数据采集习惯。
- **值得读吗**：值得作为部署经验读到配置和失败分析；摘要足以提示关键工程变量，但还不足以提炼可直接照搬的参数。

<details><summary>实验依据</summary>

摘要称扩大示范覆盖使留出集末端误差降低 30%；增加推物等次要技能后，出现新的行为模式且基线表现未下降。闭环真机实验进一步展示数据组成如何影响成功与失败，但摘要未提供各组成功率。30% 是预测误差的下降，不能写成任务成功率提升；比较基准、误差单位、试验次数及统计波动也未给出。

</details>

### 5. [MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation](items/MAST-VLA%20Skill-Conditioned%20Adaptation%20with%20Trajectory-Affordance%20Priors%20for%20Mult.md)

> MAST-VLA 把多技能控制中的两个问题显式交给模型：现在该用哪种技能，以及应关注哪里、沿哪里运动。它用技能条件选择小型专家更新，再用从示范轨迹学到的热图引导动作生成。

- **能借鉴什么**：值得借鉴的是把同一份示范用得更充分：除了动作标签，还从轨迹中提取“哪些视觉区域与执行有关”的监督。当技能会共享物体却采用不同接触方式时，技能分工与空间引导分别约束不同层面的错误。
- **值得读吗**：值得细读热图构造和双分支消融：机制清楚，但应检查额外深度信息与各组件分别带来多少收益。

<details><summary>实验依据</summary>

CALVIN 在 A–C 场景训练、未见场景 D 测试，连续执行五个子任务且中途不重置。[S22](https://arxiv.org/html/2610.32312v1#S4.SS1.p2.1) 平均完成长度为 4.65，直接基线 VLA-Adapter-Pro 为 4.50；完成全部五项的比例由 80.0% 升至 84.7%。[S24](https://arxiv.org/html/2610.32312v1#S4.T1.2) 真机使用 Franka Research 3，两个场景、八种三步序列，每种每方法 20 次。[S29](https://arxiv.org/html/2610.32312v1#S4.SS3.p1.1) [S39](https://arxiv.org/html/2610.32312v1#A3.SS2.p2.1) 节选报告优于基线但未给真机具体数值；且本文额外使用静态视角深度，不能将全部收益归于模型结构。[S30](https://arxiv.org/html/2610.32312v1#S4.SS3.p2.1)

</details>

## 扫读 7 篇

- [Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies](items/Coupling%20Execution%20Horizon%20and%20Sampling%20Depth%20in%20Flow-Matching%20VLA%20Policies.md) — Horizon–Depth 研究机器人每次生成动作时，采样算多细、接下来连续执行多久该怎样一起选。关键发现是：长时间不重新观察时，较粗的数值积分反而可能收紧动作分散程度，减少累积漂移，同时降低推理延迟。
- [Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models](items/Progress%20Probes%20%24P%202%24%20Lightweight%20Runtime%20Monitoring%20for%20Vision-Language-Action.md) — Progress Probes P² 从 VLA 自己的内部激活中读出任务进度，再把偏离预期进度的执行标为异常。它用示范训练简单的线性探针，避免运行时额外调用大型视觉语言模型来监督机器人。
- [Learning Robot Behavior Priors from Non-Robotic Synthetic Data](items/Learning%20Robot%20Behavior%20Priors%20from%20Non-Robotic%20Synthetic%20Data.md) — 这篇用不包含真实机器人行为的程序合成数据，预训练 Transformer 做动作预测。关键是让合成任务保留控制问题的数学结构，使模型在看到陌生机器人任务的上下文后，也能作出有一定效果的预测。
- [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](items/RobustRLlib%20A%20Unified%20Library%20and%20Benchmark%20for%20Robust%20Reinforcement%20Learning%20Al.md) — RobustRLlib 把多种稳健强化学习算法接到统一接口，并用大量扰动配置检查它们各自在什么情况下管用。它的主要贡献是让已有算法更容易复用、比较，并把适用边界变得可检验。
- [When Human Corrections Travel: Safety in Federated VLA Adaptation](items/When%20Human%20Corrections%20Travel%20Safety%20in%20Federated%20VLA%20Adaptation.md) — When Human Corrections Travel 是一篇观点文：一台机器人的人类纠正被分享给其他机器人时，原本的安全含义可能被冲淡或误用。作者要求共享时保留纠正的语境与不确定性、在接收机器人上闭环检查，并同时评估隐私泄漏和安全证据保留。
- [FLORA: An Open Model Suite for Scaling Robotics Data Engines](items/FLORA%20An%20Open%20Model%20Suite%20for%20Scaling%20Robotics%20Data%20Engines.md) — FLORA 把机器人视频的三类标注放进同一套数据引擎：任务是否成功、执行过程好不好、什么时间发生了什么。它的着力点是让这些标签能以较低成本大量生产，服务训练和部署监测。
- [FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models](items/FocusVLA%20Future-Intent%20Guided%20Dynamic%20View%20Routing%20for%20Vision-Language-Action%20Mo.md) — FocusVLA 让机器人根据接下来可能发生的交互，动态决定更依赖全局相机还是腕部相机。关键是从历史动作预测未来交互意图，再用这个预测引导视角路由。

## 其余存档 12 篇

- [If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs](items/If%20at%20First%20You%20Don%27t%20Succeed%2C%20Backtrack%20Lightweight%20Recovery%20for%20Frozen%20VLAs.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- [AgentVQA: A Unified Benchmark for Agentic Visual Understanding](items/AgentVQA%20A%20Unified%20Benchmark%20for%20Agentic%20Visual%20Understanding.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies](items/FastHarness%20Experience-Driven%20Review%20Scheduling%20for%20Vision-Language-Action%20Polic.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- [Regularised RL improves sim-to-real transfer](items/Regularised%20RL%20improves%20sim-to-real%20transfer.md) · 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [CEMIR vs. FISER: a comparative study of reasoning-based and enrichment-based approaches to pragmatic intent recognition](items/CEMIR%20vs.%20FISER%20a%20comparative%20study%20of%20reasoning-based%20and%20enrichment-based%20appr.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [RynnUnify: Towards Unified Embodied Brain](items/RynnUnify%20Towards%20Unified%20Embodied%20Brain.md) · 多模态基础模型 智能体 Agent 机器人学习
- [Predictive Long-Horizon Progress Modeling with Action-Aware Quantification](items/Predictive%20Long-Horizon%20Progress%20Modeling%20with%20Action-Aware%20Quantification.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning](items/When%20to%20Stop%20Penalizing%20Actions%20Martingale%20GRPO%20for%20VLA%20Reinforcement%20Learning.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems](items/Do%20VLAs%20Know%20They%20Will%20Fail%20Interpretable%20Success%20and%20Failure%20Patterns%20in%20Physic.md) · 多模态基础模型 视觉语言动作模型 VLA
- [TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation](items/TravSUITE%20Traversability%20via%20Self-Supervised%2C%20Uncertainty-Aware%20IRL%20and%20Terrain.md) · 多模态基础模型 智能体 Agent 机器人学习
- [EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions](items/EgoForesight%20Effectively%20Scaling%20Policy%20Learning%20with%20Noisy%20Egocentric%20Actions.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习
- [HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games](items/HiSTEVE%201.0%20Harnessing%20Human-Interface%20VLA%20Agents%20for%20Open-World%20Games.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2385
- 入选条目：24
- 回填已见条目：0
- 最高分论文：DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning
- 最高分论文发布时间：2026-10-23T02:55:17Z
- 主要技术对象分类：多模态基础模型 22、视觉语言动作模型 VLA 16、具身智能评测与基准 15、机器人学习 14、智能体 Agent 10、世界模型 5、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)> (after 3 attempts)

</details>
