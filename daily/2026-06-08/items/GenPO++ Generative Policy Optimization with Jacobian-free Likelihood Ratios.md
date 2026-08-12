---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06967v1"
published: "2026-06-05T06:54:09Z"
age_days: 2
score: 30
created: 2026-06-08
concepts: ["多模态基础模型", "机器人学习"]
---

# GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios

> [!summary] 一句话结论（基于摘要）
> We evaluate GenPO++ on large- scale simulated control, fine-tuning, and real-world robotic manipulation tasks, where it achieves competitive or superior performance over state-of-the-art on-policy RL methods, while improving training stability and computation…

## 关键点

- **问题**：However, applying such generative policies to likelihood- based on-policy learning remains limited by the difficulty of evaluating the probability of executed actions.
- **创新点 / 方法**：In this work, we propose GenPO++, a reversible generative policy optimization framework that uses history states as auxiliary memory in a high-order reversible ODE solver, yielding exact inversion without changing the original action dimension.
- **证据**：We evaluate GenPO++ on large- scale simulated control, fine-tuning, and real-world robotic manipulation tasks, where it achieves competitive or superior performance over state-of-the-art on-policy RL methods, while improving training stability and computational efficiency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/GenPO++ Generative Policy Optimization with Jacobian-free Likelihood Ratios.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generative policies provide expressive and multimodal action distributions, making them
attractive for reinforcement learning (RL) in complex continuous-control tasks. Among
them, flow-based policies are especially appealing because they generate actions through
deterministic transport maps. However, applying such generative policies to likelihood-
based on-policy learning remains limited by the difficulty of evaluating the probability
of executed actions. Existing flow RL methods either replace the true action-density
ratio with approximate surrogates, which can introduce biased updates, or recover exact
likelihoods through dummy-action augmentation, which enlarges the policy space and
increases computation. In this work, we propose GenPO++, a reversible generative policy
optimization framework that uses history states as auxiliary memory in a high-order
reversible ODE solver, yielding exact inversion without changing the original action
dimension. The resulting generative policy map has a log-determinant determined only by
fixed solver coefficients, enabling exact and Jacobian-free likelihood-ratio
computation. This design preserves the expressiveness of generative flow policies while
avoiding both action ratio bias and dummy-action overhead. We evaluate GenPO++ on large-
scale simulated control, fine-tuning, and real-world robotic manipulation tasks, where
it achieves competitive or superior performance over state-of-the-art on-policy RL
methods, while improving training stability and computational efficiency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06967v1
- Authors: Ke Hu, Shutong Ding, Panxin Tao, Jingya Wang, Ye Shi
- Published: 2026-06-05T06:54:09Z
- Age days: 2

</details>
