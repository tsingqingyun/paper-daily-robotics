---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-09-18
---

# 2026-09-18 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天优先看能把方法改进落到真实机器人结果上的工作：WorldContact的数据扩增、高自由度手的后训练、离线蒸馏恢复压缩模型，以及量化前的性能退化预测，都给出了具体证据。另一条值得深入的线索是监督与表示的重构：用动作相似性促进跨本体迁移、用双边遥操作辨识刚度、用三维轨迹补全学习动力学；这些工作直接影响机器人能从哪些数据中学到什么。
> **趋势**：这批论文共同把注意力转向训练与部署中的具体瓶颈：数据是否可迁移、推理是否需要全量计算、失败后如何恢复，以及不确定时是否应暂缓决策。评价也开始覆盖速度、内存、接触控制和长程执行，但不少摘要仍只有定性结论，不能与有明确实机数字的工作等量齐观。

- **规模**：2340 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 15、多模态基础模型 14、视觉语言动作模型 VLA 13、机器人学习 12、世界模型 7、智能体 Agent 5、AI 核心知识地图 1、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning](items/Uni-LaDiR%20Latent%20Diffusion%20Unifies%20Multimodal%20Reasoning.md)

> Uni-LaDiR让不同模态的推理步骤先进入共享潜空间，再用扩散模型生成后续思考块，减少跨模态推理时的表示隔阂。它同时面向视觉推理和机器人动作任务。

- **为什么值得读**：对多模态基础模型与VLA研究者，价值在于探索视觉推理与动作决策能否共用一种可生成的中间表示，而不只是共享输入编码器。
- **证据**：摘要报告在11个VLM基准和2个VLA测试套件上评估；相对最强受测基线，视觉推理任务提升7.3%，机器人操作任务提升6.1%，均为相对增幅。
- **判断**：值得精读表示学习目标和VLA实验，跨视觉推理与操作的共同收益有吸引力，但机制归因仍需全文支持。

### 2. [WorldContact: A Contact-Centric World Model for Scalable Robot Learning](items/WorldContact%20A%20Contact-Centric%20World%20Model%20for%20Scalable%20Robot%20Learning.md)

> WorldContact用少量高质量轨迹训练接触中心的世界模型，更快生成购物袋操作数据，再用这些数据改善VLA的实机表现。关键是以比原数值模拟器更大的时间步预测物体运动。

- **为什么值得读**：直接连接世界模型、数据生成和VLA适配，为机器人学习研究者提供了以策略实机收益衡量世界模型价值的案例。
- **证据**：在16项购物袋操作任务中评估；单张H100上的状态滚动速度为原模拟器的10倍，不含渲染和磁盘I/O。实机提袋单次成功率从仅用原仿真数据微调的65%提高到扩增数据后的95%。
- **判断**：值得优先精读，重点核查接触建模、数据扩增配比和实机评估规模，因其同时报告了生成效率与策略收益。

### 3. [rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference](items/rMuscle%20Robotic%20Muscle%20Memory%20for%20Efficient%20Vision-Language-Action%20Model%20Inferen.md)

> rMuscle利用机器人反复执行相似任务时的“计算重复”，缓存视觉输出和内部激活模式，减少VLA推理中的重复计算与权重读取。

- **为什么值得读**：对VLA部署研究者，尤其是重复工位任务，提供了不必每次重新完成全部计算的系统优化路径。
- **证据**：在RTX 4090和Jetson Thor上，跨LIBERO、RoboTwin及实体操作任务获得1.29—1.42倍加速；摘要称真实机器人成功率保持不变。
- **判断**：做VLA推理系统值得精读缓存策略；若关注开放环境泛化，先看缓存失效条件与适用范围。

### 4. [Towards High-DoF Dexterous Manipulation through VLA Post-Training](items/Towards%20High-DoF%20Dexterous%20Manipulation%20through%20VLA%20Post-Training.md)

> 这项工作把通用VLA接到高自由度灵巧手上，再通过示范纠错和真实机器人强化学习提高可靠性。关键是用手部动作编解码器统一动作接口，并把探索限制在协调的手部运动空间。

- **为什么值得读**：对VLA和机器人学习研究者，实际价值在于把动作接口、人工纠错质量和实机探索放在同一适配流程中处理。
- **证据**：在涵盖双手传递、手内重定向和工具使用的5项真实任务上，每项测试20次，在所报告后训练预算内均达到100%成功率。
- **判断**：灵巧手方向值得优先精读实施细节，尤其是接管连续性与潜空间残差控制，不能只看100%的结果。

### 5. [FASA: Feedback-Aware Sampling Adaptation for Efficient Diffusion-Based VLA Models](items/FASA%20Feedback-Aware%20Sampling%20Adaptation%20for%20Efficient%20Diffusion-Based%20VLA%20Models.md)

> FASA根据机器人当前看到的情况、夹爪受力和自身状态，动态调整扩散VLA的采样步骤，让不同交互阶段使用不同计算量，无需额外训练。

- **为什么值得读**：为资源受限平台上的VLA提供运行时计算分配思路，适合研究交互状态与推理预算之间的关系。
- **证据**：摘要报告在若干基准上最高达到1.45倍推理加速，并保持有竞争力的成功率；未给出基准名称、绝对成功率或具体硬件结果。
- **判断**：值得读运行时调度机制，但在看到逐任务速度与成功率对照前，不宜据摘要判断部署优势。

## 扫读 7 篇

