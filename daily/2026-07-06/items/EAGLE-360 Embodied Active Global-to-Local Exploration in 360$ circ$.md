---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02479v1"
published: "2026-07-02T17:47:27Z"
age_days: 3
score: 24
created: 2026-07-06
concepts: ["多模态基础模型"]
---

# EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that EAGLE-360 establishes a new state-of-the-art for 360$^\circ$ visual search, achieving nearly an 8-fold increase in accuracy over the base model while significantly enhancing exploration efficiency.

## 关键点

- **问题**：While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations.
- **创新点 / 方法**：To overcome these challenges, we propose EAGLE-360, a novel Embodied Active Global-to-Local Exploration framework.
- **证据**：Extensive experiments demonstrate that EAGLE-360 establishes a new state-of-the-art for 360$^\circ$ visual search, achieving nearly an 8-fold increase in accuracy over the base model while significantly enhancing exploration efficiency.
- **局限**：While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations.

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-06/EAGLE-360 Embodied Active Global-to-Local Exploration in 360$ circ$.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While Multimodal Large Language Models (MLLMs) have demonstrated exceptional
capabilities in standard visual understanding, adapting them for active visual search in
360$^\circ$ panoramic environments exposes fundamental limitations. Specifically,
standard MLLMs struggle to effectively model inherent panoramic properties, such as
severe polar distortion and continuous cylindrical topologies, which significantly
degrades target detection accuracy. Consequently, existing panoramic search methods
attempt to compensate by relying heavily on fragmented local viewpoints. Burdened by
rigid initialization and a lack of global panoramic priors, these approaches suffer from
myopic, inefficient exploration and struggle with robust error recovery when targets are
out of view. To overcome these challenges, we propose EAGLE-360, a novel Embodied Active
Global-to-Local Exploration framework. Rather than performing exhaustive local searches,
EAGLE-360 leverages global priors to establish an initial holistic perspective,
iteratively reasoning and progressively narrowing the search space. Architecturally, we
adapt RoPE Rolling, a coordinate-shifting positional encoding mechanism, to seamlessly
model the continuous topologies of panoramas. To facilitate this paradigm, we construct
the large-scale EAGLE-360 dataset, comprising 14,000+ 4K panoramas and 70,000+ rounds of
high-quality VQA dialogues. By employing a training pipeline that integrates Supervised
Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO), we effectively elicit
complex spatial reasoning and tool-calling capabilities. Extensive experiments
demonstrate that EAGLE-360 establishes a new state-of-the-art for 360$^\circ$ visual
search, achieving nearly an 8-fold increase in accuracy over the base model while
significantly enhancing exploration efficiency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02479v1
- Authors: Jingtao Xu, Zizhuo Lin, Jianwen Sun, Yi Yang, Yawei Luo
- Published: 2026-07-02T17:47:27Z
- Age days: 3

</details>
