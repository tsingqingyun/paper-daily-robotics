---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-10-02
---

# 2026-10-02 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看一个问题：怎样让机器人获得真正能支持行动的信息，并把试错花在有效的地方。想理解“看清目标”怎样影响控制，先读 GroundingPI 的坐标表示和感知预训练；想减少真机试错，先读 SimEX 的“真实失败修正仿真、仿真筛选修复”循环；想解决长任务越做越偏，读 H-WM 如何把逻辑进度与视觉变化一起交给动作模型。以下均依据给定摘要，未获得正文节选。
> **趋势**：前五篇的共同线索：这些论文共同关注行动所需的信息组织：精确位置、逻辑进度、接触反馈，以及能检验修复方案的仿真反馈。Fiatlux 则把评测推进到连续完成移动、攀爬和易碎物操作，要求模型在整段任务中维持成功条件。

- **规模**：3971 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 21、多模态基础模型 21、视觉语言动作模型 VLA 20、世界模型 13、智能体 Agent 13、机器人学习 9、Sim2Real 3
- **源异常**：2
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](items/GroundingPI%20A%20Grounding%20Foundation%20Model%20towards%20Physical%20Intelligence%20with%20Visu.md)

> GroundingPI 把“按描述找到目标，并准确指出位置”作为专门能力训练，用统一词表输出点和框的离散坐标。它再充当机器人和驾驶模型的视觉骨干，让后续决策获得更精确的目标定位信息。

- **能借鉴什么**：当动作失败源于目标选错、位置偏差时，可以先改视觉训练数据与定位监督。摘要的数据配方分析尤其提示密集定位值得检查；OCR 的作用仍被表述为潜在促进因素，不能直接当作通用配方。
- **值得读吗**：值得重点读坐标表示、数据配方和下游对照设置，因为最可借鉴的是如何把感知训练目标对准行动瓶颈。

<details><summary>实验依据</summary>

摘要报告：4B 模型在涵盖 11 类感知能力的 34 个定位基准上，与 44 个基线比较，平均成绩为 73.68%，GPT-6 Astra 为 71.54%；平均指标的聚合方式未给出。RoboTwin 2.0 的四种分布外设置均优于所测主流骨干，相对最强骨干最多提高 24.8%。RoboCasa-GR1 上，使用 50% 演示超过使用 75% 演示的基线。nuScenes 开环平均 L2 误差为 0.296 米，但未给对应基线数值。这支持所测任务中的迁移收益，不能据此确定真机闭环可靠性。

</details>

### 2. [H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model](items/H-WM%20Robotic%20Task%20and%20Motion%20Planning%20Guided%20by%20Hierarchical%20World%20Model.md)

> H-WM 同时预测“任务逻辑上接下来发生什么”和“视觉状态会怎样变化”，再把两者作为中间指引交给 VLA。它试图让长任务的动作既跟得上计划，也对得上场景变化。

- **能借鉴什么**：值得借鉴的是把“任务做到哪一步”显式提供给动作模型。对需要维护前置条件的任务，逻辑状态可以帮助区分外观看起来相近、下一步动作却不同的场景；视觉预测则提供与具体场景变化相关的信息。
- **值得读吗**：值得读到模型接口与消融实验，因为论文是否有说服力，取决于两类预测如何共同约束动作。

<details><summary>实验依据</summary>

摘要称在三个长时序基准及真实机器人上，H-WM 持续改善 VLA 表现，并将收益描述为执行更稳定、误差累积减轻。未给出基准名称、VLA 基线型号、成功率、任务长度或数值增益。因此可以确认作者报告了跨基准与真机的改善，但无法比较增益大小，也无法仅凭摘要确定改善具体来自哪种中间指引。

</details>

### 3. [SimEX: Simulation-Integrated Robotics AutoResearch](items/SimEX%20Simulation-Integrated%20Robotics%20AutoResearch.md)

> SimEX 让编程智能体先在仿真里反复开发机器人技能，再用少量真机试验同时修正技能和仿真器。巧处是让每次真实失败都改善后续虚拟实验，从而帮助筛选修复方案。

- **能借鉴什么**：仿真器可以承担一个具体职责：判断哪种修复更可能有效。这样，仿真开发的重点可以围绕当前失败所涉及的物理因素展开，而不是一开始就追求所有细节都准确。
- **值得读吗**：值得深入读真实失败到仿真修正的实例，因为这一步决定 SimEX 能否成为可复用的调试方法。

