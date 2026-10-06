---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-06
---

# 2026-10-06 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：怎样把已有基础模型的能力变成机器人真正能用的控制，而不把每个问题都交给更大规模训练。先读 FastOPD，理解如何用少量教师查询教会小模型跨步生成动作；再读 SimpleTouch，看触觉如何通过独立通路进入动作生成，以及未来预测为何只用于训练；若关心长任务如何跨环境复用，读 Skill2Real，重点检查技能知识与机器人底层实现之间的接口边界。
> **趋势**：前五篇的共同线索：这些论文都在重新安排已有能力的使用方式：压缩教师、保留触觉细节、分开协调与执行、约束易变特征，或积累可执行技能。共同证据支持的是特定任务和接口条件下的收益，尚不足以推到任意机器人、任意环境。

- **规模**：2391 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 19、多模态基础模型 14、视觉语言动作模型 VLA 13、世界模型 11、智能体 Agent 10、机器人学习 10、Sim2Real 2
- **源异常**：0
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [FastOPD: On-Policy Distillation for Lightweight VLA Deployment](items/FastOPD%20On-Policy%20Distillation%20for%20Lightweight%20VLA%20Deployment.md)

> FastOPD 把大 VLA 的动作生成能力教给小模型，让它用一两次计算完成原本需要反复更新的动作生成。巧处是每条生成轨迹只在一个学生自己到达的位置询问教师，再用自一致性把局部指导扩展成长距离跳转。

- **能借鉴什么**：值得借鉴的是：昂贵教师可以只校正学生实际会遇到的局部错误，再由学生内部约束学会跨步。这适合教师调用贵、最终部署又必须小而快的生成策略。
- **值得读吗**：值得读到损失构造和逐任务结果：它确实缓解少步压缩成本，但是否可部署要看能否接受长任务损失。

<details><summary>实验依据</summary>

