---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09749v1"
published: "2026-06-08T17:11:16Z"
age_days: 1
score: 37
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Your Model Already Knows: Attention-Guided Safety Filter for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> On the dynamic variant, where the oracle's init-time target assignment becomes stale, our method substantially outperforms it by 43%, on average.

## 关键点

- **问题**：However, these policies offer no guarantees against collisions with task-irrelevant objects in the scene.
- **创新点 / 方法**：On the original static benchmark, our method performs comparably to an oracle that uses privileged simulator state to identify the target, emulating a VLM-based identification step run once at episode initialization.
- **证据**：On the dynamic variant, where the oracle's init-time target assignment becomes stale, our method substantially outperforms it by 43%, on average.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have demonstrated impressive end-to-end performance
across a variety of robotic manipulation tasks. However, these policies offer no
guarantees against collisions with task-irrelevant objects in the scene. Existing safety
filters sidestep this problem by querying a vision-language model (VLM) to identify
obstacles and their locations. This, however, is too slow to run in the control loop and
can only be invoked at episode initialization, leaving the filter unable to track moving
obstacles. We discover that a small number of attention heads within a VLA model
reliably localize the object the policy intends to approach. These heads can be
exploited within a training-free safety framework that obtains the active target from
the attention heads at every step, treats the remainder of the scene as obstacles, and
feeds these into a Control Barrier Function (CBF) filter. Together with a lightweight
real-time object tracker, this allows for collision avoidance for non-static obstacles.
We evaluate our framework on SafeLIBERO, which we extend with moving obstacles. On the
original static benchmark, our method performs comparably to an oracle that uses
privileged simulator state to identify the target, emulating a VLM-based identification
step run once at episode initialization. On the dynamic variant, where the oracle's
init-time target assignment becomes stale, our method substantially outperforms it by
43%, on average. Our findings suggest that the perceptual signals needed for real-time
safety filtering are already present within VLA policies and can be exploited without
additional training or heavy auxiliary models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09749v1
- Authors: Seongbin Park, Fan Zhang, Baharan Mirzasoleiman, Shahriar Talebi, Nader Sehatbakhsh
- Published: 2026-06-08T17:11:16Z
- Age days: 1

</details>