<details><summary>实验依据</summary>

摘要报告进行了仿真到仿真测试及真实机器人测试，真机任务包括毛巾折叠、条码扫描和盘子操作，并称无需演示、仅需 10 分钟真机交互即可获取技能。摘要未给出成功率、基线成绩、重复次数，也未说明 10 分钟按单任务、单次适配还是整体统计。因此它支持低真实交互成本的可行性报告，尚不足以量化相对优势或稳定性。

</details>

### 4. [Tactile Curiosity Drives Robot Interaction](items/Tactile%20Curiosity%20Drives%20Robot%20Interaction.md)

> TacEx 把机器人的探索兴趣集中到“触觉上还有哪些接触现象没弄懂”。这样收集的数据更偏向碰触、抓取等操作过程，再用于离线学习拾放技能或后训练 VLA。

- **能借鉴什么**：它提供了一个可借鉴的探索原则：先判断任务所需的信息主要来自哪个感觉通道，再决定奖励哪类不确定性。对以接触为核心的操作，触觉能给探索增加方向，避免把所有不可预测变化都当成同样有用。
- **值得读吗**：值得读到探索奖励定义和模态消融，因为真正可迁移的想法是怎样把探索预算分配给有用的信息。

<details><summary>实验依据</summary>

摘要报告，无任务奖励和专家演示的探索可以产生密集接触数据，支持下游拾放策略的离线学习；TacEx 后训练也显著改善 VLA 的下游表现，并具有较高样本效率。但摘要没有列出测试环境、仿真或真机属性、基线名称、成功率及样本数。因此目前只能复述这些定性结果，无法估计提升幅度或硬件适用范围。

</details>

### 5. [Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb Replacement](items/Fiatlux%20A%20Long-Horizon%20Benchmark%20for%20Humanoid%20Ladder%20Climbing%20and%20Light-Bulb%20Rep.md)

> Fiatlux 把搬梯子、攀爬、换灯泡和处理旧灯泡连成一个人形机器人长任务，并把掉落与易碎约束纳入成功条件。它提供的是检验整段协作能力的仿真基准。

- **能借鉴什么**：可借鉴的是把跨阶段约束写进评测：局部完成抓取或攀爬，并不保证最后换灯成功。部分分数有助于定位系统卡在哪一段，但最终完整成功仍要单独看。
- **值得读吗**：值得重点读成功条件、任务衔接和观测协议；其价值首先在于明确怎样算完成整件事。

<details><summary>实验依据</summary>

摘要提供了任务、评分与实现范围：十二个子任务，参考基线涵盖 RSL-RL PPO、零样本 NVIDIA GR00T N1.7 VLA 和全身控制器。全程成功要求新灯泡就位、旧灯泡进入处理箱、两者均未掉落且不越过易碎阈值。没有给出基线得分或整段成功率，因此这份摘要支持评测设计的介绍，不能据此判断哪类方法更强。所述环境为仿真，未报告真机验证。

</details>

## 扫读 7 篇

