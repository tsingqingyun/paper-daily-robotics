---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.28090v1"
published: "2026-08-28T08:58:20Z"
age_days: 2
score: 25
created: 2026-08-31
concepts: ["Sim2Real", "具身智能评测与基准"]
---

# Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters

> [!summary] 先说人话（基于摘要）
> 论文让人形机器人坐在无动力脚轮椅上，仅靠双脚间歇蹬地实现全向移动。策略不模仿动作，actor 只看本体感觉和速度命令，却可零样本迁移到 Unitree G1。

## 问题

站立人形持续耗力，而坐姿移动涉及未固定的骨盆—座椅接触、椅子被动动力学和间歇足地推进，标准站立速度跟踪环境无法直接处理。

## 创新点或方法

在站立速度跟踪环境中加入被动椅模型、坐姿奖励、仅 critic 可见的椅子观测和定制接触设置。actor 输出关节控制，只输入本体感觉与速度命令；训练比较对称正则、足滑正则和命令课程的八种组合。

## 证据

随机命令评测中，策略几乎完成全部 20 秒 rollout，最佳坐姿策略的速度跟踪可超过 Standing 策略。四个种子上的 2^3 因子实验显示 FS 降低 CoT 但增加跟踪误差，部分 FS-only 策略陷入静止局部最优；FS 加 SY 或 CC 可避免。策略零样本迁移到 Unitree G1 并实现全向坐姿移动。


## 局限

摘要没有给实机跟踪误差、稳定时间或成功率；“几乎全部”也非精确数字，零样本迁移的稳健性需看全文和视频。

- **判断**：值得精读训练环境和因子实验；任务新颖且实机展示关键，但实际可靠性不能只凭定性迁移结论。

## 研究关联

对 Sim2Real 和人形机器人研究者，这是新的接触丰富移动形态，并提供较完整的正则化交互分析；也为未来坐姿移动操作奠定底层运动能力。

- **概念**：Sim2Real 具身智能评测与基准
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/Stay Seated Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Cha.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots with quasi-direct-drive actuators continuously generate joint torque while standing, whereas seated humans delegate weight support to chairs during desk work. As a first step toward seated loco-manipulation, we study omnidirectional seated locomotion on a passive mobile chair, requiring unfixed pelvis-seat contact and intermittent foot-floor propulsion of the robot-chair system. We extend a standard standing velocity-tracking environment with a passive-chair model, seated-state rewards, critic-only chair observations, and task-tailored contact settings. The policy is learned without motion-imitation rewards; its actor uses only proprioception and velocity commands, without contact sensing or chair states. In random-command evaluation, the policies tracked omnidirectional commands through nearly all 20-s rollouts, and the best seated policies could outperform the Standing policy in velocity tracking. Across four training seeds, a $2^3$ full-factorial comparison of symmetry regularization (SY), foot-slip regularization (FS), and command curriculum (CC) showed that FS reduced CoT but increased tracking error and that some FS-only policies converged to stationary local optima. Combining FS with either SY or CC avoided this failure without retuning FS, while SY improved bilateral leg symmetry during longitudinal motion. Direction-resolved analysis showed CoT ordered backward $<$ lateral $\ll$ forward, with planted-leg extension in backward and lateral motion and knee flexion following heel contact in forward motion. The learned policy achieved zero-shot sim-to-real transfer to a Unitree G1 and generated omnidirectional seated locomotion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.28090v1
- Authors: Kango Yanagida, Kazuki Miyazawa, Takato Horii
- Published: 2026-08-28T08:58:20Z
- Age days: 2

</details>
