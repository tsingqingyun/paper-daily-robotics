---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00478v1"
published: "2026-08-31T23:27:14Z"
age_days: 2
score: 28
created: 2026-09-03
concepts: ["具身智能评测与基准"]
---

# Beyond Object Selection:Markerless Gaze-based Robot Placement at Arbitrary Position

> [!summary] 先说人话（基于摘要）
> 论文把凝视交互从“选物体”推进到任意位置放置，并提出任务级指标 GSIE，直接测量凝视射线与目标表面的交点误差。结果说明传统位姿误差小，并不保证凝视放置更准。

## 这篇到底在做什么

- **卡在哪里**：头显与机器人跨设备对齐中，平移和旋转误差会共同作用于凝视射线，甚至相互抵消；因此优化常规位姿指标可能无法优化最终放置位置，稀疏机器人参考也增加对齐难度。
- **关键解法**：无标记交互框架配套跨设备数据集，以 Graph-based Reference Selection 选择稀疏参考，并在统一协议下比较多种任务专用对齐管线；GSIE 直接在目标表面评价最终空间误差。
- **拿什么证明**：实验发现按常规位姿指标排名靠前的方法并不总能在 GSIE 上最优；摘要未给出数据集规模或误差数字。

## 值不值得读

- **和你的研究有什么关系**：它提醒辅助操作与人机交互评测应对准最终任务误差，而非代理位姿指标，可直接影响凝视控制标定和方法选择。
- **先别急着信**：摘要未说明用户数量、表面类型、工作空间和机器人执行误差是否纳入，因而尚难判断 GSIE 的普适性。
- **判断**：值得读指标定义和排名反转分析；方法贡献可能有限，但任务级评价观点很实在。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Beyond Object Selection Markerless Gaze-based Robot Placement at Arbitrary Posit.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Gaze-based assistive manipulation typically supports object selection, while arbitrary-position placement requires accurate spatial alignment between the headset and robot. However, for gaze-based manipulation, pose accuracy does not necessarily translate into task accuracy: translational and rotational errors jointly affect the transformed gaze ray and may compensate for each other. To study cross-device alignment from this task-oriented perspective, we present a markerless interaction framework and a dedicated cross-device dataset. We propose Graph-based Reference Selection to address sparse robot references. We further develop and benchmark multiple task-specific alignment pipelines under a unified protocol. Specifically, we introduce Gaze--Surface Intersection Error (GSIE), which directly measures the spatial error of the gaze-specified target. Experiments show that alignment methods ranked highly by conventional pose metrics are not always optimal in GSIE, demonstrating the importance of evaluating gaze-based manipulation at the task level.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00478v1
- Authors: Yuzhi Lai, William Marx, Shenghai Yuan, Peizheng Li, Zhuoyu Ran, Andreas Zell
- Published: 2026-08-31T23:27:14Z
- Age days: 2

</details>
