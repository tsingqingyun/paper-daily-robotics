---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04552"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-09-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI

> [!summary] 先说人话（基于摘要）
> CFAMs 让机器人部署后把新经验存成可复用的能力单元，同时冻结慢学习模块以保留旧能力。更新在设备上完成，不需要梯度训练。

## 问题

目标场景训练数据有限、只有机载计算，系统还需适应新情况而不遗忘已有技能；摘要将开放世界新颖性明确排除在范围之外。

## 创新点或方法

冻结的慢模块分别承担三维感知、任务技能分解与结果评估、几何技能执行；快速 Capsule Field 通过 Competence Capsules 一次性、无梯度保存经验，实验室少样本安装技能，现场吸收已验证的近分布外案例。

## 证据

覆盖五种机器人形态；使用 40% 数据达到全数据标准策略的工作点，测试时动作成功率提高 13.9 个百分点；顺序仿真中后向迁移为 -0.5 个百分点，LoRA 为 -11.4 个百分点。


## 局限

需核查能力胶囊的内容、检索与验证机制，以及自建多形态数据上的基线比较是否覆盖相同能力边界。

- **判断**：值得精读现场经验验证和持续学习实验；数字明确，但结论必须限定在已验证的近分布外适应。

## 研究关联

对 VLA 部署后适应有参考价值，重点是通过结构化经验扩充实现快速更新与能力保留；摘要未展示开放世界适应。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04552v1 Announce Type: new Abstract: Unattended interactive autonomy - machines that step into danger in place of humans and complete tasks with human tools - remains a missing capability in mission-critical operations. These domains offer scarce training data and only onboard compute, yet deployed systems must face novelty without erasing prior competence. We introduce Continual Field-Adaptive Models (CFAMs), which learn efficiently in the lab and continue learning after deployment through autonomous, gradient-free, on-device updates. CFAM uses a complementary learning architecture with a frozen slow-learning component and a fast-learning Capsule Field. The slow component contains three cortices: Sensor, which maps multimodal input into 3D-grounded geometry; Reasoning, which decomposes tasks into skills and evaluates outcomes; and Action, which executes geometric skills. The Capsule Field stores field learning one-shot and gradient-free as Competence Capsules. Skill installation is few-shot in the lab and continual in the field; open-world novelty is outside scope. We evaluate CFAM across five embodiments: manipulator, quadruped, humanoid, quadrotor, and off-road vehicle. Baselines (pi0, CogACT, SpatialVLA) use the same in-house multi-embodiment dataset for physical-platform comparisons. CFAM reaches the operating point of a standard policy trained on the full prior-training dataset using 40% of the data, or 2.5x fewer trajectories. At test time, autonomous capture of verified near-OOD cases improves action success by 13.9 percentage points. In sequential simulation, backward transfer is -0.5 percentage points versus -11.4 for LoRA. CFAM therefore provides a bounded form of post-deployment physical intelligence: few-shot skill learning, autonomous field growth from verified near-OOD experience, and retention of prior competence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04552
- Authors: Amarjot Singh, Tanmay R. Pancholi, Jainam Kothari, Shrirang Mahajan, Ketan Bansal, Zackory Erickson, Giuseppe Loianno, Alexandre M. Bayen, Jeff Schneider, Vince Nakayama
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
