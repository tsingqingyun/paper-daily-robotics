---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
created: 2026-09-03
---

# 2026-09-03 AI Embodied Intelligence Update

> [!summary] 今日判断
> 今天最值得看的是三条互补路线：用受控实验厘清跨本体 VLA 的有效因素，用视频规模化与接触预测增强机器人策略，以及把长程执行改造成带前置检查、结果验证和恢复的闭环。与此同时，多篇基准论文共同提醒：标准榜单上的高分不等于部署能力，几何恢复、终止协议、安全探索和恶劣条件鲁棒性仍是明显短板。
> **趋势**：共同趋势是从单次动作预测转向“可验证、可适应、可部署”的闭环系统，并把世界模型、几何表征和内部信号引入决策。评测也正从干净单域成功率扩展到跨本体、跨域、长程状态、接触、安全与真实硬件约束。

- **规模**：2279 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 20、多模态基础模型 14、智能体 Agent 12、世界模型 11、视觉语言动作模型 VLA 10、机器人学习 4、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation](items/ZETA%20A%20Controlled%20Study%20of%20Zero-Shot%20Cross-Embodiment%20VLA%20Transfer%20for%20Tabletop.md)

> ZETA 把零样本跨本体迁移拆成严格零样本与预训练见过目标本体两种情形，并用受控基准隔离本体变化。结果表明，局部末端执行器表征、源本体多样性和辅助共训练都是明确有效的杠杆。

- **为什么值得读**：它为 VLA 和具身评测研究者提供了更可信的跨本体报告规范，也给出数据配比与动作表征设计的直接经验，能减少把预训练泄漏误当作真正零样本能力的风险。
- **证据**：局部 EEF 状态—动作表征、源本体多样性和辅助共训练分别带来约15、18和7个百分点提升；预训练中加入5%目标本体数据，使平均任务进度提高13.4个百分点。
- **判断**：值得精读实验设计和变量控制部分；它的主要价值不是新模型，而是把跨本体 VLA 的概念与证据做得可比较。

### 2. [Towards Zero-Shot Transfer Across Embodiments For Driving VLAs](items/Towards%20Zero-Shot%20Transfer%20Across%20Embodiments%20For%20Driving%20VLAs.md)

> 论文研究驾驶 VLA 对未见数据集和相机布局的零样本迁移，并提出 BEV-Forcing，用共享鸟瞰空间接口把地面物体布局知识注入 VLA。该辅助目标在训练相机布局较少时有效，但随本体多样性增加而收益减弱。

- **为什么值得读**：对驾驶 VLA 研究者，核心价值是提醒辅助几何目标必须与数据规模联合评估，不能只在小规模设置中证明有效后便宣称可扩展。
- **证据**：摘要报告 BEV-Forcing 在训练相机布局较少时同时改善分布内和分布外性能，并称随着训练本体增加，辅助目标收益下降；未给出可核查的结果数字。
- **判断**：值得读实验曲线和数据规模分析；BEV-Forcing 本身直观，真正有判断价值的是其收益随训练多样性衰减的证据。

### 3. [Monocular Depth Estimation from a Single Image: Progress and Opportunities](items/Monocular%20Depth%20Estimation%20from%20a%20Single%20Image%20Progress%20and%20Opportunities.md)

> 这篇综述系统梳理单目深度从早期学习方法到基础模型的演进，区分相对深度与度量深度，并以判别式、生成式两类组织近期方法。它还连接数据集、合成数据、视频深度及机器人感知应用。

- **为什么值得读**：对世界模型和具身研究者，它可用于判断深度模块究竟提供相对结构还是可用于控制的度量几何，并快速定位预训练、合成数据和视频一致性相关路线。
- **证据**：这是综述；摘要称包含代表模型的定量基准和定性比较，但未给出可核查的结果数字。
- **判断**：适合先通读分类、数据集和开放问题，做深度方向入门或选型索引；具体模型优劣仍应回到原论文和统一评测。

