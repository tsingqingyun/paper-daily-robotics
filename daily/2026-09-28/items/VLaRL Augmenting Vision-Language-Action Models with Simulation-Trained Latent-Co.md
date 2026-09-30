---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30868v1"
published: "2026-09-25T06:18:40Z"
age_days: 3
score: 44
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL

> [!summary] 先说人话（基于摘要）
> VLaRL 给冻结的 VLA 加一个在仿真里训练的动作修正器，改善接触操作中的执行偏差。它用 VLA 内部表示连接仿真与现实，再通过轻量映射对齐两边的表示分布。

## 问题

任务是提高接触密集操作的物理执行精度。残差 RL 可以修正 VLA，但真机训练昂贵且涉及安全；改在仿真训练后，视觉域差异又会妨碍修正策略迁移。

## 创新点或方法

残差控制以冻结 VLA 的视觉语言潜变量为条件，轻量 mapper 将仿真潜变量映射向真实分布。关键差异是以内部表示作为迁移接口，避免依赖像素级视觉对应，部署时无需真机 RL 或在线适应。

## 证据

在四个接触密集任务、两个 VLA 骨干上，所有任务与骨干组合的真机成功率均提高；受控消融支持潜变量条件和潜变量对齐都有作用。摘要未给出可核查的成功率或增益数字。

## 局限

需核查真实潜变量分布如何获取、mapper 使用哪些真实数据，以及四个任务覆盖的接触变化范围。无需真机 RL 不等于无需真实数据。

- **判断**：值得精读方法与迁移消融，重点判断潜变量对齐能否复用于自己的 VLA 和接触任务。

## 研究关联

对 VLA 和 Sim2Real 研究者，这是保留基础策略能力、通过仿真补足接触控制精度的具体路径；其直接贡献是控制迁移接口，而非世界模型预测。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：44
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/VLaRL Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Co.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models provide broad, instruction-conditioned manipulation behaviors, but their physical execution can remain imprecise during contact-rich interaction. Residual reinforcement learning (RL) can correct such errors while keeping the VLA frozen, but real-robot RL is costly and safety-critical. We propose VLA Latent-Conditioned RL (VLaRL), which enables residual RL for frozen VLAs to be trained in simulation and deployed on real robots without real-world RL or online adaptation. The key challenge is transferring the learned residual policy despite the visual gap between simulation and reality. Rather than requiring pixel-level visual correspondence, VLaRL uses the VLA's internal vision-language latent representation to condition residual control and as the sim-to-real transfer interface, and learns a lightweight mapper that transforms simulation-derived latents toward the real latent distribution. Across four contact-rich manipulation tasks and two VLA backbones, VLaRL improves real-world success in all task-backbone combinations, while controlled ablations demonstrate the importance of both latent conditioning and latent alignment for transferring simulation-trained residual control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30868v1
- Authors: Namiko Saito, Kinam Kim, Heecheol Kim, Katsushi Ikeuchi, Yasuyuki Matsushita
- Published: 2026-09-25T06:18:40Z
- Age days: 3

</details>