- [PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](items/PointZero%203D%20Point%20Track%20Completion%20for%20Learning%20Transferable%203D%20Dynamics.md) — PointZero通过“补全三维点未来怎么走”学习动力学：给定一张RGB-D观测和少量局部轨迹，预测所有已观测点的未来轨迹，预训练不需要机器人动作标签。
- [AI Smart Glasses for Wearable Intelligence: From Egocentric Sensing to Agentic Personalization](items/AI%20Smart%20Glasses%20for%20Wearable%20Intelligence%20From%20Egocentric%20Sensing%20to%20Agentic%20Pe.md) — 这篇综述把AI眼镜视为持续观察、理解并帮助用户的完整系统，梳理传感、计算、交互和应用需求如何共同决定能力。
- [Improving Cross-embodiment Transfer in Latent Action Models with Action-Similarity Supervision](items/Improving%20Cross-embodiment%20Transfer%20in%20Latent%20Action%20Models%20with%20Action-Similari.md) — 这项工作用“两个动作有多相似”监督潜动作，而不要求潜动作还原某台机器人的具体控制命令，让不同机器人的相似运动更容易对齐。
- [Co-VLA: Consensus-based Federated Training for Vision-Language-Action Models](items/Co-VLA%20Consensus-based%20Federated%20Training%20for%20Vision-Language-Action%20Models.md) — Co-VLA让不同地点的机器人保留本地数据，通过ADMM共识优化协作训练一个VLA，目标是在数据不集中时接近集中训练效果。
- [Affective Shared Autonomy: Temporal Affect Dynamics and Subjective Evaluation in Bimanual Teleoperation Tasks](items/Affective%20Shared%20Autonomy%20Temporal%20Affect%20Dynamics%20and%20Subjective%20Evaluation%20in.md) — 这项共享自主遥操作系统根据操作者持续出现的不良状态决定何时帮忙，而不是只看机械臂是否偏离目标。
- [Calibrated Probabilistic Obstruction Reasoning with Vision-Language Models for Grasping in Clutter](items/Calibrated%20Probabilistic%20Obstruction%20Reasoning%20with%20Vision-Language%20Models%20for%20G.md) — CPOR-Grasp不急着认定唯一的遮挡关系，而是综合多种可能场景，决定直接抓目标、先移开障碍，还是暂缓行动。
- [Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation](items/Recovering%20Aggressively%20Pruned%20Vision-Language-Action%20Models%20with%20Offline%20Hidden.md) — 这项工作在大幅剪小VLA后，用离线缓存的教师隐藏状态恢复能力，避免依赖在线机器人探索。关键是缩窄网络块，同时保留残差流维度，使师生状态能直接对齐。

## 其余存档 12 篇

- [Runtime Safety Filtering for Two-Terminal Hazards in Robotic Battery Recycling](items/Runtime%20Safety%20Filtering%20for%20Two-Terminal%20Hazards%20in%20Robotic%20Battery%20Recycling.md) · 视觉语言动作模型 VLA 具身智能评测与基准
- [EmbodiedMind: Adaptive Data Curation and Prefix-Tree Reinforcement Learning for Efficient Embodied Intelligence](items/EmbodiedMind%20Adaptive%20Data%20Curation%20and%20Prefix-Tree%20Reinforcement%20Learning%20for%20E.md) · 多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- [Quantifying Mechanical Intelligence in Legged Robots with Information Theory](items/Quantifying%20Mechanical%20Intelligence%20in%20Legged%20Robots%20with%20Information%20Theory.md) · 世界模型 具身智能评测与基准
- [ParticleSplat: Self-supervised Object-centric Latent Particle Splatting](items/ParticleSplat%20Self-supervised%20Object-centric%20Latent%20Particle%20Splatting.md) · AI 核心知识地图
- [Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation](items/Compliance%20for%20Free%20Learning%20Identifiable%20Impedance%20via%20Bilateral%20Teleoperation.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- [CitySTAR: Structured and Topology-Aware Reasoning for Open-Vocabulary Urban 3D Grounding](items/CitySTAR%20Structured%20and%20Topology-Aware%20Reasoning%20for%20Open-Vocabulary%20Urban%203D%20Gr.md) · 多模态基础模型 具身智能评测与基准
- [WeaveRL: Weaving Reconstruction into Scene-Aware Fabrics for Perceptive Reinforcement Learning](items/WeaveRL%20Weaving%20Reconstruction%20into%20Scene-Aware%20Fabrics%20for%20Perceptive%20Reinforce.md) · 世界模型 机器人学习 Sim2Real
- [MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution](items/MAGMA-GEN%20Validated%20Recovery%20Supervision%20from%20Ambiguous%20Failures%20via%20Counterfact.md) · 智能体 Agent 世界模型 机器人学习
- [MaskHarness-WAM: Instance-Grounded Harnessing for Long-Horizon Robot Manipulation](items/MaskHarness-WAM%20Instance-Grounded%20Harnessing%20for%20Long-Horizon%20Robot%20Manipulation.md) · 智能体 Agent 具身智能评测与基准
- [BinoGen: Scaling egocentric binocular data for embodied visual perception and learning](items/BinoGen%20Scaling%20egocentric%20binocular%20data%20for%20embodied%20visual%20perception%20and%20lea.md) · 多模态基础模型
- [LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation](items/LIFD%20Anchored%20Diffusion%20for%203D-Aware%20Scene%20Memory%20in%20Robotic%20Manipulation.md) · 视觉语言动作模型 VLA 机器人学习
- [Predict Before You Deploy: Offline Prediction of Quantization-Induced Task Degradation for World Action Models](items/Predict%20Before%20You%20Deploy%20Offline%20Prediction%20of%20Quantization-Induced%20Task%20Degrad.md) · 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2340
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning
- 最高分论文发布时间：2026-09-17T08:28:18Z
- 主要技术对象分类：具身智能评测与基准 15、多模态基础模型 14、视觉语言动作模型 VLA 13、机器人学习 12、世界模型 7、智能体 Agent 5、AI 核心知识地图 1、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