### 4. [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](items/EmbodiedSkills%20A%20Unified%20Framework%20for%20Orchestrating%2C%20Training%2C%20and%20Deploying%20VL.md)

> EmbodiedSkills 不把技能选择直接当作可执行命令，而是当作提案：执行前检查前置条件，执行后验证结果，失败则恢复。统一的可执行技能接口把高层规划、有限时长 VLA 执行和验证串成闭环。

- **为什么值得读**：它给 Agent 与 VLA 研究者一个可检查、可训练的系统边界，也能把执行日志转为组件监督；尤其适合研究长程失败究竟来自规划、前置条件、控制还是验证。
- **证据**：以 Qwen3-VL 和 OpenPI/pi0.5 实例化；适配后的低层策略在50个 RoboTwin 2.0任务上平均成功率86.20%，在四个 LIBERO 套件上97.40%，但在4个依赖记忆的 RMBench 任务上仅12.5%。
- **判断**：值得精读接口、验证和恢复机制，但评审时必须把低层策略成绩与完整 EmbodiedSkills 的增益分开看。

### 5. [Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs](items/Knowing%20When%20to%20Stop%20Adaptive%20Action%20Chunking%20via%20Internal%20Cross-Attention%20Dynam.md)

> 论文用 VLA 动作专家内部的交叉注意力熵判断“什么时候该停下当前动作块”。其训练-free 截断器检测持续高熵平台，动态缩短缺乏观测支撑的开环执行。

- **为什么值得读**：对 VLA 部署很实用：它把模型内部注意力变成执行置信信号，可在不重训策略的情况下改善闭环频率，并为研究模型自我监控提供入口。
- **证据**：在 π0.5、X-VLA，RoboTwin 2.0、LIBERO及3个真实操作任务上，平均成功率优于固定 horizon 和其他自适应分块基线，同时保持高效闭环控制；摘要未给出具体增益数字。
- **判断**：值得精读算法和真实机器人结果；若阈值无需任务级调参，这会是很容易接入现有 VLA 的实用改进。

## 扫读 7 篇

- [Latent Cluster Analysis for Vision-Language-Action Models](items/Latent%20Cluster%20Analysis%20for%20Vision-Language-Action%20Models.md) — LAVLA 用聚类分析解释 VLA 隐空间，并以交叉注意力给嵌入加权，突出与动作有关的特征。对 GR00T N1.5 的逐层分析显示，时空和运动学概念在中层逐渐细化、靠近输出时趋稳。
- [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](items/Facet-0%20A%20Robotic%20Foundation%20Model%20for%20Contact-Rich%20Precise%20Manipulation.md) — Facet-0 面向亚毫米装配，不只预测动作，还预测动作将引发的腕部力／力矩，并用 Action-Wrench Critic 区分进度相似但接触后果不同的动作。它再通过受限轻量 actor 做在机适配。
- [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](items/REFACTOR-VLA%20Unsupervised%20Library%20Learning%20of%20Typed%20Motor%20Programs.md) — REFACTOR-VLA 用 wake/sleep 机制从动作片段中无监督归纳可复用、带类型的运动程序。睡眠阶段借助潜在世界模型的 Behavioral-Equivalence Kernel 判断行为等价，清醒阶段则让动作解码器消费类型化 lambda term。
- [ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training](items/ZimaBlue%20Evolving%20Generalizable%20World%20Action%20Models%20through%20Scalable%20Video%20Pre-t.md) — ZimaBlue 把大规模无动作第一视角视频转成机器人控制能力：先做因果具身视频预训练，再以异构机器人轨迹完成视频—动作落地，最后适配目标机器人。Slow-Fast 双系统让大型世界模型提供表征、轻量分支以30 Hz出动作。
- [Provably Safe Sim-to-Real Transfer](items/Provably%20Safe%20Sim-to-Real%20Transfer.md) — 论文把安全 Sim2Real 表述为 reward-free safe RL：先利用不完美模拟器减少真实交互，再在安全约束下探索，最终可针对任意奖励求近最优可行策略。其理论界用仿真—现实偏差刻画模拟器究竟省了多少真实样本。
- [Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching](items/Evaluating%20Multimodal%20LLMs%20as%20Generalist%20Vision-Language-Action%20Agents%20for%20Drone.md) — DroneCATS-Agent 直接让多模态大模型通过提示声明的动作空间控制无人机，并用 DroneCATS 分别测试接近、跟踪、搜索和多机指挥。结果显示主要失败并非飞行，而是持续遵守动作协议和正确宣布结束。
- [HINT: Human-Intent Inception for Long-Horizon Robot Manipulation](items/HINT%20Human-Intent%20Inception%20for%20Long-Horizon%20Robot%20Manipulation.md) — HINT 在长程操作中只在操作模式切换时调用语义推理，选定子任务与目标后，通过多视角 grounding 和跟踪持续保持该意图。它用图像语义高亮或注意力先验把意图传给动作策略，无需改动基础动作模型参数。

