---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-24
---

# 2026-11-24 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先追问：机器人失败时，怎样判断该改执行流程、补练动作，还是先改评测？先读 TRIP，看怎样把即时停机和较慢的重新规划分开；再读 LS-MBPO，看冻结的视觉策略怎样参与短程想象训练；如果要判断仿真分数能否指导真机选型，就读 RoboColiseum 的配对验证和计分协议。
> **趋势**：前五篇的共同线索：几篇工作把笼统的任务失败拆成了可单独测量的问题，包括执行中何时停机、抓取后能否恢复、跨次经验是否有用，以及仿真分数能否反映真机表现。理解收益时，尤其要看对照究竟固定了底层策略、交互预算，还是只固定了任务。

- **规模**：2511 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 20、世界模型 15、智能体 Agent 10、机器人学习 10、多模态基础模型 9、视觉语言动作模型 VLA 8、Sim2Real 2
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance](items/Tripwire%20Robot%20Agents%20that%20Program%20Their%20Own%20Interrupts%20under%20Human%20Disturbance.md)

> TRIP 让高层智能体在启动机器人动作时，顺手写一段监测程序。程序发现人靠近或目标被挪动等情况时，可以先叫停机器人，再请智能体决定怎么继续。

- **能借鉴什么**：是否必须马上停，以及停下后该做什么，可以交给两个速度不同的环节。只要扰动有可及时测量的信号、底层调用也能中止，就可以保留原有策略，把耗时推理留给真正需要改计划的时刻。
- **值得读吗**：值得读到执行循环和消融。固定初始规则后 XR 的无接触率降回 61.3%，能看出随决策改写规则在该设置中的作用。[S40–S41]

<details><summary>实验依据</summary>

