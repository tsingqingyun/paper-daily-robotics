---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15058v1"
published: "2026-07-16T14:32:34Z"
age_days: 1
score: 32
created: 2026-07-18
concepts: ["多模态基础模型", "Sim2Real", "具身智能评测与基准"]
---

# SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment

> [!summary] 一句话结论（基于摘要）
> On ScanNet25k, SUFLECA achieves 33.4%/42.3% category/instance accuracy, outperforming, with a smaller computational footprint, the strongest zero-shot baseline by 10.3/12.2 percentage points and, for the first time on this benchmark, even surpassing fully sup…

## 关键点

- **问题**：CAD-to-image alignment aims to estimate an object's 9D pose (rotation, translation, and anisotropic scale) from a single RGB image, enabling applications in robotics and augmented reality.
- **创新点 / 方法**：To address these limitations, we introduce SUFLECA (Scaling Up Feature LEarning for CAD Alignment), a weakly-supervised framework for zero-shot CAD alignment with two key contributions.
- **证据**：On ScanNet25k, SUFLECA achieves 33.4%/42.3% category/instance accuracy, outperforming, with a smaller computational footprint, the strongest zero-shot baseline by 10.3/12.2 percentage points and, for the first time on this benchmark, even surpassing fully supervised methods.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/SUFLECA Scaling Up Feature Learning for CAD-to-image Alignment.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

CAD-to-image alignment aims to estimate an object's 9D pose (rotation, translation, and
anisotropic scale) from a single RGB image, enabling applications in robotics and
augmented reality. Recent zero-shot methods use visual foundation models to match image
regions to CAD models, yet typically their correspondences are appearance-driven and
degrade under occlusion or sim-to-real domain shift. To address these limitations, we
introduce SUFLECA (Scaling Up Feature LEarning for CAD Alignment), a weakly-supervised
framework for zero-shot CAD alignment with two key contributions. First, SUFLECA scales
up geometry-grounded feature learning from pretrained visual representations through
Normalized Object Coordinates (NOCs) supervision on 674K images spanning 12 real and
synthetic datasets, learning compact geometry-aware features that generalize across
domains. Second, we propose a geometrically consistent matching algorithm that
establishes reliable one-to-one CAD-to-image correspondences. Together, these
contributions enable accurate, sub-second alignment per object instance without
iterative pose refinement. On ScanNet25k, SUFLECA achieves 33.4%/42.3% category/instance
accuracy, outperforming, with a smaller computational footprint, the strongest zero-shot
baseline by 10.3/12.2 percentage points and, for the first time on this benchmark, even
surpassing fully supervised methods. Code is available at: https://github.com/snt-
arg/SUFLECA

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15058v1
- Authors: Saad Ejaz, Miguel Fernandez-Cortizas, Javier Civera, Holger Voos, Jose Luis Sanchez-Lopez
- Published: 2026-07-16T14:32:34Z
- Age days: 1

</details>
