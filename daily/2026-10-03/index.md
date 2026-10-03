---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-10-03
---

# 2026-10-03 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：VLA 在真实执行中，怎样处理当前画面不足以决定下一步动作的问题。先读 DynamicVLA，理解推理耗时为何会让动作过期，以及如何按执行时刻筛选动作；再读 MIKASA-Robo-VLA，分清机器人到底需要记住什么、实验能否把记忆能力单独测出来；如果更关心真机接触失败后的改进，读 BORA，重点看如何把人的粗略纠正变成可执行动作，再用少量交互更新策略。
> **趋势**：前五篇的共同线索：这组论文把注意力放到了动作生成前后的具体条件：观测是否过期、关键线索是否消失、纠正是否可执行，以及长任务是否有足够细的监督。它们共同提示，评估 VLA 不能只看最终成功率，还要说明信息何时可见、执行如何安排、测试时人提供了多少帮助。

- **规模**：3902 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 21、视觉语言动作模型 VLA 20、具身智能评测与基准 18、世界模型 10、智能体 Agent 9、机器人学习 9、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation](items/DynamicVLA%20A%20Vision-Language-Action%20Model%20for%20Dynamic%20Object%20Manipulation.md)

> 机器人算完动作时，移动物体可能已经不在刚才的位置。DynamicVLA 一边执行一边继续推理，并丢掉动作序列中已经过期的前半段，让实际执行尽量跟上物体运动。

- **能借鉴什么**：当环境变化速度接近模型推理速度时，减少延迟和处理延迟都值得考虑。这里可借鉴的是：除了加速模型，还检查预测序列中哪些动作在执行时仍有效；这种思路尤其适合连续输出多个动作的控制方式。
- **值得读吗**：值得读到控制调度和动作裁剪的实现细节，因为这两处决定它是否真正解决执行时的时间错位。

<details><summary>实验依据</summary>

摘要给出 DOM 的规模：200K 合成回合，覆盖 2.8K 场景和 206 个物体，并能无需遥操作地快速收集 2K 真机回合。评估覆盖仿真和真实机器人，报告在变化的物体运动、需要较多视觉判断的指令和未见运动模式下提高成功率。摘要没有列出基线名称、成功率数值、测试次数或分项消融，因此可以确认评估范围，尚不能比较增益大小，也不能判断三个机制各贡献多少。

</details>

### 2. [NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields](items/NarrativeFlow%20Flow-Based%20Vision-Language-Action%20Model%20Using%20Robot%20Velocity%20Field.md)

> NarrativeFlow 用语言指定任务，再用连续速度场描述机器人应怎样运动。它希望用这种运动表示利用不同机器人收集的数据，减少对每个平台单独收集大量数据的依赖。

- **能借鉴什么**：可借鉴的方向是先选择一种较少依赖关节编号和身体结构的运动表示，再考虑合并多平台数据。如果各机器人的数据能转成可比较的速度场，这可能降低数据整合难度；转换是否可靠，是尝试这一做法的前提。
- **值得读吗**：值得先读运动场定义与执行转换部分，再决定是否深入实验，因为跨平台数据能否真正共用取决于这两处。

<details><summary>实验依据</summary>

摘要报告在语言条件操作的标准数据集上，标准指标优于代表性基线；真实世界的多项操作任务中，成功率也高于基线。但没有给出数据集名称、任务列表、指标定义、基线名称或任何结果数字。因此目前只能知道作者做了数据集和真机两类比较，不能判断优势大小，尤其不能确认是否直接验证了跨机器人迁移。

</details>

### 3. [MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation](items/MIKASA-Robo-VLA%20Benchmarking%20Memory%20in%20VLA%20Models%20for%20Long-Horizon%20Manipulation.md)

> MIKASA-Robo-VLA 把“动作所需线索先出现、随后消失”做成明确的测试条件，检查 VLA 是否能记住过去。它主要提供评测任务和示范数据，没有在摘要中给出一种新的记忆模型。

- **能借鉴什么**：可借鉴的是用任务设计证明“此时必须记忆”，而不只是按任务总时长贴上长程标签。比较记忆机制时，保留可见线索的对照还能帮助区分基础操作困难与信息丢失困难。
- **值得读吗**：值得细读任务构造和信息间隔定义；它最有用的地方是帮助设计能解释失败原因的记忆实验。

<details><summary>实验依据</summary>

