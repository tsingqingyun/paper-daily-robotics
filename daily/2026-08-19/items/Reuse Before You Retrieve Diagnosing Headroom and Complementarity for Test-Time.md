---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17484v1"
published: "2026-08-18T08:11:31Z"
age_days: 0
score: 35
created: 2026-08-19
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies

> [!summary] 一句话结论（基于摘要）
> Frozen vision-language-action (VLA) policies are increasingly improved at test time by sampling additional policy behaviors or introducing external demonstrations.

## 关键点

- **问题**：It also transfers to a different robot and simulator and remains effective under degraded observations, while experiments with autoregressive OpenVLA illustrate the distinction between available headroom and the ability to rank candidate rollouts.
- **创新点 / 方法**：Frozen vision-language-action (VLA) policies are increasingly improved at test time by sampling additional policy behaviors or introducing external demonstrations.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Reuse Before You Retrieve Diagnosing Headroom and Complementarity for Test-Time.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Frozen vision-language-action (VLA) policies are increasingly improved at test time by sampling additional policy behaviors or introducing external demonstrations. Yet there is little guidance for deciding which intervention a deployed policy actually needs. Additional sampling is useful only when better behavior already exists within the policy's stochastic rollouts and can be identified, whereas retrieval is most useful when the relevant action prior is not reliably represented by the policy. We study this decision through two measurable factors, recoverable headroom and retrieval complementarity, which characterize how much useful behavior is already available to recover and whether an external action prior fills a measurable gap. We evaluate an episode-level retry selector under retryable or parallel execution, together with retrieval across multiple frozen VLA policies and environments. The selector consistently recovers substantial latent capability across all tested VLA backbones on LIBERO, with gains of up to 21.0 success-rate points that closely track recoverable headroom. It also transfers to a different robot and simulator and remains effective under degraded observations, while experiments with autoregressive OpenVLA illustrate the distinction between available headroom and the ability to rank candidate rollouts. Retrieval behaves differently, improving the policy with the largest measured action-prior gap and providing further gains when combined with selection. Together, these results provide an empirical basis for characterizing test-time augmentation opportunities by separating capability that can be recovered from the frozen policy from behavioral priors that may need to be introduced externally.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17484v1
- Authors: Yuhwan Jeong, Kuk-Jin Yoon
- Published: 2026-08-18T08:11:31Z
- Age days: 0

</details>
