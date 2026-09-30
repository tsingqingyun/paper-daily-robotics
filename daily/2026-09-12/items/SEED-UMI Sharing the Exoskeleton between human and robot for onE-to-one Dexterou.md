---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11753v1"
published: "2026-09-10T16:08:58Z"
age_days: 1
score: 27
created: 2026-09-12
concepts: ["机器人学习", "具身智能评测与基准"]
---

# SEED-UMI: Sharing the Exoskeleton between human and robot for onE-to-one Dexterous demonstration

> [!summary] 先说人话（基于摘要）
> SEED-UMI让人和机器人使用同一套外骨骼，使示教与执行共享测量和腕部视觉参照，减少接触操作中的跨具身偏差。

## 这篇到底在做什么

- **卡在哪里**：灵巧手模仿学习缺少能可靠迁移的接触丰富示教。以往仅在人侧记录的外骨骼系统依赖自由空间标定的开环映射，遇到接触后映射质量下降。
- **关键解法**：人和机器人均佩戴相同外骨骼，关节编码器构成共享测量，腕部相机在采集与执行时观察相同外部机构；据此建立配对跨具身监督，直接使用原始腕部图像训练策略。
- **拿什么证明**：在五项接触丰富任务中，数据采集效率为外骨骼遥操作的3.0倍，平均策略执行成功率70.0%。

## 值不值得读

- **和你的研究有什么关系**：对灵巧操作学习，价值在于通过共享硬件与视觉条件改善示教一致性，为接触任务提供数据采集路径。
- **先别急着信**：需核查采集效率的计量口径，以及机器人佩戴共享外骨骼后对动作范围和适用任务的影响。
- **判断**：值得精读硬件接口和示教流程，适合正在解决灵巧手数据采集问题的团队。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/SEED-UMI Sharing the Exoskeleton between human and robot for onE-to-one Dexterou.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Imitation learning for dexterous hands is bottlenecked by the difficulty of collecting contact-rich demonstrations that transfer faithfully to the robot. Prior wearable-exoskeleton systems record only on the human side and retarget via open-loop mappings calibrated in free space, which degrade under contact. We present SEED-UMI, a framework in which both the human and the robot wear the same exoskeleton: joint encoders become a physically shared measurement, and wrist cameras mounted to the exoskeleton observe the same outer mechanism during both human data collection and robot policy rollouts. This turns retargeting into paired cross-embodiment supervision and lets policies train directly on raw exoskeleton-centric wrist images, without segmentation or inpainting. On five contact-rich tasks, SEED-UMI achieves 3.0x greater data collection efficiency than exoskeleton-based teleoperation and a 70.0% average rollout success rate.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11753v1
- Authors: Tengbo Yu, Jiahao Wu, Daohan Li, Bingxu Chen, Hao Liu, Xiaojian Ma, Hangxin Liu
- Published: 2026-09-10T16:08:58Z
- Age days: 1

</details>