摘要给出 10 类记忆任务和两种数据格式。70 项任务有明确的信息空缺时长，其中 28 项超过所调查固定上下文 VLA 中最宽的 16 帧窗口。参考 π₀.₅ 在 14 项任务上平均成功率为 0.211 ± 0.044；摘要未说明误差项定义。这个结果不能代表全部 90 项任务，也不能代表带记忆模型。作者明确提醒，Long 划分上更低的成功率还受到开环动作块和该子集中记忆类型的混杂影响。

</details>

### 4. [BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](items/BORA%20Bridging%20Offline%20Reinforcement%20Learning%20and%20Online%20Residual%20Adaptation%20for.md)

> BORA 让灵巧手 VLA 用少量真机试错和人的纠正继续学习，同时冻结原有大模型，只训练一个小的动作修正器。它还用局部策略把人的粗略意图转成协调的手指动作，让纠正数据真正能执行。

- **能借鉴什么**：这里值得借鉴的是把“人知道该怎么纠正”与“人能直接控制每个关节”分开处理。当纠正意图明确但动作难以执行时，可以先用局部策略生成可用纠正，再用小模型学习修正已有技能。
- **值得读吗**：值得读到数据收集流程和组件消融，因为它的实用性取决于纠正是否容易获得，以及小修正器到底承担了多少改进。

<details><summary>实验依据</summary>

摘要报告六项真机任务，覆盖单臂、双臂平台及两种灵巧手。每项只使用 20 条在线轨迹，标准物体平均成功率从 60.8% 到 82.5%，留出物体从 52% 到 70%。这些数字支持该设置下的少量在线适应，但摘要未明确前后比较配置、测试次数和误差。双臂扭转中的策略辅助也提高了干预可靠性，未给具体数值；它不等同于最终任务成功率。

</details>

### 5. [FineART: Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation](items/FineART%20Fine-Grained%20Annotated%20Robotic%20Trajectory%20Dataset%20and%20Vision-Language-Ac.md)

> FineART 为长程双臂操作补上密集的子任务标注，FineART-VLA 则学习先判断下一步子任务，再据此行动。它把整段示范里的中间步骤变成可学习的监督，使模型更容易知道当前该做哪一步。

- **能借鉴什么**：可借鉴的是标注示范中的“此刻在做哪个步骤”，让策略学习中间决策，而不只拟合动作。若长任务失败主要来自步骤选择，这种监督值得尝试；如果失败主要来自低层接触控制，摘要尚不能证明它同样有效。
- **值得读吗**：值得细读标注规则与自主、人工指导两组实验，因为它们决定密集子任务监督究竟改善了步骤选择还是执行能力。

<details><summary>实验依据</summary>

摘要给出数据规模：40,543 回合、1,718 小时、533,913 个子任务，覆盖 151 项任务。使用子任务标注进行中期训练后，空间指令成功率从 32.0% 到 100.0%；在逐步人工指导下，未见长程任务成功率从 16.0% 到 76.0%。后者不能解释为自主完成率。新机器人上少量微调后，所需数据为没有这种中期训练的基线的十分之一，并对新硬件未见任务零样本泛化；摘要未给绝对数据量、任务数或误差。

</details>

## 扫读 7 篇

