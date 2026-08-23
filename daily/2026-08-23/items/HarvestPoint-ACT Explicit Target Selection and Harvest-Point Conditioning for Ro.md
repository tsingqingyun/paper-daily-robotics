---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18446v1"
published: "2026-08-19T02:21:27Z"
age_days: 4
score: 20
created: 2026-08-23
concepts: ["机器人学习", "具身智能评测与基准"]
---

# HarvestPoint-ACT: Explicit Target Selection and Harvest-Point Conditioning for Robotic Fruit Harvesting under Occlusion

> [!summary] 一句话结论（基于摘要）
> On a canopy mock-up, HarvestPoint-ACT achieves a success rate of 88%, and of 75% under heavy occlusion.

## 关键点

- **问题**：Occlusion can make the policy lose the selected fruit during harvesting, and the correct closing point is difficult to infer from pixels alone.
- **创新点 / 方法**：End-to-end imitation learning avoids hand-made robot motion for approaching and grasping, but the policy must still decide which fruit to pick and where to close the gripper.
- **证据**：On a canopy mock-up, HarvestPoint-ACT achieves a success rate of 88%, and of 75% under heavy occlusion.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：20
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/HarvestPoint-ACT Explicit Target Selection and Harvest-Point Conditioning for Ro.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end imitation learning avoids hand-made robot motion for approaching and grasping, but the policy must still decide which fruit to pick and where to close the gripper. Occlusion can make the policy lose the selected fruit during harvesting, and the correct closing point is difficult to infer from pixels alone. This paper presents HarvestPoint-ACT, which makes both decisions explicit in perception and provides them to the policy. An instance segmentation front end with a keypoint branch predicts a mask and a harvest point for each visible fruit, where the harvest point specifies the location to close the gripper. A scheduler ranks detected candidates by occlusion and travel distance and selects one target. After each attempt, it redetects and reranks the candidates because the canopy may have changed. The selected fruit is encoded for an action chunking transformer as an eight-dimensional state, containing the absolute harvest point, the vector from the gripper to that point, a validity flag, and a confidence score. When the selected fruit is temporarily undetected, the system retains the last harvest point estimate in the robot base frame and marks it as stale, and aborts the attempt if the loss persists. On a canopy mock-up, HarvestPoint-ACT achieves a success rate of 88%, and of 75% under heavy occlusion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18446v1
- Authors: Hanying Hu, Weipeng Li, Yikun Huang, Hao Chen, Zhengtao Hu, Changcai Yang, Weiwei Wan
- Published: 2026-08-19T02:21:27Z
- Age days: 4

</details>
