---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13461v1"
published: "2026-07-15T05:46:34Z"
age_days: 1
score: 32
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Joint On-and-Off Policy Learning for Vision-and-Language Navigation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate the efficacy of JOP-VLN, achieving success rates of 69.9% and 68.0% on the VLN-CE R2R and RxR benchmarks, respectively, setting a new state-of-the-art on R2R.

## 关键点

- **问题**：Vision-and-Language Navigation (VLN) necessitates an embodied agent to navigate in the physical world by adhering to natural language instructions.
- **创新点 / 方法**：Recent advancements in Vision-Language Models (VLM) have propelled the development of VLM-based VLN methods with two predominant paradigms: (1) imitation learning (IL) on expert demonstrations, followed by the Dataset Aggregation (DAgger) algorithm to bolster error recovery capabilities; (2) reinforcement learning (RL…
- **证据**：Extensive experiments demonstrate the efficacy of JOP-VLN, achieving success rates of 69.9% and 68.0% on the VLN-CE R2R and RxR benchmarks, respectively, setting a new state-of-the-art on R2R.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/Joint On-and-Off Policy Learning for Vision-and-Language Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-and-Language Navigation (VLN) necessitates an embodied agent to navigate in the
physical world by adhering to natural language instructions. Recent advancements in
Vision-Language Models (VLM) have propelled the development of VLM-based VLN methods
with two predominant paradigms: (1) imitation learning (IL) on expert demonstrations,
followed by the Dataset Aggregation (DAgger) algorithm to bolster error recovery
capabilities; (2) reinforcement learning (RL) driven by verifiable rewards to enhance
reasoning and exploration. A notable gap is the absence of integration between these two
distinct paradigms. This paper introduces JOP-VLN, a novel VLN framework that
synergistically combines off-policy imitation learning and on-policy exploration within
a three-stage training pipeline. Initially, IL is employed on expert demonstrations to
acquire basic navigation skills. Subsequently, the DAgger algorithm is utilized to
generate heuristic exploration trajectories, which are then used for imitation learning
to improve error recovery capabilities. Finally, a joint on-and-off policy learning
framework is implemented, featuring high-entropy trajectory sampling to enhance RL
training efficiency and an error-correction-prioritized trajectory sorting strategy for
effective error correction. Extensive experiments demonstrate the efficacy of JOP-VLN,
achieving success rates of 69.9% and 68.0% on the VLN-CE R2R and RxR benchmarks,
respectively, setting a new state-of-the-art on R2R. Project page:
https://qingrongh.github.io/JOP-VLN.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13461v1
- Authors: Qingrong He, Lin Zhao, Kevin Zheng, Liang Lin
- Published: 2026-07-15T05:46:34Z
- Age days: 1

</details>
