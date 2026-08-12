---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15163v1"
published: "2026-07-16T16:08:27Z"
age_days: 1
score: 34
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# Scaling Behavior Foundation Model for Humanoid Robots

> [!summary] 一句话结论（基于摘要）
> Through extensive experiments in both simulation and real-world deployment, we demonstrate that our approach yields significant improvements in control fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on the test set by over…

## 关键点

- **问题**：Behavior Foundation Models (BFMs) have recently emerged as a promising solution to address these challenges by leveraging large-scale behavioral data to achieve superior expressiveness, versatility and generalization.
- **创新点 / 方法**：Through extensive experiments in both simulation and real-world deployment, we demonstrate that our approach yields significant improvements in control fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on the test set by over 10% in local mode and 82% in global mode compared with exis…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/Scaling Behavior Foundation Model for Humanoid Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid control requires natural whole-body coordination, precise real-time responses
to control signals, and robust generalization across diverse environmental contexts,
making it a cornerstone for generalist embodied agents. Behavior Foundation Models
(BFMs) have recently emerged as a promising solution to address these challenges by
leveraging large-scale behavioral data to achieve superior expressiveness, versatility
and generalization. However, despite growing interest in scaling BFMs to further improve
their capabilities, it remains unclear how key factors, including the learning paradigm,
behavioral data and model architecture should be coordinated to enable effective
scaling. In this work, we revisit the scaling recipe for BFMs and demonstrate that
substantial performance gains can be achieved through the coordination of three core
components: 1) the learning paradigm of motion tracking that reformulates diverse
humanoid control problems as the reproduction of integrated whole-body behaviors in the
global frame; 2) the strategic synergy between on-policy rollout quantity and reference
motion diversity; and 3) the expressive and scalable model architecture termed Humanoid
Transformer that facilitates the natural emergence of structured behavioral
representations. Through extensive experiments in both simulation and real-world
deployment, we demonstrate that our approach yields significant improvements in control
fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on
the test set by over 10% in local mode and 82% in global mode compared with existing
humanoid controllers. These results establish BFM as a principled and effective
foundation for scalable and general-purpose humanoid control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15163v1
- Authors: Weishuai Zeng, Kangning Yin, Xiaojie Niu, Shunlin Lu, Weixiang Zhong, Jiahe Chen, Feiyu Jia, Xiao Chen, Zirui Wang, Furui Xu, Ming Zhou, Kailin Li, Weinan Zhang, He Wang, Li Yi, Dahua Lin, Jiangmiao Pang, Jingbo Wang
- Published: 2026-07-16T16:08:27Z
- Age days: 1

</details>
