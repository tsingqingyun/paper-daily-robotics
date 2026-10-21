---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-21
---

# 2026-10-21 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人已经会做动作之后，怎样让动作更快、更协调，并确认预测和评分真的对应实际完成任务。先读 PaceVLA，理解何时可以合并动作、何时必须频繁观察；再读 HAF-VLA，看全身动作为什么需要按身体依赖顺序生成；最后读 Ropedia W0，检查统一运动表示怎样让人类视频帮助机器人预测未来。农业论文适合了解具体适配流程，Bitter Lesson 则提醒我们区分局部进展与完整任务成功。
> **趋势**：前五篇的共同线索：这些论文共同把注意力移到动作接口：预测未来需要统一运动条件，执行动作需要选择时间粒度或身体生成顺序。另一条共同提醒是，视频质量、阶段得分和完整任务成功测量的是不同能力，不能相互替代。

- **规模**：2458 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 21、多模态基础模型 19、视觉语言动作模型 VLA 14、世界模型 13、机器人学习 13、智能体 Agent 11、Sim2Real 3
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](items/Ropedia%20W0%20Scaling%20Loco-Manipulation%20World%20Models%20across%20Embodiments%20with%20Human.md)

> Ropedia W0 用“相机怎么移动、手或机械臂骨架怎么移动”作为共同输入，让同一个模型预测人类和不同机器人接下来看到的视频。关键是统一运动的表达方式，同时保留各自身体结构，使大量人类经历能够参与机器人世界模型训练。

- **能借鉴什么**：值得借鉴的是：混合不同身体的数据前，先寻找共同可观测的运动后果，而非直接拼接关节命令。前提是能获得可靠相机轨迹和骨架；这也把标注质量变成方法成立的重要条件。
- **值得读吗**：值得细读运动接口与数据处理，再核查控制实验；目前最扎实的理由是跨数据集视频预测，而非已经得到通用物理模拟器。

<details><summary>实验依据</summary>

