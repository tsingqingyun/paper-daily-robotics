---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11270v1"
published: "2026-09-10T09:04:04Z"
age_days: 1
score: 25
created: 2026-09-12
concepts: ["机器人学习"]
---

# Beyond Noise Steering: Dual-Latent Space Reinforcement Learning for Generative Robot Policy

> [!summary] 先说人话（基于摘要）
> DLSRL在冻结生成式机器人策略的情况下，同时控制初始噪声和生成过程中的动作特征，让强化学习有更多调整行为的入口。

## 这篇到底在做什么

- **卡在哪里**：已有强化学习适配主要操纵初始噪声，无法直接改变生成器中间动作表示；摘要认为这限制了适配效率与表现。
- **关键解法**：Actor输出两个潜变量：一个控制初始噪声，另一个映射为适配特征，经残差连接注入中间动作token的隐藏状态；基础策略保持冻结。
- **拿什么证明**：摘要报告在多种生成策略架构和机器人操作任务上加快在线适配并获得有竞争力的表现，但未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人强化学习，提供复用预训练动作先验并扩展适配自由度的技术路线。
- **先别急着信**：需要核查双潜变量相对单纯噪声控制的独立收益，以及在线适配效率具体如何计量。
- **判断**：值得读特征注入和对照实验；仅凭摘要尚不足以判断额外控制入口是否稳定有效。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/Beyond Noise Steering Dual-Latent Space Reinforcement Learning for Generative Ro.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pretrained generative robot policies learn expressive action priors from demonstrations. However, existing reinforcement learning methods only steer the noisy space but fail to modulate intermediate action representations during the generation process, resulting in performance degradation and inefficiency. To address this limitation, we propose a novel Dual-Latent Space Reinforcement Learning (DLSRL) framework, which complements initial-noise steering with representation-level control inside the frozen generator. Specifically, our actor network predicts two distinct latent variables: an initial-noise latent variable that steers behavior generation, and an action-representation latent variable for intermediate feature modulation. Moreover, this representation latent variable is mapped to adapter features and ingeniously injected into the hidden states of intermediate action tokens via residual connections. Our dual-control design enables direct adjustment of action representations without updating the base policy. Experiments across generative policy architectures and robotic manipulation tasks show that DLSRL effectively accelerates online robot policy adaptation and achieves competitive performance. Our code is available at \href{https://github.com/xianchaoxiu/DLSRL}{https://github.com/xianchaoxiu/DLSRL}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11270v1
- Authors: Pengfei Zhang, Teng Sun, Xianchao Xiu
- Published: 2026-09-10T09:04:04Z
- Age days: 1

</details>
