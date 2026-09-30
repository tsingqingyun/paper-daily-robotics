---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09945v1"
published: "2026-09-09T09:35:44Z"
age_days: 2
score: 24
created: 2026-09-12
concepts: ["具身智能评测与基准"]
---

# Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending

> [!summary] 先说人话（基于摘要）
> 这篇信贷论文发现，模型抵御一种攻击，并不代表能抵御其他攻击。混合攻击训练在不同扰动间取得更均衡的鲁棒性。

## 这篇到底在做什么

- **卡在哪里**：P2P信贷申请者可能修改自报信息影响评分，而单一攻击配单一防御的评估难以揭示防御能否跨攻击类型泛化。
- **关键解法**：在Lending Club数据子集上，对逻辑回归、前馈网络和表格transformer，组合FGSM、PGD、椒盐噪声、DeepFool及混合训练；扰动限定于申请者可修改特征，并用分层交叉验证检查完整训练—测试组合。
- **拿什么证明**：摘要报告对抗训练显著改善匹配攻击鲁棒性，梯度攻击间迁移较好、向非梯度破坏迁移较弱；混合训练保持干净测试表现并取得更均衡鲁棒性。摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：与具身智能基准仅有评测设计上的间接联系：可以借鉴跨扰动类型测试的思路，没有直接机器人或VLA证据。
- **先别急着信**：结论来自信贷表格任务，不能直接外推到感知、控制或闭环机器人系统。
- **判断**：机器人日报可降级为跨领域评测参考，无需按具身核心论文深读。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/Adversarial Training for Tabular Credit Scoring A Multi-Attack Robustness Evalua.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Machine learning-based credit scoring is increasingly central to Peer-to-Peer (P2P) lending, yet its resilience to adversarial manipulation, where applicants strategically alter self-reported inputs to secure favourable decisions, remains poorly understood. Most adversarial-robustness evidence comes from image and text domains and evaluates a single attack against a matching defence, offering little guidance on how defences generalise across attack types in tabular credit data. We address this with a systematic train-test robustness benchmark on a large Lending Club subset, spanning three model families (logistic regression, a feed-forward neural network, and a transformer for tabular data) and four attacks confined to applicant-mutable features: Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), Salt-and-Pepper (S&P) noise, and DeepFool, plus a mixed-attack regime. Across a full grid evaluated with stratified cross-validation, adversarial training sharply improves robustness against the attack it is trained on and transfers well within the gradient-based family, but transfers weakly to non-gradient corruption, so single-attack defences overstate real-world resilience. Mixed training delivers the most balanced robustness across heterogeneous attacks while preserving clean-test performance, supporting multi-attack stress testing in credit-model governance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09945v1
- Authors: Gijs A. F. Niewzwaag, Marijn G. S. Veth, Manuele Massei, Marcos R. Machado
- Published: 2026-09-09T09:35:44Z
- Age days: 2

</details>
