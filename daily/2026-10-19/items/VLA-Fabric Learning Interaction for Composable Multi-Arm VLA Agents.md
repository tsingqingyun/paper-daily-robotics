---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.23018v1"
published: "2026-10-16T06:52:37Z"
age_days: 3
score: 42
created: 2026-10-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> VLA-Fabric 给每条机械臂保留一套完整 VLA，同时让它们在内部交换信息，共同决定动作。关键不只是共享画面，而是在共享上下文、同伴内部表示和动作生成阶段分别学习怎样配合。

## 问题

递物或共同托举时，每条臂的动作都依赖其他臂的状态。集中式联合策略、上层角色分配和观察同伴后的被动反应各有组织方式；本文要解决的是：怎样保留每臂完整策略的独立接口，又让紧密耦合的动作互相适配。[S3](https://arxiv.org/html/2610.23018v1#S1.p2.1) [S4](https://arxiv.org/html/2610.23018v1#S1.p3.1) [S5](https://arxiv.org/html/2610.23018v1#S1.p4.1)

### 用一个例子理解

理解用例（非论文实验）：输入“三条臂协作装盒”、各臂相机与关节状态；持盒臂与递物臂交换内部表示，递物臂据此调整位置和交接动作；输出各自的动作，而非一个统一控制所有关节的动作向量。

## 创新点或方法

从单臂策略分支出发，保留本地观测和动作输出，再通过三个位置接入同伴表示：共享上下文、私有中间表示、动作侧交互。作者比较接入位置、聚合方式和训练顺序，发现先学 Common、再加其余交互的 Common-first 更有效。[S16](https://arxiv.org/html/2610.23018v1#S3.SS2.p2.1) [S17](https://arxiv.org/html/2610.23018v1#S3.SS2.p4.1) [S18](https://arxiv.org/html/2610.23018v1#S3.SS2.p6.1) 训练要让策略学会使用通信，推理时也继续交换表示；不是把独立训练的策略接上线就能协作。相同功能在 SingleVLA 和 π₀.₅ 中分别实现，不代表权重直接迁移。

### 方法如何工作

1. 各臂用完整本地 VLA 处理自己的观测，保留本地动作生成能力。
2. 在共享上下文和中间表示处接入同伴信息，让本地策略了解其他臂掌握的条件。
3. 在动作生成阶段继续交互，使输出动作适应交接或共同支撑的约束。
4. 通过任务微调学会利用这些接口，推理时维持交换；更大团队则增加本地策略并扩展交互。

### 必要术语

- 本地动作所有权：每套策略只输出自己机械臂的动作；保持执行单位可组合。
- Private K/V：同伴内部注意力使用的键和值表示；传递本地策略加工过的信息。
- 动作侧交互：生成动作时融合同伴表示；帮助协调具体运动。
- Common-first：先学习共享上下文交互，再加入其他通路；是本文比较的训练顺序。

## 证据

真机覆盖三臂放篮、三臂接力、四臂接力和四臂套框；每任务收集 50 条示范，每种策略测试 25 次。[S26](https://arxiv.org/html/2610.23018v1#S6.p1.1) 相比独立训练策略，Full 成功率依次为 72→88%、16→56%、40→72%、36→60%。[S33](https://arxiv.org/html/2610.23018v1#S6.T3.2) 仿真还做固定权重的推理期通路移除，显示不同任务依赖不同信息；但临时关闭训练时用过的通路，与从头训练无通信策略是两种比较，不能混用。[S21](https://arxiv.org/html/2610.23018v1#S4.T1.2) [S22](https://arxiv.org/html/2610.23018v1#S4.SS2.p2.1) [S41](https://arxiv.org/html/2610.23018v1#A1.SS5.p2.1)

## 局限

作者指出长程精密装配仍难，交互不能自动补足单个 VLA 的规划和控制能力。[S25](https://arxiv.org/html/2610.23018v1#S5.p2.1) 我的待核查问题是通信带宽、同步延迟及新增机械臂需要多少再训练；三四臂结果不等于任意规模即插即用。另有 π₀.₅ 双臂对照训练预算不等，不能把全部差距归给交互。[S42](https://arxiv.org/html/2610.23018v1#A2.SS4.p1.1)

- **判断**：值得读到交互接口和训练对照：它对“完整策略之间怎样协作”给出了实证，但规模扩展仍应按具体任务评估。

## 研究关联

具体启示是按物理依赖设计通信：并行放置可能不需要很多交流，递物则需要知道对方是否能接住，共同托举还要使动作相容。结果更支持“耦合方式决定信息需求”，而不是机械臂越多就一定越需要更强通信。[S25](https://arxiv.org/html/2610.23018v1#S5.p2.1) [S34](https://arxiv.org/html/2610.23018v1#S6.p2.1)

### 下一步读哪里

先看 [S16](https://arxiv.org/html/2610.23018v1#S3.SS2.p2.1) [S17](https://arxiv.org/html/2610.23018v1#S3.SS2.p4.1) [S18](https://arxiv.org/html/2610.23018v1#S3.SS2.p6.1) 的接入、聚合和 Common-first，再对照 [S21](https://arxiv.org/html/2610.23018v1#S4.T1.2) [S22](https://arxiv.org/html/2610.23018v1#S4.SS2.p2.1) [S41](https://arxiv.org/html/2610.23018v1#A1.SS5.p2.1) [S42](https://arxiv.org/html/2610.23018v1#A2.SS4.p1.1) 分清重训与推理移除；部署前核查通信量、同步要求及新增角色的数据需求。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- **筛选分数**：42
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.23018v1
- 获取时间：2026-10-19T15:35:21.247384+00:00
- [S1] [VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents · 正文段落 1](https://arxiv.org/html/2610.23018v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.23018v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.23018v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.23018v1#S1.p3.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.23018v1#S1.p4.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.23018v1#S1.p5.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.23018v1#S1.p6.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.23018v1#S1.p7.1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.23018v1#S1.p9.1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.23018v1#S1.p10.1)
- [S11] [Cooperative physical manipulation. · 正文段落 13](https://arxiv.org/html/2610.23018v1#S2.SS0.SSS0.Px1.p1.1)
- [S12] [Learned interaction among embodied policies. · 正文段落 15](https://arxiv.org/html/2610.23018v1#S2.SS0.SSS0.Px3.p1.1)
- [S13] [3.1 Local VLA Agents and the Interaction Problem · 正文段落 16](https://arxiv.org/html/2610.23018v1#S3.SS1.p1.1)
- [S14] [3.1 Local VLA Agents and the Interaction Problem · 正文段落 19](https://arxiv.org/html/2610.23018v1#S3.SS1.p2.2)
- [S15] [3.2 Discovering the Interaction Architecture · 正文段落 24](https://arxiv.org/html/2610.23018v1#S3.SS2.p1.1)
- [S16] [3.2 Discovering the Interaction Architecture · 正文段落 25](https://arxiv.org/html/2610.23018v1#S3.SS2.p2.1)
- [S17] [3.2 Discovering the Interaction Architecture · 正文段落 27](https://arxiv.org/html/2610.23018v1#S3.SS2.p4.1)
- [S18] [3.2 Discovering the Interaction Architecture · 正文段落 29](https://arxiv.org/html/2610.23018v1#S3.SS2.p6.1)
- [S19] [4.2 Cross-Architecture Results and Interaction Use · 正文段落 35](https://arxiv.org/html/2610.23018v1#S4.SS2.p1.1)
- [S20] [4.2 Cross-Architecture Results and Interaction Use · 正文段落 36](https://arxiv.org/html/2610.23018v1#S4.T1)
- [S21] [4.2 Cross-Architecture Results and Interaction Use · 正文段落 37](https://arxiv.org/html/2610.23018v1#S4.T1.2)
- [S22] [4.2 Cross-Architecture Results and Interaction Use · 正文段落 38](https://arxiv.org/html/2610.23018v1#S4.SS2.p2.1)
- [S23] [5 Scaling VLA-Fabric Beyond Bimanual Manipulation · 正文段落 43](https://arxiv.org/html/2610.23018v1#S5.F4)
- [S24] [5 Scaling VLA-Fabric Beyond Bimanual Manipulation · 正文段落 45](https://arxiv.org/html/2610.23018v1#S5.T2)
- [S25] [5 Scaling VLA-Fabric Beyond Bimanual Manipulation · 正文段落 47](https://arxiv.org/html/2610.23018v1#S5.p2.1)
- [S26] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 48](https://arxiv.org/html/2610.23018v1#S6.p1.1)
- [S27] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 49](https://arxiv.org/html/2610.23018v1#S6.F5.2.1)
- [S28] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 50](https://arxiv.org/html/2610.23018v1#S6.F5.2.2)
- [S29] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 51](https://arxiv.org/html/2610.23018v1#S6.F5.2.3)
- [S30] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 52](https://arxiv.org/html/2610.23018v1#S6.F5.2.4)
- [S31] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 53](https://arxiv.org/html/2610.23018v1#S6.F5)
- [S32] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 54](https://arxiv.org/html/2610.23018v1#S6.T3)
- [S33] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 55](https://arxiv.org/html/2610.23018v1#S6.T3.2)
- [S34] [6 VLA-Fabric in Real-World Multi-Arm Systems · 正文段落 56](https://arxiv.org/html/2610.23018v1#S6.p2.1)
- [S35] [7 Discussion and Limitations · 正文段落 57](https://arxiv.org/html/2610.23018v1#S7.p1.1)
- [S36] [8 Conclusion · 正文段落 59](https://arxiv.org/html/2610.23018v1#S8.p1.1)
- [S37] [AI Use Statement · 正文段落 60](https://arxiv.org/html/2610.23018v1#Sx1.p1.1)
- [S38] [Appendix · 正文段落 62](https://arxiv.org/html/2610.23018v1#Ax1.p1.1)
- [S39] [A.3 Experimental Setup · 正文段落 77](https://arxiv.org/html/2610.23018v1#A1.SS3.p1.1)
- [S40] [A.5 Architecture Selection and SingleVLA Controls · 正文段落 86](https://arxiv.org/html/2610.23018v1#A1.T3)
- [S41] [A.5 Architecture Selection and SingleVLA Controls · 正文段落 89](https://arxiv.org/html/2610.23018v1#A1.SS5.p2.1)
- [S42] [B.4 Additional Interaction Controls · 正文段落 103](https://arxiv.org/html/2610.23018v1#A2.SS4.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/VLA-Fabric Learning Interaction for Composable Multi-Arm VLA Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models are rapidly expanding what individual robots can accomplish, yet many real-world manipulation settings require multiple arms to operate as a coordinated system. Existing approaches organize multi-arm coordination in different ways, including centralized joint policies, high-level task or role assignment, and locally executed policies that react to teammates. However, how complete action-producing VLAs should explicitly interact with one another during action generation remains largely unexplored. We introduce VLA-Fabric, which organizes one complete VLA per arm while preserving local perception and action ownership, and enables coordination through learned interaction across policy boundaries. We first systematically study where such interaction should occur, how peer information should be aggregated, and how the interaction should be learned, revealing complementary coordination functions spanning shared context, peer-specific latent information, and action-stage interaction. We then re-instantiate these functions in a structurally different VLA architecture, showing that the coordination principle is not tied to a particular tensor layout or backbone implementation. Finally, we compose teams of three and four arms and evaluate them in simulation and physical experiments. On all four physical tasks, Full interaction improves success over independently trained local policies by 16--40 percentage points. Together, these results suggest that explicit interaction among complete VLA policies offers a scalable path toward networked embodied intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23018v1
- Authors: Chenglong Zhang, Shuaijun Liu, Feiyang You, Shuyang Hao, Chengyu Wu, Ningxin Su
- Published: 2026-10-16T06:52:37Z
- Age days: 3

</details>
