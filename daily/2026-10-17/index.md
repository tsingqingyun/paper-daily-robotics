---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-10-17
---

# 2026-10-17 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先看：怎样让已有 VLA 在执行时少犯错，同时把额外计算花在需要的地方。想理解“选哪段动作”，先读 VeriVLA；想理解“一次执行多长”，读 PAV，尤其看失败轨迹如何提供局部监督；想直接减少单次推理成本，读 FastVLA 的动态预算与等预算对照。CarryOn 和 LIBERO-PeRM 则分别回答个性化辅助怎样运行、怎样测量。
> **趋势**：前五篇的共同线索：这些论文共同把“生成动作”之外的决策单独拿出来：记住谁的偏好、检查动作后果、决定何时重新观察，以及分配视觉计算。证据也提醒我们：任务完成、偏好满足、安全和推理成本需要分别报告，一个指标变好不能替代其他指标。

- **规模**：2348 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 19、多模态基础模型 14、视觉语言动作模型 VLA 13、世界模型 12、机器人学习 10、智能体 Agent 5、Sim2Real 2
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](items/CarryOn%20A%20Dual-Loop%20Harness%20for%20Personalized%20and%20Reliable%20Robot%20Assistance.md)

> CarryOn 给冻结的 VLA 加了两层管理：一层记住用户偏好和场景变化，决定该做什么；另一层在动作落地前避碰、失败后修复，让原任务继续。

- **能借鉴什么**：值得借鉴的是把两种经验分开保存：用户与场景知识改变下一次任务决策，失败经验改变恢复控制。这样可以改善辅助行为，而不必把所有记忆和纠错都塞进 VLA 权重。
- **值得读吗**：值得读到记忆修订、动作过滤和恢复协议细节；它最有说服力的是职责分工，数字则显示安全改善远大于任务完成改善。

<details><summary>实验依据</summary>