## 其余存档 12 篇

- [Towards Generalizable Visually Grounded Exploration of Household Devices](items/Towards%20Generalizable%20Visually%20Grounded%20Exploration%20of%20Household%20Devices.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [Toward Robust LiDAR Semantic Segmentation for Real-World Deployment: Evaluation under Coarse Labels, Adverse Conditions, and Domain Shifts](items/Toward%20Robust%20LiDAR%20Semantic%20Segmentation%20for%20Real-World%20Deployment%20Evaluation%20u.md) · [[具身智能评测与基准]]
- [Spatially Aware World Action Model via Geometric Latent Diffusion](items/Spatially%20Aware%20World%20Action%20Model%20via%20Geometric%20Latent%20Diffusion.md) · [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views](items/TAPVid-MV%20A%20Benchmark%20for%20Tracking%20Any%20Point%20in%203D%20Across%20Multiple%20Views.md) · [[世界模型]] [[具身智能评测与基准]]
- [A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference](items/A%20Survey%20on%20Self-Improving%20Test-Time%20Intelligence%20Feedback-Driven%20Adapting%2C%20Lear.md) · [[多模态基础模型]] [[智能体 Agent]]
- [Adaptive Depth-Map-Guided Bundle Adjustment for Correspondence-Free Multi-View Point Cloud Registration](items/Adaptive%20Depth-Map-Guided%20Bundle%20Adjustment%20for%20Correspondence-Free%20Multi-View%20P.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [AM-Bench: A Modular Simulation Suite and Benchmark for Aerial Manipulation Policy Learning](items/AM-Bench%20A%20Modular%20Simulation%20Suite%20and%20Benchmark%20for%20Aerial%20Manipulation%20Policy.md) · [[世界模型]] [[具身智能评测与基准]]
- [Beyond Object Selection:Markerless Gaze-based Robot Placement at Arbitrary Position](items/Beyond%20Object%20Selection%20Markerless%20Gaze-based%20Robot%20Placement%20at%20Arbitrary%20Posit.md) · [[具身智能评测与基准]]
- [Exploring Collaboration between a language and a non-language agent](items/Exploring%20Collaboration%20between%20a%20language%20and%20a%20non-language%20agent.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Discriminative World Models for Web Agents](items/Discriminative%20World%20Models%20for%20Web%20Agents.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [MV-dVRK: A Multi-Viewpoint Benchmark for Spatial Surgical Perception](items/MV-dVRK%20A%20Multi-Viewpoint%20Benchmark%20for%20Spatial%20Surgical%20Perception.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [Real-Time Dynamics-Based Torque-Sampling MPPI for Compliant and Force Aware Manipulation](items/Real-Time%20Dynamics-Based%20Torque-Sampling%20MPPI%20for%20Compliant%20and%20Force%20Aware%20Mani.md) · [[世界模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2279
- 入选条目：24
- 回填已见条目：0
- 最高分论文：ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation
- 最高分论文发布时间：2026-09-02T13:00:18Z
- 主要技术对象分类：具身智能评测与基准 20、多模态基础模型 14、智能体 Agent 12、世界模型 11、视觉语言动作模型 VLA 10、机器人学习 4、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
