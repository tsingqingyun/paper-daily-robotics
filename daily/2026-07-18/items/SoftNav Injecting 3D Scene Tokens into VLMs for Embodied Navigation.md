---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14586v1"
published: "2026-07-16T05:32:52Z"
age_days: 1
score: 29
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent"]
---

# SoftNav: Injecting 3D Scene Tokens into VLMs for Embodied Navigation

> [!summary] 一句话结论（基于摘要）
> Current approaches transmit 3D scene information to vision-language models (VLMs) through text, suggesting a representation gap in our tested configurations; a controlled ablation confirms that direct embedding-level transfer significantly outperforms the eva…

## 关键点

- **问题**：In goal-directed embodied navigation, where an agent must locate a specified target in an unseen environment, 3D scene understanding and navigation reasoning must work in concert.
- **创新点 / 方法**：We introduce SoftNav, which injects entity-level 3D continuous representations -- one token per detected object or frontier -- into a VLM's hidden space as soft tokens through a lightweight projector.
- **证据**：Current approaches transmit 3D scene information to vision-language models (VLMs) through text, suggesting a representation gap in our tested configurations; a controlled ablation confirms that direct embedding-level transfer significantly outperforms the evaluated text serialization formats.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/SoftNav Injecting 3D Scene Tokens into VLMs for Embodied Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In goal-directed embodied navigation, where an agent must locate a specified target in
an unseen environment, 3D scene understanding and navigation reasoning must work in
concert. Current approaches transmit 3D scene information to vision-language models
(VLMs) through text, suggesting a representation gap in our tested configurations; a
controlled ablation confirms that direct embedding-level transfer significantly
outperforms the evaluated text serialization formats. We introduce SoftNav, which
injects entity-level 3D continuous representations -- one token per detected object or
frontier -- into a VLM's hidden space as soft tokens through a lightweight projector.
With the 3D encoder and VLM frozen, only ~1,200 samples and ~17M trainable parameters
are needed. On HM3D-OVON, SoftNav achieves 74.2%/68.3%/66.7% SR across three splits,
surpassing all prior methods in both SR and SPL; the same navigation policy transfers
zero-shot to GOAT-Bench (67.2% SR), SG3D (47.2% s-SR), and real-world robot deployment
without retraining or architectural modification. Injecting 3D scene tokens directly
into VLMs bridges the representation gap, enabling transferable navigation with minimal
training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14586v1
- Authors: Yi Wu, Junjie An, Xiao Liu, Yiqun Zhou, Yuechen Wu, Xiaoqing Guan, Shuyang Yu, You Wang, Guang Li
- Published: 2026-07-16T05:32:52Z
- Age days: 1

</details>
