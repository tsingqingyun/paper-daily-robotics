---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25782v1"
published: "2026-05-25T12:29:47Z"
age_days: 0
score: 26
created: 2026-05-26
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# ParkourFormer: Integrating Predictive Supervision and Sequence Modeling into Parkour Locomotion

> [!summary] 一句话结论（基于摘要）
> Experiments in simulation and on a real humanoid robot show that ParkourFormer achieves a 93.85% average traversal success rate on highly challenging terrains, with improvements of up to 42.73% over strong MLP, MoE-based MLP, and vanilla Transformer baselines…

## 关键点

- **问题**：Humanoid parkour requires locomotion policies to coordinate whole-body dynamics across rapidly changing terrains such as stairs, gaps, slopes, and obstacles.
- **创新点 / 方法**：Such modeling becomes critical in agile locomotion tasks where successful motion execution depends strongly on anticipating upcoming contact transitions and body dynamics.We present ParkourFormer, a Transformer-based sequence modeling framework that reformulates humanoid locomotion as a future-conditioned decision-mak…
- **证据**：Experiments in simulation and on a real humanoid robot show that ParkourFormer achieves a 93.85% average traversal success rate on highly challenging terrains, with improvements of up to 42.73% over strong MLP, MoE-based MLP, and vanilla Transformer baselines, while maintaining a single unified policy across all terra…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/ParkourFormer Integrating Predictive Supervision and Sequence Modeling into Park.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid parkour requires locomotion policies to coordinate whole-body dynamics across
rapidly changing terrains such as stairs, gaps, slopes, and obstacles. Existing
reinforcement learning policies are largely reactive, mapping observations directly to
actions without explicitly modeling future body states. Such modeling becomes critical
in agile locomotion tasks where successful motion execution depends strongly on
anticipating upcoming contact transitions and body dynamics.We present ParkourFormer, a
Transformer-based sequence modeling framework that reformulates humanoid locomotion as a
future-conditioned decision-making problem. The current robot state queries historical
sensorimotor trajectories through cross-attention, while a lightweight prediction head
forecasts short-horizon future proprioceptive states. The predicted future states,
trained with supervised signals, are fused with temporal features to generate actions,
enabling the policy to jointly reason over motion history and anticipated future
dynamics. We evaluate ParkourFormer on a diverse multi-terrain humanoid parkour
benchmark including stairs, gaps, slopes, rough terrain, and obstacle traversal.
Experiments in simulation and on a real humanoid robot show that ParkourFormer achieves
a 93.85% average traversal success rate on highly challenging terrains, with
improvements of up to 42.73% over strong MLP, MoE-based MLP, and vanilla Transformer
baselines, while maintaining a single unified policy across all terrain types. These
results demonstrate that explicit future-state modeling significantly improves
robustness and generalization for agile whole-body locomotion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25782v1
- Authors: Yanheng Mai, Wenhao Xu, Zirui Huang, Yifei Fu, Shengwei Dong, Xinjue Wang, Kailun Huang, Yanzhe Xie, Renjing Xu
- Published: 2026-05-25T12:29:47Z
- Age days: 0

</details>
