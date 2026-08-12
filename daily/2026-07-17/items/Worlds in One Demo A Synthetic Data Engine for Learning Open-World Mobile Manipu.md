---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13154v1"
published: "2026-07-14T18:04:58Z"
age_days: 2
score: 30
created: 2026-07-17
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation

> [!summary] 一句话结论（基于摘要）
> Experiments show that policies trained with WANDA achieve long-horizon robustness, broad spatial generalization and cross- environment generalization from one real demonstration.

## 关键点

- **问题**：Learning open-world mobile manipulation policies requires vast data to achieve spatial generalization, long-horizon robustness, and scene generalization.
- **创新点 / 方法**：To this end, we introduce WANDA: learning open-World mobile mANipulation from one demonstration via a synthetic DAta engine.
- **证据**：Experiments show that policies trained with WANDA achieve long-horizon robustness, broad spatial generalization and cross- environment generalization from one real demonstration.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning open-world mobile manipulation policies requires vast data to achieve spatial
generalization, long-horizon robustness, and scene generalization. Current prevailing
data collection paradigms, teleoperation and UMI, demand prohibitive human effort and
cost at scale. To scale beyond the limits of manual data collection, we seek to maximize
the value of each human demonstration by scalable data generation. To this end, we
introduce WANDA: learning open-World mobile mANipulation from one demonstration via a
synthetic DAta engine. WANDA first reconstructs background Gaussian splats and robot-
object interaction trajectories from source RGBD observations, as a world substrate for
later planning and rendering. It then rearranges contact-rich robot-object interaction
segments into extensive spatial configurations, utilizing whole-body motion planning to
chain them into new trajectories. To enhance long-horizon robustness, it applies
Corrective State Expansion to increase the robot and object state diversity at different
stages of mobile manipulation. To unlock cross-environment generalization, trajectories
are synthesized on diverse generated 3D worlds from everyday photos. Furthermore, we
synthesize photo-realistic observations by compositing rendered robot and object meshes
with Gaussian splatting backgrounds. We evaluate our approach on extensive simulation
and real-world tasks in various scenes. Experiments show that policies trained with
WANDA achieve long-horizon robustness, broad spatial generalization and cross-
environment generalization from one real demonstration. Moreover, WANDA naturally
supports cross-embodiment data generation, validated by zero-shot deployment on another
mobile manipulator with a distinct morphology.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13154v1
- Authors: Lingxiao Guo, Huanyu Li, Guanya Shi
- Published: 2026-07-14T18:04:58Z
- Age days: 2

</details>
