---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09537v1"
published: "2026-08-10T12:35:59Z"
age_days: 1
score: 25
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型"]
---

# verdi: retrieval is not transfer for continual world model optimization

> [!summary] 一句话结论（基于摘要）
> Experiments on Ctrl-World, the Cosmos family, and RoboCoin show that VERDI reduces search cost by 68%, GPU cost by 69%, and negative transfer from 0.34 to 0.06, while predicting transfer outcomes with 83% sign accuracy.

## 关键点

- **问题**：However, optimizing a pretrained world model toward a user- specified objective remains difficult: each campaign typically rediscovers optimization strategies from scratch, and the resulting knowledge rarely transfers to the next model.
- **创新点 / 方法**：Guided by this principle, we propose VERDI , a continual framework for evidence-licensed world model optimization.
- **证据**：Experiments on Ctrl-World, the Cosmos family, and RoboCoin show that VERDI reduces search cost by 68%, GPU cost by 69%, and negative transfer from 0.34 to 0.06, while predicting transfer outcomes with 83% sign accuracy.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/verdi retrieval is not transfer for continual world model optimization.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Foundation world models have made remarkable progress in planning, simulation, and
embodied intelligence. However, optimizing a pretrained world model toward a user-
specified objective remains difficult: each campaign typically rediscovers optimization
strategies from scratch, and the resulting knowledge rarely transfers to the next model.
Existing research agents automate the optimization loop but treat successful strategies
as directly reusable recipes, without principled safeguards for when transfer is
appropriate. We argue instead that retrieval is not transfer: a strategy validated on
one model is at best an optimization hypothesis for another, and becomes transferable
knowledge only after target-side experimental valida- tion. Guided by this principle, we
propose VERDI , a continual framework for evidence-licensed world model optimization.
VERDI characterizes each world model through shared inference-time probes to construct
an Optimization Fin- gerprint, retrieves relevant prior experience as ranked hypotheses,
and validates every candidate under a frozen target-side verifier before admitting it as
reusable evidence; contradictions among nearby fingerprints further trigger probe
evolution, continually refining the diagnostic representation itself. Experiments on
Ctrl-World, the Cosmos family, and RoboCoin show that VERDI reduces search cost by 68%,
GPU cost by 69%, and negative transfer from 0.34 to 0.06, while predicting transfer
outcomes with 83% sign accuracy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09537v1
- Authors: Junyu Wu, Shiqin Nie, Youyi Kou, Baohua Yin, Guocai Yao, Qingyu Chen, Jingheng Ma, Shiji Zhou, Hongyong Song, Mingchen Zhuge, Sen Cui, Changshui Zhang
- Published: 2026-08-10T12:35:59Z
- Age days: 1

</details>
