---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-05
---

# 2026-11-05 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：怎样让预训练机器人模型适应实际执行中的条件，而不只是把单次任务分数做高。想理解连续工作为何让训练失效，先读 CRONOS，重点看两种起始状态漂移及重置干预；想让大模型控制移动目标，读 ARP，重点看如何训练快控制器使用过期信息；想降低新任务的数据成本，读 A-0 与 RoboTryOn，比较统一夹爪接口和合成机器人示范各自需要什么条件。
> **趋势**：前五篇的共同线索：这些论文共同把注意力放在模型之间、数据与执行之间的接口：特征幅度、信息时延、动作坐标和连续任务状态都会影响学习。给定证据支持针对这些接口做具体改动，但各篇验证条件不同，不能据此认定存在一种通用解法。

- **规模**：2525 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 20、具身智能评测与基准 19、世界模型 15、视觉语言动作模型 VLA 15、机器人学习 10、智能体 Agent 9、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](items/CRONOS%20Benchmarking%20Non-Episodic%20Reinforcement%20Learning%20for%20Robotic%20Manipulation.md)

> CRONOS 研究机器人不再每做完一个任务就被人工摆回原样时，VLA 还能不能靠强化学习进步。关键发现是要分别处理机械臂起始姿态漂移和物体越弄越乱，并把有限重置用在训练早期或已经无法继续的场景上。

- **能借鉴什么**：减少人工干预时，应同时统计每次交互学到了多少、用了多少次重置。尤其值得借鉴的是区分“困难但还能恢复”和“已经无法完成”：后者继续采样，只会耗掉交互预算。
- **值得读吗**：值得读到重置策略及其成本比较：它把连续学习失败拆成了可干预的具体原因，但尚不能当作真机免维护训练方案。

<details><summary>实验依据</summary>

