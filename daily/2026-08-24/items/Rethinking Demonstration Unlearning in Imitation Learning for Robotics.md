---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20784v1"
published: "2026-08-21T06:53:55Z"
age_days: 3
score: 28
created: 2026-08-24
concepts: ["世界模型", "机器人学习"]
---

# Rethinking Demonstration Unlearning in Imitation Learning for Robotics

> [!summary] 一句话结论（基于摘要）
> Retraining without them is the natural reference, but its cost grows with policy and dataset scale, motivating cheaper operators that edit a trained policy.

## 关键点

- **问题**：Imitation learning for robotics depends on human demonstrations, some of which people may later ask to remove.
- **创新点 / 方法**：Retraining without them is the natural reference, but its cost grows with policy and dataset scale, motivating cheaper operators that edit a trained policy.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/Rethinking Demonstration Unlearning in Imitation Learning for Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Imitation learning for robotics depends on human demonstrations, some of which people may later ask to remove. Retraining without them is the natural reference, but its cost grows with policy and dataset scale, motivating cheaper operators that edit a trained policy. Metrics inherited from machine unlearning, such as forgetting loss or a single membership attack, do not establish what an edit removed from a policy acting in closed loop. We therefore introduce a retrain-calibrated audit that reads demonstration unlearning along two axes: behavior, whether the edited policy acts like one retrained without the removed demonstrations, and evidence, whether an auditor can still detect it was trained on them. The behavior axis measures action divergence to that retrain at matched states, calibrated by a floor built from independent retrains, so a policy at the floor is as close to a retrain as retrains are to each other. The evidence axis applies a per-demonstration membership attack against a retrain null, reporting both its rank and its absolute member-loss level, since rank alone accepts operators that inflate member losses past the null. A conformal test then combines both axes into one hypothesis of joint retrain consistency, against a fleet of independent retrains large enough to reject at conventional significance. Across five preregistered conditions on three real-robot policy classes and two simulation suites, the axes dissociate in both directions on one checkpoint, as an edit may repair task behavior while leaving evidence unchanged, or reduce evidence while moving behavior away from retraining. On the ACT arm, a redirect edit restores blind-scored robot success to 18 of 20 trials.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20784v1
- Authors: Jiazhuo Li, Yu Zhang, Yiming Fei, Kangkang Dong, Xiaojun Zhu, Houde Liu, Jinze Tao
- Published: 2026-08-21T06:53:55Z
- Age days: 3

</details>
