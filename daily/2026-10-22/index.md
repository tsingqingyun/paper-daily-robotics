---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-10-22
---

# 2026-10-22 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看一个问题：机器人适应新任务时，怎样保住已有能力，并把对场景的理解变成可执行的动作。先读 RARA，抓住“两阶段约束表征变化”这个可以直接借鉴的适配思路；再读 GPT-6 直接控制评测，理解空间判断与精确运动之间还差什么；如果关心长任务，再读 WorldScape Policy 2.0，看它如何用近期画面和历史事件支持下一步决策。两篇综述适合随后用来补齐概念和研究地图。
> **趋势**：前五篇的共同线索：这些摘要共同指向：机器人能力不能只靠模型理解指令，还取决于适配时保留什么、执行时记住什么，以及怎样根据反馈纠正动作。视频预测和通用多模态理解提供了新工具，但预测是否符合物理、动作是否可行，仍须分别验证。

- **规模**：4032 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 21、多模态基础模型 21、视觉语言动作模型 VLA 15、智能体 Agent 11、世界模型 9、机器人学习 5、Sim2Real 1
- **源异常**：3
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Physical AI: Concepts, Techniques, and Challenges](items/Physical%20AI%20Concepts%2C%20Techniques%2C%20and%20Challenges.md)

> 《Physical AI》想把“能理解物理世界”和“能在物理世界持续行动”之间的区别讲清楚：系统必须不断感知、预测、行动，再根据真实反馈调整。这是一部梳理概念与技术关系的专著，摘要没有给出新的控制算法。

- **能借鉴什么**：可借鉴的是检查问题的顺序：面对一个会输出动作的系统，先追问它怎样获得执行后的反馈、怎样修正错误、能否赶上控制时限。这样的检查能把“模型答得对”进一步拆成“系统是否持续做得对”。
- **值得读吗**：适合按问题选读，用它建立检查物理系统的视角；仅凭摘要，不宜把它当成某种技术路线有效性的证明。

<details><summary>实验依据</summary>

摘要列出了机器人、制造、基础设施、科学实验和自主服务等应用，以及感知、世界模型、控制、多智能体和软硬件协同等技术方向。这支持它覆盖面较广，但输入没有具体案例分析、比较表、实验指标或结果，不能据此认定其组织方式已被实验证明优于其他分类。

</details>

### 2. [RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation](items/RARA%20Robust%20Policy%20Fine-Tuning%20through%20Retrieval-Anchored%20Representation%20Alignme.md)

> RARA 要解决的是：机器人用少量新示范学会任务时，别把预训练时学到的本领改坏。它先找相近旧示范来对齐内部表征，再在学习新动作时限制这些旧示范的表征变化。

- **能借鉴什么**：值得借鉴的是把“保留旧知识”变成局部约束：挑与新任务有关的旧经验作为参照，再限制它们如何变化。若能访问预训练示范及对应表征，这比笼统要求模型少遗忘更容易落实到训练目标。
- **值得读吗**：值得优先读方法和消融，因为两阶段各自解决什么问题很清楚，而实用性主要取决于检索条件及额外成本。

<details><summary>实验依据</summary>

据摘要，实验使用 Diffusion Policy 和 GR00T，覆盖 RoboTwin、RoboCasa 及真实机器人，共 13 个任务。相对微调，分布内平均成功率提高 9.5 个百分点，分布外提高 13.6 个百分点，并超过所有参与比较的基线。输入未列基线名称、绝对成功率、任务分项及误差范围，因此能支持所测设置下的平均收益，不能推出每个任务都同幅改善。

</details>

### 3. [Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning](items/Large%20Multimodal%20Models%20for%20Direct%20Robot%20Control%20GPT-6%20as%20a%20Beginning.md)

> 这篇把 GPT-6 Astra 接入机器人反馈循环，检查通用多模态模型能否直接操控物体。它发现模型能利用深度、示范和触觉信息，但理解任务与生成精确、可行的运动之间仍有明显距离。

- **能借鉴什么**：可借鉴的是评测拆法：除检查模型是否看懂目标，还要单独检查动作能否实现目标、是否预见动作后果。挑选需要对齐、转动和避让的任务，能更直接暴露语言推理指标看不到的控制短板。
- **值得读吗**：值得重点读失败案例和控制接口，因为它最有用的贡献是说明通用模型在哪些操作环节仍会失手。

