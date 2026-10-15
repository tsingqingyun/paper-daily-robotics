---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-10-15
---

# 2026-10-15 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看两个问题：预测未来怎样真正参与动作生成，以及机器人同时做动作和语言任务时怎样守住控制频率。想理解前者，先读 WAVE-0，看预测的未来表征如何进入动作专家，再读 PINT，比较保留视频生成模型的收益与代价；想解决部署中的并发开销，读 OxyGen，它把问题落到共享观测的重复计算和解码预算上。两条路线的实验设置不同，不能直接按成功率排高低。
> **趋势**：前五篇的共同线索：PINT 和 WAVE-0 都让未来预测参与推理时的动作生成，但一个保留视频生成模型，一个只预测潜在表征。另一条共同线索是减少重复或多余的工作：UniLAP 推理时摆脱未来帧，OxyGen 则让并发任务复用观测计算。

- **规模**：4944 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 24、视觉语言动作模型 VLA 22、具身智能评测与基准 19、智能体 Agent 15、世界模型 13、机器人学习 8
- **源异常**：2
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation](items/SIMPLE%20Simulation-Based%20Policy%20Learning%20and%20Evaluation%20for%20Humanoid%20Loco-manipul.md)

> SIMPLE 搭了一套让人形机器人同时练移动和操作、并接受统一测试的仿真环境：用 MuJoCo 算接触和运动，用 IsaacSim 生成逼真图像。它还提供自动规划和 VR 示教两条采集路线，让训练数据和评测可以在同一套环境中开展。

- **能借鉴什么**：可借鉴的是把“便于接触控制的动力学”和“适合视觉策略的画面”分开承担，再组成统一的数据与测试入口。如果研究的问题同时受身体运动、接触和视觉影响，这比只增加桌面物体种类更贴近实际瓶颈。
- **值得读吗**：值得读到环境接口、数据采集和仿真对真机验证部分；它的关键价值取决于测试条件能否复用，以及仿真结果能多可靠地指导真机选择。

<details><summary>实验依据</summary>

摘要给出规模：16 类全身任务、50 个室内场景、超过 1,000 个物体资产；评测涵盖轻量模仿网络、VLA 和 WAM。作者报告仿真与真机表现强相关，并称仿真数据训练的策略可在相似设置下零样本迁移到真机。但摘要未给策略名称、成功率、相关系数、真机试验次数或误差范围，因此支持的是路线可行，尚不足以量化仿真排名的可靠程度。

</details>

### 2. [UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation](items/UniLAP%20A%20Unified%20Latent%20Action%20Policy%20for%20Cross-Embodiment%20Manipulation.md)

> UniLAP 把从无动作标签视频中学到的运动知识，变成推理时可以直接使用的连续潜在动作策略。关键是向 LAM 教师学习动作表征，同时保留多种可行动作，并尽量把真正的运动与无关画面变化分开。

- **能借鉴什么**：这里值得借鉴的是将“视频中有什么在动”与“画面长什么样”分开学习。若希望多个身体共享运动知识，减少背景、纹理等信息进入动作表征，可能比单纯扩大视频预训练更切中迁移障碍；是否有效仍需消融验证。
- **值得读吗**：值得深入读蒸馏目标、运动目标构造和平台适配接口；能否把视频知识稳定转成精细控制，是比总榜成绩更关键的判断点。

<details><summary>实验依据</summary>

摘要称模型以 1.1B 参数在多来源视频上预训练，并在手部姿态预测、单臂操作、人形机器人操作和真机部署中超过先进潜在动作与 VLA 基线。但没有提供基线名称、数据量、指标数值或适配预算。现有证据只能支持作者报告了跨任务优势，无法判断优势大小，也不能据此断定新平台适配成本低。

</details>

### 3. [OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism](items/OxyGen%20Unified%20KV%20Cache%20Management%20for%20VLA%20Inference%20under%20Multi-Task%20Parallelis.md)

> OxyGen 让机器人做动作、说话等并发任务时，共用已经算过的观测缓存，并把尚未说完的语言请求接着往后排。这样既减少重复计算，又给每帧动作控制留出计算预算。

- **能借鉴什么**：可借鉴的思路是：多任务不一定要为每条输出重复处理同一幅图像。对共享输入、截止时间不同的请求，先复用计算，再按控制周期安排剩余生成工作，可能比单独加速每个任务更有效。
- **值得读吗**：如果关心多任务 VLA 上机部署，值得读到缓存兼容条件和调度实现；摘要已给明确系统收益，但还需用尾部延迟判断控制可靠性。