真机三明治实验中，直接指定偏好和跨对话记忆均派发正确子任务24/24，更新偏好后为20/24；这是规划准确性，不是整餐完成率。[S25](https://arxiv.org/html/2610.21453v1#S4.SS1.p2.1) LIBERO-Safety 共900回合，安全微调策略加过滤器后，违规率52.6%→6.1%，但无违规任务成功率仅25.3%→25.6%；主要收益是减少违规。[S29](https://arxiv.org/html/2610.21453v1#S4.SS2.p1.1) [S30](https://arxiv.org/html/2610.21453v1#S4.T3) [S31](https://arxiv.org/html/2610.21453v1#S4.T3.7) 真机避障无接触完成0/20→20/20。[S32](https://arxiv.org/html/2610.21453v1#S4.SS2.p4.1) 摘要另报恢复13%→80%，节选未给完整对应协议；不能与真机恢复3/20→18/20混为一组。[S24](https://arxiv.org/html/2610.21453v1#S4.T1.6.2)

</details>

### 2. [LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation](items/LIBERO-PeRM%20Benchmarking%20Personalized%20Robotic%20Manipulation.md)

> LIBERO-PeRM 把“任务做完”和“按用户喜欢的方式做完”分开测。它在相同任务目标下生成有偏好、无偏好的示范，并检查策略是否学会了可迁移的执行要求。

- **能借鉴什么**：最值得借鉴的是保留目标不变，只改变完成方式，再换任务和布局测试同一偏好。只有这样，才能检查模型学到的是“绕开指定区域”这类要求，还是某条熟悉轨迹。
- **值得读吗**：值得重点读变量划分、评分和数据生成；使用前先确认自动规则是否对应自己真正想测的偏好。

<details><summary>实验依据</summary>

基准含五套任务、312个偏好条件任务，覆盖37个单偏好实例及18个双偏好组合。[S6](https://arxiv.org/html/2610.22372v1#S1.p4.1) [S8](https://arxiv.org/html/2610.22372v1#S1.p6.1) 六种 VLA 的零样本测试中，π0.5 无偏好成功率97.6%，加偏好后任务成功率66.67%、偏好满足度37.92%；运动偏好下成功率97.50%，满足度仅24.38%，清楚显示做完不等于听从偏好。[S31](https://arxiv.org/html/2610.22372v1#S4.T2.7) 满足度只在任务成功时计分。[S23](https://arxiv.org/html/2610.22372v1#S3.SS4.p1.1) 摘要称混合训练更保留无偏好能力，但可能削弱运动偏好学习；节选未给对应训练结果表，无法量化收益。

</details>

### 3. [VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models](items/VeriVLA%20Adaptive%20Test-Time%20Verification%20for%20Flow-Based%20VLAs%20with%20Latent%20World%20Mo.md)

> VeriVLA 在策略拿不准时多生成几段候选动作，再用潜在世界模型预测哪段更能推进任务。它把随机采样变成选择机会，并用触发器控制额外计算。

- **能借鉴什么**：可以借鉴的是把“动作生成得不一致”用作计算分配信号，把“动作是否有用”交给另一个有动力学预测能力的模型判断。当现有策略偶尔能生成好动作、却经常选中坏样本时，这种方法尤其值得尝试。
- **值得读吗**：值得读到触发校准、验证器训练和延迟分析；核心吸引力是有选择地花计算，前提是候选池确实包含更好的动作。

<details><summary>实验依据</summary>

PiperX 真机上插笔、移液、放苹果，每方法每任务50次；平均阶段完成分由基础 π0.5 的50.8%升至65.5%，RoboMonkey 为56.0%，GPC-RANK 为52.8%。这是阶段加权完成分，不是整任务成功率。[S25](https://arxiv.org/html/2610.21985v1#S4.T1.6) [S26](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px1.p1.1) [S27](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px2.p1.1) [S28](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px3.p1.1) [S29](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px4.p1.1) RTX 4090 每次触发增加326毫秒，明确不含触发器延迟。[S30](https://arxiv.org/html/2610.21985v1#S4.SS1.SSS0.Px5.p1.1) RoboTwin 五任务始终验证时，成功率在干净环境66.4%→73.6%，干净训练到随机测试62.8%→69.6%；后者不证明触发器也能直接迁移。[S33](https://arxiv.org/html/2610.21985v1#S4.SS2.SSS0.Px1.p1.1) [S34](https://arxiv.org/html/2610.21985v1#S4.T2) [S35](https://arxiv.org/html/2610.21985v1#S4.T2.7)

</details>

### 4. [Policy-Aligned Predictive Verification for Adaptive VLA Action-Chunk Execution](items/Policy-Aligned%20Predictive%20Verification%20for%20Adaptive%20VLA%20Action-Chunk%20Execution.md)

> PAV 不改 VLA 提出的动作，而是判断这段动作执行到哪里该停下来重新观察。它预测不同前缀的后果，估计之后原策略还能否完成任务，用这个分数选择执行长度。

- **能借鉴什么**：关键启示是把“模型对动作有把握”换成“这个动作之后还能继续成功”。另外，只有最终成败标签时，不必把失败轨迹的每一步都当坏样本；可以通过整体约束保留其中有用的行为。
- **值得读吗**：值得细读监督损失和长度选择规则；它对“何时重新看世界”的定义清楚，但必须连同验证耗时评估实际收益。

<details><summary>实验依据</summary>

LIBERO 每任务50次，π0、H=50 时，PAV 成功率94.30%、平均查询12.3次；固定 h=5 为92.10%、34.6次，AutoHorizon 为94.05%、10.6次。因此并非对所有方法同时更准且更省。[S17](https://arxiv.org/html/2610.21434v1#S3.T1) [S18](https://arxiv.org/html/2610.21434v1#S3.T1.4) Franka 真机放块、叠块、按按钮，每任务30次；PAV 平均成功74.4%、重规划12.87次，固定 h=10 为41.1%、36.54次；查询次数接近的 h=30 为40.0%、11.97次。[S25](https://arxiv.org/html/2610.21434v1#S4.SS1.SSS0.Px3.p1.1) [S30](https://arxiv.org/html/2610.21434v1#S4.SS3.SSS2.p1.1) [S31](https://arxiv.org/html/2610.21434v1#S4.T6) [S32](https://arxiv.org/html/2610.21434v1#S4.T6.2) 这些支持在所测策略和任务中自适应长度有效。

</details>

### 5. [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](items/FastVLA%20Task-Conditioned%20and%20Temporally%20Adaptive%20Visual%20Token%20Compression%20for%20Ef.md)

> FastVLA 每次推理都先看任务主要依赖哪些图像区域，再决定保留多少视觉 token。注意力集中时多裁剪、分散时多保留，不用重新训练就能减少后续大模型计算。

- **能借鉴什么**：可以借鉴的是把预算分配和重要性排序分开：即便已知道哪些信息更重要，也还要判断本步需要多少信息。对于信息需求随阶段变化的闭环任务，平均预算相同也可能因分配方式不同而产生性能差异。
- **值得读吗**：值得读到动态预算公式和等预算消融；它是实用的免训练加速选择，但选型要同时接受实际成功率和硬件延迟检验。

<details><summary>实验依据</summary>

RTX 4090 上，LIBERO/OpenVLA-OFT 的 FLOPs 3.98→1.65T、动作延迟118.52→81.17毫秒，成功率97.0%→96.5%；LightVLA 在相同成功率下更快，但需要训练。[S19](https://arxiv.org/html/2610.22146v1#S4.p1.1) [S30](https://arxiv.org/html/2610.22146v1#S4.SS3.p1.1) 真机两任务每条件50次：抓取延迟121.13→96.90毫秒、成功率84%→80%；抓放120.01→97.77毫秒、68%→66%。加速明确，成功率并非完全不变。[S24](https://arxiv.org/html/2610.22146v1#S4.SS2.p2.1) [S28](https://arxiv.org/html/2610.22146v1#S4.T3.5.1) 接近相同平均 token 预算时，动态方案在四套 LIBERO 任务均优于固定方案，较直接支持动态分配的作用。[S29](https://arxiv.org/html/2610.22146v1#S4.T4.5)

</details>

## 扫读 7 篇

- [Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation](items/Spark-0%20Scaling%20Spatially%20Aligned%20Tactile%20Pretraining%20for%20Robot%20Dexterous%20Manipu.md) — Spark-0 用触觉教视觉识别接触，也让动作模块直接读取触觉。这样训练出的同一模型，既能只靠摄像头执行，也能在有触觉传感器时利用实时接触信息。
- [MOSS: Mode-Oriented Source Shaping for Robot Flow Matching Policies](items/MOSS%20Mode-Oriented%20Source%20Shaping%20for%20Robot%20Flow%20Matching%20Policies.md) — MOSS 让机器人明确选择一种可行行为，而不是把选择交给随机采样。关键是给不同动作方式安排不同的初始噪声分布，执行时从指定分布出发。
- [Fast-VLA: You Only Think Once for Robot Manipulation](items/Fast-VLA%20You%20Only%20Think%20Once%20for%20Robot%20Manipulation.md) — Fast-VLA 每回合只运行一次大型视觉语言模型，把指令和初始画面存成任务记忆。随后由轻量动作模块持续读取新画面、机器人状态和这份记忆，闭环输出动作。
- [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](items/VLA-%24%CE%94%24%20Learning%20Physical%20State%20Transition%20for%20Vision-Language-Action%20Models.md) — VLA-Δ 在训练时明确教模型“当前到未来发生了什么物理变化”，再让它学习动作。推理时仍直接从当前观察生成动作，不需要额外预测一段未来再执行。
- [KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration](items/KODA%20Kinematics--Observation%20Data%20Alignment%20for%20Humanoid%20Learning%20from%20Human%20Ego.md) — KODA 把人类第一视角视频转换成机器人全身动作与对应视角的训练数据。它先保存一份可复用的身体运动记录，再为不同控制器重新生成各自能执行的命令。
- [REKI: Registering Knowledge in VLAs](items/REKI%20Registering%20Knowledge%20in%20VLAs.md) — REKI 是一个 2.4B 参数的视觉语言动作模型，用动作专家里的少量寄存器保存近期视觉信息，让机器人少因忘记刚才发生的事而来回摆动。它还展示了只用公开数据训练较小模型的可行性。
- [EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos](items/EgoJEPA%20Beyond%20Retargeting%20for%20Dexterous%20Manipulation%20from%20Egocentric%20Videos.md) — EgoJEPA 不先把人的手指姿态硬换成机器人关节命令，而是先从第一视角视频学习“动作会带来什么变化”。之后再用轻量动作适配器，把这份知识接到不同机器人上。

## 其余存档 12 篇

- [Trajectory-based Diffusion from One-shot Human Video for Generalizable Manipulation](items/Trajectory-based%20Diffusion%20from%20One-shot%20Human%20Video%20for%20Generalizable%20Manipulat.md) · 世界模型 机器人学习 具身智能评测与基准
- [Value as Memory: Online Value-Guided Post-training for General Robot Policies](items/Value%20as%20Memory%20Online%20Value-Guided%20Post-training%20for%20General%20Robot%20Policies.md) · 智能体 Agent 机器人学习
- [Sim-to-Real Reinforcement Learning for Path-Safe Target Reaching in Robotic Harvesting of Hydroponic Lettuce](items/Sim-to-Real%20Reinforcement%20Learning%20for%20Path-Safe%20Target%20Reaching%20in%20Robotic%20Harv.md) · 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- [Training-Free Target-Aware Refinement of 3D Gaussian Language Map](items/Training-Free%20Target-Aware%20Refinement%20of%203D%20Gaussian%20Language%20Map.md) · 多模态基础模型 机器人学习 具身智能评测与基准
- [Whole-Body Dexterity](items/Whole-Body%20Dexterity.md) · 智能体 Agent Sim2Real
- [What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning](items/What%20Should%20Robot%20Policies%20Learn%20to%20Predict%20Rethinking%20Supervision%20Targets%20in%20Vi.md) · 多模态基础模型 视觉语言动作模型 VLA
- [MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models](items/MAIA%20Anticipating%20Interaction%20Anomalies%20in%20Contact-Rich%20Manipulation%20via%20Multimo.md) · 多模态基础模型 世界模型 具身智能评测与基准
- [LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models](items/LTM%20Latent%20Transition%20Based%20In-Context%20Memory%20for%20Vision-Language-Action%20Models.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习
- [DemoStream: Batched Task-and-Motion-Plan Optimization for Automated Learning from Demonstration](items/DemoStream%20Batched%20Task-and-Motion-Plan%20Optimization%20for%20Automated%20Learning%20from.md) · 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- [TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control](items/TS-WAM%20Temporal%20Latent%20Actions%20and%20World-Action%20Coupling%20for%20Vision-Language%20Rob.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](items/Sub-Millisecond%20Reflexes%20for%20Continuous%20Physical%20Human-Robot%20Interaction.md) · 具身智能评测与基准
- [Cross-Embodiment Causal Transfer from Human Videos to Robot Manipulation](items/Cross-Embodiment%20Causal%20Transfer%20from%20Human%20Videos%20to%20Robot%20Manipulation.md) · 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2348
- 入选条目：24
- 回填已见条目：0
- 最高分论文：CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance
- 最高分论文发布时间：2026-10-15T07:54:39Z
- 主要技术对象分类：具身智能评测与基准 19、多模态基础模型 14、视觉语言动作模型 VLA 13、世界模型 12、机器人学习 10、智能体 Agent 5、Sim2Real 2
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
