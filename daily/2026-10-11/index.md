---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-11
---

# 2026-10-11 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看三个问题：机器人失败后究竟该改哪里，动作正确是否意味着物体变化也正确，以及有限试错怎样换来可信的执行。先读 EVIS，理解如何把历史经验用于排试验顺序；再读《30,000 Hours》，检查世界模型是否只学好了人的动作；需要具体实现路线时读 UNITAS，看米制三维轨迹怎样同时服务控制与预测。
> **趋势**：前五篇的共同线索：这些论文共同把监督或验证落到具体变化上：技能交接后的状态、被操作物体的运动、动作随时间的变化，以及修改影响的调用路径。提供的结果支持这种细化有帮助，但还不能把短时预测、仿真成功或有限回归检查等同于长期真机可靠性。

- **规模**：2433 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、世界模型 13、智能体 Agent 9、机器人学习 9、多模态基础模型 7、视觉语言动作模型 VLA 6
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Experience-Guided Initiation Search for Learned Skills in Skill Composition](items/Experience-Guided%20Initiation%20Search%20for%20Learned%20Skills%20in%20Skill%20Composition.md)

> EVIS 给冻结的机器人技能寻找合适的起始站位：先用旧执行记录挑值得试的位置，再在新环境重复执行确认。它检查整段任务能否完成，避免“抽屉打开了，下一步却够不着”。

- **能借鉴什么**：值得借鉴的是把“哪里可能成功”和“是否有足够证据相信它”分开。旧经验可能失准、每次执行又昂贵时，先排序再验证，比要求历史模型精确预测新环境成功率更务实。
- **值得读吗**：值得读到资格检查和恢复搜索的实现，因为真正可复用的是有限预算下的接受、拒绝与继续搜索规则。

<details><summary>实验依据</summary>