<details><summary>实验依据</summary>

摘要在 RTX 4090 和 Jetson AGX Thor 上评测 π₀.₅，报告相对独立执行最高 3.7 倍加速；在 RTX 4090 上同时实现超过 200 tokens/s 的语言吞吐和 70 Hz 动作频率。另在 Xiaomi-Robotics-0、StarVLA 上验证，并展示搭载 Thor 的人形机器人推理收益。摘要未给各硬件完整结果、延迟分布或任务成功率，不能把 4090 数字归给机器人板载实验。

</details>

### 4. [PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation](items/PINT%20A%20Unified%20Model%20with%20Shared%20Predictive%20Intent%20for%20Robot%20Manipulation.md)

> PINT 让语言理解、未来视频预测和动作生成围绕同一份“接下来这段动作要做什么”的内部表示协作，同时保留各自的处理路径。推理时视频模型仍在运行，动作专家可以读取它的表征。

- **能借鉴什么**：这里可借鉴的是给不同专家一个共同的短期执行表示，让各自的预测目标约束它。如果模块融合后反而难以利用原有能力，可以尝试明确的信息接口，而不是继续增加层间共享。
- **值得读吗**：值得读懂两阶段训练和单向信息流，再决定是否深入复现；结果支持这种协作方式有潜力，但真机 OOD 与计算开销仍需权衡。

<details><summary>实验依据</summary>

摘要报告：RoboTwin 2.0-Hard 上 PINT 为 15.5%，Fast-WAM 为 1.8%、StarVLA 为 3.2%；LIBERO-Plus 上分别为 79.5%、51.5%、75.0%。五个真机双臂任务中，PINT 的 ID/OOD 成功率为 68%/24%，预训练 Motus 为 35%/9%，预训练 π₀.₅ 为 67%/35%。因此 PINT 真机 OOD 并未超过 π₀.₅。作者称其未做具身预训练，但这不等于未使用预训练视觉语言和视频模型。

</details>

### 5. [WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction](items/WAVE-0%20Bridging%20VLA%20Policies%20and%20WAMs%20with%20Lightweight%20Latent%20Future%20Prediction.md)

> WAVE-0 在预训练 VLA 中加入一个轻量世界模型：先把潜在动作计划转成预测的未来表征，再让动作专家参考这个未来生成动作。它不必生成视频像素，也不需要为这个世界模型做大规模视频预训练。

- **能借鉴什么**：可借鉴的是先问动作需要哪种未来信息，再决定是否必须生成完整视频。若紧凑表征足以指导动作，预测表征可能是利用后果信息的较省计算路线；仍需确认它学到的是可区分动作后果的动态，而不只是场景特征。
- **值得读吗**：值得优先读方法与消融：它把未来预测接入动作生成的路径很明确，真机增益也具体；复现前应核查排序目标和新增推理成本。

<details><summary>实验依据</summary>

摘要报告成功率：RoboTwin 2.0 为 91.47%，LIBERO 为 98.7%，LIBERO-Plus、Pro、Para 分别为 88.0%、61.4%、75.0%。真机任务中，π₀.₅ 从 38.3% 提高到 73.3%。这些结果支持所测操作任务上的效果，但摘要未给各仿真基线、试验次数、误差范围与推理延迟，也不能与其他论文中不同设置的数字直接排名。

</details>

## 扫读 7 篇

