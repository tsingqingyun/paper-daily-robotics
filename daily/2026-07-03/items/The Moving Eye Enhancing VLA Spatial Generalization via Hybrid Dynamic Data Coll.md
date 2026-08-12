---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02322v1"
published: "2026-07-02T15:30:26Z"
age_days: 0
score: 32
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection

> [!summary] 一句话结论（基于摘要）
> In this work, we propose a data-centric solution to enhance VLA spatial generalization.

## 关键点

- **问题**：However, their spatial generalization remains fragile.
- **创新点 / 方法**：In this work, we propose a data-centric solution to enhance VLA spatial generalization.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/The Moving Eye Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Coll.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have shown remarkable promise in generalized robotic
manipulation. However, their spatial generalization remains fragile. We argue that
simply increasing the number of viewpoints is insufficient. Models often fall into the
trap of Shortcut Learning, latching onto spurious correlations (e.g., fixed relative
poses between objects or between the camera and robot base) rather than learning true
spatial relationships. In this work, we propose a data-centric solution to enhance VLA
spatial generalization. We utilize a dual-arm setup where one arm performs manipulation
while the other serves as a mobile environmental camera. We systematically evaluate
three data distribution patterns: Fixed, Multi-Fixed, and Moving Views. Our findings
reveal that a hybrid strategy, combining continuous camera motion with diverse static
viewpoints, yields the best performance by substantially reducing spurious correlations
while maintaining training stability. Our experiments demonstrate that this strategy
mitigates spurious correlations, enabling VLAs to generalize to unseen camera poses and
object configurations where simply adding more static viewpoints fails. Crucially, we
reveal that the susceptibility to shortcut learning and the struggle with spatial
generalization are universal characteristics shared across diverse architectures.
Consequently, all evaluated models (ACT, Diffusion, and VLA models including Pi0 and
Gr00t) benefit significantly from our mixed data strategy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02322v1
- Authors: Jincheng Tang, Yilong Zhu, Zhengyuan Xie, Jiang-Jiang Liu, Jiaxing Zhang
- Published: 2026-07-02T15:30:26Z
- Age days: 0

</details>
