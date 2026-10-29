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
url: "https://arxiv.org/abs/2610.37378v1"
published: "2026-10-27T15:07:29Z"
age_days: 1
score: 39
created: 2026-10-29
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> VLA-Stem 在冻结的 VLA 后面接一个执行策略：把原动作当路线参考，遇到障碍时允许绕行、减速或等待，再继续任务。它学习保持路线的空间意图，而不是死守每个时刻的原动作。

## 问题

任务是在静态限制或移动障碍下完成抓取、放置、堆叠。给整个 VLA 补避障数据成本高，还可能损伤原能力；仅修正当前危险动作的安全过滤器，则可能避免碰撞却破坏抓取或让机器人偏离后无法继续。[S4](https://arxiv.org/html/2610.37378v1#S1.p2.1) 真正难点是避障后仍知道如何接回任务。

### 用一个例子理解

理解用例（非论文实验）：输入VLA给出的搬杯路线、机械臂状态和横穿路线的障碍信息；Stem先等待或局部绕行，再沿参考方向继续，输出新的执行动作，不要求VLA重新学习搬杯。

## 创新点或方法

旧做法局部修正动作；本文把 VLA 的短动作段转成运动参考，Stem 联合参考、机器人自身状态和局部障碍信息输出控制。轨迹引导保留空间进展，放松严格时间对齐，因此可以等待再前进。训练先学跟随，再加静态和动态障碍；教师额外看到目标物体等任务信息，帮助学偏离后的恢复，学生通过强化学习和模仿教师分布学习。[S14](https://arxiv.org/html/2610.37378v1#S3.F2) [S16](https://arxiv.org/html/2610.37378v1#S3.SS3.p1.1) [S20](https://arxiv.org/html/2610.37378v1#S3.SS4.p2.1) 部署仅用学生，既不需要教师特权信息，也不微调原 VLA。

### 方法如何工作

1. 冻结VLA并把动作段转换为参考轨迹，为安全修正保留任务运动方向。
2. 先训练无障碍跟随，再引入静态和移动障碍，让策略逐步学会空间与时间调整。
3. 教师借额外任务信息学习偏离后的恢复，学生结合强化学习和蒸馏获得可部署行为。
4. 执行时持续结合参考、自身状态和障碍信息出动作，在避险后继续推进任务。

### 必要术语

- 轨迹级引导：比较一段运动与参考的空间关系；允许本文策略改变执行时机。
- 特权信息：训练时可用、部署不假定可用的信息；帮助教师找到恢复方向。
- 蒸馏：让学生学习教师的输出分布；用于移除部署时对额外任务信息的依赖。

## 证据

ManiSkill中测试PickCube、Object Stowing、StackCube，各含正常、静态、动态场景，每个设置3200回合。对比原VLA、避障数据微调、VLSA安全过滤器。[S23](https://arxiv.org/html/2610.37378v1#S4.SS1.p1.1) [S24](https://arxiv.org/html/2610.37378v1#S4.SS1.p2.1) [S25](https://arxiv.org/html/2610.37378v1#S4.SS1.p3.1) [S26](https://arxiv.org/html/2610.37378v1#S4.SS1.p4.1) [S27](https://arxiv.org/html/2610.37378v1#S4.SS1.p5.1) 六个受限设置的平均无碰撞任务成功率为52.8%，最强安全基线23.7%（摘要）。PickCube静态场景中，VLSA-ARM碰撞率22.53%，略低于Stem的23.16%，但成功率仅15.16%，Stem为52.19%。[S22](https://arxiv.org/html/2610.37378v1#S4.T1.2.1) 这说明只看少碰撞会误判任务效果。真机结果在所给材料中只有定性结论。

## 局限

作者明确限定当前评估为结构化操作和低维障碍表示，接触、力安全及带噪视觉感知仍待扩展。[S30](https://arxiv.org/html/2610.37378v1#S5.p1.1) 仿真中Stem和VLSA使用真实障碍信息，因此结果不能直接证明现实感知链路可靠。[S26](https://arxiv.org/html/2610.37378v1#S4.SS1.p4.1) 我的待核查问题是快速障碍下的感知延迟和失败边界；学习型避障也不构成零碰撞保证。

- **判断**：值得读到轨迹奖励和教师训练细节，因为其核心贡献是同时保住避障与任务连续性，而非单独降低碰撞率。

## 研究关联

值得借鉴的是把“要去哪里”和“此刻怎么安全走”分开，并训练偏离后的恢复。执行修正不能只优化当下距离障碍多远，还要考虑是否保留后续任务可完成的状态。

### 下一步读哪里

优先核查轨迹匹配如何容许等待而不鼓励停滞，再读[S16](https://arxiv.org/html/2610.37378v1#S3.SS3.p1.1)教师信息和恢复训练；结合[S29](https://arxiv.org/html/2610.37378v1#S4.SS2.SSS1.p5.1)分析无碰撞失败，最后检查真机障碍获取方式及控制频率。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.37378v1
- 获取时间：2026-10-29T00:42:05.668684+00:00
- [S1] [VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning · 正文段落 1](https://arxiv.org/html/2610.37378v1#abstract1.1)
- [S2] [I Introduction · 正文段落 2](https://arxiv.org/html/2610.37378v1#S1.p1.1)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2610.37378v1#S1.F1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2610.37378v1#S1.p2.1)
- [S5] [I Introduction · 正文段落 5](https://arxiv.org/html/2610.37378v1#S1.p3.1)
- [S6] [I Introduction · 正文段落 6](https://arxiv.org/html/2610.37378v1#S1.p4.1)
- [S7] [I Introduction · 正文段落 7](https://arxiv.org/html/2610.37378v1#S1.I1.i1)
- [S8] [I Introduction · 正文段落 9](https://arxiv.org/html/2610.37378v1#S1.I1.i3)
- [S9] [II-A Vision-Language-Action Models · 正文段落 11](https://arxiv.org/html/2610.37378v1#S2.SS1.p2.1)
- [S10] [II-B Safety for Manipulators · 正文段落 12](https://arxiv.org/html/2610.37378v1#S2.SS2.p1.1)
- [S11] [II-B Safety for Manipulators · 正文段落 13](https://arxiv.org/html/2610.37378v1#S2.SS2.p2.1)
- [S12] [II-C Test-Time VLA · 正文段落 14](https://arxiv.org/html/2610.37378v1#S2.SS3.p1.1)
- [S13] [III Method · 正文段落 15](https://arxiv.org/html/2610.37378v1#S3.p1.1)
- [S14] [III Method · 正文段落 16](https://arxiv.org/html/2610.37378v1#S3.F2)
- [S15] [III-A VLA-Conditioned Execution · 正文段落 17](https://arxiv.org/html/2610.37378v1#S3.SS1.p1.1)
- [S16] [III-C Teacher–Student Distillation · 正文段落 41](https://arxiv.org/html/2610.37378v1#S3.SS3.p1.1)
- [S17] [III-C Teacher–Student Distillation · 正文段落 43](https://arxiv.org/html/2610.37378v1#S3.SS3.p1.2)
- [S18] [III-D RL Optimization and Curriculum Learning · 正文段落 44](https://arxiv.org/html/2610.37378v1#S3.SS4.p1.1)
- [S19] [III-D RL Optimization and Curriculum Learning · 正文段落 46](https://arxiv.org/html/2610.37378v1#S3.SS4.p1.2)
- [S20] [III-D RL Optimization and Curriculum Learning · 正文段落 47](https://arxiv.org/html/2610.37378v1#S3.SS4.p2.1)
- [S21] [IV Experiment · 正文段落 48](https://arxiv.org/html/2610.37378v1#S4.T1)
- [S22] [IV Experiment · 正文段落 49](https://arxiv.org/html/2610.37378v1#S4.T1.2.1)
- [S23] [IV-A Experimental Setup · 正文段落 50](https://arxiv.org/html/2610.37378v1#S4.SS1.p1.1)
- [S24] [IV-A Experimental Setup · 正文段落 51](https://arxiv.org/html/2610.37378v1#S4.SS1.p2.1)
- [S25] [IV-A Experimental Setup · 正文段落 52](https://arxiv.org/html/2610.37378v1#S4.SS1.p3.1)
- [S26] [IV-A Experimental Setup · 正文段落 53](https://arxiv.org/html/2610.37378v1#S4.SS1.p4.1)
- [S27] [IV-A Experimental Setup · 正文段落 54](https://arxiv.org/html/2610.37378v1#S4.SS1.p5.1)
- [S28] [IV-A Experimental Setup · 正文段落 55](https://arxiv.org/html/2610.37378v1#S4.SS1.p6.1)
- [S29] [IV-B1 Main Results · 正文段落 61](https://arxiv.org/html/2610.37378v1#S4.SS2.SSS1.p5.1)
- [S30] [V Conclusion · 正文段落 86](https://arxiv.org/html/2610.37378v1#S5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/VLA-Stem A Lightweight Safety Mechanism for Vision-Language-Action Models via Re.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control. However, most VLA models target static manipulation in unconstrained environments, overlooking spatial constraints and dynamic obstacles. Fine-tuning VLAs on obstacle-avoidance data is a straightforward solution, but collecting such data is costly, especially for dynamic scenarios, and may degrade their original task capabilities. To address these limitations, we propose VLA-Stem, a lightweight, reinforcement-learning-based safety mechanism for VLA systems. Without fine-tuning the underlying VLA policy, VLA-Stem converts its action chunks into motion references and uses trajectory-level guidance to preserve their spatial intent while allowing flexible motion and timing adjustments. Conditioned on these references, robot proprioception, and local obstacle information, the Stem policy adaptively modifies execution at inference time, preserving the original task intent while enabling responsive adaptation to spatial constraints and dynamic obstacles. For robust and sample-efficient training, we combine teacher-student distillation with curriculum learning. We evaluate VLA-Stem on reference following, static spatial constraints, and dynamic obstacle avoidance. Across six constrained simulation settings, VLA-Stem achieves 52.8% average collision-free task success versus 23.7% for the strongest safety baseline, while preserving base-policy performance in obstacle-free settings; real-world experiments further show consistent collision reductions under static and dynamic obstacles. These results demonstrate that VLA-Stem couples high-level VLA task intent with rapid, reflex-like responses to immediate physical risks, providing a brainstem-inspired mechanism for robust robot execution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37378v1
- Authors: Bojun Zou, Wenhao Yu, Jiaohao Li, Jiaxuan Lin, Guanting Ye, Haohan Geng, Weihao Yu, Yanyong Zhang, Jianmin Ji
- Published: 2026-10-27T15:07:29Z
- Age days: 1

</details>
