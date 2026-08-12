---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01410v1"
published: "2026-07-01T19:15:17Z"
age_days: 4
score: 25
created: 2026-07-06
concepts: ["世界模型", "Sim2Real"]
---

# BIFROST: Bridging Invariant Feature Representation for Observation-space Sim2Real Transfer

> [!summary] 一句话结论（基于摘要）
> We provide empirical evidence on sim2sim visual navigation and sim2real contact rich manipulation task and visual servoing task that BIFROST achieves effective transfer where domain adaptation and co-training baselines fail under both visual and dynamics doma…

## 关键点

- **问题**：Sim2real transfer for robot policy learning suffers due to mismatch between simulation and reality.
- **创新点 / 方法**：We introduce BIFROST, which learns a shared history encoder on paired cross- domain data via cross-domain bisimulation objective: observation-action sequences leading to equivalent long-term behavior are mapped to nearby latent states, regardless of domain.
- **证据**：We provide empirical evidence on sim2sim visual navigation and sim2real contact rich manipulation task and visual servoing task that BIFROST achieves effective transfer where domain adaptation and co-training baselines fail under both visual and dynamics domain gaps.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[Sim2Real]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Sim2real transfer for robot policy learning suffers due to mismatch between simulation
and reality. Existing methods typically address each gap in isolation through separate
adaptation modules, which are composed or layered when both gaps coexist. Yet the basis
for attempting sim2real in the first place is that there is shared structure between a
task in simulation and reality, where equivalent actions from equivalent configurations
produce equivalent long term outcomes regardless of domain specific differences in
rendering or physics. In this paper, we study whether we can identify and exploit this
shared structure from raw observations to train a policy that enables zero shot
transfer. We introduce BIFROST, which learns a shared history encoder on paired cross-
domain data via cross-domain bisimulation objective: observation-action sequences
leading to equivalent long-term behavior are mapped to nearby latent states, regardless
of domain. Policies trained on these latent states in simulation transfer zero-shot to
reality. We provide empirical evidence on sim2sim visual navigation and sim2real contact
rich manipulation task and visual servoing task that BIFROST achieves effective transfer
where domain adaptation and co-training baselines fail under both visual and dynamics
domain gaps.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01410v1
- Authors: Yunfu Deng, Josiah P. Hanna
- Published: 2026-07-01T19:15:17Z
- Age days: 4

</details>
