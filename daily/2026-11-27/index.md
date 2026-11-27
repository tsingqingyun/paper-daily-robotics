---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-27
---

# 2026-11-27 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看一个部署问题：机器人遇到训练时没覆盖的变化，究竟需要换目标、补观测，还是重做控制接口？先读 DTU-Bench 的同状态对照，学会识别机器人是否真的响应了新指令。再读 X-Harness 的调用时机实验，看看哪些反馈可以交给本地代码，哪些失败值得请视觉语言模型介入。关心接触控制的话，读《Can Visual World Models See Force?》的力幅值结果，先判断视觉特征能提供什么信号。
> **趋势**：前五篇的共同线索：几篇论文都把部署能力拆成可单独检验的问题：能完成固定任务、能中途换目标、能察觉接触、能估准力、能换机身执行，各需要自己的对照和指标。相应的设计也开始明确机器人在执行时需要读到什么，包括当前目标、历史观测、接触反馈和机身几何。

- **规模**：1188 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、多模态基础模型 16、视觉语言动作模型 VLA 15、世界模型 12、机器人学习 9、智能体 Agent 7
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents](items/Toward%20Agentic%20Robotics%20A%20Large-Scale%20Study%20of%20Harness%20Design%20for%20Robot-Use%20Agen.md)

> X-Harness 让视觉语言模型写会看反馈的控制代码，把精细动作交给动作策略或几何工具。机器人平时按代码运行，遇到指定的失败信号才请视觉语言模型帮忙恢复。

- **能借鉴什么**：常规反馈处理可以写成可即时执行的分支。比如夹爪空了就重试，连续重试仍失败才重新分析场景。只要传感器能可靠判定这些状态，就可以分别衡量本地重试能处理多少失败，以及额外推理能挽回多少。
- **值得读吗**：先读 §3.1 和 §4.3，再读多轮救援结果 [S47]，重点看闭环代码能处理到哪一步，以及何时值得把控制交回 VLM。

<details><summary>实验依据</summary>

