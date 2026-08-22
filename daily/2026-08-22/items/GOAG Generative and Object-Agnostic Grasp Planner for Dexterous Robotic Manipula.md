---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19759v1"
published: "2026-08-20T08:03:39Z"
age_days: 2
score: 29
created: 2026-08-22
concepts: ["具身智能评测与基准"]
---

# GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Our method delivers state-of-the-art results on the objects from the MultiDex dataset, achieving an average success rate of 86.93%.

## 关键点

- **问题**：Multifingered grasping is a crucial robotic skill, but current deep-learning grasp planners often struggle to generalize to new objects because they are trained on limited, object-specific datasets.
- **创新点 / 方法**：We introduce a fundamentally different approach, grounded in the observation that the gripper and the object share identical surface geometry at their mutual contact points.
- **证据**：Our method delivers state-of-the-art results on the objects from the MultiDex dataset, achieving an average success rate of 86.93%.
- **局限**：Unlike these methods, our approach does not rely on object-specific training data, highlighting the advantages of object-agnostic learning.

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/GOAG Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipula.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multifingered grasping is a crucial robotic skill, but current deep-learning grasp planners often struggle to generalize to new objects because they are trained on limited, object-specific datasets. We introduce a fundamentally different approach, grounded in the observation that the gripper and the object share identical surface geometry at their mutual contact points. We propose GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation, a novel deep generative model that learns a compact latent representation of a specific gripper's contact surface distribution, enabling the efficient sampling of valid grasp configurations without relying on object-specific training data. We show that by introducing object features only at inference time, our model can effectively retrieve admissible contact areas that are compatible with the gripper's capabilities. We validate our approach through extensive experiments on established grasp protocols in both simulated and real-world scenarios, demonstrating its effectiveness with different grippers from the literature. Our method delivers state-of-the-art results on the objects from the MultiDex dataset, achieving an average success rate of 86.93%. It offers significantly faster processing when generating numerous grasps, while matching the performance of leading approaches specifically trained on this dataset. Unlike these methods, our approach does not rely on object-specific training data, highlighting the advantages of object-agnostic learning. It effectively addresses the generalization challenges faced by traditional data-driven grasp planners. Code and videos are available on our project website https://cea-list.github.io/goagweb/ .

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19759v1
- Authors: Julien Merand, Boris Meden, Mathieu Grossard, Liming Chen
- Published: 2026-08-20T08:03:39Z
- Age days: 2

</details>