RoboHD 在 168 个模拟厨房场景中测试了三个 VLA 和一个 WAM。最强策略 XR 接入 TRIP 后，相比同智能体、同工具的回合制基线，无接触率从 61.3% 升到 81.3%，有人的任务成功率从 31.0% 升到 38.7%。前一指标只统计至少一种对照方法能在无人时完成的 150 个 XR 场景，后一指标要求完成且无接触。真机挂杯和挂毛巾受扰时，TRIP 成功 25/40，回合制为 5/40，单独运行策略为 1/40。[S7](https://arxiv.org/html/2611.27182v1#S1.p5.1)[S32](https://arxiv.org/html/2611.27182v1#S4.I2.i1) [S33](https://arxiv.org/html/2611.27182v1#S4.I2.i2) [S34](https://arxiv.org/html/2611.27182v1#S4.I2.i3) [S35](https://arxiv.org/html/2611.27182v1#S4.F4)

</details>

### 2. [Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models](items/Efficient%20VLA%20Reinforcement%20Learning%20via%20Subchunk%20Rollouts%20in%20Latent%20World%20Model.md)

> LS-MBPO 用世界模型预测压缩后的未来状态，省去生成整段视频的开销。冻结的 VLA 先给一串参考动作，小策略再根据预测状态逐段修正，好让强化学习能在想象中继续走下去。

- **能借鉴什么**：如果原策略通常能给出方向正确的动作，只在局部对准上出错，就可以让原策略提供参考，让一个能读压缩状态的小模型负责修正。这样能保留原策略的视觉接口，同时让想象轨迹在短时间内根据预测结果调整动作。
- **值得读吗**：值得读到训练与部署的动作刷新频率，以及 Dreamer 对照。这两处决定你能否复用子段设计和正确解读收益。

<details><summary>实验依据</summary>

LIBERO 和 RoboTwin 仿真用任务成功率比较原始 VLA、模仿学习、在线强化学习及同样用子段的 Dreamer。LIBERO Long 上 LS-MBPO 为 71.2%，Dreamer 为 69.6%，原始 π₀.₅-SFT 为 52.0%。作者也报告 VLA-MBPO 为 64.4%，两者使用不同 GPU，节选未给可直接对照的总训练时长。ALOHA 真机评估插笔和插充电器，每项 20 回合，所给节选未列各方法的真机成功率。[S6](https://arxiv.org/html/2611.27645v1#S1.p3.1)[S23](https://arxiv.org/html/2611.27645v1#S4.SS1.SSS0.Px1.p1.1) [S24](https://arxiv.org/html/2611.27645v1#S4.SS1.SSS0.Px2.p1.1) [S25](https://arxiv.org/html/2611.27645v1#S4.SS1.SSS0.Px3.p1.1) [S26](https://arxiv.org/html/2611.27645v1#S4.SS1.SSS0.Px3.p2.1) [S27](https://arxiv.org/html/2611.27645v1#S4.T1) [S28](https://arxiv.org/html/2611.27645v1#S4.T1.2)

</details>

### 3. [RoboColiseum: Co-evolution of Simulation, Evaluation, and Models](items/RoboColiseum%20Co-evolution%20of%20Simulation%2C%20Evaluation%2C%20and%20Models.md)

> RoboColiseum 把真机命令回放到仿真里，检查机器人和物体是否呈现相近的反应。它也把机器人评测拆成不同能力赛道，记录系统完成了多少、用了多少执行额度。

- **能借鉴什么**：当仿真用于筛选候选机器人方案时，可以先问关键物理交互的真机与仿真差多少，再看各赛道的分数。这样既能发现模拟接触偏差，也能避免用综合排名挑错擅长特定操作的系统。
- **值得读吗**：值得细读校准验证和执行计分协议，榜单适合按目标赛道查阅，因为总分会掩盖能力差异。

<details><summary>实验依据</summary>

22 组同机器人、同任务的真机与仿真配对分数，皮尔逊相关系数为 0.9686，表明这些配置的分数有很强的线性关联。[S1](https://arxiv.org/html/2611.27042v1#abstract1.1)[S39](https://arxiv.org/html/2611.27042v1#S5.F8) 第一季选列的 12 个策略中，Prime-0 总分最高，为 77.54，空间推理领先的却是总分 76.92 的 HiDream-O1-Embodied。[S40](https://arxiv.org/html/2611.27042v1#S5.SS2.p1.1) [S41](https://arxiv.org/html/2611.27042v1#S5.T2) [S42](https://arxiv.org/html/2611.27042v1#S5.T2.2) [S43](https://arxiv.org/html/2611.27042v1#S5.T2.3) [S44](https://arxiv.org/html/2611.27042v1#S5.SS2.p2.1) 第二季覆盖全部 11 个公开系统，但训练、任务覆盖和资源统计存在差异。[S1](https://arxiv.org/html/2611.27042v1#abstract1.1)[S46](https://arxiv.org/html/2611.27042v1#S5.SS3.p3.1)

</details>

### 4. [FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models](items/FoRe%20A%20Force-Guided%20Framework%20for%20Autonomous%20Grasp%20Recovery%20in%20Vision-Language-A.md)

> FoRe 给取放机器人加了一道物理确认：抓取命令开着时，结合力信号判断物体是否抓住或滑脱。发现失手后，它切到专门练过的重抓策略，恢复抓取后再继续搬运。

- **能借鉴什么**：能直接测到动作结果时，可以用这个信号决定下一步，再把学习资源集中在最常见的恢复起点。尤其适合示范大多成功、失手后机器人却反复落入相似错误姿态的任务。
- **值得读吗**：值得细读阶段标注、重抓起点和策略切换，这三个细节决定拿到自己的力信号后能否照搬。

<details><summary>实验依据</summary>

LIBERO-SUCTION 仿真中，VLA-Adapter 的平均任务成功率从 69.2% 升到 87.6%，π₀.₅ 从 85.9% 升到 92.4%。在 LIBERO，两种骨干接入 FoRe 后分别比接入 CycleVLA 高 1.0 和 0.4 个百分点。真机使用 DOBOT 机械臂和真空夹具，每任务 40 次，平均成功率分别从 26.7% 升到 51.7%、从 48.3% 升到 70.0%。摘要也报告两套仿真每任务仅一条示范时仍有收益，所给节选未列具体幅度。[S1](https://arxiv.org/html/2611.27011v1#abstract1.1)[S47](https://arxiv.org/html/2611.27011v1#S4.T1.5) [S48](https://arxiv.org/html/2611.27011v1#S4.T2) [S49](https://arxiv.org/html/2611.27011v1#S4.T2.5) [S50](https://arxiv.org/html/2611.27011v1#S4.SS1.SSS0.Px4.p1.1)[S53](https://arxiv.org/html/2611.27011v1#S4.SS1.SSS0.Px6.p1.1)[S56](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px1.p1.1) [S57](https://arxiv.org/html/2611.27011v1#S4.F5) [S58](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px3.p1.1) [S59](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px4.p1.1)

</details>

### 5. [Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](items/Embodied-Harness%20Towards%20Recursive%20Self-Improvement%20for%20Robotic%20Manipulation.md)

> Embodied-Harness 让 Actor 操作机器人，让 Reflector 根据动作、反馈和现场变化写下以后能用的操作规则。后续尝试复用这些规则，模型参数保持冻结。

- **能借鉴什么**：执行日志可以直接参与下次决策。如果失败与某个可复查的前置条件有关，例如动作发出前物体姿态就不对，那么一条带检查动作的指导会比笼统记录「上次放置失败」更容易复用。
- **值得读吗**：值得读到去掉短期记忆和去掉 Reflector 的两项消融，再看逐轮曲线，才能区分本轮记得住和下轮借得到经验的收益。[S27][S39]

<details><summary>实验依据</summary>

RoboTwin 2.0 从干净到随机化场景的仿真中，零示范、同用 GPT-6 Astra 时，成功率为 82.4%，RoboDawn 为 53.2%。RoboSPA L5 空间子集为 94.0% 对 65.6%，长流程为 59.5% 对 41.4%，摘要的 76.7% 是 RoboSPA 汇总。RMBench 记忆任务为 94.4%，比 MaP-WAM 高 11.1 个百分点。Piper 真机三项任务各 10 回合，平均成功率为 96.7%，π₀.₅ 为 40.0%。[S1](https://arxiv.org/html/2611.27689v1#abstract1.1)[S16](https://arxiv.org/html/2611.27689v1#S3.T1.4) [S17](https://arxiv.org/html/2611.27689v1#S4.SS1.p1.1) [S18](https://arxiv.org/html/2611.27689v1#S4.SS1.p2.1) [S19](https://arxiv.org/html/2611.27689v1#S4.T2) [S20](https://arxiv.org/html/2611.27689v1#S4.T2.2) [S21](https://arxiv.org/html/2611.27689v1#S4.T3) [S22](https://arxiv.org/html/2611.27689v1#S4.T3.2)[S25](https://arxiv.org/html/2611.27689v1#S4.T6.fig1.1)[S33](https://arxiv.org/html/2611.27689v1#S4.SS2.p5.1)

</details>

## 扫读 7 篇

- [TrajRealm: A Large-Scale Point Tracking Dataset with Diverse Dynamics](items/TrajRealm%20A%20Large-Scale%20Point%20Tracking%20Dataset%20with%20Diverse%20Dynamics.md) — TrajRealm 从游戏和具身仿真里收集大量运动场景，并为同一个点持续标注它在画面和三维空间中的位置。它让跟踪器有机会学会在复杂运动中认出原来的点，也用 TrajRealm-Bench 检查跟踪器何时丢失这种对应。
- [BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight](items/BeyondEgo%20Learning%20to%20Act%20Beyond%20Egocentric%20Perception%20via%20Humanoid%20Ego-Exo%20Fore.md) — BeyondEgo 给人形机器人加一台从外部看它的相机，帮助它在操作物体时掌握全身与环境的位置关系。训练时，它还让当前特征帮助预测两路画面稍后的样子，部署时去掉专门做预测的模块。
- [GenPA: Image Generators as Efficient Robot Policies](items/GenPA%20Image%20Generators%20as%20Efficient%20Robot%20Policies.md) — GenPA 把预训练图像生成模型直接改成机器人动作预测器，并用它原有的图像训练方式辅助感知。部署时模型前向计算一次就回归一段动作，训练消融也表明，把当前场景的深度教给模型是一种有效配方。
- [$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence](items/%24%CE%B3%24-Scape%20An%20Agent-Centric%20World%20for%20Mobile%20Embodied%20Intelligence.md) — γ-Scape 让移动机器人智能体在持续存在的仿真场景里，通过程序调用工具完成从导航到操作的整套任务。它记录工具执行和动作的物理后果，使同一次交互可用于修改程序或训练策略。
- [RoboPRO: A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipulation](items/RoboPRO%20A%20Perturbation-Resilient%20and%20Obstacle-Aware%20Benchmark%20for%20Robotic%20Manipu.md) — RoboPRO 把双臂操作放进有杂物和扰动的室内场景，除了看任务成没成，还记录机器人有没有发生不安全接触。它通过分因素比较，帮助定位策略究竟怕杂物、指令变化，还是物体层面的变化。
- [NormFlowSDE: Normalizing Flows for Amortized Bayesian State Estimation](items/NormFlowSDE%20Normalizing%20Flows%20for%20Amortized%20Bayesian%20State%20Estimation.md) — NormFlowSDE 从带噪测量和控制记录中抽取多条可能的状态轨迹。它用条件归一化流学习随机变化，用随机微分方程描述状态随时间怎样演化，训练后遇到新序列可直接采样。
- [HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots](items/HumanoidPose%20Monocular%203D%20Pose%20Estimation%20for%20Humanoid%20Robots.md) — HumanoidPose 从单目图像恢复人形机器人的三维全身姿态。它借用人体姿态估计的视觉思路，再用机器人的关节结构和运动学约束三维解。

## 其余存档 12 篇

- [RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics](items/RoboDyna%20A%20Benchmark%20for%20Evaluating%20Robotic%20Manipulation%20under%20Physically%20Ground.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [NavTTT: Adaptive Parametric Memory via Hierarchical Test-Time Training for Vision-and-Language Navigation](items/NavTTT%20Adaptive%20Parametric%20Memory%20via%20Hierarchical%20Test-Time%20Training%20for%20Vision.md) · 智能体 Agent 具身智能评测与基准
- [Embodied Interaction Policy: A Unified Model for Full-Duplex Human-Robot Interaction](items/Embodied%20Interaction%20Policy%20A%20Unified%20Model%20for%20Full-Duplex%20Human-Robot%20Interact.md) · 智能体 Agent 具身智能评测与基准
- [Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation](items/Beyond%20Future%20Views%20Exploring%20Future-State%20World%20Models%20for%20Vision-Language%20Navi.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [ManipScope: A Diagnostic Benchmark for Instruction Following and Generalization in Robotic Manipulation](items/ManipScope%20A%20Diagnostic%20Benchmark%20for%20Instruction%20Following%20and%20Generalization%20i.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [Opto-Electronic Hybrid Reinforcement Learning Based on MZI for Robotic Manipulator Control](items/Opto-Electronic%20Hybrid%20Reinforcement%20Learning%20Based%20on%20MZI%20for%20Robotic%20Manipulat.md) · 世界模型 机器人学习
- [PACE: Policy Augmentation and Compensation With Explicit Disturbance Estimation for Robust Locomotion](items/PACE%20Policy%20Augmentation%20and%20Compensation%20With%20Explicit%20Disturbance%20Estimation%20f.md) · 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [Ego4Gen: Generating Geometry-Grounded Motion Tokens as a World-Action Interface](items/Ego4Gen%20Generating%20Geometry-Grounded%20Motion%20Tokens%20as%20a%20World-Action%20Interface.md) · 世界模型 具身智能评测与基准
- [SCAP: Stochastic Context for Action Expert Pretraining](items/SCAP%20Stochastic%20Context%20for%20Action%20Expert%20Pretraining.md) · 多模态基础模型 视觉语言动作模型 VLA
- [SparseHPS: A Unified Model for Human Pose and Shape across Depth Cameras and LiDARs](items/SparseHPS%20A%20Unified%20Model%20for%20Human%20Pose%20and%20Shape%20across%20Depth%20Cameras%20and%20LiDA.md) · 具身智能评测与基准
- [Task2Hand: A Contact-Grounded Skill for Parametric Dexterous-Hand Morphology Design](items/Task2Hand%20A%20Contact-Grounded%20Skill%20for%20Parametric%20Dexterous-Hand%20Morphology%20Desi.md) · 智能体 Agent 世界模型
- [Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter](items/Humanoid%20robots%20for%20safety-critical%20electrical%20switching%20A%20perception-informed%20r.md) · 世界模型 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2511
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance
- 最高分论文发布时间：2026-11-20T06:12:51Z
- 主要技术对象分类：具身智能评测与基准 20、世界模型 15、智能体 Agent 10、机器人学习 10、多模态基础模型 9、视觉语言动作模型 VLA 8、Sim2Real 2
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
