---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18433v1"
published: "2026-08-19T01:55:04Z"
age_days: 1
score: 51
created: 2026-08-21
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# The Embodiment Gap in Robot Foundation Models

> [!summary] 一句话结论（基于摘要）
> We also propose a reporting framework for adaptation work that success rate alone does not reveal.

## 关键点

- **问题**：In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body.
- **创新点 / 方法**：Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization.
- **证据**：We also propose a reporting framework for adaptation work that success rate alone does not reveal.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：51
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/The Embodiment Gap in Robot Foundation Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs across methods and target robots, and those differences affect practical deployment. We call the gap between reusable models, representations, or data and their use in execution on the target robot the embodiment gap. This survey examines what can be reused across robot embodiments and what must still be implemented on a new robot. We place existing methods on a two-axis map that shows the type of shared structure and the stage at which adaptation is needed for execution on the target robot. We then examine recent work through three overlapping research directions: sharing semantics and perception, sharing robot data and interfaces, and learning correspondence across embodiments. We also propose a reporting framework for adaptation work that success rate alone does not reveal. The framework identifies the work that should be checked when comparing cross-embodiment learning and highlights work that remains on a new robot and questions for future study.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18433v1
- Authors: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Tomohiro Motoda, Koshi Makihara, Masaki Murooka, Takuma Yagi, Yoshiaki Bando, Ryo Hanai
- Published: 2026-08-19T01:55:04Z
- Age days: 1

</details>
