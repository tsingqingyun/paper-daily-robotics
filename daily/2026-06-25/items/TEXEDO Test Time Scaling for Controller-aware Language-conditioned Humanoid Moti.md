---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22998v2"
published: "2026-06-22T08:14:35Z"
age_days: 2
score: 31
created: 2026-06-25
concepts: ["世界模型"]
---

# TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation

> [!summary] 一句话结论（基于摘要）
> Through large- scale simulation studies and real-world deployment on a Unitree G1 humanoid robot, we show that TEXEDO consistently improves both tracking fidelity and text alignment.

## 关键点

- **问题**：Although such data provides rich semantic and kinematic priors, it fails to capture the nuances of whole-body tracking controllers, including balance, contact dynamics, actuation limits, and controller-specific failure modes.
- **创新点 / 方法**：We introduce TEXEDO, a test-time scaling framework for humanoid motion generation that improves motion quality without requiring a stronger underlying generator.
- **证据**：Through large- scale simulation studies and real-world deployment on a Unitree G1 humanoid robot, we show that TEXEDO consistently improves both tracking fidelity and text alignment.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/TEXEDO Test Time Scaling for Controller-aware Language-conditioned Humanoid Moti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Text-conditioned motion generation is a promising interface for programming humanoid
robots, yet current generators are often trained on human motion datasets retargeted to
robot morphologies. Although such data provides rich semantic and kinematic priors, it
fails to capture the nuances of whole-body tracking controllers, including balance,
contact dynamics, actuation limits, and controller-specific failure modes. As a result,
generated motions can be semantically plausible but difficult or impossible for the
robot to execute. We introduce TEXEDO, a test-time scaling framework for humanoid motion
generation that improves motion quality without requiring a stronger underlying
generator. Given a text prompt, TEXEDO samples multiple candidate motions from a
pretrained text-conditioned generator and selects the best motion that is both
executable and task-aligned. The reward model combines a dynamic feasibility verifier,
distilled from whole-body tracking rollouts to predict physical executability, with a
semantic alignment verifier that measures text-motion alignment in a learned co-
embedding space. Our pipeline treats dynamic feasibility as a hard constraint and
semantic alignment as the selection objective within the feasible set. Through large-
scale simulation studies and real-world deployment on a Unitree G1 humanoid robot, we
show that TEXEDO consistently improves both tracking fidelity and text alignment. These
results demonstrate that grounded verification is an effective path toward deployable
language-guided humanoid motion generation. Project website:
https://jianuocao.github.io/TEXEDO/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22998v2
- Authors: Jianuo Cao, Yuxin Chen, Yuzhen Song, Masayoshi Tomizuka, Chenran Li, Thomas Tian
- Published: 2026-06-22T08:14:35Z
- Age days: 2

</details>
