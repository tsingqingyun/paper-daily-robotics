---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-10-20
---

# 2026-10-20 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看三个问题：机器人怎样自己积累可复用经验、VLA 怎样更容易训练、动作生成怎样更快。想研究自主改进，先读 RAX，重点追踪探索结果如何变成可执行技能；想改善训练起点，读 EmbodiedMidtrain，检查它如何挑出贴近机器人任务的视觉语言数据；受控制延迟限制，先读 MambaAct，它把改动集中在反复执行的动作专家上，收益也最容易量化。
> **趋势**：前五篇的共同线索：这些摘要共同指向：机器人能力的改进正在细化到经验获取、训练数据衔接、动作计算、历史记忆和多策略交互等具体环节。它们采用的证据不同：单机成功率、推理延迟、多臂协作实验与综述分类不能直接合并成统一排名。

- **规模**：2945 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 18、具身智能评测与基准 16、智能体 Agent 16、视觉语言动作模型 VLA 14、世界模型 11、机器人学习 10、Sim2Real 1
- **源异常**：2
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Scaling Online Exploration for Robot Agents](items/Scaling%20Online%20Exploration%20for%20Robot%20Agents.md)

> RAX 让通用编码智能体通过实际试操作编写机器人控制程序，再把成功经验整理成可组合技能。它试图减少新机器人、新任务对遥操作示范的依赖，让机器人靠在线经验继续进步。

- **能借鉴什么**：值得借鉴的是把探索成果保存为可检查、可调用的程序：后续任务有机会复用已经验证的处理流程。适合重点检查的条件是，任务能否通过 API 操作，以及成功与失败能否可靠判断。
- **值得读吗**：值得细读探索、验证和技能复用流程，因为决定它能否落地的是经验如何可靠积累，而不只是代码能否生成。

<details><summary>实验依据</summary>

摘要报告研究覆盖单臂、双臂、灵巧手、移动和人形系统，包含仿真与真机。仿真相对顶尖基线平均高出 37.4%，但未说明这是相对增幅还是百分点，也未给基线名称与汇总方式。真机展示记忆相关、关节物体、精密、可变形物体及移动长流程任务，没有提供成功率和试验次数。证据支持方法覆盖面与探索收益，尚不足以量化部署成本。

</details>

### 2. [EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training](items/EmbodiedMidtrain%20Bridging%20the%20Gap%20between%20Vision-Language%20Models%20and%20Vision-Lang.md)

> EmbodiedMidtrain 在通用 VLM 变成机器人 VLA 之前，加一道贴近具身任务的中间训练。关键是从大规模视觉语言数据中挑选更接近机器人数据的样本，让动作学习从更合适的起点开始。

- **能借鉴什么**：这里可借鉴的是先检查预训练数据与目标任务的距离，再决定中间训练内容。若动作微调数据有限，补充与空间理解更接近的视觉语言样本，是值得检验的路径。
- **值得读吗**：值得读到选样目标和等预算消融，因为它们决定这套数据准备方式能否迁移到其他 VLA。

<details><summary>实验依据</summary>

摘要报告，在仿真操作基准和真机任务上，相比现成 VLM 检查点，不同骨干与动作头均获得提升；收益也覆盖未用于指导选样的下游任务。训练分析称收益从微调早期出现并持续扩大。摘要没有给出基准名称、成功率、训练成本或误差范围，因此能支持跨设置的一致方向，不能判断收益大小及性价比。

</details>

### 3. [MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models](items/MambaAct%20Efficient%20Mamba%20Action%20Experts%20for%20Flow-Matching%20Vision-Language-Action.md)

> MambaAct 保留 π₀.₅ 的视觉语言编码部分，把反复生成动作的 Transformer 专家换成更小的 Mamba 专家。它先压缩视觉语言信息，再用压缩结果调节动作计算，减少每轮去噪的开销。

- **能借鉴什么**：可借鉴的是先优化被反复调用的部分，并把昂贵条件信息压成便宜的调节信号。对于迭代动作生成，这能让一次结构改动在每轮计算中重复节省时间。
- **值得读吗**：若关注 VLA 实时控制，值得读到模块实现和计时设置；它的主要说服力是明确减少反复执行的计算。

