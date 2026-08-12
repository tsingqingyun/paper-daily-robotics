---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12499v1"
published: "2026-06-10T13:58:14Z"
age_days: 3
score: 26
created: 2026-06-14
concepts: ["世界模型", "机器人学习"]
---

# Action-Effect Memory Pretraining for Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> AEM consistently improves manipulation performance in both simulation and real-world settings, outperforming baselines across clean scenes, cluttered and random scenes, and non-Markovian tasks.

## 关键点

- **问题**：This design preserves a single-vector temporal bottleneck while keeping inference efficient.
- **创新点 / 方法**：We present AEM, an Action-Effect Memory pretraining framework for robot manipulation that learns compact temporal representations from vision-action history.
- **证据**：AEM consistently improves manipulation performance in both simulation and real-world settings, outperforming baselines across clean scenes, cluttered and random scenes, and non-Markovian tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present AEM, an Action-Effect Memory pretraining framework for robot manipulation
that learns compact temporal representations from vision-action history. Unlike prior
robot representation pretraining methods that mainly focus on single-frame visual
encoding, AEM targets the temporal nature of manipulation, where the current observation
alone is often insufficient under partial observability. AEM models manipulation as an
action-driven interaction process by interleaving visual and action features and
applying masked modeling to recover missing content from incomplete histories, thereby
learning action-conditioned state evolution. The Mamba-encoded output of the final
vision token is used as a compact history representation, serving as the global context
for decoding and downstream control. This design preserves a single-vector temporal
bottleneck while keeping inference efficient. We evaluate AEM with Diffusion Policy and
Flow Policy. AEM consistently improves manipulation performance in both simulation and
real-world settings, outperforming baselines across clean scenes, cluttered and random
scenes, and non-Markovian tasks. Ablation studies further show that history-aware
pretraining surpasses single-frame pretraining and direct frame stacking, while reducing
inference latency and computational cost.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12499v1
- Authors: Yijing Zhou, Qiwei Liang, Sitong Zhuang, Jiaxi Li, Xianpeng Wang, Boyang Cai, Yunyang Mo, Renjing Xu
- Published: 2026-06-10T13:58:14Z
- Age days: 3

</details>