仿真覆盖 LIBERO 的 40 项单臂任务及 RoboTwin 2.0 的 50 项双臂任务，每任务测试 50 次，对比原学生、教师及 CTM、DMD、iMF [S23](https://arxiv.org/html/2610.02832v1#S4.p1.1) [S24](https://arxiv.org/html/2610.02832v1#S4.SS1.p1.1) [S25](https://arxiv.org/html/2610.02832v1#S4.SS1.p2.1) [S26](https://arxiv.org/html/2610.02832v1#S4.SS1.p3.1)。LIBERO 两步成功率为 81.8%，教师十步为 97.5%，原学生两步为 71.4% [S28](https://arxiv.org/html/2610.02832v1#S4.T3.fig1.1)；延迟为 66 对 301 毫秒 [S32](https://arxiv.org/html/2610.02832v1#S4.T3.2)，摘要报告降低 78.1%。RoboTwin 用 LingBot 教师时，单步从原学生的 35.3% 到 51.2%，但四步 59.9% 略低于原学生 60.4% [S30](https://arxiv.org/html/2610.02832v1#S4.T3.fig2.1)。收益主要说明少步部署有效，并非所有步数都更强。

</details>

### 2. [SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining?](items/SimpleTouch%20Can%20Vision-Language-Action%20Models%20Master%20Contact-Rich%20Manipulation%20W.md)

> SimpleTouch 给 π₀.₅ 增加独立触觉专家，让动作生成直接读取完整接触特征。它用任务示范同时教动作和未来触觉预测，在已有触觉编码器的前提下，省去额外触觉策略预训练和单独对齐阶段。

- **能借鉴什么**：可借鉴的是把“已有感知特征”与“学会据此行动”分开：保留接触空间细节，用独立通路和未来预测教策略使用它们，值得作为昂贵新预训练之前的尝试。
- **值得读吗**：值得读到注意力接口和预测消融：关键是怎样让触觉参与行动，而不是仅增加一个传感器输入。

<details><summary>实验依据</summary>

UniVTAC 六项仿真任务及四项真机任务，每方法每任务均用 50 条示范，分别测试 100 和 20 次 [S21](https://arxiv.org/html/2610.02784v1#S4.SS1.SSS0.Px1.p1.1)。指标为任务成功率的等权平均：仿真 77.5%，FTP-π₀.₅ 为 45.2%，预训练 FTP-1 为 66.7%，且六任务全部领先 [S23](https://arxiv.org/html/2610.02784v1#S4.SS2.SSS0.Px1.p1.1)。真机 71.3%，FTP-1 为 62.5%；USB 插入两者均只有 30% [S24](https://arxiv.org/html/2610.02784v1#S4.SS2.SSS0.Px2.p1.1)。这支持所测任务不必追加触觉策略预训练，不证明触觉预训练普遍无用。

</details>

### 3. [DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication](items/DuoMind%20Enabling%20Distributed%20Multi-Robot%20Coordination%20with%20Semantic%20Communicatio.md)

> DuoMind 给每个机器人分别配一个负责协调的 VLM 和一个负责动作的 VLA。机器人交换意图、子目标和任务判断，再各自生成当前指令，让单机器人动作能力接上团队协作。

- **能借鉴什么**：值得借鉴的是让动作模型接收它能执行的局部命令，把“什么时候做、如何等同伴”留给协调层。这样可以复用单机器人技能，而不必先让动作模型学懂整个团队。
- **值得读吗**：值得读到指令约束和通信消融：设计容易理解，但不少长任务成功率仍低，工程边界比整体领先更值得看。

<details><summary>实验依据</summary>

测试均为仿真：RoboPoly 七任务，以及把 RoboTwin 双臂拆成独立控制的八任务，每任务 400 次 rollout [S14](https://arxiv.org/html/2610.02161v1#S4.p1.1) [S21](https://arxiv.org/html/2610.02161v1#S4.SS1.p5.1)。相比使用总指令的 π₀.₅，Cook Pot 成功率从 1.00% 到 39.25%，Hang Bag 从 52.25% 到 78.00%；Prepare Snack 仅从 16.25% 到 18.00% [S23](https://arxiv.org/html/2610.02161v1#S4.T1.4) [S24](https://arxiv.org/html/2610.02161v1#S4.T1.5)。已提供的 RoboTwin 四项也均有改善 [S26](https://arxiv.org/html/2610.02161v1#S4.T2.2)。节选描述禁用消息的消融，但没有数值，不能据此量化通信的独立贡献。

</details>

### 4. [MixVLA: Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Language-Action Models](items/MixVLA%20Adaptive%20Mixing%20of%20Non-Invariant%20Information%20for%20Generalizable%20Vision-Lan.md)

> MixVLA 不把环境易变信息全部丢掉，而用 AMI 在训练时混合这部分特征，削弱策略对特定外观的依赖。再把混合特征与较稳定特征一起用于动作预测，保留可能有用的信息。

- **能借鉴什么**：启示是易变信息不等于无用信息：与其强迫策略完全忽略它，可以打乱其稳定对应关系，让模型学会更谨慎地使用。适合外观变化明显、但又不能丢失全部细节的任务。
- **值得读吗**：值得读到完整 AMI 公式和部署实现：核心思路有依据，但相机退步与额外训练成本必须一起评估。

<details><summary>实验依据</summary>

用 LIBERO 训练，在 LIBERO-Plus 测未见扰动；还测试 RoboTwin 清洁训练到随机场景，以及真机 [S30](https://arxiv.org/html/2610.02898v1#S4.p6.1)。OpenVLA-OFT 上，LIBERO-Plus 总成功率从 69.6% 到 76.2%，但相机扰动从 56.4% 降至 49.6% [S24](https://arxiv.org/html/2610.02898v1#S4.T1.4.1)；域内从 97.1% 到 96.7% [S32](https://arxiv.org/html/2610.02898v1#S4.SS1.p1.1)。相对仅信息瓶颈，作者报告 LIBERO-Plus 再增 4.0、RoboTwin C2R 再增 2.8 个百分点 [S33](https://arxiv.org/html/2610.02898v1#S4.SS2.p1.1)。真机取面包任务各测十次，灯光扰动下为 60% 对 20%，属初步证据 [S36](https://arxiv.org/html/2610.02898v1#S4.SS3.SSS0.Px2.p1.1) [S37](https://arxiv.org/html/2610.02898v1#S4.SS3.SSS0.Px2.p2.1)。

</details>

### 5. [Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation](items/Skill2Real%20Agentic%20Skill%20Learning%20for%20Zero-Shot%20Sim-to-Real%20Robot%20Manipulation.md)

> Skill2Real 在仿真里积累经过验证的可执行技能，再把冻结技能库交给真机器人使用。它用共同 API 隔开任务知识与机器人底层差异，并让 PVG 分别负责提出程序、诊断结果和批准记忆更新。

- **能借鉴什么**：值得借鉴的是监督信息可以比执行信息更丰富：仿真知道失败真因，但留下的修复规则必须能由部署时可见信息触发。同时把“建议修复”和“验证后入库”分开，避免一次偶然成功污染长期记忆。
- **值得读吗**：值得读到 API 合同和技能入库证据：它展示了可迁移任务知识，但复现难点在后端能力与验证流程。

<details><summary>实验依据</summary>

Sol 在 LIBERO-90 学技能，Astra 测未训练的 Pro Long，成功率从无记忆 2.0% 经局部技能 35.3% 到完整层级 56.3% [S7](https://arxiv.org/html/2610.02788v1#S1.p5.1)；删除 Verifier 或 Governor 后为 39.0%、43.0% [S38](https://arxiv.org/html/2610.02788v1#S5.SS4.p2.1)。独立 Robosuite 七任务训练分别达 85.1%、89.4%，不能当作同一库的迁移成绩 [S7](https://arxiv.org/html/2610.02788v1#S1.p5.1)。真机 UR5e 四任务，每方法每任务 20 次，固定 Astra 和 API 后，平均完成率从 27.50% 到 78.75%，局部技能单独为 56.25% [S26](https://arxiv.org/html/2610.02788v1#S4.SS3.p1.1) [S27](https://arxiv.org/html/2610.02788v1#S4.SS4.p1.1) [S28](https://arxiv.org/html/2610.02788v1#S5.p1.1) [S29](https://arxiv.org/html/2610.02788v1#S5.F7) [S30](https://arxiv.org/html/2610.02788v1#S5.T1) [S31](https://arxiv.org/html/2610.02788v1#S5.T1.4) [S32](https://arxiv.org/html/2610.02788v1#S5.SS2.p1.1)，支持层级知识在该接口下有贡献。

</details>

## 扫读 7 篇

- [RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer](items/RoboBridge%20A%20Self-Evolving%20Embodied%20Agent%20Framework%20for%20Sim-to-Real%20Transfer.md) — RoboBridge 把仿真到现实的迁移变成“继续修改可执行技能”：保留任务流程，依据真实执行反馈调整不适用的操作。底层 VLA 作为动作工具使用，通过推理时引导执行，不需要重新训练它。
- [RoboChemGym: A Protocol-Driven Generative Simulation Framework for Long-Horizon Chemical Manipulation](items/RoboChemGym%20A%20Protocol-Driven%20Generative%20Simulation%20Framework%20for%20Long-Horizon%20C.md) — RoboChemGym 要按真实化学实验规程，在仿真中生成长流程操作示范。它反复调整任务执行和场景配置，目标是产出遵守流程约束、包含十步以上交互的轨迹。
- [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](items/Reconstruct%2C%20Practice%2C%20Go%20Real%20Guided%20Self-Improvement%20for%20Embodied%20Agents.md) — RPG 让机器人先从离线数据中找出可练习的能力，再在仿真里反复诊断失败、修改技能和系统提示词。它不更新模型权重，而是通过跨任务测试筛选修改，最终把积累的执行知识交给多模态 LLM 使用。
- [PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation](items/PointWAM%203D%20World%20Action%20Modeling%20for%20Dexterous%20Robotic%20Manipulation.md) — PointWAM 同时预测手和环境中的点在三维空间里怎样运动，再把预测的手部运动转换成机器人动作。它希望机器人不仅知道手往哪去，还能预测动作会让物体怎样变化。
- [SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation](items/SARI%20Phase-Split%20Sim-Real%20Co-Training%20for%20Contact-Rich%20Manipulation.md) — SARI 把操作分成接近物体和接触物体两个阶段：仿真提供丰富的接近路径，真实示范提供可信的接触动作。它将两类数据共同训练成一个 VLA 策略，执行时无需人工标记阶段或切换控制器。
- [DeltaWorld: Physically Consistent Interactive World Simulators via Action-Conditioned Latent Increment Learning](items/DeltaWorld%20Physically%20Consistent%20Interactive%20World%20Simulators%20via%20Action-Conditi.md) — DeltaWorld 不让模型重新猜整幅未来场景，而是先预测机器人动作会让当前状态改变多少，再把变化加回去。它还专门监督交互区域的变化，试图减少预测视频里的物体穿透和过度变形。
- [Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination](items/Imagine%20the%20Future%2C%20Internalize%20the%20Gist%20Efficient%20VLA%20Reasoning%20via%20Internalize.md) — IG-VLA 先在视觉特征里学习“接下来场景会怎样变化”，帮助机器人选动作，再把这种推演得到的关联收进 Scene Gist Token。部署时可以直接利用这个紧凑表示，省去每次显式想象未来的计算。

## 其余存档 12 篇

- [UniIntervene++: An Adaptive Intervention Agent for Efficient Real-World Reinforcement Learning](items/UniIntervene%2B%2B%20An%20Adaptive%20Intervention%20Agent%20for%20Efficient%20Real-World%20Reinforce.md) · 智能体 Agent 机器人学习 具身智能评测与基准
- [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](items/ManiPhysicsBench%20Physics-Based%20Assessment%20of%20Object%20Preservation%20in%20VLA%20Manipula.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [World Action Learning via Interaction-Centric Spectral Latent Guidance](items/World%20Action%20Learning%20via%20Interaction-Centric%20Spectral%20Latent%20Guidance.md) · 世界模型 机器人学习 具身智能评测与基准
- [EmbPASS: Towards Cross-Embodiment Open Panoramic Segmentation](items/EmbPASS%20Towards%20Cross-Embodiment%20Open%20Panoramic%20Segmentation.md) · 具身智能评测与基准
- [Co-design Gym: A Unified Benchmark for Embodiment-Policy Co-optimization](items/Co-design%20Gym%20A%20Unified%20Benchmark%20for%20Embodiment-Policy%20Co-optimization.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [SocialVLA: A Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery in VLA Manipulation](items/SocialVLA%20A%20Social%20Perception%20Gateway%20for%20Human-Reaction-Based%20Failure%20Detection.md) · 多模态基础模型 视觉语言动作模型 VLA
- [Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models](items/Detect%20and%20Suppress%20A%20Mechanistic%20Defense%20against%20Adversarial%20Patches%20in%20VLA%20Mod.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation](items/MobiAgent%20Dual-Loop%20Recursive%20Policy%20Self-Improvement%20for%20Long-Horizon%20Mobile%20Ma.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- [DexJoCo-X: Benchmarking Action Representations for Multi-Hand Dexterous Manipulation](items/DexJoCo-X%20Benchmarking%20Action%20Representations%20for%20Multi-Hand%20Dexterous%20Manipulat.md) · 机器人学习 具身智能评测与基准
- [Equivariant Visual-Tactile Diffusion Policy for Contact-Rich Manipulation](items/Equivariant%20Visual-Tactile%20Diffusion%20Policy%20for%20Contact-Rich%20Manipulation.md) · 世界模型 机器人学习
- [CHASE-VLA: Post-Training Quantization Framework for Vision-Language-Action Models with Chunk-Aware Scale Estimation](items/CHASE-VLA%20Post-Training%20Quantization%20Framework%20for%20Vision-Language-Action%20Models.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [EVOL: Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation](items/EVOL%20Simulator-Guided%20Evolutionary%20Expert%20Synthesis%20for%20Deployment-Free%20Learning.md) · 智能体 Agent 机器人学习

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2391
- 入选条目：24
- 回填已见条目：0
- 最高分论文：FastOPD: On-Policy Distillation for Lightweight VLA Deployment
- 最高分论文发布时间：2026-10-02T05:24:20Z
- 主要技术对象分类：具身智能评测与基准 19、多模态基础模型 14、视觉语言动作模型 VLA 13、世界模型 11、智能体 Agent 10、机器人学习 10、Sim2Real 2
- 信息源错误：0
- 自动恢复信息源：0

</details>
