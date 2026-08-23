---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19188v1"
published: "2026-08-19T17:56:11Z"
age_days: 3
score: 21
created: 2026-08-23
concepts: ["世界模型", "具身智能评测与基准"]
---

# PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views

> [!summary] 一句话结论（基于摘要）
> This work proposes PartialBiGrasp, a dual-arm grasp generation framework that operates directly on partial point cloud observations.

## 关键点

- **问题**：Dual-arm robotic grasping is essential for manipulating large, heavy, and geometrically complex objects that cannot be reliably handled using a single manipulator.
- **创新点 / 方法**：This work proposes PartialBiGrasp, a dual-arm grasp generation framework that operates directly on partial point cloud observations.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Dual-arm robotic grasping is essential for manipulating large, heavy, and geometrically complex objects that cannot be reliably handled using a single manipulator.

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/PartialBiGrasp Inferring Hidden Local Geometry for Bimanual Grasping from Partia.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Dual-arm robotic grasping is essential for manipulating large, heavy, and geometrically complex objects that cannot be reliably handled using a single manipulator. These large objects often contain only sparse graspable regions determined by local geometric properties such as thickness, edge structure, and gripper clearance. Prior bimanual grasping methods assume access to a full point cloud of the object which inherently contains this geometric information, but may not be accessible in real scenarios. This work proposes PartialBiGrasp, a dual-arm grasp generation framework that operates directly on partial point cloud observations. Our model learns geometric features implicitly through convolutional occupancy networks, enabling local reasoning about graspability, collision-free contact regions, and object thickness. We leverage this understanding to generate force-closure compliant grasp pairs, which are further refined using a sampling-based optimization to correct for ambiguity caused by incomplete geometry. We evaluate our approach using analytical force-closure metrics, large-scale simulation experiments, and real-world robot evaluations on noisy partial point clouds of novel objects, demonstrating robust and physically stable dual-arm grasp generation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19188v1
- Authors: Ayush Kaura, Vignesh Vembar, Md Faizal Karim, Keshab Patra, K Madhava Krishna
- Published: 2026-08-19T17:56:11Z
- Age days: 3

</details>
