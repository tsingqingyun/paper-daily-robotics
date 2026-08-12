---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18262v1"
published: "2026-05-18T11:59:52Z"
age_days: 1
score: 31
created: 2026-05-20
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# On Improving Multimodal Pedestrian Trajectory Prediction with CVAE: A Study on Benchmark and Robot Data

> [!summary] 一句话结论（基于摘要）
> Results show moderate gains on public benchmarks, but more consistent endpoint accuracy and improved trajectory diversity across different crowd configurations.

## 关键点

- **问题**：Social Spatio-Temporal Graph Convolutional Neural Networks (Social- STGCNN) have shown strong performance by modeling social interactions; however, producing diverse and well-calibrated future trajectories remains challenging.
- **创新点 / 方法**：In this work, we build on a Social-STGCNN backbone and introduce a Conditional Variational Autoencoder (CVAE)-based probabilistic formulation to explicitly model multimodal future trajectories.
- **证据**：Results show moderate gains on public benchmarks, but more consistent endpoint accuracy and improved trajectory diversity across different crowd configurations.
- **局限**：Social Spatio-Temporal Graph Convolutional Neural Networks (Social- STGCNN) have shown strong performance by modeling social interactions; however, producing diverse and well-calibrated future trajectories remains challenging.

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Accurate pedestrian trajectory prediction is crucial for autonomous systems operating in
complex environments, such as modular buses and delivery robots in suburban or semi-
structured areas. Social Spatio-Temporal Graph Convolutional Neural Networks (Social-
STGCNN) have shown strong performance by modeling social interactions; however,
producing diverse and well-calibrated future trajectories remains challenging. In this
work, we build on a Social-STGCNN backbone and introduce a Conditional Variational
Autoencoder (CVAE)-based probabilistic formulation to explicitly model multimodal future
trajectories. We evaluate the method on the ETH and UCY pedestrian trajectory datasets
as well as on a real-world pedestrian dataset collected by a mobile robot. Results show
moderate gains on public benchmarks, but more consistent endpoint accuracy and improved
trajectory diversity across different crowd configurations. Evaluation on robot-
collected data further demonstrates the approach's effectiveness beyond curated
benchmarks and supports its applicability in practical deployments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18262v1
- Authors: Yuzhou Liu, Cristina Olaverri-Monreal
- Published: 2026-05-18T11:59:52Z
- Age days: 1

</details>
