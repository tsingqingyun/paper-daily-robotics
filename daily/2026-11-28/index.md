---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: mixed
created: 2026-11-28
---

# 2026-11-28 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 优先阅读建议：今天优先解决的问题是，长流程失败时，怎样定位是哪一步出了错。想判断视觉距离还能不能指路，先读 Graph Anchors 的排序诊断。想估计人工接管数据带来的收益，读 FailPoint-X 对齐更新次数和失败起点的实验，再看正常开局的表现。想评估智能体会不会在证据不足时贸然行动，读 AIRIS 如何给同一段视频的不同时间点设题。
> **趋势**：前五篇的共同线索：这批工作把评估移到错误发生的具体位置：固定仿真起点检验动作效果或恢复能力，截断视频检验判断时机，直接检查工具产物是否有效。这样能定位最终成功率或总分掩盖的问题。

- **规模**：2519 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、世界模型 12、智能体 Agent 9、视觉语言动作模型 VLA 8、多模态基础模型 7、机器人学习 6、AI 核心知识地图 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的结论与启发，点开单篇看方法和依据；需要进一步核查时进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics](items/Co-World%20Model%20for%20Human-Video-to-Robot%20Transfer%20via%20Co-Constructed%20Shared%20Laten.md)

> CoWM 让机器人看一段未见过的人类示范，学着复现物体发生的一连串变化。它按动作对物体的效果来对齐人和机器人，再用机器人已有的动作经验约束执行。

- **能借鉴什么**：跨机器人迁移时，可以先明确什么结果值得复用，再决定控制信号该怎么映射。物体关系的变化若容易跟踪，就可以用同起点换动作的测试，检查共享表示能否支撑实际替换，早于整段任务成功率暴露问题。
- **值得读吗**：值得读到两条训练约束和同状态干预协议，它们决定了“效果相同就可以替换”究竟能检验到什么程度。

<details><summary>实验依据</summary>

