---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-09-23
---

# 2026-09-23 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天最值得看的是把机器人控制中被隐式处理的变量显式化：目标的三维位置、接触力、执行阶段和失败状态，分别对应更精准的操作、更可靠的接触和更有效的恢复。世界模型也出现两种实用路线：把内部表征蒸馏进轻量策略，或用预测后果辅助强化学习评价动作。阅读时应优先关注闭环评测和指标口径，尤其别把旧任务受到抑制、动作供应速度或步骤完成率直接当成新任务成功、反馈频率或整任务成功率。
> **趋势**：这批工作共同指向：可靠机器人需要明确知道操作对象、当前阶段和动作后果，并在证据不足时更新判断。评测也从干净场景中的成功率，转向视觉时效、任务语义变化、主动获取信息和失败恢复。

- **规模**：2355 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 21、多模态基础模型 17、视觉语言动作模型 VLA 17、智能体 Agent 13、机器人学习 11、世界模型 8、Sim2Real 1
- **源异常**：0
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Grounded Action Model: 3D Grounding as a Foundation for Robotics](items/Grounded%20Action%20Model%203D%20Grounding%20as%20a%20Foundation%20for%20Robotics.md)

> Grounded Action Models（GAM）先明确“操作哪个物体、它在三维空间哪里”，再预测动作。它把语言、点或框提示统一成带真实尺度几何的物体表示，减少策略从机器人示范中自行摸索空间定位的负担。

- **为什么值得读**：对VLA和分层机器人系统研究者，价值在于把目标定位变成明确的策略接口，既便于研究空间泛化，也方便Agent通过点、框等方式指定操作对象。
- **证据**：RoboTwin 2.0 的50项任务平均成功率55.3%，Spatial Forcing为52.0%；场景随机化下47.6%，Abot-M0为30.4%。LIBERO-PRO为61%，π₀.₅为53%。YAM视觉变化下成功17/20，对照为4/20；与Molmo2组合的Franka长程任务ID/OOD步骤完成率为64.7%/49.8%。
- **判断**：值得精读表示构造与扰动实验：跨基准和真实机器人结果都支持三维目标定位这一设计方向。

### 2. [Bridge3D: Enabling Vision-Language-Action Models to See and Act in 3D](items/Bridge3D%20Enabling%20Vision-Language-Action%20Models%20to%20See%20and%20Act%20in%203D.md)

> Bridge3D让已有二维VLA既能看出三维结构，也能在生成动作时受到几何约束。关键是同时增强视觉特征，并把显式三维语义场接入动作去噪。

- **为什么值得读**：适合希望保留预训练二维VLA、逐步加入三维能力的研究者，提供了分别作用于感知端和动作端的改造路径。
- **证据**：RoboTwin 2.0上比π₀高14.0个百分点；真实实验比Spatial Forcing高11.7个百分点。摘要未提供绝对成功率。
- **判断**：值得读方法和消融，重点判断显式动作条件是否带来超出视觉特征增强的收益。

### 3. [LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models](items/LIBERO-VPro%20Benchmarking%20Closed-Loop%20Visual%20Robustness%20of%20Robotic%20Foundation%20Mod.md)

> LIBERO-VPro专门测试机器人执行途中“看不清、看到旧画面、不同视角不一致”时还能否正确行动。它揭示了标准成功率可能掩盖的视觉依赖和适应缺陷。

- **为什么值得读**：为具身评测提供更细的诊断轴，帮助研究者区分视觉定位、观测时效和行为适应问题，而非仅报告一个总体成功率。
- **证据**：包含12类挑战、96种设置、3,296个任务条件组合；评测3个VLA和3个WAM，约19.6万次仿真及200次Franka真实运行。物体严重遮挡未必导致失败，但局部交互线索破坏、旧观测和任务前提变化会显著削弱表现。
- **判断**：值得精读评测协议和失败案例，适合直接用于检查机器人基础模型的闭环可靠性。

### 4. [Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation](items/Opt2VLA%20Force-Aware%20Vision-Language-Action%20for%20Contact-Rich%20Humanoid%20Whole-Body.md)

> Opt2VLA让人形机器人不仅知道“往哪里动”，还知道“该用多大力”。VLA同时输出运动目标和接触力参考，再由全身控制器执行。

- **为什么值得读**：对接触型VLA和机器人学习，核心价值是明确语义策略与物理控制之间的力接口；摘要没有提供直接的世界模型贡献。
- **证据**：在3项人形接触任务上，显式力条件比纯运动控制具有更准确、一致的力调节；轨迹优化提供的力矩监督进一步改善跟踪与稳定性。仿真和硬件展示语言条件下的力调制；摘要未给出可核查的结果数字。
- **判断**：做全身接触控制值得精读，重点看力命令如何生成、跟踪和验证。

### 5. [Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies](items/Think%20Like%20a%20World%20Model%2C%20Act%20Like%20a%20VLA%20Distilling%20World-Model%20Representations.md)

> 这项工作把世界模型学到的场景表征教给小型VLA，部署时不用再生成未来。机制是在普通策略训练中加入特征对齐，让学生吸收教师的内部表示。

- **为什么值得读**：为世界模型研究者提供脱离在线生成的价值验证方式，也为VLA研究者提供不增加部署结构的表征增强手段。
- **证据**：0.8B学生在LIBERO达97.9%；RoboCasa-GR1从48.2%升至50.5%。RTX 5090上推理32毫秒、显存1.86GB；单臂和双臂硬件均验证迁移，收益在不同学生规模、骨干、对齐层和教师下仍存在。
- **判断**：值得精读并考虑复现，方法改动集中，适合检验世界模型表征能否稳定提升策略。

## 扫读 7 篇

