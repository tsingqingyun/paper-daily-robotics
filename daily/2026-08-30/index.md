---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-30
---

# 2026-08-30 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天最值得看的，是机器人研究正在同时压缩“规模、延迟和数据”三类成本：PredVLA用不足百万参数挑战大模型控制，FlashVLA把流匹配 VLA 推到实时异步执行，CLAP、Zero-WAM 和 Riemann-1.0 则探索跨本体、跨任务的大规模经验迁移。另一条同样重要的主线是可靠性：历史建模、失败恢复、后门攻击、持续学习和更严格的评测边界，开始从附加功能变成系统设计的核心。
> **趋势**：共同趋势是把策略与世界动态放进更统一、因果且可流式执行的模型，同时用结构化中间量——预测误差、时间流、进度、事件、几何代理或记忆锚点——弥补纯动作预测的盲区。研究重点正从“离线成功率更高”转向实时性、长时程稳定性、跨本体泛化和失败可控性。

- **规模**：2269 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 15、智能体 Agent 14、多模态基础模型 11、世界模型 10、视觉语言动作模型 VLA 10、机器人学习 8、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [PredVLA: A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation](items/PredVLA%20A%20Sub-Million-Parameter%20Predictive-Coding%20Policy%20for%20Robot%20Manipulation.md)

> PredVLA说明语言条件操控未必需要巨型 VLA：它用仅 0.68M 可训练参数的预测编码循环策略，通过感知预测误差在线修正隐状态。

- **为什么值得读**：对 VLA 和机器人学习研究者，它给出了研究小模型控制、反馈修正及世界模型式内部预测的强基线，也便于分析闭环观测到底贡献了多少。
- **证据**：短时程三个 LIBERO 套件平均成功率 86.9%，计入长时程套件后为 75.4%。在冻结前端、演示、动作解码器和评测协议一致时，成功率分别是参数匹配 Transformer 和 LSTM 的 3.7 倍、7.4 倍。
- **判断**：值得精读方法和受控对比：亮点不只是小，而是把预测误差反馈做成了可测量的控制机制。

### 2. [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](items/CLAP%20Cross-Embodiment%20Video%20World%20Models%20are%20Zero-Shot%20Physical%20Simulators.md)

> CLAP把不同机器人乃至人类视频放进同一个动作条件视频世界模型：先用潜在动作从无标签视频学物理先验，再落到末端位姿等可执行动作空间。

- **为什么值得读**：对世界模型研究者，价值在于把互联网人类视频转化为机器人动力学先验，并提供跨本体预训练后再适配单平台的路线。
- **证据**：摘要称其在 DROID 等环境中接近或超过先进单本体视频模型，且少样本适配后优势进一步扩大；覆盖 DROID、Bridge、双臂 YAM 和 G1 等本体，但未给出可核查数字。
- **判断**：值得精读训练课程和动作统一方式；跨本体规模化很重要，但性能主张需看完整表格后再判断。

### 3. [FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](items/FlashVLA%20Streaming%20Action%20Decoding%20for%20Fast%20and%20Asynchronous%20VLA%20Inference.md)

> FlashVLA让流匹配 VLA 边生成边执行：维护处于不同噪声级的动作块缓冲区，用分块因果注意力每步产出一个可执行动作块。

- **为什么值得读**：对 VLA 落地者，这是直接针对控制频率和执行空转的系统机制，可能比继续缩小视觉语言骨干更能改善真实机器人闭环体验。
- **证据**：摘要称模拟和真实实验中显著提速并维持较强任务表现；单 GPU 可达到至少 30Hz，真实部署支持平滑异步推理。其余成功率和延迟数字未给出。
- **判断**：做实时流匹配 VLA 的研究者应精读；其他读者至少看清流式缓冲与因果分块设计。

### 4. [Riemann-1.0: An Embodied World Action Model for Physical AI](items/Riemann-1.0%20An%20Embodied%20World%20Action%20Model%20for%20Physical%20AI.md)

> Riemann-1.0试图用一个全因果自回归 World Action Model 同时承担机器人策略和动作条件世界模拟，并以渐进式预训练吸收人类、夹爪和多机器人数据。

- **为什么值得读**：对世界模型、VLA 和具身预训练研究者，它提供了统一策略—模拟器接口与大规模异构数据配方，也给出了高门槛基准结果。
- **证据**：基于超过 20 万小时交互数据；RoboTwin2.0、LIBERO、RoboCasa-365 成功率分别为 94.3%、99.0%、62.6%，后者超过此前最佳 8.4 个百分点。长时程真实操控 SR 85.0%、PSR 94.4%，SR 比最强开源基线高 15 个百分点。
- **判断**：今天最值得阅读全文的规模化工作之一，但应重点审查数据公平性和“一个模型双重用途”的实证强度。

### 5. [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](items/TrapVLA%20Trapping%20Vision-Language-Action%20Models%20in%20Configured%20Failure%20Modes.md)

> TrapVLA研究一种更危险也更具体的 VLA 后门：隐蔽文本触发器不仅让任务失败，还能指定机器人以何种偏差方式失败。核心是学习触发器诱导的动作残差。

- **为什么值得读**：对 VLA 安全和具身评测研究者，它把威胁模型从“让机器人坏掉”推进到“控制机器人怎么坏”，两个基准也可用于防御和审计。对世界模型本身的直接价值有限。
- **证据**：摘要称在模拟与真实机器人中能注入四类配置化故障，同时大体保持干净数据性能；未给出攻击成功率、干净性能下降或检测率数字。
- **判断**：安全研究者值得精读任务定义和指标；若只做控制性能，读基准与威胁模型即可。