- [UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](items/UniT%20Toward%20a%20Unified%20Physical%20Language%20for%20Human-to-Humanoid%20Policy%20Learning%20an.md) — UniT 想让人类示范教会人形机器人动作，关键是用动作造成的视觉变化连接两种不同身体。它把这种联系压成共享动作令牌，供机器人策略和视频世界模型使用。
- [MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation](items/MedVLA%20A%20Hierarchical%20Vision-Language-Action%20Framework%20for%20Closed-Loop%20Precision.md) — MedVLA 把精密医疗操作拆成高层判断和受约束的函数执行，让模型除了决定怎么动，也能调用系统功能。它用生成的技能推理数据训练这种分工，并报告柔性电极植入闭环试验的成功率。
- [METIS: Multi-Source Egocentric Training for Integrated Dexterous Vision-Language-Action Model](items/METIS%20Multi-Source%20Egocentric%20Training%20for%20Integrated%20Dexterous%20Vision-Language-.md) — METIS 用多来源的人类与机器人第一视角数据预训练灵巧操作模型。它先把数据整理到一致动作空间，再提取紧凑的离散运动表示，让 VLA 从这些表示中学习动作。
- [SEAR: Self-Evolving Agentic Robotics](items/SEAR%20Self-Evolving%20Agentic%20Robotics.md) — SEAR 让语言模型写控制代码、在线控制或自行微调 VLA，并保留有效技能和经验。它更关键的贡献是检验：后续任务做得更好，究竟来自经验积累，还是更多重试和计算时间。
- [AnolisVLA: Lightweight Vision-Language-Action Model with Deep State Space Models for Mobile Manipulation](items/AnolisVLA%20Lightweight%20Vision-Language-Action%20Model%20with%20Deep%20State%20Space%20Models.md) — AnolisVLA 用深度状态空间模型处理视觉和语言序列，减少 VLA 生成动作轨迹的计算负担。摘要报告它在移动操作中同时取得更高成功率和更快推理。
- [Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models](items/Towards%20Long-horizon%20Embodied%20Agents%20with%20Tool-Aligned%20Vision-Language-Action%20Mo.md) — VLAs-as-Tools 让高层模型负责安排长任务，让多个专门的 VLA 工具各做一段局部操作。关键是把工具选择、调用指令和执行进度接起来，使规划器能在需要时调整计划。
- [SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos](items/SeeTraceAct%20Visibility-Aware%20Latent%20Planning%20from%20Cross-Embodiment%20Demonstration.md) — SeeTraceAct 让机器人看一次示范视频后执行新任务，重点解决“小目标到底在哪里”的问题。它通过考虑可见性的未来末端轨迹预测，让动作学习更明确地关注操作位置。

## 其余存档 12 篇

- [Flow-based Policy Adaptation without Policy Updates](items/Flow-based%20Policy%20Adaptation%20without%20Policy%20Updates.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation](items/Let%20the%20Mind%20Conceive%2C%20Let%20the%20Hand%20Achieve%20Following%20Multimodal%20Instructions%20fo.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [NeuroVLA: A Brain-inspired Embodied Intelligence for Fluid and Fast Reflexive Robotics Control](items/NeuroVLA%20A%20Brain-inspired%20Embodied%20Intelligence%20for%20Fluid%20and%20Fast%20Reflexive%20Rob.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- [RoboHarness: A Simple Harness Outperforms VLA and World Actions Models](items/RoboHarness%20A%20Simple%20Harness%20Outperforms%20VLA%20and%20World%20Actions%20Models.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- [Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies](items/Axiom-0%20Hierarchical%20Self-Refinement%20for%20Vision-Language-Action%20Policies.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA](items/Listen%20Before%20Act%20Audio-Conditioned%20Robot%20Manipulation%20with%20ListenVLA.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems](items/World-Value-Action%20Model%20Implicit%20Planning%20for%20Vision-Language-Action%20Systems.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [WireCraft: A Simulation Benchmark for Industrial DLO Manipulation](items/WireCraft%20A%20Simulation%20Benchmark%20for%20Industrial%20DLO%20Manipulation.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](items/Agentic%20Real2Sim%20Physics-based%20World%20Modeling%20with%20Vision-Language%20Agents.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies](items/Think%20Like%20a%20World%20Model%2C%20Act%20Like%20a%20VLA%20Distilling%20World-Model%20Representations.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [ASENA: Self-evolving Agents for Embodied Navigation](items/ASENA%20Self-evolving%20Agents%20for%20Embodied%20Navigation.md) · 多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- [Video Prediction Policy 2: Predict Better, Act Better](items/Video%20Prediction%20Policy%202%20Predict%20Better%2C%20Act%20Better.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：4944
- 入选条目：24
- 回填已见条目：0
- 最高分论文：SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation
- 最高分论文发布时间：Wed, 14 Oct 2026 00:00:00 -0400
- 主要技术对象分类：多模态基础模型 24、视觉语言动作模型 VLA 22、具身智能评测与基准 19、智能体 Agent 15、世界模型 13、机器人学习 8
- 信息源错误：1
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: HTTP Error 429: Unknown Error (after 1 attempts); recovered via 4/4 configured fallback feeds

### 信息源错误

- OpenAI News: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