测试覆盖五个机器人基准及未见人类视频。Xp-Teleop 上，A14B midtrain 无后训练的 PSNR/SSIM/LPIPS 为16.42/0.537/0.259，优于 Cosmos3-Nano 全数据后训练的14.98/0.508/0.293[S26](https://arxiv.org/html/2610.26855v1#S6.T4.4)。人类测试含200段未见视频[S19](https://arxiv.org/html/2610.26855v1#S6.SS2.p1.1)。这些支持视频预测与数据迁移能力；不能单凭图像指标证明接触物理准确。下游控制效果在[S8](https://arxiv.org/html/2610.26855v1#S1.p4.1)有定性结论，节选未给具体数值。

</details>

### 2. [Robot Learning with Vision-Language-Action Models for Agricultural Manipulation](items/Robot%20Learning%20with%20Vision-Language-Action%20Models%20for%20Agricultural%20Manipulation.md)

> 这篇把 Octo 和 π₀.₅ 适配到番茄接近与抓握：先在 MuJoCo 中遥操作收集示范并微调，再用真机示范继续微调。它的重点是跑通农业任务的数据与执行流程，并比较换视角、换布局之后两种策略还能做得怎样。

- **能借鉴什么**：可借鉴的是把仿真用于低成本示范和可控扰动，再用真机数据校正外观、延迟和夹爪差异。对接近与抓握这类能保持相似动作接口的任务，这是一条可以逐环节检查的适配路线。
- **值得读吗**：适合读到数据采集与部署细节；若要据此选择策略或估算仿真收益，必须补看结果表和受控对比。

<details><summary>实验依据</summary>

仿真比较同分布、视角/空间偏移及分布外条件，也比较有无本体状态输入；真机是 FR3 与人工番茄植株，配外部和腕部相机[S25](https://arxiv.org/html/2610.26717v1#S3.SS2.p1.1) [S29](https://arxiv.org/html/2610.26717v1#S4.p1.1) [S30](https://arxiv.org/html/2610.26717v1#S4.F7) [S31](https://arxiv.org/html/2610.26717v1#S4.SS2.p1.1)。摘要报告π₀.₅任务得分更高、分布变化下退化更少，但提供材料未包含得分定义、具体结果、试验次数及误差范围，因此无法量化优势，也无法判断本体状态究竟帮了多少。

</details>

### 3. [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models](items/PaceVLA%20Adaptive%20Temporal%20Action%20Quantization%20in%20Vision-Language-Action%20Models.md)

> PaceVLA 让机器人自己判断当前能否加快：空旷移动可以合并动作，精细接触则保留小步和较短预测。它同时学习多种时间粒度的动作解码器，并根据当前场景选择使用哪一种。

- **能借鉴什么**：这里最可借鉴的是把“多久重新看一次、动作走多大步”也交给策略选择。只有当任务中确实同时存在可快速通过的阶段和精细交互阶段时，这种额外学习才有明确动机。
- **值得读吗**：值得细读训练目标与控制器配置；它把加速落实为可测试的场景决策，但复现不能只添加一个模式选择头。

<details><summary>实验依据</summary>

覆盖 RoboCasa-Kitchen、LIBERO、DexJoCo 仿真及六项真机任务[S9](https://arxiv.org/html/2610.25961v1#S1.p4.1)。DexJoCo 中，相比 GR00T N1.5，成功率从76.3%到77.3%，有效加速指标为1.11[S34](https://arxiv.org/html/2610.25961v1#S4.T4.fig1.7)；真机 ALLEX 输送任务吞吐量从每分钟3.6件到6.3件，成功率从86%到94%[S36](https://arxiv.org/html/2610.25961v1#S4.T4.fig2.7)。固定合并在该任务仅72%成功。结果支持这些任务上的速度与成功率兼顾，不能把最高加速倍数当所有场景的收益。

</details>

### 4. [The Bitter Lesson Comes to Robotics](items/The%20Bitter%20Lesson%20Comes%20to%20Robotics.md)

> The Bitter Lesson Comes to Robotics 把多种通用多模态语言模型接到同一台真机上，比较它们直接指定夹爪位姿能做多少事、花多久和多少钱。它发现局部操作能力正在进步，但有限动作预算内完整完成任务仍然困难。

- **能借鉴什么**：值得借鉴的是把失败尝试也计入每项有效进展的时间与成本：模型能偶尔完成一个动作，不代表它能经济地完成任务。定位、验证抓取和错误恢复应当与语言推理能力分开观察。
- **值得读吗**：值得细读评测协议和失败轨迹；标题里的长期判断应当作为待验证假设，当前证据更适合说明能力与效率的实际边界。

<details><summary>实验依据</summary>

七个模型、十二种配置，在叠碗、收纳入保险箱、分类、盖笔帽、装倒水果和扶瓶六项真机任务上，每配置每任务20次[S13](https://arxiv.org/html/2610.25287v1#S3.F1.3) [S17](https://arxiv.org/html/2610.25287v1#S3.p3.1)。最强模型平均阶段得分45%–48%，主要来自局部进展，并非同等比例的完整成功[S22](https://arxiv.org/html/2610.25287v1#S4.p3.1)。摘要按2026年7月至9月的结果估计得分翻倍时间44.5天、最佳执行率提高4.4倍、最低成本下降6.2倍；这些是短期观测趋势。

</details>

### 5. [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control](items/HAF-VLA%20Hierarchical%20Action%20Flow%20Framework%20for%20Humanoid%20Vision-Language-Action%20C.md)

> HAF-VLA 不再一次生成全部人形机器人动作，而是先生成移动和头部动作，再加入腰部，最后生成全身操作。后续阶段读取前面阶段的动作表示并允许小幅修正，让双臂操作建立在较一致的身体移动方案上。

- **能借鉴什么**：可借鉴的是按身体依赖组织生成：先确定支撑后续操作的移动与姿态，再生成精细操作，同时留出回修空间。若误差常表现为手臂替错误站位补偿，这比单纯增加去噪步数更有针对性。
- **值得读吗**：值得细读累计动作掩码与缓存实现；真实硬件和受控消融提供了理由，但还不足以证明这种阶段顺序适合所有全身任务。

<details><summary>实验依据</summary>

在天工2.0与3.0上，每任务采集120条示范，主测试六任务、各设置10次真机运行[S21](https://arxiv.org/html/2610.26584v1#S4.SS1.p1.1) [S24](https://arxiv.org/html/2610.26584v1#S4.SS1.p3.1)。对比ACT、π₀.₅、GR00T N1.7和Cosmos Policy，平均归一化阶段得分由最强基线π₀.₅的53.3%升至68.3%[S29](https://arxiv.org/html/2610.26584v1#S4.T1.4)。搬箱消融中完整方法86.7%，训练部署均去缓存为50.0%，改成手臂优先为60.0%[S32](https://arxiv.org/html/2610.26584v1#S4.T2.4)。支持该设置下顺序与缓存有用；这些分数不是完整成功率。

</details>

## 扫读 7 篇

- [Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation](items/Vector-Quantized%20World%20Model%20Latent%20Feedback%20Motion%20Planning%20for%20Robot%20Manipulat.md) — VQ-WM 把长任务拆成一串视觉状态：先在离散状态之间找路线，再让连续控制器看着实际画面逐段走到。巧处是按“控制器需要多久才能到达”划分状态，让规划地图更贴近机器人真正能走的路。
- [AQUAACT: A Joystick-Level Underwater Teleoperation Dataset and Closed-Loop Benchmark](items/AQUAACT%20A%20Joystick-Level%20Underwater%20Teleoperation%20Dataset%20and%20Closed-Loop%20Benchm.md) — AQUAACT 记录水下驾驶员“看到什么、怎样拨摇杆”，让策略学习接替驾驶员，并保留原有飞控负责把指令变成运动。它同时提供闭环测试：会预测驾驶动作，离真正完成水下任务仍有明显距离。
- [Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation](items/Vision-Language-Delta-Action%20Learning%20Compact%20Deltas%20as%20Actionable%20Transition%20In.md) — VLDA 不要求模型把完整未来都预测出来，而是学习一个紧凑的 Delta，表示任务需要发生什么变化，再用它引导动作生成。关键是同时保留局部操作变化与整体目标方向，避免容量被静止背景占用。
- [PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](items/PVBench%20Quantifying%20Physical%20Plausibility%20in%20Video%20Generation%20with%20Object-Level.md) — PVBench 把“视频看起来符合物理吗”拆成可检查的对象属性和运动量，尽量用姿态、尺度、运动及守恒残差来测。它的关键是把部分物理判断落实到数值测量，而不只请视觉语言模型打一个总分。
- [HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation](items/HandsOn%20A%20Large-Scale%20Simulation%20Benchmark%20for%20Generalizable%20Dexterous%20Manipulat.md) — HandsOn 提供可以组合机械臂、灵巧手、物体和任务的仿真平台，检验策略能否可靠完成多样操作及迁移任务。它还把失败拆到接触、动作协调和保持已完成目标等阶段，帮助解释机器人究竟卡在哪里。
- [FR-VLA: Implicit Force Reasoning VLA for Contact-Rich Manipulation](items/FR-VLA%20Implicit%20Force%20Reasoning%20VLA%20for%20Contact-Rich%20Manipulation.md) — FR-VLA 让机器人先根据画面和语言任务判断当前有多需要力反馈，再调节力信息对动作的影响。巧处是把“测到了多少力”和“现在该多重视它”分开处理。
- [SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models](items/SPAR%20Structural%20Pruning%20and%20Action%20Recovery%20for%20Vision-Language-Action%20Models.md) — SPAR 先把 VLA 语言骨干中的隐藏维度和前馈中间维度大幅裁小，再用强化学习恢复操作能力。它把压缩和动作恢复分成两个相接的步骤，使模型变小后仍有机会重新学会完成任务。

## 其余存档 12 篇

- [Robotic Photography System based on Vision-Language-Action Model](items/Robotic%20Photography%20System%20based%20on%20Vision-Language-Action%20Model.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [ReDOA: Real-World Distillation via Observation Alignment for Image-Based Manipulation Policy Learning](items/ReDOA%20Real-World%20Distillation%20via%20Observation%20Alignment%20for%20Image-Based%20Manipula.md) · 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [ReInsVLN: Revisiting Historical Evidence for Training-Free Vision-and-Language Navigation](items/ReInsVLN%20Revisiting%20Historical%20Evidence%20for%20Training-Free%20Vision-and-Language%20Na.md) · 视觉语言动作模型 VLA 具身智能评测与基准
- [TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models](items/TILDE%20Teacher-in-the-Loop%20Distillation%20from%20Embodied%20Foundation%20Models.md) · 多模态基础模型 机器人学习 具身智能评测与基准
- [Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds](items/Compile%20Once%2C%20Run%20Cheap%20Frozen%2C%20Portable%20Skills%20for%20Embodied%20Agents%2C%20and%20What%20Re.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation](items/Physical%20Words%20A%20Vocabulary%20for%20Structuring%20Latent%20Reasoning%20in%20Robot%20Manipulati.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation](items/GPT-6%20Astra%20Is%20a%20Native%20Visuo-Tactile%20Policy%20for%20Contact-Rich%20Manipulation.md) · 多模态基础模型 机器人学习 具身智能评测与基准
- [RoboValue: A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models](items/RoboValue%20A%20Fine-Grained%20Sim-and-Real%20Benchmark%20for%20Unified%20Evaluation%20of%20Roboti.md) · 世界模型 机器人学习 具身智能评测与基准
- [ForagerSim: Evaluating Embodied Map-Based Reasoning in Large-Scale Dynamic Worlds](items/ForagerSim%20Evaluating%20Embodied%20Map-Based%20Reasoning%20in%20Large-Scale%20Dynamic%20Worlds.md) · 世界模型 机器人学习 具身智能评测与基准
- [PhantomTac: Hijacking Robotic Tactile Systems with Deploy-and-forget Tags](items/PhantomTac%20Hijacking%20Robotic%20Tactile%20Systems%20with%20Deploy-and-forget%20Tags.md) · 多模态基础模型 具身智能评测与基准
- [CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA](items/CondenseVLA%20Learnable%20History%20Condensation%20for%20Efficient%20Multi-Frame%20VLA.md) · 多模态基础模型 视觉语言动作模型 VLA
- [Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving](items/Think%20Densely%2C%20Act%20Sparsely%20Latent%20Expert%20Cognitive%20Chains%20for%20Vision-Language-A.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2458
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience
- 最高分论文发布时间：2026-10-19T17:59:55Z
- 主要技术对象分类：具身智能评测与基准 21、多模态基础模型 19、视觉语言动作模型 VLA 14、世界模型 13、机器人学习 13、智能体 Agent 11、Sim2Real 3
- 信息源错误：0
- 自动恢复信息源：0

</details>