- [Phrase-Level Robotic Guqin Performance: Bimanual Motion Planning and Audio-Tactile Interaction Monitoring](items/Phrase-Level%20Robotic%20Guqin%20Performance%20Bimanual%20Motion%20Planning%20and%20Audio-Tactil.md) — 这套古琴机器人把连续乐句拆成需要精确配合的双手接触事件，并结合触觉监测和声音校准完成演奏。难点不只是手臂不碰撞，还包括何时拨弦、何时按触以及发出什么声音。
- [CARE: Experience-Guided Atomic Corrective Execution for Vision-Language-Action Policies](items/CARE%20Experience-Guided%20Atomic%20Corrective%20Execution%20for%20Vision-Language-Action%20Po.md) — CARE让VLA从实际执行失败中学习如何补救，而不是只学顺利完成任务的轨迹。它按任务阶段归纳常见偏差，再训练小幅修正或局部重做。
- [Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning](items/Imagine-RL%20Residual-Confidence-Guided%20Cross-Attention%20for%20World-Model-Augmented.md) — Imagine-RL在强化学习评价动作时，先预测它可能带来的视觉和接触后果。它还根据过去的预测误差降低不可靠未来信息的权重，避免评价器盲信世界模型。
- [Topology-Informed Visual Prompting For Vision Language Action Policies](items/Topology-Informed%20Visual%20Prompting%20For%20Vision%20Language%20Action%20Policies.md) — 这项拓扑视觉提示方法帮助VLA分清“看起来相似、却必须走不同路线”的状态。它先用仿真几何构造正确路线的示范，再把预测的末端路点画到实时图像上引导动作。
- [HumynexSurg-1: A Curated Expert Liposuction Dataset](items/HumynexSurg-1%20A%20Curated%20Expert%20Liposuction%20Dataset.md) — HumynexSurg-1提供一小批专家吸脂操作记录，把口述决策与视觉、压力和手部力信息同步保存。价值主要在于怎样采集视觉难以直接解释的接触操作，而非已经实现自主手术。
- [AR-WAM: A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulation](items/AR-WAM%20A%20Visual-Conditioned%20Agent-Ready%20World%20Action%20Model%20for%20Robotic%20Manipulat.md) — AR-WAM让上层Agent用“目标框＋技能编号”指挥机器人，减少语言指令中的指代和空间歧义。底层模型同时预测场景变化和动作，把长期记忆与纠错交给Agent。
- [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](items/ARSTAG%20An%20Agentic%20Real2Sim2Real%20System%20for%20Task-Specific%20Robot%20Data%20Generation.md) — ARSTAG把一张现场图片和一句任务描述转成机器人训练示范。多个语言Agent负责搭仿真场景、生成可执行轨迹和随机化数据，再将训练好的策略迁移到真实机器人。

## 其余存档 12 篇

- [ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation](items/ActiveArena%20Benchmarking%20and%20Understanding%20Active%20Perception%20in%20Robotic%20Manipula.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models](items/Beyond%20Appearance%20Shifts%20Task-Semantic%20Action%20Calibration%20for%20VLA%20Models.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation](items/CompVLA%20A%20Variable%20Compliance%20Vision-Language-Action%20Model%20for%20Contact-rich%20Mani.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [ReVeal: A Reconstruction-Aware Real-to-Sim Framework for VLA Policy Evaluation](items/ReVeal%20A%20Reconstruction-Aware%20Real-to-Sim%20Framework%20for%20VLA%20Policy%20Evaluation.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [EgoWild2Dex: Learning Dexterous Robotic Manipulation from In-the-Wild Human Experience](items/EgoWild2Dex%20Learning%20Dexterous%20Robotic%20Manipulation%20from%20In-the-Wild%20Human%20Exper.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [ME-VLM:A Unified VLM for Embodied Cognition and Agent Coordination](items/ME-VLM%20A%20Unified%20VLM%20for%20Embodied%20Cognition%20and%20Agent%20Coordination.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality](items/InsertAnything%20Generalizable%20Contact-Rich%20Precision%20Insertion%20from%20Simulation%20to.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Zeva-Ego: Egocentric Mid-Training with In-Context Causal Learning for Robot Manipulation](items/Zeva-Ego%20Egocentric%20Mid-Training%20with%20In-Context%20Causal%20Learning%20for%20Robot%20Manip.md) · [[视觉语言动作模型 VLA]] [[机器人学习]]
- [TaskAnchor: Grounding Task State in Reactive VLAs for Long-Horizon Manipulation](items/TaskAnchor%20Grounding%20Task%20State%20in%20Reactive%20VLAs%20for%20Long-Horizon%20Manipulation.md) · [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [MIGU: Multimodal Instruction Grounding under Uncertainty for Manipulation Planning](items/MIGU%20Multimodal%20Instruction%20Grounding%20under%20Uncertainty%20for%20Manipulation%20Plannin.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [vla.simd: Efficient CPU Inference for Language-Conditioned Manipulation](items/vla.simd%20Efficient%20CPU%20Inference%20for%20Language-Conditioned%20Manipulation.md) · [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [A Topological Representation with Object-Path Graphs for Open-Vocabulary Instance Navigation](items/A%20Topological%20Representation%20with%20Object-Path%20Graphs%20for%20Open-Vocabulary%20Instanc.md) · [[多模态基础模型]] [[智能体 Agent]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2355
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Grounded Action Model: 3D Grounding as a Foundation for Robotics
- 最高分论文发布时间：2026-09-20T20:35:39Z
- 主要技术对象分类：具身智能评测与基准 21、多模态基础模型 17、视觉语言动作模型 VLA 17、智能体 Agent 13、机器人学习 11、世界模型 8、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