<details><summary>实验依据</summary>

摘要称动作专家缩小至约十分之一，流匹配去噪延迟在 LIBERO 降低 64.8%，真机部署降低 58.8%。三个独立微调种子下，LIBERO 平均成功率增加 1.08 个百分点，并在 LIBERO-Plus 和真机基准维持收益。摘要未给硬件、绝对延迟和方差；这些结果支持减少动作生成开销，不能直接理解成整套机器人控制延迟同比下降。

</details>

### 4. [From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models](items/From%20Sliding%20Windows%20to%20Self-evolving%20Lifelong%20Memory%20A%20Dual-perspective%20Survey.md)

> 这篇综述按记忆覆盖范围和保存时长，整理长流程 VLA 的记忆设计。它帮助读者区分模型究竟能记住当前任务的什么，哪些经验又能保留到以后。

- **能借鉴什么**：具体启示是先问信息需要保存多久、在哪些任务间复用，再选择记忆机制。例如，保存当前任务的一次观测，与跨任务保留操作经验，需要不同的写入、检索和更新策略。
- **值得读吗**：适合作为选读地图，先读分类与比较表，再沿具体机制找原论文；不要仅凭综述摘要选择记忆架构。

<details><summary>实验依据</summary>

摘要给出的主要结论是：所比较系统中，架构越复杂通常伴随开源成熟度越低。它还讨论高效记忆管理和终身知识演化。没有提供机器人测试任务、统一基线、成功率或比较样本数量，因此这是文献整理所得的观察，不能当作某种记忆机制提升任务成功率的实验，也不能解释成复杂架构导致开源不足。

</details>

### 5. [VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents](items/VLA-Fabric%20Learning%20Interaction%20for%20Composable%20Multi-Arm%20VLA%20Agents.md)

> VLA-Fabric 给每条机械臂配置一个完整 VLA，再让这些策略在生成动作时交换信息。关键是保留各臂自己的感知和动作责任，同时学习如何利用队友信息完成协作。

- **能借鉴什么**：值得借鉴的是把协作当作动作生成过程的一部分：一条臂作决定时就能利用其他策略的信息。对于各臂必须保留独立控制接口的系统，这提供了比单纯分工更细的协调切入点。
- **值得读吗**：值得细读交互位置消融和组队训练设置，因为它们决定协调机制能否复用，以及扩展团队需要付出多少代价。

<details><summary>实验依据</summary>

摘要报告三臂、四臂团队的仿真与实物实验。在全部四项实物任务上，Full interaction 相比独立训练的本地策略提高 16—40 个百分点。另一种 VLA 架构上的结果支持原则不依赖单一实现，但摘要未给对应数字。任务名称、绝对成功率、试验次数及其他协调基线结果未提供，不能据此判断优于所有集中式方案。

</details>

## 扫读 7 篇

