---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09125v1"
published: "2026-08-10T05:04:02Z"
age_days: 1
score: 38
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Trajectory Divergence Horizon Decision for Reliable Dual-Arm Surgical Subtask Manipulation

> [!summary] 一句话结论（基于摘要）
> On real hardware with 20 trials per task setting, TDHD consistently improves performance over the latest VLA baselines: success increases from 55\% to 60\% for needle manipulation and from 55\% to 80\% for tissue manipulation, with the largest gains observed…

## 关键点

- **问题**：Learning-based controllers improve generalization compared with rule-based and analytic approaches, but most are trained for individual tasks and remain difficult to reuse across procedures.
- **创新点 / 方法**：Surgical robotic systems are increasingly being adopted as clinical workload rises, motivating autonomous solutions for repetitive manipulation subtasks.
- **证据**：On real hardware with 20 trials per task setting, TDHD consistently improves performance over the latest VLA baselines: success increases from 55\% to 60\% for needle manipulation and from 55\% to 80\% for tissue manipulation, with the largest gains observed in the final manipulation stages.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Surgical robotic systems are increasingly being adopted as clinical workload rises,
motivating autonomous solutions for repetitive manipulation subtasks. Learning-based
controllers improve generalization compared with rule-based and analytic approaches, but
most are trained for individual tasks and remain difficult to reuse across procedures.
Vision-Language-Action (VLA) models provide a unified framework that integrates visual
perception, language grounding, and action generation, offering a promising path toward
more composable surgical autonomy. However, existing VLA policies rely on fixed-length
open-loop action sequences, where changing scene conditions can lead to accumulated
errors and potential risks in surgical manipulation. To mitigate this issue, we
formulate surgical VLA deployment as an adaptive execution-horizon decision problem and
propose Trajectory Divergence Horizon Decision (TDHD), a test-time mechanism that
estimates step-wise action reliability by measuring the divergence between two flow-
matching-generated trajectories under small noise perturbations and truncates execution
using a dual-threshold rule to trigger timely replanning. We further establish a real-
world da Vinci-like dual-arm benchmark with synchronized multi-view perception and
language instructions, and collect 600 teleoperated demonstrations across needle (reach,
pick, regrasp) and tissue (reach, lift, resection) manipulation suites. On real hardware
with 20 trials per task setting, TDHD consistently improves performance over the latest
VLA baselines: success increases from 55\% to 60\% for needle manipulation and from 55\%
to 80\% for tissue manipulation, with the largest gains observed in the final
manipulation stages. These results highlight the importance of adaptive execution
control for reliable deployment of VLA models in surgical robotic manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09125v1
- Authors: Mingwu Su, Guankun Wang, Jinsong Lin, Rulin Zhou, Ziyi Hao, Zhiwei Fang, Huxin Gao, Jiewen Lai, Jiazheng Wang, Fan Zhang, Hongliang Ren
- Published: 2026-08-10T05:04:02Z
- Age days: 1

</details>
