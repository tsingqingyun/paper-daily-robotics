---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-28
---

# 2026-10-28 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看一个问题：机器人已经能理解指令，怎样让这种理解变成可靠动作，并确认评测真的反映执行能力？先读 SO-101 Bench，理解仿真排名能替代多少真机测试；再读 EBench-Astra，检查大模型与动作策略交接时为什么会丢掉各自优势；若关注训练方法，读 E0.5，重点看预测未来几何是否比重建当前场景更有帮助。
> **趋势**：前五篇的共同线索：这些论文把注意力从“换一个更大的模型”转向动作接口、监督目标和评测条件：动作如何被比较、委派或表示，直接影响执行结果。共同边界也很清楚：视频看起来合理、仿真分数高或组合系统更强，都需要另外验证物理一致性、真机表现及收益来源。

- **规模**：2392 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、智能体 Agent 15、多模态基础模型 14、视觉语言动作模型 VLA 10、机器人学习 8、世界模型 7、Sim2Real 3
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [SO-101 Bench: Accessible Spatial Manipulation](items/SO-101%20Bench%20Accessible%20Spatial%20Manipulation.md)

> SO-101 Bench 把低成本机械臂的语言空间操作搬进可重复的仿真，并用真机检查模型排名是否可信。它既测抓取，也专门测“放在两物之间”“旋转后才能塞进去”等容易被总成功率掩盖的能力。

- **能借鉴什么**：值得借鉴的是先验证评测器，再相信排行榜；还要把抓取、空间放置和旋转规划拆开看，否则可靠抓取可能掩盖空间执行短板。
- **值得读吗**：值得读到评测协议和配对真机结果；主要收获是学会怎样构造可信比较，而不只是记住榜首。

<details><summary>实验依据</summary>

