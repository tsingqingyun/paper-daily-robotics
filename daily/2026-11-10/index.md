---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-10
---

# 2026-11-10 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人执行出错或换了任务之后，究竟该补什么信息，才能决定下一步动作。先读 MR0，理解如何把失败动作与人工纠正配成训练数据；再读 VICTR，理解为什么检索示范要对齐任务阶段；最后读 AMP1，检查通用模型直接控制机器人能做到什么，以及等待推理的代价。DobotTrack 适合进一步研究如何在有限视觉记忆里保住目标身份；BAIR at CoRL 是会议日程，不能作为方法论文解读。
> **趋势**：前五篇的共同线索：这些材料共同强调：动作预测之外，还要明确保留决定下一步所需的信息，包括纠错对照、目标身份、执行阶段和跨回合经验。不过，新增信息分别通过训练、推理上下文或外部记忆起作用，实验结论不能互相替代。

- **规模**：2542 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 21、多模态基础模型 15、智能体 Agent 15、视觉语言动作模型 VLA 14、世界模型 10、机器人学习 10、AI 核心知识地图 1、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [BAIR at CoRL 2026](items/BAIR%20at%20CoRL%202026.md)

> 《BAIR at CoRL 2026》是伯克利相关研究的会议日程，输入混入了网页样式和筛选脚本，并非一篇方法论文。它能帮助定位报告和候选论文，不能据此解释这些论文如何训练、如何控制机器人。

- **能借鉴什么**：可借鉴的是把它当作阅读索引：看到感兴趣的标题后，再取得对应摘要和实验设置。尤其不要从“世界模型”“触觉”“自学习”等标题词直接推断贡献；标题能说明作者关注什么，不能说明机制是否有效。
- **值得读吗**：值得快速浏览以选题和找报告，不值得按方法论文精读；下一步应转向具体论文材料。

<details><summary>实验依据</summary>

输入中的日程正文列出 33 篇主会论文、4 项 late-breaking results，以及 3 场 oral 和 7 场 spotlight，并注明主会与工作坊日期。这些是活动覆盖范围，不是模型实验结果。材料没有给出任何单篇研究的测试环境、对比算法、成功率或消融结果，因此无法据此判断 MEM、SuperMimic 等工作的实际效果。

</details>

### 2. [Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation](items/Meituan-Robotics-0%20A%20Vision-Language-Action%20Foundation%20Model%20for%20Desktop%20Manipul.md)

> Meituan-Robotics-0（MR0）让桌面机器人先从多来源数据学动作，再用真实执行中的纠错补上恢复能力。最值得注意的是 Rollback：保留机器人走错的一段，并从共同起点采集人工替代动作，让策略同时学“该怎么做”和“该避开什么”。

- **能借鉴什么**：纠错采集不必只留下“正确答案”：从相近起点保留错误与替代动作，可以直接形成有方向的监督。如果任务允许可靠回到历史状态，这比额外训练价值估计器更值得先尝试。
- **值得读吗**：值得重点读 Rollback 和 CFG-DAgger；它们给出了具体可复用的数据采集思路，比整体系统成绩更容易转化为实验。

<details><summary>实验依据</summary>

