---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-08
---

# 2026-10-08 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先解决的问题是：机器人已经会生成动作，怎样让这些动作更可控，并从部署中的错误里学到正确东西？先读 TempoBridge，看如何把“快慢”接到冻结策略的执行控制上；再读 Robo-COP，看更新策略时为什么必须一起检查技能和旧记忆；若关注未来状态预测怎样真正帮助控制，读 Juno，重点看预测分支与部署适应的数据分工。
> **趋势**：前五篇的共同线索：这些论文共同把注意力从“模型能表示什么”移向“表示怎样影响实际动作”：速度语义要接到执行控制，未来状态要能支持动作解码，失败特征要成为可修改的目标。部署数据也需要区别使用：失败轨迹可以包含有效技能或真实动力学，但不能直接全部当作正确动作示范。

- **规模**：2299 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、多模态基础模型 15、世界模型 11、机器人学习 11、视觉语言动作模型 VLA 10、智能体 Agent 9、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies](items/TempoBridge%20Language-Guided%20Tempo%20Control%20for%20Vision-Language-Action%20Policies.md)

> TempoBridge 让机器人听懂“先快拿、再慢放”，而不用重新训练原有 VLA。它从冻结模型中读出快慢要求，判断当前做到哪一步，再调整原策略动作的执行幅度。

- **能借鉴什么**：值得借鉴的是：已有策略能完成任务时，可以把执行偏好接到明确的控制变量上，再让阶段判断决定何时生效；不必为了每种偏好重学整套动作。
- **值得读吗**：值得读到动作调节与指标定义，因为它的巧处是控制接口，而判断效果必须同时看任务完成和真实速度。

<details><summary>实验依据</summary>

