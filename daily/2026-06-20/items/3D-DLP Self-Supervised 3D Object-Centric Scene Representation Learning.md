---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19451v1"
published: "2026-06-17T18:00:08Z"
age_days: 2
score: 29
created: 2026-06-20
concepts: ["AI 核心知识地图"]
---

# 3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning

> [!summary] 一句话结论（基于摘要）
> Furthermore, we show that leveraging these compact 3D latent particles for downstream robotic manipulation improves performance over baselines that either lack explicit 3D information or rely on memory-intensive dense 3D inputs without object-centric structur…

## 关键点

- **问题**：Furthermore, we show that leveraging these compact 3D latent particles for downstream robotic manipulation improves performance over baselines that either lack explicit 3D information or rely on memory-intensive dense 3D inputs without object-centric structure.
- **创新点 / 方法**：We introduce 3D-DLP, a self-supervised object-centric representation learning model that decomposes scene-level RGB-D or voxel observations into a set of 3D latent particles.
- **证据**：Furthermore, we show that leveraging these compact 3D latent particles for downstream robotic manipulation improves performance over baselines that either lack explicit 3D information or rely on memory-intensive dense 3D inputs without object-centric structure.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/3D-DLP Self-Supervised 3D Object-Centric Scene Representation Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce 3D-DLP, a self-supervised object-centric representation learning model that
decomposes scene-level RGB-D or voxel observations into a set of 3D latent particles.
Building on the Deep Latent Particles (DLP) framework, each particle encodes
disentangled attributes, including 3D keypoint position, bounding box dimensions, and
appearance features, and represents a distinct entity in the scene. The model learns
interpretable per-particle segmentation maps through an end-to-end self-supervised
reconstruction objective. We demonstrate on both simulated and real-world datasets that
the learned latent space is interpretable and controllable: by manipulating particle
positions and decoding, we can generate novel scene configurations. Furthermore, we show
that leveraging these compact 3D latent particles for downstream robotic manipulation
improves performance over baselines that either lack explicit 3D information or rely on
memory-intensive dense 3D inputs without object-centric structure. Code and videos are
available at https://eubooks3003.github.io/3d-dlp.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19451v1
- Authors: Ellina Zhang, Madhaven Iyengar, Amir Zadeh, Chuan Li, Deepak Pathak, David Held, Tal Daniel
- Published: 2026-06-17T18:00:08Z
- Age days: 2

</details>
