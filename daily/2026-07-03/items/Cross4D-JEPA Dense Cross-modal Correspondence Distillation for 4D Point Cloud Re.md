---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00514v1"
published: "2026-07-01T06:49:17Z"
age_days: 2
score: 33
created: 2026-07-03
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Cross4D-JEPA: Dense Cross-modal Correspondence Distillation for 4D Point Cloud Representation Learning

> [!summary] 一句话结论（基于摘要）
> Experimental results show that, under a matched protocol, the proposed method consistently outperforms intra-modal and global cross-modal baselines across the four benchmarks and is competitive with heavier published 4D methods; further analysis attributes th…

## 关键点

- **问题**：Existing pretext tasks, however, are almost entirely intra-modal, and the few methods that transfer knowledge from 2D foundation models rely on a single global embedding per clip, discarding the rich per-patch semantics that these models compute.
- **创新点 / 方法**：To address this gap, we propose Cross4D-JEPA, a teacher-student method that distills a frozen 2D foundation model, an image model DINOv2, or a video model V-JEPA 2, into a 4D point encoder.
- **证据**：Experimental results show that, under a matched protocol, the proposed method consistently outperforms intra-modal and global cross-modal baselines across the four benchmarks and is competitive with heavier published 4D methods; further analysis attributes this gain primarily to the granularity of the correspondence r…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Automatic understanding of dynamic 4D point clouds, the 3D-point sequences captured over
time by depth sensors and LiDAR, is central to robotics and embodied perception. Yet
annotating them densely is expensive, making self-supervised pretraining the natural
route to transferable representations. Existing pretext tasks, however, are almost
entirely intra-modal, and the few methods that transfer knowledge from 2D foundation
models rely on a single global embedding per clip, discarding the rich per-patch
semantics that these models compute. To address this gap, we propose Cross4D-JEPA, a
teacher-student method that distills a frozen 2D foundation model, an image model
DINOv2, or a video model V-JEPA 2, into a 4D point encoder. The proposed method combines
(1) a dense cross-modal correspondence that maps every 3D point to the teacher patch
feature it projects to, and (2) a per-point objective that trains the student to match
these features in latent space with no masking, negatives, or decoder. We evaluate
Cross4D-JEPA on four benchmarks, MSR-Action3D, DeformingThings4D, NTU-RGB+D 60, and
HOI4D, against intra-modal and global cross-modal baselines. Experimental results show
that, under a matched protocol, the proposed method consistently outperforms intra-modal
and global cross-modal baselines across the four benchmarks and is competitive with
heavier published 4D methods; further analysis attributes this gain primarily to the
granularity of the correspondence rather than the teacher modality. Beyond recognition
accuracy, the dense representation learned by Cross4D-JEPA transfers across domains,
improves label efficiency, and improves full-label fine-tuning under the same training
budget, while a 13x smaller encoder matches a heavyweight pooling backbone.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00514v1
- Authors: Trung Thanh Nguyen, Hai Nguyen-Truong, Tu Vo, Hoang M. Truong, Tuan-Anh Vu
- Published: 2026-07-01T06:49:17Z
- Age days: 2

</details>
