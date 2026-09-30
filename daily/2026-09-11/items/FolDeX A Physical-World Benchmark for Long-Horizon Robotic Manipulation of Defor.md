---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10243v1"
published: "2026-09-09T14:33:44Z"
age_days: 1
score: 39
created: 2026-09-11
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects

> [!summary] 先说人话（基于摘要）
> We introduce FolDeX, a physical-world benchmark built entirely from real-robot data, with garment folding as its primary task.

## 这篇到底在做什么

- **卡在哪里**：Existing real-robot benchmarks mainly focus on short-horizon rigid-object tasks and offer limited coverage of long-horizon deformable manipulation.
- **关键解法**：We introduce FolDeX, a physical-world benchmark built entirely from real-robot data, with garment folding as its primary task.
- **拿什么证明**：摘要未报告明确实验结论；需阅读全文核查。

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/FolDeX A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Defor.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world. Yet methods that perform well in simulation can degrade substantially on real robots, especially in long-horizon deformable-object manipulation, where policies must track changing states and execute reliable multi-stage bimanual interactions. Existing real-robot benchmarks mainly focus on short-horizon rigid-object tasks and offer limited coverage of long-horizon deformable manipulation. We introduce FolDeX, a physical-world benchmark built entirely from real-robot data, with garment folding as its primary task. Since real-robot data collection is costly, FolDeX studies how heterogeneous physical experience can be reused efficiently. The benchmark is organized around four research axes: leveraging human intervention and recovery data collected during deployment; transferring data across tasks, including across garment categories and from rigid to deformable-object manipulation; reusing data across scenes with changes in lighting, background, and layout; and transferring data across robotic embodiments. FolDeX provides 2,000+ hours of real-robot data spanning 20+ tasks and 10+ embodiments. We also establish a fair real-robot evaluation platform for externally submitted policies, with standardized tasks, held-out physical objects, controlled initializations, and a unified execution protocol. The platform is publicly accessible at https://ai.midea.com/#/fold-challenge. We hope FolDeX will serve as a unified testbed for heterogeneous real-robot data reuse and reliable long-horizon deformable manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10243v1
- Authors: Chenhuan Liu, Yi Xu, Feng Wu, Hanyang Wang, Wenxiao Kuai, Weihao Ding, Shan Wang, Yang Liu, Shuyong Gao, Wenqiang Zhang
- Published: 2026-09-09T14:33:44Z
- Age days: 1

</details>
