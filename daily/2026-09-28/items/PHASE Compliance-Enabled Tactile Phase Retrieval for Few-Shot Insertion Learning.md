---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30889v1"
published: "2026-09-25T06:53:56Z"
age_days: 3
score: 31
created: 2026-09-28
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# PHASE: Compliance-Enabled Tactile Phase Retrieval for Few-Shot Insertion Learning

> [!summary] 先说人话（基于摘要）
> PHASE 根据接触阶段检索示范，让少样本插孔学习能借到正确阶段的经验。柔顺腕部维持接触，产生可用于区分搜索、插入等阶段的触觉和力信号。

## 问题

少量示范难以覆盖插孔中的接触变化。检索增强模仿学习可以补数据，但如何按接触阶段选择相关经验仍不明确，阶段不匹配的示范未必适用于当前交互。

## 创新点或方法

PHASE 将柔顺接触、多模态接触表示学习、基于触觉的变长阶段分割和阶段一致检索结合起来，再用检索数据学习策略。关键区别是以交互信号定义检索单位和匹配条件。

## 证据

在五种插销几何的真机插孔任务上，以共享策略架构比较不同检索方案；相对最强非阶段感知基线，总体成功率提高 13 个百分点，未见初始位置下提高 30 个百分点。

## 局限

方法的核心前提是柔顺腕部能够维持有效接触；需核查示范数量、先验数据来源及阶段分割错误如何影响检索。

- **判断**：做少样本装配或示范检索值得精读，机制与真机结果之间的对应关系比较清楚。

## 研究关联

对机器人学习研究者，它把触觉从策略输入扩展为数据组织与检索依据；共享策略架构的比较有助于评估检索机制本身的价值。

- **概念**：多模态基础模型 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/PHASE Compliance-Enabled Tactile Phase Retrieval for Few-Shot Insertion Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich assembly tasks such as peg-in-hole insertion remain difficult to learn from limited demonstrations. While retrieval-augmented imitation learning, which augments target demonstrations with relevant prior data, offers a promising direction, its applicability to contact-rich manipulation remains largely unexplored. Contact-rich insertion unfolds over multiple phases from search to insert, and retrieving phase-specific experience from prior data in principled ways remains an open question. Our key insight is that a compliant wrist enables the robot to sustain contact throughout execution, producing rich tactile and force signals that naturally reveal the phase structure of insertion and inform what should be retrieved. Based on this insight, we present PHASE (PHase-Aware Segmentation and REtrieval), a framework for compliance-enabled tactile phase retrieval that integrates multimodal contact-aware representation learning, variable-length phase segmentation from tactile signals, and phase-consistent retrieval for policy learning. We evaluate PHASE on real-world peg-in-hole insertion across five peg geometries, comparing against retrieval strategies drawn from state-of-the-art methods under a shared policy architecture. PHASE improves the overall success rate by 13 percentage points over the strongest non-phase-aware baseline, and improves performance under unseen initial positions by 30 percentage points. These results demonstrate that aligning retrieval with interaction-defined contact phases substantially improves robustness in few-shot insertion learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30889v1
- Authors: Jeremy Siburian, Cristian C. Beltran-Hernandez, Tatsuya Matsushima, Yusuke Iwasawa, Masashi Hamaya, Mai Nishimura
- Published: 2026-09-25T06:53:56Z
- Age days: 3

</details>
