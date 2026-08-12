---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24628v1"
published: "2026-06-23T14:24:07Z"
age_days: 1
score: 29
created: 2026-06-25
concepts: ["智能体 Agent", "世界模型"]
---

# ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos

> [!summary] 一句话结论（基于摘要）
> We present ArtiTwinSplat, a framework that automatically constructs articulated, photo-realistic digital twins of objects directly from RGB-D videos, requiring no CAD models, simulation assets, or manual annotations.

## 关键点

- **问题**：Constructing these models at scale remains a critical bottleneck for robotic system integration.
- **创新点 / 方法**：We present ArtiTwinSplat, a framework that automatically constructs articulated, photo-realistic digital twins of objects directly from RGB-D videos, requiring no CAD models, simulation assets, or manual annotations.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/ArtiTwinSplat Interactable Digital Twin Reconstruction via Gaussian Splatting fr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Deploying robots in unstructured real-world environments needs accurate, interactive
models of the objects. Constructing these models at scale remains a critical bottleneck
for robotic system integration. We present ArtiTwinSplat, a framework that automatically
constructs articulated, photo-realistic digital twins of objects directly from RGB-D
videos, requiring no CAD models, simulation assets, or manual annotations. Our method is
built on 3D Gaussian Splatting that preserve geometric fidelity and photometric realism,
coupled with an unsupervised articulation discovery pipeline that recovers part
structure and joint kinematics from observed motion alone. With tracking and
optimization stages our method provides stable, queryable digital twins that support
real-time rendering, viewpoint control, and interactive manipulation. Unlike prior
methods confined to simulation, ArtiTwinSplat operates directly on real-world
observations and produces twins that are immediately usable by downstream robot planning
and learning systems. This method offers a practical, scalable pathway toward digital
twin construction, lowering the integration barrier for articulated object manipulation
in embodied AI and human-robot collaboration contexts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24628v1
- Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum
- Published: 2026-06-23T14:24:07Z
- Age days: 1

</details>
