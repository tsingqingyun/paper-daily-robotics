---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19589v1"
published: "2026-08-20T03:10:31Z"
age_days: 2
score: 32
created: 2026-08-22
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation

> [!summary] 一句话结论（基于摘要）
> To this end, we propose OrthoSkillVLA, a parameter-efficient framework for continual skill learning in pretrained VLA models without demonstration replay.

## 关键点

- **问题**：We analyze the distinct roles of internal VLA components and identify two VLA-specific challenges.
- **创新点 / 方法**：To this end, we propose OrthoSkillVLA, a parameter-efficient framework for continual skill learning in pretrained VLA models without demonstration replay.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/OrthoSkillVLA Continual Skill Learning via Gradient-Informed Skill Subspace Adap.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pretrained Vision-Language-Action models provide a strong foundation for robot learning, but sequentially adapting them to diverse skills can perturb the representations and velocity mappings used by previous skills, leading to catastrophic forgetting. Architecture-based approaches improve retention by isolating skills but lead to increased inference footprint. Recent subspace-constrained methods restrict parameter updates in an orthogonal subspace to minimize interference but impose a unified constraint on the entire model. We analyze the distinct roles of internal VLA components and identify two VLA-specific challenges. First, the VLM maintains broad semantic representations, making it vulnerable to capacity exhaustion, whereas the ActionHead refines semantics into localized velocity patterns that are highly sensitive to perturbations. Second, the final velocity decoder serves as a readout layer. Freezing it forms an output-stage expressivity bottleneck, while updating it risks overwriting previous velocity mappings. To this end, we propose OrthoSkillVLA, a parameter-efficient framework for continual skill learning in pretrained VLA models without demonstration replay. Given the representation heterogeneity, we impose separate subspace constraints on the VLM and ActionHead, preserving reusable semantic capacity while protecting localized velocity patterns. For the output layer, we introduce a lightweight feature-aware MoE decoder, where each skill is allocated a compact expert and a training-free router selects the expert according to feature-space affinity. Extensive simulated and real-world evaluations, together with ablations, demonstrate that OrthoSkillVLA better preserves prior skills while acquiring new ones.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19589v1
- Authors: Jiaqi Wang, Zhou Fang, Qiongfeng Shi, Yi Zhou
- Published: 2026-08-20T03:10:31Z
- Age days: 2

</details>
