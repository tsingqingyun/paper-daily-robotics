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
url: "https://arxiv.org/abs/2610.09940v1"
published: "2026-10-07T12:24:17Z"
age_days: 0
score: 37
created: 2026-10-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Juno: Taming Predictive Latents for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Juno 让“预测下一步会看到什么”真正服务于动作生成：先学机器人相关变化，再让独立预测分支同时接受未来状态和动作训练。部署失配时先修世界模型，再用经过验证的执行调整策略。

## 问题

互联网视频表示可能忽略机器人能控制的局部变化；预测训练挤进共享通路会干扰动作学习；环境改变后，冻结教师本身也可能预测错。失败动作不能直接拿来模仿，却仍记录了真实后果。[S5](https://arxiv.org/html/2610.09940v1#S1.p2.1) [S8](https://arxiv.org/html/2610.09940v1#S1.p5.1)

### 用一个例子理解

理解用例（非论文实验）：输入新高度桌面上的积木图像和“放入碗中”；当前特征与预测分支共同生成动作。若执行失败，观察到的变化先用于修动力学；验证有效的执行才用于策略再训练。

## 创新点或方法

预训练用匹配机器人轨迹的动作条件 JEPA，再让全局状态变化学习运动加权的局部变化。策略训练融合当前图像特征，独立变换参数的预测分支学习未来状态，同时为动作解码提供输入。未来图像只在训练中作目标，推理只看当前观察和指令。部署更新先用全部转移修世界模型，冻结后再用验证执行更新 LoRA 和动作头。[S6](https://arxiv.org/html/2610.09940v1#S1.p3.1) [S7](https://arxiv.org/html/2610.09940v1#S1.p4.1) [S8](https://arxiv.org/html/2610.09940v1#S1.p5.1)

### 方法如何工作

1. 在匹配机器人轨迹上训练动作条件预测，得到贴近实际控制的表示。
2. 用运动加权局部变化监督全局状态，防止关键接触被背景稀释。
3. 融合当前特征，并让独立分支学习未来状态和动作生成，使预测信息可供控制使用。
4. 部署后用所有真实转移修正世界模型，再冻结教师，用验证执行保守调整策略。

### 必要术语

- JEPA：预测表示而非完整像素；提供未来状态教师。
- CLS状态：概括整幅图像的紧凑向量；本文让它保留控制相关变化。
- 未来状态蒸馏：用未来观察的编码训练当前预测；未来图像不作为推理输入。
- 测试时训练：用部署经验更新参数；这里分世界模型和策略两阶段。

## 证据

SimplerEnv 四个 WidowX 任务，每任务96次评估：Qwen3GR00T 60.9%，Juno 68.5%，额外部署训练后72.7%；胡萝卜任务未更新时60.4%→59.4%，并非全部改善。[S25](https://arxiv.org/html/2610.09940v1#S4.T1.6.1) [S40](https://arxiv.org/html/2610.09940v1#A3.SS1.p1.1) RoboCasa-GR1 24任务各50次，基线47.8%→59.6%。[S23](https://arxiv.org/html/2610.09940v1#S4.SS1.SSS0.Px3.p1.1) [S28](https://arxiv.org/html/2610.09940v1#S4.T2.4) 真机红方块入碗任务的背景、叠加高度与物体变化下，冻结 Juno 为75%、70%、70%，基线均0%，各20次；这些不是 TTT 结果。[S30](https://arxiv.org/html/2610.09940v1#S4.F4) [S31](https://arxiv.org/html/2610.09940v1#S4.T4.fig1) [S32](https://arxiv.org/html/2610.09940v1#S4.T4.fig1.1.1) [S39](https://arxiv.org/html/2610.09940v1#A2.SS1.SSS0.Px3.p1.1)

## 局限

作者明确表示，表示分析没有独立隔离数据、架构与目标的贡献。[S34](https://arxiv.org/html/2610.09940v1#A1.p1.1) 因而不能据此断言小模型普遍胜过大模型。我的待核查问题是验证执行的筛选机制、TTT交互预算和消融；真机抗变化证据集中于一个基础任务。

- **判断**：值得读到训练梯度分工与适应流程，因为它解释了为什么“预测得像”还不足以“动作做对”。

## 研究关联

关键启示是给失败数据分配合适用途：抓空的动作不值得模仿，但“这个动作实际造成什么变化”仍可训练动力学。预测教师也应先校准，再指导策略。

### 下一步读哪里

结合[S17](https://arxiv.org/html/2610.09940v1#S3.SS2.p2.1) [S18](https://arxiv.org/html/2610.09940v1#S3.SS2.SSS1.p2.3) [S19](https://arxiv.org/html/2610.09940v1#S3.SS3.SSS2.p2.1)检查全局变化目标与未来状态对齐，核查独立分支的注意力和梯度路径；再查未提供的TTT筛选与预算，分开比较冻结策略和适应后的成绩。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.09940v1
- 获取时间：2026-10-08T01:54:41.684943+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.09940v1#p1.3)
- [S2] [Juno : Taming Predictive Latents for Vision-Language-Action Models · 正文段落 2](https://arxiv.org/html/2610.09940v1#abstract1.1)
- [S3] [Juno : Taming Predictive Latents for Vision-Language-Action Models · 正文段落 3](https://arxiv.org/html/2610.09940v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.09940v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.09940v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.09940v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.09940v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.09940v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.09940v1#S1.I1.i1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.09940v1#S1.I1.i3)
- [S11] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.09940v1#S2.p2.1)
- [S12] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.09940v1#S2.p3.1)
- [S13] [3 Method · 正文段落 16](https://arxiv.org/html/2610.09940v1#S3.F2)
- [S14] [3.1 Preliminaries · 正文段落 17](https://arxiv.org/html/2610.09940v1#S3.SS1.p1.1)
- [S15] [3.1 Preliminaries · 正文段落 21](https://arxiv.org/html/2610.09940v1#S3.F3)
- [S16] [3.2 Control-Aligned Pretraining · 正文段落 22](https://arxiv.org/html/2610.09940v1#S3.SS2.p1.1)
- [S17] [3.2 Control-Aligned Pretraining · 正文段落 23](https://arxiv.org/html/2610.09940v1#S3.SS2.p2.1)
- [S18] [3.2.1 Dynamic CLS Loss · 正文段落 29](https://arxiv.org/html/2610.09940v1#S3.SS2.SSS1.p2.3)
- [S19] [3.3.2 Future Latent-State Distillation and Action Generation · 正文段落 36](https://arxiv.org/html/2610.09940v1#S3.SS3.SSS2.p2.1)
- [S20] [4 Experiments · 正文段落 50](https://arxiv.org/html/2610.09940v1#S4.p1.1)
- [S21] [4.1 Experimental Setup · 正文段落 51](https://arxiv.org/html/2610.09940v1#S4.SS1.SSS0.Px1.p1.1)
- [S22] [4.1 Experimental Setup · 正文段落 52](https://arxiv.org/html/2610.09940v1#S4.SS1.SSS0.Px2.p1.1)
- [S23] [4.1 Experimental Setup · 正文段落 53](https://arxiv.org/html/2610.09940v1#S4.SS1.SSS0.Px3.p1.1)
- [S24] [4.2 Simulation Benchmark Results · 正文段落 54](https://arxiv.org/html/2610.09940v1#S4.T1)
- [S25] [4.2 Simulation Benchmark Results · 正文段落 55](https://arxiv.org/html/2610.09940v1#S4.T1.6.1)
- [S26] [4.2 Simulation Benchmark Results · 正文段落 56](https://arxiv.org/html/2610.09940v1#S4.SS2.SSS0.Px1.p1.1)
- [S27] [4.2 Simulation Benchmark Results · 正文段落 57](https://arxiv.org/html/2610.09940v1#S4.T2)
- [S28] [4.2 Simulation Benchmark Results · 正文段落 58](https://arxiv.org/html/2610.09940v1#S4.T2.4)
- [S29] [4.2 Simulation Benchmark Results · 正文段落 59](https://arxiv.org/html/2610.09940v1#S4.SS2.SSS0.Px2.p1.1)
- [S30] [4.3 Real-World Robot Evaluation · 正文段落 60](https://arxiv.org/html/2610.09940v1#S4.F4)
- [S31] [4.3 Real-World Robot Evaluation · 正文段落 61](https://arxiv.org/html/2610.09940v1#S4.T4.fig1)
- [S32] [4.3 Real-World Robot Evaluation · 正文段落 62](https://arxiv.org/html/2610.09940v1#S4.T4.fig1.1.1)
- [S33] [5 Conclusion · 正文段落 75](https://arxiv.org/html/2610.09940v1#S5.p1.1)
- [S34] [Appendix A Additional Representation Analysis · 正文段落 76](https://arxiv.org/html/2610.09940v1#A1.p1.1)
- [S35] [B.1 Training Data · 正文段落 83](https://arxiv.org/html/2610.09940v1#A2.SS1.SSS0.Px1.p1.1)
- [S36] [B.1 Training Data · 正文段落 84](https://arxiv.org/html/2610.09940v1#A2.T6)
- [S37] [B.1 Training Data · 正文段落 85](https://arxiv.org/html/2610.09940v1#A2.T6.4)
- [S38] [B.1 Training Data · 正文段落 86](https://arxiv.org/html/2610.09940v1#A2.SS1.SSS0.Px2.p1.1)
- [S39] [B.1 Training Data · 正文段落 87](https://arxiv.org/html/2610.09940v1#A2.SS1.SSS0.Px3.p1.1)
- [S40] [C.1 SimplerEnv · 正文段落 95](https://arxiv.org/html/2610.09940v1#A3.SS1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/Juno Taming Predictive Latents for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts. We introduce Juno, a unified framework built around one action-conditioned JEPA that serves as a control-aligned representation backbone, a predictive teacher, and an adaptable dynamics model. During pretraining, we train it on embodiment-matched trajectories and use a dynamic CLS loss to transfer motion-weighted patch dynamics to a compact global state. During policy learning, we fuse current-frame JEPA patches into VLA perception and use a decoupled reasoning branch with separate transformation parameters to distill future latent states for action generation. During deployment, we adapt the world model on all observed transitions, including failed rollouts, freeze the adapted teacher, and re-align the policy on verified executions using LoRA adapters and a trainable action head, without expert corrections or task rewards. On SimplerEnv, Juno raises average success from $60.9\%$ to $68.5\%$ over Qwen3GR00T, the strongest baseline, and test-time adaptation further reaches $72.7\%$; on a real robot, it retains $70\%$--$75\%$ success under background, height, and object shifts where the base policy collapses to $0\%$.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09940v1
- Authors: Yuchen Zhu, Chenyi Xu, Yulin Zhang, Gang Xu, Wentao Zhu
- Published: 2026-10-07T12:24:17Z
- Age days: 0

</details>