仿真覆盖 30 个 LIBERO 操作任务和 120 段留出视频，另用 ManiSkill 做跨基准测试 [S23](https://arxiv.org/html/2611.34302v1#S4.SS1.p1.1)。两台实体机器人各做同样的 5 个桌面任务，每任务 15 次 [S24](https://arxiv.org/html/2611.34302v1#S4.SS1.p2.1)。对照包括直接映射、只看终点的规划器，以及共用骨干和规划器但省去联合训练的模型 [S28](https://arxiv.org/html/2611.34302v1#S4.SS1.p3.1)。指标包括任务成功率、末端物体平移误差，以及同一仿真状态下的效果复现率和不同效果拒绝率 [S29](https://arxiv.org/html/2611.34302v1#S4.SS1.p4.1)[S31](https://arxiv.org/html/2611.34302v1#S4.SS2.p2.1)。摘要报告两类环境均验证了方法，但节选没有给出各平台的成绩、对照差值或干预结果，因而无法量化优势和各组件的贡献。

</details>

### 2. [Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments](items/Crucible%20Evaluating%20LLM%20Agents%20in%20Executable%20Chemistry%20Research%20Environments.md)

> Crucible Bench 让语言模型用专业软件完成化学任务，然后检查它交出的结果。软件顺利跑完也可能得到化学上无效的答案，评分器会按任务规则检查这一点。

- **能借鉴什么**：设计工具型智能体评测时，可以分别记录软件是否运行成功、输出是否通过领域检查、最终提交是否遵守这些检查。这样才能区分工具选错、参数设错，以及工具已经指出问题但模型仍提交错误结果。
- **值得读吗**：值得读到评分规则和误差案例，因为它们决定了一次扣分究竟意味着科学判断出错，还是答案与参考不同。

<details><summary>实验依据</summary>

评测在 7 个隔离环境中给智能体提供 75 种工具，涵盖 12 个任务族、1,078 道题 [S6](https://arxiv.org/html/2611.34254v1#S1.p4.1)。14 个模型的最高总分是 0.545，总排名第 12 的模型反而在闭环优化上第一 [S1](https://arxiv.org/html/2611.34254v1#abstract1.1)。优化分数以等预算随机搜索的期望最佳值为参照 [S22](https://arxiv.org/html/2611.34254v1#S3.SS3.p4.1)。禁用工具后所有模型得分都明显下降 [S28](https://arxiv.org/html/2611.34254v1#S5.SS2.p1.1)，表明工具访问在这套评测中有贡献。节选未给出各模型的禁用前后分差或不确定性，难以进一步判断增益差异。

</details>

### 3. [FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers](items/FailPoint-X%20A%20Policy-Matched%2C%20Failure-Anchored%20Benchmark%20for%20Offline%20VLA%20Post-Tr.md)

> FailPoint-X 让机器人策略从同一个失败现场重新开始，测它能不能自己补救。它用同样的更新次数比较模仿人工接管和继续学原示范，并另外测正常开局的成功率。

- **能借鉴什么**：做纠错后训练时，值得保留两套起点：真实出错后到达的状态，用于测补救；任务自然开局的状态，用于测原技能。混合数据看起来能保住多少原技能，还可能取决于给策略多少时间。
- **值得读吗**：值得细读表 3 和恢复评测协议。这里最可复用的是如何控制起点和训练预算，以及如何同时发现恢复收益与原技能损失。

<details><summary>实验依据</summary>

在 LIBERO-X 仿真的 240 个 L1–L3 留出失败上，给 1,200 步，Takeover-BC 恢复成功率为 51.9%，Demo-continue 为 22.5%，差 +29.4 个百分点，按任务家族配对的 95% 区间为 +16.9 至 +44.7 [S1](https://arxiv.org/html/2611.33769v1#abstract1.1)[S23](https://arxiv.org/html/2611.33769v1#S5.SS1.SSS0.Px1.p1.1)。IQL-R2 相对克隆多 1.5 个百分点，区间跨零 [S18](https://arxiv.org/html/2611.33769v1#S4.T3.10)。探索性正常开局测试中，纯克隆和混合训练比原策略低 30.0 和 16.5 个百分点，缩短时限后两者的损失更接近 [S9](https://arxiv.org/html/2611.33769v1#S1.p6.1)。主对照支持这批接管数据整体带来恢复收益 [S23](https://arxiv.org/html/2611.33769v1#S5.SS1.SSS0.Px1.p1.1)。

</details>

### 4. [Long-Horizon Planning with Latent World Models via Graph Anchors](items/Long-Horizon%20Planning%20with%20Latent%20World%20Models%20via%20Graph%20Anchors.md)

> Graph Anchors 把远处的目标图片拆成沿历史轨迹可逐步追踪的近目标。它用已有画面建图找路线，再让冻结的世界模型带着控制器一段一段走。

- **能借鉴什么**：如果世界模型能稳定做好短程控制，先用已有轨迹测目标距离会不会给候选动作排错序。若问题集中在远距离或接触阶段，可以先改目标的选法，再决定是否值得投入更多搜索或重训预测器。
- **值得读吗**：值得细读排序诊断和目标选择消融，这两处能帮助判断瓶颈出在动作预测、搜索强度，还是目标评分本身。

<details><summary>实验依据</summary>

仿真长目标表中，同一组起终点上，Graph Anchors 将 LeWM 的成功率从 13% 提至 85%（PointMaze-Medium，200 步），从 8% 提至 87%（PointMaze-Large，400 步），以及从 5% 提至 71%（Push-T，150 步，接触设置）。只给远目标加途中最近评分时，三项分别为 12%、26%、9% [S14](https://arxiv.org/html/2611.34509v1#S5.p1.1)–[S16](https://arxiv.org/html/2611.34509v1#S5.T1.10)。这支持近锚点在这些环境中的作用。同期对照也有局部强项，例如 NGC 在中型迷宫 200 步达到 100% [S23](https://arxiv.org/html/2611.34509v1#S5.T3.6.1)。

</details>

### 5. [AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos](items/AIRIS%20Benchmarking%20Social%20Embodied%20Intelligence%20in%20Egocentric%20Streaming%20Videos.md)

> AIRIS 用第一视角视频测试模型能否看懂社交线索、等到证据足够，再选对什么时候介入和怎么回应。它在同一段互动的多个时间点提问，每次只给当时能看到、听到的信息。

- **能借鉴什么**：评估会主动介入的智能体，可以在同一事件的早晚阶段分别发问，并给恰当等待记分。再对同一次回应做联合评分，才能看出模型是否把几个各自合理的答案拼成了时机和内容都合适的行动。
- **值得读吗**：值得读到时间标注和严格联合评分，因为它们把“猜得过早”和“局部答对、整体配错”变成了可单独检查的错误。

<details><summary>实验依据</summary>

评测比较 45 个通用、具身、流式视频和全模态模型，在 357 段第一视角片段上回答 8,000 道题 [S6](https://arxiv.org/html/2611.34347v1#S1.p4.1)[S20](https://arxiv.org/html/2611.34347v1#S3.SS1.p1.1)[S21](https://arxiv.org/html/2611.34347v1#S3.SS1.p2.1)。Gemini-3.7-Flash 在证据不足时仍有 42% 的查询给出具体意图 [S24](https://arxiv.org/html/2611.34347v1#S3.SS2.p3.1)。HY-Embodied-VLM-1.0 的回应分项汇总为 0.688，严格联合得分只有 0.028，所有模型的联合得分都未超过 0.147 [S25](https://arxiv.org/html/2611.34347v1#S3.SS2.p4.1)。这说明在这套视频问答里，看懂线索、选对单项回应与完整答对同一事件之间存在明显差距。

</details>

## 扫读 7 篇

- [BOT-Scale: A Traceable Evaluation Methodology for Robotic Manipulation](items/BOT-Scale%20A%20Traceable%20Evaluation%20Methodology%20for%20Robotic%20Manipulation.md) — BOT-Scale 给机器人操作打分时，把每笔扣分绑到一个能回查的行为事件上。物体中途掉落后又被捡起，即使任务最终完成，读者也能从分数里查到掉落为何影响了评价。
- [Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models](items/Rehearse%20in%203D%2C%20Render%20in%202D%20Physically%20Consistent%20and%20Editable%20Robot%20World%20Mode.md) — RehearsalWorld 先在三维空间预演物体怎么动、夹爪是否持续抓住它，再把这段运动投影给视频生成器。这样，物体结构和接触关系可以在生成画面前单独处理。
- [Towards 360$^\circ$ Embodied UAV Tracking Without Turning](items/Towards%20360%24%20circ%24%20Embodied%20UAV%20Tracking%20Without%20Turning.md) — 360UAV-TVLA 让无人机用全景画面持续认出被指定的目标，并结合过去的观测和三维轨迹监督学习如何跟飞。这样，目标即使移到机身侧后方，跟踪也可以在机头朝向不主动调整的设定下继续。
- [Dynamic Forcing: Learning Action-Grounded Sparse Dynamic Representations with Dense Future Guidance for World Action Models](items/Dynamic%20Forcing%20Learning%20Action-Grounded%20Sparse%20Dynamic%20Representations%20with%20Den.md) — CompactWAM 保留当前画面作参照，只用少量动态 token 表达接下来可能发生的变化。Dynamic Forcing 在训练时用真实动作目标和密集未来信息教这些 token 该保留什么，执行时只用紧凑表示生成动作。
- [WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation](items/WhatIf%20Counterfactual%20World%20Models%20over%20Action-Grounded%20Causal%20Graphs%20for%20Roboti.md) — WhatIf 比较机器人可以采取的动作时，先用同一段历史推断物理状态和随机扰动，再让各候选动作共享这些条件。CAP 据此估计改用新方案相对当前方案的收益，以及改换后结果变差的概率。
- [Distractor-Robust Reinforcement Learning via Variational Bisimulation](items/Distractor-Robust%20Reinforcement%20Learning%20via%20Variational%20Bisimulation.md) — 背景一直在变时，世界模型可能忙着记住背景。VIBES 把像素重建换成对抗式训练，让有限的状态表示优先保留预测奖励和下一状态所需的信息。
- [Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models](items/Commit2Drive%20Perception-Grounded%20Language%20Decisions%20as%20Commitments%20for%20Trajector.md) — 会说要做什么的驾驶模型，有时会规划出另一种动作。Commit2Drive 把语言决策写成能从轨迹反查的机动类别和连续参数，并训练规划器兑现这项承诺。

## 其余存档 12 篇

- [Embodied Lower-limb Exoskeleton Assistance: Survey, Challenges, and Perspectives](items/Embodied%20Lower-limb%20Exoskeleton%20Assistance%20Survey%2C%20Challenges%2C%20and%20Perspectives.md) · AI 核心知识地图
- [CoTacWAM: Joint Modeling of Vision and Touch for Robotic Manipulation](items/CoTacWAM%20Joint%20Modeling%20of%20Vision%20and%20Touch%20for%20Robotic%20Manipulation.md) · 视觉语言动作模型 VLA 具身智能评测与基准
- [RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies](items/RePace%20Reasoning%20about%20Demonstration%20Speedup%20for%20Faster%20Vision-Language-Action%20P.md) · 多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [Beyond Natural-Language Instructions: Temporal Logic as a Task Language for VLA Models with Visual-Logical Fusion](items/Beyond%20Natural-Language%20Instructions%20Temporal%20Logic%20as%20a%20Task%20Language%20for%20VLA%20M.md) · 多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- [A Simple Yet Effective Agent for Open-World Aerial Object Search](items/A%20Simple%20Yet%20Effective%20Agent%20for%20Open-World%20Aerial%20Object%20Search.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [MMotion: Collaborative Cross-Scale Memory for Text-to-Motion Generation](items/MMotion%20Collaborative%20Cross-Scale%20Memory%20for%20Text-to-Motion%20Generation.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [PROVE: Predict-to-Specify and Observe-to-Verify for Human-Aligned Evaluation of Mobile Manipulation](items/PROVE%20Predict-to-Specify%20and%20Observe-to-Verify%20for%20Human-Aligned%20Evaluation%20of%20M.md) · 多模态基础模型 具身智能评测与基准
- [Split-RL: Local Conflict Resolution in Reinforcement Learning](items/Split-RL%20Local%20Conflict%20Resolution%20in%20Reinforcement%20Learning.md) · 机器人学习
- [Geometric Acceleration Obstacles: Physical Boundary Structure and Affine Safety Certificates](items/Geometric%20Acceleration%20Obstacles%20Physical%20Boundary%20Structure%20and%20Affine%20Safety%20C.md) · 智能体 Agent 世界模型 具身智能评测与基准
- [Hetero-Associative Visuomotor Memory: Soft Recall as a Base for Learned Residuals in Few-Demonstration Imitation](items/Hetero-Associative%20Visuomotor%20Memory%20Soft%20Recall%20as%20a%20Base%20for%20Learned%20Residuals.md) · 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- [CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution Matching](items/CondUQ%20Calibrated%20Conditional%20Uncertainty%20Quantification%20Using%20Distribution%20Matc.md) · 世界模型 具身智能评测与基准
- [Practice Makes Fluent: Learning to Use Earlier Predictions in Looped Models](items/Practice%20Makes%20Fluent%20Learning%20to%20Use%20Earlier%20Predictions%20in%20Looped%20Models.md) · 具身智能评测与基准

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2519
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics
- 最高分论文发布时间：2026-11-25T12:54:52Z
- 主要技术对象分类：具身智能评测与基准 16、世界模型 12、智能体 Agent 9、视觉语言动作模型 VLA 8、多模态基础模型 7、机器人学习 6、AI 核心知识地图 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Google DeepMind Blog: not well-formed (invalid token): line 1, column 0 (after 3 attempts)

</details>