仿真含四场景、16 个抓放任务，以成功率衡量。重置间隔从 80 增至 320、2560 步，OpenVLA 从 65% 降至 37%、0%，SpatialVLA 从 65% 降至 25%、2% [S17](https://arxiv.org/html/2611.05080v1#S3.SS2.p1.1)。SpatialVLA 加 EER 分别提高 25、10 个百分点 [S27](https://arxiv.org/html/2611.05080v1#S4.SS1.p3.1)；CL 的域内/域外成功率为 40%/32%，对应基线为 14%/8% [S28](https://arxiv.org/html/2611.05080v1#S4.SS2.p3.1)；HSR 域内为 64%，无 HSR 为 14% [S32](https://arxiv.org/html/2611.05080v1#S4.SS3.p2.1)。这些是不同干预比较，不能相加。节选只定性报告连续任务与新布局收益，未给对应数值。

</details>

### 2. [Asynchronous Robot Policies](items/Asynchronous%20Robot%20Policies.md)

> ARP 让大模型慢慢理解任务，小模型持续看最新画面并控制机器人，两者不必互相等待。巧处是训练时就让快控制器练习使用过期语义，并处理动作算出来时机器人已经前进的问题。

- **能借鉴什么**：当任务含义变化慢、物体位置变化快时，两类信息无需同频更新。可借鉴的不只是拆进程，而是把部署中的信息年龄显式带进训练，否则旧语义可能让快循环做出错误反应。
- **值得读吗**：值得细读时序训练与消融：证据最有说服力的部分，是展示了为什么异步控制必须连同信息过期一起训练。

<details><summary>实验依据</summary>

LIBERO 中 ARP-1B 平均成功率 84.8%，复现的 π₀-1B 为 80.2%；但原始 π₀ 报告值为 94.2%，所以不能概括为全面领先 [S30](https://arxiv.org/html/2611.05155v1#S4.T1.6)。目标中途位移 5 cm 的仿真中，两者为 51.5% 与 9.5% [S26](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px2.p1.1) [S38](https://arxiv.org/html/2611.05155v1#S4.SS3.p1.1)。更关键的训练消融是：VLM 以 0.5 Hz 更新时，只用同步记忆训练为 2.0%，默认较宽过期范围训练为 81.8% [S44](https://arxiv.org/html/2611.05155v1#S4.T4.4.1)。真机覆盖三任务；20% 更短平均回合长度的具体陈述来自 RoboLab 仿真评估 [S28](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px4.p1.1) [S35](https://arxiv.org/html/2611.05155v1#S4.SS2.SSS0.Px2.p2.1)。

</details>

### 3. [Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy](items/Controlling%20Action-Head%20Co-Adaptation%20to%20VLM%20Representation%20Anisotropy.md)

> AdaIE 处理一个容易忽略的问题：动作头可能越来越依赖 VLM 中变化幅度大的特征，但这些特征未必最适合控制。它在训练中跟踪动作头对各通道的敏感程度，动态调整输入权重，减少依赖过度集中。

- **能借鉴什么**：预训练特征接上新预测头时，先检查下游究竟依赖哪些维度，可能比直接扩大骨干更划算。尤其当预训练目标与下游目标差异大时，特征变化大不能自动解释为更有用。
- **值得读吗**：值得读到敏感度定义、缩放公式和消融，适合作为低成本接口改动的候选，但不能把“均衡特征总是更好”当成结论。

<details><summary>实验依据</summary>

受控实验里，RoboCasa 的 Equalize、基线、强化原有敏感模式 Exploit 分别为 22.9%、19.4%、16.2%；深度和分类任务差异很小 [S20](https://arxiv.org/html/2611.04006v1#S2.T1.2)。正式 AdaIE 在 RoboCasa-GR1 的 24 任务上，2B 基线 42.36% 提至 47.64%；RoboTwin 为 66.92% 至 68.60% [S27](https://arxiv.org/html/2611.04006v1#S4.SS1.SSS1.Px1.p1.1) [S28](https://arxiv.org/html/2611.04006v1#S4.SS1.SSS1.Px1.p2.1) [S29](https://arxiv.org/html/2611.04006v1#S4.T2) [S30](https://arxiv.org/html/2611.04006v1#S4.T2.2) [S31](https://arxiv.org/html/2611.04006v1#S4.SS1.SSS1.Px2.p1.1) [S32](https://arxiv.org/html/2611.04006v1#S4.SS1.SSS1.Px2.p2.1) [S33](https://arxiv.org/html/2611.04006v1#S4.T3) [S34](https://arxiv.org/html/2611.04006v1#S4.T3.2)。真机五任务，每方法每任务20次，完整成功率从30%至49% [S39](https://arxiv.org/html/2611.04006v1#S4.SS1.SSS2.Px2.p1.1) [S40](https://arxiv.org/html/2611.04006v1#S4.T4) [S41](https://arxiv.org/html/2611.04006v1#S4.T4.2)。这些支持接口干预有效；世界模型扩展节选没有具体成绩。

</details>

### 4. [AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](items/AIRoA-0%20Long-Horizon%2C%20Precise%2C%20Cross-Embodiment%20Manipulation%20from%20Handheld%20Data.md)

> AIRoA-0（A-0）让人拿着带相机的夹爪示范，再把学到的策略装到使用同款夹爪的机器人上。它用夹爪相对动作统一接口，再结合视觉筛选、任务阶段预测和连续动作解码，处理只有腕部视角的长任务。

- **能借鉴什么**：跨机器人迁移可以先通过统一末端、相机和动作定义，减少数据本身对机身的依赖。长任务则值得显式表达“现在做到哪一步”，避免把所有进度判断都留给动作分布隐式解决。
- **值得读吗**：值得按数据接口、阶段建模、推理解码三层细读；它展示了完整手持学习路线，但不能简化成任意人类视频可直接驱动任意机器人。

<details><summary>实验依据</summary>

作者采集16,151小时手持数据 [S3](https://arxiv.org/html/2611.03815v1#S1.p1.1)。未见采集地点的 Franka 十任务评估，每任务15次，含部分完成计分，平均78%；四个同任务后训练的 VLA 为14%—27% [S10](https://arxiv.org/html/2611.03815v1#S2.SS1.p1.1) [S11](https://arxiv.org/html/2611.03815v1#S2.SS1.p2.1) [S12](https://arxiv.org/html/2611.03815v1#S2.T1)。同任务权重还在 TX-G2、OpenArm、UR 上展示部分任务，但节选未给各平台成功率 [S14](https://arxiv.org/html/2611.03815v1#S2.SS3.p1.1) [S15](https://arxiv.org/html/2611.03815v1#S2.SS3.p2.1)。数据扩展实验支持更多手持数据降低留出动作损失 [S30](https://arxiv.org/html/2611.03815v1#S4.SS6.p1.1) [S31](https://arxiv.org/html/2611.03815v1#S4.F9) [S32](https://arxiv.org/html/2611.03815v1#S4.F10) [S33](https://arxiv.org/html/2611.03815v1#S4.SS6.p2.1) [S34](https://arxiv.org/html/2611.03815v1#S4.SS6.p3.1)，不能直接换算成机器人成功率增幅。

</details>

### 5. [RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](items/RoboTryOn%20Synthesizing%20Dexterous%20Robot%20Demonstrations%20from%20Human%20Videos%20via%20Virt.md)

> RoboTryOn 先把人类操作视频转换成机器人执行同一动作的视频，再从生成视频估计动作标签来训练策略。它把外观转换和动作估计分开，避免直接把人手姿态硬映射成灵巧手机器人的关节命令。

- **能借鉴什么**：人类视频不必直接提供准确机器人动作，可以先转成目标机器人观测，再用学过机器人运动的模型补标签。值得尝试的条件是已有该机型基础录像，而新任务遥操作昂贵、又不依赖精细力控。
- **值得读吗**：值得细读动作标注与失败边界：真机结果支持它降低新任务示范门槛，但生成得像机器人并不保证动作标签足够精确。

<details><summary>实验依据</summary>

两台真机 OpenArm、RB-Y1 各测11任务，每任务28次；七个新任务各有50个人类视频、没有该任务机器人示范 [S26](https://arxiv.org/html/2611.05163v1#S4.SS1.p1.1) [S27](https://arxiv.org/html/2611.05163v1#S4.SS1.p2.1) [S28](https://arxiv.org/html/2611.05163v1#S4.SS1.p3.1) [S29](https://arxiv.org/html/2611.05163v1#S4.T1)。作者报告跨两机域外平均成功率从2.1%至60.0%，双臂任务45.9% [S8](https://arxiv.org/html/2611.05163v1#S1.p5.1)。EgoMimic、Masquerade 共享策略、遥操作数据和人类视频，以比较转换方式 [S27](https://arxiv.org/html/2611.05163v1#S4.SS1.p2.1)；但节选没给主表数值行，不能补出各基线成绩。约三分之一采集成本的比较见 [S8](https://arxiv.org/html/2611.05163v1#S1.p5.1)，具体成本构成尚需核查。

</details>

## 扫读 7 篇

- [DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](items/DiMuRe%20Diagnosis-Guided%20Multilevel%20Recovery%20for%20Robotic%20Task%20Execution.md) — DiMuRe 让机器人受干扰后先判断下一步动作的条件还在不在，再决定复用程序、调用恢复技能，或交给模型重新写纠错代码。巧处是把补救分层，让仍然有效的程序继续发挥作用。
- [Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy](items/Online%20Hamilton-Jacobi%20Reachability%20Onboard%20the%20Robot%20Control%20Loop%20A%20Real-Time%20G.md) — 这篇把 HJ 可达性计算搬进机器人控制循环：用 CUDA 加速经典数值求解器，及时算出哪些状态在最坏扰动下可能走向危险。关键贡献是把原本常离线计算的安全分析做到低维系统的实时速度。
- [Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training](items/Trusting%20Imagined%20Futures%20Auditing%20Imagined%20Rewards%20for%20VLA%20Post-Training.md) — TIF 在用世界模型辅助 VLA 后训练时，先审计“看起来高分”的候选是否可能被高估。只有预计收益足够大、风险也过关才替换原监督，避免机器人跟着漂亮但执行差的想象学。
- [GUILD: Guided Iterative Data Collection for Imitation Learning](items/GUILD%20Guided%20Iterative%20Data%20Collection%20for%20Imitation%20Learning.md) — GUILD 把机器人示教采集变成循环：先建议采什么，再估计新轨迹对目标部署表现有没有帮助，用结果调整下一轮。巧处是把数据筛选的判断前移，让反馈影响尚未花出去的采集预算。
- [Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots](items/Action%20Intent%20as%20a%20Bridge%20Transferring%20Manipulation%20Knowledge%20from%20Human-Centric.md) — AIT 想让机器人从现成的人类操作视频学习，先提取人和机器人都能共享的动作意图，再把意图转换成机器人动作。关键是减少场景杂讯混进动作表示，避免把背景差异也当成需要迁移的知识。
- [FlowBench: Counterfactual Imagination Training for Spatial Intelligence](items/FlowBench%20Counterfactual%20Imagination%20Training%20for%20Spatial%20Intelligence.md) — FlowBench 让模型回答“如果物体这样动，场景会变成什么样”，检验它能否在结果尚未出现时推断空间变化。关键是自动把假设运动与空间问题配对，并在仿真中提供准确的结果画面和光流，让同一批场景既能训练问答，也能训练运动预测。
- [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](items/PrimeSim%20A%20Generalist%20World%20Model%20Simulator%20from%20Large-Scale%20Cross-Embodiment%20De.md) — PrimeSim 要把视频生成器变成能接受机器人动作的模拟器：动作要执行对，多个相机要看到同一件事，连续推演也不能很快失真。它先用大量跨机器人示范建立动作与画面的对应，再通过因果生成、自生成历史训练和分层记忆维持长时间推演。

## 其余存档 12 篇

- [Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs](items/Say%20the%20Same%2C%20Act%20Differently%20Diagnosing%20and%20Steering%20Text-Action%20Divergence%20in.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](items/Aero-VPA%20Few-Step%20Flow-Matching%20Control%20over%20Non-Reconstructive%20JEPA%20Latents%20for.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [GSBR: Geometric Support Behavior Regularization for Online RL](items/GSBR%20Geometric%20Support%20Behavior%20Regularization%20for%20Online%20RL.md) · 机器人学习 具身智能评测与基准
- [Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs](items/Should%20the%20Action%20Expert%20Train%20the%20VLM%20Action-Token%20Supervision%20and%20Gradient%20Rou.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [All-For-One: Distilling Visual Foundation Models to a Fast, Memory-Efficient Visuomotor Policy](items/All-For-One%20Distilling%20Visual%20Foundation%20Models%20to%20a%20Fast%2C%20Memory-Efficient%20Visu.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs](items/Human-to-Robot%20Transfer%20via%20Bridging%20Representation%20and%20Action%20Space%20in%20VLAs.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习
- [PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](items/PolicyIK%20High-Precision%20Inverse%20Kinematics%20for%20Robot%20Arms%20with%20Reinforcement%20Lea.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- [Low-Density 3D Point Cloud Classification](items/Low-Density%203D%20Point%20Cloud%20Classification.md) · 具身智能评测与基准
- [LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](items/LLMs%20as%20MDP%20Designers%20A%20Dependency-Aware%20Agentic%20Framework%20for%20Automated%20Robot%20P.md) · 智能体 Agent 机器人学习 具身智能评测与基准
- [Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture](items/Caging%20Vision-Language%20Navigation%20for%20Legged%20Robots%20via%20Barrier-Certified%20Safety.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation](items/Physical%20Diffusion%20Policy%20via%20MPM-Guided%203D%20Gaussian%20Simulation.md) · 多模态基础模型 世界模型 机器人学习
- [DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?](items/DualWorldBench%20Can%20Agents%20Plan%20Deliveries%20across%20Symbolic%20and%20Grounded%20Worlds.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2525
- 入选条目：24
- 回填已见条目：0
- 最高分论文：CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation
- 最高分论文发布时间：2026-11-03T15:41:07Z
- 主要技术对象分类：多模态基础模型 20、具身智能评测与基准 19、世界模型 15、视觉语言动作模型 VLA 15、机器人学习 10、智能体 Agent 9、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
