---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15539v1"
published: "2026-08-16T05:25:04Z"
age_days: 1
score: 31
created: 2026-08-18
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# CrossView: Can Vision-Language Models Reason Across Cameras?

> [!summary] 一句话结论（基于摘要）
> Evaluation of proprietary models, such as GPT-5.2, and open-source models, like Qwen3-VL, reveals consistently low accuracy, with open-source models trailing by a wide margin.

## 关键点

- **问题**：We argue that this is not simply "more" of the single-camera problem; it is fundamentally different.
- **创新点 / 方法**：We introduce CrossView, a multi-camera video question-answering benchmark spanning autonomous driving, security surveillance, egocentric/exocentric video, and robotics.
- **证据**：Evaluation of proprietary models, such as GPT-5.2, and open-source models, like Qwen3-VL, reveals consistently low accuracy, with open-source models trailing by a wide margin.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/CrossView Can Vision-Language Models Reason Across Cameras.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video understanding benchmarks have long centered on single-camera settings, where modern multi-modal language models achieve strong performance across image and video tasks. Yet, the real world runs on multi-camera networks: autonomous vehicles, security systems, and robots all gather data across many simultaneous views. We argue that this is not simply "more" of the single-camera problem; it is fundamentally different. Multi-camera reasoning requires handling context that scales with the number of views, resolving occlusions visible from only a subset of cameras, judging which views matter, and integrating evidence across perspectives that may overlap or diverge. Current models struggle with exactly these challenges, yet no benchmark systematically targets them. We introduce CrossView, a multi-camera video question-answering benchmark spanning autonomous driving, security surveillance, egocentric/exocentric video, and robotics. Evaluation of proprietary models, such as GPT-5.2, and open-source models, like Qwen3-VL, reveals consistently low accuracy, with open-source models trailing by a wide margin. Performance scales strongly with a model's ability to jointly process multiple viewpoints, positioning CrossView as a rigorous benchmark for multi-camera video. We open-source our code and dataset at https://utaustin-swarmlab.github.io/CrossView.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15539v1
- Authors: Sahil Shah, S P Sharan, Harsh Goel, Manvik Pasula, Adithya Hebbalae, Minkyu Choi, Sandeep P. Chinchali
- Published: 2026-08-16T05:25:04Z
- Age days: 1

</details>
