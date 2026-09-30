---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-09-12
---

# 2026-09-12 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天优先看能改变机器人训练与执行方式的工作：HuRo扩大可用示教来源，IMLE-VLA减少动作生成延迟，2AM与MaP-WAM探索如何把长期记忆转成执行器可用的指令。安全方面，ReactHuman暴露突发危险响应的不足，ActSafeGuard和FARM分别切入动作约束与失败监测；三者证据边界不同，不能合并理解为部署安全已解决。
> **趋势**：共同趋势是把复杂能力拆成可检验的接口：人类视频与机器人动作、历史记忆与当前计划、生成策略与可行约束。评审重点也随之转向这些接口是否真的改善闭环执行，以及收益能否跨任务、场景和机器人保持。

- **规模**：2313 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 14、智能体 Agent 10、多模态基础模型 9、视觉语言动作模型 VLA 9、机器人学习 8、世界模型 7、Sim2Real 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs](items/ReactHuman%20A%20Physics-Grounded%20Benchmark%20for%20Human-Like%20Reactive%20Decision-Making.md)

> 机器人看懂危险，不代表来得及做对。ReactHuman让多模态模型在物理仿真中处理突发家庭事故，并实际执行其计划，检查反应是否合理、安全且符合物理。

- **为什么值得读**：对具身评测和世界模型研究者，价值在于把物理判断落实为有后果的动作测试，可区分危险识别、策略选择与空间执行问题。
- **证据**：评测七个MLLM，报告模型约每三次危险处理失误一次；存在固定反应倾向、过度相信外观，以及动作类型正确但拦截位置出现米级误差。摘要称这些失败未随模型规模增大而减轻。
- **判断**：值得精读评测协议与失败分类，适合检验模型物理理解是否真正支持安全行动。

### 2. [HuRo: Robotizing Human Videos for Scalable VLA Pretraining](items/HuRo%20Robotizing%20Human%20Videos%20for%20Scalable%20VLA%20Pretraining.md)

> HuRo把人类视频同时转换成机器人视角的观测和动作轨迹，让VLA能从更大规模的人类活动中预训练。关键是共同处理视觉与动作的跨具身差异。

- **为什么值得读**：为VLA研究者提供了扩大预训练数据的具体路径，并把数据规模收益与真实机器人泛化联系起来。
- **证据**：数据来自五个人类视频源，约63万段episode、1.42亿处理帧。四项真实操作任务中，扩大预训练规模使总体完成率从51.5%升至80.3%，空间与视觉偏移下的OOD完成率从34.9%升至72.2%；消融支持视觉转换及动作监督的作用。
- **判断**：值得精读流水线和规模实验，是本批次中数据路线证据较直接的一篇。

### 3. [ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies](items/ActSafeGuard%20Differentiable%20and%20Training-Aligned%20Constraint%20Enforcement%20for%20Flow.md)

> ActSafeGuard让动作生成模型在训练时就面对硬约束，减少执行时临时纠偏带来的不一致。关键是一个可微的解析射线缩放层，让约束边界参与学习。

- **为什么值得读**：对VLA研究者，这是将动作可行性直接纳入策略训练的实现方向，也便于研究安全修正如何影响策略本身。
- **证据**：在π0.5和Fast-WAM等骨干、多项任务上，摘要报告100%的逐步安全率，同时保持或提高任务成功率；未给出具体任务数量和成功率数值。
- **判断**：值得精读算子推导与约束定义，论文价值取决于保证适用范围和任务收益能否同时成立。

### 4. [IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies](items/IMLE-VLA%20Fast%20Single-Step%20Action%20Generation%20for%20Vision-Language-Action%20Policies.md)

> IMLE-VLA把多轮迭代生成动作改成一步生成，减少机器人等待推理的停顿。它用条件隐式最大似然估计保留多种可行动作，避免简单回归头的模式坍缩。

- **为什么值得读**：直接关联VLA延迟、动作平滑性和任务表现，适合需要实时闭环操作的研究者。
- **证据**：应用于π0.5后推理频率由15 Hz升至55 Hz，动作吞吐量最高提高11倍；LIBERO的40项任务平均成功率98.0%，LIBERO-plus保持原模型鲁棒性。Franka四项真实任务均优于π0.5，jerk降低2.2—3.0倍，每回合累计VLA推理时间降低3.9—6.6倍。
- **判断**：值得精读并考虑复现动作头替换，速度收益同时有基准和实机证据支撑。

### 5. [2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation](items/2AM%20Grounding%20Agent-Side%20Memory%20as%20Guidance%20for%20Steerable%20Action%20Models%20in%20Long-.md)

> 2AM把长期记忆放在Agent里，让动作模型只执行当前明确指令。Agent通过子任务语言和二维抓取、放置、移动提示，把记忆转成机器人能落实的意图。

- **为什么值得读**：为Agent与VLA如何分工提供可检验设计，提示接口精度可能是长程机器人性能的重要变量。
- **证据**：在不使用深度、在线几何和规划器物体运动的LIBERO-Mem设置中，平均完成率76.3%，比摘要所列最强基线14.8%高61.5个百分点；宽松成功率63.0%，严格成功率11.8%。
- **判断**：值得精读接口设计和指标定义，尤其适合研究Agent记忆与VLA执行能力的归因。

## 扫读 7 篇

