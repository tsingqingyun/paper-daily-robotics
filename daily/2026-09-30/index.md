---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-09-30
---

# 2026-09-30 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天我会先看 RawVLA 和 RoboSkill：前者提醒你，机器人表现差，问题可能出在相机把什么信息丢掉了；后者解决每次遇到相似任务都从头摸索的浪费。如果关心世界模型，再看 WorldLine，重点不是视频像不像，而是预测有没有帮机器人选对动作。另有一篇基准审计值得优先扫读：部分方法排名会因评测 bug 修复而反转。
> **趋势**：这些论文给我的共同启发是：先找失败具体发生在哪一步，再决定要不要换更大的模型。输入、记忆、执行反馈和评测规则，都可能是更直接的改进入口。

- **规模**：2377 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 21、具身智能评测与基准 20、视觉语言动作模型 VLA 13、智能体 Agent 12、世界模型 11、机器人学习 9、Sim2Real 4
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations](items/AeroManip-VLA%20Scalable%20Vision-Language-Action%20Learning%20for%20Aerial%20Manipulation%20w.md)

> AeroManip-VLA 给空中机械臂建了一套训练场：让机器人在仿真中自动演示抓取和搬运，批量产出示范，并记录每次卡在哪一步。贡献主要在数据生产和故障分析，目前只在仿真里验证，还没证明能搬到真机上用。

- **能借鉴什么**：如果要扩充机器人训练数据，可以借鉴它的做法：把已经会的基础技能放进不同场景反复执行，同时记录抓取、运输等各阶段的成败。这样既能增加数据，也能看出该补哪类示范，而不是只盯着最终成功率。
- **值得读吗**：做空中操作，重点看自动示范和负载控制；做其他机器人，轨迹分阶段诊断更值得借鉴。真机能否受益还要等验证。

<details><summary>实验依据</summary>

