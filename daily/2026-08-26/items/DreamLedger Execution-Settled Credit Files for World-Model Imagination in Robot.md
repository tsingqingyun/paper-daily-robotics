---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.23863v1"
published: "2026-08-24T22:12:10Z"
age_days: 1
score: 28
created: 2026-08-26
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# DreamLedger: Execution-Settled Credit Files for World-Model Imagination in Robot Decision Loops

> [!summary] 一句话结论（基于摘要）
> Robots are beginning to act on world-model predictions, yet reliability is still expressed through instantaneous, model-internal signals.

## 关键点

- **问题**：The resulting credit gates consumption: low-credit predictions shorten the dependent horizon or trigger additional observation; every reliance event remains auditable via dependency tickets and replayable logs.
- **创新点 / 方法**：Robots are beginning to act on world-model predictions, yet reliability is still expressed through instantaneous, model-internal signals.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/DreamLedger Execution-Settled Credit Files for World-Model Imagination in Robot.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots are beginning to act on world-model predictions, yet reliability is still expressed through instantaneous, model-internal signals. DreamLedger instead treats reliability as a persistent deployment object: an execution-settled credit file recording how often consumed predictions are borne out, indexed by operating condition, region, and prediction horizon, and consulted before each use. Each consumed prediction is registered as a claim; attributable outcomes are settled against arriving reality at zero labeling cost, an attribution stage excludes measurement-contaminated outcomes, and a settlement-supervised head complements sparse bins. The resulting credit gates consumption: low-credit predictions shorten the dependent horizon or trigger additional observation; every reliance event remains auditable via dependency tickets and replayable logs. We evaluate DreamLedger in three simulated domains (indoor flight, tabletop manipulation, 2D navigation), via mounts on unmodified DreamerV3, TD-MPC2, and V-JEPA 2-AC, and on a real Franka manipulator. Claim failure is dose-monotone in all 12 held-out condition-horizon cells. Credit-gated planning reduces burned imagination (consumed claims that later fail to redeem) by 62% (95% CI 43-81%) versus blind consumption, with equal success and comparable collision rates. At matched risk targets, persistent books cut verification probes from 1.00 to 0.36/episode in manipulation, at success 0.94 versus 0.98; settlement-grounded calibration retains moderate, seed-consistent operating points unlike raw instantaneous gates. The same trust layer operates across decoder-, latent-, and token-space interfaces, including V-JEPA 2-AC settled on real robot frames. On hardware, settlement remains operational under real sensing and contact noise, a deployment failure loop is re-priced online, and all 1,062 registered spends replay from the audit logs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.23863v1
- Authors: Xianyao Li, Ruitong Tian, Rui Min, Fang Xu, Jing Du
- Published: 2026-08-24T22:12:10Z
- Age days: 1

</details>
