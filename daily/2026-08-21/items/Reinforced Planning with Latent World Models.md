---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18669v1"
published: "2026-08-19T08:21:28Z"
age_days: 1
score: 26
created: 2026-08-21
concepts: ["智能体 Agent", "世界模型"]
---

# Reinforced Planning with Latent World Models

> [!summary] 一句话结论（基于摘要）
> Across visual navigation, arm reaching, and robotic manipulation on two world-model backbones, RP1 substantially outperforms hand-designed search algorithms, reaching near-perfect success in several settings while using $1,000 \times$ less world-model rollout…

## 关键点

- **问题**：Humans solve complex problems by constructing plans and mentally simulating their outcomes with an internal model of the world.
- **创新点 / 方法**：We introduce the Reinforced Planning, a method based on the idea that search can be learned by reinforcing good search rules into a neural planner.
- **证据**：Across visual navigation, arm reaching, and robotic manipulation on two world-model backbones, RP1 substantially outperforms hand-designed search algorithms, reaching near-perfect success in several settings while using $1,000 \times$ less world-model rollouts and being up to $67 \times$ faster than the strongest alte…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Reinforced Planning with Latent World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humans solve complex problems by constructing plans and mentally simulating their outcomes with an internal model of the world. Machine learning has produced world models that similarly predict the outcomes of action sequences, but the improvement of candidate plans still isn't fully learned. Current planners are either hand-designed, distilled from a hand-designed optimizer, or learned only to inform an amortized policy rather than to revise the plan itself. We introduce the Reinforced Planning, a method based on the idea that search can be learned by reinforcing good search rules into a neural planner. Our implementation RP1 learns both how to evaluate imagined outcomes through a critic, as well as how to improve multi-step plans through an optimizer trained fully offline from imagined world-model roll-outs. To our knowledge, RP1 is the first method to fully learn how to improve multi-step plans. Furthermore, it can be trained independently of and attached to any pretrained latent world model. Across visual navigation, arm reaching, and robotic manipulation on two world-model backbones, RP1 substantially outperforms hand-designed search algorithms, reaching near-perfect success in several settings while using $1,000 \times$ less world-model rollouts and being up to $67 \times$ faster than the strongest alternative under concurrent planner inference.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18669v1
- Authors: Armin Sommer, Jannik Schilling
- Published: 2026-08-19T08:21:28Z
- Age days: 1

</details>