- [UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling](items/UniMPA%20A%20Unified%20Memory-Prediction-Action%20Model%20via%20Action-Grounded%20Transition%20M.md) — UniMPA试图让机器人预测的下一步既符合任务进度，也确实能执行。它用历史视觉—动作经验约束未来预测，再用动作原型引导当前动作生成。
- [Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation](items/Rapid%20Learning%20of%20Dexterous%20In-Hand%20Pen%20Writing%20through%20Real-Time%20Jacobian%20Estim.md) — 这项工作让机械手靠短时间在线辨识，学会在手内转动笔来书写。关键是实时估计手与笔整体的任务Jacobian，并持续修正控制。
- [SwarmNxt: Open-source Software-Hardware Platform for Fast and Agile Aerial Swarms](items/SwarmNxt%20Open-source%20Software-Hardware%20Platform%20for%20Fast%20and%20Agile%20Aerial%20Swarms.md) — SwarmNxt把多无人机实验所需的硬件装配、批量部署和自主飞行软件整合起来，降低搭建实体集群的工程成本。
- [FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model](items/FARM%20Reading%20Failure%20Signals%20from%20the%20Internal%20Predictive%20States%20of%20a%20Frozen%20Rob.md) — FARM从冻结机器人世界模型的内部预测状态中读出失败风险，只训练一个很小的监督读出器。它检验已有预测表征能否兼做在线监控。
- [Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection](items/Harness%20Robotic%20OS%20A%20Unified%20Embodied-Agent%20Runtime%20for%20Closed-Loop%20Quadruped%20In.md) — HROS把四足巡检中的导航、场景理解、语音交互和告警报告接成可追溯闭环。Argos是它在住宅社区巡检中的具体实现。
- [When Validation Stops Learning: Auditing Update Admission for Continual Embodied Agents](items/When%20Validation%20Stops%20Learning%20Auditing%20Update%20Admission%20for%20Continual%20Embodied.md) — 这篇论文提醒：更新审核过严，也可能让机器人永远学不到新东西。它提出同时审计误放风险与错失学习机会，并用配对检验降低部分审核成本。
- [Safety-aware Skill Adaptation for Reinforcement Learning in Dynamic Environments](items/Safety-aware%20Skill%20Adaptation%20for%20Reinforcement%20Learning%20in%20Dynamic%20Environments.md) — Dist-GPRL让机器人逐段调整已有技能轨迹，并用障碍距离引导探索。它通过高斯过程保持相邻轨迹修改连贯，降低整段动作一起优化的难度。

## 其余存档 12 篇

- [Morphology-Aware Human Motion Retargeting for Wheeled-Humanoid Loco-Manipulation](items/Morphology-Aware%20Human%20Motion%20Retargeting%20for%20Wheeled-Humanoid%20Loco-Manipulation.md) · 智能体 Agent
- [ObstaDiff: Generalizable Diffusion Policy Learning via Obstacle-aware Representations](items/ObstaDiff%20Generalizable%20Diffusion%20Policy%20Learning%20via%20Obstacle-aware%20Representat.md) · 机器人学习
- [Memory as Plans: World-Action Modeling with Memory-Grounded Planning](items/Memory%20as%20Plans%20World-Action%20Modeling%20with%20Memory-Grounded%20Planning.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [SEED-UMI: Sharing the Exoskeleton between human and robot for onE-to-one Dexterous demonstration](items/SEED-UMI%20Sharing%20the%20Exoskeleton%20between%20human%20and%20robot%20for%20onE-to-one%20Dexterou.md) · 机器人学习 具身智能评测与基准
- [LTLDiff: Finite Linear Temporal Logic-Guided Data Generation and Diffusion Policies for Multi-agent Robotic Manipulation](items/LTLDiff%20Finite%20Linear%20Temporal%20Logic-Guided%20Data%20Generation%20and%20Diffusion%20Polici.md) · 智能体 Agent 机器人学习 具身智能评测与基准
- [BridgeMatch: Conditional Transport Bridges in Matching Matrix Space for 3D Deformable Registration](items/BridgeMatch%20Conditional%20Transport%20Bridges%20in%20Matching%20Matrix%20Space%20for%203D%20Deform.md) · 世界模型
- [Beyond Noise Steering: Dual-Latent Space Reinforcement Learning for Generative Robot Policy](items/Beyond%20Noise%20Steering%20Dual-Latent%20Space%20Reinforcement%20Learning%20for%20Generative%20Ro.md) · 机器人学习
- [MuJoCable: Reduced-Order Surface-Routed Cable Transmission for Tendon-Driven Robots](items/MuJoCable%20Reduced-Order%20Surface-Routed%20Cable%20Transmission%20for%20Tendon-Driven%20Robo.md) · 世界模型 Sim2Real 具身智能评测与基准
- [Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents](items/Autonomy%2C%20Social%20Norms%2C%20and%20Alignment%20Towards%20a%20Developmental%20Framework%20for%20Auto.md) · 智能体 Agent
- [Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models](items/Your%20Model%20Already%20Knows%20Don%27t%20Teach%20It%2C%20Learn%20to%20Ask%20It%20Soft%20Prompting%20for%20Few-.md) · 多模态基础模型 视觉语言动作模型 VLA
- [Topological Necessities: Mechanism-Invariant Strategic Subgoals for Cross-Embodiment Goal-Conditioned Control](items/Topological%20Necessities%20Mechanism-Invariant%20Strategic%20Subgoals%20for%20Cross-Embodim.md) · 智能体 Agent 机器人学习
- [Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending](items/Adversarial%20Training%20for%20Tabular%20Credit%20Scoring%20A%20Multi-Attack%20Robustness%20Evalua.md) · 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2313
- 入选条目：24
- 回填已见条目：0
- 最高分论文：ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs
- 最高分论文发布时间：2026-09-09T22:56:21Z
- 主要技术对象分类：具身智能评测与基准 14、智能体 Agent 10、多模态基础模型 9、视觉语言动作模型 VLA 9、机器人学习 8、世界模型 7、Sim2Real 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