实验在 RoboCasa365 仿真中使用冻结的 RLDX-1-FT-RC365，搜索底座平移及朝向，测试 OpenDrawer 和两种两阶段任务。[S26](https://arxiv.org/html/2610.11418v1#S5.SS1.p1.1) [S27](https://arxiv.org/html/2610.11418v1#S5.SS1.p2.1) 单技能对比固定预算、历史复用、Scratch-Sobol；一个示例首次成功需要 5 次查询，对方需 12 次，不能当作平均收益。[S31](https://arxiv.org/html/2610.11418v1#S5.SS2.p2.1) [S32](https://arxiv.org/html/2610.11418v1#S5.F4) [S33](https://arxiv.org/html/2610.11418v1#S5.SS2.p4.1) 两阶段资格检查使两个任务的可靠返回精度从 41.7%、8.3% 到 100%，但减少返回覆盖。[S36](https://arxiv.org/html/2610.11418v1#S5.T3.2.1) [S37](https://arxiv.org/html/2610.11418v1#S5.SS3.p6.1) 恢复实验中 EVIS Fallback 的最终可靠率为 41.7%，Sobol 为 33.3%，平均查询为 13.00、13.83。[S39](https://arxiv.org/html/2610.11418v1#S5.T4.2.1) 节选未给主实验完整均值和不确定性。

</details>

### 2. [What 30,000 Hours of Ego-centric Video Does Not Teach](items/What%2030%2C000%20Hours%20of%20Ego-centric%20Video%20Does%20Not%20Teach.md)

> 《What 30,000 Hours of Ego-centric Video Does Not Teach》发现，视频世界模型可以把手画在正确位置，却仍预测错手里的物体。它用骨架条件先解决身体运动，再通过 object-centric adaptive noise scheduling 把训练信号转向物体变化。

- **能借鉴什么**：评估动作条件世界模型时，可以先把可直接提供的身体运动信息喂清楚，再单独检查物体响应。否则“更多数据让视频更好”可能主要意味着手更准确，无法说明模型更适合预测操作后果。
- **值得读吗**：值得读到评估协议和噪声消融，因为它最有用的地方是揭示总体分数究竟掩盖了什么。

<details><summary>实验依据</summary>

Cosmos 3 变体在 300 至 30,000 小时数据上训练，测试来自不同设备、地点和参与者的 150 段真人视频，每窗口预测 16 帧。[S15](https://arxiv.org/html/2610.12464v1#S3.p1.1) [S22](https://arxiv.org/html/2610.12464v1#S3.SS2.p2.1) [S23](https://arxiv.org/html/2610.12464v1#S3.SS3.SSS0.Px1.p1.1) [S24](https://arxiv.org/html/2610.12464v1#S3.SS3.SSS0.Px1.p2.1) 骨架条件下 1,000 小时的身体保真度超过标准条件的 30,000 小时。[S7](https://arxiv.org/html/2610.12464v1#S1.p5.1) 物体 SCS 在百倍数据增长中仅增加约 0.09；拟合渐近值为 0.565。[S25](https://arxiv.org/html/2610.12464v1#S4.SS0.SSS0.Px2.p3.1) 新监督在 30,000 小时把物体分数从 0.527 提至 0.546，随机区域替换几乎消除收益，支持干预位置确实重要。[S26](https://arxiv.org/html/2610.12464v1#S5.SS0.SSS0.Px4.p1.1) [S27](https://arxiv.org/html/2610.12464v1#S5.SS0.SSS0.Px4.p2.1) 人形机器人迁移测试是仿真，物体 SCS 从人类预训练后的 0.73 到 0.79。[S28](https://arxiv.org/html/2610.12464v1#S6.SS0.SSS0.Px3.p1.1) [S31](https://arxiv.org/html/2610.12464v1#S6.T2.4)

</details>

### 3. [RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments](items/RoboRSI%20Stable%2C%20efficient%2C%20and%20reusable%20robot%20self-evolution%20in%20complex%20real-wor.md)

> RoboRSI 用 Top-Down Skill Refinement（TSR）把机器人程序分成责任明确的技能，失败后找到源头，只修改相关分支。修复先经过检查和历史用例验证，再供后续任务复用。

- **能借鉴什么**：可以借鉴软件维护中的责任边界：先规定技能承诺什么、怎样验证承诺，再谈自动改进。这样失败记录才有明确归属，修复才可能成为跨任务能力，而不是越来越长的临时补丁。
- **值得读吗**：值得读到技能接口、发布条件和失败归因实例，才能判断这套自动修复是否适用于自己的工具边界。

<details><summary>实验依据</summary>

仿真对比 CaP-X、Maestro、OpenETA，匹配骨干、工具和每回合交互预算。RoboRSI 在 LIBERO、LIBERO-PRO、RoboTwin 随评估在线改进，对方技能固定。[S17](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px1.p1.1) [S18](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px2.p1.1) [S19](https://arxiv.org/html/2610.12424v1#S4.SS2.SSS0.Px5.p1.1) [S20](https://arxiv.org/html/2610.12424v1#S4.SS3.SSS0.Px1.p1.1) 成功率分别为 56.0%、49.5%、24.0%，OpenETA 为 50.7%、38.5%、21.3%；冻结库的 LIBERO-Plus 为 42.1%，对方 36.4%。RoboTwin 回合数为 154 对 150。[S22](https://arxiv.org/html/2610.12424v1#S4.T1.9) 真机经历 104 轮家务开发并跨场景变化，但所给节选没有完整真机成功率曲线。[S7](https://arxiv.org/html/2610.12424v1#S1.p6.1)

</details>

### 4. [UNITAS: A 3D-Native World Action Model for Embodied Manipulation](items/UNITAS%20A%203D-Native%20World%20Action%20Model%20for%20Embodied%20Manipulation.md)

> UNITAS 把观察、手或夹爪运动、物体变化放进同一个米制三维坐标系，学习“怎么动”和“动后世界怎么变”。它用 action flow 表示操作点轨迹，用 scene flow 表示环境点位移，执行时也可以只生成控制指令。

- **能借鉴什么**：可借鉴的是让动作监督与场景预测共享有实际距离含义的坐标，而非仅给视觉网络附加深度。不同相机或身体可以改变外观，但同样的物理运动仍能使用共同轨迹接口。
- **值得读吗**：值得读到坐标约定与训练、推理分支，因为最有用的是三维接口设计，最容易误解的是把联合训练当成在线规划。

<details><summary>实验依据</summary>

RoboTwin 场景预测相对 PointWorld，Moving ADE、Moving FDE、Static ADE 分别降低 35%、21%、49%。[S7](https://arxiv.org/html/2610.12099v1#S1.p7.1) 策略在 LIBERO 平均成功率 99.8%，LIBERO-Plus 为 89.1%；消融中去掉三维位置编码，使参考模型成功率从 85.74% 降至 81.35%，尤其影响相机扰动。[S26](https://arxiv.org/html/2610.12099v1#S4.T1.2.1) [S35](https://arxiv.org/html/2610.12099v1#S4.SS4.p1.1) 真机两任务各 20 次：整理书籍 18/20，装球并拉链封袋 16/20，超过 π₀.₅ 和 Fast-WAM。[S29](https://arxiv.org/html/2610.12099v1#S4.SS3.p1.1) [S30](https://arxiv.org/html/2610.12099v1#S4.T2.fig1) [S31](https://arxiv.org/html/2610.12099v1#S4.T2.fig2) [S32](https://arxiv.org/html/2610.12099v1#S4.T2.fig2.1) 但引言 [S7](https://arxiv.org/html/2610.12099v1#S1.p7.1) 把后者写成 65%，与表格和正文的 80% 冲突，需核查版本。

</details>

### 5. [Higher-Order Action Supervision Makes A Strong Policy Class](items/Higher-Order%20Action%20Supervision%20Makes%20A%20Strong%20Policy%20Class.md)

> 《Higher-Order Action Supervision》不仅教策略“现在输出什么动作”，还教它“状态变化时动作应该怎样变化”。关键是用策略对状态的导数监督动作变化率，不增加一个独立动作输出头。

- **能借鉴什么**：如果连续轨迹可用，可以把相邻样本之间的变化趋势作为额外标签。与统一惩罚动作变化相比，它允许必要的快速转向，同时约束策略在数据经过的方向上别乱跳，特别适合检验少量演示是否被充分利用。
- **值得读吗**：值得读到损失推导和低数据消融：改动直接、可试验，但当前节选的数值证据不足以支持强性能判断。

<details><summary>实验依据</summary>

实验把方法加入 TD3+BC、ReBRAC 均值监督、IQL 和 IFQL，比较各自原版本；测试 OGBench reward-based singletask 和 D4RL MuJoCo 低数据环境。[S18](https://arxiv.org/html/2610.11175v1#S5.SS1.p1.1) [S19](https://arxiv.org/html/2610.11175v1#S5.SS1.p2.1) D4RL 每任务仅 10k 条转移，结果按 5 个随机种子汇总。[S20](https://arxiv.org/html/2610.11175v1#S5.T2) maze2d 示例使用 20 条成功轨迹和 500k 训练步，展示更平滑轨迹。[S4](https://arxiv.org/html/2610.11175v1#S1.F1) 摘要宣称性能和鲁棒性改善，但输入没有主结果表数值，不能给出平均增益、显著性或最强受益任务。

</details>

## 扫读 7 篇

- [WOVEN: Weaving Visual World Modeling into Multimodal LLMs](items/WOVEN%20Weaving%20Visual%20World%20Modeling%20into%20Multimodal%20LLMs.md) — WOVEN 让多模态模型练习判断画面经过某种变化后会怎样，再检查这项能力能否帮助其他任务。它最值得关注的发现是：选训练数据时，教会哪种推理操作可能比展示哪类场景或动作更关键。
- [DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception](items/DVD%20Dynamic%20Vector%20Decoding%20for%20Efficient%20MLLM-based%20Perception.md) — DVD 把框、掩码等几何结果转换成紧凑的离散 token，再用轻量解码器还原。这样，多模态模型不用逐个输出长串坐标文字，同时尝试缓解固定坐标量化的范围和精度限制。
- [Unifying Policy Learning and State Prediction through Spatial Language Modeling](items/Unifying%20Policy%20Learning%20and%20State%20Prediction%20through%20Spatial%20Language%20Modeling.md) — Spatial Language Modeling 用同一套坐标和语义 token 表达场景、目标、动作以及动作后的状态，让一个 Transformer 同时学“往哪推”和“推完会怎样”。控制时，它只生成可执行动作，再用实际观察更新历史。
- [Fast Pose Tracking of Rigid Objects with Compact Pose Graph Optimization](items/Fast%20Pose%20Tracking%20of%20Rigid%20Objects%20with%20Compact%20Pose%20Graph%20Optimization.md) — 这篇把长期物体姿态跟踪的优化对象，从大量匹配点改成少量相对姿态约束，并按几何对齐的不确定性分配权重。这样每次优化不用处理所有点，仍能利用多次观察限制漂移。
- [PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies](items/PathTime-VLA%20Path-Time%20Decoupling%20for%20Factorized%20Post-Training%20of%20Vision-Languag.md) — PathTime-VLA 把机器人“沿哪里走”和“走多快”分开学习，避免把遥操作中的停顿和延迟一起当成理想动作。它先建立路径能力，再分别用机器人交互调整速度、用执行结果改进路径。
- [Neural Networks for Temporal Pattern Recognition and Dynamic Arm Gesture Speed Estimation for Robot Control](items/Neural%20Networks%20for%20Temporal%20Pattern%20Recognition%20and%20Dynamic%20Arm%20Gesture%20Speed%20E.md) — 这篇先比较哪些小型网络擅长读懂时间序列，再把筛出的 BiGRU、TCN 和 GRUReLU 用于估计人做手臂手势的速度。关键是把“速度”拆成三种可测目标，分别检验骨架序列能预测得多准。
- [Generative Neural Retargeting for Human-to-Robot Dexterous Manipulation](items/Generative%20Neural%20Retargeting%20for%20Human-to-Robot%20Dexterous%20Manipulation.md) — Generative Neural Retargeting（GNR）把人类灵巧操作转换成机器人可执行轨迹：先学习多条示范共享的可行运动分布，再按当前人类动作生成候选。巧处是让此前积累的轨迹帮助下一次转换，减少每条示范从头搜索的成本。

## 其余存档 12 篇

- [ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation](items/ContourVLA%20A%20Closed-Loop%20Perception-Action%20Contour%20Policy%20for%20Generalized%20Referr.md) · 多模态基础模型 视觉语言动作模型 VLA
- [CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding](items/CAPABLE%20Capability-Aware%20Policy%20Adaptation%20via%20Behavioral%20Latent%20Encoding.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning](items/TACROSS%20An%20Efficient%20and%20Low-Cost%20Scalable%20Human%20Touch%20System%20Across%20Heterogeneo.md) · 机器人学习
- [When to Intervene? State-Aware Sparse Manipulation in Federated Reinforcement Learning](items/When%20to%20Intervene%20State-Aware%20Sparse%20Manipulation%20in%20Federated%20Reinforcement%20Lea.md) · 智能体 Agent 机器人学习 具身智能评测与基准
- [FloorSAV: Elucidating Spatial Audio-Visual Context with 2D Floormap for AV-LLMs](items/FloorSAV%20Elucidating%20Spatial%20Audio-Visual%20Context%20with%202D%20Floormap%20for%20AV-LLMs.md) · 智能体 Agent 具身智能评测与基准
- [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](items/OmniDex%20Scaling%20Dexterous%20Hand%20Grasping%20to%20Diverse%20Cluttered%20Scenes.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [MiniWAM: Learning Compact Future Targets for Efficient World-Action Modeling](items/MiniWAM%20Learning%20Compact%20Future%20Targets%20for%20Efficient%20World-Action%20Modeling.md) · 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Leveraging Human-In-The-Loop Demonstrations in Reinforcement Learning for Digital Twin-Driven Robot Flexibility](items/Leveraging%20Human-In-The-Loop%20Demonstrations%20in%20Reinforcement%20Learning%20for%20Digita.md) · 世界模型 机器人学习 具身智能评测与基准
- [Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception](items/Acting%20from%20Belief%2C%20Looking%20When%20Needed%20A%20Bayesian%20Spatial%20World%20Model%20for%20Navig.md) · 智能体 Agent 世界模型
- [DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors](items/DAMP%20Humanoid%20Locomotion%20via%20Denoised%20Belief%20Learning%20and%20Adversarial%20Motion%20Pri.md) · 世界模型 机器人学习 具身智能评测与基准
- [GLIO2: A GPU-Parallelized Tightly-Coupled LiDAR-Inertial-GNSS System for Robust and Real-Time Global Localization and Mapping](items/GLIO2%20A%20GPU-Parallelized%20Tightly-Coupled%20LiDAR-Inertial-GNSS%20System%20for%20Robust%20a.md) · 具身智能评测与基准
- [Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction](items/Multi-Agent%20Egocentric%20World%20Model%20with%20Fine-Grained%20Embodied%20Interaction.md) · 智能体 Agent 世界模型

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2433
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Experience-Guided Initiation Search for Learned Skills in Skill Composition
- 最高分论文发布时间：2026-10-08T07:46:08Z
- 主要技术对象分类：具身智能评测与基准 17、世界模型 13、智能体 Agent 9、机器人学习 9、多模态基础模型 7、视觉语言动作模型 VLA 6
- 信息源错误：0
- 自动恢复信息源：0

</details>
