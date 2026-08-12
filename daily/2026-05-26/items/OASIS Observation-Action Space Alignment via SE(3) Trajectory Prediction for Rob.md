---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25829v1"
published: "2026-05-25T13:28:33Z"
age_days: 0
score: 36
created: 2026-05-26
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Across simulation and real-world experiments, OASIS outperforms VLA and WAM baselines in success rate and out-of-distribution generalization.

## 关键点

- **问题**：However, these representations largely remain within the observation space and do not share the rigid-body geometry of the action space, forcing the action decoder to implicitly recover this geometry.
- **创新点 / 方法**：We propose OASIS, a visuomotor policy that aligns the intermediate representation with the action space via $SE(3)$ end-effector trajectory prediction.
- **证据**：Across simulation and real-world experiments, OASIS outperforms VLA and WAM baselines in success rate and out-of-distribution generalization.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/OASIS Observation-Action Space Alignment via SE(3) Trajectory Prediction for Rob.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent vision-language-action (VLA) models and world action models (WAMs) advance
robotic manipulation by enriching intermediate representations with auxiliary spatial
features or future visual-state prediction. However, these representations largely
remain within the observation space and do not share the rigid-body geometry of the
action space, forcing the action decoder to implicitly recover this geometry. We propose
OASIS, a visuomotor policy that aligns the intermediate representation with the action
space via $SE(3)$ end-effector trajectory prediction. OASIS couples a 3D-aware feature
encoder that fuses vision-language and metric-depth features with an $SE(3)$ trajectory
predictor that produces a camera-frame end-effector trajectory. Conditioned on the
predictor's pose-supervised hidden states, the action decoder generates action chunks
consistent with rigid-body motion. Across simulation and real-world experiments, OASIS
outperforms VLA and WAM baselines in success rate and out-of-distribution
generalization. Our project page is available at
https://npuhandsome.github.io/OASIS_web.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25829v1
- Authors: Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li, Xingyu Chen, Zeyang Liu, Xuguang Lan
- Published: 2026-05-25T13:28:33Z
- Age days: 0

</details>
