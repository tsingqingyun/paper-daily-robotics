---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22540v1"
published: "2026-06-21T14:54:07Z"
age_days: 2
score: 40
created: 2026-06-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3$\times$ and reduces physical execution steps by 51.4\%.

## 关键点

- **问题**：Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency.
- **创新点 / 方法**：To address this, we propose \textbf{PolicyTrim}, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps.
- **证据**：Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3$\times$ and reduces physical execution steps by 51.4\%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/PolicyTrim Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation,
yet their real-world deployment is often bottlenecked by execution efficiency. While
existing efforts predominantly focus on compute-centric efficiency to reduce per-step
inference latency, the intrinsic \textbf{policy efficiency} of these models remains
largely unexplored. Policy efficiency is fundamentally affected by two factors, namely
the effective executable length of predicted action chunks and the total physical steps
required to complete a task. These two factors jointly determine the total number of
forward inference calls during execution. We observe that current VLA policies struggle
with planning unreliability and action redundancy, suffering from severe prediction
degradation at the tail of action chunks and tending to generate unnecessarily redundant
physical steps. To address this, we propose \textbf{PolicyTrim}, a reinforcement
learning-based post-training framework that extends the reliable action chunk length and
reduces redundant physical steps. For reliable chunk extension, we employ a dynamic
exploration strategy that explicitly rewards the successful completion of longer
executable lengths, progressively pushing the trustworthy prediction horizon to its
empirical limit. For step efficiency, we design a redundancy-aware reward that directly
favors successful task completions with fewer steps while penalizing unreproducible
shortcuts, effectively eliminating redundant physical actions. Extensive experiments
across three benchmarks and three VLA models demonstrate that PolicyTrim improves action
chunk utilization by 3$\times$ and reduces physical execution steps by 51.4\%.
Ultimately, our framework delivers up to a 5.83$\times$ end-to-end deployment speedup
without compromising task success rates.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22540v1
- Authors: Xianghui Wang, Feng Chen, Wenbo Zhang, Hua Yan, Zixuan Wang, Changsheng Li, Yinjie Lei
- Published: 2026-06-21T14:54:07Z
- Age days: 2

</details>
