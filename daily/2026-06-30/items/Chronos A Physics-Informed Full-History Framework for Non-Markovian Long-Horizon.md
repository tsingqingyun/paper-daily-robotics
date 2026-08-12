---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30318v1"
published: "2026-06-29T14:00:17Z"
age_days: 0
score: 33
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Chronos: A Physics-Informed Full-History Framework for Non-Markovian Long-Horizon Manipulation

> [!summary] 一句话结论（基于摘要）
> Across 16 simulated tasks and 4 real-world experiments, Chronos is evaluated on precision insertion, general manipulation, and memory-dependent long- horizon control.

## 关键点

- **问题**：This Markovian shortcut fails in memory-dependent manipulation: identical observations can demand different actions after different histories.
- **创新点 / 方法**：We present Chronos, a physics- informed full-history framework for non-Markovian long-horizon manipulation.
- **证据**：Across 16 simulated tasks and 4 real-world experiments, Chronos is evaluated on precision insertion, general manipulation, and memory-dependent long- horizon control.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose robot policies should be modeled as dynamical systems, yet many VLA and
generative imitation policies still rely on present observations or short windows. This
Markovian shortcut fails in memory-dependent manipulation: identical observations can
demand different actions after different histories. We present Chronos, a physics-
informed full-history framework for non-Markovian long-horizon manipulation. The key
idea is to elevate observation history from auxiliary context to the latent state of the
policy dynamics. At each physical control step, Chronos forms one state-representative
token by fusing observation and proprioception, so the token sequence is aligned one-to-
one with physical time. A selective state space model propagates this causal historical
state, which conditions a multimodal coarse action prior through implicit maximum
likelihood estimation (IMLE). This prior is then refined by a second-order Schrodinger-
inspired bridge that predicts acceleration fields, yielding smoother and more physically
grounded robot motion. Across 16 simulated tasks and 4 real-world experiments, Chronos
is evaluated on precision insertion, general manipulation, and memory-dependent long-
horizon control. On RMBench, where success requires remembering task phase, Chronos
achieves 73.6% average success, outperforming Markovian VLA baseline pi0.5 by +62.4
percentage points, a 6.6x relative gain, while using 10x fewer parameters. It also
surpasses the memory VLA Mem-0 by 22.8 points while using over 30x fewer parameters. In
real-world dual-arm experiments using a single RGB camera, Chronos achieves 78% average
success over four tasks, including 72% on the three memory-dependent tasks, whereas
pi0.5 achieves 7% overall and 0% on the memory-dependent subset. These results suggest
that history should not be treated as auxiliary context, but as the latent state of the
manipulation policy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30318v1
- Authors: Yulin Zhou, Yimeng Wang, Nengyu Wang, Shaojia Xing, Shiyun Tu, Xiang Li, Jingkai Zhang, Ningbo Jiang, Yuankai Lin, Hua Yang, Xiangrui Zeng, Zhouping Yin
- Published: 2026-06-29T14:00:17Z
- Age days: 0

</details>
