---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23090v2"
published: "2026-06-22T09:36:30Z"
age_days: 2
score: 36
created: 2026-06-25
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation

> [!summary] 一句话结论（基于摘要）
> Across standard benchmarks, our method outperforms representative baseline methods on standard metrics, while achieving approximately 33$\times$ faster generation.

## 关键点

- **问题**：Cross-embodiment data have become central to training robotic foundation models.
- **创新点 / 方法**：We propose Flow as Flow, a framework that models robot flows as probability flows based on a flow matching formulation.
- **证据**：Across standard benchmarks, our method outperforms representative baseline methods on standard metrics, while achieving approximately 33$\times$ faster generation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Cross-embodiment data have become central to training robotic foundation models. To
leverage such heterogeneous data, we focus on flow-based object manipulation, where
robot flows (robot velocity fields) serve as embodiment-agnostic motion representations.
Previous studies do not formulate robot flows as dense velocity fields, but as
displacements of sparse keypoints, while such velocity fields better match the
continuous-time nature of motions. We propose Flow as Flow, a framework that models
robot flows as probability flows based on a flow matching formulation. By naturally
modeling such velocity fields within this formulation, our method achieves efficient and
high-quality robot flow generation. Across standard benchmarks, our method outperforms
representative baseline methods on standard metrics, while achieving approximately
33$\times$ faster generation. Furthermore, through real-world experiments evaluating 9
methods with 260 trials per method across 13 manipulation tasks, we show that our method
achieves a higher average success rate than the baseline methods. Our project page is
available at https://flow-as-flow-u0n5y.kinsta.page.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23090v2
- Authors: Koki Seno, Daichi Yashima, Yusuke Takagi, Kento Tokura, Komei Sugiura
- Published: 2026-06-22T09:36:30Z
- Age days: 2

</details>
