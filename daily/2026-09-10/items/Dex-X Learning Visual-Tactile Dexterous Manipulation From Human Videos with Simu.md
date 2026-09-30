---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07747v1"
published: "2026-09-07T16:47:39Z"
age_days: 2
score: 25
created: 2026-09-10
concepts: ["世界模型", "机器人学习", "Sim2Real"]
---

# Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction

> [!summary] 先说人话（基于摘要）
> DEX-X 用仿真补上人类视频里看不到的触觉：先重建手与物体的接触，再用模拟触觉训练可部署的视觉—触觉灵巧操作策略。

## 问题

人类视频提供丰富动作，却缺少接触密集操作需要的触觉监督；任务是在不采集机器人侧示范数据的条件下学到可部署策略。

## 创新点或方法

由单目示范重建仿真手物交互，用物理接触动力学生成触觉监督，训练策略后蒸馏为接收点云观测和触觉感知的部署策略。

## 证据

教师策略在仿真六类任务中平均成功率为 65.9%；蒸馏策略零样本迁移实机，方块拾取成功率 93%，擦桌任务为 53%，并在拾取中观察到对未见物体几何的零样本泛化。


## 局限

需核查手物重建与接触参数的准确性；仿真平均值和两个实机任务的成功率口径不同，不能据此比较教师与学生强弱。

- **判断**：值得重点读重建、触觉生成和蒸馏链路，真实接触任务结果有价值，但距大规模任意人类视频学习仍需验证。

## 研究关联

对机器人学习和 Sim2Real 研究者，提供了将人类视频转成多模态接触监督的具体路径；仿真在这里承担物理信息补全作用。

- **概念**：世界模型 机器人学习 Sim2Real
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/Dex-X Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simu.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human videos are an abundant source of dexterous manipulation behaviors, but they lack tactile information that is crucial for contact-rich interaction. This raises a fundamental question: can robots learn deployable visual-tactile dexterous manipulation policies from human video demonstrations without robot-side data collection? We present DEX-X, a framework for learning visual-tactile dexterous manipulation from human videos through simulation. Our key insight is that simulation can serve as a tactile completion engine. Given monocular human demonstrations, DEX-X reconstructs hand-object interactions in simulation, where physically grounded contact dynamics provide tactile supervision unavailable in the original videos. Leveraging this recovered tactile information, we train visual-tactile dexterous manipulation policies and distill them into deployable policies operating on point-cloud observations and tactile sensing. We demonstrate zero-shot sim-to-real transfer on a dexterous hand-arm platform across diverse grasping and contact-rich tool-use tasks. The teacher policy achieves 65.9% average success across six task categories in simulation, while the distilled visual-tactile policy achieves 93% success on real-world cube picking and 53% on the challenging table-cleaning task. Zero-shot generalization to unseen object geometries is also observed on object-picking tasks. Our results suggest that simulated interaction is a key bridge between human videos and deployable dexterous manipulation policies, providing the missing physical supervision needed for scalable robot skill learning from Internet-scale human video data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07747v1
- Authors: Ruoqu Chen, Feixiang Ruan, Liu Cao, Zihao Wang, Botian Xu, Shiqin Tong, Jiajun Liu, Mingzhi Pei, Chenyu Zhang, Wanli Xing, Kaifeng Zhang, Mengdi Xu
- Published: 2026-09-07T16:47:39Z
- Age days: 2

</details>
