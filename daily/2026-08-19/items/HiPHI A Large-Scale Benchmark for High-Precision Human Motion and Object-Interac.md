---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16222v1"
published: "2026-08-17T07:54:26Z"
age_days: 1
score: 30
created: 2026-08-19
concepts: ["具身智能评测与基准"]
---

# HiPHI: A Large-Scale Benchmark for High-Precision Human Motion and Object-Interaction

> [!summary] 一句话结论（基于摘要）
> Created using an optical motion capture pipeline, HiPHI provides sub-millimeter spatial marker tracking accuracy for full-body human motion and mesh-level object trajectories.

## 关键点

- **问题**：However, existing embodied datasets remain fundamentally limited: internet-scale video data lack precise physical states and interaction grounding, while laboratory motion datasets provide high fidelity but only narrow behavioral coverage.
- **创新点 / 方法**：We present HiPHI, a 600+ hour scale high-fidelity whole-body human motion dataset designed to systematically maximize coverage of the human motion and interaction manifold.
- **证据**：Created using an optical motion capture pipeline, HiPHI provides sub-millimeter spatial marker tracking accuracy for full-body human motion and mesh-level object trajectories.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/HiPHI A Large-Scale Benchmark for High-Precision Human Motion and Object-Interac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid intelligence requires learning over an extremely diverse space of whole-body motions and physically grounded interactions. However, existing embodied datasets remain fundamentally limited: internet-scale video data lack precise physical states and interaction grounding, while laboratory motion datasets provide high fidelity but only narrow behavioral coverage. This mismatch creates a critical bottleneck for scalable humanoid policy learning. We present HiPHI, a 600+ hour scale high-fidelity whole-body human motion dataset designed to systematically maximize coverage of the human motion and interaction manifold. HiPHI is theoretically guided by FrameNet, a linguistic framework organizing human primitives. Created using an optical motion capture pipeline, HiPHI provides sub-millimeter spatial marker tracking accuracy for full-body human motion and mesh-level object trajectories. We further introduce a benchmark suite evaluating motion-space diversity, interaction grounding, object consistency, and physical AI applications. Our analyses demonstrate that HiPHI significantly expands motion coverage compared to existing motion datasets while maintaining high-fidelity interaction quality, and establishes a scalable data foundation for training, evaluating, and generalizing humanoid policies in real-world embodied tasks, where similar extensions are also applicable to motion prior models in computer graphics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16222v1
- Authors: Jiahao Ji, Ji Ma, Runhan Zhang, Runyi Yu, Wenjia Wang, Weiheng Chi, Qianqian Peng, Weichao Yan, Yongfei Gu, Ye Tian, Ting Wu, Longwei Li, Chun Yuan, Ruoli Dai, Lei Han
- Published: 2026-08-17T07:54:26Z
- Age days: 1

</details>
