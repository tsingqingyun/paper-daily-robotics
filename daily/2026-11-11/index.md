---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-11
---

# 2026-11-11 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：机器人缺的究竟是哪种学习信号，以及怎样确认它真的学会了。先读“机器人棋子搬运”，理解为什么离线误差和未经降学习率的检查点会误导选择；再读 PAIR，看怎样把相机几何与机器人状态变成互补监督；若关心少示范学习，读 WICL，重点检查仿真排练如何转成可迁移的任务记忆，以及部署时的信息边界。
> **趋势**：前五篇的共同线索：这些论文都在给视觉补上任务需要的依据：相机射线、接触区域、温度属性或环境反馈。共同启示是，增加输入或数据量只是起点，还要明确它如何参与学习，并用实际任务成功率检查效果；这些工作尚不能共同证明某一种机制普遍最优。

- **规模**：2548 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、多模态基础模型 17、世界模型 14、视觉语言动作模型 VLA 13、智能体 Agent 12、机器人学习 8
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation](items/PAIR%20Proprioception-Aligned%20Image-Ray%20Representations%20for%20Viewpoint-Robust%20Manip.md)

> PAIR 要解决的是：相机换个位置，机器人就不会操作了。它把图像与相机射线一起编码，再用机械臂自身状态判断哪些观测应该接近，让模型学会跨视角认出相近的机器人配置。

- **能借鉴什么**：值得借鉴的是：先让表示知道“这个像素从哪里看过来”，再要求它跨视角一致。已有相机标定和机器人状态、且部署视角会变化时，这比单独要求图像不变更有依据。
- **值得读吗**：值得读方法和消融：重点是射线与本体状态如何互相补足，而最高检查点口径需要在比较时保留。

<details><summary>实验依据</summary>

