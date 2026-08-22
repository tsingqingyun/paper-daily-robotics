---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18498v1"
published: "2026-08-19T03:44:28Z"
age_days: 3
score: 24
created: 2026-08-22
concepts: ["世界模型", "视觉语言动作模型 VLA"]
---

# DyG$^2$T: Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Graph Transformer

> [!summary] 一句话结论（基于摘要）
> Experiments on both synthetic and real-world datasets demonstrate that DyG$^2$T achieves accurate dynamics modeling and reasoning, and exhibits strong cross-object and real-world generalization.

## 关键点

- **问题**：Modeling object dynamics from limited visual observations is a fundamental problem for enabling accurate motion trajectory prediction in embodied interaction scenarios.
- **创新点 / 方法**：To tackle these issues, we propose DyG$^2$T, a dynamics modeling framework that infers object motion trajectories by spatially completing and temporally discriminating Key Point representations and modeling multi-scale interaction over particle graphs.
- **证据**：Experiments on both synthetic and real-world datasets demonstrate that DyG$^2$T achieves accurate dynamics modeling and reasoning, and exhibits strong cross-object and real-world generalization.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/DyG$ 2$T Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Gra.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Modeling object dynamics from limited visual observations is a fundamental problem for enabling accurate motion trajectory prediction in embodied interaction scenarios. Existing dynamics modeling methods first compress reconstructed particle representations into sparse Key Points and model their evolution using locally constrained interactions, thereby discarding fine-grained local details and obscuring discriminative interaction modeling across spatial and temporal scales, leading to drifting trajectories and inaccurate appearance prediction. To tackle these issues, we propose DyG$^2$T, a dynamics modeling framework that infers object motion trajectories by spatially completing and temporally discriminating Key Point representations and modeling multi-scale interaction over particle graphs. Spatially, DyG$^2$T enriches each Key Point by aggregating neighboring raw particle positions to recover fine-grained local details, while explicitly encoding relative offsets among Key Points to enhance geometric structure perception. Temporally, we introduce a Temporal Disentangling Network (TDN) to identify dominant cross-frame variations in latent space and amplify inter-frame differences, yielding temporally discriminative representations that are subsequently aggregated via Temporal Attention to capture frame-wise temporal evolution cues. For comprehensive interaction modeling, a Particle Graph Transformer leverages global attention to preserve discriminative long-range dependencies among Key Points, mitigating representation homogenization induced by locality-constrained modeling and providing a robust basis for accurate trajectory prediction. Experiments on both synthetic and real-world datasets demonstrate that DyG$^2$T achieves accurate dynamics modeling and reasoning, and exhibits strong cross-object and real-world generalization.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18498v1
- Authors: Yansong Wang, Zhaobo Qi, Xinyan Liu, Beichen Zhang, Shuhui Wang, Weigang Zhang, Qingming Huang
- Published: 2026-08-19T03:44:28Z
- Age days: 3

</details>
