---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18238v1"
published: "2026-05-18T11:32:12Z"
age_days: 1
score: 31
created: 2026-05-20
concepts: ["智能体 Agent"]
---

# Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning

> [!summary] 一句话结论（基于摘要）
> Grounded in this geometry, our repulsion-based allocation is not bounded by any fixed provisioning count; we demonstrate 10M non-colliding virtual identity embeddings against a gallery of 360K real identities.

## 关键点

- **问题**：BIP is therefore a constrained packing problem: available gaps vastly exceed any foreseeable enrollment scale, and provisioned identities remain non-colliding even as new real identities are subsequently enrolled.
- **创新点 / 方法**：We introduce Biometric Identity Provisioning (BIP), a new problem and solution framework that addresses: given an enrollment gallery of real human identities, provision virtual identities that are non-colliding with every enrolled identity, maintain sufficient inter-class separability, and are realizable as high- fide…
- **证据**：Grounded in this geometry, our repulsion-based allocation is not bounded by any fixed provisioning count; we demonstrate 10M non-colliding virtual identity embeddings against a gallery of 360K real identities.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Digital entities such as AI agents and humanoid robots increasingly operate alongside
real humans, yet their identity infrastructure is based on credentials rather than
embodied biometric identity. We introduce Biometric Identity Provisioning (BIP), a new
problem and solution framework that addresses: given an enrollment gallery of real human
identities, provision virtual identities that are non-colliding with every enrolled
identity, maintain sufficient inter-class separability, and are realizable as high-
fidelity face images. The key geometric insight is that real face identities occupy a
low-dimensional subspace of the embedding hypersphere, leaving no residual subspace for
virtual identities. Hence, virtual identities must instead be allocated as unclaimed
gaps within the real face manifold itself. BIP is therefore a constrained packing
problem: available gaps vastly exceed any foreseeable enrollment scale, and provisioned
identities remain non-colliding even as new real identities are subsequently enrolled.
Grounded in this geometry, our repulsion-based allocation is not bounded by any fixed
provisioning count; we demonstrate 10M non-colliding virtual identity embeddings against
a gallery of 360K real identities. Realizing these embeddings as face images requires a
generator that operates outside the training distribution of real face images; we
introduce GapGen, a gap-aware generator trained with a curriculum that progressively
extends synthesis into non-colliding regions, validated at 1M photorealistic virtual
face images. We further construct v-LFW, a virtual counterpart to LFW face dataset, with
protocols for virtual face verification, cross-reality matching, real-vs-virtual
detection, and unified recognition and detection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18238v1
- Authors: Yuyang Ji, Yixuan Shen, Anil Jain, Xiaoming Liu, Feng Liu
- Published: 2026-05-18T11:32:12Z
- Age days: 1

</details>