RoboTwin 2.0 仿真成功率为 93.6%，RoboDojo VLA 赛道排名第五；三项真机任务中，相同 HG-DAgger 后训练下，MR0 的平均成功率与进度分高于 π₀.₅。[S8](https://arxiv.org/html/2611.08577v1#S1.p5.1) 网线插入中，同一 Rollback 数据上，CFG-DAgger 优于 HG-DAgger 和 RECAP，达到 70% 成功率、0.90 进度分。[S8](https://arxiv.org/html/2611.08577v1#S1.p5.1) 节选未给试验次数、误差范围及对照具体数值；事件检索与任务恢复仅有定性展示。

</details>

### 3. [DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking](items/DobotTrack%20Target-Grounded%20Vision-Language-Action%20Learning%20for%20Embodied%20Person%20T.md)

> DobotTrack 让机器人按语言描述跟人，同时明确学习“目标是谁、在哪儿”。它的 Q-identity 用目标位置引导历史图像压缩，尽量保留能认出同一个人的外观与空间线索。

- **能借鉴什么**：当行动成败依赖某个特定目标时，压缩历史应由目标信息引导。这里值得借鉴的是先问“下一步必须记住谁的什么特征”，再决定保留哪些视觉信息，而非统一压缩整幅画面。
- **值得读吗**：值得精读目标监督与 Q-identity，并重点检查同预算消融；真机可靠性仍需看更完整的闭环结果。

<details><summary>实验依据</summary>

在仿真 EVT-Bench 的单目标、干扰与目标消歧三类任务上，0.8B 模型平均成功率 77.9%，比 OmTrackVLA 高 16.9 个百分点（摘要）。DT 消融中，仅轨迹监督为 55.9%，加框和掩码为 63.7%；但碰撞率最低的是仅加掩码，并非双监督。[S44](https://arxiv.org/html/2611.09041v1#S5.T2.2) 每帧历史 token 从 256 压到 16。[S42](https://arxiv.org/html/2611.09041v1#S5.SS1.p3.1) 真机数据有 126 段、596,323 张目标掩码，数据规模本身不证明真机闭环成功率。

</details>

### 4. [VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models](items/VICTR%20Value-Informed%20In-Context%20Learning%20for%20Vision-Language-Action%20Models.md)

> VICTR 让机器人从示范里找“现在这一步该参考哪一段”，而不只找画面最像的一段。IC-VFE 同时看参考示范、指令和当前观察，估计任务进度，再检索相应阶段的片段帮助 π₀.₅ 生成动作。

- **能借鉴什么**：检索的相似性应该服务于下一步决策：当任务包含状态转换时，“做到哪一步”可能比“长得多像”更有用。可以借鉴先学习阶段对齐，再让动作模型参考片段，而不是直接复制示范动作。
- **值得读吗**：值得读透进度估计与检索接口，但应先核对互相不一致的主结果数字，再判断提升幅度。

<details><summary>实验依据</summary>

测试使用固定配置的 YOR 双臂真机，含 8 个域内和 8 个域外任务，每任务 10 次运行。[S17](https://arxiv.org/html/2611.08698v1#S4.p2.1) [S18](https://arxiv.org/html/2611.08698v1#S4.p3.1) [S24](https://arxiv.org/html/2611.08698v1#S4.p8.1) 摘要报告域外成功率从微调 π₀.₅ 的 6.2% 到 23.8%，进度从 28.9% 到 55.5%。但 [S9](https://arxiv.org/html/2611.08698v1#S1.I1.i3) 另报成功率 2.7%／15.0%／25.0%，[S3](https://arxiv.org/html/2611.08698v1#S1.F1) 的进度数字也不同，节选未解释口径差异。这些结果支持该设置下进度检索有帮助，精确增益必须核对。

</details>

### 5. [On Agentic Manipulation Policies](items/On%20Agentic%20Manipulation%20Policies.md)

> AMP1 让通用 AI 模型直接看机器人画面、写代码并发出运动命令，执行一段后再观察和改策略。它不预置抓取、推放技能，而是把这些动作的组织交给模型；增加持久记忆后，还能复用此前尝试得到的经验。

- **能借鉴什么**：困难有时来自行动策略选错，而非动作预测不够精细。值得借鉴的是保留观察后改变策略的能力，并将已成功的程序存下来，减少每回合重新推导；适用前提是场景允许较慢的观察与决策循环。
- **值得读吗**：值得深入读控制接口、恢复协议和评测设置；结果有冲击力，但对动态操作和实时控制的结论必须收窄。

<details><summary>实验依据</summary>

RoboLab-120 仿真成功率为 85.6%，对照 VLA、WAM 为 49.2%、42.9%（摘要）。Franka 真机 12 项任务共 108 次，AMP1 成功 104 次，FLUX 和 π₀.₅ 分别成功 49、30 次。[S6](https://arxiv.org/html/2611.09892v1#S1.p4.1) [S11](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p1.1) 允许控制器报错恢复时为上述成绩，不提供恢复接口则降到 94 次。[S14](https://arxiv.org/html/2611.09892v1#S2.SS1.SSS2.p4.1) RoboDojo 仿真练习后从 26.4% 到 84.1%，但每任务练习五次并选最成功的一次评估。[S18](https://arxiv.org/html/2611.09892v1#S2.F4) 不能据此推断所有任务都稳定复现。

</details>

## 扫读 7 篇

- [Toward the Era of Agentic Embodied Intelligence](items/Toward%20the%20Era%20of%20Agentic%20Embodied%20Intelligence.md) — A2-MEAS 想让机器人失败后能根据现场情况改动作，而不只是重试。它把纠正建议、空间信息和执行历史组织成纠错代码，训练时写入策略，部署时用新代码引导冻结的策略。
- [Q-OIL: Optimistic Exploration in Learning from Human Interventions](items/Q-OIL%20Optimistic%20Exploration%20in%20Learning%20from%20Human%20Interventions.md) — Q-OIL 让机器人把人工接管当作值得探索的线索，同时允许人的动作不够好。它给接管相关转移增加乐观奖励，并用分开的价值评估器限制这些奖励向接管前状态传播。
- [ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use](items/ToolDex%20An%20Ego-Exo%20Human%20Demonstration%20Dataset%20for%20Creative%20Physical%20Tool%20Use.md) — ToolDex 记录人在没有标准工具时，如何挑选、改造和借用身边物体完成操作。它用同步第一视角和八台外部相机记录过程，并用这些数据评测工具推理、重建和机器人策略学习。
- [ODEAction: From Predicting Chunks to Evolving Actions](items/ODEAction%20From%20Predicting%20Chunks%20to%20Evolving%20Actions.md) — ODEAction 不再一次预测一段动作，而是学习当前动作接下来该怎样变化。执行时从当前动作出发积分这个变化规律，让后续动作显式接续前一个动作。
- [PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation](items/PRISM%20Primitive%20Routing%20via%20In-context%20Skill%20Mixing%20for%20Retentive%20VLA%20Adaptation.md) — PRISM 把已有技能分别保存在低秩适配器中，再按任务进度选择和混合它们。学习复合任务时冻结这些技能适配器，同时训练调用方式和其他组件，以减少旧技能被覆盖。
- [HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety](items/HomeLoop%20A%20Simulation%20Framework%20and%20Benchmark%20for%20Robot-IoT%20Coordination%20in%20Ever.md) — HomeLoop 让机器人面对“同一个警报、不同真实原因”的家庭场景，检验它能否结合现场观察和联网设备做出恰当处置。它既检查危险有没有解除，也检查过程中有没有贸然采取不该做的动作。
- [SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning](items/SURE%20Spatiotemporal%20Uncertainty%20Representation%20for%20Efficient%20Vision-Language-Act.md) — SURE 不再要求机器人逐时刻精确复刻一条示范，而是容纳邻近动作和局部快慢差异。它用概率动作解码器处理空间变化，再用 Soft-DTW 对齐动作片段，减少学习示范者个人动作习惯的负担。

## 其余存档 12 篇

- [ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective](items/ABHBench%20Evaluating%20Moral%20Decision-Making%20of%20Foundation%20Models%20from%20an%20Agentic%20P.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics](items/A%20Controlled%20Study%20of%20Models%2C%20Skills%2C%20Feedback%2C%20and%20Curriculum%20in%20Agentic%20Roboti.md) · 智能体 Agent 世界模型
- [ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models](items/ActPrune%20Action-Grounded%20Visual%20Token%20Pruning%20for%20Efficient%20Vision-Language-Acti.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning](items/DexDICE%20Reconciling%20Safety%20and%20Performance%20via%20Dual-Expert%20Offline%20Imitation%20Lea.md) · 智能体 Agent 机器人学习 具身智能评测与基准
- [HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes](items/HiMEM%20Hippocampus-Inspired%20Memory%20Consolidation%2C%20Pruning%2C%20and%20Composition%20for%20Vi.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [Localizing and Editing the Goal Representation of a Vision-Language-Action Model](items/Localizing%20and%20Editing%20the%20Goal%20Representation%20of%20a%20Vision-Language-Action%20Model.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation](items/Grasp-TAGS%20Task-Aware%20Grasp%20Selection%20via%20Critic%20Distillation%20for%20Prehensile%20Loc.md) · 世界模型 机器人学习 具身智能评测与基准
- [InstantHMR : Real-Time Human Mesh Recovery on Your Phone](items/InstantHMR%20Real-Time%20Human%20Mesh%20Recovery%20on%20Your%20Phone.md) · AI 核心知识地图
- [Augmentron: Scalable Multi-View Visual Augmentation for Robot Learning](items/Augmentron%20Scalable%20Multi-View%20Visual%20Augmentation%20for%20Robot%20Learning.md) · 机器人学习 具身智能评测与基准
- [VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models](items/VLA%20Handover%20Failure-Prediction-Based%20Switching%20from%20On-Robot%20to%20Server%20VLA%20Mode.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents](items/Flex-RSI%20Benchmarking%20Recursive%20Self-Improvement%20of%20Frontier%20Agents.md) · 智能体 Agent 具身智能评测与基准
- [Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning](items/Encoding%20Memory%20in%20World%20Models%20with%20Test-Time%20Model-Based%20Reinforcement%20Learnin.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2542
- 入选条目：24
- 回填已见条目：0
- 最高分论文：BAIR at CoRL 2026
- 最高分论文发布时间：Mon, 09 Nov 2026 01:00:00 -0800
- 主要技术对象分类：具身智能评测与基准 21、多模态基础模型 15、智能体 Agent 15、视觉语言动作模型 VLA 14、世界模型 10、机器人学习 10、AI 核心知识地图 1、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