- [Token-World: World Modeling in Vision-Language Model Token Space for Robot Manipulation](items/Token-World%20World%20Modeling%20in%20Vision-Language%20Model%20Token%20Space%20for%20Robot%20Manipu.md) — Token-World 不先生成机器人未来看到的图片，而是直接预测策略会读取的视觉特征。它先把庞大的 VLM 视觉 token 压缩，再学习动作如何改变这些状态，最后还原成策略可用的表示。
- [Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies](items/Divide-and-Remember%20Recursive%20Action-Relevant%20Memory%20for%20Long-Horizon%20VLA%20Polici.md) — Divide-and-Remember（D&R）让机器人学习保留“当前画面看不出、但会影响下一动作”的历史。它反复从 2K 个 token 中选出 K 个，并共享同一个选择器，让固定大小的记忆处理不断增长的历史。
- [DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication](items/DuoMind%20Enabling%20Distributed%20Multi-Robot%20Coordination%20with%20Semantic%20Communicatio.md) — DuoMind 让每台机器人分别负责“商量下一步”和“准确执行动作”。上层 VLM 根据本地画面与同伴消息安排任务，下层 VLA 执行具体操作，并通过语义消息持续协调。
- [Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models](items/Guide%2C%20Think%2C%20Act%20Interactive%20Embodied%20Reasoning%20in%20Vision-Language-Action%20Model.md) — GTA-VLA 给机器人一个可接收人类视觉纠正的接口：用户可以点位置、画框或轨迹，模型据此重新推理，再生成动作。它让“你应该操作这里”成为策略可用的明确输入。
- [DriftOPD: Sequence-Level Reverse-KL Distillation for One-Step VLA Policies](items/DriftOPD%20Sequence-Level%20Reverse-KL%20Distillation%20for%20One-Step%20VLA%20Policies.md) — DriftOPD 用离线示范学习“这个动作对后续完成任务有多大帮助”，再把这种依据加入一步动作生成的训练。它无需在线试跑或独立教师，目标是让生成便宜的动作专家也顾及长期后果。
- [Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining](items/Towards%20a%20General%20Humanoid%20Loco-Manipulation%20Model%20via%20Egocentric%20Whole-Body%20Hum.md) — λ₀ 想让人形机器人一边移动、一边用双手操作物体，关键是先从人类视频学交互，再从同步的身体与手部运动学协调，最后适配机器人。HumanVerse-500 补上了普通第一视角视频难以提供的全身运动监督。
- [WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation](items/WBAG%20A%20Whole-Body%20and%20Attached-Geometry%20Safety%20Framework%20for%20Vision-Language-Act.md) — WBAG 给 VLA 的动作加一道避碰修正：不仅保护手，还保护整个机器人和抓住的物体。它随抓取状态更新保护范围，再尽量少改原动作，使动作满足避碰约束。

## 其余存档 12 篇

- [HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution](items/HumanoidToolBench%20Benchmarking%20Humanoid%20Tool%20Use%20from%20Selection%20to%20Mobile%20Execut.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs](items/Same%20Scene%2C%20Different%20Task%20Skill%20Alignment%20for%20Compositional%20Generalization%20in%20V.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Bridging the Sim-to-Real Gap with multipanda_ros2: A Real-Time ROS2 Framework for Multimanual Systems](items/Bridging%20the%20Sim-to-Real%20Gap%20with%20multipanda_ros2%20A%20Real-Time%20ROS2%20Framework%20for.md) · 世界模型 Sim2Real 具身智能评测与基准
- [ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection](items/ATI-VLA%20Action-Centric%20Predictive%20Vision-Language-Action%20Models%20via%20Actionable%20A.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA
- [eRLT: Efficient VLA Reinforcement Learning via Action-Relevant Token Routing](items/eRLT%20Efficient%20VLA%20Reinforcement%20Learning%20via%20Action-Relevant%20Token%20Routing.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习
- [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](items/Is%20Success%20All%20You%20Need%20Investigating%20the%20Impact%20of%20Input%20Perturbations%20on%20VLA%20B.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](items/Reconstruct%2C%20Practice%2C%20Go%20Real%20Guided%20Self-Improvement%20for%20Embodied%20Agents.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization](items/Direct%20Action-Head%20Injection%20of%20A%20Grounded%203D%20Point%20Unlocks%20Spatial%20and%20Task%20Gen.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [WholeBodyWAM: Learning Whole-Body World Action Models with Scalable Motion Priors](items/WholeBodyWAM%20Learning%20Whole-Body%20World%20Action%20Models%20with%20Scalable%20Motion%20Priors.md) · 世界模型 视觉语言动作模型 VLA 机器人学习
- [LangMap: A Human-Verified Benchmark for Hierarchical Open-Vocabulary Goal Navigation](items/LangMap%20A%20Human-Verified%20Benchmark%20for%20Hierarchical%20Open-Vocabulary%20Goal%20Navigat.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [Devol-ONE: One Autoregressive Mixture of Transformers to Unify Vision-Language-Action and Latent World Modeling](items/Devol-ONE%20One%20Autoregressive%20Mixture%20of%20Transformers%20to%20Unify%20Vision-Language-Ac.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies](items/When%20Reasoning%20Helps%20Action%20Monitoring%20and%20Steering%20Chain-of-Thought%20in%20Vision-L.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：3902
- 入选条目：24
- 回填已见条目：0
- 最高分论文：DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation
- 最高分论文发布时间：Fri, 02 Oct 2026 00:00:00 -0400
- 主要技术对象分类：多模态基础模型 21、视觉语言动作模型 VLA 20、具身智能评测与基准 18、世界模型 10、智能体 Agent 9、机器人学习 9、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: HTTP Error 503: Service Unavailable (after 1 attempts); recovered via 4/4 configured fallback feeds

</details>
