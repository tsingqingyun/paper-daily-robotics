---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
created: 2026-09-09
---

# 2026-09-09 AI Embodied Intelligence Update

> [!summary] 今日判断
> 今天最值得精读的是三类工作：揭示机器人评测如何给出假阳性的语言迁移研究、通过测试时更新或示例检索实现适配的方法，以及拆解世界模型与动作学习关系的受控实验。硬件与系统侧也有扎实结果：相机可动性、通信预算和触觉传感器差异都会直接影响能力，不能只看模型成功率。
> **趋势**：共同趋势是把部署过程纳入方法设计：策略开始利用探索、检索、记忆修正和执行反馈持续调整行为。与此同时，研究越来越重视语言、视觉、动力学与硬件约束之间的接口，但不少摘要仍缺少足以判断收益来源的定量对照。

- **规模**：2300 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 20、多模态基础模型 14、世界模型 12、智能体 Agent 11、视觉语言动作模型 VLA 11、机器人学习 7
- **源异常**：1
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy](items/Measuring%20Language%20Transfer%20in%20Robot%20Policies%20Adding%20Greek%20to%20a%20Cosmos3%20Vision-L.md)

> 给 Cosmos3 VLA 加上希腊语，难点首先是证明机器人真的听懂了。论文通过错误指令对照、多随机种子和有区分力的任务集，发现双语训练有效，但离英语水平仍有明显距离。

- **为什么值得读**：对VLA本地化和具身评测最直接的价值，是提供检验策略是否真正利用语言的对照思路；世界模型研究者也应注意，语言适配的收益未必能迁移到动作策略。
- **证据**：单目标测试中，正确与错误希腊语指令得分分别为84.6%和82.6%。90任务评测中，希腊语单语训练最多超过对照2.7个百分点，双语训练稳定超过6.7—7.1个百分点，达到约四成英语性能；每任务7种措辞约减半措辞过拟合惩罚。语言适配世界模型热启动及解冻文本塔均使性能下降。
- **判断**：优先精读评测设计与负结果，它比单纯报告多语言成功率更能帮助排除虚假进展。

### 2. [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](items/Monkey%20See%2C%20Can%20Monkey%20Do%20A%20Benchmark%20for%20Evaluating%20Robot%20Skill%20Learning%20by%20Obs.md)

> RoboReel把“看人类视频学操作”放进统一考场，让不同方法可以公平比较。它同时提供人类视频、仿真机器人轨迹和测试环境，重点检验干扰鲁棒性与长任务能力。

- **为什么值得读**：适合机器人学习和VLA研究者用来比较人类视频利用方式，尤其能检验方法是否只在短任务或宽松执行条件下有效。
- **证据**：摘要报告覆盖超过7种先进算法及VLA变体，发现长时程和低容错操作仍然困难；摘要未给出可核查的结果数字。
- **判断**：做人类视频模仿学习值得精读协议与基线实现，其他方向可先读任务设计和失败分析。

### 3. [WorldAgen: Unified State-Action Prediction with Test-Time World Model Training](items/WorldAgen%20Unified%20State-Action%20Prediction%20with%20Test-Time%20World%20Model%20Training.md)

> WorldAgen让VLA进入新环境后先探索、再用真实状态变化更新世界模型，以改善动作预测。关键是世界预测与动作预测共享骨干，使部署时学到的环境信息能够影响策略。

- **为什么值得读**：为世界模型如何实际帮助VLA部署适配提供了具体路径：利用新环境转移更新预测能力，再观察动作收益。
- **证据**：在CALVIN和LIBERO上，基础模型与先进方法相当或部分更优；摘要称少量样本的测试时训练进一步超过现有先进模型。摘要未给出可核查的结果数字。
- **判断**：值得精读适配协议和信息流设计，但“少量更新即领先”的强度需要结果表支撑。

### 4. [ComVLA: Communication-Aware Split Inference for VLA Models in 6G-Connected Robotics](items/ComVLA%20Communication-Aware%20Split%20Inference%20for%20VLA%20Models%20in%206G-Connected%20Roboti.md)

> ComVLA根据任务指令挑选关键视觉token，再按无线链路容量决定传多少。它让云端VLA少看大量冗余信息，以小幅成功率损失换取计算和延迟下降。

- **为什么值得读**：对需要云端推理的VLA系统具有直接价值，给出了通信预算、推理成本和任务成功率之间可量化的取舍。
- **证据**：LIBERO上从512个token降至32个，相对OpenVLA-OFT计算量减少74%、推理延迟降低22%；平均成功率从96.9%降至95.4%，下降1.5个百分点，并在Rayleigh和Rician衰落条件下满足容量预算。
- **判断**：部署与系统方向值得精读实验设置，纯策略学习方向掌握语言引导的容量自适应机制即可。

### 5. [ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models](items/ICI-VLA%20In-Context%20Imitation%20with%20Spatiotemporally%20Aligned%20Demonstrations%20for%20Vi.md)

> ICI-VLA让固定策略在执行时检索几段与当前动作阶段、空间几何匹配的示范，再据此生成动作。适配靠上下文示例完成，无需现场更新策略参数。

- **为什么值得读**：为VLA少样本适配提供可操作的检索路线，也提示机器人示范库应按子任务阶段与几何关系组织，而不只按语言语义索引。
- **证据**：平均成功率为LIBERO 97.7%、RoboTwin 2.0 60.4%；后者超过最高已报告基线平均值19.3个百分点。在4项实体任务上达到83.2%。
- **判断**：优先精读检索构造与评测划分，固定策略下的收益及实体实验使它值得深入复现。

