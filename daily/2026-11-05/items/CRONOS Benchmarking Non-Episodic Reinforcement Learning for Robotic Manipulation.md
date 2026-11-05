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
url: "https://arxiv.org/abs/2611.05080v1"
published: "2026-11-03T15:41:07Z"
age_days: 1
score: 44
created: 2026-11-05
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> CRONOS 研究机器人不再每做完一个任务就被人工摆回原样时，VLA 还能不能靠强化学习进步。关键发现是要分别处理机械臂起始姿态漂移和物体越弄越乱，并把有限重置用在训练早期或已经无法继续的场景上。

## 问题

任务是在共享桌面上连续抓放。常规 RL 每轮重置，悄悄替机器人清除了上轮错误；取消这项便利后，新任务从陌生布局和手臂姿态开始，甚至物体已掉出工作区。过去面向小策略、从零训练的非回合方法，不能直接回答预训练 VLA 是否适应这些变化。

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放进碗”，上轮留下积木靠桌边、机械臂停在碗上方；系统先归位机械臂，保留桌面继续训练；若积木已掉落，才重置场景，再收集能产生奖励的轨迹。

## 创新点或方法

旧做法是固定间隔重置整个场景；本文拆开干预：切任务时自动归位末端执行器 EER，先较频繁重置再延长间隔 CL，以及检测物体掉落或越界后强制重置 HSR。它们分别减少姿态偏移、逐步扩大训练状态范围、终止不可能成功的采样。训练用 PPO 微调 OpenVLA、SpatialVLA；部署时仍由策略根据观测和指令出动作，重置属于训练环境管理。评估包含独立任务与连续任务，不能把非回合训练理解成所有测试都不重置。[S9](https://arxiv.org/html/2611.05080v1#S2.SS0.SSS0.Px2.p1.1) [S12](https://arxiv.org/html/2611.05080v1#S3.SS1.p2.1) [S13](https://arxiv.org/html/2611.05080v1#S3.SS1.p3.1) [S14](https://arxiv.org/html/2611.05080v1#S3.SS1.p4.1) [S15](https://arxiv.org/html/2611.05080v1#S3.SS1.p5.1) [S25](https://arxiv.org/html/2611.05080v1#S4.p1.1) [S26](https://arxiv.org/html/2611.05080v1#S4.SS1.p1.1) [S27](https://arxiv.org/html/2611.05080v1#S4.SS1.p3.1) [S28](https://arxiv.org/html/2611.05080v1#S4.SS2.p3.1) [S29](https://arxiv.org/html/2611.05080v1#S4.SS3.p1.1) [S30](https://arxiv.org/html/2611.05080v1#S4.F8.fig1.2) [S31](https://arxiv.org/html/2611.05080v1#S4.F8.fig1) [S32](https://arxiv.org/html/2611.05080v1#S4.SS3.p2.1) [S33](https://arxiv.org/html/2611.05080v1#S4.SS3.p3.1)

### 方法如何工作

1. 让多个任务共享场景，下一任务继承上轮结果，使训练暴露于实际累积的错误。
2. 切任务时归位末端执行器，减少预训练起始姿态与当前姿态的差距。
3. 早期多重置、后期少重置，让策略先学会成功，再接触更分散的布局。
4. 检查掉落和越界，遇到不可恢复场景便重置，恢复有效学习信号。

### 必要术语

- 非回合训练：任务切换时通常保留环境；本文用它研究错误如何跨任务累积。
- 初始状态分布漂移：新任务开始时的状态越来越不同于熟悉状态；本文分别检查物体布局和机械臂姿态。
- 重置效率：用多少次场景恢复换来学习效果；需要与交互效率一起衡量。

## 证据

仿真含四场景、16 个抓放任务，以成功率衡量。重置间隔从 80 增至 320、2560 步，OpenVLA 从 65% 降至 37%、0%，SpatialVLA 从 65% 降至 25%、2% [S17](https://arxiv.org/html/2611.05080v1#S3.SS2.p1.1)。SpatialVLA 加 EER 分别提高 25、10 个百分点 [S27](https://arxiv.org/html/2611.05080v1#S4.SS1.p3.1)；CL 的域内/域外成功率为 40%/32%，对应基线为 14%/8% [S28](https://arxiv.org/html/2611.05080v1#S4.SS2.p3.1)；HSR 域内为 64%，无 HSR 为 14% [S32](https://arxiv.org/html/2611.05080v1#S4.SS3.p2.1)。这些是不同干预比较，不能相加。节选只定性报告连续任务与新布局收益，未给对应数值。

## 局限

结果主要来自仿真；HSR 触发场景重置仍意味着现实中的人工成本。EER 干预支持姿态漂移会影响学习，但不足以排除其他原因；节选也不足以判断真实重置耗时及检测误差。

- **判断**：值得读到重置策略及其成本比较：它把连续学习失败拆成了可干预的具体原因，但尚不能当作真机免维护训练方案。

## 研究关联

减少人工干预时，应同时统计每次交互学到了多少、用了多少次重置。尤其值得借鉴的是区分“困难但还能恢复”和“已经无法完成”：后者继续采样，只会耗掉交互预算。

### 下一步读哪里

先看 [S12](https://arxiv.org/html/2611.05080v1#S3.SS1.p2.1) [S13](https://arxiv.org/html/2611.05080v1#S3.SS1.p3.1) [S14](https://arxiv.org/html/2611.05080v1#S3.SS1.p4.1) [S15](https://arxiv.org/html/2611.05080v1#S3.SS1.p5.1) [S16](https://arxiv.org/html/2611.05080v1#S3.F2) [S17](https://arxiv.org/html/2611.05080v1#S3.SS2.p1.1) 的训练与评估协议，再核查 [S27](https://arxiv.org/html/2611.05080v1#S4.SS1.p3.1) [S28](https://arxiv.org/html/2611.05080v1#S4.SS2.p3.1) [S29](https://arxiv.org/html/2611.05080v1#S4.SS3.p1.1) [S30](https://arxiv.org/html/2611.05080v1#S4.F8.fig1.2) [S31](https://arxiv.org/html/2611.05080v1#S4.F8.fig1) [S32](https://arxiv.org/html/2611.05080v1#S4.SS3.p2.1) [S33](https://arxiv.org/html/2611.05080v1#S4.SS3.p3.1) [S34](https://arxiv.org/html/2611.05080v1#S4.F9) 各比较共享哪些设置、实际用了多少次重置；连续任务收益需要进一步检查具体结果与失败累计方式。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.05080v1
- 获取时间：2026-11-05T00:11:38.809627+00:00
- [S1] [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2611.05080v1#abstract1.1)
- [S2] [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation · 正文段落 2](https://arxiv.org/html/2611.05080v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.05080v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.05080v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.05080v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.05080v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.05080v1#S1.p5.1)
- [S8] [Multi-task RL. · 正文段落 9](https://arxiv.org/html/2611.05080v1#S2.SS0.SSS0.Px1.p1.1)
- [S9] [Non-episodic Scene Reset Multi-Task RL (NSR-MTRL). · 正文段落 11](https://arxiv.org/html/2611.05080v1#S2.SS0.SSS0.Px2.p1.1)
- [S10] [3 Non-episodic scene reset trades interaction efficiency for reset efficiency · 正文段落 13](https://arxiv.org/html/2611.05080v1#S3.p1.1)
- [S11] [3.1 A Challenging Benchmark for NSR-MTRL · 正文段落 14](https://arxiv.org/html/2611.05080v1#S3.SS1.p1.1)
- [S12] [3.1 A Challenging Benchmark for NSR-MTRL · 正文段落 15](https://arxiv.org/html/2611.05080v1#S3.SS1.p2.1)
- [S13] [3.1 A Challenging Benchmark for NSR-MTRL · 正文段落 16](https://arxiv.org/html/2611.05080v1#S3.SS1.p3.1)
- [S14] [3.1 A Challenging Benchmark for NSR-MTRL · 正文段落 17](https://arxiv.org/html/2611.05080v1#S3.SS1.p4.1)
- [S15] [3.1 A Challenging Benchmark for NSR-MTRL · 正文段落 18](https://arxiv.org/html/2611.05080v1#S3.SS1.p5.1)
- [S16] [3.1 A Challenging Benchmark for NSR-MTRL · 正文段落 19](https://arxiv.org/html/2611.05080v1#S3.F2)
- [S17] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 20](https://arxiv.org/html/2611.05080v1#S3.SS2.p1.1)
- [S18] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 21](https://arxiv.org/html/2611.05080v1#S3.SS2.p2.1)
- [S19] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 22](https://arxiv.org/html/2611.05080v1#S3.F3.sf1)
- [S20] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 23](https://arxiv.org/html/2611.05080v1#S3.F3.sf2)
- [S21] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 24](https://arxiv.org/html/2611.05080v1#S3.F3.sf3)
- [S22] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 25](https://arxiv.org/html/2611.05080v1#S3.F3)
- [S23] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 26](https://arxiv.org/html/2611.05080v1#S3.F4)
- [S24] [3.2 Pretrained VLAs Struggle to Learn under Non-Episodic Scene Resets · 正文段落 27](https://arxiv.org/html/2611.05080v1#S3.F5)
- [S25] [4 Targeted Resets Enable Non-Episodic Scene Reset Fine-Tuning · 正文段落 28](https://arxiv.org/html/2611.05080v1#S4.p1.1)
- [S26] [4.1 End-Effector Resets Reduce Initial-State Distribution Drift · 正文段落 29](https://arxiv.org/html/2611.05080v1#S4.SS1.p1.1)
- [S27] [4.1 End-Effector Resets Reduce Initial-State Distribution Drift · 正文段落 31](https://arxiv.org/html/2611.05080v1#S4.SS1.p3.1)
- [S28] [4.2 Frequent Scene Resets Early Improve NSR-MTRL Efficiency · 正文段落 34](https://arxiv.org/html/2611.05080v1#S4.SS2.p3.1)
- [S29] [4.3 Resetting Unrecoverable Scenes Prevent Loss of Learning Signals · 正文段落 36](https://arxiv.org/html/2611.05080v1#S4.SS3.p1.1)
- [S30] [4.3 Resetting Unrecoverable Scenes Prevent Loss of Learning Signals · 正文段落 37](https://arxiv.org/html/2611.05080v1#S4.F8.fig1.2)
- [S31] [4.3 Resetting Unrecoverable Scenes Prevent Loss of Learning Signals · 正文段落 38](https://arxiv.org/html/2611.05080v1#S4.F8.fig1)
- [S32] [4.3 Resetting Unrecoverable Scenes Prevent Loss of Learning Signals · 正文段落 39](https://arxiv.org/html/2611.05080v1#S4.SS3.p2.1)
- [S33] [4.3 Resetting Unrecoverable Scenes Prevent Loss of Learning Signals · 正文段落 40](https://arxiv.org/html/2611.05080v1#S4.SS3.p3.1)
- [S34] [4.3 Resetting Unrecoverable Scenes Prevent Loss of Learning Signals · 正文段落 42](https://arxiv.org/html/2611.05080v1#S4.F9)
- [S35] [5 Non-Episodic Training Brings Benefits Beyond Reset Efficiency · 正文段落 44](https://arxiv.org/html/2611.05080v1#S5.F10)
- [S36] [5.2 Continual Training Improves Sequential Task Execution · 正文段落 51](https://arxiv.org/html/2611.05080v1#S5.F11.2)
- [S37] [6 Related Work · 正文段落 53](https://arxiv.org/html/2611.05080v1#S6.p1.1)
- [S38] [6 Related Work · 正文段落 54](https://arxiv.org/html/2611.05080v1#S6.p2.1)
- [S39] [7 Conclusion · 正文段落 55](https://arxiv.org/html/2611.05080v1#S7.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-05/CRONOS Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning (RL) is promising for adapting robot policies to unstructured real-world environments. However, standard RL pipelines rely on episodic training with frequent scene resets, which is impractical for real-world deployment due to the need for substantial human intervention. While prior work has studied non-episodic RL in relatively small policies trained from scratch, its behavior when fine-tuning modern large-scale pre-trained vision-language-action (VLA) models remains underexplored. In this work, we introduce CRONOS, a simulation benchmark for RL fine-tuning of VLAs under non-episodic scene resets. CRONOS leverages high-fidelity physics simulators and adopts shared-scene multi-task settings. Using CRONOS, we show that naively fine-tuning pre-trained policies fails in non-episodic settings due to shifts in object configurations and end-effector poses; however, these challenges can be mitigated through targeted reset allocation and by addressing biases in pre-trained models. Moreover, we find that non-episodic training enhances long-horizon manipulation and improves generalization to previously unseen object configurations and task sequences. Project page: https://embodiedai-ntu.github.io/cronos/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.05080v1
- Authors: Po-Yi Wu, Djengo Cyun-Jyun Fang, Dian Cheng, Tsung-Wei Ke
- Published: 2026-11-03T15:41:07Z
- Age days: 1

</details>
