---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23634v1"
published: "2026-06-22T17:23:57Z"
age_days: 1
score: 32
created: 2026-06-24
concepts: ["世界模型", "具身智能评测与基准"]
---

# Pose Anything Anywhere:Model-free Object Poses from Arbitrary References

> [!summary] 一句话结论（基于摘要）
> Extensive experiments show that PANY achieves state-of-the-art performance across multiple benchmarks, substantially outperforming existing model-free methods, improving pose accuracy by +12% on YCB-V and over +20% on LM-O.

## 关键点

- **问题**：Estimating the 6D pose of unseen objects is a fundamental yet challenging problem for open-world robotics and embodied perception.
- **创新点 / 方法**：Therefore, we present PANY, a unified model- free framework that seamlessly supports both RGB and RGB-D inputs, operates on one or sparse pose-free reference views, and generalizes effectively to novel objects.
- **证据**：Extensive experiments show that PANY achieves state-of-the-art performance across multiple benchmarks, substantially outperforming existing model-free methods, improving pose accuracy by +12% on YCB-V and over +20% on LM-O.
- **局限**：Model-based methods are accurate but depend on CAD assets or heavy onboarding, while most model-free approaches are still limited to pairwise single-anchor matching and thus fail under occlusion and large viewpoint changes with low query-reference overlap.

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/Pose Anything Anywhere Model-free Object Poses from Arbitrary References.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Estimating the 6D pose of unseen objects is a fundamental yet challenging problem for
open-world robotics and embodied perception. Model-based methods are accurate but depend
on CAD assets or heavy onboarding, while most model-free approaches are still limited to
pairwise single-anchor matching and thus fail under occlusion and large viewpoint
changes with low query-reference overlap. Therefore, we present PANY, a unified model-
free framework that seamlessly supports both RGB and RGB-D inputs, operates on one or
sparse pose-free reference views, and generalizes effectively to novel objects. Built on
a multi-view transformer geometry backbone, PANY moves beyond pairwise matching by
learning view-consistent geometry and cross-view alignment cues that remain stable under
wide baselines and limited overlap. When additional unposed assist views are available,
PANY aggregates them via pose-graph canonical registration to increase geometric
coverage and reinforce the final pose. Extensive experiments show that PANY achieves
state-of-the-art performance across multiple benchmarks, substantially outperforming
existing model-free methods, improving pose accuracy by +12% on YCB-V and over +20% on
LM-O. Furthermore, PANY consistently performs well under both single-reference and
sparse-reference settings, demonstrating strong robustness in real-world environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23634v1
- Authors: Hongli Xu, Jiaqi Hu, Junwen Huang, Boyang Zhong, Peter KT Yu, Nassir Navab, Benjamin Busam, Slobodan Ilic
- Published: 2026-06-22T17:23:57Z
- Age days: 1

</details>
