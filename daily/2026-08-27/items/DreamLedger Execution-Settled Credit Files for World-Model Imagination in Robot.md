---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.23863v1"
published: "2026-08-24T22:12:10Z"
age_days: 2
score: 28
created: 2026-08-27
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# DreamLedger: Execution-Settled Credit Files for World-Model Imagination in Robot Decision Loops

> [!summary] 先说人话（基于摘要）
> DreamLedger 给世界模型建立可持续更新的“信用档案”：每次采用预测都登记、随后用真实执行结果结算，并按条件、区域和预测时域决定缩短规划或追加观测。

## 问题

机器人开始依赖世界模型规划，但可靠性通常只是瞬时、模型内部的分数，不能积累某类预测在实际部署中是否兑现，也难以审计依赖链。

## 创新点或方法

每个被消费的预测注册为claim，真实观测到达后零标注结算；归因阶段排除测量污染结果，监督头补充稀疏分箱。信用门控预测消费，低信用时缩短依赖时域或请求验证，并用票据和日志记录所有依赖。

## 证据

跨3个仿真域、DreamerV3、TD-MPC2、V-JEPA 2-AC及真机Franka评测；12个留出条件—时域单元中失败率均随使用剂量单调变化。相对盲用，烧毁想象减少62%（95% CI 43%–81%），成功率相等、碰撞率相近；操作任务验证探针从每回合1.00降至0.36，成功率0.94对0.98。真机1,062次登记消费均可由日志回放。


## 局限

减少失败预测消费并未提高成功率，且示例中成功率略降；结算延迟、归因错误和分布快速变化时的信用滞后需重点核查。

- **判断**：今天最有新意的可靠性工作，值得精读协议与统计设计；它不是更强世界模型，而是更谨慎、可审计地使用世界模型。

## 研究关联

这为世界模型规划增加了与模型架构无关的部署信任层，尤其适合高风险机器人系统的在线校准、审计和主动复核。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/DreamLedger Execution-Settled Credit Files for World-Model Imagination in Robot.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots are beginning to act on world-model predictions, yet reliability is still expressed through instantaneous, model-internal signals. DreamLedger instead treats reliability as a persistent deployment object: an execution-settled credit file recording how often consumed predictions are borne out, indexed by operating condition, region, and prediction horizon, and consulted before each use. Each consumed prediction is registered as a claim; attributable outcomes are settled against arriving reality at zero labeling cost, an attribution stage excludes measurement-contaminated outcomes, and a settlement-supervised head complements sparse bins. The resulting credit gates consumption: low-credit predictions shorten the dependent horizon or trigger additional observation; every reliance event remains auditable via dependency tickets and replayable logs. We evaluate DreamLedger in three simulated domains (indoor flight, tabletop manipulation, 2D navigation), via mounts on unmodified DreamerV3, TD-MPC2, and V-JEPA 2-AC, and on a real Franka manipulator. Claim failure is dose-monotone in all 12 held-out condition-horizon cells. Credit-gated planning reduces burned imagination (consumed claims that later fail to redeem) by 62% (95% CI 43-81%) versus blind consumption, with equal success and comparable collision rates. At matched risk targets, persistent books cut verification probes from 1.00 to 0.36/episode in manipulation, at success 0.94 versus 0.98; settlement-grounded calibration retains moderate, seed-consistent operating points unlike raw instantaneous gates. The same trust layer operates across decoder-, latent-, and token-space interfaces, including V-JEPA 2-AC settled on real robot frames. On hardware, settlement remains operational under real sensing and contact noise, a deployment failure loop is re-priced online, and all 1,062 registered spends replay from the audit logs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.23863v1
- Authors: Xianyao Li, Ruitong Tian, Rui Min, Fang Xu, Jing Du
- Published: 2026-08-24T22:12:10Z
- Age days: 2

</details>