LIBERO 四套共40个任务，每方法800次执行，使用同一 π₀.₅、匹配初始状态与种子。[S34](https://arxiv.org/html/2610.09451v1#S4.SS1.p1.1) [S40](https://arxiv.org/html/2610.09451v1#S4.SS2.p1.1) 相对快慢成功率52.6%→89.7%，任务成功率93.6%→92.9%，两者同时成功48.8%→82.0%。[S32](https://arxiv.org/html/2610.09451v1#S4.T1.6.1) 快慢指标只在成功且可比较的执行中计算，要求快段平均速度高于慢段，不考核指定绝对速度。[S37](https://arxiv.org/html/2610.09451v1#S4.SS1.p4.1) [S38](https://arxiv.org/html/2610.09451v1#S4.SS1.p5.1) 真机三个任务成功60/67，对照60/66；节选未给速度差值。[S43](https://arxiv.org/html/2610.09451v1#S4.SS6.p1.1) [S44](https://arxiv.org/html/2610.09451v1#S4.SS6.p2.1) [S45](https://arxiv.org/html/2610.09451v1#S4.SS6.p3.1)

</details>

### 2. [Co-Evolving Robot Orchestrators and Policies through Deployment](items/Co-Evolving%20Robot%20Orchestrators%20and%20Policies%20through%20Deployment.md)

> Robo-COP 让机器人从自己的任务尝试中收集有效技能，择机训练新策略，验证后才替换旧策略。它还重审“这个技能别交给 VLA”之类旧记忆，让调度方式跟上能力变化。

- **能借鉴什么**：最可借鉴的是把新检查点当候选，并把“这个工具能做什么”的记忆与工具版本一起维护。否则能力更新了，调度器仍可能沿用绕开它的旧建议。
- **值得读吗**：值得细读数据筛选和候选验证规则，因为决定成败的是哪些经验能学、学完怎样确认可用。

<details><summary>实验依据</summary>

十个 RoboLab 仿真任务各100次部署学习、50个共享留出初始状态；平均留出成功率冻结调度器64.8%，Robo-COP 73.8%，固定周期且不验证65.8%。[摘要、S32、S43–S44] 真机三任务各50次学习、20次测试，均值38.3%→50.0%；增益集中在带盖容器任务35%→70%，另两任务持平。[S33](https://arxiv.org/html/2610.09228v1#S4.SS3.p1.1) [S39](https://arxiv.org/html/2610.09228v1#S4.T2.6) 说明完整流程在这些任务有效，并非每次训练都会改善。

</details>

### 3. [Juno: Taming Predictive Latents for Vision-Language-Action Models](items/Juno%20Taming%20Predictive%20Latents%20for%20Vision-Language-Action%20Models.md)

> Juno 让“预测下一步会看到什么”真正服务于动作生成：先学机器人相关变化，再让独立预测分支同时接受未来状态和动作训练。部署失配时先修世界模型，再用经过验证的执行调整策略。

- **能借鉴什么**：关键启示是给失败数据分配合适用途：抓空的动作不值得模仿，但“这个动作实际造成什么变化”仍可训练动力学。预测教师也应先校准，再指导策略。
- **值得读吗**：值得读到训练梯度分工与适应流程，因为它解释了为什么“预测得像”还不足以“动作做对”。

<details><summary>实验依据</summary>

SimplerEnv 四个 WidowX 任务，每任务96次评估：Qwen3GR00T 60.9%，Juno 68.5%，额外部署训练后72.7%；胡萝卜任务未更新时60.4%→59.4%，并非全部改善。[S25](https://arxiv.org/html/2610.09940v1#S4.T1.6.1) [S40](https://arxiv.org/html/2610.09940v1#A3.SS1.p1.1) RoboCasa-GR1 24任务各50次，基线47.8%→59.6%。[S23](https://arxiv.org/html/2610.09940v1#S4.SS1.SSS0.Px3.p1.1) [S28](https://arxiv.org/html/2610.09940v1#S4.T2.4) 真机红方块入碗任务的背景、叠加高度与物体变化下，冻结 Juno 为75%、70%、70%，基线均0%，各20次；这些不是 TTT 结果。[S30](https://arxiv.org/html/2610.09940v1#S4.F4) [S31](https://arxiv.org/html/2610.09940v1#S4.T4.fig1) [S32](https://arxiv.org/html/2610.09940v1#S4.T4.fig1.1.1) [S39](https://arxiv.org/html/2610.09940v1#A2.SS1.SSS0.Px3.p1.1)

</details>

### 4. [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](items/Beyond%20Reconstruction%20What%20Matters%20in%20Action%20Tokenization%20for%20Robot%20Policies.md)

> ProAct 改变动作分词器的训练标准：还原动作准确之外，还要让策略容易选对词，并让陌生词组合解码得合理。它只使用动作数据训练，试图减少分词接口给控制带来的错误。

- **能借鉴什么**：这里值得借鉴的是按下游使用方式评价压缩表示。动作编码即使还原精确，若策略很难预测、错一个词就产生糟糕动作，仍不是好接口。比较分词器时应同时看重建误差、预测难度和执行结果。
- **值得读吗**：值得继续读方法与分词器对照实验，但目前只能确认它提出了合理的评价转向，还不能复述 ProAct 的具体训练算法。

<details><summary>实验依据</summary>

摘要报告：在 Robomimic、LIBERO、RoboTwin 和多种分词器架构上，执行成功率平均增加11.3个百分点；VLA与真机操作分别平均增加21.8、36.7个百分点。输入没有正文，未给任务数量、具体对照配置、绝对成功率、样本数或平均权重。这支持其训练方法在所测设置中有收益，但无法判断收益分布或稳定性。

</details>

### 5. [Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models](items/Sparse%20Feature%20Policy%20Unlearning%20Mitigates%20State%20Hallucination%20in%20Vision-Languag.md)

> SOUL 针对“没抓住却继续搬运”这类状态幻觉，找出与错误和成功分别相关的内部稀疏特征。它训练策略压低前者、强化后者，把修正写进参数，推理时无需反复干预特征。

- **能借鉴什么**：可借鉴的是用普通失败作参照，避免把“任何失败都会激活的特征”误当幻觉目标；同时明确保留成功表示，比只压制错误更符合机器人技能相互耦合的现实。
- **值得读吗**：值得细读特征选择与行为保留实验，因为它把解释结果变成了训练目标，但需要确认修正没有只适配已知失败。

<details><summary>实验依据</summary>

对照原策略与梯度上升遗忘：LIBERO-Plus/OpenVLA 幻觉率70%→44%，总成功26%→58%；RoboCasa/π₀.₅ 为40%→22.9%、41.9%→54.3%。梯度上升对照总成功降至0%和4.8%。[S30](https://arxiv.org/html/2610.09496v1#S4.T1.6.1) Franka真机跨两模型共50次执行，无幻觉成功平均增加20个百分点、幻觉失败减少22个百分点。[S43](https://arxiv.org/html/2610.09496v1#S5.SS2.p3.1) 结果支持这些设置下的选择性修正；节选未给仿真样本数与不确定性。

</details>

## 扫读 7 篇

- [Towards Accurate End-Effector Localization for UMI-Style Robotic Manipulation Teaching](items/Towards%20Accurate%20End-Effector%20Localization%20for%20UMI-Style%20Robotic%20Manipulation%20Te.md) — 手持操作接口采集示范时，贴近物体和相机被挡都会让末端轨迹难以准确、连续地记录。本文用 MILD 专门测这件事，再用 AprilVINS 将鱼眼视觉、惯性信息和本段序列里的 AprilTag 几何关系一起估计，减少定位误差。
- [RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation](items/RobotAPO%20Adversarial%20Physics%20Preference%20Optimization%20for%20Robotic%20Manipulation%20Vi.md) — RobotAPO 要让用于机器人规划的生成视频，在接触瞬间也符合物理。它用物理好坏偏好训练生成器，并让一个轻量对抗模块持续寻找容易出错的生成方向，避免只记住固定错误样例。
- [RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies](items/RoboPace%20Contact-Aware%20Time-Optimal%20Retiming%20for%20Action-Chunk%20Policies.md) — RoboPace 让机器人沿策略原本给出的路径运动，但重新安排快慢：自由空间可以加速，预计接触时要限速。它在执行时同时考虑接触和机器人运动约束，不需要重新训练策略。
- [Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment](items/Immiscible%20Diffusion%20Policy%20Preserving%20Multimodal%20Robot%20Actions%20through%20Label-Fr.md) — Immiscible Diffusion Policy 处理扩散策略学会一种动作、却丢掉其他有效动作的问题。它只改训练时动作与噪声的配对，让通向不同动作的去噪路线较少混在一起，网络和推理流程都不用改。
- [YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding](items/YUBI-STAG%20Contact%20and%20Semantic-Rich%20Alignment%20for%20VLAs%20via%20Automated%20Video-Langu.md) — YUBI-STAG 把只有粗任务名称的机器人视频，补成能说明哪只夹爪接触什么、怎样抓取和移动的细致标注。再把标注流程蒸馏成 YUBI-VLM，以较少调用处理原始视频，并用这些标注继续训练 VLA 的细粒度语言控制。
- [PAIR: Bridging Perception and Action in Vision-Language-Action Models](items/PAIR%20Bridging%20Perception%20and%20Action%20in%20Vision-Language-Action%20Models.md) — PAIR 给视觉语言动作模型补了一道“把看懂的场景变成动作准备”的接口：训练时用专家动作教会中间表示该保留什么，执行时只靠图像和指令生成这个表示，再交给动作模块细化。
- [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](items/Beyond%20Policy%20Support%20Interaction%20Constrained%20Offline%20Reinforcement%20Learning%20for.md) — ICDP 检查的不只是“我的驾驶动作在数据里常不常见”，还检查“它和周围车辆的行为搭不搭”。它用对比学习估计这部分交互支持，限制离线强化学习选择看似高价值、却缺少交互数据依据的轨迹。

## 其余存档 12 篇

- [RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning](items/RLHND%20Video%20Foundation%20Models%20as%20Physically%20Grounded%20Hand%20Trackers%20for%20Robot%20Lea.md) · 多模态基础模型 世界模型 机器人学习 具身智能评测与基准
- [Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization](items/Many%20Ways%20to%20Succeed%20Diversity-Driven%20RL%20Fine-Tuning%20for%20VLA%20Generalization.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习
- [Careful Judge: Safe and Efficient Human-AI Collaborative Decision Making](items/Careful%20Judge%20Safe%20and%20Efficient%20Human-AI%20Collaborative%20Decision%20Making.md) · 具身智能评测与基准
- [STRIKE: Learning Visual State Transitions for Physical World Modeling](items/STRIKE%20Learning%20Visual%20State%20Transitions%20for%20Physical%20World%20Modeling.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control](items/Precise%20SE%283%29%20End-Effector%20Tracking%20in%20Whole-Body%20Humanoid%20Control.md) · 世界模型 机器人学习 具身智能评测与基准
- [Controllable Crowd Generation through World-Model Planning](items/Controllable%20Crowd%20Generation%20through%20World-Model%20Planning.md) · 智能体 Agent 世界模型
- [LeCuration: A Tiny World Model as a Data Curation Multi-Tool](items/LeCuration%20A%20Tiny%20World%20Model%20as%20a%20Data%20Curation%20Multi-Tool.md) · 智能体 Agent 世界模型
- [PhysEvo: Astra Can Act, Let It](items/PhysEvo%20Astra%20Can%20Act%2C%20Let%20It.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [End-to-End Autonomous Generation of Human Assembly Plans](items/End-to-End%20Autonomous%20Generation%20of%20Human%20Assembly%20Plans.md) · 多模态基础模型 智能体 Agent
- [Point It, Strike It: Direction-Conditioned Dynamic Manipulation of Deformable Linear Objects](items/Point%20It%2C%20Strike%20It%20Direction-Conditioned%20Dynamic%20Manipulation%20of%20Deformable%20Lin.md) · 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies](items/DIVA%20Dual-Space%20Intent-Aware%20Visual%20Attenuation%20for%20Vision-Language-Action%20Polic.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Humanity's Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models](items/Humanity%27s%20Sixth%20Sense%20Benchmarking%20Intuitive%20Visual%20Reasoning%20in%20Multimodal%20Mod.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2299
- 入选条目：24
- 回填已见条目：0
- 最高分论文：TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies
- 最高分论文发布时间：2026-10-07T05:07:31Z
- 主要技术对象分类：具身智能评测与基准 16、多模态基础模型 15、世界模型 11、机器人学习 11、视觉语言动作模型 VLA 10、智能体 Agent 9、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
