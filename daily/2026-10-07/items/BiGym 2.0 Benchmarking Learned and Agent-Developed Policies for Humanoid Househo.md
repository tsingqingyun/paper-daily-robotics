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
url: "https://arxiv.org/abs/2610.07594v1"
published: "2026-10-06T01:33:35Z"
age_days: 1
score: 39
created: 2026-10-07
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> BiGym 2.0 测的是人形机器人边走、边保持姿态、边做家务，而不是把身体当成平稳移动底座。它让学习策略和智能体编写的程序共用身体控制器，比较两条路线在哪些任务上可靠。

## 问题

端盘子或够洗碗机时，步态会让躯干晃动，接触也会影响平衡。旧 BiGym 发布的示范主要使用可直接移动的底座模式，隔开了行走与操作；因此不能直接回答策略如何应对腿式执行的迟滞和扰动 [S6](https://arxiv.org/html/2610.07594v1#S1.p1.1) [S7](https://arxiv.org/html/2610.07594v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入双腕画面、关节状态和“两手分别碰到目标”；程序分别计算左右目标的像素偏差，输出肩关节调整和身体参考；身体控制器保持支撑，下一帧继续纠偏。

## 创新点或方法

本文改用 G1，把身体速度、高度等参考交给冻结的 GR00T-WBC 实现，并让 VR 示范、评测和重置共用它 [S5](https://arxiv.org/html/2610.07594v1#S0.F2)。学习路线从示范微调 π₀.₅、训练模仿策略或结合强化学习；程序路线让编码智能体在有限交互中开发 Python 策略。部署时程序冻结，不调用语言模型 [S24](https://arxiv.org/html/2610.07594v1#S3.SS5.p4.1)。共同接口使差异更容易解释，但动作表示和训练资源并非全部相同，例如 π₀.₅ 用相对手臂动作 [S33](https://arxiv.org/html/2610.07594v1#A2.SS2.p2.1)。

### 方法如何工作

1. 把家务任务适配到 G1，并引入真实步态式身体执行，让操作面对身体扰动。
2. 通过同一控制器采集 VR 示范，记录相机和全身动作，减少示范与评测的执行差异。
3. 分别训练学习策略或让智能体开发程序，最终都输出共同接口下的命令。
4. 恢复控制器内部状态后在隐藏种子上闭环执行，使成绩反映策略差异而非残留控制状态。
5. 按任务分析成功与失败，识别双手纠偏、持续接触和跨工作区搬运的不同难点。

### 必要术语

- 全身控制器：把身体参考变成腿和腰的动作；本文固定它来比较上层策略。
- 本体感知：机器人自身关节和身体状态；与相机共同构成输入。
- 冷启动程序开发：每项任务重新开发程序，不沿用其他任务技能；衡量找到可用策略的可靠性。

## 证据

套件有 20 项任务，每项 60 段 VR 示范；主比较选九项（摘要）。π₀.₅ 九任务均值最高，两个编码智能体均值超过各示范驱动 RL，双手同时到达目标时也领先学习策略 [S26](https://arxiv.org/html/2610.07594v1#S4.SS1.p1.1) [S28](https://arxiv.org/html/2610.07594v1#S5.SS2.p1.1) [S31](https://arxiv.org/html/2610.07594v1#S7.p1.1)。但材料没有主结果表的具体成功率。非 VLA 学习方法用三次训练，π₀.₅ 每任务仅一次；程序用三个开发会话，隐藏种子评测 [S20](https://arxiv.org/html/2610.07594v1#S3.SS4.p2.1) [S24](https://arxiv.org/html/2610.07594v1#S3.SS5.p4.1)。这些结果支持任务间能力分化，不能外推到全部任务或真机。

## 局限

作者明确说明全部评测在仿真中、依赖一个冻结身体控制器，智能体也可能受益于预训练中已有的 G1 知识 [S30](https://arxiv.org/html/2610.07594v1#S6.p2.1)。相同交互次数不代表相同总计算或先验；VLA 的单次训练也使其排名稳定性需要核查。固定初始状态任务与随机物体位置任务应分别看。

- **判断**：值得读控制接口、重置协议和逐任务失败分析；九任务均值可以定位方向，但不足以宣判学习或写程序哪条路线更强。

## 研究关联

程序能把两只手各自的目标和纠偏明确拆开，双手到达结果提示这种结构值得借鉴 [S26](https://arxiv.org/html/2610.07594v1#S4.SS1.p1.1)。但接触搬运仍困难，说明可分解的视觉纠偏与持续接触不是同一类能力。

### 下一步读哪里

先读 [S32](https://arxiv.org/html/2610.07594v1#A2.SS2.p1.1) [S33](https://arxiv.org/html/2610.07594v1#A2.SS2.p2.1) 看策略真正控制什么，再看 [S24](https://arxiv.org/html/2610.07594v1#S3.SS5.p4.1) [S28](https://arxiv.org/html/2610.07594v1#S5.SS2.p1.1) 区分程序开发与运行。核查主结果表的任务权重、失败类型和各会话差异；[S40](https://arxiv.org/html/2610.07594v1#A5.p1.1) [S41](https://arxiv.org/html/2610.07594v1#A5.p2.1) 解释为什么应看预先固定的末期成绩，而非最佳检查点。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.07594v1
- 获取时间：2026-10-07T02:13:51.958729+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.07594v1#p1.3)
- [S2] [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation · 正文段落 2](https://arxiv.org/html/2610.07594v1#abstract1.1)
- [S3] [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation · 正文段落 3](https://arxiv.org/html/2610.07594v1#S0.F2.3.1)
- [S4] [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation · 正文段落 4](https://arxiv.org/html/2610.07594v1#S0.F2.4.1)
- [S5] [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation · 正文段落 5](https://arxiv.org/html/2610.07594v1#S0.F2)
- [S6] [I Introduction · 正文段落 6](https://arxiv.org/html/2610.07594v1#S1.p1.1)
- [S7] [I Introduction · 正文段落 7](https://arxiv.org/html/2610.07594v1#S1.p2.1)
- [S8] [I Introduction · 正文段落 8](https://arxiv.org/html/2610.07594v1#S1.p3.1)
- [S9] [I Introduction · 正文段落 9](https://arxiv.org/html/2610.07594v1#S1.p4.1)
- [S10] [II Related Work · 正文段落 10](https://arxiv.org/html/2610.07594v1#S2.p1.1)
- [S11] [II Related Work · 正文段落 11](https://arxiv.org/html/2610.07594v1#S2.p2.1)
- [S12] [II Related Work · 正文段落 12](https://arxiv.org/html/2610.07594v1#S2.p3.1)
- [S13] [II Related Work · 正文段落 13](https://arxiv.org/html/2610.07594v1#S2.T1)
- [S14] [II Related Work · 正文段落 14](https://arxiv.org/html/2610.07594v1#S2.T1.7)
- [S15] [II Related Work · 正文段落 15](https://arxiv.org/html/2610.07594v1#S2.T1.8)
- [S16] [II Related Work · 正文段落 16](https://arxiv.org/html/2610.07594v1#S2.p4.1)
- [S17] [II Related Work · 正文段落 17](https://arxiv.org/html/2610.07594v1#S2.p5.1)
- [S18] [III-A Loco-manipulation challenges and tasks · 正文段落 21](https://arxiv.org/html/2610.07594v1#S3.SS1.p4.1)
- [S19] [III-A Loco-manipulation challenges and tasks · 正文段落 22](https://arxiv.org/html/2610.07594v1#S3.SS1.p5.1)
- [S20] [III-D Observations and evaluation · 正文段落 34](https://arxiv.org/html/2610.07594v1#S3.SS4.p2.1)
- [S21] [III-E Policy families · 正文段落 35](https://arxiv.org/html/2610.07594v1#S3.SS5.p1.1)
- [S22] [III-E Policy families · 正文段落 36](https://arxiv.org/html/2610.07594v1#S3.SS5.p2.1)
- [S23] [III-E Policy families · 正文段落 37](https://arxiv.org/html/2610.07594v1#S3.SS5.p3.1)
- [S24] [III-E Policy families · 正文段落 38](https://arxiv.org/html/2610.07594v1#S3.SS5.p4.1)
- [S25] [III-E Policy families · 正文段落 39](https://arxiv.org/html/2610.07594v1#S3.F5)
- [S26] [IV-A Dual reaching and transport separate the methods · 正文段落 43](https://arxiv.org/html/2610.07594v1#S4.SS1.p1.1)
- [S27] [IV-A Dual reaching and transport separate the methods · 正文段落 44](https://arxiv.org/html/2610.07594v1#S4.SS1.p2.1)
- [S28] [V-B Visual servoing under strict constraints, but contact vulnerability · 正文段落 54](https://arxiv.org/html/2610.07594v1#S5.SS2.p1.1)
- [S29] [V-B Visual servoing under strict constraints, but contact vulnerability · 正文段落 55](https://arxiv.org/html/2610.07594v1#S5.SS2.p2.1)
- [S30] [VI Discussion and limitations · 正文段落 61](https://arxiv.org/html/2610.07594v1#S6.p2.1)
- [S31] [VII Conclusion · 正文段落 62](https://arxiv.org/html/2610.07594v1#S7.p1.1)
- [S32] [B-B Action Representation and Controller Contract · 正文段落 71](https://arxiv.org/html/2610.07594v1#A2.SS2.p1.1)
- [S33] [B-B Action Representation and Controller Contract · 正文段落 72](https://arxiv.org/html/2610.07594v1#A2.SS2.p2.1)
- [S34] [B-D Simulation Throughput and Training Compute · 正文段落 78](https://arxiv.org/html/2610.07594v1#A2.SS4.p1.1)
- [S35] [B-D Simulation Throughput and Training Compute · 正文段落 79](https://arxiv.org/html/2610.07594v1#A2.SS4.p2.1)
- [S36] [B-D Simulation Throughput and Training Compute · 正文段落 80](https://arxiv.org/html/2610.07594v1#A2.T3)
- [S37] [B-D Simulation Throughput and Training Compute · 正文段落 81](https://arxiv.org/html/2610.07594v1#A2.T3.10)
- [S38] [C-B Demonstration Motion Statistics · 正文段落 83](https://arxiv.org/html/2610.07594v1#A3.SS2.p1.1)
- [S39] [D-D Shared Training Augmentation · 正文段落 107](https://arxiv.org/html/2610.07594v1#A4.T5)
- [S40] [Appendix E Evaluation Protocol and Checkpoint Selection · 正文段落 111](https://arxiv.org/html/2610.07594v1#A5.p1.1)
- [S41] [Appendix E Evaluation Protocol and Checkpoint Selection · 正文段落 112](https://arxiv.org/html/2610.07594v1#A5.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/BiGym 2.0 Benchmarking Learned and Agent-Developed Policies for Humanoid Househo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchronised multi-camera views and full-body execution records. We benchmark vision-language-action fine-tuning, imitation learning, demo-driven reinforcement learning, and cold-start coding agents given the interaction budget of online reinforcement learning. With the same onboard views, proprioception and whole-body controller for every method, vision-language-action fine-tuning has the highest nine-task mean, and agent-developed programs outperform every demo-driven reinforcement learning baseline on this mean and lead on bimanual reaching. Cross-workspace stacking remains open, $π_{0.5}$ stays low on pick-box, and multi-object transport is hard for imitation learning, demo-driven reinforcement learning and coding agents. All environments, human demonstrations, and evaluation traces are open-sourced at https://github.com/swirl-uk/BiGym2.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.07594v1
- Authors: Zexi Zhang, Zecheng Zhu, Zidong Chen, Zulkhuu Tuya, Stephen James
- Published: 2026-10-06T01:33:35Z
- Age days: 1

</details>