仿真覆盖 MimicGen、双臂 AlohaGym 和语言条件 LIBERO。LIBERO 中，SmolVLA 的平均成功率从无射线 BC 的 81.4%、有射线 BC 的 83.3%，升至 PAIR 加射线的 88.9%；结果采用三个种子、每种子五个检查点中的最高成功率。[S34](https://arxiv.org/html/2611.11798v1#S4.T4) [S35](https://arxiv.org/html/2611.11798v1#S4.T4.8.1) 真机为 FR3 三项桌面任务，每项每设置测试 30 次，最终完成率平均 57.8%，比无射线 BC 高 26.7 个百分点。[S39](https://arxiv.org/html/2611.11798v1#S4.SS6.p1.1) 这些支持所测相机变化下的收益，不能外推到任意遮挡或持续移动相机。

</details>

### 2. [SurgTAP-3D: A Large-Scale Cross-Surgery Video Dataset with Contact-Aware 3D Motion Tracking](items/SurgTAP-3D%20A%20Large-Scale%20Cross-Surgery%20Video%20Dataset%20with%20Contact-Aware%203D%20Motio.md)

> SurgTAP-3D 把未标定的单目手术视频加工成器械与组织随时间运动的伪三维轨迹。关键是先利用已有模型估计，再通过几何和运动约束纠正漂移，同时把标注重点放在可见的器械接触区域。

- **能借鉴什么**：可借鉴的是把基础模型当成可修正的标注助手：先批量生成初值，再用领域约束筛掉不一致运动。对难以获取真实三维标注的视频，这提供了扩大监督规模的路线。
- **值得读吗**：值得读标注流程和评测协议，尤其要先弄清伪三维的精度与尺度，再决定如何用它监督模型。

<details><summary>实验依据</summary>

数据包含 519,642 帧、4,549 个片段和 1,376,987 条轨迹，来自多种真实体内手术。[S3](https://arxiv.org/html/2611.11697v1#S1.T1.24) 在 SurgT、SurgPose、STIR 上，平均 AJ3D 为 56.57，TAPNext 为 55.69；平均 APD3D 为 64.77，对比 62.88。[S16](https://arxiv.org/html/2611.11697v1#S4.T4.4.1) 优势并非所有指标都有，例如平均遮挡准确率低于 AllTracker。这些结果支持所测点跟踪性能；提供材料未给指标阈值、完整尺度对齐规则或置信区间，不能据此认定具有毫米级临床精度。

</details>

### 3. [VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess](items/VLA%20Adaptation%20with%20Real%20and%20Simulated%20Data%20A%20Case%20Study%20on%20Robotic%20Chess.md)

> 这篇用 π₀.₅ 搬棋王，研究示范量、训练时长、检查点选择和仿真预训练怎样影响实际成功率。最值得记住的是：先把学习率降下来再比较模型，而且离线动作误差不能可靠替代闭环执行。

- **能借鉴什么**：可以直接借鉴评估顺序：先统一训练收尾方式，再看闭环成功率，最后判断更多数据或更复杂学习方法是否值得。否则，优化状态差异可能被误读为数据或算法差异。
- **值得读吗**：值得细读训练分支和评估协议；它对实验怎么做的提醒，比搬棋任务本身更容易迁移。

<details><summary>实验依据</summary>

仿真每模型使用同一组 1,000 次闭环试验。10k 示范、165k 更新时，降学习率模型成功率 60.2%，恒定学习率为 48.9%；237k 更新达到 64.1%。[S21](https://arxiv.org/html/2611.12676v1#S3.SS1.p4.1) [S40](https://arxiv.org/html/2611.12676v1#A2.T1.2) 真机 128 条示范、45k 更新时，仿真初始化成功 18/25 次，基础初始化为 2/25 次。[S41](https://arxiv.org/html/2611.12676v1#A2.T2.2) 自身回放、自动纠错和残差强化学习未带来稳定收益。[S30](https://arxiv.org/html/2611.12676v1#S3.SS2.p4.1) [S31](https://arxiv.org/html/2611.12676v1#S3.SS2.p5.1) 这支持该任务中的训练选择，不能推广为所有 VLA 的排序。

</details>

### 4. [Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation](items/Thermo-VLA%20A%20Thermal-Aware%20Vision-Language-Action%20Model%20with%20Gated%20Residual%20Modu.md)

> Thermo-VLA 让机器人根据温度选对操作对象，而不是只把热成像当成另一张图片。它用 ThermoRes Encoder 提取冷、热属性，再由语言控制这些信息如何补进 RGB 表示，随后生成连续动作。

- **能借鉴什么**：当新增传感器主要帮助判断“选哪个”，可以尝试让它修正已有视觉表示，而不是全面重写控制输入。本文的残差置零实验尤其有用：它检查了新增信息影响的是目标选择还是基本动作。
- **值得读吗**：值得读融合机制与消融；它给出了属性如何进入动作策略的可检查解释，但精细温度比较仍是明显短板。

<details><summary>实验依据</summary>

真机为双臂 Unitree G1，六任务共 1,307 条专家示范，每指令测试 20 次。[S15](https://arxiv.org/html/2611.11981v1#S4.SS1.SSS1.p1.1) 摘要报告四项温度任务平均成功率 0.86，比直接加入热图的 π₀.₅ 高 18 个百分点；相对温度咖啡任务仅 0.58。[S13](https://arxiv.org/html/2611.11981v1#S4.T2.4.1) 小目标测试中去掉门控，成功率由 0.85 降至 0.60；热残差置零后，温度任务接近随机二选一，但仍能抓放。[S22](https://arxiv.org/html/2611.11981v1#S4.SS3.p1.1) [S23](https://arxiv.org/html/2611.11981v1#S4.SS3.p2.1) [S24](https://arxiv.org/html/2611.11981v1#S4.T4) [S25](https://arxiv.org/html/2611.11981v1#S4.T4.2) 消融支持残差参与目标选择，不能仅凭注意力图认定其具有人类式推理。

</details>

### 5. [World In-Context Learning for Agentic Robot Manipulation](items/World%20In-Context%20Learning%20for%20Agentic%20Robot%20Manipulation.md)

> WICL 让冻结模型从一次示范出发，在仿真中反复练习，把反馈写进上下文里的 Task Memory，而不更新网络权重。RoboScript 再把这份记忆带到新场景执行，尝试迁移任务步骤和物体角色，而不是记住原场景长相。

- **能借鉴什么**：值得借鉴的是把任务经验保存成可迁移的执行知识，而非只依赖参数更新。若能方便地试错、任务又能用步骤和物体角色表达，上下文记忆可能成为适应新任务的另一种成本选择；是否划算还取决于排练和模型调用开销。
- **值得读吗**：值得继续读方法和评测协议；核心主张很明确，但目前摘要不足以判断优势来自记忆学习、工具接口还是不同的交互预算。

<details><summary>实验依据</summary>

摘要报告：RoboTwin 2.0 全部 50 项任务，每任务一次示范、无梯度更新，干净与随机化设置平均成功率 83.4%，比最强受训动作策略高超过 20 个百分点。还报告跨视觉分布、反思收益、基础模型扩展和物理双臂迁移，但未给具体对比模型、试验次数、排练成本或真机成功率。这些支持一个值得核查的仿真结果，不能把 83.4% 当成真机表现。

</details>

## 扫读 7 篇

- [Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](items/Learning%20Heterogeneous%20Tactile%20Representation%20for%20General%20Dexterous%20Manipulation.md) — LingBot-Touch 想让机器人更换触觉传感器后，仍能使用同一类触觉表示。它把压阻、磁性和视触觉传感器的数据变成统一的触觉 token，再交给动作策略使用。
- [Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos](items/Compass%201%20Towards%20Open-World%20and%20Persistent%20Embodied%20Navigation%20from%20Monocular%20R.md) — Compass 1 让导航机器人利用较长时间前看过的场景，而不只盯着最近几帧。它用稀疏关键帧和显式历史地图保存线索，再通过三类问答监督训练模型使用这些线索。
- [Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation](items/Decoupled%20Asynchronous%20System%20for%20Humanoids%20%28DASH%29%20Latency-Agnostic%20Scaling%20of%20V.md) — DASH 把慢速理解和快速动作生成拆开并发运行，让大模型算得慢时机器人仍能及时控制。动作头同时接收较旧的语义和自己读取的最新视觉，并在训练中学习应对这种时间差。
- [$Σ$-LeWM: Learning World Models via S-Information for Robot Control](items/%24%CE%A3%24-LeWM%20Learning%20World%20Models%20via%20S-Information%20for%20Robot%20Control.md) — Σ-LeWM 在 LeWorldModel 原有的“预测下一状态”训练之外，再要求表示能预测过去状态、反推动作。它希望让压缩后的状态保留更多与控制有关的信息，从而改善规划表现和效率。
- [VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation](items/VLA-MOPD%20On-Policy%20Distillation%20for%20Multi-Task%20VLA%20Policy%20Consolidation.md) — VLA-MOPD 把多个流匹配 VLA 专家合成一个学生，并让专家在学生实际遇到的观察上指导它。指导不仅针对最终动作，还覆盖动作生成过程中的中间状态。
- [Embodied First Exam](items/Embodied%20First%20Exam.md) — Embodied First Exam 要检查的是：会写代码的智能体，能否在机器人持续行动、信息有限、不能随意重来的条件下完成任务。它允许智能体自己选择直接控制、写控制代码或训练策略，再通过不同权限和时间条件检验能力。
- [SPARK: Simple Post-training for Adapting pRetrained Knowledge to Robot Control](items/SPARK%20Simple%20Post-training%20for%20Adapting%20pRetrained%20Knowledge%20to%20Robot%20Control.md) — SPARK 把现成视觉基础模型继续训练成更适合机器人控制的编码器：既保留物体和场景的语义，也让紧凑特征保留动作相关的时间变化。巧处是同时约束“适应控制”和“保住旧知识”，避免只顾其中一头。

## 其余存档 12 篇

- [When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary](items/When%20Coding%20Agents%20Get%20Arms%20Safety%20Risks%20Across%20the%20Digital-Physical%20Boundary.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Gemini Robotics 2.5 accelerates real-world general dexterity](items/Gemini%20Robotics%202.5%20accelerates%20real-world%20general%20dexterity.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [An Evaluation of Tabular Foundation Models as Training-Free World Models](items/An%20Evaluation%20of%20Tabular%20Foundation%20Models%20as%20Training-Free%20World%20Models.md) · 多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation](items/Kimodo-Policy%20Learning%20Kinematic%20Action%20Models%20for%20Humanoid%20Loco-Manipulation.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA
- [Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation](items/Bridging%20Task%20Planning%20and%20Execution%20for%20Language-Conditioned%20Bimanual%20Manipulat.md) · 多模态基础模型 智能体 Agent
- [Be My Eye: Learning to See Beyond a Robot's Own Perspective](items/Be%20My%20Eye%20Learning%20to%20See%20Beyond%20a%20Robot%27s%20Own%20Perspective.md) · 多模态基础模型 视觉语言动作模型 VLA
- [GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation](items/GeoMind%20A%20Benchmark%20for%20Spatial%20Understanding%20in%20Robotic%20Manipulation.md) · 智能体 Agent 具身智能评测与基准
- [Benchmarking Real-World Robotic Manipulation through Stochastic Challenges](items/Benchmarking%20Real-World%20Robotic%20Manipulation%20through%20Stochastic%20Challenges.md) · 世界模型 具身智能评测与基准
- [How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens](items/How%20Many%20Candidates%20Does%20a%20One-Step%20World%20Model%20Need%20A%20Random-Codebook%20Account%20o.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [Flip Anything with Agentic Robotics Self-Learning](items/Flip%20Anything%20with%20Agentic%20Robotics%20Self-Learning.md) · 智能体 Agent 世界模型
- [ForeAct: Geometry-Guided Action Learning from World Representations](items/ForeAct%20Geometry-Guided%20Action%20Learning%20from%20World%20Representations.md) · 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- [LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data](items/LHNav%20Long-Horizon%20Humanoid%20Navigation%20via%20Multirate%20Coordination%20and%20Physics-Gr.md) · 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2548
- 入选条目：24
- 回填已见条目：0
- 最高分论文：PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation
- 最高分论文发布时间：2026-11-09T02:54:44Z
- 主要技术对象分类：具身智能评测与基准 18、多模态基础模型 17、世界模型 14、视觉语言动作模型 VLA 13、智能体 Agent 12、机器人学习 8
- 信息源错误：0
- 自动恢复信息源：0

</details>