八项仿真基准共记录 489,380 次执行，主要指标是留出回合成功率，动作策略单独运行时在相同回合只接收指令 [S4](https://arxiv.org/html/2611.34778v1#S1.p3.1)[S17](https://arxiv.org/html/2611.34778v1#S3.SS2.p4.1)。摘要报告相对基础策略最高提高 42.8 个百分点。在 RoboCasa365 的 Awomo-0.5I 设置，触发式多轮救援成功率为 77.3%，逐子目标调用为 76.8%，前者每回合少用 42% 的 VLM token [S47](https://arxiv.org/html/2611.34778v1#A7.p12.1)。这组数字给出了该配置的成本与成功率。作者另报告双臂真机验证，节选未给出其任务数与逐项结果 [S34](https://arxiv.org/html/2611.34778v1#S7.p2.1)。

</details>

### 2. [M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation](items/M%24%20%7B2%7D%24AdaptVLA%20Multimodal%20Memory-Augmented%20Vision-Language-Action%20Model%20with%20Pr.md)

> M2AdaptVLA 同时记住机器人看到了什么、接触时受了什么力，并按任务阶段决定多依赖哪种信息。部署时，它用预测接触力与实测值的误差微调动作策略。

- **能借鉴什么**：实测接触信号既能告诉策略刚刚发生了什么，也能在动作执行后检验它原先的预测。能把预测和传感器读数按时间对齐时，机器人便可以在没有新增人工示范的情况下获得更新信号。
- **值得读吗**：值得读到 §3.3 和部署时序 [S42]，因为能否复用这套方法，取决于预测、执行与测量是否能对上。

<details><summary>实验依据</summary>

八项真机任务按所有阶段均完成计成功，平均成功率 82.71%，最强整体基线 π-Mem 为 51.25% [S27](https://arxiv.org/html/2611.34560v1#S4.T1.6) [S28](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px5.p1.1)。同骨干的初始抽屉回忆任务中，带快权重的缓存为 90%，独立帧缓存为 70%，只用快权重为 75% [S23](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p2.1)[S36](https://arxiv.org/html/2611.34560v1#S4.T3.6) [S37](https://arxiv.org/html/2611.34560v1#S4.SS3.SSS0.Px1.p3.1)。同一擦板策略在两种板面位置变化下，开启适配使平均成功率从 85.0% 升到 97.5%，RTX 5090 上每次更新平均 159.5 毫秒 [S5](https://arxiv.org/html/2611.34560v1#S1.p5.1)[S25](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p4.1)。后一个对照直接检验这两种变化下的更新效果。

</details>

### 3. [HoloBrain-0.5 Technical Report](items/HoloBrain-0.5%20Technical%20Report.md)

> HoloBrain-0.5 先统一各机器人关节和工具坐标的写法，再让策略看着机身结构和标定相机生成动作。离散版在预训练仿真中学得更快，连续版在报告的真机后训练设置中表现更好。

- **能借鉴什么**：跨机器人学习时，坐标转换可以先在数据管线中验证。关节和工具坐标的含义一致后，才容易检查共享策略究竟学会了可复用的动作规律，还是在适应各数据源的表达习惯。
- **值得读吗**：先读 URDF 变换和真机评分协议，再看两种动作头的学习曲线；这三处决定了报告里的迁移成绩能怎么解读。

<details><summary>实验依据</summary>

六个闭环仿真设置的平均成功率，离散版为 56.77%，连续版为 49.71% [S25](https://arxiv.org/html/2611.34449v1#S4.SS1.p1.1) [S26](https://arxiv.org/html/2611.34449v1#S4.F11) [S27](https://arxiv.org/html/2611.34449v1#S4.SS1.p2.1)。真机按里程碑给进度分，七项任务直接运行的离散版平均为 87.76%，后训练后的连续版为 94.52%，对照 π₀.₅ 为 86.25% [S30](https://arxiv.org/html/2611.34449v1#S4.T2) [S31](https://arxiv.org/html/2611.34449v1#S4.T2.5.1) [S32](https://arxiv.org/html/2611.34449v1#S4.SS2.p1.1) [S33](https://arxiv.org/html/2611.34449v1#S4.SS2.p2.1)[S39](https://arxiv.org/html/2611.34449v1#A2.T9.5)。双臂十一项任务中，后训练的 D-Init. 为 79.07%，π₀.₅ 为 69.41% [S35](https://arxiv.org/html/2611.34449v1#S4.SS2.p4.1) [S36](https://arxiv.org/html/2611.34449v1#S4.T3) [S37](https://arxiv.org/html/2611.34449v1#S4.T3.5.1)。Piper 到 Piper-X 的五项迁移平均为 63.28%，条件是 Piper-X 上没有这些任务的示范。未纳入预训练的 G1 则用过目标机示范 [S3](https://arxiv.org/html/2611.34449v1#abstract1.2)[S9](https://arxiv.org/html/2611.34449v1#S1.p5.1)[S24](https://arxiv.org/html/2611.34449v1#S4.p1.1)。

</details>

### 4. [Can Visual World Models See Force?](items/Can%20Visual%20World%20Models%20See%20Force.md)

> 《Can Visual World Models See Force?》用一个小读出器检查冻结模型的视觉特征能透露多少接触力。受测模型大多能看出何时接触，但要从特征里读出实际用了多大的力，仍然很难。

- **能借鉴什么**：评估视觉力反馈时，接触报警、变化跟踪和定量估力应分别验收。一个信号可以在碰到目标时提醒机器人切换控制阶段，却仍不足以判断压力是否超过任务允许的范围。
- **值得读吗**：值得细读探针协议和力监督迁移实验，尤其要对着看相关系数与接触 R²，避免把曲线同步当成定量估力。

<details><summary>实验依据</summary>

Hoi! 是人持测力夹爪操作门和抽屉的数据，RH20T 提供机器人操作记录 [S6](https://arxiv.org/html/2611.34422v1#S1.p4.1)[S20](https://arxiv.org/html/2611.34422v1#S4.SS1.SSS0.Px1.p1.1)。Hoi! 夹爪视角中，DreamZero 相对基础模型 Wan 的力跟踪相关系数为 0.46 对 0.35，换到 RH20T 为 0.15 对 0.18。四组基础与机器人后训练模型的对照整体未显示稳定改善 [S21](https://arxiv.org/html/2611.34422v1#S4.SS3.SSS0.Px3.p1.1)。Hoi! 夹爪视角的冻结 V-JEPA 2.1 接触 R² 为 0.166，事后用评估数据做仿射校准也只有 0.190 [S25](https://arxiv.org/html/2611.34422v1#S10.T14.6)。力监督后，把 RH20T 读出器原样搬到 Hoi!，相关系数由 0.03 升到 0.21，接触 R² 仍明显为负 [S22](https://arxiv.org/html/2611.34422v1#S4.SS5.p1.1)。

</details>

### 5. [Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation](items/Dynamic%20Task%20Update%20Benchmark%20%28DTU-Bench%29%20Evaluating%20Runtime%20Task%20Adaptation%20in.md)

> DTU-Bench 在机器人做到一半时换指令，保留当时的抓握和物体位置，检验策略能不能从那里改做新任务。它也检查机器人是否先完成了旧任务，以及新目标能否保持住。

- **能借鉴什么**：能恢复同一执行状态时，可以把“只改指令”的分支用作行为对照。把它与旧目标完成顺序和新目标保持时间一起看，才有依据区分及时改道、先做完旧任务再改道，以及偶然经过新目标。
- **值得读吗**：值得读到同状态续跑和时间顺序分析 [S27][S40–S41]，这两处最能说明常规任务成功率漏掉了什么。

<details><summary>实验依据</summary>

LIBERO 仿真包含 40 个修订情境、七类改动和三个切换阶段。13 个配置在对象类原任务的平均成功率为 95.8%，中途换对象后为 1.6% [S1](https://arxiv.org/html/2611.34538v1#abstract1.1)。这两个数字对应不同目标。同一新目标的对照中，OpenVLA-OFT 在复合目标改动的 Held-10 从头与中途差距为 96.7 个百分点 [S35](https://arxiv.org/html/2611.34538v1#S5.SS2.p1.1)。另有 94 对同状态诊断，37 对无论给哪条指令都曾维持新目标十次观测，三对只在给新指令时做到 [S40](https://arxiv.org/html/2611.34538v1#S5.SS4.p2.1)。换对象的脚本诊断中，松手后撤让 π₀.₅ 从 2% 升到 38%，DM0.5 从 8% 升到 48% [S1](https://arxiv.org/html/2611.34538v1#abstract1.1)[S28](https://arxiv.org/html/2611.34538v1#S4.SS2.p7.1)。

</details>

## 扫读 7 篇

- [SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator](items/SOLVE%20Sparse%2C%20Ordered%20Keyposes%20Make%20LLM%20Agents%20Versatile%20and%20Efficient%20Robot%20Man.md) — SOLVE 让多模态大模型一次写出一串有序的机械臂末端关键位姿，中间动作交给运动规划器补齐。走远路时可以少写几个点，到了需要精确对齐的地方再加密，执行一段后重新观察。
- [ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking](items/ELMO%20Emergent%20Representations%20In%20Imitation%20Learning%20Via%20Dynamic%20Hierarchical%20Act.md) — ELMO 让机器人先预测一整个操作阶段的潜在动作码，再让解码器看着当前场景把代码变成实际动作。同一个码因此有机会表达“抓起积木”这类意图，具体怎么伸手由眼前的摆放决定。
- [Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs](items/Cairn%20Object-Centric%203D%20Trajectory%20Priors%20for%20Steering%20Frozen%20VLAs.md) — Cairn 在推理时给冻结的视觉语言动作模型加一条物体三维路线，让它知道夹着的东西该怎么绕障、转向和放下。原策略的动作意图先帮忙选路和改路，选好的路线再引导它生成动作。
- [RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](items/RoboEvo%24%202%24%20Recursive%20Robot%20Self-Improvement%20via%20Harness-Policy%20Co-Evolution.md) — RoboEvo² 让机器人控制策略暴露失败，再让能写代码的智能体尝试并验证修法。成功修法一部分留给智能体复用，一部分变成训练数据，让策略下次有机会直接完成操作。
- [Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics](items/Motion%20Beyond%20Pixels%20Learning%20Future%20Visual%20Representations%20for%20Object-Centric%20D.md) — MotionRep 一起预测未来的视觉特征和物体表面点的三维运动。生成时先让视觉特征走在前面，再用逐渐清楚的视觉信息帮助确定物体各点怎么动。
- [One Patch, Many Policies: Object-Associated Physical Patch Attacks on Robotic Manipulation](items/One%20Patch%2C%20Many%20Policies%20Object-Associated%20Physical%20Patch%20Attacks%20on%20Robotic%20Man.md) — OAPA 研究机器人视觉策略对实体贴片干扰的脆弱性。摘要报告，同一贴片在不同任务物体上的关联位置，会影响哪项操作受到干扰，且这种现象能跨策略出现。
- [One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics](items/One%20Ocean%2C%20Many%20Tasks%20A%20Data-Grounded%20Simulation%20Suite%20and%20Benchmark%20for%20Marine.md) — OneOcean 把海底地形、随时空变化的洋流和潮汐放进同一个海洋模拟环境，让导航、巡检、清污等任务可以在统一的海况表示下评测。它还统一记录运行条件和指标，方便比较规划与控制方法。

## 其余存档 12 篇

- [Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution](items/Nav4Manip%20From%20Navigation%20to%20Dexterous%20Mobile%20Manipulation%20through%20Co-Evolution.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies](items/Keep%20or%20Roll%20Back%20Out-of-Loop%20Judges%20for%20Self-Improving%20VLA%20and%20End-to-End%20Embod.md) · 视觉语言动作模型 VLA 具身智能评测与基准
- [ScanAR: Parallel Row-Scan Decoding for Efficient Image Generation in Unified Autoregressive Models](items/ScanAR%20Parallel%20Row-Scan%20Decoding%20for%20Efficient%20Image%20Generation%20in%20Unified%20Auto.md) · 多模态基础模型
- [Event-WAM: Learning to Act with Event-Derived Futures](items/Event-WAM%20Learning%20to%20Act%20with%20Event-Derived%20Futures.md) · 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](items/FineDex%20Bridging%20Fine-Grained%20Human-Object%20Interaction%20Generation%20to%20Dexterous%20H.md) · 智能体 Agent 世界模型 机器人学习
- [Most of the Way There: Turning a Strong Video Prior into an Action-Conditioned World Model](items/Most%20of%20the%20Way%20There%20Turning%20a%20Strong%20Video%20Prior%20into%20an%20Action-Conditioned%20Wo.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [Escapingthe instruction blackhole of vision-language-action policies via optimal-transport wormholes](items/Escapingthe%20instruction%20blackhole%20of%20vision-language-action%20policies%20via%20optimal.md) · 多模态基础模型 视觉语言动作模型 VLA
- [DriftWAM: Faster World-Action Models via Action-Aware Video Drifting](items/DriftWAM%20Faster%20World-Action%20Models%20via%20Action-Aware%20Video%20Drifting.md) · 视觉语言动作模型 VLA 具身智能评测与基准
- [Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform](items/Triage%20Before%20Fine-Tuning%20Feasibility-Gated%20Selection%20and%20Monitored%20Adaptation%20o.md) · 多模态基础模型 具身智能评测与基准
- [A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models](items/A%20Failure-Driven%20Data%20Flywheel%20for%20Post-Training%20Vision-Language-Action%20Models.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Do We Still Need Reinforcement Learning When We Can Read the World Model?](items/Do%20We%20Still%20Need%20Reinforcement%20Learning%20When%20We%20Can%20Read%20the%20World%20Model.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions](items/LUDIUS%20A%20Benchmark%20for%20Embodied%20Social%20Intelligence%20in%20Everyday%20Human-Robot%20Inte.md) · 多模态基础模型 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：1188
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents
- 最高分论文发布时间：2026-11-25T17:39:10Z
- 主要技术对象分类：具身智能评测与基准 18、多模态基础模型 16、视觉语言动作模型 VLA 15、世界模型 12、机器人学习 9、智能体 Agent 7
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- OpenAI News: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
