---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.31349v1"
published: "2026-09-25T14:47:17Z"
age_days: 2
score: 29
created: 2026-09-28
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models

> [!summary] 先说人话（基于摘要）
> DyMD 要解决视频世界模型压缩后“画面还行，但机器人和物体不怎么动”的问题。它同时调整教师去噪指导和评分模型训练，让少步生成保留交互动力学。

## 问题

多步视频扩散推理昂贵，而 DMD 蒸馏可能保留外观却削弱运动。摘要指出，弱重加噪会使教师难以纠正缺运动轨迹，较强运动轨迹又容易产生更大的 fake-score 拟合误差。

## 创新点或方法

按当前轨迹的交互保真度调整重加噪时间步分布，平衡恢复运动与细化外观；再用噪声条件预测器估计动力学相关拟合难度，提高困难轨迹在 critic 损失中的权重。辅助机制无需在推理时保留。

## 证据

将 14B 教师蒸馏为四步 1.3B 学生。相对 Base DMD，R-Bench 任务遵循提高 9.6 个百分点，PAI-Bench-G Domain 分数提高 5.1 分，视觉质量相近；两个 WorldArena 任务的下游规划平均成功率为 34%，基线为 16%。

## 局限

下游规划证据只有两个任务，平均成功率仍为 34%；需核查动力学指标与规划收益是否在更广任务上保持一致。

- **判断**：值得精读失效分析和蒸馏消融，是今天世界模型效率方向较有实证支撑的一篇。

## 研究关联

对世界模型与智能体研究者，它把压缩评价从视觉观感推进到交互运动和下游规划，直接回应快速预测是否仍对行动有用。

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/DyMD Preserving Interaction Dynamics through Distribution Matching Distillation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large video diffusion models offer expressive priors for embodied prediction and learning, yet their many-step sampling remains costly for interactive downstream use. Distribution Matching Distillation (DMD) enables few-step video generation, but can suppress robot--object motion while preserving visual quality. Examining DMD's teacher and fake-score signals, we find that weak re-noising keeps the teacher posterior concentrated near motion-deficient rollouts, limiting motion-restoring guidance. Meanwhile, stronger-motion rollouts tend to incur larger fake-score fitting errors, which can hinder the generator's learning of interaction dynamics. We propose DyMD, a DMD framework that adapts both teacher supervision and critic fitting to the evolving student. Temporal affinity--conditioned re-noise sampling adapts the timestep distribution to each rollout's current interaction fidelity by mixing the base schedule with a teacher prior motivated by local posterior variation, thereby balancing motion recovery and appearance refinement. To better track stronger-motion rollouts, dynamics-guided fake-score tracking uses a noise-conditioned predictor to estimate noise-relative fitting difficulty from latent temporal dynamics, then upweights predicted-hard rollouts in the critic loss. Using DyMD, we distill a 14B teacher into a four-step 1.3B student with no auxiliary modules at inference. On embodied-video benchmarks, the student improves R-Bench task adherence by $9.6$ percentage points and PAI-Bench-G Domain score by $5.1$ points over Base DMD while maintaining comparable visual quality. As a backbone for downstream action planning, our student achieves 34% mean success across two WorldArena tasks, compared with 16% for Base DMD.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.31349v1
- Authors: Haojun Xu, Jie Huang, Xin Lu, Mingchen Zhong, Zihao Fan, Linjiang Huang, Si Liu
- Published: 2026-09-25T14:47:17Z
- Age days: 2

</details>
