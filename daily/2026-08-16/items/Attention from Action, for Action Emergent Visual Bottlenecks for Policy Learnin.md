---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13422v1"
published: "2026-08-13T16:14:07Z"
age_days: 2
score: 24
created: 2026-08-16
concepts: ["世界模型", "具身智能评测与基准"]
---

# Attention from Action, for Action: Emergent Visual Bottlenecks for Policy Learning

> [!summary] 一句话结论（基于摘要）
> In simulation and the real world, Seeker improves data efficiency and robustness over no-crop, augmentation, and action-derived crop baselines.

## 关键点

- **问题**：Visual bottlenecks that focus policy inputs on regions of interest (ROIs) can improve data-efficient visuomotor learning by separating where to look from how to act.
- **创新点 / 方法**：We propose Seeker, a task- and state-conditioned readout that learns attention from action.
- **证据**：In simulation and the real world, Seeker improves data efficiency and robustness over no-crop, augmentation, and action-derived crop baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Attention from Action, for Action Emergent Visual Bottlenecks for Policy Learnin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual bottlenecks that focus policy inputs on regions of interest (ROIs) can improve data-efficient visuomotor learning by separating where to look from how to act. Many ROI interfaces rely on external spatial labels, such as gaze, object classes, or affordance annotations. Label-free alternatives often derive crops from trajectories by detecting gripper or motion events and centering a fixed crop at the projected end-effector. Such action-derived crops are useful spatial priors that require no additional labels, but they encode fixed choices about event timing, proxy points, and crop scale. When the visual evidence needed for control lies away from the end-effector or changes continuously with task progress, these crops can become misaligned. We propose Seeker, a task- and state-conditioned readout that learns attention from action. Starting from frozen DINOv3 features, Seeker iteratively updates a query with gathered visual evidence, producing progression-aware ROIs solely from action supervision. The learned ROI serves as a spatial interface for RGB cropping, mask-guided background augmentation, and point-cloud filtering. In simulation and the real world, Seeker improves data efficiency and robustness over no-crop, augmentation, and action-derived crop baselines. On real robots, Seeker raises average in-domain success from the best baseline's 48.3% to 76.7% and success under lighting/background shifts from 20.0% to 60.0%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13422v1
- Authors: Zheyu Zhuang, Ruiyu Wang, Nick Heppert, Johannes Fabian Hahn, Abhinav Valada, Florian T. Pokorny, Danica Kragic
- Published: 2026-08-13T16:14:07Z
- Age days: 2

</details>