<details><summary>实验依据</summary>

据摘要，评测覆盖五个既有操作基准和六个能力维度；RoboDojo 成功率为 26.92%，RoboTwin 2.0 为 76.0%，LIBERO-GeoMotion 零样本成功率为 11.1%。这些是不同任务集，不能直接横向解释为同一能力的升降。真机实验也报告简单任务可零样本执行，但有运动可行性、精度、安全和延迟问题；输入没有真机数字、基线名单或重复试验信息。

</details>

### 4. [WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning](items/WorldScape%20Policy%202.0%20Empowering%20Steerable%20World%20Action%20Modeling%20with%20Reasoning-.md)

> WorldScape Policy 2.0 让同时预测画面变化和机器人动作的模型，既保留近期画面，也按事件查找过去发生过什么。检索出的历史帮助生成下一步计划，事件级数据则把具体指令、画面和动作联系起来。

- **能借鉴什么**：可借鉴的是按时间尺度保存不同内容：近期画面保留动作细节，较久历史保存事件和进度。如果任务失败源于重复步骤或忘记已完成事项，这种组织方式值得尝试，前提是事件记录与检索足够准确。
- **值得读吗**：值得读记忆更新与训练目标，但目前输入只能支持机制解释，性能判断需要具体对照和消融。

<details><summary>实验依据</summary>

据摘要，ManipEvent-5M 含近 500 万个事件片段，对齐动作轨迹、整段指令、子任务描述、目标图像和视频示范。这说明监督粒度，但不是性能结果。摘要称仿真与真机实验在长任务规划、指令遵循和上下文适应上表现更好，却未给基准名、比较对象、指标或数值，无法量化收益。

</details>

### 5. [Robotic Video World Models: A Survey of Applications, Research Challenges, Future Directions](items/Robotic%20Video%20World%20Models%20A%20Survey%20of%20Applications%2C%20Research%20Challenges%2C%20Future.md)

> 这篇综述讨论怎样把视频生成模型用于机器人：生成训练经验、预测动作后果、辅助评估和规划。关键边界是，画面逼真并不保证预测符合物理，机器人若依赖错误未来作决策，就可能选错动作。

- **能借鉴什么**：值得借鉴的是按用途判断预测需要多准：生成训练素材，重点要看策略最终学到了什么；用预测选择下一动作，则必须检查动作后果是否可信。先确定预测在决策中承担的责任，再选择评测方式，比只比较生成视频的视觉质量更有用。
- **值得读吗**：适合按用途查读原始研究，尤其关注模型如何接受动作条件、如何验证预测；摘要本身不足以支持替代物理仿真的结论。

<details><summary>实验依据</summary>

摘要提供的是应用分类和挑战清单，没有具体模型对比、任务、指标或实验数字。关于逼真画面、软体交互及物理一致性的描述应视为综述讨论的潜力，不能当成视频模型普遍可靠的实证；同一摘要也明确指出物理违规、指令遵循差及数据和计算开销。

</details>

## 扫读 7 篇