- [CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots](items/CoEvolve%20Self-Evolving%20Code%20Policies%20from%20Skills%20to%20Strategies%20for%20Humanoid%20Robo.md) — CoEvolve 让机器人团队用可执行代码组织已有动作技能，执行不符合物理要求时，就依据验证结果修改协调方式。它调整的是“谁在什么时候怎样配合”，底层运动技能保持固定。
- [NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models](items/NestedVLA%20Learning%20to%20Consolidate%20and%20Generate%20Skills%20for%20Vision-Language-Action.md) — NestedVLA 不把各任务学到的参数直接混在一起，而是训练一个按任务生成动作专家参数的网络。生成的专家与冻结的基础 VLA 配合，让独立学到的技能能按需使用。
- [Has GPT-6-Astra Achieved Embodied Intelligence?](items/Has%20GPT-6-Astra%20Achieved%20Embodied%20Intelligence.md) — 这份报告研究 GPT-6-Astra 在机器人任务中能做到什么，以及这些成绩要付出什么代价。其关键是同时检查示范条件、执行预算、高低层控制配合和真机约束，而非仅凭任务完成率判断实用性。
- [Unifying Embodied Foundation Models via a Model-to-Policy Formulation](items/Unifying%20Embodied%20Foundation%20Models%20via%20a%20Model-to-Policy%20Formulation.md) — 这篇论文用同一套概率描述解释 VLA 和 WAM 怎样变成机器人策略：模型先产生输出，再通过动作实现规则变成可执行动作。它帮助澄清不同模型的控制接口，摘要未报告新的控制成绩。
- [NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation](items/NativeMEM%20Native%20Memory%20Compression%20for%20Long-Horizon%20Robotic%20Manipulation.md) — NativeMEM 把每个相机的每张历史画面压成一个 token，再放进 VLA 输入，让动作决策能直接查看过去。它复用模型自己的视觉编码器，目标是同时保留较长历史和高频更新能力。
- [Towards Unified World Models for Visual Navigation via Memory-Augmented Planning and Foresight](items/Towards%20Unified%20World%20Models%20for%20Visual%20Navigation%20via%20Memory-Augmented%20Planning.md) — UniWM 让导航机器人把“接下来会看到什么”和“接下来怎么走”放进同一个模型，让选动作时能依据想象出的视觉结果。它还把眼前线索与此前走过的轨迹结合起来，帮助连续决策保持一致。
- [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](items/Monkey%20See%2C%20Can%20Monkey%20Do%20A%20Benchmark%20for%20Evaluating%20Robot%20Skill%20Learning%20by%20Obs.md) — RoboReel 把人类示范视频、机器人仿真轨迹和评测环境配套提供，用来比较机器人“看别人做，再自己做”的能力。它的关键贡献是统一比较条件，并专门检查视觉干扰和长任务等难点。

## 其余存档 12 篇

- [Pedicel-Targeted Strawberry Harvesting via Imitation Learning on a Low-Cost Teleoperated Robotic Arm](items/Pedicel-Targeted%20Strawberry%20Harvesting%20via%20Imitation%20Learning%20on%20a%20Low-Cost%20Tele.md) · 智能体 Agent 机器人学习
- [LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence](items/LAW%20Unifying%20Language%2C%20Action%2C%20and%20World%20Modeling%20for%20Agentic%20Physical%20Intellige.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [ME-VLM: A Unified VLM for Embodied Cognition and Agent Coordination](items/ME-VLM%20A%20Unified%20VLM%20for%20Embodied%20Cognition%20and%20Agent%20Coordination.md) · 多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- [Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors](items/Sample-Efficient%20Reinforcement%20Learning%20for%20Policy%20Improvement%20via%20Flow-Reversed.md) · 机器人学习 具身智能评测与基准
- [GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation](items/GRASP%20Global-Local%20Representation%20Alignment%20and%20Spatial-Physical%20Grounding%20for%20B.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation](items/Look%20Before%20You%20Act%20Bridging%20Active%20Perception%20and%20Vision-Language-Action%20Models.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization](items/Enhancing%20Visual%20Task-Redirection%20Attacks%20on%20Vision-Language-Action%20Models%20via%20C.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA
- [OpenDexGrasp: Open-vocabulary Task-Oriented Dexterous Grasping](items/OpenDexGrasp%20Open-vocabulary%20Task-Oriented%20Dexterous%20Grasping.md) · 多模态基础模型 世界模型 机器人学习
- [DexBioLab: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](items/DexBioLab%20Benchmarking%20Dexterous%20Manipulation%20with%20Dynamic%20Experimental%20Phenomen.md) · 智能体 Agent 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](items/WorldOracle%20Benchmarking%20Action-Conditioned%20World%20Models%20against%20Real-World%20Exec.md) · 世界模型 具身智能评测与基准
- [InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration](items/InstAgent%20A%20Recursively%20Self-Improving%20Agent%20Operating%20System%20for%20Heterogeneous.md) · 多模态基础模型 智能体 Agent
- [Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems](items/Beyond%20Success%20Rate%20Interventional%20Evaluation%20of%20Memory%20in%20Vision-Language-Actio.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2945
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Scaling Online Exploration for Robot Agents
- 最高分论文发布时间：Mon, 19 Oct 2026 00:00:00 -0400
- 主要技术对象分类：多模态基础模型 18、具身智能评测与基准 16、智能体 Agent 16、视觉语言动作模型 VLA 14、世界模型 11、机器人学习 10、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: HTTP Error 429: Unknown Error (after 1 attempts); recovered via 4/4 configured fallback feeds

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