数据超过 8 万条，覆盖基础技能及导航与操作结合的长任务，但评测目前都在仿真中。[S30](https://arxiv.org/html/2609.36915v1#S5.p1.1) 在 Pick 上，BC 用约 6.7万—8.1万个示范状态转移就接近专家成功率；PPO 需要数百万次环境交互，测试成功率仍低于专家。因此“训练更省”不是 PPO 的优势。[S23](https://arxiv.org/html/2609.36915v1#S4.SS1.p1.1) 它的优势是成功走法更多样、执行更快：TidyHouse 中成功轨迹平均耗时从专家/BC 的 15.8 秒降到 3.8 秒；PrepareGroceries 从约 14.7 秒降到 4.0 秒。[S26](https://arxiv.org/html/2609.36915v1#S4.SS1.p4.1)[S27](https://arxiv.org/html/2609.36915v1#S4.SS1.p5.1) 这些耗时只算成功回合，不能直接说整体采集吞吐提高同样倍数。[S27](https://arxiv.org/html/2609.36915v1#S4.SS1.p5.1) 下游测了 ACT、Diffusion Policy、π0、π0.5；已核对的正文未包含完整成绩表，无法据此比较所有模型的整体排名。[S29](https://arxiv.org/html/2609.36915v1#S4.SS2.p1.1)

</details>

### 2. [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](items/Explore%2C%20Execute%2C%20Evolve%20A%20Skill%20Acquisition%20and%20Reuse%20Loop%20for%20Embodied%20Agents.md)

> RoboSkill 让机器人把一次试错留下的经验写成说明和可复用代码，下次遇到类似任务先查着用，省掉重复思考与摸索。它还用触觉确认有没有碰到、抓住物体，再根据执行结果修订技能库。

- **能借鉴什么**：一个值得试的方向是：在现有智能体上保存可执行的经验，让成功做过的步骤下次直接复用。判断它是否划算时，要把最初建库、失败重试和维护错误经验的成本一起算进去；论文的真机省时数字只统计了成功试验。
- **值得读吗**：如果机器人总在重复任务上从头探索，这篇很对症；先看技能怎样保存、纠错，以及积累多久才省回建库成本。

<details><summary>实验依据</summary>

LIBERO-10 主实验有 10 个任务，每个任务 4 个评测种子，共 40 组；建库种子被排除在这次评测之外。[S14](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px1.p1.1)[S34](https://arxiv.org/html/2609.37810v1#S6.SS1.p1.1) 四种智能体的首次回合成功率都提高。例如 Astra 从 72.5% 到 97.5%；Sol 从 27.5% 到 52.5%，平均耗时从 94.5 分钟到 35.9 分钟。比较对象是不保存技能的同类智能体。[S16](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px3.p1.1)[S18](https://arxiv.org/html/2609.37810v1#S4.T1.6) 真机用 Piper 机械臂做 12 个任务，每任务 10 次：Astra 在简单任务中从 91.7% 到 100%，困难任务从 80% 到 88.3%；成功试验平均耗时分别从 20.3 到 16.6 分钟、27.0 到 23.1 分钟。[S15](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px2.p1.1)[S20](https://arxiv.org/html/2609.37810v1#S4.T2.fig1.7)[S24](https://arxiv.org/html/2609.37810v1#S4.SS2.p4.1) 这说明复用经验能减少重复摸索，但不是每项任务都改善：针孔抽线任务从 7/10 降到 5/10。[S46](https://arxiv.org/html/2609.37810v1#S7.T13.7)

</details>

### 3. [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](items/MotorMind%20Scaffolding%20General%20Vision%20Language%20Models%20for%20Zero-Shot%20Robot%20Manipul.md)

> MotorMind 把通用视觉语言模型接上机械臂：模型看图决定下一小步怎么移动、何时开合夹爪，控制器负责执行，系统再检查做成没有并决定是否重来。它不训练任务专用动作模型，主要改进在于把观察、行动和纠错组织成一个能反复运行的过程。

- **能借鉴什么**：做机器人智能体时，可以先拆开检查三个环节：命令是否足够具体，执行后是否确认结果，环境变化后是否及时改计划。这样能把问题定位到规划、控制接口或失败恢复，知道下一步到底该改哪一层。
- **值得读吗**：想知道通用大模型离直接控制机器人还有多远，优先读这篇；重点看动作接口和失败恢复，真机成绩仍只代表其测试任务。

<details><summary>实验依据</summary>

LIBERO-PRO 仿真中，基础任务成功率为 66.7%，扰动任务为 53.8%；所比较零样本基线最好分别为 13.3% 和 19.2%。MotorMind 对应平均任务耗时为 223.4 秒和 248.5 秒，仍有明显的执行等待成本。[S24](https://arxiv.org/html/2609.38078v1#S4.T4.2.1) 换用更强但经 API 调用、更慢的 VLM，基础成功率升至 83.3%。[S6](https://arxiv.org/html/2609.38078v1#S1.p4.1) xArm6 真机的直接操作与人为扰动设置平均成功率为 95%，无需任务专用示范或微调；已核对的正文未提供各任务试验次数，不能据此推断复杂长任务也有同样水平。[S2](https://arxiv.org/html/2609.38078v1#Sx1.p1.1) [S28](https://arxiv.org/html/2609.38078v1#S5.p1.1) [S29](https://arxiv.org/html/2609.38078v1#S5.T7)

</details>

### 4. [RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation](items/RawVLA%20Embodied%20Neural%20Image%20Signal%20Processor%20For%20Robotic%20Manipulation.md)

> RawVLA 把“怎么把相机原始信号变成图片”也纳入训练，让画面处理服务于机器人做对动作，原有动作模型保持冻结。真机实验显示，在低光下调整这层处理，就能明显改善同一个动作策略的表现。

- **能借鉴什么**：机器人一换光照就失灵时，先检查相机输出丢了什么信息，再决定是否重训动作模型。一个直接可做的对照是固定策略和任务，只换图像处理；这能把感知输入的问题与策略本身的问题分开。
- **值得读吗**：已有机器人在暗光下表现差，值得优先读。先确认能否拿到相机 RAW 数据；论文需要为每个动作策略单独训练图像处理模块。

<details><summary>实验依据</summary>

最直观的证据来自四项真机双臂任务，动作底座是已经微调的 π₀.₅。正常光照下，RawVLA、默认图像处理和 DarkISP 的平均成功率分别为 75.0%、76.5%、50.0%；低光下分别为 66.5%、0%、11.0%。这说明在这些任务上，改图像处理能恢复暗光下的操作能力，同时大体保持正常光下的表现。[S24](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px6.p1.1) 仿真还覆盖 LIBERO 与 RoboTwin 2.0；LIBERO 的跨底座平均成功率从最强对照的 43.01% 提到 68.82%。[S20](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px4.p1.1) 论文报告的 168 FPS 仅是图像处理模块速度，不能当作整个机器人策略的控制频率。[S24](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px6.p1.1)

</details>

### 5. [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](items/Counterfactual%20Video%20Generation%20Enables%20Scalable%20Humanoid%20Loco-Manipulation.md)

> PRISM 把少量真人搬运视频生成不同物体的版本，再按手和物体的接触关系修正动作，拿去训练人形机器人。它证明生成视频可以帮助扩充搬运训练数据，最终在真机上搬起并运输了未见过的物体，但仍由人用摇杆给方向和放下指令。

- **能借鉴什么**：想用生成视频补机器人数据，关键要检查手接触哪里、物体怎样跟着动，不能只看视频是否逼真。这篇把接触约束一路用于重建、动作转换和训练，提供了一个把“看着合理”变成“可以学着做”的具体办法。
- **值得读吗**：缺搬运数据时值得读，重点看接触约束如何修正生成错误。其效果依赖较清楚的种子视频，对柔性物体仍有明显限制。

<details><summary>实验依据</summary>

数据扩充有一个需要看清的漏斗：4 条真实视频生成了 256 条视频，但最后得到的是 137 条可行轨迹和 129 条成功教师执行，不是所有生成视频都能直接变成训练数据。[S41](https://arxiv.org/html/2609.38172v1#S7.p3.1) 真机用 Unitree G1，每个物体试 5 次，抓起并稳定搬运至少 3 米才算成功；箱子是 15/15，球是 12/15，未见类别的物体也有成功记录。[S30](https://arxiv.org/html/2609.38172v1#S5.SS2.p1.1)[S34](https://arxiv.org/html/2609.38172v1#S5.T2.4.1) 仿真消融中，逐步加入接触相关修正后，域内成功率从 22.50% 到 96.25%，域外从 12.50% 到 72.92%。这些数据支持接触处理对这套系统有用；不能把仿真数字当作真机成绩。[S36](https://arxiv.org/html/2609.38172v1#S5.T3.4.1)

</details>

## 扫读 7 篇

- [Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control](items/Urgent%20Actions%20Go%20First%20Urgency-Aware%20Denoising%20for%20Real-Time%20VLA%20Control.md) — UAD 抓住一个简单事实：机器人现在只急着用第一步动作，后面的动作可以晚一点算完。它先交付近期动作，边执行边细化后续动作，再补偿提前交付造成的误差；摘要报告这能缩短动作等待时间，并保持相当的任务成功率。
- [EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation](items/EgoHumanoid-V2%20Human-to-Humanoid%20Transfer%20of%20Coordinated%20Whole-Body%20Skills%20for%20L.md) — EgoHumanoid-V2 尝试用人的第一视角示范教机器人边走边操作：先把人的动作修正到机器人身体能做到，再处理人手与机器手在画面中的差别。四项真机任务中，这种人类数据训练出的策略，任务得分可与遥操作数据训练的策略相当。
- [Real2Gym: Building Gyms from Videos, Bringing Skills to Robots](items/Real2Gym%20Building%20Gyms%20from%20Videos%2C%20Bringing%20Skills%20to%20Robots.md) — Real2Gym 先照示范视频搭一个能实际执行动作的仿真练习场，让智能体在里面试错，把成功步骤和失败后的补救办法存下来，再带到真机使用。它积累的是可复用流程和操作代码，底层大模型权重不变。
- [Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies](items/Remember%20What%20You%20Did%20Action-History%20Memory%20with%20Dual-Expert%20Denoising%20for%20Long-.md) — ActMem-VLA 给已有机器人模型加上动作记忆，解决“眼前画面差不多，但任务其实已经走到另一阶段”的混淆。记忆模块先决定下一步往哪个阶段推进，原模型再细化动作；LIBERO-Mem 的平均成功率从 65.2% 提到 80.8%，原模型无需重新训练。
- [CrossBFM: Distilling a Shared Latent Behavior Space Across Humanoid Embodiments](items/CrossBFM%20Distilling%20a%20Shared%20Latent%20Behavior%20Space%20Across%20Humanoid%20Embodiments.md) — CrossBFM 让不同人形机器人共用一套“动作词汇”：用同一个向量表达要模仿的动作或到达的姿态，再由控制器落实成各自的关节运动。它用动作重定向建立身体之间的对应关系，减少为每种机器人从头学习独立行为空间的成本。
- [Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of Vision-Language-Action Acceleration](items/Faster%20and%20Better%20Benchmark%20Bugs%20and%20Design%20Limitations%20Distort%20the%20Evaluation%20o.md) — VLA 算得更快之后，成功率反而涨了，原因可能是评测把没做成的动作也算成了成功。这篇论文把物体实际轨迹和成功判定对照检查，在七个仿真基准里找到 22 个 bug；部分任务修好后，方法排名直接反转。
- [When to Adapt: Multi-Signal Domain Shift Detection for Efficient Training-Free Adaptation in Open-Vocabulary Segmentation](items/When%20to%20Adapt%20Multi-Signal%20Domain%20Shift%20Detection%20for%20Efficient%20Training-Free%20Ad.md) — 机器人连续看视频，环境没怎么变，却每帧都调整一次感知模型，很多计算可能白花了。《When to Adapt》同时观察画面、当前适配状态和语义的变化，检测到需要调整时才更新模型。

## 其余存档 12 篇

- [VLALight: A Vision-Language-Action Model for Traffic Signal Control](items/VLALight%20A%20Vision-Language-Action%20Model%20for%20Traffic%20Signal%20Control.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- [DROM: A Language-Guided Diffusion Framework for Multi-Skill Robotic Manipulation](items/DROM%20A%20Language-Guided%20Diffusion%20Framework%20for%20Multi-Skill%20Robotic%20Manipulation.md) · 智能体 Agent 世界模型 机器人学习
- [RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts](items/RoXDrive%20Closed-Loop%20Reinforcement%20Learning%20for%20End-to-End%20Autonomous%20Driving%20vi.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception](items/UniAfford%20Token-Routed%20Multitask%20Learning%20for%20Generalizable%202D-3D%20Affordance%20Per.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead](items/Disentangling%20Spurious%20Correlations%20in%20Vision-Language-Action%20Models%20via%20Predict.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference](items/Beyond%20Token%20Importance%20Preserving%20Spatial%20Scaffolds%20for%20Efficient%20Vision-Langua.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding](items/Exemplar2VQA%20A%20Scalable%20Exemplar-Driven%20Visual%20Question%20Answering%20Generation%20Fra.md) · 多模态基础模型 智能体 Agent Sim2Real 具身智能评测与基准
- [Video2STL: Grounding VLM-Generated Temporal Specifications for Robot Learning](items/Video2STL%20Grounding%20VLM-Generated%20Temporal%20Specifications%20for%20Robot%20Learning.md) · 多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- [Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing](items/Taming%20VLAs%20under%20Robot%20Execution%20Errors%20Self-Compensation%20and%20Stress%20Testing.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation](items/MultiTalk%20Scaling%20Full-Duplex%20Speech%20Models%20to%20Long%2C%20Multi-Party%2C%20Bilingual%20Conv.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [LongLive-Plug: Once-for-All Distillation for Video Generation](items/LongLive-Plug%20Once-for-All%20Distillation%20for%20Video%20Generation.md) · 多模态基础模型 世界模型
- [WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](items/WorldLine%20Action-Driven%20Visual%20Simulation%20for%20Robotic%20Manipulation.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2377
- 入选条目：24
- 回填已见条目：0
- 最高分论文：AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations
- 最高分论文发布时间：2026-09-29T07:34:54Z
- 主要技术对象分类：多模态基础模型 21、具身智能评测与基准 20、视觉语言动作模型 VLA 13、智能体 Agent 12、世界模型 11、机器人学习 9、Sim2Real 4
- 信息源错误：0
- 自动恢复信息源：0

</details>