## 扫读 7 篇

- [SpatialCrafter: Single Image World Modeling with Generative 3D Proxies](items/SpatialCrafter%20Single%20Image%20World%20Modeling%20with%20Generative%203D%20Proxies.md) — SpatialCrafter从单图生成可探索三维场景时，先生成全局 3D 代理，再让视频扩散模型沿代理几何补足写实细节，以降低漂移和跨视角幻觉。
- [GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation](items/GRAFT%20Grounded%20and%20Efficient%20Online%20Reinforcement%20Adaptation%20for%20Fine-Grained%20Ro.md) — GRAFT让预训练 VLA 用较少真实交互适配精细生物医学操作：用区域监督学视角相关视觉锚点，再以单步动作生成和前缀缓存压低在线更新成本。
- [TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation](items/TemporalFlow-VLA%20Learning%20Physically%20Grounded%20Execution%20History%20for%20Long-Horizon.md) — TemporalFlow-VLA不直接堆历史帧，而是在训练时用机器人几何构造表面时间流，监督两个时间查询，把有物理含义的执行历史压缩给动作专家。部署时不需要几何计算。
- [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](items/FLARE%20A%20Failure-Aware%20Framework%20for%20Autonomous%20Correction%20and%20Recovery%20in%20Visual.md) — FLARE用“Retry + Reset”给 VLA 加恢复能力：轻微偏差由带扰动和桥接段的策略自行重试，破坏任务状态的严重失败则由监控器调用专门复位技能。
- [LM-X: Explainable Action Modeling with Progress, Event, and Uncertainty Prediction for Generalist Robot Manipulation](items/LM-X%20Explainable%20Action%20Modeling%20with%20Progress%2C%20Event%2C%20and%20Uncertainty%20Predictio.md) — LM-X让 VLA 在出动作时同步预测进度 RTG、下一语义事件 ETG 和动作不确定性，并让这些显式状态反过来条件化动作，而非事后生成解释。
- [Embodied Scene Rearrangement Planning](items/Embodied%20Scene%20Rearrangement%20Planning.md) — ESRP把家具重排改造成更接近真实部署的长时程任务：智能体只能看第一视角观测，却要对齐俯视目标布局，并处理物体相互遮挡。
- [Rapid On-Robot Learning for Dynamic Manipulation Skills: Robot Juggling](items/Rapid%20On-Robot%20Learning%20for%20Dynamic%20Manipulation%20Skills%20Robot%20Juggling.md) — 该工作让双臂机器人在真机上几分钟内学会多种三球杂耍：局部记忆模型吸收新经验，原有全局模型负责稀疏区域外推，再用互相可达集合约束连续抛接安全。

## 其余存档 12 篇

- [Reconstructing Humans and Objects in Interaction using Large Reconstruction Models](items/Reconstructing%20Humans%20and%20Objects%20in%20Interaction%20using%20Large%20Reconstruction%20Mode.md) · 具身智能评测与基准
- [Tensegrity Continuum Robots Enable Task-Adaptive Morphologies for Cooperative Behaviors](items/Tensegrity%20Continuum%20Robots%20Enable%20Task-Adaptive%20Morphologies%20for%20Cooperative%20Be.md) · 多模态基础模型
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](items/Zero-WAM%20In-Context%20World-Action%20Modeling%20from%20Human%20Videos%20for%20Open-Ended%20Task.md) · 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Surgical Video Generation From Diffusion to World Models: A Survey](items/Surgical%20Video%20Generation%20From%20Diffusion%20to%20World%20Models%20A%20Survey.md) · 智能体 Agent 世界模型
- [Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation](items/Diffusion%20Policies%20for%20Short-Horizon%20Planning%20in%20Robot%20Crowd%20Navigation.md) · 多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- [Active sensing to characterize the heterogeneity of plant stress](items/Active%20sensing%20to%20characterize%20the%20heterogeneity%20of%20plant%20stress.md) · 智能体 Agent
- [Decoupling Planning and Control for Instructable Agents](items/Decoupling%20Planning%20and%20Control%20for%20Instructable%20Agents.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- [Memory Anchors for Continual Robot Learning](items/Memory%20Anchors%20for%20Continual%20Robot%20Learning.md) · 机器人学习 具身智能评测与基准
- [WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression](items/WALL-SS%20Scaling%20Long-horizon%20World%20Models%20via%20Next-Scale%20Autoregression.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [4DStreamCtrl: Interactive Video Generation with Online 4D Control](items/4DStreamCtrl%20Interactive%20Video%20Generation%20with%20Online%204D%20Control.md) · 智能体 Agent 世界模型
- [DINOcular: Self-Supervised Visuospatial Representations](items/DINOcular%20Self-Supervised%20Visuospatial%20Representations.md) · 多模态基础模型 具身智能评测与基准
- [Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots](items/Cross-Platform%20Benchmark%20of%20Neural%203D%20Reconstruction%20for%20Autonomous%20Laboratory%20R.md) · 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2269
- 入选条目：24
- 回填已见条目：0
- 最高分论文：PredVLA: A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation
- 最高分论文发布时间：2026-08-27T06:27:11Z
- 主要技术对象分类：具身智能评测与基准 15、智能体 Agent 14、多模态基础模型 11、世界模型 10、视觉语言动作模型 VLA 10、机器人学习 8、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
