---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08814v1"
published: "2026-08-09T17:03:15Z"
age_days: 2
score: 27
created: 2026-08-12
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# 360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents

> [!summary] 一句话结论（基于摘要）
> We present 360CityArena, a benchmark for evaluating the urban exploration capabilities of embodied agents within a photorealistic environment constructed from 360-degree videos.

## 关键点

- **问题**：Existing outdoor benchmarks either lack sufficient photorealism or complexity, resulting in a considerable gap from real-world urban environments.
- **创新点 / 方法**：We present 360CityArena, a benchmark for evaluating the urban exploration capabilities of embodied agents within a photorealistic environment constructed from 360-degree videos.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/360CityArena A Realistic Virtual Urban Navigation Benchmark for Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present 360CityArena, a benchmark for evaluating the urban exploration capabilities
of embodied agents within a photorealistic environment constructed from 360-degree
videos. Existing outdoor benchmarks either lack sufficient photorealism or complexity,
resulting in a considerable gap from real-world urban environments. 360CityArena is
built on a realistic reconstruction of the Akihabara district in Tokyo, Japan, using 602
360-degree video segments covering 85 streets, and consists of 175 meticulously human-
crafted tasks. It encompasses three task categories: Environment Understanding, Path
Reasoning, and Spatial Reasoning, covering fundamental abilities required for urban
exploration, such as localization, landmark search, path planning, and relational
spatial reasoning, thereby enabling comprehensive evaluation in realistic urban scenes.
Our evaluation using state-of-the-art LMM-based agents shows that even the strongest
model, Gemini 2.5 Flash, performs far below human level (human: 77.3% vs. Gemini 2.5
Flash: 17.1%), revealing substantial challenges that remain in city-scale embodied
navigation and reasoning. 360CityArena provides a necessary and challenging testbed for
photorealistic urban-district navigation and spatial reasoning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08814v1
- Authors: Kenta Watanabe, Atsuyuki Miyai, Mizuki Takenawa, Kiyoharu Aizawa, Toshihiko Yamasaki
- Published: 2026-08-09T17:03:15Z
- Age days: 2

</details>
