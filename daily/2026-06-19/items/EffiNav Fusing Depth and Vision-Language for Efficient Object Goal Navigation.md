---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18634v1"
published: "2026-06-17T03:04:11Z"
age_days: 1
score: 33
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# EffiNav: Fusing Depth and Vision-Language for Efficient Object Goal Navigation

> [!summary] 一句话结论（基于摘要）
> Across two standard metrics--Success Rate (SR) and Success weighted by Path Length (SPL), EffiNav matches or outperforms recent baselines, reflecting its efficiency, robustness, and practical applicability.

## 关键点

- **问题**：In ObjNav, successful arrival at the target object provides a basic measure of performance; however, the efficiency of the navigation trajectory is equally important, as it indicates how intelligently the agent explores and how much time remains for subsequent tasks.
- **创新点 / 方法**：To locate a target object while exploring the unknown environment is a fundamental capability for autonomous agents, with applications ranging from search-and-rescue to field robots.
- **证据**：Across two standard metrics--Success Rate (SR) and Success weighted by Path Length (SPL), EffiNav matches or outperforms recent baselines, reflecting its efficiency, robustness, and practical applicability.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-19/EffiNav Fusing Depth and Vision-Language for Efficient Object Goal Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

To locate a target object while exploring the unknown environment is a fundamental
capability for autonomous agents, with applications ranging from search-and-rescue to
field robots. A simplified version of such task is Object Goal Navigation (ObjNav). In
ObjNav, successful arrival at the target object provides a basic measure of performance;
however, the efficiency of the navigation trajectory is equally important, as it
indicates how intelligently the agent explores and how much time remains for subsequent
tasks. In unknown environments, the key to efficient navigation lies in deciding where
to explore next. While many prior works aim to address this core challenge and achieved
promising performance in certain settings, recent training-based models and non-training
frameworks still suffer from generalization and efficiency issues respectively, which in
the worst cases can lead to excessive exploration of already-visited areas or redundant
back-and-forth motion. We evaluate EffiNav on two widely used simulation benchmarks
Habitat Matterport 3D (HM3D) and Open-Vocabulary Object goal Navigation (OVON), and
further validate its effectiveness on physical robots in real-world settings. We conduct
failure analysis on massive simulation episodes. With minimal modification, we also
extend EffiNav to a memory-augmented ObjNav task on the GOAT-BENCH dataset,
demonstrating its adaptability beyond standard ObjNav settings. Across two standard
metrics--Success Rate (SR) and Success weighted by Path Length (SPL), EffiNav matches or
outperforms recent baselines, reflecting its efficiency, robustness, and practical
applicability. Recognizing the different emphases of the two datasets, the performances
reveals this framework is more balanced and generalizable for efficient ObjNav.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18634v1
- Authors: Zecheng Yin, Benedict Jun Ma
- Published: 2026-06-17T03:04:11Z
- Age days: 1

</details>
