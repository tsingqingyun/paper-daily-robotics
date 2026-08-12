---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23589v1"
published: "2026-06-22T16:57:43Z"
age_days: 2
score: 31
created: 2026-06-25
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies

> [!summary] 一句话结论（基于摘要）
> Compared with the memory-free baseline (e.g., $π_{0.5}$), KEMO improves aggregate Task Success Rate by 23.6\% and Stage Completion Rate by 34.1\%.

## 关键点

- **问题**：Long-horizon robot manipulation remains challenging because similar observations may occur at different execution stages, while the appropriate action depends on previously completed operations.
- **创新点 / 方法**：In this work, we propose propose KEMO, a lightweight plug-in memory framework that automatically selectively preserves keyframes associated with task-relevant state changes for VLA policies.
- **证据**：Compared with the memory-free baseline (e.g., $π_{0.5}$), KEMO improves aggregate Task Success Rate by 23.6\% and Stage Completion Rate by 34.1\%.
- **局限**：Long-horizon robot manipulation remains challenging because similar observations may occur at different execution stages, while the appropriate action depends on previously completed operations.

## 研究关联

- **概念**：[[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/KEMO Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA P.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon robot manipulation remains challenging because similar observations may
occur at different execution stages, while the appropriate action depends on previously
completed operations. Memory can address this ambiguity by enabling policies to infer
task progress from execution history. However, existing memory-augmented approaches
often either retain dense histories that require compression or rely primarily on recent
context that may discard earlier task-relevant events. In this work, we propose propose
KEMO, a lightweight plug-in memory framework that automatically selectively preserves
keyframes associated with task-relevant state changes for VLA policies. KEMO combines
robot kinematics with visual filtering to detect events, encodes the selected keyframes
as compact temporally ordered memory tokens, and integrates them with current visual
features through cross-attention and gated residual fusion for VLA training. The
detected events also define higher-weight training samples near critical transitions. We
evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored
subtasks, and trajectory length ranging from 830 steps to 2846 execution steps
(durations from 28 to 95 seconds). Compared with the memory-free baseline (e.g.,
$π_{0.5}$), KEMO improves aggregate Task Success Rate by 23.6\% and Stage Completion
Rate by 34.1\%. Ablations show that event-driven keyframe selection outperforms uniform
sampling and recent-frame retention, while the proposed gated fusion and keyframe-
aligned loss weighting provide complementary gains.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23589v1
- Authors: Yihan Zeng, Minghao Ye, Yiyuan Chen, Yide Shentu, Philipp Wu, Zike Yan, Zhongyu Li
- Published: 2026-06-22T16:57:43Z
- Age days: 2

</details>
