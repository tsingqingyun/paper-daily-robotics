---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29247v1"
published: "2026-06-28T07:29:25Z"
age_days: 2
score: 40
created: 2026-06-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SurgVLA-Bench: Towards Evaluating Vision-Language-Action Models for Laparoscopic Surgical Robotics

> [!summary] 一句话结论（基于摘要）
> Leveraging the SurRoL simulation platform, we construct a hierarchical task taxonomy ranging from atomic actions to complete surgical procedures, complemented by a multi- dimensional evaluation framework assessing action accuracy and semantic consistency.

## 关键点

- **问题**：Despite the prevalence of VLA benchmarks for general robotics, standardized evaluation platforms specifically designed for surgical contexts remain absent.
- **创新点 / 方法**：To address this limitation, we present SurgVLA-Bench, the first comprehensive benchmark for evaluating VLA models in laparoscopic surgical robotics.
- **证据**：Leveraging the SurRoL simulation platform, we construct a hierarchical task taxonomy ranging from atomic actions to complete surgical procedures, complemented by a multi- dimensional evaluation framework assessing action accuracy and semantic consistency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/SurgVLA-Bench Towards Evaluating Vision-Language-Action Models for Laparoscopic.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models represent a promising direction for embodied
intelligence in surgical robotics. Despite the prevalence of VLA benchmarks for general
robotics, standardized evaluation platforms specifically designed for surgical contexts
remain absent. To address this limitation, we present SurgVLA-Bench, the first
comprehensive benchmark for evaluating VLA models in laparoscopic surgical robotics.
Leveraging the SurRoL simulation platform, we construct a hierarchical task taxonomy
ranging from atomic actions to complete surgical procedures, complemented by a multi-
dimensional evaluation framework assessing action accuracy and semantic consistency. We
then systematically evaluate two representative paradigms, including autoregressive
models such as OpenVLA, and flow matching models such as $π_{0}$, $π_{0.5}$, and
SmolVLA. Our experiments show that autoregressive models tend to excel in semantic
understanding, while flow matching models often achieve higher task precision but may
face generalization trade-offs. However, even the best-performing models remain far from
satisfactory, as the constrained endoscopic field of view, restricted viewing angles,
and frequent occlusions persist as fundamental physical bottlenecks. The code and data
are available at https://github.com/VCL-HNU/SurgVLA

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29247v1
- Authors: Jiashuo Sun, Yue He, Wenxuan Liu, Tao Mao, Jiazheng Wang, Xiang Chen, Min Liu
- Published: 2026-06-28T07:29:25Z
- Age days: 2

</details>
