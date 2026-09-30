---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11433v1"
published: "2026-09-10T12:05:54Z"
age_days: 1
score: 29
created: 2026-09-12
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Safety-aware Skill Adaptation for Reinforcement Learning in Dynamic Environments

> [!summary] 先说人话（基于摘要）
> Dist-GPRL让机器人逐段调整已有技能轨迹，并用障碍距离引导探索。它通过高斯过程保持相邻轨迹修改连贯，降低整段动作一起优化的难度。

## 这篇到底在做什么

- **卡在哪里**：动态杂乱环境中，探索可能靠近障碍或移动物体，引起碰撞和学习不稳定；已有技能适配方法常依赖固定观测或严格探索日程。
- **关键解法**：对稀疏轨迹途经点的重叠局部窗口顺序适配，用GP协方差关联策略输出；HAP安全子空间先验引导探索，动态距离场及梯度奖励提供局部避障信息，运动学相似正则保留示教速度和加速度特征。
- **拿什么证明**：在两项仿真动态物体操作任务中评估，并将学习策略迁移到真实机器人。摘要报告成功率更高、碰撞更少、学习更稳定且保留示教运动学特征，但未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：适合机器人学习中已有示教技能的局部适配，提供轨迹结构、探索与障碍感知共同设计的方案。
- **先别急着信**：安全主要通过先验与奖励引导，摘要未给出硬约束保证；需要核查实机迁移结果和动态障碍设置。
- **判断**：值得读局部窗口与安全引导机制，优先确认量化收益后再考虑复现。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/Safety-aware Skill Adaptation for Reinforcement Learning in Dynamic Environments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Skill adaptation frameworks based on reinforcement learning often require restrictive assumptions to maintain stability, such as fixed observations or tightly controlled exploration schedules. In cluttered and dynamic environments, however, unrestricted exploration can lead to unsafe behaviour and unstable learning, particularly when task-relevant observations lie near obstacles or involve moving objects. In this work, we present Dist-GPRL, a distance-aware and safety-guided reinforcement learning framework for structured robot skill adaptation. Building upon Gaussian Process (GP)-based skill parameterisation, our framework sequentially adapts overlapping local windows of sparse trajectory via-points rather than modifying the complete skill at every policy step. Raw policy outputs are correlated through the GP covariance structure, producing temporally coherent trajectory updates while reducing the action-space and credit-assignment difficulties associated with global trajectory adaptation. Safety is incorporated through two complementary forms of guidance. A safe-subspace prior derived from the Hausdorff Approximation Planner (HAP) biases policy exploration toward feasible regions, while dynamically updated distance field clearance and gradient rewards provide local obstacle awareness. A trajectory-kinematics similarity regulariser further preserves the demonstrated velocity and acceleration characteristics during adaptation. We evaluate the framework on two dynamic object-manipulation tasks in simulation and transfer the learned policy to real-world robot execution. Experimental results demonstrate higher task success, lower collision frequency, and more stable learning than the baselines, while preserving the kinematic characteristics of the demonstrated skill.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11433v1
- Authors: A K M Nadimul Haque, Sheila Sutjipto, Marc G. Carmichael, Teresa Vidal-Calleja
- Published: 2026-09-10T12:05:54Z
- Age days: 1

</details>