## 扫读 7 篇

- [DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination](items/DeCAL%20Towards%20Physically-Grounded%20Dexterous%20Vision-Language-Action%20Models%20via%20Co.md) — DeCAL面向遮挡严重、接触复杂的灵巧操作，让模型按接触状态选择如何使用触觉，并共同预测视觉与触觉变化。关键是把感知、动态想象和动作生成接入专门化专家。
- [Visible-Reachable Workspace for Perception-Aware Humanoid Design](items/Visible-Reachable%20Workspace%20for%20Perception-Aware%20Humanoid%20Design.md) — VRW衡量机器人在真正伸手操作的姿态下，目标是否也能被看见。论文用可独立转动的相机扩大“看得见且够得着”的区域，并减少为看清目标而产生的身体运动。
- [TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](items/TANGO%20Humanoid%20Navigation%20in%20Cluttered%20Environments%20with%20a%20Whole-Body%20Vision-Lan.md) — TANGO让人形机器人根据语言和第一视角图像，直接预测全身29自由度动作来穿过杂乱空间。它在仿真中合成可执行的全身穿行示范，学习手臂、躯干和步态的协调。
- [BIFTA: Brain-Inspired Few-Shot Tactile Adaptation for Unknown Sensors](items/BIFTA%20Brain-Inspired%20Few-Shot%20Tactile%20Adaptation%20for%20Unknown%20Sensors.md) — BIFTA用少量新传感器标注，修正冻结触觉编码器在陌生硬件上的特征关系。关键是支持集条件化图结构与不确定性门控传播，让可靠样本帮助其他预测。
- [PhysReal: Learning Real-World Deformable Object Physics via Hybrid Constitutive Modeling](items/PhysReal%20Learning%20Real-World%20Deformable%20Object%20Physics%20via%20Hybrid%20Constitutive%20M.md) — PhysReal从视频反推可变形物体的材料行为，再用物理仿真预测运动。它让解析材料模型负责物理先验，神经残差补足复杂响应，并允许物体不同位置具有不同材料性质。
- [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](items/OpenWAM%20An%20Open%2C%20Modular%20Exploration%20Towards%20Systematic%20World-Action%20Model%20Pretr.md) — OpenWAM把世界—动作模型拆成可替换模块，系统研究哪些生成先验、表示和信息流真正帮助控制。它据此训练OpenWAM-α，并提供基础设施、评测协议、模型和数据配方。
- [CLAMP: Constrained Decoding for Vision-Language Embodied Planning](items/CLAMP%20Constrained%20Decoding%20for%20Vision-Language%20Embodied%20Planning.md) — CLAMP在冻结VLM生成计划时，直接屏蔽不符合场景或动作规则的词元，并用状态前瞻偏向可达目标的方案。它把“计划是否可执行”变成解码过程中的约束。

## 其余存档 12 篇

- [Safe Task Planning with Long-Term Graph Memory for Embodied Agents](items/Safe%20Task%20Planning%20with%20Long-Term%20Graph%20Memory%20for%20Embodied%20Agents.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Bridging Language and Physics: Automated Design of Continuum Robots with Large Language Models](items/Bridging%20Language%20and%20Physics%20Automated%20Design%20of%20Continuum%20Robots%20with%20Large%20La.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Proxy Policy Steering](items/Proxy%20Policy%20Steering.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Observe Before You Alert: Adaptive Driver Alerting with Vision-Language Models](items/Observe%20Before%20You%20Alert%20Adaptive%20Driver%20Alerting%20with%20Vision-Language%20Models.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [A Multimodal Label Forecasting Method for Aperiodic Visuo-Motor Time Series](items/A%20Multimodal%20Label%20Forecasting%20Method%20for%20Aperiodic%20Visuo-Motor%20Time%20Series.md) · [[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- [MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging](items/MemForest%20Efficient%20Agent%20Memory%20Management%20via%20EventTree%20Partitioning%20and%20Progr.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints](items/3DWay%20Generalizing%20Robot%20Manipulation%20via%203D%20Consistent%20Waypoints.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [OmniNav: Robust Long-Horizon Target Navigation in Dynamic Environments](items/OmniNav%20Robust%20Long-Horizon%20Target%20Navigation%20in%20Dynamic%20Environments.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements](items/CosmoH2G%20A%20Hand-to-Gripper%20Transfer%20Dataset%20and%20Baseline%20Method%20for%20Object%20Manip.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [CAST: Alternating State-Value Targets and Expanded Policy Gradients for Model-Based Reinforcement Learning](items/CAST%20Alternating%20State-Value%20Targets%20and%20Expanded%20Policy%20Gradients%20for%20Model-Bas.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method](items/Towards%20Embodied%20Air-Ground%20Cooperative%20Object%20Search%20Benchmark%2C%20Dataset%20and%20Age.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [VeriScene: Reconstructing Crime Scenes from Legal Evidence via World-Model Agent](items/VeriScene%20Reconstructing%20Crime%20Scenes%20from%20Legal%20Evidence%20via%20World-Model%20Agent.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2300
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy
- 最高分论文发布时间：2026-09-07T13:24:23Z
- 主要技术对象分类：具身智能评测与基准 20、多模态基础模型 14、世界模型 12、智能体 Agent 11、视觉语言动作模型 VLA 11、机器人学习 7
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
