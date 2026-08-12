---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00678v1"
published: "2026-07-01T09:21:20Z"
age_days: 1
score: 38
created: 2026-07-03
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ABot-M0.5: Unified Mobility-and-Manipulation World Action Model

> [!summary] 一句话结论（基于摘要）
> Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained control accuracy.

## 关键点

- **问题**：Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods.
- **创新点 / 方法**：We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency.
- **证据**：Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained control accuracy.
- **局限**：Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/ABot-M0.5 Unified Mobility-and-Manipulation World Action Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Mobile manipulation is a key capability for general-purpose robots, yet remains
challenging for current embodied learning methods. VLA policies are typically reactive
and lack explicit world modeling, while existing World Action Models (WAMs) are still
poorly aligned with the structure of mobile manipulation: they operate on coarse video
chunks, model entangled navigation-manipulation actions, and train inverse dynamics
under supervision that does not match autoregressive inference. As a result, they often
miss fine-grained contact dynamics, suffer from action-distribution conflicts, and
accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new WAM built on
the insight that mobile manipulation requires alignment at three levels: temporal
granularity, action space, and train-test consistency. To align temporal granularity, we
introduce intermediate latent actions that capture local visual state transitions and
serve as an bridging action space between video latents and embodiment-specific
controls. To align action space, we design a dual-level Mixture-of-Transformers
architecture that disentangles both modality representations and heterogeneous action
subspaces such as base movement and arm manipulation. To align inference conditions, we
propose the dream-forcing training strategy that progressively trains inverse dynamics
on model-predicted videos, improving train-test alignment and robustness during
autoregressive prediction. Experiments on challenging mobile and fine-grained
manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance
in both long-horizon task success and finegrained control accuracy. These results
highlight the critical importance of granularity-aligned, action-disentangled, and
inference-consistent world-action modeling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00678v1
- Authors: Ronghan Chen, Yandan Yang, Zuojin Tang, Dongjie Huo, Tong Lin, Haoning Wu, Haoyun Liu, Yuzhi Chen, Lulu Zheng, Botai Yuan, Tianlun Li, Mingxin Wang, Dekang Qi, Bin Hu, Wei Mei, Yuze Xuan, Haolong Yang, Yanqing Zhu, Mu Xu, Zhiheng Ma, Xinyuan Chang
- Published: 2026-07-01T09:21:20Z
- Age days: 1

</details>
