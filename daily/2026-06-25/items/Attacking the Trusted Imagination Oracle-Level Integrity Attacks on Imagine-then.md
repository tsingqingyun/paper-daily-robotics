---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22966v1"
published: "2026-06-22T07:45:34Z"
age_days: 2
score: 30
created: 2026-06-25
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models

> [!summary] 一句话结论（基于摘要）
> Many recent vision-language-action (VLA) policies adopt an imagine-then-act design.

## 关键点

- **问题**：Targeted control remains bounded.
- **创新点 / 方法**：Many recent vision-language-action (VLA) policies adopt an imagine-then-act design.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：The robustness of the policy therefore does not entail the robustness of systems that rely on the WAM.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/Attacking the Trusted Imagination Oracle-Level Integrity Attacks on Imagine-then.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Many recent vision-language-action (VLA) policies adopt an imagine-then-act design. A
world-action model (WAM) first imagines a short future as a latent trajectory z~, on
which the action is then conditioned. We identify this trusted imagination, rather than
the reactive policy, as the exposed attack surface. A downstream oracle, such as a
safety gate, a visual model-predictive-control (MPC) planner, or an imagine-then-check
verifier, consumes z~ as a prediction of the future. The robustness of the policy
therefore does not entail the robustness of systems that rely on the WAM. The underlying
phenomenon is an asymmetry. Corrupting the imagination is easy, since it requires only
displacing z~ from its natural-future manifold. Steering it precisely is hard, since it
must reach a specified on-manifold target. We adopt a capability-based threat model with
an L-infinity-bounded observation perturbation. The attacker applies projected gradient
descent through the fully differentiable observation-to-imagination map. The same off-
manifold property motivates a parameter-free denoiser detector. We evaluate three
targets: RynnVLA-002, LingBot-VA, and LaDi-WM. Untargeted corruption is roughly 60x
stronger than random and is detected at AUC 1.0. Targeted control remains bounded. An
adaptive attacker evades detection only by forgoing corruption. The reactive policy
remains robust to corrupted imagination. A native imagination-driven MPC, however,
exhibits the first adversary-specific task failure (at epsilon=0.01, success 0.70 versus
0.05; Fisher p < 10^-4).

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22966v1
- Authors: Linghan Chen, Kaiyan Ji, Minyu Guo
- Published: 2026-06-22T07:45:34Z
- Age days: 2

</details>
