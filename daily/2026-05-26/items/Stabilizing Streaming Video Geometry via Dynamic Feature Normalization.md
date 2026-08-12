---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25308v1"
published: "2026-05-25T00:13:15Z"
age_days: 1
score: 27
created: 2026-05-26
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Stabilizing Streaming Video Geometry via Dynamic Feature Normalization

> [!summary] 一句话结论（基于摘要）
> We adapt powerful pretrained monocular geometry models for streaming by finetuning only DyFN, a mere 2\% additional parameters, while keeping the backbone frozen, thereby achieving temporal consistency without compromising single-image accuracy.

## 关键点

- **问题**：Consistent 3D geometry estimation from streaming RGB input is crucial for real-world applications such as autonomous driving, embodied AI, and large-scale reconstruction.
- **创新点 / 方法**：Building on this insight, we introduce Dynamic Feature Normalization (DyFN), a lightweight, causal recurrent module that dynamically and robustly modulates feature statistics to maintain stable geometry over time.
- **证据**：We adapt powerful pretrained monocular geometry models for streaming by finetuning only DyFN, a mere 2\% additional parameters, while keeping the backbone frozen, thereby achieving temporal consistency without compromising single-image accuracy.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/Stabilizing Streaming Video Geometry via Dynamic Feature Normalization.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Consistent 3D geometry estimation from streaming RGB input is crucial for real-world
applications such as autonomous driving, embodied AI, and large-scale reconstruction.
While modern monocular geometry foundation models achieve strong single-image accuracy,
they exhibit severe temporal inconsistency on continuous input, notably dominated by
scale--shift drifting. Through targeted empirical analysis, we trace this instability to
its root cause: fluctuations in latent feature statistics, whose mean and variance
directly determine the predicted depth's scale and shift. Building on this insight, we
introduce Dynamic Feature Normalization (DyFN), a lightweight, causal recurrent module
that dynamically and robustly modulates feature statistics to maintain stable geometry
over time. We adapt powerful pretrained monocular geometry models for streaming by
finetuning only DyFN, a mere 2\% additional parameters, while keeping the backbone
frozen, thereby achieving temporal consistency without compromising single-image
accuracy. Extensive experiments across four benchmarks show that DyFN effectively
eliminates temporal artifacts such as disjointed layering and positional jitter, and
achieves state-of-the-art temporal stability, improving over prior streaming methods by
up to 14\% and even outperforming heavier non-causal video baselines. Project Page:
https://shawlyu.github.io/DyFN

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25308v1
- Authors: Xiaoyang Lyu, Muxin Liu, Xiaoshan Wu, Ruicheng Wang, Yi-Hua Huang, Yang-Tian Sun, Shaoshuai Shi, Xiaojuan Qi
- Published: 2026-05-25T00:13:15Z
- Age days: 1

</details>
