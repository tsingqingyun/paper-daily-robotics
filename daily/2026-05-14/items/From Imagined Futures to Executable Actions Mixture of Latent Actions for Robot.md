---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12167v1"
published: "2026-05-12T14:15:16Z"
age_days: 1
score: 29
created: 2026-05-14
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> To address this gap, we propose MoLA (Mixture of Latent Actions), a control-oriented interface that transforms imagined future videos into executable representations.

## 关键点

- **问题**：Video generation models offer a promising imagination mechanism for robot manipulation by predicting long-horizon future observations, but effectively exploiting these imagined futures for action execution remains challenging.
- **创新点 / 方法**：To address this gap, we propose MoLA (Mixture of Latent Actions), a control-oriented interface that transforms imagined future videos into executable representations.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Video generation models offer a promising imagination mechanism for robot manipulation by predicting long-horizon future observations, but effectively exploiting these imagined futures for action execution remains challenging.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/From Imagined Futures to Executable Actions Mixture of Latent Actions for Robot.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video generation models offer a promising imagination mechanism for robot manipulation
by predicting long-horizon future observations, but effectively exploiting these
imagined futures for action execution remains challenging. Existing approaches either
condition policies on predicted frames or directly decode generated videos into actions,
both suffering from a mismatch between visual realism and control relevance. As a
result, predicted observations emphasize perceptual fidelity rather than action-centric
causes of state transitions, leading to indirect and unstable control. To address this
gap, we propose MoLA (Mixture of Latent Actions), a control-oriented interface that
transforms imagined future videos into executable representations. Instead of passing
predicted frames directly to the policy, MoLA leverages a mixture of pretrained inverse
dynamics models to infer a mixture of latent actions implied by generated visual
transitions. These modality-aware inverse dynamics models capture complementary
semantic, depth, and flow cues, providing a structured and physically grounded action
representation that bridges video imagination and policy execution. We evaluate our
approach on simulated benchmarks (LIBERO, CALVIN, and LIBERO-Plus) and real-world robot
manipulation tasks, achieving consistent gains in task success, temporal consistency,
and generalization.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12167v1
- Authors: Yajie Li, Bozhou Zhang, Chun Gu, Zipei Ma, Jiahui Zhang, Jiankang Deng, Xiatian Zhu, Li Zhang
- Published: 2026-05-12T14:15:16Z
- Age days: 1

</details>
