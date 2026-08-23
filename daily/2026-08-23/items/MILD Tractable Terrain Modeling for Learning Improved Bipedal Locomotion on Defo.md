---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19955v1"
published: "2026-08-20T12:24:34Z"
age_days: 3
score: 20
created: 2026-08-23
concepts: ["机器人学习"]
---

# MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces

> [!summary] 一句话结论（基于摘要）
> Through hardware experiments, we demonstrate the system's capability for online terrain identification and adaptation across a wide range of surface stiffness.

## 关键点

- **问题**：While bipedal robots hold immense potential, their locomotion on deformable surfaces remains limited as current simulators fail to capture the spatiotemporal heterogeneity of such yielding substrates.
- **创新点 / 方法**：We present MILD, featuring a physics-grounded discrete-element contact solver that accurately simulates spatially varying foot-terrain interactions.
- **证据**：Through hardware experiments, we demonstrate the system's capability for online terrain identification and adaptation across a wide range of surface stiffness.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：20
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/MILD Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Defo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Enabling robots to walk on yielding terrain is vital for applications ranging from disaster response to planetary exploration. While bipedal robots hold immense potential, their locomotion on deformable surfaces remains limited as current simulators fail to capture the spatiotemporal heterogeneity of such yielding substrates. We present MILD, featuring a physics-grounded discrete-element contact solver that accurately simulates spatially varying foot-terrain interactions. Complementing this model, we train a terrain-aware locomotion controller via deep reinforcement learning with latent modulation and proprioceptive estimation. Quantitative comparisons against state-of-the-art methods show our approach generates more diverse and realistic contact scenarios during training, resulting in controllers that exhibit natural adaptation on real deformable surfaces. Through hardware experiments, we demonstrate the system's capability for online terrain identification and adaptation across a wide range of surface stiffness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19955v1
- Authors: Zeren Luo, Jiahui Zhang, Zhe Xu, Wanyue Li, Xinqi Li, Xuechao Chen, Zhangguo Yu, Annan Tang, Peng Lu
- Published: 2026-08-20T12:24:34Z
- Age days: 3

</details>
