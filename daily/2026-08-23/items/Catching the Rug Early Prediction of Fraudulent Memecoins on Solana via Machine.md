---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20271v1"
published: "2026-08-20T17:09:41Z"
age_days: 2
score: 22
created: 2026-08-23
concepts: ["世界模型"]
---

# Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine Learning

> [!summary] 一句话结论（基于摘要）
> Despite the absence of code-level features, we demonstrate that classic machine learning models, particularly Gradient Boosting (XGBoost), achieve robust performance in detecting potential rug pulls using only the first 5 minutes of trading data.

## 问题

The rapid proliferation of memecoins on blockchain platforms has increased the risk of fraudulent activities, particularly rug pulls.

## 创新点或方法

While previous studies have focused on Ethereum-based tokens, this paper shifts the spotlight to Solana, the leading blockchain for memecoins by trading volume and token count.

## 证据

Despite the absence of code-level features, we demonstrate that classic machine learning models, particularly Gradient Boosting (XGBoost), achieve robust performance in detecting potential rug pulls using only the first 5 minutes of trading data.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：世界模型
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/Catching the Rug Early Prediction of Fraudulent Memecoins on Solana via Machine.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The rapid proliferation of memecoins on blockchain platforms has increased the risk of fraudulent activities, particularly rug pulls. While previous studies have focused on Ethereum-based tokens, this paper shifts the spotlight to Solana, the leading blockchain for memecoins by trading volume and token count. Unlike Ethereum, where rug pulls often exploit smart contract backdoors, Solana memecoin rug pulls are predominantly driven by liquidity manipulation and social dynamics. This research pioneers large-scale rug pull early detection in the Solana ecosystem by assembling a dataset of 6.4 million tokens over 7 months. Market analysis reveals that a vast majority of these memecoins exhibit rug pull characteristics within one hour of launch, highlighting the urgency of short-horizon prediction. Despite the absence of code-level features, we demonstrate that classic machine learning models, particularly Gradient Boosting (XGBoost), achieve robust performance in detecting potential rug pulls using only the first 5 minutes of trading data. Furthermore, we evaluate cross-platform generalization between PumpFun and Raydium, revealing that multi-source data fusion significantly mitigates domain shift and improves detection reliability. This study advances the understanding of DeFi fraud on high-throughput chains and provides a practical framework for protecting investors.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20271v1
- Authors: Jianghai Li, Pavel Kuznetsov, Yury Yanovich, Konstantin Nott-Whaley, Igor Vodolazov
- Published: 2026-08-20T17:09:41Z
- Age days: 2

</details>
