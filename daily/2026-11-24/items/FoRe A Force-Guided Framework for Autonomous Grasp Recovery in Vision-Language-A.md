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
url: "https://arxiv.org/abs/2611.27011v1"
published: "2026-11-20T02:39:15Z"
age_days: 3
score: 36
created: 2026-11-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> FoRe 给取放机器人加了一道物理确认：抓取命令开着时，结合力信号判断物体是否抓住或滑脱。发现失手后，它切到专门练过的重抓策略，恢复抓取后再继续搬运。

## 问题

模仿成功取放的 VLA 有时抓空也继续搬运，因为此时的关节位置或手臂姿态可能已经很像成功示范中的搬运阶段。作者把这种依赖自身状态的解释作为一种可能原因。成功演示也很少教机器人怎样从抓空的位置重新接近。部署时靠人工或视觉模型纠正会增加干预或推理开销，扩增演示则要补纠正轨迹。[S3](https://arxiv.org/html/2611.27011v1#S1.p2.1)[S5](https://arxiv.org/html/2611.27011v1#S1.p3.1)[S13](https://arxiv.org/html/2611.27011v1#S2.SS2.p1.1)

### 用一个例子理解

理解用例（非论文实验）——吸盘要把塑料盒从桌面搬进筐。盒子刚离桌就脱落，抓取命令仍开着，但载荷降了下来。控制器切到重抓策略，机械臂重新对准桌上的盒子，恢复接触后再切回搬放。

## 创新点或方法

旧策略从整条成功演示学一套动作。FoRe 先用加速度减轻力读数中的惯性影响，再用力阈值和抓取命令给演示分段，分别微调抓取与搬放策略。重抓策略从抓取策略初始化，在失败附近通过强化学习练习。部署时，控制器结合力和命令识别主动释放与意外失去接触，决定该继续搬还是重抓。真机版的重抓策略在机器人上训练。[S20](https://arxiv.org/html/2611.27011v1#S3.SS2.p1.1) [S21](https://arxiv.org/html/2611.27011v1#S3.SS2.p2.1) [S22](https://arxiv.org/html/2611.27011v1#S3.SS3.p1.1) [S23](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.1) [S24](https://arxiv.org/html/2611.27011v1#S3.E2) [S25](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.2) [S26](https://arxiv.org/html/2611.27011v1#S3.E3) [S27](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.3) [S28](https://arxiv.org/html/2611.27011v1#S3.SS4.p1.1) [S29](https://arxiv.org/html/2611.27011v1#S3.SS4.p2.1)[S40](https://arxiv.org/html/2611.27011v1#S3.SS5.p1.1)[S58](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px3.p1.1)

### 方法如何工作

1. 用力读数和抓取命令标出成功演示的阶段边界，分别训练抓取与搬放。
2. 在仿真中让机械臂处在刚开始搬运的位置，却把物体留在原处，构造需要回头抓的起点。
3. 让同一起点尝试多种重抓，按提起后能否保持载荷给分，使重抓策略偏向成功动作。
4. 实际运行时监测命令和力的组合，仍要求抓取却失去接触就重抓，恢复后继续搬放。

### 必要术语

- 抓取命令状态：夹具当前是否被要求抓住物体；配合力信号区分主动松开和意外脱落。
- 提起测试：提起时检查载荷是否保持；用来给重抓训练判定成败。
- 局部强化学习：从失手附近开始练恢复动作；在 FoRe 中只优化重抓策略。

## 证据

LIBERO-SUCTION 仿真中，VLA-Adapter 的平均任务成功率从 69.2% 升到 87.6%，π₀.₅ 从 85.9% 升到 92.4%。在 LIBERO，两种骨干接入 FoRe 后分别比接入 CycleVLA 高 1.0 和 0.4 个百分点。真机使用 DOBOT 机械臂和真空夹具，每任务 40 次，平均成功率分别从 26.7% 升到 51.7%、从 48.3% 升到 70.0%。摘要也报告两套仿真每任务仅一条示范时仍有收益，所给节选未列具体幅度。[S1](https://arxiv.org/html/2611.27011v1#abstract1.1)[S47](https://arxiv.org/html/2611.27011v1#S4.T1.5) [S48](https://arxiv.org/html/2611.27011v1#S4.T2) [S49](https://arxiv.org/html/2611.27011v1#S4.T2.5) [S50](https://arxiv.org/html/2611.27011v1#S4.SS1.SSS0.Px4.p1.1)[S53](https://arxiv.org/html/2611.27011v1#S4.SS1.SSS0.Px6.p1.1)[S56](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px1.p1.1) [S57](https://arxiv.org/html/2611.27011v1#S4.F5) [S58](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px3.p1.1) [S59](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px4.p1.1)

## 局限

作者明确指出，如果初始策略一直碰不到目标，控制器可能连触发重抓所需的状态都进不去。[S62](https://arxiv.org/html/2611.27011v1#S6.p2.1) 我会核查轻物体、碰到桌面和快速运动时的误判率。两种骨干的整体收益也不足以单独证明原策略确实过度依赖自身姿态。

- **判断**：值得细读阶段标注、重抓起点和策略切换，这三个细节决定拿到自己的力信号后能否照搬。

## 研究关联

能直接测到动作结果时，可以用这个信号决定下一步，再把学习资源集中在最常见的恢复起点。尤其适合示范大多成功、失手后机器人却反复落入相似错误姿态的任务。

### 下一步读哪里

对照 [S23](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.1) [S24](https://arxiv.org/html/2611.27011v1#S3.E2) [S25](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.2) [S26](https://arxiv.org/html/2611.27011v1#S3.E3) [S27](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.3) 的分段条件与 [S33](https://arxiv.org/html/2611.27011v1#S3.SS4.p4.1) [S34](https://arxiv.org/html/2611.27011v1#S3.SS4.p5.1) [S35](https://arxiv.org/html/2611.27011v1#S3.E5) [S36](https://arxiv.org/html/2611.27011v1#S3.SS4.p5.2) 的提起测试，注意训练奖励要求提起时保持载荷。再看 [S12](https://arxiv.org/html/2611.27011v1#S2.F2)[S51](https://arxiv.org/html/2611.27011v1#S4.F3) 的部署切换，核查力阈值标定和第一次完全抓空时的处理。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.27011v1
- 获取时间：2026-11-24T01:58:56.017214+00:00
- [S1] [FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models · 正文段落 1](https://arxiv.org/html/2611.27011v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.27011v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.27011v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.27011v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.27011v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.27011v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.27011v1#S1.I1.i1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.27011v1#S1.I1.i2)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.27011v1#S1.I1.i3)
- [S10] [2.1 Vision-Language-Action Models · 正文段落 10](https://arxiv.org/html/2611.27011v1#S2.SS1.p1.1)
- [S11] [2.1 Vision-Language-Action Models · 正文段落 11](https://arxiv.org/html/2611.27011v1#S2.SS1.p2.1)
- [S12] [2.1 Vision-Language-Action Models · 正文段落 12](https://arxiv.org/html/2611.27011v1#S2.F2)
- [S13] [2.2 Failure Recovery in Robotic Manipulation · 正文段落 13](https://arxiv.org/html/2611.27011v1#S2.SS2.p1.1)
- [S14] [2.2 Failure Recovery in Robotic Manipulation · 正文段落 14](https://arxiv.org/html/2611.27011v1#S2.SS2.p2.1)
- [S15] [2.3 Reinforcement Learning for VLA Models · 正文段落 15](https://arxiv.org/html/2611.27011v1#S2.SS3.p1.1)
- [S16] [2.3 Reinforcement Learning for VLA Models · 正文段落 16](https://arxiv.org/html/2611.27011v1#S2.SS3.p2.1)
- [S17] [3.1 Problem Formulation · 正文段落 17](https://arxiv.org/html/2611.27011v1#S3.SS1.p1.1)
- [S18] [3.1 Problem Formulation · 正文段落 18](https://arxiv.org/html/2611.27011v1#S3.SS1.p2.1)
- [S19] [3.1 Problem Formulation · 正文段落 20](https://arxiv.org/html/2611.27011v1#S3.SS1.p2.2)
- [S20] [3.2 Framework Overview · 正文段落 21](https://arxiv.org/html/2611.27011v1#S3.SS2.p1.1)
- [S21] [3.2 Framework Overview · 正文段落 22](https://arxiv.org/html/2611.27011v1#S3.SS2.p2.1)
- [S22] [3.3 Dataset Stage Annotation · 正文段落 24](https://arxiv.org/html/2611.27011v1#S3.SS3.p1.1)
- [S23] [3.3 Dataset Stage Annotation · 正文段落 25](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.1)
- [S24] [3.3 Dataset Stage Annotation · 正文段落 26](https://arxiv.org/html/2611.27011v1#S3.E2)
- [S25] [3.3 Dataset Stage Annotation · 正文段落 27](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.2)
- [S26] [3.3 Dataset Stage Annotation · 正文段落 28](https://arxiv.org/html/2611.27011v1#S3.E3)
- [S27] [3.3 Dataset Stage Annotation · 正文段落 29](https://arxiv.org/html/2611.27011v1#S3.SS3.p2.3)
- [S28] [3.4 RL-Based Retry Policy Optimization · 正文段落 30](https://arxiv.org/html/2611.27011v1#S3.SS4.p1.1)
- [S29] [3.4 RL-Based Retry Policy Optimization · 正文段落 31](https://arxiv.org/html/2611.27011v1#S3.SS4.p2.1)
- [S30] [3.4 RL-Based Retry Policy Optimization · 正文段落 32](https://arxiv.org/html/2611.27011v1#S3.SS4.p3.1)
- [S31] [3.4 RL-Based Retry Policy Optimization · 正文段落 33](https://arxiv.org/html/2611.27011v1#S3.E4)
- [S32] [3.4 RL-Based Retry Policy Optimization · 正文段落 34](https://arxiv.org/html/2611.27011v1#S3.SS4.p3.2)
- [S33] [3.4 RL-Based Retry Policy Optimization · 正文段落 35](https://arxiv.org/html/2611.27011v1#S3.SS4.p4.1)
- [S34] [3.4 RL-Based Retry Policy Optimization · 正文段落 36](https://arxiv.org/html/2611.27011v1#S3.SS4.p5.1)
- [S35] [3.4 RL-Based Retry Policy Optimization · 正文段落 37](https://arxiv.org/html/2611.27011v1#S3.E5)
- [S36] [3.4 RL-Based Retry Policy Optimization · 正文段落 38](https://arxiv.org/html/2611.27011v1#S3.SS4.p5.2)
- [S37] [3.4 RL-Based Retry Policy Optimization · 正文段落 39](https://arxiv.org/html/2611.27011v1#S3.SS4.p6.1)
- [S38] [3.4 RL-Based Retry Policy Optimization · 正文段落 40](https://arxiv.org/html/2611.27011v1#S3.E6)
- [S39] [3.4 RL-Based Retry Policy Optimization · 正文段落 41](https://arxiv.org/html/2611.27011v1#S3.SS4.p6.2)
- [S40] [3.5 Force-Guided Policy Switching · 正文段落 42](https://arxiv.org/html/2611.27011v1#S3.SS5.p1.1)
- [S41] [Unified policy switching · 正文段落 47](https://arxiv.org/html/2611.27011v1#S3.SS5.SSS0.Px3.p1.1)
- [S42] [4 Experiments · 正文段落 50](https://arxiv.org/html/2611.27011v1#S4.p1.1)
- [S43] [4 Experiments · 正文段落 51](https://arxiv.org/html/2611.27011v1#S4.I1.i1)
- [S44] [4 Experiments · 正文段落 52](https://arxiv.org/html/2611.27011v1#S4.I1.i2)
- [S45] [4 Experiments · 正文段落 53](https://arxiv.org/html/2611.27011v1#S4.p3.1)
- [S46] [4 Experiments · 正文段落 54](https://arxiv.org/html/2611.27011v1#S4.T1)
- [S47] [4 Experiments · 正文段落 55](https://arxiv.org/html/2611.27011v1#S4.T1.5)
- [S48] [4 Experiments · 正文段落 56](https://arxiv.org/html/2611.27011v1#S4.T2)
- [S49] [4 Experiments · 正文段落 57](https://arxiv.org/html/2611.27011v1#S4.T2.5)
- [S50] [Evaluation protocol · 正文段落 61](https://arxiv.org/html/2611.27011v1#S4.SS1.SSS0.Px4.p1.1)
- [S51] [Evaluation protocol · 正文段落 62](https://arxiv.org/html/2611.27011v1#S4.F3)
- [S52] [Results on LIBERO-SUCTION · 正文段落 63](https://arxiv.org/html/2611.27011v1#S4.SS1.SSS0.Px5.p1.1)
- [S53] [Results on LIBERO · 正文段落 65](https://arxiv.org/html/2611.27011v1#S4.SS1.SSS0.Px6.p1.1)
- [S54] [Results on LIBERO · 正文段落 66](https://arxiv.org/html/2611.27011v1#S4.T3)
- [S55] [Results on LIBERO · 正文段落 68](https://arxiv.org/html/2611.27011v1#S4.T4)
- [S56] [Experimental setup · 正文段落 70](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px1.p1.1)
- [S57] [Experimental setup · 正文段落 71](https://arxiv.org/html/2611.27011v1#S4.F5)
- [S58] [Baselines and evaluation · 正文段落 73](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px3.p1.1)
- [S59] [Results · 正文段落 74](https://arxiv.org/html/2611.27011v1#S4.SS2.SSS0.Px4.p1.1)
- [S60] [Results · 正文段落 75](https://arxiv.org/html/2611.27011v1#S4.F6)
- [S61] [Results · 正文段落 76](https://arxiv.org/html/2611.27011v1#S4.F7)
- [S62] [6 Conclusion and Limitation · 正文段落 87](https://arxiv.org/html/2611.27011v1#S6.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/FoRe A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-A.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have demonstrated strong performance in grasp-based manipulation, yet reliable recovery from local grasping failures remains challenging. Specifically, in pick-and-place tasks, policies may continue transport after a failed grasp instead of retrying, potentially reflecting overreliance on proprioceptive cues for stage progression and limited retry supervision. Existing recovery approaches typically rely on deployment-time guidance or demonstration augmentation. We introduce Force-guided Recovery (FoRe), a framework for autonomous recovery from local grasping failures. Using force feedback, FoRe partitions demonstrations into approach-grasp and transport-placement stages to train separate policies. To supplement limited retry supervision, FoRe then initializes a dedicated retry policy from the approach-grasp policy and refines it through local reinforcement learning (RL) from post-failure states. To avoid inappropriate stage progression, a controller combines force feedback with grasp-command status at inference to coordinate the stage policies, detect grasp failures, and invoke the retry policy. We also construct LIBERO-SUCTION, a force-augmented suction manipulation benchmark adapted from LIBERO, with complete demonstration trajectories for policy training. FoRe consistently improves task success rates for VLA-Adapter and $π_{0.5}$ on LIBERO-SUCTION, LIBERO, and real-world tasks. On LIBERO-SUCTION, average absolute gains are 18.4% and 6.5%, respectively. The corresponding real-world absolute gains are 25.0% and 21.7%. FoRe also remains effective with only one demonstration per task on both simulation benchmarks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27011v1
- Authors: Shuai Peng, Yongkai Liao, Yuxin Cheng, Haoyuan Wang, Jian Huang
- Published: 2026-11-20T02:39:15Z
- Age days: 3

</details>