- [Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning](items/Embodied%20Playground%20A%20Long-Horizon%20Agentic%20Robotics%20Benchmark%20for%20Physical%2C%20Stra.md) — Embodied Playground 要测的是：机器人能否连续完成一串互相影响的操作，并在执行出错后继续推进。它用不同规划深度、几何约束和操作难度的任务，分别检查最终目标、过程守规和物理有效性。
- [EMMA: Enhancing Robotic Control Robustness through a Generative Visual Model](items/EMMA%20Enhancing%20Robotic%20Control%20Robustness%20through%20a%20Generative%20Visual%20Model.md) — EMMA 用生成视频补充机器人训练数据，让 VLA 见过更多物体外观、背景和光照。关键是 DreamTransfer 尽量保留操作的空间几何，再由 AdaMix 根据策略表现增加困难样本的训练权重。
- [FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models](items/FIT-MAC%20A%20Closed-Loop%20Multi-Agent%20Framework%20for%20Robust%20Vision-Language-Action%20Mo.md) — FIT-MAC 在 VLA 执行时加一层检查与纠错：先判断是认错目标，还是抓取、放置没执行好，再选择相应恢复动作。正常情况下仍由原来的 VLA 产生动作。
- [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](items/FastVLA%20Task-Conditioned%20and%20Temporally%20Adaptive%20Visual%20Token%20Compression%20for%20Ef.md) — FastVLA 根据当前任务挑选重要视觉 token，再随时间调整压缩力度，让 VLA 少处理一些图像信息。它无需训练，关键是同时回答“现在该看哪里”和“这一步需要保留多少”。
- [VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs](items/VLA-Retain%20Benchmarking%20Cross-Dimension%20Effects%20of%20Vision%20Tuning%20in%20VLAs.md) — VLA-Retain 检查视觉微调的副作用：模型适应新视角或传感器噪声后，其他变化条件下是否退步。它把每个微调模型与自己的原始版本比较，发现目标条件涨得多，并不能说明其他能力保留得好。
- [LayerRoute: Action-Conditioned Mixture-of-Layers Routing for Vision-Language-Action Policies](items/LayerRoute%20Action-Conditioned%20Mixture-of-Layers%20Routing%20for%20Vision-Language-Acti.md) — LayerRoute 让机器人生成动作时，按当前计算状态选择视觉语言模型哪些层的信息，并重新读取先前的动作表示。巧处在于把固定的信息接口改成随动作计算变化的选择过程。
- [Evaluating Social Reasoning in Embodied Vision-Language Models](items/Evaluating%20Social%20Reasoning%20in%20Embodied%20Vision-Language%20Models.md) — 这篇在 SHREC 真人与机器人互动数据上测试 Gemini Robotics-ER，发现它判断错误或能力表现较好，细致判断人的社会属性却较弱。研究还发现，增加一帧图像对两类任务的影响方向相反。

## 其余存档 12 篇

- [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](items/AgenticRoboRL%20Bringing%20Coding-Agent%20Post-Training%20to%20Agentic%20Robotics.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum](items/Frontier%20LLMs%20Enter%20the%20World%20of%20Robotics%20A%20Cross-Model%20Evaluation%20on%20RoboColise.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](items/ACE-Brain-0.6%20Scaling%20Spatial%20Grounding%20for%20Physical%20Foundation%20Models.md) · 多模态基础模型 具身智能评测与基准
- [PLaCA: Learning Patch-Level Future Latent Change for Action Generation](items/PLaCA%20Learning%20Patch-Level%20Future%20Latent%20Change%20for%20Action%20Generation.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future](items/Plausible%20Future%2C%20Wrong%20Choice%20Steering%20World-Action%20Models%20toward%20Intended%20Futu.md) · 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](items/OPIS%20An%20Input-Grounded%20Benchmark%20for%20Multi-Object%20Memory%20in%20Video%20World%20Models.md) · 世界模型 具身智能评测与基准
- [A Phenomenology of Neural Geometry in Vision-Language-Action Models](items/A%20Phenomenology%20of%20Neural%20Geometry%20in%20Vision-Language-Action%20Models.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA
- [From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation](items/From%20Predictive%20Geometry%20to%20Action%20Learning%20Complementary%20Predictive%20Representat.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [UniWALM: Unified World Action Language Model for Embodied Robot Control](items/UniWALM%20Unified%20World%20Action%20Language%20Model%20for%20Embodied%20Robot%20Control.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- [MMTA: Benchmarking Multimodal Temporal Analysis with Time Series, Text, and Vision](items/MMTA%20Benchmarking%20Multimodal%20Temporal%20Analysis%20with%20Time%20Series%2C%20Text%2C%20and%20Visio.md) · 多模态基础模型 具身智能评测与基准
- [Automating the Design of Embodied Agent Architectures](items/Automating%20the%20Design%20of%20Embodied%20Agent%20Architectures.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [EventSync: Event-Driven Memory Updates for History-Dependent Manipulation](items/EventSync%20Event-Driven%20Memory%20Updates%20for%20History-Dependent%20Manipulation.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：4032
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Physical AI: Concepts, Techniques, and Challenges
- 最高分论文发布时间：Wed, 21 Oct 2026 00:00:00 -0400
- 主要技术对象分类：具身智能评测与基准 21、多模态基础模型 21、视觉语言动作模型 VLA 15、智能体 Agent 11、世界模型 9、机器人学习 5、Sim2Real 1
- 信息源错误：2
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: HTTP Error 503: Service Unavailable (after 1 attempts); recovered via 4/4 configured fallback feeds

### 信息源错误

- Berkeley BAIR Blog: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)> (after 3 attempts)
- MIT Technology Review AI: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)> (after 3 attempts)

</details>