主评测有916回合，分数是15个任务族×物体划分单元的平均成功率；九种 VLA/WAM 中最佳约61%，PLAN均不超过17%，组合智能体为83.2%、PLAN为75%。[S8](https://arxiv.org/html/2610.36420v1#S1.p4.1) [S20](https://arxiv.org/html/2610.36420v1#S3.SS6.p1.1) 五个系统各做45组仿真/真机测试，排名完全一致，Spearman为1.00，但仿真高估成功率9–31个百分点。[S23](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px2.p1.1) [S24](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px4.p1.1) 这支持该设置内的相对比较，不能把仿真分数直接当真机成功率。

</details>

### 2. [Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](items/Profiling%20a%20Frontier%20Agent%20with%20EBench%20From%20Direct%20Control%20to%20Harness%20with%20Polic.md)

> EBench-Astra 检查 GPT-6-Astra 何时适合直接控制机器人，何时应该调用学过机器人示范的策略。组合后总体更强、更省token，但调用时机、子目标传递和控制交接仍会制造失败。

- **能借鉴什么**：组合系统应把“谁来做、做哪一步、交回时保持什么状态”当成明确接口。仅给大模型增加一个策略调用按钮，并不会自动获得两者最好的能力。
- **值得读吗**：值得读执行轨迹和失败交接案例；它对组合控制的诊断，比总体分数更能指导实现。

<details><summary>实验依据</summary>

在仿真EBench的510个测试回合中，直接控制成功率46.7%，阶段完成分0.654；短任务73.2%，长任务27.3%，桌面操作20.0%，精密接触任务11.3%。它超过包括π0.5在内的部分后训练策略，但非所有策略。[S5](https://arxiv.org/html/2610.35832v1#S1.p4.1) [S6](https://arxiv.org/html/2610.35832v1#S1.p5.1) 调用π0.5或InternW0-Δ后，总成功率为53.0%和56.0%，每次成功的token成本下降超过一半。[S7](https://arxiv.org/html/2610.35832v1#S1.p6.1) 结果显示能力互补，尚未达到逐任务选择更强组件的上界。

</details>

### 3. [JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies](items/JevVLA%20Jev-Inspired%20Energy-Based%20Adaptation%20for%20Vision-Language-Action%20Policies.md)

> JevVLA 冻结原策略，另学一个小模型判断动作好坏：离散动作靠比较分数来选，连续动作靠分数对动作的梯度来修正。巧处是同一种标量函数同时承担“挑选”和“微调方向”两种工作。

- **能借鉴什么**：若已有可用策略，问题集中在候选取舍或局部偏差，可以先尝试训练评价器；但若要用梯度修动作，训练目标必须教会它邻域方向，不能只要求好动作排名更高。
- **值得读吗**：值得细读能量监督与推理更新规则；把它当作小型适配器方案评估，别把跨基准结构复用理解成通用控制器。

<details><summary>实验依据</summary>

在MetaWorld MT50、VIMA、LanguageTable、LIBERO Plus、CLIPort的独立测试集，相对各自冻结基线的成功率分别增加1.28、2.31、1.60、1.52、1.28个百分点。[S8](https://arxiv.org/html/2610.35010v1#S1.p6.1) 基线包括π0.5、VIMA-200M、行为克隆和CLIPort；核心为79,817参数，CLIPort按闭环执行后的完整成功计分。[S28](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px1.p1.1) [S29](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px2.p1.1) [S30](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px2.p2.1) [S31](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px3.p1.1) 证据支持同一结构适配不同接口，但增益较小，不能解释为一套权重跨任务通用。

</details>

### 4. [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](items/RynnWorld-Latent%20A%20Cross-Embodiment%20World%20Model%20Conditioned%20on%20Universal%20Latent.md)

> RynnWorld-Latent 用视频中提取的潜在动作代替各机器人互不兼容的控制指令，学习“给定这些变化，未来画面怎样发展”。它还把这种可控生成用于制作机器人训练数据。

- **能借鉴什么**：值得借鉴的是把“跨平台共享的运动描述”和“某台机器实际怎样执行”分开：前者吸收无动作标签的视频，后者在目标机器人适配时处理。不过制作训练数据仍需要可靠动作标签，生成画面并没有自动解决这个问题。
- **值得读吗**：值得读动作时间对齐与伪标签生成细节；判断价值应以闭环策略收益为主，不能只看生成视频。

<details><summary>实验依据</summary>

预训练覆盖23个数据集、约5.535亿帧。[摘要] 公共基准和两种真机平台的保留示范用于评估视频预测；下游以π0、π0.5为基础，报告LIBERO系列及真机策略相对仅真实示范训练有所改善。[S9](https://arxiv.org/html/2610.36791v1#S1.p7.1) [S24](https://arxiv.org/html/2610.36791v1#S4.SS1.p2.1) [S25](https://arxiv.org/html/2610.36791v1#S4.SS1.p3.1) [S26](https://arxiv.org/html/2610.36791v1#S4.F4) 但输入没有提供预测指标名称、分数和策略增益，无法判断改善幅度。真机每任务35次试验；同首帧更换动作序列的可控性证据主要是定性展示。[S37](https://arxiv.org/html/2610.36791v1#S5.SS0.SSS0.Px1.p1.1)

</details>

### 5. [E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling](items/E0.5%20From%20Reconstructive%20to%20Future-Predictive%203D%20Foundations%20for%20Robotic%20World-A.md)

> E0.5 直接把3D基础模型改成机器人策略骨干，同时学习动作和动作结束时的未来几何。它希望模型不只看懂“现在东西在哪里”，还学会“这一段操作之后空间结构会怎样变”。

- **能借鉴什么**：可借鉴的是让辅助目标对齐动作的时间跨度：预测执行后的物体位置，比只重建输入更直接要求表示与控制后果有关。它给已有3D模型提供了一条转向动作学习的路线。
- **值得读吗**：值得读到未来几何消融和监督构造；最有说服力的是与当前重建的直接比较，而非笼统的几何优势。

<details><summary>实验依据</summary>

RoboTwin 2.0仅用每任务50条干净示范训练，每任务100次测试；无机器人数据预训练时，干净/随机场景成功率为89.90%/50.09%。这高于π0.5的70.66%/46.00%，但低于PatchWAM的91.56%/66.72%。[S18](https://arxiv.org/html/2610.36011v1#S4.T1.7) [S24](https://arxiv.org/html/2610.36011v1#S4.SS2.SSS0.Px1.p1.1) 未来几何相对无几何、当前重建变体分别提高9.43、7.93个百分点。[S9](https://arxiv.org/html/2610.36011v1#S1.p8.1) 另用160,010条轨迹预训练后，真机Piper平均成功率70.0%→85.0%，H1约81.7%→88.3%。[S27](https://arxiv.org/html/2610.36011v1#S4.SS3.p2.1) [S30](https://arxiv.org/html/2610.36011v1#S4.SS4.SSS0.Px3.p1.1)

</details>

## 扫读 7 篇

- [EmbodiedLab: Benchmarking Embodied Agents That Act to Know](items/EmbodiedLab%20Benchmarking%20Embodied%20Agents%20That%20Act%20to%20Know.md) — EmbodiedLab 让机器人自己设计并操作实验，从实际读数中找出答案。它评测的不只是机器人有没有改变物体状态，还包括它是否通过操作获得了有证据支持的知识。
- [Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data](items/Zero-HLM%20Generalizable%20Humanoid%20Loco-Manipulation%20without%20Real%20Robot%20Data.md) — Zero-HLM 用手机采集真实环境，在仿真里修正场景和全身动作，生成可执行的示范，再训练人形机器人。巧处在于场景和动作一起改，避免得到看着像真的环境却跑不通的动作。
- [OmniBrain-0: A Unified Agentic Model for Embodied Intelligence](items/OmniBrain-0%20A%20Unified%20Agentic%20Model%20for%20Embodied%20Intelligence.md) — OmniBrain-0 把操作和导航的高层决策经验压进同一个轻量模型，让它负责安排步骤、跟踪进度和失败恢复。它先培养领域专家，再通过 MOPD 合并决策能力，并用执行证据继续改进专家。
- [OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation](items/OpenJaws%20An%20Open%20Hardware%20UMI%20Framework%20with%20Stereo%20Localization%20for%20Generalist.md) — OpenJaws 用双目相机配合手持夹爪采集示范，让人的操作轨迹成为机器人更可靠的动作标签。关键是更准确地恢复带真实尺度的轨迹，同时开放硬件、软件和定位评测。
- [HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](items/HIDRA%20Hierarchical%20Dual-Routing%20Attention%20for%20Replay-Free%20Lifelong%20Imitation%20Lea.md) — HIDRA 针对机器人连续学习新任务后“选错专家”的问题：先按指令找专家，再按当前情境细化选择。它还约束用于检索的键，让同任务保持接近、不同任务保持分离，减少学习新任务时的路由混乱。
- [The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](items/The%20Trinity%20Capability-Driven%20Recursive%20Self-Improvement%20for%20Multimodal%20Agents.md) — The Trinity 把不同外观的任务按所需能力重新组织，再为这些能力造简化练习环境、改进智能体的工具与执行配置。它要积累的是可以跨任务复用的能力模块，并按新任务选择合适配置。
- [Labference: Benchmarking the Reasoning-Action Connection in Robotic Laboratories](items/Labference%20Benchmarking%20the%20Reasoning-Action%20Connection%20in%20Robotic%20Laboratories.md) — Labference 要测清实验室机器人究竟是“下一步选错了”，还是“选对了但没做成”。它通过控制机器人看到的执行结果，并从相同检查点提供不同帮助，检查观察、决策与动作之间的联系。

## 其余存档 12 篇

- [RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](items/RoboAuto%20Autonomous%20Robot%20Program%20Search%20through%20Multi-Level%20Physical%20Understand.md) · 智能体 Agent 具身智能评测与基准
- [Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](items/Pretraining%20Knows%20What%2C%20Simulation%20Teaches%20How%20Compositional%20Generalization%20in%20a.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation](items/TOPS%20Reshaping%20Flow%20Source%20and%20Transport%20for%20Multi-Task%20Robot%20Manipulation.md) · 多模态基础模型
- [Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos](items/Mimetic%20Embodiment%20Transfer%20of%20Human-Humanoid%20Interaction%20from%20In-the-Wild%20Video.md) · 视觉语言动作模型 VLA 具身智能评测与基准
- [ActiveAlign: Aligning Egocentric Manipulation via Active Perception](items/ActiveAlign%20Aligning%20Egocentric%20Manipulation%20via%20Active%20Perception.md) · 智能体 Agent 世界模型 Sim2Real
- [VISTA: Active Exploration for Self-Improvement in Embodied Agents](items/VISTA%20Active%20Exploration%20for%20Self-Improvement%20in%20Embodied%20Agents.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [ASPEN: Adaptive Semantic Reasoning via Command Persistence Prediction for Efficient Navigation VLAs](items/ASPEN%20Adaptive%20Semantic%20Reasoning%20via%20Command%20Persistence%20Prediction%20for%20Efficie.md) · 多模态基础模型 视觉语言动作模型 VLA
- [DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models](items/DriveUniTok%20A%20Unified%20Multimodal%20Tokenizer%20for%20Driving%20World-Action%20Models.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- [Evolving Agent Teams](items/Evolving%20Agent%20Teams.md) · 多模态基础模型 智能体 Agent
- [A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation](items/A%20fully%20articulated%20humanoid%20dexterous%20hand%20with%20human-level%20joint%20structure%20ena.md) · 具身智能评测与基准
- [Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution](items/Multi-Objective%20Reinforcement%20Learning%20Using%20Routed%20Ensembles%20and%20Trajectory%20Att.md) · 机器人学习 具身智能评测与基准
- [Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution](items/Making%20Self-Driving%20Laboratories%20Auditable%20A%20Unified%20Framework%20for%20Hybrid%20Action.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2392
- 入选条目：24
- 回填已见条目：0
- 最高分论文：SO-101 Bench: Accessible Spatial Manipulation
- 最高分论文发布时间：2026-10-27T00:02:28Z
- 主要技术对象分类：具身智能评测与基准 16、智能体 Agent 15、多模态基础模型 14、视觉语言动作模型 VLA 10、机器人学习 8、世界模型 7、Sim2Real 3
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>

> [!warning] 外链核验（2026-10-28）
> Evolving Agent Teams 的代码仓库 https://github.com/caoshiyi/EAT 返回 `HTTP Error 404: Not Found`；论文来源可访问。代码公开状态待作者确认，后续重试。
