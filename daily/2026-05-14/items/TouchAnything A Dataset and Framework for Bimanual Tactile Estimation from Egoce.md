---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13083v1"
published: "2026-05-13T06:54:36Z"
age_days: 0
score: 32
created: 2026-05-14
concepts: ["世界模型", "具身智能评测与基准"]
---

# TouchAnything: A Dataset and Framework for Bimanual Tactile Estimation from Egocentric Video

> [!summary] 一句话结论（基于摘要）
> Experiments show that incorporating wrist-mounted views generally improves tactile prediction over egocentric- only input, achieving up to 5.0% relative improvement in Contact IoU and 6.1% relative improvement in Volumetric IoU.

## 关键点

- **问题**：However, existing egocentric datasets typically lack tactile sensing, a critical modality that provides direct cues about contact, force, and pressure in human-object interaction.
- **创新点 / 方法**：To enable research in this direction, we introduce EgoTouch, a large-scale multi-view egocentric dataset with dense tactile supervision for bimanual hand-object interaction.
- **证据**：Experiments show that incorporating wrist-mounted views generally improves tactile prediction over egocentric- only input, achieving up to 5.0% relative improvement in Contact IoU and 6.1% relative improvement in Volumetric IoU.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/TouchAnything A Dataset and Framework for Bimanual Tactile Estimation from Egoce.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric human video data, which captures rich human-environment interactions and can
be collected at scale, has become a key driver of embodied intelligence research.
However, existing egocentric datasets typically lack tactile sensing, a critical
modality that provides direct cues about contact, force, and pressure in human-object
interaction. Without such signals, models struggle to learn physically grounded
representations of real-world interaction dynamics. While tactile sensors provide these
cues, deploying high-quality tactile hardware at scale remains expensive and cumbersome.
This raises a central question: can tactile feedback be inferred directly from visual
observations, enabling scalable tactile supervision for egocentric video data and
supporting physically grounded embodied learning? To enable research in this direction,
we introduce EgoTouch, a large-scale multi-view egocentric dataset with dense tactile
supervision for bimanual hand-object interaction. EgoTouch comprises 208 manipulation
tasks spanning 1,891 episodes in diverse indoor and outdoor environments, with
synchronized multi-view RGB (head-mounted egocentric and dual wrist-mounted cameras),
bimanual 3D hand pose, and continuous pressure maps from wearable tactile sensors.
Building on EgoTouch, we introduce TouchAnything, a baseline multi-view vision-to-touch
prediction framework that uses the egocentric view as the primary input and flexibly
leverages available wrist-mounted views at inference time. Experiments show that
incorporating wrist-mounted views generally improves tactile prediction over egocentric-
only input, achieving up to 5.0% relative improvement in Contact IoU and 6.1% relative
improvement in Volumetric IoU. We will publicly release the dataset, code, and
benchmark.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13083v1
- Authors: Jianyi Zhou, Ziteng Gao, Feiyang Hong, Zirui Liu, Guannan Zhang, Weisheng Dai, Ruichen Zhen, Chuqiao Lyu, Haotian Wu, Yinian Mao, Xushi Wang, Yuxiang Jiang, Wenbo Ding, Shuo Yang
- Published: 2026-05-13T06:54:36Z
- Age days: 0

</details>