- [Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics](items/Exploiting%20Vulnerabilities%20Universal%20Adversarial%20Attacks%20on%20Vision-Language-Acti.md) — 机器人视野里多一个球，就可能明显干扰它完成指令。Universal Adversarial Object 的关键是优化球面纹理，让同一个实体物体同时干扰 VLA 的轨迹、任务执行和动作控制。
- [DexHoldem: An Agentic Robotics Benchmark for Dexterous Manipulation in Texas Hold'em](items/DexHoldem%20An%20Agentic%20Robotics%20Benchmark%20for%20Dexterous%20Manipulation%20in%20Texas%20Hold.md) — DexHoldem 用真实 ShadowHand 执行德州扑克相关桌面操作，检查机器人能否看清局面、完成动作，并给下一步留下可用的现场。它最有用的区分是：一次动作完成，不等于整局还能继续。
- [Bridge-WA: Learning Action-Relevant World Dynamics for Robotic Manipulation](items/Bridge-WA%20Learning%20Action-Relevant%20World%20Dynamics%20for%20Robotic%20Manipulation.md) — Bridge-WA 不只让机器人猜未来画面，还让它预测哪里会改变、局部会怎样运动，再把这些信息送进动作生成过程。关键是选择与动作有关的未来信息，并调节模型对这些预测的依赖。
- [Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory](items/Don%27t%20Drop%20the%20BATON%20Long-Horizon%20Robot%20Manipulation%20via%20Agentic%20Subtask%20Explora.md) — BATON 把长任务拆成可分别探索、记忆和复用的子任务，同时检查每一步留下的状态能否让下一步接手。它解决的不只是“这一招会不会”，还有“什么时候能用、用完后别人能不能继续”。
- [rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference](items/rMuscle%20Robotic%20Muscle%20Memory%20for%20Efficient%20Vision-Language-Action%20Model%20Inferen.md) — rMuscle 利用机器人重复做相似任务时的内部计算相似性，减少 VLA 每次推理的重复工作。它分别缓存视觉 token 输出和动作阶段的神经元激活模式，对准计算量与权重读取两种开销。
- [CrossSafe: Towards Cross-Embodiment Latent Safety Filters](items/CrossSafe%20Towards%20Cross-Embodiment%20Latent%20Safety%20Filters.md) — CrossSafe 想让不同机器人共用一个安全过滤器，同时让它知道当前机器人的身体长什么样、能怎么动。关键是在包含身体与环境信息的潜在表示里判断危险，并共享安全价值函数和避险策略。
- [RankQ: Offline-to-Online Reinforcement Learning via Self-Supervised Action Ranking](items/RankQ%20Offline-to-Online%20Reinforcement%20Learning%20via%20Self-Supervised%20Action%20Rankin.md) — RankQ 解决的是：机器人先用旧数据学习，再在线练习时，怎样既避免高估陌生动作，又不被旧数据里的差动作拴住。它给 Q 学习加入自监督动作排序损失，让价值函数学习动作之间的优劣关系。

## 其余存档 12 篇

- [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](items/Memorize%2C%20Adapt%2C%20Ignore%20Diagnosing%20Robot%20Learning%20Mechanisms%20under%20Training%20Data.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 Sim2Real 具身智能评测与基准
- [DSDyn-VLA: A Dual-Stream Dynamic Manipulation Framework with Motion Perception, Future Awareness, and Realtime Correction](items/DSDyn-VLA%20A%20Dual-Stream%20Dynamic%20Manipulation%20Framework%20with%20Motion%20Perception%2C%20F.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [Colosseum V2: Benchmarking Generalization for Vision-Language-Action Models](items/Colosseum%20V2%20Benchmarking%20Generalization%20for%20Vision-Language-Action%20Models.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](items/SafeVLA-Bench%20A%20Benchmark%20for%20the%20Success-Safety%20Gap%20in%20Vision-Language-Action%20M.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation](items/Uni-VLaT%20Whole-Body%20Tactile%20Adaptation%20of%20VLA%20Policies%20for%20Humanoid%20Loco-Manipul.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Language-Conditioned World Modeling for Visual Navigation](items/Language-Conditioned%20World%20Modeling%20for%20Visual%20Navigation.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [TALK-Dem: Benchmarking Embodied Task Planning under Dementia-Associated Communication Patterns](items/TALK-Dem%20Benchmarking%20Embodied%20Task%20Planning%20under%20Dementia-Associated%20Communica.md) · 智能体 Agent 具身智能评测与基准
- [Correcting WHERE, Preserving HOW: Compositional Generalization for Vision-Language-Action Models via Referential Guidance](items/Correcting%20WHERE%2C%20Preserving%20HOW%20Compositional%20Generalization%20for%20Vision-Languag.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [The Planning Limits of Latent World Models](items/The%20Planning%20Limits%20of%20Latent%20World%20Models.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models](items/Learning%20from%20Runtime%20Feedback%20through%20Failure-Bank%20Self-Evolution%20for%20Vision-La.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [EWAM: Emergent Depth-Wise Specialization in a Unified Embodied Model -- From Semantic Understanding through Visual Foresight to Action](items/EWAM%20Emergent%20Depth-Wise%20Specialization%20in%20a%20Unified%20Embodied%20Model%20--%20From%20Sema.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds](items/Scaling%20Sim-to-Real%20VLA%20Reinforcement%20Learning%20with%20Generative%203D%20Worlds.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 Sim2Real

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：3971
- 入选条目：24
- 回填已见条目：0
- 最高分论文：GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives
- 最高分论文发布时间：Thu, 01 Oct 2026 00:00:00 -0400
- 主要技术对象分类：具身智能评测与基准 21、多模态基础模型 21、视觉语言动作模型 VLA 20、世界模型 13、智能体 Agent 13、机器人学习 9、Sim2Real 3
- 信息源错误：1
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: The read operation timed out (after 1 attempts); recovered via 4/4 configured fallback feeds

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
