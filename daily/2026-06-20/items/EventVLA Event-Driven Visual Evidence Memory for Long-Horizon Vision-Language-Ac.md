---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20092v1"
published: "2026-06-18T11:11:37Z"
age_days: 1
score: 38
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies

> [!summary] 一句话结论（基于摘要）
> Extensive evaluations show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks, EventVLA achieves an average success rate improvement of +40% over state-of-the-art memory-augmented VLAs.

## 关键点

- **问题**：Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded or unobservable over time.
- **创新点 / 方法**：To address these limitations, we introduce EventVLA, an end-to-end framework founded on the concept of sparse visual evidence memory that comprises two core components: foundational visual anchors to retain initial and short-term contexts, and a dynamic Keyframe Evidence Memory (KEM) module.
- **证据**：Extensive evaluations show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks, EventVLA achieves an average success rate improvement of +40% over state-of-the-art memory-augmented VLAs.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/EventVLA Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Ac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard
Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded
or unobservable over time. While existing memory-augmented methods utilize historical
context, they either suffer from severe information bottlenecks, incur high latency via
decoupled dual systems, or rely on unselective buffers that accumulate massive visual
redundancies. To address these limitations, we introduce EventVLA, an end-to-end
framework founded on the concept of sparse visual evidence memory that comprises two
core components: foundational visual anchors to retain initial and short-term contexts,
and a dynamic Keyframe Evidence Memory (KEM) module. Specifically, KEM directly predicts
future keyframe probabilities from the VLA's latent embeddings to autonomously capture
and store sparse, task-critical visual events. This foresight-driven mechanism empowers
the policy to dynamically evaluate the future causal utility of current observations,
preserving transient visual evidence before it becomes unobservable. Furthermore, we
propose RoboTwin-MeM, a diagnostic benchmark specifically designed to evaluate non-
Markovian manipulation tasks with interactive visual evidence. Extensive evaluations
show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks,
EventVLA achieves an average success rate improvement of +40% over state-of-the-art
memory-augmented VLAs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20092v1
- Authors: Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong, Tianxing Chen, Jiaqi Peng, Jing Xiong, Jiafei Cao, Jifeng Dai, Wengang Zhou, Yao Mu, Tai Wang
- Published: 2026-06-18T11:11:37Z
- Age days: 1

</details>
